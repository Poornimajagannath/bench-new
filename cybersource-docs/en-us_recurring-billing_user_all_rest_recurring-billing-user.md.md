Recurring Billing User Guide {#doctemp-about-guide}
===================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This guide is written for merchants who use the upgraded or new Recurring Billing service that is available through the `Business Center` and the REST API.

Conventions
:
This statement appears in this document:

    > IMPORTANT
    > An *Important* statement contains information essential to successfully completing a task or learning a concept.

Related Documentation
:
Visit the [`Cybersource` documentation hub](https://developer.cybersource.com/docs.md "") to find additional technical documentation.

Customer Support
:
For support information about any service, visit the Support Center:

<http://support.visaacceptance.com>

Recent Revisions to This Document {#recurring-billing-user-doc-revisions}
=========================================================================

26.04.01
--------

Added the [Skip Payments within a Subscription](/docs/cybs/en-us/recurring-billing/user/all/rest/recurring-billing-user/manage-subscriptions/skip-payment.md "") topic.

25.11.01
--------

Added new section [Recurring Billing Settings](/docs/cybs/en-us/recurring-billing/user/all/rest/recurring-billing-user/olh-recurring-billing-settings.md "").  
Added new section [Reactivate a Suspended Subscription](/docs/cybs/en-us/recurring-billing/user/all/rest/recurring-billing-user/manage-subscriptions/reactivate-subscription.md "").

25.09.01
--------

This revision contains only editorial changes and no technical updates.

25.06.01
--------

Updated information about the amount of time allowed between subscription payments in these sections:

* [Create a Follow-On Subscription from an Existing Transaction](/docs/cybs/en-us/recurring-billing/user/all/rest/recurring-billing-user/manage-subscriptions/create-subscriptions-follow-on-cust-token.md "")
* [Create a Subscription](/docs/cybs/en-us/recurring-billing/user/all/rest/recurring-billing-user/manage-subscriptions/create-subscriptions.md "")
* [Create a Plan](/docs/cybs/en-us/recurring-billing/user/all/rest/recurring-billing-user/manage-plans/create-plan.md "")

25.05.01
--------

Added a new section. See [Create a Follow-On Subscription from an Existing Transaction](/docs/cybs/en-us/recurring-billing/user/all/rest/recurring-billing-user/manage-subscriptions/create-subscriptions-follow-on-cust-token.md "").  
Updated the graphic in this section:

* [Managing Subscriptions](/docs/cybs/en-us/recurring-billing/user/all/rest/recurring-billing-user/manage-subscriptions.md "")
  {#recurring-billing-user-doc-revisions_ul_zrk_dfm_w2c}

24.09.01
--------

This revision contains only editorial changes and no technical updates.

Introduction to Recurring Billing {#recur-bill-services-intro}
==============================================================

This guide explains how to use the Recurring Billing service in the `Business Center`.  
Recurring Billing is also available using the REST API. For information about REST, see the `Cybersource` [Hello world sandbox](https://developer.cybersource.com/hello-world.md "") at the Developer Center.  
The Recurring Billing service enables you to create and manage payment plans and subscriptions for recurring payment schedules. It automates the storage and handling of your customer's payment information and personal data within secure Visa data centers in compliance with credentials-on-file (COF) best practices. Storage risks and the PCI DSS scope are reduced through the use of the `Token Management Service` (`TMS`).  
`Cybersource` Recurring Billing consists of these three elements:

* **Plan:** Stores the billing schedule.
* **Subscription:** Combines the token and plan and defines the subscription start date, name, and description.
* **Token:** Stores customer billing, shipping, and payment details.  
  For information on Recurring Billing for developers, see the [*Recurring Billing Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-dev-intro.md "").

Recurring Billing Settings {#olh-recurring-billing-settings}
============================================================

Recurring Billing settings are available to users with administrative or settings permissions. The Recurring Billing settings permission is called *View or manage settings under Recurring Billing* . This setting can be configured in **Account Management \&gt; Roles** by creating a new role or editing a role.

Notification Settings
---------------------

Follow these steps to configure Recurring Billing to send email notifications to your customers:

1. Log in to the `Business Center`.
2. In the left-navigation menu, choose **Recurring Billing \&gt; Manage Subscriptions** or **Recurring Billing \&gt; Manage Plans**.
3. Click the ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/recurring-billing/images/settings-icon.png/jcr:content/renditions/original) **Settings** button in the upper-right corner of the page. The Settings page opens.
4. Click the **Notifications** tab to email notifications for your customers about recurring payments.
5. Click the box labeled **Yes, send the customer notifications**. The email types are displayed on the right side of the page.
   {#olh-recurring-billing-settings_ol_wdr_51p_ghc}

> IMPORTANT Some mandates require customer notification. If notifications are not enabled, the merchant is responsible for sending notifications in accordance with mandate requirements.

Reactivation Settings
---------------------

Follow these steps to configure the Recurring Billing reactivation payment settings:
1. Log in to the `Business Center`.
2. In the left-navigation menu, choose **Recurring Billing \&gt; Manage Subscriptions** or **Recurring Billing \&gt; Manage Plans**.
3. Click the ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/recurring-billing/images/settings-icon.png/jcr:content/renditions/original) **Settings** button in the upper-right corner of the page. The Settings page opens.
4. Click the **Payments** tab to use the reactivation payment settings.  
   These settings enable you to choose to process the payments that were missed during the time the subscription was in a SUSPEND status, due to failed payment or merchant action.

Managing Plans {#manage-plans}
==============================

You can search plans using these filters:

* Plan code
* Plan name
* Plan status
  {#manage-plans_ul_srx_jkx_r4b}  
  Only plans with an *ACTIVE* status can be attached to a subscription.

Create a Plan {#create-plan}
============================

A plan consists of this information:

* Plan code: generated by the Recurring Billing service (default) or assigned by the merchant.
* Plan name
* Plan description
* Plan ID: generated by the Recurring Billing service.
* Billing amount
* Currency: assigned when the plan is created.
* Billing period: the length and calendar unit of the billing frequency, which cannot exceed a 12-month period.
* Billing cycle options: indefinite, or a defined billing end period.
* Set-up fee: 0.00 if not included when the plan is created.

{#create-plan_ul_lnn_rkx_r4b}  
Follow these steps to create a plan:

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.cybersource.com`](https://businesscentertest.cybersource.com/ebc2/ "")
   * **Production:** [`https://businesscenter.cybersource.com`](https://businesscenter.cybersource.com/ebc2/ "")
     {#create-plan_ebc-login}
     {#create-plan_ebc-login}
2. On the left navigation panel, choose ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-recur-bill.png/jcr:content/renditions/original) **Recurring Billing \&gt; Manage Plans \&gt; Add New Plan**. The Create Plan page appears.
3. Click **`Manage Plans`**. The Manage Plans page appears.
4. Click **Add New Plan**.
5. Enter this information:
   1. Plan code: generated automatically when not assigned by the merchant.
   2. Plan name
   3. Plan description (optional)
   4. Billing amount
   5. Currency
   6. Billing period length
   7. Billing period unit
6. Choose the billing cycle by choosing one of these options:
   * Bill indefinitely.
   * Define billing period end and enter the plan period length. The plan period unit defaults to the same length as the billing period length.
7. Enter the set-up fee (optional).
8. Click **Save as Draft** or **Submit**. The Manage Plans page appears.

View a Plan {#view-plan}
========================

You can search for any plan by the plan code, plan name, or plan status. You can activate, deactivate, or delete the plan on the View Plan page.  
Follow these steps to view or change the status of a plan:

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.cybersource.com`](https://businesscentertest.cybersource.com/ebc2/ "")
   * **Production:** [`https://businesscenter.cybersource.com`](https://businesscenter.cybersource.com/ebc2/ "")
2. On the left navigation panel, click ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-recur-bill.png/jcr:content/renditions/original) **Recurring Billing**.
3. Click **`Manage Plans`**. The Manage Plans page appears.
4. To search for plans, click **Add a Filter** , and then select **Plan Code** , **Plan Name** , or **Plan Status**.
5. Enter the exact plan code, name, or status, and press **Enter**. Matching search results display in the list.
6. To view the details for a plan, click the plan code. The Plan Details page appears.
7. To change the status of the plan, choose one of these options:
   * Click **Activate Plan** . You can activate a plan that has a *DRAFT* or *INACTIVE* status.
   * Click **Deactivate Plan**.
   * Click **Delete Plan** . You can delete a plan that has a *DRAFT* status or that has an *ACTIVE* or *INACTIVE* status and has never been assigned to a subscription.
     {#view-plan_choices_zbc_c3x_r4b}

Edit a Plan {#update-plan}
==========================

Follow these steps to edit a plan:

1. Log in to the `Business Center`:

   * **Test:** [`https://businesscentertest.cybersource.com`](https://businesscentertest.cybersource.com/ebc2/ "")
   * **Production:** [`https://businesscenter.cybersource.com`](https://businesscenter.cybersource.com/ebc2/ "")
2. On the left navigation panel, click ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-recur-bill.png/jcr:content/renditions/original) **Recurring Billing**.

3. Click **`Manage Plans`**. The Manage Plans page appears.

4. Click the plan code. The Plan Details page appears.

5. Click **Edit**. The Edit Plan Page appears.

6. Make changes to the plan.

7. Under Plan Change - Subscription Update, choose **New Subscriptions Only** or **All (New and Existing)**.

8. Click **Save**. The Plan Details page appears.

   #### ADDITIONAL INFORMATION

   This information can be edited:

   * Plan code
   * Plan name
   * Plan description
   * Billing amount
   * Set-up fee
   * Subscription update: change the plan for all new and existing or only new subscriptions.
     {#update-plan_ul_pnc_zmx_r4b}

Managing Subscriptions {#manage-subscriptions}
==============================================

You can manage subscriptions in `Manage Subscriptions` and `Token Management` areas of the `Business Center`.

#### Figure:

Subscription Flow ![](/content/dam/documentation/cybs/en-us/olh/RecurringBilling/images/subscription-status-flow-600x450.svg/jcr:content/renditions/original)  
A subscription always has one of these statuses:

Pending
:
The first payment is scheduled, or the subscription is in transition to another state.

Active
:
The subscription is currently in use. It is set with a payment instrument, and a payment is scheduled at a pre-determined frequency that you agreed upon with your customer.

Delinquent
:
When a scheduled recurring payment fails, the account is placed in a Delinquent status while the system retries the payment a number of times. If the retries all fail, the account is placed into a Suspended status.

Suspended
:
The automated retry logic failed to obtain successful payment, or you have explicitly suspended the subscription. In order to resume a suspended subscription for the next billing cycle, choose one of these options:

    * Collect a different payment method from your customer and then reactivate the subscription.
    * Cancel the subscription and create a new subscription for your customer.

Cancelled
:
You have explicitly cancelled the subscription, and it cannot be reactivated. You might cancel an active or pending subscription when you and the customer agree to end the subscription. You might choose to cancel a delinquent subscription rather than wait for the automatic retry logic to proceed. You might cancel a suspended subscription if the customer does not have an acceptable alternate payment method.
> IMPORTANT You cannot cancel a subscription within 10 minutes before or after a payment begins processing.

Completed
:
All scheduled payments were made. This is the state of a subscription that ends with all scheduled payments successfully completed. This state applies to subscriptions set up with a scheduled end date.
> IMPORTANT You cannot reactivate a completed subscription.

{#manage-subscriptions_dl_v53_cdm_y2c}

> IMPORTANT
> For information about managing subscriptions from the ` Token Management ` area in the ` Business Center `, see [Managing Subscriptions in Token Management](/docs/cybs/en-us/recurring-billing/user/all/rest/recurring-billing-user/manage-subscriptions-tms.md "").

Search for Subscriptions {#manage-subscriptions-rb}
===================================================

When you manage subscriptions from the `Manage Subscriptions` area in the `Business Center`, you can search for them using these filters:

* Subscription code
* First name
* Last name
* Plan name
* Subscription status

Create a Subscription {#create-subscriptions}
=============================================

You can add a differential fee when you create a subscription. The surcharge amount is added to the billing amount when the recurring payment is processed. Before including a surcharge in your subscription, refer to your local regulations for compliance on surcharging customers, and confirm that your processor supports surcharges.  
Follow these steps to create a subscription with an existing plan:

1. Log in to the `Business Center`:

   * **Test:** [`https://businesscentertest.cybersource.com`](https://businesscentertest.cybersource.com/ebc2/ "")
   * **Production:** [`https://businesscenter.cybersource.com`](https://businesscenter.cybersource.com/ebc2/ "")
2. On the left navigation panel, click ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-tkn-mgmt.svg/jcr:content/renditions/original) **`Token Management`**. The Token Management page appears.

3. Click **`Tokens`**. The Token List page appears.

4. Click the token ID for which you want to create a subscription.

5. Click **Create Subscription**. The Create Subscription page appears.

6. Under Subscription Information, enter this information:

   * Subscription code: generated by the Recurring Billing service (default) or assigned by the merchant
   * Subscription name
   * Start date (payment processing time starts at 2:00 a.m. in your time zone.)
     {#create-subscriptions_ul_vyj_1rr_p4b}
7. Under Plan Options, choose an existing active plan or **New One Time Plan**.  
   The customer's payment and billing information appear.

8. Under Billing Details, enter or edit this information:

   * Billing amount
   * Currency
   * Billing period length
   * Billing period unit
   * Set-up fee (optional)

   {#create-subscriptions_ul_y51_dgz_r4b} IMPORTANT The interval between subscription payments cannot exceed 12 months.

9. Edit or enter the billing cycle by choosing one of these options:

   * Bill indefinitely.
   * Define billing period end and enter the plan period length. The plan period unit defaults to the same length as the billing period length.
10. Under Differential Fee, enter this information:

    * Surcharge amount
    * Surcharge description
11. Click **Submit**. The Token Management Customer Details page appears.

12. Click the **Subscriptions** tab, and view the new subscription in the subscriptions list.

Create a Subscription with an Existing Customer Token {#create-subscriptions-cust-token}
========================================================================================

Follow these steps to create a subscription with an existing plan and an existing customer token:

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.cybersource.com`](https://businesscentertest.cybersource.com/ebc2/ "")
   * **Production:** [`https://businesscenter.cybersource.com`](https://businesscenter.cybersource.com/ebc2/ "")
2. On the left navigation panel, choose ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-recur-bill.png/jcr:content/renditions/original) Recurring Billing \&gt; `Manage Subscriptions`.
3. Click **Create Subscription**.
4. Select **Existing Customer**. The Create Subscription page appears.
5. Enter the customer first and last name, and then click **Search**.
6. Find the customer in the results and click **Select**. The payment and shipping address details are pre-populated. The Subscription Details panel appears.
7. Enter these subscription details:
   * Subscription name
   * Start date (payment processing time starts at 2:00 a.m. in your time zone.)
   * Subscription code
   * (Optional) Merchant Reference Number: the value that you enter will be used as the Merchant Reference Number for all subscription payments. If no value is provided, the system will automatically generate a random number for each subsequent payment.
     {#create-subscriptions-cust-token_ul_xns_3xn_zsb}
8. Select a subscription billing plan, and then click **Apply**. The billing details appear.
9. Click **Change** to edit these billing details:
   * Billing amount
   * Billing cycles
   * Set-up fee
     {#create-subscriptions-cust-token_ul_ehn_kf4_zsb}
10. Click **Create Now** , and then click **Yes, create** to create the new subscription with the new customer token.
11. Click the **Subscriptions** tab and view the new subscription in the subscriptions list.

Create a Subscription with a New Customer Token {#create-subscriptions-new-cust-token}
======================================================================================

Create a subscription with a new customer token. Only plans with an *ACTIVE* status can be attached to a subscription.

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.cybersource.com`](https://businesscentertest.cybersource.com/ebc2/ "")
   * **Production:** [`https://businesscenter.cybersource.com`](https://businesscenter.cybersource.com/ebc2/ "")
2. On the left navigation panel, choose ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-recur-bill.png/jcr:content/renditions/original) Recurring Billing \&gt; `Manage Subscriptions`.
3. Click **Create Subscription**.
4. Choose **New Customer** , and then click **Continue**. The Create Subscription page appears.
5. Enter customer details.
6. Add merchant-defined data fields, if necessary.
7. Click **Continue**. The Payment Details panel appears.
8. Choose the payment method, and then click **Apply**.
9. Enter these card details:
   * Card type
   * Card number
   * Expiration date
   * Currency
10. Enter these billing address details:
    * First name
    * Last name
    * Company (optional)
    * Country
    * Address
    * Apartment, suite, floor, building, etc. (optional)
    * City
    * State/province
    * Postal code
    * Email
    * Phone (optional)
      {#create-subscriptions-new-cust-token_ul_vxf_5vn_zsb}
11. Click **Continue**. The Shipping Address Details panel appears.
12. Click **Yes** to edit shipping address details.
13. Click **Continue**.
14. Enter these subscription details:
    * Subscription name
    * Start date (payment processing time starts at 2:00 a.m. in your time zone.)
    * Subscription code
    * (Optional) Merchant Reference Number: the value that you enter will be used as the Merchant Reference Number for all subscription payments. If no value is provided, the system will automatically generate a random number for each subsequent payment.
      {#create-subscriptions-new-cust-token_ul_xns_3xn_zsb}
15. Choose a subscription billing plan, and then click **Apply**. The billing details appear.
16. Click **Change** to edit these billing details:
    * Billing amount
    * Billing cycles
    * Set-up fee
      {#create-subscriptions-new-cust-token_ul_ehn_kf4_zsb}
17. Click **Create Now** , and then click **Yes, create** to create the new subscription with the new customer token.
18. Click the **Subscriptions** tab, and view the new subscription in the subscriptions list.

Create a Follow-On Subscription from an Existing Transaction {#create-subscriptions-follow-on-cust-token}
=========================================================================================================

This method eliminates the need to create a new customer token or search for an existing one.  
You can use an existing plan that has *ACTIVE* status or you can use a one-time plan to set up the subscription.  
You can add a differential fee to a subscription using the surcharge amount and surcharge description fields when you create a subscription. You add the surcharge amount to the billing amount when you process the recurring payment.

> IMPORTANT
> Before including a surcharge in your subscription, refer to your local regulations for compliance on surcharging customers, and confirm that your processor supports surcharges.  
> Follow these steps to create a follow-on subscription from an existing transaction:

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.cybersource.com`](https://businesscentertest.cybersource.com/ebc2/ "")
   * **Production:** [`https://businesscenter.cybersource.com`](https://businesscenter.cybersource.com/ebc2/ "")
2. On the left navigation panel, click ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-trxn-mgmt.svg/jcr:content/renditions/original) Transaction Management.
3. Click Transactions. The Transactions List page appears.
4. Search for a successful transaction from the past using filters.
5. Click the request ID of a transaction from which you want to create a subscription. The Transaction Details page appears.
6. Click Actions and then select Create Subscription. The Create Subscription page appears.

   > IMPORTANT
   > The Action button appears only when the transaction is successful.

7. The system populates the customer, payments, and shipping address details with the transaction data.
8. Under Subscription Details, enter this information:
   * Subscription name
   * Start date (payment processing time starts at 2:00 a.m. in your time zone)
   * Subscription code (generated by the default Recurring Billing service or assigned by the merchant)
     {#create-subscriptions-follow-on-cust-token_ul_h5t_x2x_s2c}
9. Choose a subscription billing plan. You can choose an existing active plan or create a new one-time plan.
10. Click Apply.
11. If you selected a new one-time plan, you must complete these billing details:
    * Currency
    * Billing amount
    * Billing frequency. Choose one of the predefined options or click Custom to create your own. Enter the billing period length (number) and billing period unit. The interval between subscription payments cannot exceed 12 months.
    * Billing cycle options (a bill indefinitely subscription continues without a defined end date until it is manually cancelled by the merchant).
    * Number of billing cycles (enter a number in the billing cycles field).
      {#create-subscriptions-follow-on-cust-token_ul_dps_bhx_s2c}
12. (Optional) Enter a set-up fee, which is an amount that is added to the first payment.
13. (Optional) Enter a differential fee:
    * Enter the surcharge amount. Click Calculate to automatically calculate an amount.
    * Enter the surcharge description.
14. Click Create Now. The Subscription Details page appears.
    {#create-subscriptions-follow-on-cust-token_steps_cps_bhx_s2c}

View a Subscription {#view-subscriptions}
=========================================

You can view subscription details, including payment history and the next scheduled payment.  
Follow these steps to view a subscription:

1. Log in to the `Business Center`:

   * **Test:** [`https://businesscentertest.cybersource.com`](https://businesscentertest.cybersource.com/ebc2/ "")
   * **Production:** [`https://businesscenter.cybersource.com`](https://businesscenter.cybersource.com/ebc2/ "")
2. On the left navigation panel, choose ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-recur-bill.png/jcr:content/renditions/original) Recurring Billing \&gt; `Manage Subscriptions`. The Manage Subscriptions page appears.

3. To search for subscriptions, click **Add a Filter**, and choose one of these filters:

   #### ADDITIONAL INFORMATION

   * Subscription code
   * First name
   * Last name
   * Plan name
   * Subscription status
     {#view-subscriptions_ul_zvp_hdq_ghc}
4. Enter the exact information. Search results appear in the list.

5. To view the details for a subscription, click the subscription code. The Subscription Details page appears.
   {#view-subscriptions_steps_ov2_msy_r4b}

Edit a Subscription {#update-subscriptions}
===========================================

You can add a differential fee to a subscription using the **Surcharge Amount** and **Surcharge Description** fields when you create a subscription. The surcharge amount is added to the billing amount when the recurring payment is processed. Before including a surcharge in your subscription, refer to your local regulations for compliance on surcharging customers, and confirm that your processor supports surcharges.  
Follow these steps to edit a subscription:

1. Log in to the `Business Center`:

   * **Test:** [`https://businesscentertest.cybersource.com`](https://businesscentertest.cybersource.com/ebc2/ "")
   * **Production:** [`https://businesscenter.cybersource.com`](https://businesscenter.cybersource.com/ebc2/ "")
2. On the left navigation panel, choose ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-recur-bill.png/jcr:content/renditions/original) Recurring Billing \&gt; `Manage Subscriptions`. The Manage Subscriptions page appears.

3. Find the subscription and click the subscription code. The Subscription Details page appears.

4. Click **Edit**. The Edit Subscription page appears.

5. To change the status of the subscription, click **Suspend Subscription** or **Cancel Subscription**.

6. To edit the subscription, click **Edit**.

7. Edit any of these options:

   #### ADDITIONAL INFORMATION

   * Subscription code
   * Subscription name
   * Plan option
   * Billing amount
8. Click **Update**. The Subscription Details page appears.

Reactivate a Suspended Subscription {#reactivate-subscription}
==============================================================

You can reactivate a suspended subscription for the next billing cycle.  
Follow these steps to reactivate a subscription:

1. In the `Business Center`, navigate to **Recurring Billing** \&gt; **Manage Subscriptions**. The Manage Subscriptions page opens.
2. Find the subscription and click the subscription code. The Subscription Details page opens.
3. To reactivate the subscription, click **Change Status** and then select **Reactivate**. The confirmation window appears.
4. Depending on the reactivation settings:
   1. **Ask each time before reactivating** : the system will display information about the number and total monetary amount of missed payments that occurred when the subscription was in a suspended state. You can then choose one of these options:
      1. **Process missed payments and fees**: processes the transactions that were missed when the subscription was suspended.
      2. **Only process future payments**: does not process the transactions that were missed when the subscription was suspended.
         {#reactivate-subscription_ol_fjk_w4f_fhc}
   2. **Always process all missed payments**: the system will display information about the number and total monetary amount of missed payments that occurred when the subscription was in a suspended state
   3. **Don't process any missed payments**: the system will display a total amount equal to 0.00.
      {#reactivate-subscription_ol_oym_v4f_fhc}
5. Click **Reactivate**.
   {#reactivate-subscription_ol_n53_h4f_fhc}

Skip Payments within a Subscription {#skip-payment}
===================================================

There are two ways that you can stop and restart subscription payments:

* Use the Suspend function to pause subscription payments. You can reactivate payments at any time and choose whether to retry any payments that were missed while the subscription was suspended.
* When the period of skipped payments is known, you can choose the Skip option from the Subscription Details Page. The instructions are below.  
  You can skip a single payment or set of future payments. Follow these steps to skip a payment:

1. In the Business Center, navigate to **Recurring Billing \&gt; Manage Subscriptions**. The Manage Subscriptions page opens.
2. Find the subscription and click the subscription code. The Subscription Details page opens.
3. To Skip a scheduled payment within the subscription, navigate to the scheduled payments and click the **Skip** option next to the date of the payment that you would like skipped. The confirmation window appears.

A skipped payment can be restored by following step 3 and clicking **Restore** instead of skip.
IMPORTANT The payment cannot be added to the list if it is a retry attempt. The payment cannot be added to or removed from the list if it is on the same day as its scheduled processing time.

Managing Subscriptions in `Token Management` {#manage-subscriptions-tms}
========================================================================

When you manage subscriptions from the `Token Management` area in the `Business Center`, you can search tokens using these filters:

* Date Range
* Card Expiration
* Email
* Card Number
* Token ID
* Zip/Postal Code
* Last Name
* First Name
* Merchant Defined
* Account Number
* Payment Account Reference

{#manage-subscriptions-tms_ul_vmn_4rr_zsb} IMPORTANT

> Due to mandates from the Reserve Bank of India, Indian merchants cannot store personal account numbers (PANs). Use network tokens instead.  
> For more information on network tokens, see the Network Tokenization section of the [` Token Management Service ` Developer Guide .](https://developer.cybersource.com/docs/vas/en-us/tms/developer/ctv/rest/tms/tms-net-tkn-onboard.md "")

Create a Customer Token {#create_cust_token}
============================================

The token represents customer-related information including details for a payment card or electronic check, billing address, shipping address, and merchant-defined data.

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.cybersource.com`](https://businesscentertest.cybersource.com/ebc2/ "")
   * **Production:** [`https://businesscenter.cybersource.com`](https://businesscenter.cybersource.com/ebc2/ "")
2. On the left navigation pane, click ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-tkn-mgmt.svg/jcr:content/renditions/original) **`Token Management`**.
3. Click **Customers**. The Customers page appears.
4. Click **Create token**. The Create Customer page opens.
5. Under Customer Details, enter:
   1. Reference: a name for the customer token.
   2. Email: email address for the customer.
   3. Description: description of the customer token.
6. Under Payment Information, enter:
   1. Currency.
   2. Payment type.
   3. Account information for the selected payment type.
7. Enter the billing information for the customer.
8. Enter the shipping information for the customer. If it is the same as billing information, check the **Same as Billing Information** box.
9. (Optional) Enter any merchant-defined data fields.
10. Click **Save**.

View a Subscription in Token Management {#view-subscriptions-tms}
=================================================================

You can view subscription details, including payment history and the next scheduled payment. Use these filters to search for subscriptions:

* Subscription code
* First name
* Last name
* Plan name
* Subscription status

Follow these steps to view a subscription in the Token Management area of the Business Center:

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.cybersource.com`](https://businesscentertest.cybersource.com/ebc2/ "")
   * **Production:** [`https://businesscenter.cybersource.com`](https://businesscenter.cybersource.com/ebc2/ "")
2. On the left navigation panel, click ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-tkn-mgmt.svg/jcr:content/renditions/original) **`Token Management`**. The Token Management page appears.
3. Click **`Tokens`**. The Token List page appears.
4. To view the details for a subscription, click the token ID. The Subscription Details page appears.
   {#view-subscriptions-tms_steps_ov2_msy_r4b}

Edit a Subscription in Token Management {#update-subscriptions-tms}
===================================================================

You can add a differential fee when you create a subscription. The surcharge amount is added to the billing amount when the recurring payment is processed. Before including a surcharge in your subscription, refer to your local regulations for compliance on surcharging customers, and confirm that your processor supports surcharges.

> IMPORTANT Before including a surcharge in your subscription, refer to your local regulations for compliance on surcharging customers, and confirm that your processor supports surcharges.
> Follow these steps to edit a subscription in Token Management:

1. Log in to the `Business Center`:

   * **Test:** [`https://businesscentertest.cybersource.com`](https://businesscentertest.cybersource.com/ebc2/ "")
   * **Production:** [`https://businesscenter.cybersource.com`](https://businesscenter.cybersource.com/ebc2/ "")
2. On the left navigation panel, click ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-tkn-mgmt.svg/jcr:content/renditions/original) **`Token Management`**.

3. Click **`Tokens`**. The Token List page appears.

4. Check the box for the token ID. The Token Details page appears.

5. Click the **Subscriptions** tab.

6. Click the subscription code. The Subscription Details page appears.

7. Click **Edit**. The Edit Subscription page appears.

8. To change the status of the subscription, click **Suspend Subscription** or **Cancel Subscription**.

9. To edit the subscription, click **Edit**.

10. Edit any of these sections:

    #### ADDITIONAL INFORMATION

    * Subscription code
    * Subscription name
    * Plan option
    * Billing amount
      {#update-subscriptions-tms_ul_h2z_p3x_r4b}
11. Click **Update**. The Subscription Details page appears.

VISA Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Visa Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Visa/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER VISA NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Visa Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER VISA NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Visa Platform Connect ACQUIRER.
