Merchant Boarding {#boarding-about-guide}
=========================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This guide is for developers who integrate the `Cybersource` `REST API` into their system and use the `REST API` to board merchants.

Conventions
:
The following special statement appears in this document:

    > IMPORTANT
    > An *Important* statement contains information essential to successfully completing a task or learning a concept.

Related Documentation
:
Refer to the Technical Documentation Hub in the `Cybersource` Developer Center for additional technical documentation:

    [https://developer.cybersource.com/docs.html](https://developer.cybersource.com/docs.md "")

Customer Support
:
For support information about any service, visit the Support Center:

<http://support.cybersource.com>

Recent Revisions to This Document {#boarding-revisions}
=======================================================

25.05.01
--------

Organization ID
:
Added note about Organization ID security check for sensitive information. See [Understanding Organization IDs](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro-overview/boarding-intro-ids.md "").

25.04.01
--------

Board Status, Test Values
:
Added board status and test values for Payer Authentication. See [Payer Authentication](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-products-intro/boarding-payer-auth.md ""), [Required Fields for Enabling Payer Authentication](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-products-intro/boarding-payer-auth/boarding-payer-auth-enable-intro/boarding-payer-auth-enable-reqfields.md ""), and [Required Fields for Configuring Payer Authentication Using the PECS API](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-products/boarding-pecs-payer-auth/pecs-config-payerauth/pecs-config-payerauth-req-fields.md "").
:
Updated section titles.

24.05
-----

Product Enablement and Configuration
:
Updated the REST example for enabling the `Token Management Service` and enrolling in network tokenization. See [Enable TMS and Enroll in Network Tokenization for a New Merchant](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-products-intro/boarding-tms/boarding-tms-enable-net-tkn-intro.md "").

24.04
-----

This revision contains only editorial changes and no technical updates.

24.03
-----

Product Enablement and Configuration
:
Added support for the `Token Management Service`. See [`Token Management Service` for the BRS API](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-products-intro/boarding-tms.md "") and [`Token Management Service` for the PECS API](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-products/boarding-pecs-tms.md "").
:
Updated the required fields for enabling Payer Authentication using the BRS and PECS APIs. See [Required Fields for Enabling Payer Authentication](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-products-intro/boarding-payer-auth/boarding-payer-auth-enable-intro/boarding-payer-auth-enable-reqfields.md "") and [Required Fields for Configuring Payer Authentication Using the PECS API](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-products/boarding-pecs-payer-auth/pecs-config-payerauth/pecs-config-payerauth-req-fields.md "").

Organization Management
:
Added an example for creating a transacting organization with integration information. See [REST Example: Creating a Transacting Organization](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-reg-intro/boarding-reg-create-transacting-api/boarding-reg-create-transacting-api-example.md "").

24.02
-----

Updated product template information. See [Product Templates](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro-template.md "").

24.01
-----

Initial release.

VISA Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Visa Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Visa/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER VISA NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE VISA PLATFORM CONNECT ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER VISA NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT VISA PLATFORM CONNECT ACQUIRER.

Introduction to the Boarding Registration Service {#boarding-intro-overview}
============================================================================

Boarding Registration streamlines and automates the boarding of merchant accounts using the `Cybersource` `REST API`. You can create a simple or complex hierarchy of accounts that represents merchant business units, and configure payment products for those accounts. To understand accounts, organizations, their hierarchy, and status, see these topics:

* [Understanding Accounts and Organizations](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro-overview/boarding-intro-organizations.md "")
* [Extending the Hierarchy](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-extend-hierarchy.md "")

Requirements {#boarding-intro-requirements}
===========================================

Before boarding organizations, you must complete these requirements:

* You must have a portfolio account on our platform. Contact your representative to have a portfolio account set up for you.
* Set up users, roles, and permissions. You must have at least one administrator account.

Understanding Accounts and Organizations {#boarding-intro-organizations}
========================================================================

You are assigned a **portfolio** account when you sign up. All merchant accounts are subordinate to the portfolio account. A merchant account consists of a **merchant** organization and its subordinate organizations, which always includes at least one **transacting** organization. You can use **structural** organizations to extend the hierarchy of merchant accounts.

* The **portfolio** account is always the top node in the hierarchy.

* A **merchant** organization represents a business entity. For example, a brand or company. There can only be one merchant in any branch of the hierarchy.

* A **transacting** organization represents an entity that processes payment transactions. For example, a physical store or a payment form on a web page or app. No other organization can be directly subordinate to a transacting organization.

* A **structural** organization represents a conceptual entity that enables you to build an expansive hierarchy between merchant and transacting nodes. For more information on using structural organizations to extend the hierarchy, see [Extending the Hierarchy](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-extend-hierarchy.md "").
  The image below shows a simple merchant account. The merchant organization is directly beneath the portfolio organization, and contains one transacting organization.

  #### Figure: {#boarding-intro-organizations_fig_cnv_xgj_cfc}

  Sample Merchant Account ![](/content/dam/new-documentation/documentation/en-us/topics/platform/bam/boarding-user/images/create-merchant-account.svg/jcr:content/renditions/original)
  {#boarding-intro-organizations_ul_e22_mgl_g5b}

Understanding Organization IDs {#boarding-intro-ids}
====================================================

Organizations relate to each other using IDs. Every organization is assigned an organization ID. When an organization has a subordinate, it is assigned a child ID that identifies the subordinate. The subordinate is assigned a parent ID that identifies the parent organization. Organization IDs must be unique, not just within the portfolio or account, but across the system.
In the illustration below, merchant's ID is `Merchant Account 1`. The merchant's child IDs are `Transacting MID1` and `Transacting MID2`. The merchant's parent ID is `Portfolio`.

#### Figure: {#boarding-intro-ids_fig_ut4_p5f_q5b}

Understanding Organization IDs ![](/content/dam/new-documentation/documentation/en-us/topics/platform/bam/boarding/images/create-merchant-account-new-transacting.svg/jcr:content/renditions/original)
IMPORTANT Do not include sensitive information in the Org ID field. A security validation check is in place to ensure that the unique Org ID field (e.g., Cybersource MID) does not contain PAN or other sensitive information to provide an additional layer of protection for your data during the onboarding process.

Configure a Single Merchant {#boarding-intro-workflow-single-mid}
=================================================================

#### Figure:

Merchant Boarding with a Single MID ![](/content/dam/new-documentation/documentation/en-us/topics/platform/bam/boarding-user/images/merchant-boarding-workflow-single-mid.svg/jcr:content/renditions/original)
Follow these steps to configure a merchant hierarchy with a single merchant:
1. Contact your representative to have a portfolio account set up for you.
2. Configure product templates. See [Product Templates](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro-template.md "").
3. Create a merchant organization. See [Create a Merchant Organization](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-reg-intro/boarding-reg-create-merch-api.md "").
4. Set up your transacting organization and products. See [Add a Transacting Organization to an Existing Organization](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-reg-intro/boarding-reg-create-transacting-api.md "").
5. Configure products. See [Product Enablement and Configuration Using the PECS API](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-products.md "").

Configure Multiple Merchants {#boarding-intro-workflow-multi-mid}
=================================================================

#### Figure:

Merchant Boarding with Multiple MIDs ![](/content/dam/new-documentation/documentation/en-us/topics/platform/bam/boarding-user/images/merchant-boarding-workflow-multi-mid.svg/jcr:content/renditions/original)
Follow these steps to configure a merchant hierarchy with multiple merchants:
1. Create a merchant organization. See [Create a Merchant Organization](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-reg-intro/boarding-reg-create-merch-api.md "").
2. Configure product templates. See [Product Templates](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro-template.md "").
3. Set up your transacting organization and products. See [Add a Transacting Organization to an Existing Organization](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-reg-intro/boarding-reg-create-transacting-api.md "").
4. Extend the hierarchy. See [Add a Structural Organization to a Merchant Organization](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-extend-hierarchy/boarding-reg-create-structural-api.md "").
5. Configure products. See [Product Enablement and Configuration Using the PECS API](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-products.md "").
6. Contact your representative to have a portfolio account set up for you.
7. Configure product templates. See [Product Templates](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro-template.md "").
8. Create a merchant organization. See [Create a Merchant Organization](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-reg-intro/boarding-reg-create-merch-api.md "").
9. Set up your transacting organization and products. See [Add a Transacting Organization to an Existing Organization](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-reg-intro/boarding-reg-create-transacting-api.md "").
10. Configure products. See [Product Enablement and Configuration Using the PECS API](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-products.md "").

Configure Multiple Merchants with an Extended Hierarchy {#boarding-intro-workflow-extend-multi-mid}
===================================================================================================

#### Figure:

Merchant Boarding with Multiple MIDs and Extended Hierarchy ![](/content/dam/new-documentation/documentation/en-us/topics/platform/bam/boarding-user/images/merchant-boarding-workflow-extend-multi-mid.svg/jcr:content/renditions/original)
Follow these steps to configure a merchant hierarchy with multiple merchants and structural organizations:
1. Contact your representative to have a portfolio account set up for you.
2. Configure product templates. See [Product Templates](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro-template.md "").
3. Create a merchant organization. See [Create a Merchant Organization](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-reg-intro/boarding-reg-create-merch-api.md "").
4. Extend the hierarchy. See [Add a Structural Organization to a Merchant Organization](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-extend-hierarchy/boarding-reg-create-structural-api.md "").
5. Set up your transacting organization and products. See [Add a Transacting Organization to an Existing Organization](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-reg-intro/boarding-reg-create-transacting-api.md "").
6. Configure products. See [Product Enablement and Configuration Using the PECS API](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-products.md "").

Product Templates {#boarding-intro-template}
============================================

A product template enables and configures a product and is applied to more transacting organizations. Product templates are created in the `Business Center` by an administrator user. Before you board a transacting organization, you must create a product template for each product that you will assign to it. Not every product support templates.
You will apply product templates to a transacting organization when you create it. You can also create multiple templates for a product, configured differently, and decide which one to apply to a transacting organization, depending on the organization's needs.
Templates can be modified at any time; however, organizations that already have the template applied do not inherit the modifications. Modifying a template only affects new organizations that you apply to it.
For product-level boarding information, see the [Product Boarding Template Reference](/docs/cybs/en-us/boarding/developer/all/rest/boarding/templates-matrix-intro.md "").
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

IMPORTANT You can see templates only for enabled products on your account.

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
8. Set the configuration options for the selected template. See [Product Boarding Template Reference](/docs/cybs/en-us/boarding/developer/all/rest/boarding/templates-matrix-intro.md "") for individual template options.
9. Some templates with multiple tabs require you to click Save before moving to the next configuration tab. If you navigate away before saving, your settings will be lost.
10. When you have configured all the tabs for the product, click Submit. The new template appears in the list of product templates.

Editing Templates {#templates-editing}
======================================

You can update a template as necessary.
To update a boarding template for a merchant account:

1. Follow the steps to [retrieve a template](/docs/cybs/en-us/boarding/developer/all/rest/boarding/templates-tasks/templates-retrieving.md "").
2. Next to the template you want to modify, click the **Edit** icon.
3. Edit the existing template.
4. Click **Save**.

Deleting Templates {#templates-deleting}
========================================

When a template is no longer used, you can delete it.
To delete a boarding template for a merchant account:

1. In the `Business Center`, go to the left navigation panel and choose Portfolio Management \&gt; Portfolio Tools \&gt; Template Management.
2. Follow the steps to [retrieve a template](/docs/cybs/en-us/boarding/developer/all/rest/boarding/templates-tasks/templates-retrieving.md "").
3. Next to the template you want to delete, click the **Delete** icon.

Setting the Default Template {#templates-default}
=================================================

You can set any template as the default. The default template is the first template listed when you retrieve a template.
To set a template as default:

1. In the `Business Center`, go to the left navigation panel and choose Portfolio Management \&gt; Portfolio Tools \&gt; Template Management.
2. Follow the steps to [retrieve a template](/docs/cybs/en-us/boarding/developer/all/rest/boarding/templates-tasks/templates-retrieving.md "").
3. Next to the template you want to modify, click the **Make Default (...)** icon.

Product Boarding Template Reference {#templates-matrix-intro}
=============================================================

Use this information as a guide to configure the boarding templates. We update this reference as existing templates are updated and new templates are added.

Account Updater Templates {#templates-matrix-au}
================================================

Select configuration options for these fields:

| Field                           | Option 1         | Option 2        | Option 3        | Option 4 | Option 5 | Option 6 |
|:--------------------------------|:-----------------|:----------------|:----------------|:---------|:---------|:---------|
| Visa/Mastercard Mode            | Pan Upload       | Token API       | Monthly Harvest |          |          |          |
| AMEX Mode                       | Token API        | Monthly Harvest |                 |          |          |          |
| Request Updates from AMEX       | Yes              | No              |                 |          |          |          |
| AMEX SE Number                  | INPUT SE #       |                 |                 |          |          |          |
| AMEX Subscriber ID              | INPUT ID #       |                 |                 |          |          |          |
| Request Updates from Mastercard | Yes              | No              |                 |          |          |          |
| Mastercard ICA Number           | 10426            | 10427           | 1835            | 1836     | 4845     | 8773     |
| Mastercard Merchant ID          | INPUT MID #      |                 |                 |          |          |          |
| Request Updates from Visa       | Yes              | No              |                 |          |          |          |
| VISA Segment ID                 | 0040             | 0043            | 0044            | 0048     | 0057     | 0088     |
| VISA Merchant ID                | INPUT Visa MID # |                 |                 |          |          |          |
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

These processor-specific fields are frequently configured in a card-processing template. For more information about these and other fields in the template, see the [*API Field Reference Guide*](https://docs.cybersource.com/en/reference/api-fields.md "").

Accepted Currencies
:
Select all of the currencies that the merchant accepts. The currencies listed in this field depend on the payment processor selected.

    As an example, if you are creating a card-processing template for the TSYS/Vital processor, the list of accepted currencies is as follows:

    * CAD (Canadian Dollar)
    * USD (US Dollar)


    For more information about currency codes, see [*ISO Standard Currency Codes*](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf "").

Accepted Payment Types
:
Select all of the card types that the merchant accepts. The card types listed in this field depend on the payment processor selected.

    Depending on your payment processor, these are some of the card types you can expect to see listed:

    * Visa
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
When you attempt to enable `Pay by Link` without enabling `Unified Checkout`, the boarding calls will fail with the error `&lt;&gt;`.
To enable `Unified Checkout` at the portfolio level, talk to your sales representative.
Customer Invoicing must be enabled at the portfolio level before in can be added to merchant accounts. To enable at Customer Invoicing at the portfolio level, contact your sales representative.

Enabling Customer Invoicing on the Business Center
--------------------------------------------------

Before you can add Customer Invoicing, Unified Checkout must be added to the merchant account. To add Unified Checkout, see: [Unified Checkout](/docs/cybs/en-us/boarding/developer/all/rest/boarding/templates-matrix-intro/templates-matrix-unified-checkout.md "").

1. Navigate to the Merchant Details Page within Portfolio Management.
2. Click the Add products button.
3. Select Customer Invoicing, and click the Add button.

Customer Invoicing should appear on the Merchant's product list.

Enabling Customer Invoicing with the REST API
---------------------------------------------

To enable `Unified Checkout`:
Set the productInformation.selectedProducts.payments.customerInvoicing.subscriptionInformation.enabled field to `yes`
When enabling both Customer Invoicing and `Unified Checkout` at the same time, you can include both products in the same request.

REST Example: Enabling Customer Invoicing
-----------------------------------------

Production Endpoint: `POST ``https://api.cybersource.com``/boarding/v1/registrations`
Test Endpoint: `POST ``https://apitest.cybersource.com``/boarding/v1/registrations`

```
{
   "productInformation":{
      "selectedProducts":{
         "payments":{
            "unifiedCheckout":{
               "subscriptionInformation":{
                  "enabled":"true"
               }
            },
            "customerInvoicing":{
               "subscriptionInformation":{
                  "enabled":"true"
               }
            }
         }
      }
   }
}
```

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

Visa Secure with EMV
:
The Visa card type uses Visa Secure with EMV as the authentication service. The acquirer ID is a text string that consists of 6 to 20 digits and starts with the number 4.

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
When you attempt to enable `Pay by Link` without enabling `Unified Checkout`, the boarding calls will fail with the error `&lt;&gt;`.
To enable `Unified Checkout` at the portfolio level, talk to your sales representative.
`Pay by Link` must be enabled at the portfolio level before in can be added to merchant accounts. To enable at `Pay by Link` the portfolio level, contact your sales representative.

Enabling `Pay by Link` on the Business Center
---------------------------------------------

Before you can add `Pay by Link`, Unified Checkout must be added to the merchant account. To add Unified Checkout, see: [Unified Checkout](/docs/cybs/en-us/boarding/developer/all/rest/boarding/templates-matrix-intro/templates-matrix-unified-checkout.md "").

1. Navigate to the Merchant Details Page within Portfolio Management.
2. Click the Add products button.
3. Select `Pay by Link`, and click the Add button.

`Pay by Link` should appear on the Merchant's product list.

Enabling `Pay by Link` with the REST API
----------------------------------------

To enable `Unified Checkout`:
Set the productInformation.selectedProducts.payments.payByLink.subscriptionInformation.enabled field to `yes`
When enabling both `Pay by Link` and `Unified Checkout` at the same time, you can include both products in the same request.

REST Example: Enabling `Pay by Link`
------------------------------------

Production Endpoint: `POST ``https://api.cybersource.com``/boarding/v1/registrations`
Test Endpoint: `POST ``https://apitest.cybersource.com``/boarding/v1/registrations`

```
{
   "productInformation":{
      "selectedProducts":{
         "payments":{
            "unifiedCheckout":{
               "subscriptionInformation":{
                  "enabled":"true"
               }
            },
            "payByLink":{
               "subscriptionInformation":{
                  "enabled":"true"
               }
            }
         }
      }
   }
}
```

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
| Enable Network Tokenization Services | VISA (Enable/Disable\*) Disabling this option requires the following information for authorization: - TRID, Client ID - API KEY, Post Back API Key - Shared Secret, Post Back Shared Secret | Mastercard (Required) Disabling this option requires the following information for authorization: - Enable Transactions with Mastercard Network Tokens - Enter TRID |                                                                  |
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

Enabling `Unified Checkout` with the REST API
---------------------------------------------

To enable `Unified Checkout`:
Set the productInformation.selectedProducts.payments.unifiedCheckout.subscriptionInformation.enabled field to `yes`

REST Example: Enabling `Unified Checkout`
-----------------------------------------

Production Endpoint: `POST ``https://api.cybersource.com``/boarding/v1/registrations`
Test Endpoint: `POST ``https://apitest.cybersource.com``/boarding/v1/registrations`

```
{
   "productInformation":{
      "selectedProducts":{
         "payments":{
            "unifiedCheckout":{
               "subscriptionInformation":{
                  "enabled":"true"
               }
            }
         }
      }
   }
}
```

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

Create Organizations {#boarding-reg-intro}
==========================================

You can create organizations using the API. Instructions for creating organizations are included in these sections:

* [Create a Merchant Organization](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-reg-intro/boarding-reg-create-merch-api.md "")
* [Add a Transacting Organization to a New Merchant Organization](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-reg-intro/boarding-reg-create-new-transacting-api.md "")
* [Add a Transacting Organization to an Existing Organization](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-reg-intro/boarding-reg-create-transacting-api.md "")

{#boarding-reg-intro_ul_rw5_3bq_hvb}
For API field descriptions, see the [Boarding API Reference Guide](https://developer.cybersource.com/api-reference-assets/index.md?stage=pilot#merchant-boarding_merchant-boarding_create-a-boarding-registration ""). You can test API requests using the reference guide's live console.
Before beginning, review these topics:

* [Understanding Accounts and Organizations](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro-overview/boarding-intro-organizations.md "")
* [Understanding Organization IDs](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro-overview/boarding-intro-ids.md "")

If you use the API, keep in mind these considerations:

* The organization registration is done once using the `/registrations` endpoint. Modifications to existing organizations are done using the `/organizations` endpoint. Modifications to the product setups of an organization are done using the `/product-setups` endpoint. Examples of these endpoints are shown in the sections for those operations.
* The boardingFlow field has two values: `ENTERPRISE` and `SMB`. Enterprise creates one organization at a time. SMB (Small Business) creates a combination of one merchant organization and one transacting organization. Enterprise requires two requests, but defines an organization ID for the transacting organization instead of an automatically generated one. Enterprise is recommended. When you create a structural organization, you must set the value of boardingFlow to `ENTERPRISE`.
* The mode field is not currently supported.
* The configurable field must be set to `true` for merchant organizations and `false` for transacting and structural organizations.

Create a Merchant Organization {#boarding-reg-create-merch-api}
===============================================================

Use these instructions to create a merchant account using the API.

Endpoint {#boarding-reg-create-merch-api_d7e665}
------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/boarding/v1/registrations`{#boarding-reg-create-merch-api_d7e672}
**Test:** `POST ``https://apitest.cybersource.com``/boarding/v1/registrations`{#boarding-reg-create-merch-api_d7e682}

Required Fields for Boarding a Merchant Organization {#boarding-reg-create-merch-api-req-fields}
================================================================================================

[organizationInformation.businessInformation.address.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-address1.md "")
:

[organizationInformation.businessInformation.address.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-country.md "")
:

[organizationInformation.businessInformation.address.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-locality.md "")
:

[organizationInformation.businessInformation.businessContact.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-contact-email.md "")
:

[organizationInformation.businessInformation.businessContact.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-first-name.md "")
:

[organizationInformation.businessInformation.businessContact.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-last-name.md "")
:

[organizationInformation.businessInformation.businessContact.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-phone-num.md "")
:

[organizationInformation.businessInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-name.md "")
:

[organizationInformation.configurable](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-configurable.md "")
:
Set the value to `true`.

[organizationInformation.parentOrganizationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-parent-organization-id.md "")
:
Set to the ID of the organization that you want to be above this one in the hierarchy, which in this case would be the portfolio.

[organizationInformation.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-type.md "")
:
Set the value to `MERCHANT`.

REST Example: Creating a Merchant Organization {#boarding-reg-create-merch-api-example}
=======================================================================================

Request

```
{
    "registrationInformation": {
        "boardingFlow": "ENTERPRISE"
    },
    "organizationInformation": {
        "organizationId": "yourmerchantorgidhere",
        "status": "LIVE",
        "parentOrganizationId": "yourportfolioorgidhere",
        "type": "MERCHANT",
        "configurable": true,
        "businessInformation": {
            "address": {
                "country": "US",
                "address1": "123 Main",
                "postalCode": "99999",
                "administrativeArea": "WA",
                "locality": "Seattle"
            },
            "businessContact": {
                "firstName": "Jane",
                "lastName": "Smith",
                "phoneNumber": "5551234567",
                "email": "email@domain.com"
            },
            "technicalContact": {
                "firstName": "Jane",
                "lastName": "Smith",
                "phoneNumber": "5551234567",
                "email": "email@domain.com"
            },
            "emergencyContact": {
                "firstName": "Jane",
                "lastName": "Smith",
                "phoneNumber": "5551234567",
                "email": "email@domain.com"
            },
            "name": "Test Merchant",
            "websiteUrl": "https://www.MerchantUrlHere.com",
            "phoneNumber": "5551234567",
            "timeZone": "America/Los_Angeles",
            "merchantCategoryCode": "5999"
        }
    }
}
```

Response to a Successful Request

```
{
    "id": "1695804001",
    "submitTimeUtc": "2022-04-13T20:58:28Z",
    "status": "SUCCESS",
    "registrationInformation": {
        "mode": "COMPLETE",
        "boardingPackageId": "123456789012"
    },
    "organizationInformation": {
        "organizationId": "yourmercahntorgidhere",
        "parentOrganizationId": "yourportfolioorgidhere"
    },
    "message": "Request was processed successfully"
}
```

Add a Transacting Organization to a New Merchant Organization {#boarding-reg-create-new-transacting-api}
========================================================================================================

Use these instructions to create a transacting account using the API, as part of creating a new merchant account.

Endpoint {#boarding-reg-create-new-transacting-api_d7e665}
----------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/boarding/v1/registrations`{#boarding-reg-create-new-transacting-api_d7e672}
**Test:** `POST ``https://apitest.cybersource.com``/boarding/v1/registrations`{#boarding-reg-create-new-transacting-api_d7e682}

Required Fields for Adding a Transacting Organization to an Existing Organization {#boarding-reg-create-new-transacting-api-req-fields}
=======================================================================================================================================

[organizationInformation.businessInformation.address.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-address1.md "")
:

[organizationInformation.businessInformation.address.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-country.md "")
:

[organizationInformation.businessInformation.address.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-locality.md "")
:

[organizationInformation.businessInformation.businessContact.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-contact-email.md "")
:

[organizationInformation.businessInformation.businessContact.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-first-name.md "")
:

[organizationInformation.businessInformation.businessContact.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-last-name.md "")
:

[organizationInformation.businessInformation.businessContact.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-phone-num.md "")
:

[organizationInformation.businessInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-name.md "")
:

[organizationInformation.configurable](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-configurable.md "")
:
Set the value to `false`.

[organizationInformation.parentOrganizationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-parent-organization-id.md "")
:
Set to the ID of the merchant organization that you created during the previous section.

[organizationInformation.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-type.md "")
:
Set the value to `TRANSACTING`.

REST Example: Creating a Transacting Organization {#boarding-reg-create-new-transacting-api-example}
====================================================================================================

Request

```
{
    "registrationInformation": {
        "boardingFlow": "ENTERPRISE"
    },
    "organizationInformation": {
        "organizationId": "yourtransactingorgidhere",
        "status": "LIVE",
        "businessInformation": {
            "address": {
                "country": "US",
                "address1": "123 Main",
                "postalCode": "99999",
                "administrativeArea": "WA",
                "locality": "Seattle"
            },
            "businessContact": {
                "firstName": "Jane",
                "lastName": "Smith",
                "phoneNumber": "5551234567",
                "email": "email@domain.com"
            },
            "technicalContact": {
                "firstName": "Jane",
                "lastName": "Smith",
                "phoneNumber": "5551234567",
                "email": "email@domain.com"
            },
            "emergencyContact": {
                "firstName": "Jane",
                "lastName": "Smith",
                "phoneNumber": "5551234567",
                "email": "email@domain.com"
            },
            "name": "Test Merchant",
            "websiteUrl": "https://www.MerchantUrlHere.com",
            "phoneNumber": "5551234567",
            "timeZone": "America/Los_Angeles",
            "merchantCategoryCode": "5999"
        },
        "parentOrganizationId": "yourmercahntorgidhere",
        "type": "TRANSACTING",
        "configurable": false
    },
    "productInformation": {
        "selectedProducts": {
            "payments": {
                "customerInvoicing": {
                    "subscriptionInformation": {
                        "enabled": true,
                        "selfServiceability": "NOT_SELF_SERVICEABLE"
                    }
                }
            },
            "risk": {
                "fraudManagementEssentials": {
                    "subscriptionInformation": {
                        "enabled": true,
                        "selfServiceability": "NOT_SELF_SERVICEABLE"
                    }
                }
            },
            "commerceSolutions": {
                "tokenManagement": {
                    "subscriptionInformation": {
                        "enabled": true,
                        "selfServiceability": "NOT_SELF_SERVICEABLE"
                    }
                }
            },
            "valueAddedServices": {
                "transactionSearch": {
                    "subscriptionInformation": {
                        "enabled": true,
                        "selfServiceability": "NOT_SELF_SERVICEABLE"
                    }
                },
                "reporting": {
                    "subscriptionInformation": {
                        "enabled": true,
                        "selfServiceability": "NOT_SELF_SERVICEABLE"
                    }
                }
            }
        }
    }
}
```

Response to a Successful Request

```
{
    "id": "1696604001",
    "submitTimeUtc": "2022-04-13T21:03:02Z",
    "status": "SUCCESS",
    "registrationInformation": {
        "mode": "COMPLETE",
        "boardingPackageId": "123456789012"
    },
    "organizationInformation": {
        "organizationId": "yourtransactingorgidhere",
        "parentOrganizationId": "yourmercahntorgidhere"
    },
    "message": "Request was processed successfully"
}
```

Add a Transacting Organization to an Existing Organization {#boarding-reg-create-transacting-api}
=================================================================================================

Use these instructions to create a transacting account using the API.
You can also onboard a transacting organization using a solution identifier. See [REST Example: Creating a Transacting Organization with Integration Information](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-reg-create-transacting-integ-api-example.md ""). IMPORTANT This feature is in pilot phase. You have early access to this feature even though it might contain bugs or unfinished work. Please consider the risk when using this feature.

Endpoint {#boarding-reg-create-transacting-api_d7e665}
------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/boarding/v1/registrations`{#boarding-reg-create-transacting-api_d7e672}
**Test:** `POST ``https://apitest.cybersource.com``/boarding/v1/registrations`{#boarding-reg-create-transacting-api_d7e682}

Required Fields for Adding a Transacting Organization to an Existing Organization {#boarding-reg-create-transacting-api-req-fields}
===================================================================================================================================

[organizationInformation.businessInformation.address.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-address1.md "")
:

[organizationInformation.businessInformation.address.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-country.md "")
:

[organizationInformation.businessInformation.address.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-locality.md "")
:

[organizationInformation.businessInformation.businessContact.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-contact-email.md "")
:

[organizationInformation.businessInformation.businessContact.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-first-name.md "")
:

[organizationInformation.businessInformation.businessContact.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-last-name.md "")
:

[organizationInformation.businessInformation.businessContact.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-phone-num.md "")
:

[organizationInformation.businessInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-name.md "")
:

[organizationInformation.configurable](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-configurable.md "")
:
Set the value to `false`.

[organizationInformation.parentOrganizationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-parent-organization-id.md "")
:
Set to the ID of the organization that you want to be above this one in the hierarchy.

[organizationInformation.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-type.md "")
:
Set the value to `TRANSACTING`.

REST Example: Creating a Transacting Organization {#boarding-reg-create-transacting-api-example}
================================================================================================

Request

```
{
    "registrationInformation": {
        "boardingFlow": "ENTERPRISE"
    },
    "organizationInformation": {
        "organizationId": "yourtransactingorgidhere",
        "status": "LIVE",
        "businessInformation": {
            "address": {
                "country": "US",
                "address1": "123 Main",
                "postalCode": "99999",
                "administrativeArea": "WA",
                "locality": "Seattle"
            },
            "businessContact": {
                "firstName": "Jane",
                "lastName": "Smith",
                "phoneNumber": "5551234567",
                "email": "email@domain.com"
            },
            "technicalContact": {
                "firstName": "Jane",
                "lastName": "Smith",
                "phoneNumber": "5551234567",
                "email": "email@domain.com"
            },
            "emergencyContact": {
                "firstName": "Jane",
                "lastName": "Smith",
                "phoneNumber": "5551234567",
                "email": "email@domain.com"
            },
            "name": "Test Merchant",
            "websiteUrl": "https://www.MerchantUrlHere.com",
            "phoneNumber": "5551234567",
            "timeZone": "America/Los_Angeles",
            "merchantCategoryCode": "5999"
        },
        "parentOrganizationId": "yourmercahntorgidhere",
        "type": "TRANSACTING",
        "configurable": false
    },
    "productInformation": {
        "selectedProducts": {
            "payments": {
                "customerInvoicing": {
                    "subscriptionInformation": {
                        "enabled": true,
                        "selfServiceability": "NOT_SELF_SERVICEABLE"
                    }
                }
            },
            "risk": {
                "fraudManagementEssentials": {
                    "subscriptionInformation": {
                        "enabled": true,
                        "selfServiceability": "NOT_SELF_SERVICEABLE"
                    }
                }
            },
            "commerceSolutions": {
                "tokenManagement": {
                    "subscriptionInformation": {
                        "enabled": true,
                        "selfServiceability": "NOT_SELF_SERVICEABLE"
                    }
                }
            },
            "valueAddedServices": {
                "transactionSearch": {
                    "subscriptionInformation": {
                        "enabled": true,
                        "selfServiceability": "NOT_SELF_SERVICEABLE"
                    }
                },
                "reporting": {
                    "subscriptionInformation": {
                        "enabled": true,
                        "selfServiceability": "NOT_SELF_SERVICEABLE"
                    }
                }
            }
        }
    }
}
```

Request with Integration Information

```
{
  "registrationInformation": {
    "boardingFlow": "ENTERPRISE",
    "mode": "COMPLETE",
    "boardingPackageId": "16885604124"
  },
  "organizationInformation": {
    "status": "LIVE",
    "businessInformation": {
      "address": {
        "country": "GB",
        "address1": "Sample Street 1234",
        "locality": "London",
        "postalCode": "98765"
      },
      "businessContact": {
        "firstName": "Test",
        "lastName": "Test",
        "phoneNumber": "123456789",
        "email": "test@test.com"
      },
      "technicalContact": {
        "firstName": "Test",
        "lastName": "Test",
        "phoneNumber": "123456789",
        "email": "test@test.com"
      },
      "emergencyContact": {
        "firstName": "Test",
        "lastName": "Test",
        "phoneNumber": "123456789",
        "email": "test@test.com"
      },
      "name": "Test 4",
      "websiteUrl": "",
      "phoneNumber": "123456789",
      "timeZone": "GMT",
      "merchantCategoryCode": "5399"
    },
    "parentOrganizationId": "cptesting06",
    "type": "TRANSACTING",
    "configurable": false
  },
  "integrationInformation": {
    "tenantConfigurations": [
      {
        "solutionId": "wrqgaz3e"
      }
    ]
  },
  "productInformation": {
    "selectedProducts": {
      "payments": {
        "cardProcessing": {
          "subscriptionInformation": {
            "enabled": true,
            "features": {
              "cardNotPresent": {
                "enabled": false
              },
              "cardPresent": {
                "enabled": true
              }
            }
          },
          "configurationInformation": {
            "configurations": {
              "common": {
                "merchantCategoryCode": "5399",
                "defaultAuthTypeCode": "FINAL",
                "processors": {
                  "barclayshiso": {
                    "acquirer": {acq123
                    },
                    "paymentTypes": {
                      "MAESTRO": {
                        "enabled": true
                      },
                      "MASTERCARD": {
                        "enabled": true
                      },
                      "DISCOVER": {
                        "enabled": true
                      },
                      "JCB": {
                        "enabled": true
                      },
                      "VISA": {
                        "enabled": true
                      },
                      "VISA_ELECTRON": {
                        "enabled": true
                      },
                      "DINERS_CLUB": {
                        "enabled": true
                      },
                      "CUP": {
                        "enabled": true
                      }
                    },
                    "batchGroup": "barclayshiso_test",
                    "merchantId": "1234567",
                    "terminalId": null
                  }
                }
              },
              "features": {
                "cardNotPresent": {
                  "processors": {
                    "barclayshiso": {
                      "relaxAddressVerificationSystem": true,
                      "relaxAddressVerificationSystemAllowExpiredCard": true,
                      "relaxAddressVerificationSystemAllowZipWithoutCountry": true
                    }
                  }
                }
              }
            },
            "templateId": "F4EEFE3C-ED8C-4937-A48A-C013B228488E"
          }
        },
        "cybsReadyTerminal": {
          "subscriptionInformation": {
            "enabled": true,
            "selfServiceability": "NOT_SELF_SERVICEABLE"
          }
        }
      }
    }
  }
}
```

Response to Successful Request

```
{
    "id": "1696604001",
    "submitTimeUtc": "2022-04-13T21:03:02Z",
    "status": "SUCCESS",
    "registrationInformation": {
        "mode": "COMPLETE",
        "boardingPackageId": "123456789012"
    },
    "organizationInformation": {
        "organizationId": "yourtransactingorgidhere",
        "parentOrganizationId": "yourmercahntorgidhere"
    },
    "message": "Request was processed successfully"
}
```

Manage Organizations {#boarding-manage-org-intro}
=================================================

This section describes how to manage organizations:

* [Retrieve a List of Organizations](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-manage-org-intro/boarding-retrieve-organizations.md "")
* [Retrieve Organization Details](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-manage-org-intro/boarding-retrieve-an-organization.md "")
* [Update an Organization's Information](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-manage-org-intro/boarding-update-information-api.md "")
* [Change an Organization's Status](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-manage-org-intro/boarding-change-org-status.md "")

Retrieve a List of Organizations {#boarding-retrieve-organizations}
===================================================================

You can send a GET request to retrieve a list of all your organizations. You can use the GET request without parameters to retrieve the full list or use query parameters to limit the results. You can retrieve up to 1000 rows of organizations. To retrieve a list of organizations:

Endpoint {#boarding-retrieve-organizations_d7e717}
--------------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/oms/v1/organizations`{#boarding-retrieve-organizations_d7e724}
**Test:** `GET ``https://apitest.cybersource.com``/oms/v1/organizations`{#boarding-retrieve-organizations_d7e734}

Using Query Parameters to Filter Results {#boarding-retrieve-organizations-query-parameters}
============================================================================================

When you request the list of organizations for your account, you can use URL-encoded query parameters to narrow the list.

hierarchyQuery
:
See [Using the hierarchyQuery Parameter](#boarding-retrieve-organizations-query-parameters_hierarchyQuery "")

filters
:
Specify API field values using Lucene syntax. Keyword matching is supported. AND is the supported operator. For example, `type:"TRANSACTING" AND businessInformation.country:"US"` will return transacting organizations in the US.

fields
:
This will allow you to limit the response payload. Pass the payload attributes you want and the response will only contain those values:

    ```
      {
          organizationId,
          businessInformation:{
            phoneNumber
          }
      }
    ```

offset
:
The number specified in this parameter excludes that many items from the response. The default is `0`

limit
:
The number specified in this parameter limits how many items to include in the response. When combined with offset, limits the items returned to a specific number of items starting from a specific item. The default is `10`.

sort
:
The order in which you would like your results sorted. For example, `type:desc,entityName:asc`.

Using the hierarchyQuery Parameter {#boarding-retrieve-organizations-query-parameters_hierarchyQuery}
-----------------------------------------------------------------------------------------------------

The hierarchy query allows you to query relationships and explore your parents and children. This is a type of graph, so there is a defined language syntax that is flexible enough for you to explore this hierarchy in a natural way. The structure of the query is:
`organizationId.direction.distance`

* `organizationId` indicates the organizationId.
* `direction` specifies hierarchical relationships. Values can be `descendents` or `ancestors`.
* `distance` indicates levels of hierarchy. You can provide a whole number to specify the number levels of hierarchy to return. You can also use the asterisk `*` to include all levels.

**Examples:**

* `org1.descendents.*` - This will retrieve all descendents.
* `org1.ancestors.*` - This will retrieve all ancestors.
* `revent1234.descendents.1` - This will retrieve all direct children.

REST Example: Retrieving a List of Organizations {#boarding-retrieve-organizations-example}
===========================================================================================

Request

```keyword
GET https://api.cybersource.com/oms/v1/organizations?hierarchyQery=org1.descendents.1
```

Response to a Successful Request

```
200 OK
```

Retrieve Organization Details {#boarding-retrieve-an-organization}
==================================================================

You can send a GET request to retrieve the details of an organization. You can use the GET request without parameters to retrieve the full details or use the `fields` query parameter to limit the results. See [Using Query Parameters to Filter Results](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-manage-org-intro/boarding-retrieve-organizations/boarding-retrieve-organizations-query-parameters.md "") for more information about using the `fields` parameter.

Endpoint {#boarding-retrieve-an-organization_d7e743}
----------------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/oms/v1/organizations/{organizationId}`{#boarding-retrieve-an-organization_d7e750}
**Test:** `GET ``https://apitest.cybersource.com``/oms/v1/organizations/{organizationId}`{#boarding-retrieve-an-organization_d7e760}
Where *`{organizationId}`*is the ID that returned in the organization's boarding API response. Include only the fields you want to update.

REST Example: Retrieving an Organization {#boarding-retrieve-an-organization-example}
=====================================================================================

Request

```keyword
GET https://api.cybersource.com/oms/v1/organizations/org1
```

Response

```
200 OK
```

Update an Organization's Information {#boarding-update-information-api}
=======================================================================

Use these instructions to update an organization's information using the API.
Although organizationId is the only required field, any other field that contains organization information can be added to the API request to update the information in that field.

Endpoint {#boarding-update-information-api_d7e743}
--------------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/oms/v1/organizations/{organizationId}`{#boarding-update-information-api_d7e750}
**Test:** `GET ``https://apitest.cybersource.com``/oms/v1/organizations/{organizationId}`{#boarding-update-information-api_d7e760}
Where *`{organizationId}`*is the ID that returned in the organization's boarding API response. Include only the fields you want to update.

REST Example: Updating an Organization's Information {#boarding-update-information-api-example}
===============================================================================================

Request

```
{
  "organizationInformation": {
    "businessInformation": {
      "phoneNumber": "5121230987"
        }
    }
}
```

Response to a Successful Request

```
200 OK
```

Change an Organization's Status {#boarding-change-org-status}
=============================================================

You can change the status of organization by sending a GET request and including only the fields that you want to update in your request.

Endpoint {#boarding-change-org-status_d7e743}
---------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/oms/v1/organizations/{organizationId}`{#boarding-change-org-status_d7e750}
**Test:** `GET ``https://apitest.cybersource.com``/oms/v1/organizations/{organizationId}`{#boarding-change-org-status_d7e760}
Where *`{organizationId}`*is the ID that returned in the organization's boarding API response. Include only the fields you want to update.

REST Example: Changing an Organization's Status {#boarding-change-org-status-example}
=====================================================================================

Request

```
{}
```

Response to a Successful Request

```
200 OK
```

Product Enablement and Configuration Using the BRS API {#boarding-products-intro}
=================================================================================

You can enable and configure different products for merchants in the `Business Center` and the Product Enablement and Configuration Service (PECS) API.
You can use the PECS API to enable, subscribe, and configure products for a merchant. The PECS API is used during merchant onboarding and after merchant onboarding:

* **Merchant onboarding**: PECS is invoked by the Boarding Registration Service (BRS) API.
* **Post-merchant onboarding**: PECS is called to update the merchant's product subscriptions or configurations.
  {#boarding-products-intro_ul_pkv_ptf_lzb}
  During merchant onboarding, products can be enabled and configured. PECS supports multiple products that can be assigned to a merchant. Some products are available only for enablement and there is no capability to update configurations for these products. Some products are available for both enablement and configuration:

Enablement-only products:
:
* Acceptance Devices
* Card Present Connect
* `Checkout API`
* Customer Invoicing
* Digital Payment Suite
* Installments
* `Pay by Link`
* Receivables Manager
* Recurring Billing
* Reporting
* Tax Calculation
* Transaction Search
* `Unified Checkout`
{#boarding-products-intro_ul_p22_wtf_lzb}

Enablement and configuration products:
:
* Account Updater
* Advanced Billing
* Alternative Payment Methods
* Card Processing
* `Decision Manager`
* eCheck
* `Fraud Management Essentials`
* Gift Cards
* `Payer Authentication`
* `Service Orchestration`
* Payouts
* `Secure Acceptance`
* `Token Management Service`
* Virtual Terminal
{#boarding-products-intro_ul_ewv_wtf_lzb}
{#boarding-products-intro_dl_zfd_44m_lzb}

`Payer Authentication` {#boarding-payer-auth}
=============================================

`Payer Authentication` uses the 3-D Secure protocol in online transactions to verify that payment is coming from the legitimate cardholder. Authenticating the payer before the transaction is authorized benefits the merchant by shifting chargeback liability from the merchant to the card issuer.

Prerequisites {#boarding-payer-auth_pa-prereqs}
-----------------------------------------------

You must meet these requirements to enable and configure `Payer Authentication` for your merchants:

* You must include a merchant website URL. 3-D Secure protocol requires that the website URL must be in the format `https://www.example.com`.
* You must include a merchant category code for your merchant.
* At least one 3-D Secure template must be available. For information on creating product templates, see [Product Templates](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro-template.md "").

Status {#boarding-payer-auth_pa-status}
---------------------------------------

When you add Payer Authentication to a merchant account, one of these statuses is assigned:

* Boarded: The Payer Authentication configuration was successfully saved and the merchant can proceed to transact the card network using the specified currency.
* Pending: The Payer Authentication configuration is partially saved or incomplete. Raise a ticket with customer support.
  {#boarding-payer-auth_ul_gn4_xfb_q2c}

Enable `Payer Authentication` {#boarding-payer-auth-enable-intro}
=================================================================

This section shows you how to enable `Payer Authentication`.

Endpoint {#boarding-payer-auth-enable-intro_d7e665}
---------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/boarding/v1/registrations`{#boarding-payer-auth-enable-intro_d7e672}
**Test:** `POST ``https://apitest.cybersource.com``/boarding/v1/registrations`{#boarding-payer-auth-enable-intro_d7e682}

Required Fields for Enabling `Payer Authentication` {#boarding-payer-auth-enable-reqfields}
===========================================================================================

[organizationInformation.businessInformation.address.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-address1.md "")
:

[organizationInformation.businessInformation.address.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-admin-area.md "")
:

[organizationInformation.businessInformation.address.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-country.md "")
:

[organizationInformation.businessInformation.address.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-locality.md "")
:

[organizationInformation.businessInformation.address.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-postal-code.md "")
:

[organizationInformation.businessInformation.businessContact.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-contact-email.md "")
:

[organizationInformation.businessInformation.businessContact.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-first-name.md "")
:

[organizationInformation.businessInformation.businessContact.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-last-name.md "")
:

[organizationInformation.businessInformation.businessContact.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-phone-num.md "")
:

[organizationInformation.businessInformation.businessContact.websiteUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-website-url.md "")
:
Must be in the format `http://www.example.com`.

[organizationInformation.businessInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-name.md "")
:

[organizationInformation.configurable](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-configurable.md "")
:
Set to `false`.

[organizationInformation.parentOrganizationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-parent-organization-id.md "")
:

[organizationInformation.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-type.md "")
:
Set to `TRANSACTING`.

[registrationInformation.boardingFlow](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reg-info-aa/reg-info-boarding-flow.md "")
:
Set to `ADDPRODUCT`.

American Express SafeKey-Specific Fields
----------------------------------------

Include these fields in addition to the required fields to enable and configure American Express SafeKey:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.amexSafeKey.currencies\[\].acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-0.md "")
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
{#boarding-payer-auth-enable-reqfields_boarding-acq-id}
{#boarding-payer-auth-enable-reqfields_boarding-acq-id}
:
For testing purposes, use Acquirer ID: `cybersource`.
{#boarding-payer-auth-enable-reqfields_boarding-acq-id-test}
{#boarding-payer-auth-enable-reqfields_boarding-acq-id-test}

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.amexSafeKey.currencies\[\].currencyCodes\[\]](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-1.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.amexSafeKey.currencies\[\].processorMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-2.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.amexSafeKey.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-4.md "")
:
Set to `true`.

Cartes Bancaires-Specific Fields
--------------------------------

Include these fields in addition to the required fields to enable and configure Cartes Bancaires:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.CB.currencies\[\].acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-5.md "")
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.CB.currencies\[\].currencyCodes\[\]](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-6.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.CB.currencies\[\].processorMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-7.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.CB.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-10.md "")
:
Set to `true`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.CB.requestorId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-8.md "")
:

Discover/Diners Club ProtectBuy-Specific Fields
-----------------------------------------------

Include these fields in addition to the required fields to enable and configure Discover/Diners Club ProtectBuy:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.dinersClubInternationalProtectBuy.currencies\[\].acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-12.md "")
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.dinersClubInternationalProtectBuy.currencies\[\].currencyCodes\[\]](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-13.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.dinersClubInternationalProtectBuy.currencies\[\].processorMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-14.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.dinersClubInternationalProtectBuy.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-17.md "")
:
Set to `true`.

ELO-Specific Fields
-------------------

Include these fields in addition to the required fields to enable and configure ELO:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.ELO.currencies\[\].acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-18.md "")
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.ELO.currencies\[\].currencyCodes\[\]](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-19.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.ELO.currencies\[\].processorMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-20.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.ELO.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-23.md "")
:
Set to `true`.

JCB J/Secure-Specific Fields
----------------------------

Include these fields in addition to the required fields to enable and configure JCB J/Secure:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.jCBJSecure.currencies\[\].acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-25.md "")
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.jCBJSecure.currencies\[\].currencyCodes\[\]](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-26.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.jCBJSecure.currencies\[\].processorMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-27.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.jCBJSecure.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-29.md "")
:
Set to `true`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.jCBJSecure.securePasswordForJCB](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-30.md "")
:

Mastercard/Meeza Identity Check-Specific Fields
-----------------------------------------------

Include these fields in addition to the required fields to enable and configure Mastercard/Meeza Identity Check:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.masterCardSecureCode.currencies\[\].acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-33.md "")
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.masterCardSecureCode.currencies\[\].currencyCodes\[\]](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-34.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.masterCardSecureCode.currencies\[\].processorMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-35.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.masterCardSecureCode.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-36.md "")
:
Set to `true`.

UnionPay 3-D Secure-Specific Fields
-----------------------------------

Include these fields in addition to the required fields to enable and configure UnionPay 3-D Secure:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.UPI.currencies\[\].acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-37.md "")
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.UPI.currencies\[\].currencyCodes\[\]](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-38.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.UPI.currencies\[\].processorMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-39.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.UPI.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-42.md "")
:
Set to `true`.

Visa Secure-Specific Fields
---------------------------

Include these fields in addition to the required fields to enable and configure Visa Secure:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.verifiedByVisa.currencies\[\].acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-44.md "")
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.verifiedByVisa.currencies\[\].currencyCodes\[\]](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-45.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.verifiedByVisa.currencies\[\].processorMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-46.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.verifiedByVisa.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-48.md "")
:
Set to `true`.

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/api-fields-about-guide.md "")
  {#boarding-payer-auth-enable-reqfields_ul_kpc_xzz_sxb}

REST Example: Enabling `Payer Authentication` {#boarding-payer-auth-enable-ex-rest}
===================================================================================

Request

```
{
  "registrationInformation": {
    "boardingFlow": "ADDPRODUCT"
  },
  "organizationInformation": {
    "organizationId": "apitester00",
    "parentOrganizationId": "nishtx",
    "type": "TRANSACTING",
    "configurable": false,
    "businessInformation": {
      "address": {
        "country": "US",
        "address1": "123 Main",
        "postalCode": "99999",
        "administrativeArea": "WA",
        "locality": "Seattle"
      },
      "businessContact": {
        "firstName": "Jane",
        "lastName": "Smith",
        "phoneNumber": "5551234567",
        "email": "email@domain.com"
      },
      "name": "Test Merchant",
      "websiteUrl": "https://www.example.com"
    }
  },
  "productInformation": {
    "selectedProducts": {
      "payments": {
        "payerAuthentication": {
          "configurationInformation": {
            "configurations": {
              "cardTypes": {
                "amexSafeKey": {
                  "enabled": true,
                  "currencies": [
                    {
                      "currencyCodes": ["ALL"],
                      "acquirerId": "12345678901-1000",
                      "processorMerchantId": "procmerch123"
                    }
                  ]
                },
                "CB": {
                  "requestorId": "",
                  "enabled": true,
                  "currencies": [
                    {
                      "currencyCodes": ["ALL"],
                      "acquirerId": "211111-1000",
                      "processorMerchantId": "procmerch123"
                    }
                  ]
                },
                "dinersClubInternationalProtectBuy": {
                  "enabled": true,
                  "currencies": [
                    {
                      "currencyCodes": ["ALL"],
                      "acquirerId": "311111-1000",
                      "processorMerchantId": "procmerch123"
                    }
                  ]
                },
                "ELO": {
                  "enabled": true,
                  "currencies": [
                    {
                      "currencyCodes": ["ALL"],
                      "acquirerId": "11111111-1000",
                      "processorMerchantId": "procmerch123"
                    }
                  ]
                },
                "jCBJSecure": {
                  "securePasswordForJCB": "jcbpass",
                  "enabled": true,
                  "currencies": [
                    {
                      "currencyCodes": ["ALL"],
                      "acquirerId": "123456-1000",
                      "processorMerchantId": "procmerch123"
                    }
                  ]
                },
                "masterCardSecureCode": {
                  "enabled": true,
                  "currencies": [
                    {
                      "currencyCodes": ["ALL"],
                      "acquirerId": "522222-1000",
                      "processorMerchantId": "procmerch123"
                    }
                  ]
                },
                "UPI": {
                  "enabled": true,
                  "currencies": [
                    {
                      "currencyCodes": ["ALL"],
                      "acquirerId": "611111-1000",
                      "processorMerchantId": "procmerch123"
                    }
                  ]
                },
                "verifiedByVisa": {
                  "enabled": true,
                  "currencies": [
                    {
                      "currencyCodes": ["ALL"],
                      "acquirerId": "411111-1000",
                      "processorMerchantId": "procmerch123"
                    }
                  ]
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

Response to a Successful Request

```
{
  "id": "87304104004",
  "submitTimeUtc": "2024-05-14T15:53:19Z",
  "status": "PROCESSING",
  "registrationInformation": {
    "mode": "COMPLETE",
    "boardingPackageId": "190303004"
  },
  "organizationInformation": {
    "organizationId": "apitester00",
    "parentOrganizationId": "nishtx"
  },
  "message": "Request is being processed"
}
```

`Token Management Service` {#boarding-tms}
==========================================

The `Token Management Service` (`TMS`) links tokens across service providers, payment types, and channels for sellers, acquirers, and technology partners. `TMS` tokenizes, securely stores, and manages the primary account number (PAN), the payment card expiration date, electronic check details, and customer data. `TMS` also enables merchants to create a network token of a customer's payment card.

> IMPORTANT
> When you board a merchant and enable ` TMS ` and network tokenization, the token requestor ID is enrolled at the merchant account organization level where the token vault is configured. You must include the merchant business information during token requestor ID enrollment and when you create the ` TMS ` token vault. This ensures that the network tokens that are provisioned are assigned to the merchant that owns the tokens.
> For more information on `TMS` and network tokenization, see [Token Vault Management](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-products-intro/boarding-tms/tms-vault-hierarchy.md "").

Token Vault Management {#tms-vault-hierarchy}
=============================================

Token vaults are where merchants store their customer and payment data. A `Business Center` internal user can enable the `TMS` vault.
Vaults are assigned to an owner, and all data within the vault belongs to the owner. You can grant permission to individual MIDs to create, retrieve, update, and delete tokens within a vault. Created tokens belong to the owner of the vault, not the creator of the token. If you remove a MID from a vault, it can no longer access any tokens within that vault, including tokens created under that MID.
IMPORTANT It is not currently possible to merge vaults, so ensure that merchants are set up with the correct vault by creating a new vault or granting access to an existing vault.

Token Requestor IDs {#tms-trids}
================================

A token requestor ID (TRID) is a unique identifier that entities such as merchants use to request network tokens from token providers. Having a TRID is a prerequisite for enabling network tokenization.
Each entity must register with the token provider to get a TRID. Contact a `Cybersource` representative to enroll a merchant as a token requestor.

Visa and Mastercard TRIDs
-------------------------

An internal user can enroll a merchant as a VISA or Mastercard token requestor through the `Business Center`.
Follow these steps to enroll a merchant as a token requestor in the `Business Center`:
1. Navigate to Token Management.

2. Click Vault Management.

3. Use the Vault Owner filter to search for the merchant account that has `TMS` enabled.

4. Choose the merchant account to view the `TMS` vaults that are configured for the merchant.

5. Click Network Tokenization.

6. Click Enroll to VISA/Mastercard token services.

7. Enter the required information for each card type:

   Mastercard
   :
   Business entity name

   Visa
   :
   Merchant name
   :
   Merchant website URL
   :
   Merchant country code

8. Click Onboard with Acquirer ID.

9. Enter the required information:

   Acquirer ID
   :
   Set the value to `40010052242`. It is a static acquirer ID that is used for `TMS`.

   Acquirer Merchant ID
   :
   Enter your organization ID.

10. Click Enroll to Network Token Services to complete enrollment.
    When the enrollment is submitted, the relationship ID and token requestor ID appear on the page for Visa Token Service (VTS) and the token requestor ID appears for Mastercard.
    In order to request a TRID from the token provider, `Cybersource` uses merchant business details already stored. If any of the details are not present, a dialog form should appear prompting you to complete the missing information.

American Express TRIDs
----------------------

Enrollment as a token requestor for American Express is a manual process. Contact your `Cybersource` representative to request the TRID for American Express.
Allow 2 to 3 days for the completion of your request.

> IMPORTANT
> **Service establishment (SE) Numbers** are required in order to process American Express card transactions.

Configure the Token Vault Settings Using the `Business Center` {#tms-vault-settings}
====================================================================================

Follow these steps to configure your merchant token vault settings:

1. Log in to the `Business Center` test environment or production environment.

   * **Test:** `https://businesscentertest.cybersource.com`
   * **Production:** `https://businesscenter.cybersource.com`
2. In the left navigation panel, click the Token Management icon ( ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-tkn-mgmt.svg/jcr:content/renditions/original) ).

3. Click Vault Management New. The Vault Management page appears.

4. From the Vault Owner drop-down list, select the vault owner..

5. In the Details column, click Vault Settings. The Edit Vault page appears.

6. Click Edit.
   A dialog box appears with a message to warn you that changing your vault settings could result in your merchants being unable to access tokens, which could result in failing transactions. Click Yes if you want to continue.

7. Enter the vault name, supported payment methods, supported token types and formats, card number masking format, payment instrument storing configuration, and the webhook URL.
   For each token type, you can choose from these token formats:

   * 32 Character Hex
   * 22 Digits
   * 19 Digits Luhn Check Passing
   * 16 Digits Luhn Check Passing

   > IMPORTANT Account Updater is incompatible with instrument identifier tokens in the 22-digit format.

8. Click SAVE.

9. To return to the vault management page, click VAULT MANAGEMENT.

Configure the Token Vault Access Using the `Business Center` {#tms-vault-mid-access}
====================================================================================

Follow these steps to configure your merchant token vault access settings:

1. Log in to the `Business Center` test environment or production environment.
   * **Test:** `https://businesscentertest.cybersource.com`
   * **Production:** `https://businesscenter.cybersource.com`
2. In the left navigation panel, click the Token Management icon ( ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-tkn-mgmt.svg/jcr:content/renditions/original) ).
3. Click Vault Management New. The Vault Management page appears.
4. Select the vault owner that you want to configure from the Vault Owner drop-down list.
5. In the Details column, click Access Settings. The MID Access page appears.
6. Check the box for the vault settings you want to enable for each merchant you want to configure:
   * Visa Token
   * Mastercard Token
   * Card Unmasked
   * Create
   * Update
   * Retrieve
7. Click Submit to save your settings.

Enable `Token Management Service` Using a Template {#boarding-tms-enable-intro}
===============================================================================

This section shows you how to enable `TMS`.

Endpoint {#boarding-tms-enable-intro_d7e665}
--------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/boarding/v1/registrations`{#boarding-tms-enable-intro_d7e672}
**Test:** `POST ``https://apitest.cybersource.com``/boarding/v1/registrations`{#boarding-tms-enable-intro_d7e682}

Required Fields for Enabling `TMS` Using a Template {#boarding-tms-enable-reqfields}
====================================================================================

[organizationInformation.businessInformation.address.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-address1.md "")
:

[organizationInformation.businessInformation.address.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-admin-area.md "")
:

[organizationInformation.businessInformation.address.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-country.md "")
:

[organizationInformation.businessInformation.address.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-locality.md "")
:

[organizationInformation.businessInformation.address.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-postal-code.md "")
:

[organizationInformation.businessInformation.businessContact.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-contact-email.md "")
:

[organizationInformation.businessInformation.businessContact.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-first-name.md "")
:

[organizationInformation.businessInformation.businessContact.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-last-name.md "")
:

[organizationInformation.businessInformation.businessContact.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-phone-num.md "")
:

[organizationInformation.businessInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-name.md "")
:

[organizationInformation.configurable](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-configurable.md "")
:
Set to `false`.

[organizationInformation.parentOrganizationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-parent-organization-id.md "")
:

[organizationInformation.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-type.md "")
:
Set to `TRANSACTING`.

[productInformation.selectedProducts.commerceSolutions.tokenManagement.configurationInformation.templateId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-tem.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement.subscriptionInformation.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-sub-enab.md "")
:
Set to `true` to enable `Token Management Service`.

[productInformation.selectedProducts.commerceSolutions.tokenManagement.subscriptionInformation.selfServiceability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-sub-self.md "")
:

[registrationInformation.boardingFlow](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reg-info-aa/reg-info-boarding-flow.md "")
:
Set to `ADDPRODUCT`.

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/api-fields-about-guide.md "")
  {#boarding-tms-enable-reqfields_ul_kpc_xzz_sxb}

REST Example: Enabling `TMS` Using a Template {#boarding-tms-enable-ex-rest}
============================================================================

Request

```
{
  "registrationInformation": {
    "boardingFlow": "ADDPRODUCT"
  },
  "organizationInformation": {
    "parentOrganizationId": "3b2bwnhbm7cdzath0qcn0luhkpvb",
    "type": "TRANSACTING",
    "configurable": false,
    "businessInformation": {
      "name": "Test Merchant",
      "address": {
        "country": "US",
        "address1": "123 Main",
        "locality": "Seattle",
        "administrativeArea": "WA",
        "postalCode": "99999"
      },
      "businessContact": {
        "firstName": "Jane",
        "lastName": "Smith",
        "phoneNumber": "5551234567",
        "email": "email@domain.com"
      }
    }
  },
  "productInformation": {
    "selectedProducts": {
      "commerceSolutions": {
        "tokenManagement": {
          "subscriptionInformation": {
            "enabled": true,
            "selfServiceability": "NOT_SELF_SERVICEABLE"
          },
          "configurationInformation": {
            "templateId": "43107BC1-E3DA-4019-9306-4510AD4DE05F"
          }
        }
      }
    }
  }
}
```

Response to Successful Request

```
{
  "id": "94498504004",
  "submitTimeUtc": "2024-07-01T16:25:20Z",
  "status": "SUCCESS",
  "registrationInformation": {
    "mode": "COMPLETE",
    "boardingPackageId": "1168704004"
  },
  "organizationInformation": {
    "organizationId": "{MerchantAccountOrgId}",
    "parentOrganizationId": "{PortfolioOrgId}"
  },
  "message": "Request was processed successfully"
}
```

Enable `TMS` and Enroll in Network Tokenization for a New Merchant {#boarding-tms-enable-net-tkn-intro}
=======================================================================================================

This section shows you how to enable `TMS` and enroll in network tokenization for a new merchant.

Endpoint {#boarding-tms-enable-net-tkn-intro_d7e665}
----------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/boarding/v1/registrations`{#boarding-tms-enable-net-tkn-intro_d7e672}
**Test:** `POST ``https://apitest.cybersource.com``/boarding/v1/registrations`{#boarding-tms-enable-net-tkn-intro_d7e682}

Required Fields for Enabling `TMS` and Enrolling in Network Tokenization for a New Merchant {#boarding-tms-enable-net-tkn-reqfields}
====================================================================================================================================

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.defaultTokenType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-vau.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.location](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-21.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.sensitivePrivileges.cardNumberMaskingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-22.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.tokenFormats.customer](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-23.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.tokenFormats.instrumentIdentifierBankAccount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-24.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.tokenFormats.instrumentIdentifierCard](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-25.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.tokenFormats.paymentInstrument](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-26.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.acquirer.acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-net.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement.configurationInformation. configurations.networkTokenEnrollment.businessInformation.acquirer.acquirerMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--0.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.address.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--1.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.address.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--2.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.doingBusinessAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--4.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement.configurationInformation. configurations.networkTokenEnrollment.businessInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--5.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.networkTokenServices. mastercardDigitalEnablementService.enrollment](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-13.md "")
:
Set to `true`.

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.networkTokenServices.visaTokenService.enrollment](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-18.md "")
:
Set to `true`.

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.websiteUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--3.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.mastercardDigitalEnablementService.enableService](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-12.md "")
:
Set to `true`.

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.mastercardDigitalEnablementService.enableTransactionalTokens](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-11.md "")
:
Set to `true`.

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.notifications.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-15.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.paymentCredentials.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-10.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.visaTokenService.enableService](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-17.md "")
:
Set to `true`.

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.visaTokenService.enableTransactionalTokens](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-16.md "")
:
Set to `true`.

[organizationInformation.businessInformation.address.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-address1.md "")
:

[organizationInformation.businessInformation.address.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-admin-area.md "")
:

[organizationInformation.businessInformation.address.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-country.md "")
:

[organizationInformation.businessInformation.address.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-locality.md "")
:

[organizationInformation.businessInformation.address.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-postal-code.md "")
:

[organizationInformation.businessInformation.businessContact.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-contact-email.md "")
:

[organizationInformation.businessInformation.businessContact.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-first-name.md "")
:

[organizationInformation.businessInformation.businessContact.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-last-name.md "")
:

[organizationInformation.businessInformation.businessContact.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-phone-num.md "")
:

[organizationInformation.businessInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-name.md "")
:

[organizationInformation.configurable](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-configurable.md "")
:
Set to `true`.

[organizationInformation.organizationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-organization-id.md "")
:

[organizationInformation.parentOrganizationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-parent-organization-id.md "")
:

[organizationInformation.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-type.md "")
:
Set to `MERCHANT`.

[registrationInformation.boardingFlow](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reg-info-aa/reg-info-boarding-flow.md "")
:
Set to `ADDPRODUCT`.

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/api-fields-about-guide.md "")
  {#boarding-tms-enable-net-tkn-reqfields_ul_kpc_xzz_sxb}

REST Example: Enabling `TMS` and Enrolling in Network Tokenization for a New Merchant {#boarding-tms-enable-net-tkn-ex-rest}
============================================================================================================================

Request

```
{
  "registrationInformation": {
    "boardingFlow": "ENTERPRISE"
  },
  "organizationInformation": {
    "organizationId": "yourmerchantorgidhere",
    "parentOrganizationId": "yourportfolioorgidhere",
    "type": "MERCHANT",
    "configurable": true,
    "businessInformation": {
      "name": "NetworkTokenMerchant",
      "address": {
        "country": "US",
        "address1": "123456 SandMarket",
        "locality": "ORMOND BEACH",
        "administrativeArea": "FL",
        "postalCode": "32176"
      },
      "websiteUrl": "https://www.NetworkTokenMerchant.com",
      "businessContact": {
        "firstName": "Token",
        "lastName": "Man",
        "phoneNumber": "6574567813",
        "email": "networktokenman@visa.com"
      }
    }
  },
  "productInformation": {
    "selectedProducts": {
      "commerceSolutions": {
        "tokenManagement": {
          "subscriptionInformation": {
            "enabled": true
          },
          "configurationInformation": {
            "configurations": {
              "vault": {
                "location": "GDC",
                "defaultTokenType": "CUSTOMER",
                "tokenFormats": {
                  "customer": "32_HEX",
                  "paymentInstrument": "32_HEX",
                  "instrumentIdentifierCard": "19_DIGIT_LAST_4",
                  "instrumentIdentifierBankAccount": "32_HEX"
                },
                "sensitivePrivileges": {
                  "cardNumberMaskingFormat": "FIRST_6_LAST_4"
                },
                "networkTokenServices": {
                  "notifications": {
                    "enabled": true
                  },
                  "paymentCredentials": {
                    "enabled": true
                  },
                  "synchronousProvisioning": {
                    "enabled": false
                  },
                  "visaTokenService": {
                    "enableService": true,
                    "enableTransactionalTokens": true
                  },
                  "mastercardDigitalEnablementService": {
                    "enableService": true,
                    "enableTransactionalTokens": true
                  }
                }
              },
              "networkTokenEnrollment": {
                "businessInformation": {
                  "name": "NetworkTokenMerchant",
                  "doingBusinessAs": "NetworkTokenCo1",
                  "address": {
                    "country": "US",
                    "locality": "ORMOND BEACH"
                  },
                  "websiteUrl": "https://www.NetworkTokenMerchant.com",
                  "acquirer": {
                    "acquirerId": "40010052242",
                    "acquirerMerchantId": "MerchantOrgID"
                  }
                },
                "networkTokenServices": {
                  "visaTokenService": {
                    "enrollment": true
                  },
                  "mastercardDigitalEnablementService": {
                    "enrollment": true
                  }
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

Response to Successful Request

```
{
  "id": "94498504004",
  "submitTimeUtc": "2024-07-01T16:25:20Z",
  "status": "SUCCESS",
  "registrationInformation": {
    "mode": "COMPLETE",
    "boardingPackageId": "1168704004"
  },
  "organizationInformation": {
    "organizationId": "{MerchantAccountOrgId}",
    "parentOrganizationId": "{PortfolioOrgId}"
  },
  "message": "Request was processed successfully"
}

```

Enable `TMS` and Enroll in Network Tokenization for an Existing Merchant {#boarding-tms-enable-net-tkn-existing-intro}
======================================================================================================================

This section shows you how to enable `TMS` and enroll in network tokenization for an existing merchant organization.

Endpoint {#boarding-tms-enable-net-tkn-existing-intro_d7e665}
-------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/boarding/v1/registrations`{#boarding-tms-enable-net-tkn-existing-intro_d7e672}
**Test:** `POST ``https://apitest.cybersource.com``/boarding/v1/registrations`{#boarding-tms-enable-net-tkn-existing-intro_d7e682}

Required Fields for Enabling `TMS` and Enrolling in Network Tokenization for an Existing Merchant {#boarding-tms-enable-net-tkn-existing-reqfields}
===================================================================================================================================================

[organizationInformation.parentOrganizationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-parent-organization-id.md "")
:

[organizationInformation.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-type.md "")
:
Set to `MERCHANT`.

[organizationInformation.configurable](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-configurable.md "")
:
Set to `true`.

[registrationInformation.boardingFlow](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reg-info-aa/reg-info-boarding-flow.md "")
:
Set to `ADDPRODUCT`.

[organizationInformation.businessInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-name.md "")
:

[organizationInformation.businessInformation.address.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-country.md "")
:

[organizationInformation.businessInformation.address.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-address1.md "")
:

[organizationInformation.businessInformation.address.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-postal-code.md "")
:

[organizationInformation.businessInformation.address.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-admin-area.md "")
:

[organizationInformation.businessInformation.address.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-locality.md "")
:

[organizationInformation.businessInformation.businessContact.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-first-name.md "")
:

[organizationInformation.businessInformation.businessContact.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-last-name.md "")
:

[organizationInformation.businessInformation.businessContact.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-phone-num.md "")
:

[organizationInformation.businessInformation.businessContact.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-contact-email.md "")
:

[organizationInformation.organizationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-organization-id.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.location](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-21.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.defaultTokenType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-vau.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.tokenFormats.customer](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-23.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.tokenFormats.paymentInstrument](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-26.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.tokenFormats.instrumentIdentifierCard](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-25.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.tokenFormats.instrumentIdentifierBankAccount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-24.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.sensitivePrivileges.cardNumberMaskingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-22.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement.configurationInformation. configurations.networkTokenEnrollment.businessInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--5.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.doingBusinessAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--4.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.address.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--1.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.address.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--2.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.websiteUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--3.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.acquirer.acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-net.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement.configurationInformation. configurations.networkTokenEnrollment.businessInformation.acquirer.acquirerMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--0.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.networkTokenServices.visaTokenService.enrollment](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-18.md "")
:
Set to `true`.

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.networkTokenServices. mastercardDigitalEnablementService.enrollment](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-13.md "")
:
Set to `true`.

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.notifications.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-15.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.paymentCredentials.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-10.md "")
:

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.visaTokenService.enableService](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-17.md "")
:
Set to `true`.

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.visaTokenService.enableTransactionalTokens](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-16.md "")
:
Set to `true`.

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.mastercardDigitalEnablementService.enableService](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-12.md "")
:
Set to `true`.

[productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.mastercardDigitalEnablementService.enableTransactionalTokens](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-11.md "")
:
Set to `true`.

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/api-fields-about-guide.md "")
  {#boarding-tms-enable-net-tkn-existing-reqfields_ul_kpc_xzz_sxb}

REST Example: Enabling `TMS` and Enrolling in Network Tokenization for an Existing Merchant {#boarding-tms-enable-net-tkn-existing-ex-rest}
===========================================================================================================================================

Request

```
{
   "registrationInformation":{
      "boardingFlow":"ADDPRODUCT"
   },
   "organizationInformation":{
      "organizationId":"yourmerchantorgidhere",
      "parentOrganizationId":"yourportfolioorgidhere",
      "type":"MERCHANT",
      "configurable":true,
      "businessInformation":{
         "name":"TokenMerchant",
         "address":{
            "country":"US",
            "address1":"123456 SandMarket",
            "locality":"ORMOND BEACH",
            "administrativeArea":"FL",
            "postalCode":"32176"
         },
         "websiteUrl":"https://www.MerchantUrlHere.com",
         "businessContact":{
            "firstName":"Token",
            "lastName":"Man",
            "phoneNumber":"6574567813",
            "email":"tokenman@visa.com"
         }
      }
   },
   "productInformation":{
      "selectedProducts":{
         "commerceSolutions":{
            "tokenManagement":{
               "subscriptionInformation":{
                  "enabled":true
               },
               "configurationInformation":{
                  "configurations":{
                        "vault":{
                        "location": "GDC",
                        "defaultTokenType":"CUSTOMER",
                        "tokenFormats":{
                           "customer":"32_HEX",
                           "paymentInstrument":"32_HEX",
                           "instrumentIdentifierCard":"19_DIGIT_LAST_4",
                           "instrumentIdentifierBankAccount":"32_HEX"
                        },
                        "sensitivePrivileges":{
                           "cardNumberMaskingFormat":"FIRST_6_LAST_4"
                        }                     },
                     "networkTokenEnrollment":{
                        "businessInformation":{
                           "name":"TokenMerchant",
                           "doingBusinessAs":"NetworkTokenCo1",
                           "address":{
                              "country":"US",
                              "locality":"ORMOND BEACH"
                           },
                           "websiteUrl":"https://www.MerchantUrlHere.com",
                           "acquirer":{
                              "acquirerId":"40010052242",
                              "acquirerMerchantId":"yourmerchantorgidhere"
                           }
                        },
                        "networkTokenServices":{
                           "visaTokenService":{
                              "enrollment":true
                           },
                           "mastercardDigitalEnablementService":{
                              "enrollment":true
                           }
                        }
                     },
                        "networkTokenServices":{
                           "notifications":{
                              "enabled":true
                           },
                           "paymentCredentials":{
                              "enabled":true
                           },
                           "visaTokenService":{
                              "enableService":true,
                              "enableTransactionalTokens":true
                           },
                           "mastercardDigitalEnablementService":{
                              "enableService":true,
                              "enableTransactionalTokens":true
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

Response to Successful Request

```
{
  "id": "94498504004",
  "submitTimeUtc": "2024-07-01T16:25:20Z",
  "status": "SUCCESS",
  "registrationInformation": {
    "mode": "COMPLETE",
    "boardingPackageId": "1168704004"
  },
  "organizationInformation": {
    "organizationId": "{MerchantAccountOrgId}",
    "parentOrganizationId": "{PortfolioOrgId}"
  },
  "message": "Request was processed successfully"
}

```

Product Enablement and Configuration Using the PECS API {#boarding-products}
============================================================================

You can enable and configure different products for merchants in the `Business Center` and the Product Enablement and Configuration Service (PECS) API.
You can use the PECS API to enable, subscribe, and configure products for a merchant. The PECS API is used during merchant onboading and after merchant onboarding:

* **Merchant onboarding**: PECS is invoked by the Boarding Registration Service (BRS) API.
* **Post-merchant onboarding**: PECS is called to update the merchant's product subscriptions or configurations.
  {#boarding-products_ul_pkv_ptf_lzb}
  During merchant onboarding, products can be enabled and configured. PECS supports multiple products that can be assigned to a merchant. Some products are available only for enablement and there is no capability to update configurations for these products. Some products are available for both enablement and configuration:

Enablement-only products:
:
* Acceptance Devices
* Card Present Connect
* `Checkout API`
* Customer Invoicing
* Digital Payment Suite
* Installments
* `Pay by Link`
* Receivables Manager
* Recurring Billing
* Reporting
* Tax Calculation
* Transaction Search
* `Unified Checkout`
{#boarding-products_ul_p22_wtf_lzb}

Enablement and configuration products:
:
* Account Updater
* Advanced Billing
* Alternative Payment Methods
* Card Processing
* `Decision Manager`
* eCheck
* `Fraud Management Essentials`
* Gift Cards
* `Payer Authentication`
* `Service Orchestration`
* Payouts
* `Secure Acceptance`
* `Token Management Service`
* Virtual Terminal
{#boarding-products_ul_ewv_wtf_lzb}

Add a New Product to an Existing Organization {#boarding-update-product-api}
============================================================================

To add a product, you must subscribe to it, and if there are configurations available, configure it.

Endpoint {#boarding-update-product-api_d7e638}
----------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/products/v1/product-setups`{#boarding-update-product-api_d7e645}
**Test:** `POST ``https://apitest.cybersource.com``/products/v1/product-setups`{#boarding-update-product-api_d7e655}

Subscribing to a Product {#boarding-update-product-api_section_r3n_f3r_y5b}
---------------------------------------------------------------------------

Product fields are in the selectedProducts object. Include the field for the product you are adding, and set `subscriptionInformation.enabled` field for that product to `true`
***Product Features***
Some products also have a `features` block within the `subscriptionInformation` object that gives you the ability to enable features of a product.

```
"subscriptionInformation": {
  "enabled": true,
  "features": {
    "cardNotPresent": {
      "enabled": true
      },
    "cardPresent": {
      "enabled": true
      }
```

Configuring a Product {#boarding-update-product-api_section_s3n_f3r_y5b}
------------------------------------------------------------------------

Some products have a `configurationInformation` object that contains a `templateId` field and a `configurations` object.
The `templateId` field refers to a product configuration template that is already created in the `Business Center` and is required to configure a product using the Boarding API. If the `templateId` field is not submitted or is left blank, the default template for the account is used. For more information about templates, see [Product Templates](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro-templat-0.md "").
You can override product template values by submitting the `configurations` object.
***Configurations Object Example***

```
"configurationInformation": {
 "templateId": "A57EB750-6543-46A5-83BE-CCA38D9C9083",
 "configurations": {
   "common": {
     "defaultAuthTypeCode": "final",
     "foodAndConsumerServiceId": "1234",
     "enablePartialAuth": true,
     "useParentTransactionAmountForFollowOn": false,
     "merchantCategoryCode": "1234",
     "processors": {
       "processorName": {
         "batchGroup": "processorname_batch_00",
         "acquirer": {
           "interbankCardAssociationId": "20490",
           "discoverInstitutionId": "666666",
           "institutionId": "432870",
           "fileDestinationBin": "432870",
           "countryCode": "840_usa"
           },
         "merchantId": "20003791",
         "terminalId": "yD9mP42e",
         "sicCode": "1234",
         "allowMultipleBills": true,
         "fireSafetyIndicator":false,
         "quasiCash":false,
         "paymentTypes":{
           "VISA": {"enabled": true}, "MASTERCARD": {"enabled": true},"AMERICAN_EXPRESS": {"enabled": true},"CUP": {"enabled": true},"JCB": {"enabled": true},"DISCOVER": {"enabled": true},"FALABELLA_PLCC": {"enabled": true},"COSTCO_PLCC": {"enabled": true},"DINERS_CLUB": {"enabled": true}
           },
         "currencies": {
           "USD": {"enabled": true }
         }
         }
       }
     },
     "features": {
       "cardNotPresent": {
         "ignoreAddressVerificationSystem": true,
         "processors": {
           "gpx": {
             "relaxAddressVerificationSystem":true,
             "relaxAddressVerificationSystemAllowZipWithoutCountry":true,
             "relaxAddressVerificationSystemAllowExpiredCard":false,
             "visaSTPOnly":false,
             "enableEmsTransactionRiskScore":false
             }
```

Required Fields for Adding a New Products {#boarding-update-product-api-req-fields}
===================================================================================

organizationId
:

\[productSectionName\].\[productName\].subscriptionInformation.enabled
:
For example, to enable payment subscription information, set the value of the payments.cardProcessing.subscriptionInformation.enabled, field to `true`.

Example: Adding a New Product to an Existing Organization Using the PECS API {#boarding-update-product-api-example}
===================================================================================================================

Request

```
{
  "organizationId": "ergaergaerg001",
  "commerceSolutions": {
    "tokenManagement": {
      "subscriptionInformation": {
        "enabled": true,
        "selfServiceability": "NOT_SELF_SERVICEABLE"
      },
      "configurationInformation": {
        "templateId": "43107BC1-E3DA-4019-9306-4510AD4DE05F"
      }
    }
  }
}
```

Response to a Successful Request

```
{
  "setups": {
    "commerceSolutions": {
      "tokenManagement": {
        "configurationStatus": {
          "status": "SUCCESS",
          "message": "Profile Assigned Successfully"
        },
        "subscriptionStatus": {
          "status": "SUCCESS",
          "message": "success"
        }
      }
    }
  },
  "status": "PROCESSED",
  "submitTimeUtc": "2022-06-03T08:46:13+0000"
}
```

Update Batch Group Using the PECS API {#pecs-update-batch}
==========================================================

This section shows you how to update a batch group.

Endpoint {#pecs-update-batch_d7e638}
------------------------------------

**Production:** `POST ``https://api.cybersource.com``/products/v1/product-setups`{#pecs-update-batch_d7e645}
**Test:** `POST ``https://apitest.cybersource.com``/products/v1/product-setups`{#pecs-update-batch_d7e655}

Required Fields for Updating a Batch Group Using the PECS API {#pecs-update-batch-req-fields}
=============================================================================================

Use these required fields to update the configuration of a product.

organizationId
:

payments.cardProcessing.configurationInformation.configurations.common. processors.\[processorName\].batchGroup
:
Where \[processorName\] is the payment processor.

payments.cardProcessing.configurationInformation.configurations.common. processors.\[processorName\].paymentTypes.\[paymentType\].enabled
:
Where \[processorName\] is the payment processor and \[paymentType\] is the payment type.

payments.cardProcessing.subscriptionInformation.enabled
:

payments.cardProcessing.subscriptionInformation.features.cardPresent.enabled
:

Example: Updating a Batch Group Using the API {#pecs-update-batch-ex}
=====================================================================

Request

```
{
  "payments": {
    "cardProcessing": {
      "subscriptionInformation": {
        "enabled": true,
        "features": {
          "cardPresent": {
            "enabled": true
          }
        }
      },
      "configurationInformation": {
        "configurations": {
          "common": {
            "processors": {
              "barclayshiso": {
                "paymentTypes": {
                  "VISA": {
                    "enabled": true
                  }
                },
                "batchGroup": "barclays_hiso_03"
              }
            }
          }
        }
      }
    }
  },
  "organizationId": "davestestguitarsaad009"
}
```

{#pecs-update-batch-ex_codeblock_ulf_bvh_jzb}
Response to a Successful Request

```
{
  "setups": {
    "payments": {
      "cardProcessing": {
        "configurationStatus": {
          "status": "SUCCESS",
          "message": "Configuration Instance updated successfully"
        },
        "subscriptionStatus": {
          "status": "SUCCESS",
          "message": "success"
        }
      }
    }
  },
  "status": "PROCESSED",
  "submitTimeUtc": "2023-11-14T06:33:34+0000"
}
```

{#pecs-update-batch-ex_codeblock_wlf_bvh_jzb}

Add a Processor Using the PECS API {#pecs-add-processor}
========================================================

This section shows you how to add a processor.

Endpoint {#pecs-add-processor_d7e638}
-------------------------------------

**Production:** `POST ``https://api.cybersource.com``/products/v1/product-setups`{#pecs-add-processor_d7e645}
**Test:** `POST ``https://apitest.cybersource.com``/products/v1/product-setups`{#pecs-add-processor_d7e655}

Required Fields for Adding a Processor Using the PECS API {#pecs-add-processor-req-fields}
==========================================================================================

Use these required fields to add an additional processor.

organizationId
:

payments.cardProcessing.configurationInformation.configurations.common.merchantCategoryCode
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.city
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.country
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.name
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.phone
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.zip
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.state
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.street
:

payments.cardProcessing.configurationInformation.configurations.common. processors.\[processorName\].currencies.\[currency\].serviceEnablementNumber
:
Where \[processorName\] is the payment processor and \[currency\] is the currency.

payments.cardProcessing.configurationInformation.features.cardNotPresent. processors.\[processorName\]relaxAddressVerificationSystem
:
Where \[processorName\] is the payment processor.

payments.cardProcessing.configurationInformation.features.cardNotPresent. processors.\[processorName\]relaxAddressVerificationSystemAllowExpiredCard
:
Where \[processorName\] is the payment processor.

payments.cardProcessing.configurationInformation.features.cardNotPresent. processors.\[processorName\]relaxAddressVerificationSystemAllowZipWithoutCountry
:
Where \[processorName\] is the payment processor.

payments.cardProcessing.configurationInformation.templateId
:

payments.cardProcessing.subscriptionInformation.enabled
:

Example: Adding a Processor Using the PECS API {#pecs-add-processor-ex}
=======================================================================

Request

```
{
  "organizationId": "cp_transacting1",
  "payments": {
    "cardProcessing": {
      "subscriptionInformation": {
        "enabled": true,
        "features": {
          "cardPresent": {
            "enabled": true
          }
        }
      },
      "configurationInformation": {
        "configurations": {
          "common": {
            "merchantCategoryCode": "5399",
            "merchantDescriptorInformation": {
              "city": "London",
              "country": "GBR",
              "name": "BCTest1",
              "phone": "1234567",
              "zip": "RG1 4BB",
              "state": "LN",
              "street": "Sample Street"
            },
            "processors": {
              "amexdirect": {
                "currencies": {
                  "GBP": {
                    "serviceEnablementNumber": "1234567891"
                  }
                }
              }
            }
          },
          "features": {
            "cardNotPresent": {
              "processors": {
                "amexdirect": {
                  "relaxAddressVerificationSystem": true,
                  "relaxAddressVerificationSystemAllowZipWithoutCountry": true,
                  "relaxAddressVerificationSystemAllowExpiredCard": true
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

{#pecs-add-processor-ex_codeblock_ulf_bvh_jzb}
Response to a Successful Request

```
{
    "setups": {
        "payments": {
            "cardProcessing": {
                "configurationStatus": {
                    "status": "SUCCESS",
                    "message": "Configuration Instance updated successfully"
                },
                "subscriptionStatus": {
                    "status": "SUCCESS",
                    "message": "success"
                }
            }
        }
    },
    "status": "PROCESSED",
    "submitTimeUtc": "2022-04-04T12:58:02+0000"
}
```

{#pecs-add-processor-ex_codeblock_wlf_bvh_jzb}

Delete a Processor Using the PECS API {#pecs-delete-processor}
==============================================================

This section shows you how to soft-delete a processor. All configuration settings are preserved but the processor is no longer visible in the API or the `Business Center`.

Endpoint {#pecs-delete-processor_d7e638}
----------------------------------------

**Production:** `POST ``https://api.cybersource.com``/products/v1/product-setups`{#pecs-delete-processor_d7e645}
**Test:** `POST ``https://apitest.cybersource.com``/products/v1/product-setups`{#pecs-delete-processor_d7e655}

Required Fields for Deleting a Processor Using the PECS API {#pecs-delete-processor-req-fields}
===============================================================================================

Use these required fields to delete a processor.

organizationId
:

payments.cardProcessing.configurationInformation.configurations. common.processors.\[processorName\].batchGroup
:
Where `[processorName]` is the payment processor.

payments.cardProcessing.configurationInformation.configurations. common.processors.\[processorName\].paymentTypes.\[paymentType\].enabled
:
Where \[processor\] is the payment processor and \[paymentTypes\] is the payment type.

    Set to `false`. IMPORTANT You must include this field for all card types configured for the processor.

payments.cardProcessing.subscriptionInformation.enabled
:

payments.cardProcessing.subscriptionInformation.features.cardNotPresent.enabled
:

payments.cardProcessing.subscriptionInformation.features.cardPresent.enabled
:

Example: Deleting a Processor Using the PECS API {#pecs-delete-processor-ex}
============================================================================

Request

```
{
    "payments": {
        "cardProcessing": {
            "subscriptionInformation": {
                "enabled": true,
                "features": {
                    "cardNotPresent": {
                        "enabled": true
                    },
                    "cardPresent": {
                        "enabled": false
                    }
                }
            },
            "configurationInformation": {
                "configurations": {
                    "common": {
                        "processors": {
                            "amexdirect": {
                                "paymentTypes": {
                                    "VISA": {
                                        "enabled": false
                                    },
                                     "MASTERCARD": {
                                        "enabled": false
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "organizationId": "amextestajtxmid1013"
}
```

{#pecs-delete-processor-ex_codeblock_ulf_bvh_jzb}
Response to a Successful Request

```
{
  "setups": {
    "payments": {
      "cardProcessing": {
        "configurationStatus": {
          "status": "SUCCESS",
          "message": "Configuration Instance updated successfully"
        },
        "subscriptionStatus": {
          "status": "SUCCESS",
          "message": "success"
        }
      }
    }
  },
  "status": "PROCESSED",
  "submitTimeUtc": "2023-11-14T06:40:15+0000"
}
```

{#pecs-delete-processor-ex_codeblock_wtf_m4g_lzb}

Add and Delete a Processor Using the PECS API {#pecs-add-delete-processor}
==========================================================================

This section shows you how to soft-delete a processor and add a new processor. All configuration settings are preserved but the processor is no longer visible in the API or the `Business Center`.

Endpoint {#pecs-add-delete-processor_d7e638}
--------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/products/v1/product-setups`{#pecs-add-delete-processor_d7e645}
**Test:** `POST ``https://apitest.cybersource.com``/products/v1/product-setups`{#pecs-add-delete-processor_d7e655}

Required Fields for Adding and Deleting a Processor Using the PECS API {#pecs-add-delete-processor-req-fields}
==============================================================================================================

Use these required fields to delete a processor.

organizationId
:

payments.cardProcessing.configurationInformation.configurations. common.processors.\[processorName\].batchGroup
:
Where `[processorName]` is the payment processor.

payments.cardProcessing.configurationInformation.configurations. common.processors.\[processorName\].paymentTypes.\[paymentType\].enabled
:
Where \[processor\] is the payment processor and \[paymentTypes\] is the payment type.

    Set to `false`. IMPORTANT You must include this field for all card types configured for the processor.

payments.cardProcessing.subscriptionInformation.enabled
:

payments.cardProcessing.subscriptionInformation.features.cardNotPresent.enabled
:

payments.cardProcessing.subscriptionInformation.features.cardPresent.enabled
:

organizationId
:

payments.cardProcessing.configurationInformation.configurations.common.merchantCategoryCode
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.city
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.country
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.name
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.phone
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.zip
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.state
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.street
:

payments.cardProcessing.configurationInformation.configurations.common. processors.\[processorName\].currencies.\[currency\].serviceEnablementNumber
:
Where \[processorName\] is the payment processor and \[currency\] is the currency.

payments.cardProcessing.configurationInformation.features.cardNotPresent. processors.\[processorName\]relaxAddressVerificationSystem
:
Where \[processorName\] is the payment processor.

payments.cardProcessing.configurationInformation.features.cardNotPresent. processors.\[processorName\]relaxAddressVerificationSystemAllowExpiredCard
:
Where \[processorName\] is the payment processor.

payments.cardProcessing.configurationInformation.features.cardNotPresent. processors.\[processorName\]relaxAddressVerificationSystemAllowZipWithoutCountry
:
Where \[processorName\] is the payment processor.

payments.cardProcessing.configurationInformation.templateId
:

payments.cardProcessing.subscriptionInformation.enabled
:

Example: Adding and Deleting a Processor Using the PECS API {#pecs-add-delete-processor-ex}
===========================================================================================

Request

```
{
    "payments": {
        "cardProcessing": {
            "subscriptionInformation": {
                "enabled": true,
                "features": {
                    "cardNotPresent": {
                        "enabled": true
                    },
                    "cardPresent": {
                        "enabled": false
                    }
                }
            },
            "configurationInformation": {
                "configurations": {
                    "common": {
                        "processors": {
                            "amexdirect": {
                                "paymentTypes": {
                                    "VISA": {
                                        "enabled": false
                                    },
                                     "MASTERCARD": {
                                        "enabled": false
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "organizationId": "amextestajtxmid1013"
}
```

{#pecs-add-delete-processor-ex_codeblock_ulf_bvh_jzb}
Response to a Successful Request

```
{
  "setups": {
    "payments": {
      "cardProcessing": {
        "configurationStatus": {
          "status": "SUCCESS",
          "message": "Configuration Instance updated successfully"
        },
        "subscriptionStatus": {
          "status": "SUCCESS",
          "message": "success"
        }
      }
    }
  },
  "status": "PROCESSED",
  "submitTimeUtc": "2023-11-14T06:40:15+0000"
}
```

{#pecs-add-delete-processor-ex_codeblock_wtf_m4g_lzb}

`Payer Authentication` {#boarding-pecs-payer-auth}
==================================================

`Payer Authentication` uses the 3-D Secure protocol in online transactions to verify that payment is coming from the legitimate cardholder. Authenticating the payer before the transaction is authorized benefits the merchant by shifting chargeback liability from the merchant to the card issuer.

Prerequisites
-------------

You must meet these requirements to enable and configure `Payer Authentication` for your merchants:

* You must include a merchant website URL. 3-D Secure protocol requires that the website URL must be in the format `https://www.example.com`.
* You must include a merchant category code for your merchant.
* At least one 3-D Secure template must be available. For information on creating product templates, see [Product Templates](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro-template.md "").

Status
------

When you add Payer Authentication to a merchant account, one of these statuses is assigned:

* Boarded: The Payer Authentication configuration was successfully saved and the merchant can proceed to transact the card network using the specified currency.
* Pending: The Payer Authentication configuration is partially saved or incomplete. Raise a ticket with customer support.
  {#boarding-pecs-payer-auth_d16e53}

Configure `Payer Authentication` Using the PECS API {#pecs-config-payerauth}
============================================================================

This section shows you how to configure `Payer Authentication`.

Endpoint {#pecs-config-payerauth_d7e638}
----------------------------------------

**Production:** `POST ``https://api.cybersource.com``/products/v1/product-setups`{#pecs-config-payerauth_d7e645}
**Test:** `POST ``https://apitest.cybersource.com``/products/v1/product-setups`{#pecs-config-payerauth_d7e655}

Required Fields for Configuring `Payer Authentication` Using the PECS API {#pecs-config-payerauth-req-fields}
=============================================================================================================

Use these required fields to configure `Payer Authentication` for these card types.

American Express SafeKey-Specific Fields
----------------------------------------

Include these fields in addition to the required fields to enable and configure American Express SafeKey:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. amexSafeKey.currencies\[\].acquirerId
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. amexSafeKey.currencies\[\].currencyCodes\[\]
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. amexSafeKey.currencies\[\].processorMerchantId
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. amexSafeKey.enabled
:
Set to `true`.

Cartes Bancaires-Specific Fields
--------------------------------

Include these fields in addition to the required fields to enable and configure Cartes Bancaires:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. CB.currencies\[\].acquirerId
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. CB.currencies\[\].currencyCodes\[\]
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. CB.currencies\[\].processorMerchantId
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes.CB.enabled
:
Set to `true`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes.CB.requestorId
:

Discover/Diners Club ProtectBuy-Specific Fields
-----------------------------------------------

Include these fields in addition to the required fields to enable and configure Discover/Diners Club ProtectBuy:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. dinersClubInternationalProtectBuy.currencies\[\].acquirerId
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. dinersClubInternationalProtectBuy.currencies\[\].currencyCodes\[\]
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. dinersClubInternationalProtectBuy.currencies\[\].processorMerchantId
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. dinersClubInternationalProtectBuy.enabled
:
Set to `true`.

ELO-Specific Fields
-------------------

Include these fields in addition to the required fields to enable and configure ELO:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. ELO.currencies\[\].acquirerId
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. ELO.currencies\[\].currencyCodes\[\]
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. ELO.currencies\[\].processorMerchantId
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes.ELO.enabled
:
Set to `true`.

JCB J/Secure-Specific Fields
----------------------------

Include these fields in addition to the required fields to enable and configure JCB J/Secure:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. jCBJSecure.currencies\[\].acquirerId
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. jCBJSecure.currencies\[\].currencyCodes\[\]
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. jCBJSecure.currencies\[\].processorMerchantId
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. jCBJSecure.enabled
:
Set to `true`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. jCBJSecure.securePasswordForJCB
:

Mastercard/Meeza Identity Check-Specific Fields
-----------------------------------------------

Include these fields in addition to the required fields to enable and configure Mastercard/Meeza Identity Check:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. masterCardSecureCode.currencies\[\].acquirerId
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. masterCardSecureCode.currencies\[\].currencyCodes\[\]
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. masterCardSecureCode.currencies\[\].processorMerchantId
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. masterCardSecureCode.enabled
:
Set to `true`.

UnionPay 3-D Secure-Specific Fields
-----------------------------------

Include these fields in addition to the required fields to enable and configure UnionPay 3-D Secure:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. UPI.currencies\[\].acquirerId
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. UPI.currencies\[\].currencyCodes\[\]
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. UPI.currencies\[\].processorMerchantId
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. UPI.enabled
:
Set to `true`.

Visa Secure-Specific Fields
---------------------------

Include these fields in addition to the required fields to enable and configure Visa Secure:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. verifiedByVisa.currencies\[\].acquirerId
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. verifiedByVisa.currencies\[\].currencyCodes\[\]
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. verifiedByVisa.currencies\[\].processorMerchantId
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. verifiedByVisa.enabled
:
Set to `true`.

Example: Configuring Payer Authentication Using the PECS API {#pecs-config-payerauth-ex}
========================================================================================

Request to Configure American Express SafeKey

```
{"organizationId":"lrsebctest20001",
  "payments": {
    "payerAuthentication": {
      "configurationInformation": {
        "configurations": {
          "cardTypes": {
            "amexSafeKey": {
              "enabled": true,
              "currencies": [
                {
                  "currencyCodes": [
                    "ALL",
                    "978"
                  ],
                  "acquirerId": "acquirertest-1000",
                  "processorMerchantId": "procmerchtest"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

Request to Configure Cartes Bancaires

```
{
  "payments": {
    "payerAuthentication": {
      "configurationInformation": {
        "configurations": {
          "cardTypes": {
            "CB": {
              "requestorId": "reqtestid",
              "enabled": true,
              "currencies": [
                {
                  "currencyCodes": [
                    "ALL",
                    "978"
                  ],
                  "acquirerId": "acquirertest-1000",
                  "processorMerchantId": "procmerchtest"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

Request to Configure Discover/Diners Club ProtectBuy

```
{
  "payments": {
    "payerAuthentication": {
      "configurationInformation": {
        "configurations": {
          "cardTypes": {
            "dinersClubInternationalProtectBuy": {
              "enabled": true,
              "currencies": [
                {
                  "currencyCodes": [
                    "ALL",
                    "978"
                  ],
                  "acquirerId": "acquirertest-1000",
                  "processorMerchantId": "procmerchtest"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

Request to Configure ELO

```
{
  "payments": {
    "payerAuthentication": {
      "configurationInformation": {
        "configurations": {
          "cardTypes": {
            "ELO": {
              "enabled": true,
              "currencies": [
                {
                  "currencyCodes": [
                    "ALL",
                    "978"
                  ],
                  "acquirerId": "acquirertest-1000",
                  "processorMerchantId": "procmerchtest"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

Request to Configure JCB J/Secure

```
{
  "payments": {
    "payerAuthentication": {
      "configurationInformation": {
        "configurations": {
          "cardTypes": {
            "jCBJSecure": {
              "securePasswordForJCB": "testpassword",
              "enabled": true,
              "currencies": [
                {
                  "currencyCodes": [
                    "ALL",
                    "978"
                  ],
                  "acquirerId": "acquirertest-1000",
                  "processorMerchantId": "procmerchtest"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

Request to Configure Mastercard/Meeza Identity Check

```
{
  "payments": {
    "payerAuthentication": {
      "configurationInformation": {
        "configurations": {
          "cardTypes": {
            "masterCardSecureCode": {
              "enabled": true,
              "currencies": [
                {
                  "currencyCodes": [
                    "ALL",
                    "978"
                  ],
                  "acquirerId": "acquirertest-1000",
                  "processorMerchantId": "procmerchtest"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

Request to Configure UnionPay 3-D Secure

```
{
  "payments": {
    "payerAuthentication": {
      "configurationInformation": {
        "configurations": {
          "cardTypes": {
            "UPI": {
              "enabled": true,
              "currencies": [
                {
                  "currencyCodes": [
                    "ALL",
                    "978"
                  ],
                  "acquirerId": "acquirertest-1000",
                  "processorMerchantId": "procmerchtest"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

Request to Configure Visa Secure

```
{
  "payments": {
    "payerAuthentication": {
      "configurationInformation": {
        "configurations": {
          "cardTypes": {
            "verifiedByVisa": {
              "enabled": true,
              "currencies": [
                {
                  "currencyCodes": [
                    "ALL",
                    "978"
                  ],
                  "acquirerId": "acquirertest-1000",
                  "processorMerchantId": "procmerchtest"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

{#pecs-config-payerauth-ex_codeblock_ulf_bvh_jzb}
Response to a Successful Request

```
{
    "configurationId": "7593E16A-21D0-452E-8F7F-53805C1AE571",
    "submitTimeUtc": "2024-05-17T12:39:28Z",
    "status": "SUCCESS"
}
```

{#pecs-config-payerauth-ex_codeblock_wtf_m4g_lzb}For more information on response reason codes, see [Reason Codes](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-error-codes.md "").

`Token Management Service` {#boarding-pecs-tms}
===============================================

The `Token Management Service` (`TMS`) links tokens across service providers, payment types, and channels for sellers, acquirers, and technology partners. `TMS` tokenizes, securely stores, and manages the primary account number (PAN), the payment card expiration date, electronic check details, and customer data. `TMS` also enables merchants to create a network token of a customer's payment card.

> IMPORTANT
> When you board a merchant and enable ` TMS ` and network tokenization, the token requestor ID is enrolled at the merchant account organization level where the token vault is configured. You must include the merchant business information during token requestor ID enrollment and when you create the ` TMS ` token vault. This ensures that the network tokens that are provisioned are assigned to the merchant that owns the tokens.
> For more information on `TMS` and network tokenization, see [Token Vault Management](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-products-intro/boarding-tms/tms-vault-hierarchy.md "").

Enable `TMS` with a Template Using the PECS API {#boarding-pecs-tms-enable-intro}
=================================================================================

This section shows you how to enable `TMS` with a template.

Endpoint {#boarding-pecs-tms-enable-intro_d7e638}
-------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/products/v1/product-setups`{#boarding-pecs-tms-enable-intro_d7e645}
**Test:** `POST ``https://apitest.cybersource.com``/products/v1/product-setups`{#boarding-pecs-tms-enable-intro_d7e655}

Required Fields for Enabling `TMS` with a Template Using the PECS API {#boarding-pecs-tms-enable-reqfields}
===========================================================================================================

organizationId
:

commerceSolutions.tokenManagement.subscriptionInformation.enabled
:
Set to `true`.

commerceSolutions.tokenManagement.configurationInformation.templateId
:

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/api-fields-about-guide.md "")
  {#boarding-pecs-tms-enable-reqfields_ul_kpc_xzz_sxb}

REST Example: Enabling `TMS` with a Template Using the PECS API {#boarding-pecs-tms-enable-ex-rest}
===================================================================================================

Request

```
{
  "organizationId": "ergaergaerg001",
  "commerceSolutions": {
    "tokenManagement": {
      "subscriptionInformation": {
        "enabled": true,
        "selfServiceability": "NOT_SELF_SERVICEABLE"
      },
      "configurationInformation": {
        "templateId": "43107BC1-E3DA-4019-9306-4510AD4DE05F"
      }
    }
  }
}
```

Response to Successful Request

```
{
  "setups": {
    "commerceSolutions": {
      "tokenManagement": {
        "configurationStatus": {
          "status": "SUCCESS",
          "message": "Profile Assigned Successfully"
        },
        "subscriptionStatus": {
          "status": "SUCCESS",
          "message": "success"
        }
      }
    }
  },
  "status": "PROCESSED",
  "submitTimeUtc": "2022-06-03T08:46:13+0000"
}
```

Enable `TMS` and Enroll in Network Tokenization Using the PECS API {#boarding-pecs-tms-enable-intro}
====================================================================================================

This section shows you how to enable `TMS` and enroll in network tokenization.

Endpoint {#boarding-pecs-tms-enable-intro_d7e638}
-------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/products/v1/product-setups`{#boarding-pecs-tms-enable-intro_d7e645}
**Test:** `POST ``https://apitest.cybersource.com``/products/v1/product-setups`{#boarding-pecs-tms-enable-intro_d7e655}

Required Fields for Enabling `TMS` and Enrolling in Network Tokenization Using the PECS API {#boarding-tms-enable-net-tkn-reqfields}
====================================================================================================================================

commerceSolutions.tokenManagement.configurationInformation.configurations.vault.defaultTokenType
:

commerceSolutions.tokenManagement.configurationInformation.configurations.vault.location
:

commerceSolutions.tokenManagement.configurationInformation.configurations. vault.sensitivePrivileges.cardNumberMaskingFormat
:

commerceSolutions.tokenManagement.configurationInformation.configurations.vault.tokenFormats.customer
:

commerceSolutions.tokenManagement.configurationInformation.configurations. vault.tokenFormats.instrumentIdentifierBankAccount
:

commerceSolutions.tokenManagement.configurationInformation.configurations.vault.tokenFormats.instrumentIdentifierCard
:

commerceSolutions.tokenManagement.configurationInformation.configurations.vault.tokenFormats.paymentInstrument
:

commerceSolutions.tokenManagement.configurationInformation.configurations.networkTokenEnrollment.acquirer.acquirerId
:

commerceSolutions.tokenManagement.configurationInformation.configurations. networkTokenEnrollment.acquirer.acquirerMerchantId
:

commerceSolutions.tokenManagement.configurationInformation.configurations. networkTokenEnrollment.businessInformation.address.country
:

commerceSolutions.tokenManagement.configurationInformation.configurations. networkTokenEnrollment.businessInformation.address.locality
:

commerceSolutions.tokenManagement.configurationInformation.configurations. networkTokenEnrollment.businessInformation.doingBusinessAs
:

commerceSolutions.tokenManagement.configurationInformation.configurations. networkTokenEnrollment.businessInformation.name
:

commerceSolutions.tokenManagement.configurationInformation.configurations. networkTokenEnrollment.networkTokenServices.mastercardDigitalEnablementService.enrollment
:
Set to `true`.

commerceSolutions.tokenManagement.configurationInformation.configurations. networkTokenEnrollment.networkTokenServices.visaTokenService.enrollment
:
Set to `true`.

commerceSolutions.tokenManagement.configurationInformation.configurations.networkTokenEnrollment.websiteUrl
:

commerceSolutions.tokenManagement.configurationInformation.configurations. networkTokenServices.mastercardDigitalEnablementService.enableService
:
Set to `true`.

commerceSolutions.tokenManagement.configurationInformation.configurations. networkTokenServices.mastercardDigitalEnablementService.enableTransactionalTokens
:
Set to `true`.

commerceSolutions.tokenManagement.configurationInformation.configurations.networkTokenServices.notifications.enabled
:

commerceSolutions.tokenManagement.configurationInformation.configurations. networkTokenServices.paymentCredentials.enabled
:

commerceSolutions.tokenManagement.configurationInformation.configurations. networkTokenServices.visaTokenService.enableService
:
Set to `true`.

commerceSolutions.tokenManagement.configurationInformation.configurations. networkTokenServices.visaTokenService.enableTransactionalTokens
:
Set to `true`.

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/api-fields-about-guide.md "")
  {#boarding-tms-enable-net-tkn-reqfields_ul_kpc_xzz_sxb}

REST Example: Enabling `TMS` and Enrolling in Network Tokenization Using the PECS API {#boarding-pecs-tms-enable-ex-rest}
=========================================================================================================================

Request

```
{
  "organizationId": "ergaergaerg001",
  "commerceSolutions": {
    "tokenManagement": {
      "subscriptionInformation": {
        "enabled": true
      },
      "configurationInformation": {
        "configurations": {
          "vault": {
            "location": "GDC",
            "defaultTokenType": "CUSTOMER",
            "tokenFormats": {
              "customer": "32_HEX",
              "paymentInstrument": "32_HEX",
              "instrumentIdentifierCard": "19_DIGIT_LAST_4",
              "instrumentIdentifierBankAccount": "32_HEX"
            },
            "sensitivePrivileges": {
              "cardNumberMaskingFormat": "FIRST_6_LAST_4"
            }
          },
          "networkTokenEnrollment": {
            "businessInformation": {
              "name": "TokenMerchant",
              "doingBusinessAs": "NetworkTokenCo1",
              "address": {
                "country": "US",
                "locality": "ORMOND BEACH"
              },
              "websiteUrl": "https://www.MerchantUrlHere.com",
              "acquirer": {
                "acquirerId": "40010052242",
                "acquirerMerchantId": "yourmerchantorgidhere"
              }
            },
            "networkTokenServices": {
              "visaTokenService": {
                "enrollment": true
              },
              "mastercardDigitalEnablementService": {
                "enrollment": true
              }
            }
          },
          "networkTokenServices": {
            "notifications": {
              "enabled": true
            },
            "paymentCredentials": {
              "enabled": true
            },
            "visaTokenService": {
              "enableService": true,
              "enableTransactionalTokens": true
            },
            "mastercardDigitalEnablementService": {
              "enableService": true,
              "enableTransactionalTokens": true
            }
          }
        }
      }
    }
  }
}
```

Response to Successful Request

```
{
  "setups": {
    "commerceSolutions": {
      "tokenManagement": {
        "configurationStatus": {
          "status": "SUCCESS",
          "message": "Profile Assigned Successfully"
        },
        "subscriptionStatus": {
          "status": "SUCCESS",
          "message": "success"
        }
      }
    }
  },
  "status": "PROCESSED",
  "submitTimeUtc": "2022-06-03T08:46:13+0000"
}
```

Extending the Hierarchy {#boarding-extend-hierarchy}
====================================================

The Boarding service enables you to build a hierarchy to model your actual business structure or the business structures of your merchants if you are a reseller. You can board a small hierarchy of organizations using only merchant and transacting organizations. You can also use structural organizations to extend the hierarchy. Extending the hierarchy is optional.
Structural organizations can be placed under merchant organizations to represent things like different types of payment systems, different geographical regions, or any other distinction that your business needs. Transacting organizations are then placed under the structural organizations.

Hierarchy Example {#boarding-extend-hierarchy-diagram}
======================================================

In this diagram of a relatively simple hierarchy, a merchant organization has two structural organizations: one for eCommerce, and one for physical store locations. Transacting organizations are added under the structural organizations. This is an example of using structural organizations to represent card-not-present transactions (online transactions) and card-present transactions (physical store locations). The Stores node has two physical locations that process payments. The eCommerce node has one transacting organization, which represents a payment form on a website.

#### Figure: {#boarding-extend-hierarchy-diagram_fig_zgk_hgy_r5b}

Hierarchy Example ![](/content/dam/new-documentation/documentation/en-us/topics/platform/bam/boarding-user/images/create-merchant-hierarchy.svg/jcr:content/renditions/original)

Add a Structural Organization to a Merchant Organization {#boarding-reg-create-structural-api}
==============================================================================================

Use these instructions to create a structural account using the API.

Endpoint {#boarding-reg-create-structural-api_d7e665}
-----------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/boarding/v1/registrations`{#boarding-reg-create-structural-api_d7e672}
**Test:** `POST ``https://apitest.cybersource.com``/boarding/v1/registrations`{#boarding-reg-create-structural-api_d7e682}

Required Fields for Boarding a Structural Organization {#boarding-reg-create-structural-api-req-fields}
=======================================================================================================

organizationInformation.businessInformation.name
:

organizationInformation.configurable
:
Set the value to `false`.

organizationInformation.parentOrganizationId
:
Set to the ID of the organization that you want to be above this one in the hierarchy.

organizationInformation.status
:

organizationInformation.type
:
Set the value to `STRUCTURAL`.

registrationInformation.boardingFlow
:
Set the value to `ENTERPRISE`.

REST Example: Creating a Structural Organization {#boarding-reg-create-structural-api-example}
==============================================================================================

Request

```
{
    "registrationInformation": {
        "boardingFlow": "ENTERPRISE"
    },
    "organizationInformation": {
        "organizationId": "yourstructuralorgidhere",
        "status": "LIVE",
        "parentOrganizationId": "yourmercahntorgidhere",
        "type": "STRUCTURAL",
        "configurable": false,
        "businessInformation": {
            "address": {
                "country": "US",
                "address1": "123 Main",
                "postalCode": "99999",
                "administrativeArea": "WA",
                "locality": "Seattle"
            },
            "businessContact": {
                "firstName": "Jane",
                "lastName": "Smith",
                "phoneNumber": "5551234567",
                "email": "email@domain.com"
            },
            "technicalContact": {
                "firstName": "Jane",
                "lastName": "Smith",
                "phoneNumber": "5551234567",
                "email": "email@domain.com"
            },
            "emergencyContact": {
                "firstName": "Jane",
                "lastName": "Smith",
                "phoneNumber": "5551234567",
                "email": "email@domain.com"
            },
            "name": "Test Merchant",
            "websiteUrl": "https://www.MerchantUrlHere.com",
            "phoneNumber": "5551234567",
            "timeZone": "America/Los_Angeles",
            "merchantCategoryCode": "5999"
        }
    }
}
```

Response to a Successful Request

```
{
    "id": "1695804002",
    "submitTimeUtc": "2022-04-13T20:58:28Z",
    "status": "SUCCESS",
    "registrationInformation": {
        "mode": "COMPLETE",
        "boardingPackageId": "123456789012"
    },
    "organizationInformation": {
        "organizationId": "yourstructuralorgidhere",
        "parentOrganizationId": "yourmercahntorgidhere"
    },
    "message": "Request was processed successfully"
}
```

ISO Standard Currency Codes {#currency-codes}
=============================================

Not all currencies are supported for all processors.

| Currency Code | Numerical Currency Code | Currency Name                                                                                                                        | Decimal Places |
|:--------------|-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| AED           | 784                     | United Arab Emirates dirham                                                                                                          | 2              |
| AFN           | 971                     | Afghanistan afghani                                                                                                                  | 2              |
| ALL           | 008                     | Albanian lek                                                                                                                         | 2              |
| AMD           | 051                     | Armenian dram                                                                                                                        | 2              |
| ANG           | 532                     | Netherlands Antillean guilder                                                                                                        | 2              |
| AOA           | 973                     | Angola kwanza                                                                                                                        | 2              |
| ARS           | 032                     | Argentine peso                                                                                                                       | 2              |
| AUD           | 036                     | Australian dollar                                                                                                                    | 2              |
| AWG           | 533                     | Aruban guilder                                                                                                                       | 2              |
| AZN           | 944                     | Azerbaijanian manat                                                                                                                  | 2              |
| BAM           | 977                     | Bosnia and Herzegovina convertible mark                                                                                              | 2              |
| BBD           | 052                     | Barbados dollar                                                                                                                      | 2              |
| BDT           | 050                     | Bangladeshi taka                                                                                                                     | 2              |
| BGN           | 975                     | Bulgarian lev                                                                                                                        | 2              |
| BHD           | 048                     | Bahraini dinar                                                                                                                       | 3              |
| BIF           | 108                     | Burundian franc                                                                                                                      | 0              |
| BMD           | 060                     | Bermuda dollar                                                                                                                       | 2              |
| BND           | 096                     | Brunei dollar                                                                                                                        | 2              |
| BOB           | 068                     | Bolivian boliviano                                                                                                                   | 2              |
| BOV           | 984                     | Bolivian mvdol                                                                                                                       | 2              |
| BRL           | 986                     | Brazilian real                                                                                                                       | 2              |
| BSD           | 044                     | Bahamian dollar                                                                                                                      | 2              |
| BTN           | 064                     | Bhutani ngultrum                                                                                                                     | 2              |
| BWP           | 072                     | Botswana pula                                                                                                                        | 2              |
| BYR           | 933                     | Belarussian ruble BYR has been replaced by BYN as the Belarussian ruble currency.                                                    | 0              |
| BYN           | 933                     | Belarussian ruble                                                                                                                    | 2              |
| BZD           | 084                     | Belize dollar                                                                                                                        | 2              |
| CAD           | 124                     | Canadian dollar                                                                                                                      | 2              |
| CDF           | 976                     | Congolese franc                                                                                                                      | 2              |
| CHF           | 756                     | Swiss franc                                                                                                                          | 2              |
| CLF           | 990                     | Chilean unidad de fomento                                                                                                            | 4              |
| CLP           | 152                     | Chilean peso                                                                                                                         | 0              |
| CNY           | 156                     | Chinese yuan renminbi                                                                                                                | 2              |
| COP           | 170                     | Columbian peso                                                                                                                       | 2              |
| COU           | 970                     | Columbian unidad de valor real                                                                                                       | 2              |
| CRC           | 188                     | Costa Rican colon                                                                                                                    | 2              |
| CSK           | 203                     | Czech koruna                                                                                                                         | 2              |
| CUC           | 931                     | Cuban peso, convertible                                                                                                              | 2              |
| CUP           | 192                     | Cuban peso                                                                                                                           | 2              |
| CVE           | 132                     | Cape Verde escudo                                                                                                                    | 2              |
| CZK           | 203                     | Czech koruna                                                                                                                         | 2              |
| DJF           | 262                     | Djiboutian franc                                                                                                                     | 0              |
| DKK           | 208                     | Danish krone                                                                                                                         | 2              |
| DOP           | 214                     | Dominican peso                                                                                                                       | 2              |
| DZD           | 012                     | Algerian dinar                                                                                                                       | 2              |
| EGP           | 818                     | Egyptian pound                                                                                                                       | 2              |
| ERN           | 232                     | Eritrean nakfa                                                                                                                       | 2              |
| ETB           | 230                     | Ethiopian birr                                                                                                                       | 2              |
| EUR           | 978                     | Euro                                                                                                                                 | 2              |
| FJD           | 242                     | Fiji dollar                                                                                                                          | 2              |
| FKP           | 238                     | Falkland Islands pound                                                                                                               | 2              |
| GBP           | 826                     | British pound sterling                                                                                                               | 2              |
| GEL           | 981                     | Georgian lari                                                                                                                        | 2              |
| GHS           | 936                     | Ghana cedi                                                                                                                           | 2              |
| GIP           | 292                     | Gibraltar pound                                                                                                                      | 2              |
| GMD           | 270                     | Gambian dalasi                                                                                                                       | 2              |
| GNF           | 324                     | Guinean franc                                                                                                                        | 0              |
| GTQ           | 320                     | Guatemalan quetzal                                                                                                                   | 2              |
| GWP           |                         | Guinea-Bissau peso                                                                                                                   | 0              |
| GYD           | 328                     | Guyanese dollar                                                                                                                      | 2              |
| HKD           | 344                     | Hong Kong dollar                                                                                                                     | 2              |
| HNL           | 340                     | Hunduran Lempira                                                                                                                     | 2              |
| HTG           | 332                     | Haitian gourde                                                                                                                       | 2              |
| HUF           | 348                     | Hungarian forint                                                                                                                     | 2              |
| IDR           | 360                     | Indonesian rupiah                                                                                                                    | 2              |
| ILS           | 376                     | Israeli sheqel                                                                                                                       | 2              |
| INR           | 356                     | Indian rupee                                                                                                                         | 2              |
| IQD           | 368                     | Iraqi dinar                                                                                                                          | 3              |
| IRR           | 364                     | Iranian rial                                                                                                                         | 2              |
| ISK           | 352                     | Icelandic krona                                                                                                                      | 0              |
| JMD           | 388                     | Jamaican dollar                                                                                                                      | 2              |
| JOD           | 400                     | Jordanian dinar                                                                                                                      | 3              |
| JPY           | 392                     | Japanese yen                                                                                                                         | 0              |
| KES           | 404                     | Kenyan shilling                                                                                                                      | 2              |
| KGS           | 417                     | Kyrgyzstani som                                                                                                                      | 2              |
| KHR           | 116                     | Cambodian riel                                                                                                                       | 2              |
| KMF           | 174                     | Comoro franc                                                                                                                         | 0              |
| KPW           | 408                     | North Korean won                                                                                                                     | 2              |
| KRW           | 410                     | South Korean won                                                                                                                     | 0              |
| KWD           | 414                     | Kuwaiti dinar                                                                                                                        | 3              |
| KYD           | 136                     | Cayman Islands dollar                                                                                                                | 2              |
| KZT           | 398                     | Kazakhstani tenge                                                                                                                    | 2              |
| LAK           | 418                     | Lao kip                                                                                                                              | 2              |
| LBP           | 422                     | Lebanese pound                                                                                                                       | 2              |
| LKR           | 144                     | Sri Lanka rupee                                                                                                                      | 2              |
| LRD           | 430                     | Liberian dollar                                                                                                                      | 2              |
| LSL           | 426                     | Lesotho loti                                                                                                                         | 2              |
| LTL           |                         | Lithuanian litas                                                                                                                     | 2              |
| LVL           |                         | Latvian lats                                                                                                                         | 2              |
| LYD           | 434                     | Libyan dinar                                                                                                                         | 3              |
| MAD           | 504                     | Moroccan dirham                                                                                                                      | 2              |
| MDL           | 498                     | Moldovan leu                                                                                                                         | 2              |
| MGA           | 969                     | Malagasy ariary                                                                                                                      | 2              |
| MKD           | 807                     | Macedonian denar                                                                                                                     | 2              |
| MMK           | 104                     | Myanmar kyat                                                                                                                         | 2              |
| MNT           | 496                     | Mongolian tugrik                                                                                                                     | 2              |
| MOP           | 446                     | Macanese pataca                                                                                                                      | 2              |
| MRO           |                         | Mauritanian ouguiya                                                                                                                  | 2              |
| MUR           | 480                     | Mauritius rupee                                                                                                                      | 2              |
| MVR           | 462                     | Maldivian rufiyaa                                                                                                                    | 2              |
| MWK           | 454                     | Malawian kwacha                                                                                                                      | 2              |
| MXN           | 484                     | Mexican peso                                                                                                                         | 2              |
| MYR           | 458                     | Malaysian ringgit                                                                                                                    | 2              |
| MZN           | 943                     | Mozambican metical                                                                                                                   | 2              |
| NAD           | 516                     | Namibian dollar                                                                                                                      | 2              |
| NGN           | 566                     | Nigerian naira                                                                                                                       | 2              |
| NIO           | 558                     | Cordoba oro                                                                                                                          | 2              |
| NOK           | 578                     | Norwegian krone                                                                                                                      | 2              |
| NPR           | 524                     | Nepalese rupee                                                                                                                       | 2              |
| NZD           | 554                     | New Zealand dollar                                                                                                                   | 2              |
| OMR           | 512                     | Omani rial                                                                                                                           | 3              |
| PAB           | 590                     | Panamanian balboa                                                                                                                    | 2              |
| PEN           | 604                     | Peruvian nuevo sol                                                                                                                   | 2              |
| PGK           | 598                     | Papua New Guinean kina                                                                                                               | 2              |
| PHP           | 608                     | Philippine peso                                                                                                                      | 2              |
| PKR           | 586                     | Pakistan rupee                                                                                                                       | 2              |
| PLN           | 985                     | Polish zloty                                                                                                                         | 2              |
| PYG           | 600                     | Paraguayan guarani                                                                                                                   | 0              |
| QAR           | 634                     | Qatari rial                                                                                                                          | 2              |
| RON           | 946                     | Romanian leu                                                                                                                         | 2              |
| RSD           | 941                     | Serbian dinar                                                                                                                        | 2              |
| RUB           | 643                     | Russian ruble                                                                                                                        | 2              |
| RWF           | 646                     | Rwanda franc                                                                                                                         | 0              |
| SAR           | 682                     | Saudi Arabian riyal                                                                                                                  | 2              |
| SBD           | 090                     | Solomon Islands dollar                                                                                                               | 2              |
| SCR           | 690                     | Seychelles rupee                                                                                                                     | 2              |
| SDG           | 938                     | Sudanese pound                                                                                                                       | 2              |
| SEK           | 752                     | Swedish krona                                                                                                                        | 2              |
| SGD           | 702                     | Singapore dollar                                                                                                                     | 2              |
| SHP           | 654                     | Saint Helena pound                                                                                                                   | 2              |
| SLE           | 925                     | Sierra Leonean leone > IMPORTANT > Effective **October 1, 2022** , the ` SLL ` currency code is valid only for exemption processing. | 2              |
| SOS           | 706                     | Somali shilling                                                                                                                      | 2              |
| SRD           | 968                     | Surinamese dollar                                                                                                                    | 2              |
| SSP           | 728                     | South Sudanese pound                                                                                                                 | 2              |
| STD           |                         | Sao Tome and Principe dobra                                                                                                          | 2              |
| SVC           | 222                     | El Salvadorean colon                                                                                                                 | 2              |
| SYP           | 760                     | Syrian pound                                                                                                                         | 2              |
| SZL           | 784                     | Swaziland lilangeni                                                                                                                  | 2              |
| THB           | 764                     | Thai baht                                                                                                                            | 2              |
| TJS           | 972                     | Tajikistani somoni                                                                                                                   | 2              |
| TMT           | 934                     | Turkmenistan new manat                                                                                                               | 2              |
| TND           | 788                     | Tunisian dinar                                                                                                                       | 3              |
| TOP           | 776                     | Tongan pa'anga                                                                                                                       | 2              |
| TRY           | 949                     | Turkish lira                                                                                                                         | 2              |
| TTD           | 780                     | Trinidad and Tobago dollar                                                                                                           | 2              |
| TWD           | 901                     | Taiwan dollar                                                                                                                        | 2              |
| TZS           | 834                     | Tanzanian shilling                                                                                                                   | 2              |
| UAH           | 980                     | Ukrainian hryvnia                                                                                                                    | 2              |
| UGX           | 800                     | Ugandan shilling                                                                                                                     | 2              |
| USD           | 840                     | United States dollar                                                                                                                 | 2              |
| UYU           | 858                     | Uruguayan peso                                                                                                                       | 2              |
| UZS           | 860                     | Uzbekistan som                                                                                                                       | 2              |
| VEF           | 937                     | Venezuelan bolivar fuerte                                                                                                            | 2              |
| VND           | 704                     | Vietnamese dong                                                                                                                      | 0              |
| VUV           | 548                     | Vanuatu vatu                                                                                                                         | 0              |
| WST           | 882                     | Samoan tala                                                                                                                          | 2              |
| XAF           | 950                     | CFA franc BEAC (Central African CFA franc)                                                                                           | 0              |
| XCD           | 951                     | East Caribbean dollar                                                                                                                | 2              |
| XOF           | 952                     | CFA Franc BCEAO (West African CFA franc)                                                                                             | 0              |
| XPF           | 953                     | CFP franc                                                                                                                            | 0              |
| YER           | 886                     | Yemeni rial                                                                                                                          | 2              |
| ZAR           | 710                     | South African rand                                                                                                                   | 2              |
| ZMK           |                         | Zambian kwacha                                                                                                                       | 2              |
| ZMW           | 967                     | Zambian kwacha                                                                                                                       | 2              |
| ZWD           |                         | Zimbabwean dollar                                                                                                                    | 2              |
| ZWL           | 932                     | Zimbabwean dollar                                                                                                                    | 2              |

Reason Codes {#boarding-error-codes}
====================================

These tables list the reason codes and the possible status and reason values that are returned with the response from the Boarding Registration Service (BRS) API and the Product Enablement and Configuration Service (PECS) API. `Cybersource` reserves the right to add new reason codes at any time. If your error handler receives a reason code that it does not recognize, it should use the decision field to determine the result.

BRS API Reason Codes
--------------------

| Reason Code | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200         | Successful. Possible status values: * `PROCESSING`: The registration is still in progress. You can get the latest status by calling the `GET` endpoint using the registration ID. * `SUCCESS`: The request was successful. * `FAILURE`: The registration failed before the organization was created. Refer to the details section in the response for more information. * `PARTIAL`: The registration created the organization successfully but failed in at least on step while configuring it. Refer to the details section in the response for more information. |
| 400         | Bad request. Possible reason values: * `INVALID_DATA` * `SYSTEM_ERROR` * `RESOURCE_NOT_FOUND`                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 422         | Business validations failed. Possible reason values: * `INVALID_DATA`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 500         | Internal server error. Possible reason values: * `SYSTEM_ERROR `                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
[Reason Codes]

Example: Partial Processed Response from the BRS API
----------------------------------------------------

```
{
  "id": "87373503001",
  "submitTimeUtc": "2023-11-16T22:15:02Z",
  "status": "PARTIAL",
  "registrationInformation": {
    "mode": "COMPLETE",
    "boardingPackageId": "15118503001"
  },
  "organizationInformation": {
    "organizationId": "davescustomguitars067",
    "parentOrganizationId": "davescustomguitars"
  },
  "message": "Request was processed successfully",
  "productInformationSetups": [
    {
      "organizationId": "davescustomguitars067",
      "setups": {
        "payments": {
          "cardProcessing": {
            "configurationStatus": {
              "status": "FAILURE",
              "reason": "INVALID_REQUEST",
              "details": [
                {
                  "field": "name",
                  "reason": "/configurations/common/merchantDescriptorInformation/name should contain only alphabets and numeric characters."
                }
              ],
              "message": "Field validation errors"
            },
            "subscriptionStatus": {
              "status": "SUCCESS",
              "message": "success"
            }
          },
          "digitalPayments": {
            "subscriptionStatus": {
              "status": "SUCCESS",
              "message": "success"
            }
          }
        },
        "risk": {
          "fraudManagementEssentials": {
            "configurationStatus": {
              "status": "SUCCESS"
            },
            "subscriptionStatus": {
              "status": "SUCCESS",
              "message": "success"
            }
          }
        },
        "valueAddedServices": {
          "transactionSearch": {
            "subscriptionStatus": {
              "status": "SUCCESS",
              "message": "success"
            }
          },
          "reporting": {
            "subscriptionStatus": {
              "status": "SUCCESS",
              "message": "success"
            }
          }
        }
      }
    }
  ]
}
```

PECS API Reason Codes
---------------------

| Reason Code | Description                                                                                                                                                                                                                                                           |
|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200         | Successful Possible status values: * `PROCESSED`: The request was successful. * `PARTIAL_PROCESSED`: An error occurred and the configuration settings were not updated for one or more products. {#boarding-error-codes_ul_yxh_5sm_lzb}                               |
| 400         | Invalid request Possible status value: * `INVALID_REQUEST` {#boarding-error-codes_ul_mcj_wsm_lzb} Possible reason values: * `MANDATORY_FIELD_MISSING` * `BUSINESS_VALIDATION_FAILED` * `INVALID_VALUE` {#boarding-error-codes_ul_xq2_ssm_lzb}                         |
| 401         | Unauthorized Possible status value: * `UN_AUTHENTICATED` {#boarding-error-codes_ul_urd_ysm_lzb} Possible reason values: * `INVALID_API_KEY` * `UNSUPPORTED_ORG` * `INVALID_ORG_HIERARCHY` {#boarding-error-codes_ul_cx1_msm_lzb}                                      |
| 403         | Forbidden Possible status value: * `UN_AUTHENTICATED` {#boarding-error-codes_ul_n45_zsm_lzb} Possible reason values: * `INVALID_API_KEY ` * `UNSUPPORTED_ORG` * `INVALID_ORG_HIERARCHY` {#boarding-error-codes_ul_qjm_3sm_lzb}                                        |
| 404         | Not found Possible status value: * `NOT_FOUND` {#boarding-error-codes_ul_b4s_btm_lzb} Possible reason value: * `NOT_FOUND` {#boarding-error-codes_ul_apq_hsm_lzb}                                                                                                     |
| 502         | Bad gateway Possible status value: * `BAD_GATEWAY` {#boarding-error-codes_ul_aqr_ctm_lzb} Possible reason values: * `SYSTEM_ERROR` * `SERVER_TIMEOUT` * `SERVICE_TIMEOUT ` * `INVALID_OR_MISSING_CONFIG` * `PROCESSOR_TIMEOUT` {#boarding-error-codes_ul_bdj_2sm_lzb} |
[Reason Codes]

Example: Partial Processed Response from the PECS API
-----------------------------------------------------

```
{
  "setups": {
    "payments": {
      "cardProcessing": {
        "configurationStatus": {
          "status": "FAILURE",
          "reason": "INVALID_REQUEST",
          "details": [
            {
              "field": "paymentTypes",
              "reason": "MASTERCARD,VISA are invalid paymentTypes in /configurations/common/processors/amexdirect/paymentTypes"
            }
          ],
          "message": "Field validation errors"
        },
        "subscriptionStatus": {
          "status": "SUCCESS",
          "message": "success"
        }
      }
    }
  },
  "status": "PARTIAL_PROCESSED",
  "submitTimeUtc": "2023-11-14T06:36:44+0000"
}
```

{#boarding-error-codes_codeblock_wlf_bvh_jzb}

Add Merchant Account Information {#boarding-merchants-v2-add-merch-acct-info}
=============================================================================

Follow these steps to add merchant account information:

1. In Basic Information, enter the merchant account name and the organization ID in the provided text fields.

   #### ADDITIONAL INFORMATION

   * The merchant account name is the name of the business.
   * The organization ID is the name or identifier of the account that you are creating. It must be unique, not just in the portfolio or account, but in the system.
2. Enter the merchant information in the provided text fields. Required fields are noted with an asterisk (\*).

3. Click **Save** . You are returned to the Add Merchant page. You can skip the optional hierarchy step by clicking **Skip**.

REST Example: Creating a Transacting Organization with Integration Information {#boarding-reg-create-transacting-integ-api-example}
===================================================================================================================================

Request with Integration Information

```
{
  "registrationInformation": {
    "boardingFlow": "ENTERPRISE",
    "mode": "COMPLETE",
    "boardingPackageId": "16885604124"
  },
  "organizationInformation": {
    "status": "LIVE",
    "businessInformation": {
      "address": {
        "country": "GB",
        "address1": "Sample Street 1234",
        "locality": "London",
        "postalCode": "98765"
      },
      "businessContact": {
        "firstName": "Test",
        "lastName": "Test",
        "phoneNumber": "123456789",
        "email": "test@test.com"
      },
      "technicalContact": {
        "firstName": "Test",
        "lastName": "Test",
        "phoneNumber": "123456789",
        "email": "test@test.com"
      },
      "emergencyContact": {
        "firstName": "Test",
        "lastName": "Test",
        "phoneNumber": "123456789",
        "email": "test@test.com"
      },
      "name": "Test 4",
      "websiteUrl": "",
      "phoneNumber": "123456789",
      "timeZone": "GMT",
      "merchantCategoryCode": "5399"
    },
    "parentOrganizationId": "cptesting06",
    "type": "TRANSACTING",
    "configurable": false
  },
  "integrationInformation": {
    "tenantConfigurations": [
      {
        "solutionId": "wrqgaz3e",
      }
    ]
  },
  "productInformation": {
    "selectedProducts": {
      "payments": {
        "cardProcessing": {
          "subscriptionInformation": {
            "enabled": true,
            "features": {
              "cardNotPresent": {
                "enabled": false
              },
              "cardPresent": {
                "enabled": true
              }
            }
          },
          "configurationInformation": {
            "configurations": {
              "common": {
                "merchantCategoryCode": "5399",
                "defaultAuthTypeCode": "FINAL",
                "processors": {
                  "barclayshiso": {
                    "acquirer": {},
                    "paymentTypes": {
                      "MAESTRO": {
                        "enabled": true
                      },
                      "MASTERCARD": {
                        "enabled": true
                      },
                      "DISCOVER": {
                        "enabled": true
                      },
                      "JCB": {
                        "enabled": true
                      },
                      "VISA": {
                        "enabled": true
                      },
                      "VISA_ELECTRON": {
                        "enabled": true
                      },
                      "DINERS_CLUB": {
                        "enabled": true
                      },
                      "CUP": {
                        "enabled": true
                      }
                    },
                    "batchGroup": "barclayshiso_test",
                    "merchantId": "1234567",
                    "terminalId": null
                  }
                }
              },
              "features": {
                "cardNotPresent": {
                  "processors": {
                    "barclayshiso": {
                      "relaxAddressVerificationSystem": true,
                      "relaxAddressVerificationSystemAllowExpiredCard": true,
                      "relaxAddressVerificationSystemAllowZipWithoutCountry": true
                    }
                  }
                }
              }
            },
            "templateId": "F4EEFE3C-ED8C-4937-A48A-C013B228488E"
          }
        },
        "cybsReadyTerminal": {
          "subscriptionInformation": {
            "enabled": true,
            "selfServiceability": "NOT_SELF_SERVICEABLE"
          }
        }
      },
      "risk": {},
      "commerceSolutions": {},
      "valueAddedServices": {}
    }
  }
}
```

Response to a Successful Request

```
{
  "id": "12351234",
  "submitTimeUtc": "2023-06-11T22:47:57.000Z",
  "status": "SUCCESS",
  "registrationInformation": {
    "mode": "COMPLETE",
    "boardingPackageId": "16885604124"
  },
  "organizationInformation": {
    "organizationId": "cptesting061830",
    "parentOrganizationId": "cptesting06"
  },
  "integrationInformation": {
    "tenantConfigurations": [
      {
        "solutionId": "YumSolution1",
        "tenantConfigurationId": "id1234",
        "status": "LIVE",
        "submitTimeUtc": "2019-08-24T14:15:22Z"
      }
    ]
  },
  "message": "Request was processed succesfully.",
  "details": {}
}
```

Product Templates {#boarding-intro-template}
============================================

A product template enables and configures a product and is applied to more transacting organizations. Product templates are created in the `Business Center` by an administrator user. Before you board a transacting organization, you must create a product template for each product that you will assign to it. Not every product support templates.
You will apply product templates to a transacting organization when you create it. You can also create multiple templates for a product, configured differently, and decide which one to apply to a transacting organization, depending on the organization's needs.
Templates can be modified at any time; however, organizations that already have the template applied do not inherit the modifications. Modifying a template only affects new organizations that you apply to it.
For product-level boarding information, see the [Product Boarding Template Reference](/docs/cybs/en-us/boarding/developer/all/rest/boarding/templates-matrix-intro.md "").
Partners can use various boarding templates to customize merchant onboarding and meet the business needs of each merchant.
A boarding template is a collection of predefined attributes and rules that an acquirer (bank), technical partner, or merchant uses to board merchants onto their platform. Boarding templates help automate the entire boarding process by packaging all of the required information needed to board merchants. You can use templates to reduce the manual steps and time it takes for merchant accounts to start processing payments.
Templates also allow an acquirer or partner to make configuration changes to individual and multiple merchants in the portfolio.
You can use a boarding template to initialize or make changes to any of the following:

* Accounts
* Transacting nodes
* Structural nodes
