Recent Revisions to This Document {#template-doc-rev}
=====================================================

23.01
-----

General update
:
This revision contains only editorial changes and no technical updates.

21.05
-----

General update
:
This revision contains only editorial changes and no technical updates.

21.04
-----

Payer Authentication Fields
:
The following card types have been added:

    * Secure transaction in France
    * Elo Compra Segura
    * UnionPay 3D Secure

21.03
-----

Product Names
:
Product names were updated throughout the document.

Card Processing Fields
:
The information in [Card Processing Templates](/docs/gateway/en-us/boarding-template-management/user/all/ada/boarding-template-mgmt/templates-matrix-intro/templates-matrix-card.md "") has been updated. This section now describes some processor-specific fields. For all card-processing template fields, see the *API Field Reference Guide*.

Payer Authentication Fields
:
The following card types have been updated in [Payer Authentication Templates](/docs/gateway/en-us/boarding-template-management/user/all/ada/boarding-template-mgmt/templates-matrix-intro/templates-matrix-pa.md ""), and configuration information has been updated:

    * Verified by Relay is now Relay Secure
    * Mastercard SecureCode is now Mastercard Identity Check
    * AMEX SafeKey is now American Express SafeKey
    * JCB Secure is now JCB J/Secure
    * Diners Club Protect Buy is now Discover / Diners Club ProtectBuy

About This Guide {#templates-about-guide}
=========================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
--------------------

This guide is for administrators who board merchants using the `Payment Gateway` `Business Center` and developers who integrate the `Payment Gateway` API into their system.

Conventions
-----------

The following special statements are used in this document:

> IMPORTANT
> An *Important* statement contains information essential to successfully completing a task or learning a concept.
> WARNING
> A *Warning* contains information or instructions, which, if not heeded, can result in a security risk, irreversible loss of data, or significant cost in time or revenue or both.

Customer Support
----------------

For support information about any service, visit the Support Center:  
<http://support.example.com>

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Payment Gateway for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Payment Gateway.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE CARD PLATFORM CONNECT ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT CARD PLATFORM CONNECT ACQUIRER.

Boarding Templates {#templates-about}
=====================================

Partners can use various boarding templates to customize merchant onboarding and meet the business needs of each merchant.  
A boarding template is a collection of predefined attributes and rules that an acquirer (bank), technical partner, or merchant uses to board merchants onto their platform. Boarding templates help automate the entire boarding process by packaging all of the required information needed to board merchants. You can use templates to reduce the manual steps and time it takes for merchant accounts to start processing payments.  
Templates also allow an acquirer or partner to make configuration changes to individual and multiple merchants in the portfolio.  
You can use a boarding template to initialize or make changes to any of the following:

* Accounts
* Transacting nodes
* Structural nodes

Template Components {#templates-components}
===========================================

The boarding template combines these essential components:

* **Products and Product Bundles**  
  Partners can offer a list of products and product bundles to merchants. All products and bundles are available in a partner's catalog.
* **Billing Template**  
  A combination of BUY and SELL rates that is associated with a product (or product bundle). A billing template is required for products sold by OBO partners. Non-OBO partners can choose to set a value on billing templates for tracking purposes.
* **Product Configuration Templates**  
  A collection of pre-configured product settings that partners can use for boarding activities. When applied along with a merchant-specific configuration, the product is fully enabled for the merchant.
* **Boarding Workflow**  
  A boarding workflow is a sequence of steps controlled by partner-specific business rules to board merchants.
* **Additional Metadata**  
  These include mandatory, optional, and self-provisioned products, token IDs, and other attributes.

Products {#templates-products}
==============================

You can use boarding templates to configure these products in merchant accounts.
* Account Updater
* Card Processing
* Echeck/ACH
* `Fraud Management Essentials`
* Gift Cards
* Payer Authentication
* `Secure Acceptance`
* `Token Management Service`
* Virtual Terminal

Using Templates {#templates-tasks}
==================================

This section describes the template tasks you can perform.

Retrieving Templates {#templates-retrieving}
============================================

You can retrieve merchant boarding templates for a specified product. The default template is the first template listed when you retrieve a template.  
To retrieve merchant boarding templates:

1. In the `Business Center`, go to the left navigation panel and choose Portfolio Management \&gt; Portfolio Tools \&gt; Template Management.

2. Go to the Applied Filters section and choose a product from the drop-down list.

3. Click **Search** to filter the results by product.

   #### ADDITIONAL INFORMATION

   If templates are available for the product, the message *Templates Have Been Retrieved* appears at the top of the screen. The message *Unable to Retrieve Templates At This Time* appears if templates are unavailable or do not exist.

4. You can sort the filtered results by the column headings. The default template is the first template in the results list.

5. Click a template's name link to open an individual template.

Add Templates {#templates-adding}
=================================

You can add a template containing configured fields for easy first-time account initialization.  
Follow these steps to add a product template for a merchant account:

1. In the `Business Center`, go to the left navigation panel and choose Portfolio Management \&gt; Portfolio Tools \&gt; Template Management.
2. Click Add new template \| +.
3. On the Template Details page, select a product from the drop-down menu.
4. Click Apply selected product.
5. Enter a name and description.
6. Set the template as your default template for that product (optional).
7. Click Next.
8. Set the configuration options for the selected template. See [Product Boarding Template Reference](/docs/gateway/en-us/boarding-template-management/user/all/ada/boarding-template-mgmt/templates-matrix-intro.md "") for individual template options.
9. Some templates with multiple tabs require you to click Save before moving to the next configuration tab. If you navigate away before saving, your settings will be lost.
10. When you have configured all the tabs for the product, click Submit. The new template appears in the list of product templates.

Editing Templates {#templates-editing}
======================================

You can update a template as necessary.  
To update a boarding template for a merchant account:

1. Follow the steps to [retrieve a template](/docs/gateway/en-us/boarding-template-management/user/all/ada/boarding-template-mgmt/templates-tasks/templates-retrieving.md "").
2. Next to the template you want to modify, click the **Edit** icon.
3. Edit the existing template.
4. Click **Save**.

Deleting Templates {#templates-deleting}
========================================

When a template is no longer used, you can delete it.  
To delete a boarding template for a merchant account:

1. In the `Business Center`, go to the left navigation panel and choose Portfolio Management \&gt; Portfolio Tools \&gt; Template Management.
2. Follow the steps to [retrieve a template](/docs/gateway/en-us/boarding-template-management/user/all/ada/boarding-template-mgmt/templates-tasks/templates-retrieving.md "").
3. Next to the template you want to delete, click the **Delete** icon.

Setting the Default Template {#templates-default}
=================================================

You can set any template as the default. The default template is the first template listed when you retrieve a template.  
To set a template as default:

1. In the `Business Center`, go to the left navigation panel and choose Portfolio Management \&gt; Portfolio Tools \&gt; Template Management.
2. Follow the steps to [retrieve a template](/docs/gateway/en-us/boarding-template-management/user/all/ada/boarding-template-mgmt/templates-tasks/templates-retrieving.md "").
3. Next to the template you want to modify, click the **Make Default (...)** icon.

Product Boarding Template Reference {#templates-matrix-intro}
=============================================================

Use this information as a guide to configure the boarding templates. We update this reference as existing templates are updated and new templates are added.

Account Updater Templates {#templates-matrix-au}
================================================

Select configuration options for these fields:

| Field                           | Option 1         | Option 2        | Option 3        | Option 4 | Option 5 | Option 6 |
|:--------------------------------|:-----------------|:----------------|:----------------|:---------|:---------|:---------|
| Relay/Mastercard Mode            | Pan Upload       | Token API       | Monthly Harvest |          |          |          |
| AMEX Mode                       | Token API        | Monthly Harvest |                 |          |          |          |
| Request Updates from AMEX       | Yes              | No              |                 |          |          |          |
| AMEX SE Number                  | INPUT SE #       |                 |                 |          |          |          |
| AMEX Subscriber ID              | INPUT ID #       |                 |                 |          |          |          |
| Request Updates from Mastercard | Yes              | No              |                 |          |          |          |
| Mastercard ICA Number           | 10426            | 10427           | 1835            | 1836     | 4845     | 8773     |
| Mastercard Merchant ID          | INPUT MID #      |                 |                 |          |          |          |
| Request Updates from Relay       | Yes              | No              |                 |          |          |          |
| CARD Segment ID                 | 0040             | 0043            | 0044            | 0048     | 0057     | 0088     |
| CARD Merchant ID                | INPUT Relay MID # |                 |                 |          |          |          |
[Account Updater Template Configuration Options]

Card Processing Templates {#templates-matrix-card}
==================================================

Create a card-processing template for each payment processor you use. Each card-processing template is specific to a single payment processor. Apply the appropriate template when you are boarding new merchants.

Configuring a Card Processing Template {#templates-matrix-card-config}
======================================================================

Follow these steps to configure a template for card processing:

1. In the `Business Center`, go to the left navigation panel and choose Portfolio Management \&gt; Portfolio Tools \&gt; Template Management.
2. Click **Add New Template**.
3. Select **Card Processing** from the drop-down menu.
4. Click **Apply selected product**.
5. Enter a unique name for the new card-processing template, and then click **Next**.
6. Select the type of card processing: Card Present, Card Not Present, or Both.
7. Click the **Processor** field, and then choose the payment processor name.
8. If an Acceptance Type field appears, click the field, and then choose the acceptance type.
9. In the processor tab (labeled with the name of the processor you selected), configure the required and optional fields available for the selected payment processor.
10. In the Common Settings tab, you can configure fields that are common for the merchant but that could potentially be used across multiple payment processors.

Processor-Specific Fields {#templates-matrix-card-fields}
=========================================================

These processor-specific fields are frequently configured in a card-processing template. For more information about these and other fields in the template, see the [*API Field Reference Guide*](https://docs.example.com/en/reference/api-fields.md "").

Accepted Currencies
:
Select all of the currencies that the merchant accepts. The currencies listed in this field depend on the payment processor selected.

    As an example, if you are creating a card-processing template for the TSYS/Vital processor, the list of accepted currencies is as follows:

    * CAD (Canadian Dollar)
    * USD (US Dollar)


    For more information about currency codes, see [*ISO Standard Currency Codes*](https://developer.example.com/library/documentation/sbc/quickref/currencies.pdf "").

Accepted Payment Types
:
Select all of the card types that the merchant accepts. The card types listed in this field depend on the payment processor selected.

    Depending on your payment processor, these are some of the card types you can expect to see listed:

    * Relay
    * Mastercard
    * American Express
    * Diners Club


    For more information about the specific card types that your processor supports, log in to the `Business Center` and go to **Template Management for Card Processing**.

Batch Group
:
The Batch Group groups all of the capture (bill and credit) requests into a batch bound for your payment processor.

    Choose the batch group for processing capture requests.

    The name of a batch group identifies the time of day that capture requests are grouped into a batch and sent to your payment processor. The last two digits of the batch group name identify the hour (in 24-hour time) of the processor cutoff time for that batch group.

    As an example, if you are creating a card processing template for the American Express Direct processor, the list of batch group names you can select includes the following:

    * amexdirect_2 (processor cutoff time is 2:00 a.m. PST daily)
    * amexdirect_17 (processor cutoff time is 5:00 p.m. PST daily)
    * amexdirect_21 (processor cutoff time is 9:00 p.m. PST daily)


    > IMPORTANT Processor cutoff times identified in the batch group names are in Pacific Standard Time (PST).

Merchant ID
:
Enter the merchant's acquirer processing ID assigned by the acquiring bank.
:
Note that it is unlikely that you would specify this field in a card-processing template. Typically, the merchant ID is merchant specific. Also, many merchants have more than one merchant ID to support processing in multiple currencies or to process both card present (in store) transactions and card-not-present (e-commerce) transactions.

Terminal ID
:
Enter the terminal ID assigned by the acquirer or the processor. This value should not be overridden by any other party.
:
Enter the merchant's processing terminal ID assigned by the acquiring bank or payment processor.
:
Note that it is unlikely that you would specify this field in a card-processing template. Typically, the terminal ID is merchant specific. Also, many merchants have more than one terminal ID to support processing in multiple currencies or to process both card-present (in store) transactions and card-not-present (e-commerce) transactions.

Customer Invoicing {#templates-matrix-customer-invoicing}
=========================================================

Customer Invoicing allows merchants to create and manage invoices, send customers links to invoices, securely collect payments for invoices.

Prerequisites
-------------

`Unified Checkout` must be enabled for the merchant. Before `Unified Checkout` can be enabled for a merchant, it must be enabled at the portfolio level.  
To enable `Unified Checkout` at the portfolio level, talk to your sales representative.  
Customer Invoicing must be enabled at the portfolio level before in can be added to merchant accounts. To enable at Customer Invoicing at the portfolio level, contact your sales representative.

Enabling Customer Invoicing on the Business Center
--------------------------------------------------

Before you can add Customer Invoicing, Unified Checkout must be added to the merchant account. To add Unified Checkout, see: [Unified Checkout](/docs/gateway/en-us/boarding-template-management/user/all/ada/boarding-template-mgmt/templates-matrix-intro/templates-matrix-unified-checkout.md "").

1. Navigate to the Merchant Details Page within Portfolio Management.
2. Click the Add products button.
3. Select Customer Invoicing, and click the Add button.

Customer Invoicing should appear on the Merchant's product list.

ACH Templates {#templates-matrix-echeck}
========================================

Select configuration options for these fields:

| Field                       | Value or Option                                                                                                                                                                                                   |
|:----------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| echeck Processor            | Bofa ACH                                                                                                                                                                                                          |
| Batch Group                 | Select a batch group. Batch time is identified by the last two digits in military time. Example: *\&lt;processor\&gt;_16* means the cut-off time is 4:00 p.m. PST. Convert the time to your local time as needed. |
| Auto Set to Completed State | Select **Yes** to automatically update transactions to "Completed" status a number of days after the transaction is processed.                                                                                    |
| Company ID                  | Merchant's ID assigned by the acquiring bank.                                                                                                                                                                     |
| ACH Entry Description       | Merchant-defined description. Example: Payroll, Gas Bill, Insurance Premium.                                                                                                                                      |
[ACH Template Configuration Options]

`Fraud Management Essentials` Templates {#templates-matrix-fme}
===============================================================

1. On the General Settings page, select options for each of the following:

   | Section Name       | Field Name             | Available Options / Details                                                                                                              |
   |:-------------------|:-----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
   | Payment Processing | Settlement             | Disable Settlement Enable Settlement Enable with settlement selected by default                                                          |
   | Decision Reject    | Authorization Reversal | Disable authorization reversal option Enable authorization reversal option Enable with authorization reversal option selected by default |
   | Local Currency     | Local Currency         | Select the local currency from the list.                                                                                                 |
   [`Fraud Management Essentials` Template General Settings Options]

2. On the Rule Configuration page, configure the options for each of the following:

   | Tab Name                             | Field Name                   | Available Options / Details                                                                                                                                     |
   |:-------------------------------------|:-----------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | Score Threshold                      | Score Threshold              | Score between 50-69 Score between 70-94 Score between 95-100 Each threshold has an enable/disable check box. Each score can be adjusted to user specifications. |
   | Standard Rules                       | AVS Mismatch                 | Monitor, Review, Reject, Disable                                                                                                                                |
   | Standard Rules                       | AVS Partial Match            | Monitor, Review, Reject, Disable                                                                                                                                |
   | Standard Rules                       | AVS Not Verifiable           | Monitor, Review, Reject, Disable                                                                                                                                |
   | Standard Rules                       | CVV Mismatch                 | Monitor, Review, Reject, Disable                                                                                                                                |
   | Standard Rules                       | CVV Not Verifiable           | Monitor, Review, Reject, Disable                                                                                                                                |
   | Standard Rules                       | Invalid Address              | Monitor, Review, Reject, Disable                                                                                                                                |
   | Standard Rules                       | Billing-Shipping Mismatch    | Monitor, Review, Reject, Disable                                                                                                                                |
   | Standard Rules                       | Billing-IP Mismatch          | Monitor, Review, Reject, Disable                                                                                                                                |
   | Standard Rules                       | Shipping-IP Country Mismatch | Monitor, Review, Reject, Disable                                                                                                                                |
   | Regional \& Country IP Address Rules | Decision                     | Review, Reject, Monitor                                                                                                                                         |
   | Regional \& Country IP Address Rules | Region                       | Regions include: Asia, Europe, Africa, Oceania, Central America/Caribbean, Arctic/Antarctica, South America, North America, Middle East                         |
   | Regional \& Country IP Address Rules | Countries                    | Check the **All** box for all countries in a region or select individually listed countries.                                                                    |
   | Velocity Rules                       | Decision                     | Monitor, Review, Reject                                                                                                                                         |
   | Velocity Rules                       | Field                        | Email, Total count, Device, Shipping Address, Account Number, IP Address                                                                                        |
   | Velocity Rules                       | Value                        | Input Value for Transactions in Field                                                                                                                           |
   | Velocity Rules                       | Time Range                   | Range of time the rule is valid for.                                                                                                                            |
   | Threshold Rules                      | Decision                     | Monitor, Review, Reject, Disable                                                                                                                                |
   | Threshold Rules                      | Rule - Min Order Amount      | Order Amount minimum amount                                                                                                                                     |
   | Threshold Rules                      | Value                        | Input order dollar amount                                                                                                                                       |
   | Threshold Rules                      | Decision                     | Monitor, Review, Reject, Disable                                                                                                                                |
   | Threshold Rules                      | Rule - Max Order Amount      | Order Amount Maximum amount                                                                                                                                     |
   | Threshold Rules                      | Value                        | Input order dollar amount                                                                                                                                       |
   [`Fraud Management Essentials` Template Rule Configuration Options]

{#templates-matrix-fme_ol_tll_tdj_1xb}

Gift Card Templates {#templates-matrix-gift-card}
=================================================

Select configuration options for these fields:

| Field                                                 | Value or Option                                                                                                     |
|:------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|
| Gift Card MID                                         | The Valuelink Gift card assigned merchant number which includes the plan, root, merchant location, and check digit. |
| Merchant SIC Code                                     | Merchant Category Code.                                                                                             |
| Merchant Store ID                                     | Store ID number.                                                                                                    |
| Enable PIN encryption?                                | Select **Yes** to encrypt the PIN before sending it to the processor.                                               |
| Enable Merchant defined Transaction Reference Number? | Select **Yes** to allow the merchant to define the transaction reference number. Otherwise, it is auto-generated.   |
[Gift Card Template Configuration Options]

Payer Authentication Templates {#templates-matrix-pa}
=====================================================

`Payer Authentication` templates specify the payer authentication services that a merchant account will accept. To specify a payer authentication service, enter the acquirer ID in the associated field. This template supports the following payer authentication services:

Relay Secure with EMV
:
The Relay card type uses Relay Secure with EMV as the authentication service. The acquirer ID is a text string that consists of 6 to 20 digits and starts with the number 4.

Mastercard/Meeza Identity Check
:
The Mastercard card type uses Mastercard Identity Check as the authentication service. The acquirer ID is a text string that consists of 6 to 20 digits and starts with the number 5 or 2.

American Express SafeKey
:
The American Express card type uses American Express SafeKey as the authentication service. The acquirer ID is a text string that consists of 11 to 20 digits and starts with the number 1.

Cartes Bancaires Fast'R
:
The Cartes Bancaires card type uses Fast'R as the authentication service. The acquirer ID is a text string that consists of 6 to 20 digits and starts with the number 4, 5, or 2.

Discover / Diners Club ProtectBuy
:
The Discover / Diners Club card type uses ProtectBuy as the authentication service. The acquirer ID is a text string that consists of 6 to 20 digits and starts with the number 3 or 6.

Elo Compra Segura
:
The Elo card type uses Elo Compra Segura as the authentication service. The acquirer ID is a text string that consists of 4 digits. The acquirer ID is a text string that consists of 8 digits and starts with the number 1.

JCB J/Secure
:
The JCB card type uses J/Secure as the authentication service.

UnionPay 3D Secure
:
3D Secure is a protocol designed to be an additional security layer for online credit and debit card transactions. The acquirer ID is a text string that consists of 6 to 20 digits and begins with the number 4, 5, 2, or 6.

Pay By Link {#templates-matrix-pay-by-link}
===========================================

`Pay by Link` provides merchants an easy and fast way to sell products or accept donations without any coding.

Prerequisites
-------------

`Unified Checkout` must be enabled for the merchant. Before `Unified Checkout` can be enabled for a merchant, it must be enabled at the portfolio level.  
To enable `Unified Checkout` at the portfolio level, talk to your sales representative.  
`Pay by Link` must be enabled at the portfolio level before in can be added to merchant accounts. To enable at `Pay by Link` the portfolio level, contact your sales representative.

Enabling `Pay by Link` on the Business Center
---------------------------------------------

Before you can add `Pay by Link`, Unified Checkout must be added to the merchant account. To add Unified Checkout, see: [Unified Checkout](/docs/gateway/en-us/boarding-template-management/user/all/ada/boarding-template-mgmt/templates-matrix-intro/templates-matrix-unified-checkout.md "").

1. Navigate to the Merchant Details Page within Portfolio Management.
2. Click the Add products button.
3. Select `Pay by Link`, and click the Add button.

`Pay by Link` should appear on the Merchant's product list.

`Secure Acceptance` Templates {#templates-matrix-sa}
====================================================

Complete the Template Details Page. This information is populated in the `Secure Acceptance` - General Settings tab:

| Fields               | Option 1                                             | Option 2                                                          | Option 3                                                  |
|:---------------------|:-----------------------------------------------------|:------------------------------------------------------------------|:----------------------------------------------------------|
| Integration Methods  | Select `Hosted Checkout Integration` or Checkout API | Input the Company Name, Contact Information (Name, Email, Phone). |                                                           |
| Added Value Services | Payment Tokenization                                 | `Decision Manager` Select Verbose Data                            | `Decision Manager` Select the Generate Fingerprint Device |
[`Secure Acceptance` Template General Settings Options]

Select these fields on the Configuration page:

| Configuration Tab | Option 1                                                                                 | Option 2                                                                                                                                                                | Option 3                                                                            | Option 4                                                                              | Option 5                                                                       | Option 6                                                                      |
|:------------------|:-----------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| General Settings  | Profile Information                                                                      | Integration Methods                                                                                                                                                     | Contact Information                                                                 | Added Value Services                                                                  |                                                                                |                                                                               |
| Payment Settings  | Card Type Select Card Type(s). Search for Card Types using the **Add card type** button. | Payer Authentication 3DS Version Select **Payer Authentication Legacy flow (Supports 3DS 1.0)** or **Payer Authentication Cruise flow (Supports 3DS 1.0 and 3DS 2.x)**. | Automatic Authorization Reversal Select **Fails AVS Check** or **Fails CVN Check**. | Echeck Select **Enable Echeck Payments**.                                             | CVN Select **CVN Display** , **CVN Required** and/or **Payer Authentication**. | Currencies Select accepted currencies.                                        |
| Payment Form      | Payment Form Flow Select **Multi-Step** or **Single Page**.                              | Checkout Steps Input customer Billing, Shipping, and Payment Information.                                                                                               | Payment Information Select sensitive fields to mask.                                | Order Review Select to Display or to Edit Billing, Shipping, and Payment Information. |                                                                                |                                                                               |
| Notifications     | Merchant Notifications Input the Merchant's POST URL and Email.                          | Customer Notifications Select to send an Email Receipt to the Customer.                                                                                                 |                                                                                     |                                                                                       |                                                                                |                                                                               |
| Customer Response | Transaction Response Page Select the Host.                                               | Transaction Response Message Set the Decline Limit.                                                                                                                     | Custom Cancel Response Page Select the Host.                                        | Custom Redirect After Checkout Enter the URL.                                         |                                                                                |                                                                               |
| Branding          | Header Content Select the Display Header, color, logo, and placement.                    | Main Body Select Colors, Type Face.                                                                                                                                     | Total Amount Select the Colors.                                                     | Progress Bar Select the Colors.                                                       | Pay/Finish Button Select the Colors.                                           | Footer Content Select Display Footer and add the image, color, and placement. |
[`Secure Acceptance` Template Configuration Options]

`Token Management Service` Templates {#templates-matrix-tms}
============================================================

Select payment method and service configuration options for these fields:

| Fields                               | Option 1                                                                                                                                                                                    | Option 2                                                                                                                                                            | Option 3                                                         |
|:-------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------|
| Supported Payment Methods            | Card                                                                                                                                                                                        | Echeck                                                                                                                                                              |                                                                  |
| Tokens: Token Types                  | Customers                                                                                                                                                                                   | Payment Instrument                                                                                                                                                  | Instrument Identifier                                            |
|                                      | Click check box; then select from the following formats: - 32-character Hex - 22 Digits - 19 Digits Luhn Check Passing - 16 Digits Luhn Check Passing                                       | Click check box; then select from the following formats: - 32-character Hex - 22 Digits - 19 Digits Luhn Check Passing - 16 Digits Luhn Check Passing               | Format - Card, echeck (ACH) Formats default to 32 Character Hex. |
| Card Number Masking Format           | Select either First 6 digits OR Last 4 returned clear                                                                                                                                       | Select either First 6 digits OR Last 4 returned clear                                                                                                               |                                                                  |
| Enable Network Tokenization Services | CARD (Enable/Disable\*) Disabling this option requires the following information for authorization: - TRID, Client ID - API KEY, Post Back API Key - Shared Secret, Post Back Shared Secret | Mastercard (Required) Disabling this option requires the following information for authorization: - Enable Transactions with Mastercard Network Tokens - Enter TRID |                                                                  |
| Push Notification Webhook            | Add Test URL if using Webhook for push notifications.                                                                                                                                       | Push notifications sent when there are updates to tokenized cards, (new card numbers, new expiration date, account closures).                                       |                                                                  |
[`Token Management Service` Template Configuration Options]

`Unified Checkout` {#templates-matrix-unified-checkout}
=======================================================

`Unified Checkout` allows merchants to accept many different digital payment types using a single interface.

Prerequisites
-------------

`Unified Checkout` must be enabled at the portfolio level before in can be added to merchant accounts. To enable at the `Unified Checkout` at the portfolio level, contact your sales representative.

Enabling `Unified Checkout` on the Business Center
--------------------------------------------------

1. Navigate to the Merchant Details Page within Portfolio Management.
2. Click the Add products button.
3. Select Unified Checkout, and click the Add button.

`Unified Checkout` should appear on the Merchant's product list.

Virtual Terminal Templates {#templates-matrix-vt}
=================================================

Select configuration options for these fields:

> IMPORTANT Virtual Terminal selections also apply to One-Time Payments.

| Fields                            | Option 1         | Option 2                                                      | Option 3 |
|:----------------------------------|:-----------------|:--------------------------------------------------------------|:---------|
| Default Transaction Type          | Card Not Present | Card Present                                                  |          |
| Acceptance Type                   | Card Not Present | Card Present                                                  | Both     |
| Merchants Edit Template?          | YES              | NO                                                            |          |
| Add Check Related Fields?         | YES              | NO Selecting **No** does not disable echeck/ACH transactions. |          |
| Add Merchant Defined Data Fields? | YES              | NO                                                            |          |
| Add EMV Fields?                   | YES              | NO                                                            |          |
| Add Level 3 Fields?               | YES              | NO                                                            |          |
| Add Service Fee Fields?           | YES              | NO                                                            |          |
[Virtual Terminal Template Configuration Options]

