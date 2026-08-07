Recurring Billing Developer Guide {#recur-bill-about-guide}
===========================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This guide is for merchants who use the upgraded or new `Cybersource` Recurring Billing service. The service is available through the `Business Center` and the REST API.

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

<http://support.example.com>

Recent Revisions to This Document {#recur-bill-recentrevisions_RecentRevisions}
===============================================================================

26.05.01
--------

Added these sections:

* [Retrieving a List of Payments in a Subscription](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/retrieve-list-payments-in-sub.md "")
* [Skipping or Restoring Payments Within a Subscription](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/skip-restore-payment.md "")

25.11.01
--------

Added information about the merchant reference number in these sections:

* [Subscriptions](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions.md "")

* [Retrieving a List of Subscriptions](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/recur-bill-getting-all-subscriptions.md "")

* [Retrieving a Subscription](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/recur-bill-getting-a-subscription.md "")

* [Amendable Fields](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/rb-amend-subs/rb-amend-subs-amend-fields.md "")
  {#recur-bill-recentrevisions_ul_mbb_mxt_dhc}  
  Updated these sections with optional fields for subscription information and merchant reference number:

* [Create a Subscription with an Existing Plan](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/rb-cre-subs-w-exist-plan/rb-cre-subs-w-exist-plan-reqd-fields.md "")

* [Creating a Subscription with Plan Overrides](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/rb-cre-subs-w-subs-overrides/rb-cre-subs-w-subs-overrides-reqd-fields.md "")

* [Creating a Fully Customized Subscription with a One-Time Plan](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/rb-cre-subs-fully-cust-w-otp/rb-cre-subs-fully-cust-w-otp-reqd-fields.md "")

* [Creating a Follow on Subscription from an Existing Transaction](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/rb-cre-follow-on-subs-w-exist-trans/rb-cre-follow-on-subs-w-exist-trans-reqd-fields.md "")
  {#recur-bill-recentrevisions_ul_v5f_wzt_dhc}  
  Updated this section with information about processing missed payments: [Reactivating a Suspended Subscription](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/recur-bill-activating-a-subscription.md "")  
  Updated this section with information about mandates and system settings: [Customer Notifications](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-addl-feat/recur-bill-cust-not.md "")  
  Updated this example with client reference information: [REST Examples: Retrieving a List of Subscriptions](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/recur-bill-getting-all-subscriptions/recur-bill-get-all-subscriptions-examples.md "")

25.09.01
--------

This revision contains only editorial changes and no technical updates.

25.06.01
--------

Updated information about the amount of time allowed between subscription payments in these sections:

* [Creating a Plan](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-plans-intro/recur-bill-creating-a-plan.md "")
* [Subscription ID](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/recur-bill-sub-id.md "")

25.05.02
--------

Updated this section:

* [System Retry Logic](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-addl-feat/recur-bill-sys-retry.md "")

25.05.01
--------

Added these sections:

* [Creating a Follow-on Subscription from an Existing Transaction](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/rb-cre-follow-on-subs-w-exist-trans.md "")

* [Retrieving the Details of a Follow-on Subscription Based on an Existing Transaction](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/recur-bill-getting-dets-fo-subscriptions.md "")  
  Updated these sections:

* [Account Validation (Pre-Authorization)](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-dev-intro/recur-bill-acct-valid.md "")

* [Subscription Statuses](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/recur-bill-subscriptions-statuses.md "")

* [Zero-Amount Authorizations](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/recur-bill-zero-auths.md "")
  {#recur-bill-recentrevisions_ul_fd5_2c2_t2c}  
  Updated these sections:

* [Creating a Subscription with an Existing Plan](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/rb-cre-subs-w-exist-plan.md "")

* [Creating a Subscription with Plan Overrides](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/rb-cre-subs-w-subs-overrides.md "")

* [Creating a Fully Customized Subscription with a One-Time Plan](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/rb-cre-subs-fully-cust-w-otp.md "")

* [Amending a Subscription](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/rb-amend-subs.md "")  
  Updated the example in this section:

* [REST Example: Switching a Subscription to a Different Plan](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/rb-amend-subs/rb-amend-subs-ex.md "")

{#recur-bill-recentrevisions_ul_lh3_fj2_t2c}  
Updated the graphics in these sections:

* [Plan Statuses](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-plans-intro/recur-bill-plan-statuses.md "")
* [Subscription Statuses](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/recur-bill-subscriptions-statuses.md "")
  {#recur-bill-recentrevisions_ul_wzw_y2m_w2c}

Introduction to Recurring Billing {#recur-bill-dev-intro}
=========================================================

This guide explains how to integrate the Recurring Billing REST API into your payment system.  
The Recurring Billing service enables you to create and manage payment plans and subscriptions for recurring payment schedules. It automates the storage and handling of your customer's payment information and personal data within secure Relay data centers in compliance with credentials-on-file (COF) best practices. Storage risks and the PCI DSS scope are reduced through the use of the `Token Management Service` (`TMS`).  
`Cybersource` Recurring Billing consists of these three elements:

* **Plan:** Stores the billing schedule.
* **Subscription:** Combines the token and plan and defines the subscription start date, name, and description.
* **Token:** Stores customer billing, shipping, and payment details.  
  For information about Recurring Billing in the `Business Center`, see the [Recurring Billing User Guide](https://developer.cybersource.com/docs/cybs/en-us/recurring-billing/user/all/rest/recurring-billing-user/recur-bill-services-intro.md "").  
  Recurring payments can also be handled with the payments API. Merchant-initiated transactions (MITs) are part of the payments API. For more information on recurring payments using MITs, see the Recurring Payments section in the [Payments Developer Guide](https://developer.cybersource.com/docs.md#PaymentServices "").
  IMPORTANT Do not use this document if you are using the payments API to process recurring payments. When using payments API for MITs, you must capture and store the customer's payment credentials manually. Also, you send the payments API MIT requests to different endpoints than you send the recurring billing requests.  
  The Recurring Billing service is available for the `REST` API only. The service is not available in the `SCMP` API or the `Simple Order` API.

> IMPORTANT
> These Latin American processors are not yet supported for Recurring Billing services:
>
> * ` Comercio Latino `
> * ` Prosa `

Prerequisites
-------------

Your account must be enabled for Recurring Billing and configured for the `Token Management Service` (`TMS`). The customer token is the only token type that can be used with Recurring Billing.  
For more information about `TMS`, see the [`Token Management Service` REST API Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/tms/developer/ctv/rest/tms/tms-overview.md "").

Getting Started with the REST API
---------------------------------

If you have not already, you must register and obtain authentication credentials for the REST API.  
Go to the `Cybersource` [Hello world sandbox](https://developer.cybersource.com/hello-world.md "") in the Developer Center.  
When your system is REST compliant, you can test your Recurring Billing integration by sending requests to the `Cybersource` test server. See *[Getting Started with REST Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-about-guide.md "")*

Account Validation (Pre-Authorization) {#recurr-bill-acct-valid}
================================================================

When you capture payment card data for future use, `Cybersource` recommends that you ensure that the account number entered is an active, valid account. You can also use the Address Verification Service (AVS), the Card Verification Number (CVN), and expiration date validation. To validate the account, initiate a zero-amount authorization transaction. To verify that your processor supports zero-amount authorization, see the zero-amount authorization information in the [Payment Services Optional Features Supplement](https://docs.cybersource.com/content/dam/new-documentation/documentation/en/credit-card/supplement/credit-card-services-optional-features-so.pdf "").  
If your processor does not support account validation, you can use the minimal supported amount and do a reversal later. You can also enable the *Data Enrichment for Card Verification* feature, which automatically chooses the minimal authorization amount. Contact customer support for more details.  
For more information about how to perform a pre-authorization, see the [*Token Management Service Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms/tms-overview.md "").

Plans {#recur-bill-plans-intro}
===============================

A plan defines the payment amount and billing schedule for recurring or subscription payments.  
After you create a plan, you can assign it to multiple subscriptions and manage changes for multiple subscriptions.
IMPORTANT Installment-based plans are not available.  
Recurring Billing supports two types of plans:

* **Standard plans**: created and stored within the recurring billing service for re-use. You can assign these plans to multiple subscriptions.

* **One-time plans**: created specifically for a single subscription and not stored for re-use nor assigned to other subscriptions.  
  Both plan types have two billing cycle options. Choose one of these billing cycles when defining the number of recurring payments:

* Bill indefinitely

* Fixed number of payments

Bill Indefinitely {#recur-bill-plans-intro_bill-indef}
------------------------------------------------------

This billing cycle option has a fixed payment amount and a payment schedule with no end date. This option comprises these elements:

* Plan code
* Plan name
* Plan description (optional)
* Billing frequency
* Currency
* Payment amount
* Set-up fee (optional)

> IMPORTANT One-time plans do not include a plan code, plan name, or plan description.

Fixed Number of Payments {#recur-bill-plans-intro_fixed-num}
------------------------------------------------------------

This billing cycle option has a fixed payment amount, a payment schedule, and a fixed number of payments. This option comprises these elements:

* Plan code
* Plan name
* Plan description (optional)
* Billing frequency
* Currency
* Payment amount
* Number of billing cycles
* Set-up fee (optional)

IMPORTANT One-time plans do not include a plan code, plan name, or plan description.

Plan Statuses {#recur-bill-plan-statuses}
=========================================

A plan has one of these statuses:

#### Figure: {#recur-bill-plan-statuses_fig_zst_vwr_mwb}

Plan Status Flow ![Diagram of the plan flow and possible plan statuses.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/recurring-billing/images/plan-status-flow-600x100-v2.svg/jcr:content/renditions/original)

* **Draft**: a draft plan cannot be assigned to new or existing subscriptions. Draft plans can be changed to active or deleted.
* **Active**: an active plan can be used when you create a new subscription or assigned to an existing subscription. Active plans can be changed to inactive or deleted.
* **Inactive**: subscriptions that are assigned to an inactive plan are billed until the subscription is completed or canceled. You cannot use inactive plans to create new subscriptions, nor switch subscriptions to an inactive plan. Inactive plans can be changed to active.
* **Deleted**: a deleted plan is removed from the system.

> IMPORTANT You cannot amend an inactive plan. To make changes, move the plan to active or draft status.
> IMPORTANT You can delete a standard plan that has a draft status or has an active or inactive status and has never been assigned to any subscriptions.

Assigning a Plan Code {#recurr-bill-assign-plan-code}
=====================================================

When you create a standard plan, you can choose to supply a plan code that relates to your business and is used for reference to the plan. This code can be numeric or alphanumeric with dash (-) and dot (.) characters, and up to 10 characters long.  
If no plan code is assigned, the system automatically assigns a system-generated value.

Creating a Plan {#recur-bill-creating-a-plan}
=============================================

Create a plan to define the billing schedule, which includes the amount, frequency, and billing cycles for a subscription. The interval between subscription payments cannot exceed 12 months. IMPORTANT If a subscription is to use a one-time plan instead of a standard plan, you create the one-time plan when you create the subscription. The plan details are embedded in the subscription request.  
When you create a plan, the system assigns an ID to the plan. Use the plan ID to request these actions:

* Creating a subscription
* Retrieving a plan
* Amending a plan
* Activating a plan
* Deactivating a plan
* Deleting a plan  
  Follow these steps to create a plan:

1. Send the request to the recurring billing endpoint:
   * **Production:** `POST https://api.cybersource.com/rbs/v1/plans`
   * **Test:** `POST https://apitest.cybersource.test.com/rbs/v1/plans`
2. Verify that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").{#recur-bill-creating-a-plan_d9e19}

Required Fields for Creating a Plan {#recur-bill-create-plan-reqd-fields}
=========================================================================

Include these fields in your request to create a plan:

orderInformation.amountDetails.billingAmount
:

orderInformation.amountDetails.currency
:

planInformation.billingCycles.total
:
Required for a plan with a defined plan period.

planInformation.billingPeriod.length
:

planInformation.billingPeriod.unit
:

planInformation.name
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

Optional Fields for Creating a Plan {#recur-bill-create-plan-opt-fields}
========================================================================

orderInformation.amountDetails.setupFee
:

planInformation.code
:

planInformation.description
:

planInformation.status
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Creating a Plan {#recur-bill-create-a-plan-examples}
==================================================================

Request

```
{
    "planInformation": {
        "billingPeriod": {
            "unit": "w",
            "length": "1"
        },
        "billingCycles":
        {
            "total": "4"
        },
        "code":"1619310018",
        "name": "Test plan",
        "description": "Description",
        "status":"active"
    },
    "orderInformation": {
        "amountDetails": {
            "billingAmount": "7",
            "currency": "USD",
            "setupFee": "0"
        }
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/plans/1619212820",
            "method": "GET"
        },
        "update": {
            "href": "/rbs/v1/plans/1619212820",
            "method": "PATCH"
        },
        "deactivate": {
            "href": "/rbs/v1/plans/1619212820/deactivate",
            "method": "POST"
        }
    },
    "id": "1619212820",
    "status": "COMPLETED",
    "planInformation": {
        "code": "1619310018",
        "status": "ACTIVE"
    }
}
```

Error Response

```
{
   "status": "INVALID_REQUEST",
   "reason": "INVALID_DATA",
   "message": "One or more fields in the request contains invalid data.",
   "details": [
       {
          "field": "planInformation.code",
          "reason": "DUPLICATE"
       }
    ]
 }
```

Retrieving a List of Plans {#recur-bill-getting-all-plans}
==========================================================

A list of plans provides these details for each plan:

* Plan ID
* Plan code
* Plan name
* Description
* Status
* Billing period unit
* Billing period length
* Billing cycles total
* Currency
* Billing amount
* Set-up fee

After you retrieve the list of plans, use the plan ID to retrieve, amend, activate, deactivate, or delete a subscription.  
Follow these steps to retrieve a list of plans:

1. Filter the list of plans using these query string parameters:
   * `filters`: Use Lucene query syntax. Only keyword-matching and `AND` are supported. Example: `name:"Test plan" AND code:"009" AND status:"ACTIVE"`
   * `offset`: Page offset number.
   * `limit`: Number of items to be returned. Default is `20` and maximum is `100`.
     {#recur-bill-getting-all-plans_ul_ij4_1fj_r4b}
2. Send to one of these endpoints:  
   Production: `GET https://api.cybersource.com/rbs/v1/plans`  
   Test: `GET https://apitest.cybersource.test.com/rbs/v1/plans`
3. Verify that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").{#recur-bill-getting-all-plans_d9e19}

REST Example: Retrieving a List of Plans {#recur-bill-get-all-plans-examples}
=============================================================================

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/plans?limit=2",
            "method": "GET"
        },
        "next": {
            "href": "/rbs/v1/plans?offset=2&limit=2",
            "method": "GET"
        }
    },
    "totalCount": 96,
    "plans": [
        {
            "_links": {
                "self": {
                    "href": "/rbs/v1/plans/1619212820",
                    "method": "GET"
                },
                "update": {
                    "href": "/rbs/v1/plans/1619212820",
                    "method": "PATCH"
                },
                "deactivate": {
                    "href": "/rbs/v1/plans/1619212820/deactivate",
                    "method": "POST"
                }
            },
            "id": "1619212820",
            "planInformation": {
                "code": "1619310018",
                "status": "ACTIVE",
                "name": "Test plan",
                "description": "Description",
                "billingPeriod": {
                    "length": "1",
                    "unit": "W"
                },
                "billingCycles": {
                    "total": "4"
                }
            },
            "orderInformation": {
                "amountDetails": {
                    "currency": "USD",
                    "billingAmount": "7.00",
                    "setupFee": "0.00"
                }
            }
        },
        {
            "_links": {
                "self": {
                    "href": "/rbs/v1/plans/6183561970436023701960",
                    "method": "GET"
                },
                "update": {
                    "href": "/rbs/v1/plans/6183561970436023701960",
                    "method": "PATCH"
                },
                "activate": {
                    "href": "/rbs/v1/plans/6183561970436023701960/activate",
                    "method": "POST"
                }
            },
            "id": "6183561970436023701960",
            "planInformation": {
                "code": "1616024773",
                "status": "DRAFT",
                "name": "Plan Test",
                "description": "12123",
                "billingPeriod": {
                    "length": "9999",
                    "unit": "Y"
                },
                "billingCycles": {
                    "total": "123"
                }
            },
            "orderInformation": {
                "amountDetails": {
                    "currency": "USD",
                    "billingAmount": "1.00",
                    "setupFee": "0.00"
                }
            }
        }
    ]
}
```

Error Response

```
{
  "status": "INVALID_REQUEST",
  "reason": "VALIDATION_ERROR",
  "message": "Field validation errors.",
  "details": [
    {
      "field": "customerInformation.email",
      "reason": "Invalid email"
    }
  ]
}
```

Retrieving a Plan {#recur-bill-getting-a-plan}
==============================================

You can retrieve the details of a specific plan using the plan ID. These plan details are returned in the response:

* Plan ID
* Plan code
* Plan name
* Description
* Status
* Billing period unit
* Billing period length
* Billing cycles total
* Currency
* Billing amount
* Set-up fee

Follow these steps to retrieve a plan:

1. In the endpoint path, include the plan ID that you received when you retrieved a list of plans.
2. Send the request to the recurring billing endpoint:  
   Production: `GET https://api.cybersource.com/rbs/v1/plans/{id}`  
   Test: `GET https://apitest.cybersource.test.com/rbs/v1/plans/{id}`
3. Verify that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").{#recur-bill-getting-a-plan_d9e19}

REST Example: Retrieving a Plan {#reference_i4k_3sz_n4b}
========================================================

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/plans/6183561970436023701960",
            "method": "GET"
        },
        "update": {
            "href": "/rbs/v1/plans/6183561970436023701960",
            "method": "PATCH"
        },
        "activate": {
            "href": "/rbs/v1/plans/6183561970436023701960/activate",
            "method": "POST"
        }
    },
    "id": "6183561970436023701960",
    "planInformation": {
        "code": "1616024773",
        "status": "DRAFT",
        "name": "Plan Test",
        "description": "12123",
        "billingPeriod": {
            "length": "9999",
            "unit": "Y"
        },
        "billingCycles": {
            "total": "123"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "currency": "USD",
            "billingAmount": "1.00",
            "setupFee": "0.00"
        }
    }
}
```

Error Response

```
{
  "status": "NOT_FOUND",
  "reason": "INVALID_DATA"
}
```

Retrieving a Plan Code {#recur-bill-getting-a-plan-code}
========================================================

When you specify your own plan codes, you can request the next consecutive alphabetical or numeric plan code based on the last plan code that you specified. For example, if the last plan code that you specified was `Plan104`, the system returns the code `Plan105`.  
Follow these steps to retrieve a plan code:

1. Send the request to the Recurring Billing endpoint:  
   Production: `GET https://api.cybersource.com/rbs/v1/plans/code`  
   Test: `GET https://apitest.cybersource.test.com/rbs/v1/plans/code`
2. Verify that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").{#recur-bill-getting-a-plan-code_d9e19}

REST Example: Retrieving a Plan Code {#recur-bill-get-a-plan-code-examples}
===========================================================================

Response to a Successful Request

```
{
    "code": "1619310019",
}
```

Error Response

```
{
  "status": "NOT_FOUND",
  "reason": "INVALID_DATA"
}
```

Amending a Plan {#recur-bill-amending-a-plan}
=============================================

Amend a plan by entering one of two values in the processingInformation.subscriptionBillingOptions.applyTo field. Possible values:

* `ALL`: change is applied to all subscriptions (existing and new).
* `NEW` (default): change is applied to new subscriptions only.

You can also make changes to individual subscriptions. See [Amending a Subscription](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/rb-amend-subs.md "").  
For a **draft** plan, you can amend all plan information.  
For an **active** plan, you can amend only the information in these fields:

* planInformation.billingPeriod
* planInformation.billingCycles
* orderInformation.amountDetails.currency
  IMPORTANT You cannot amend an inactive plan. To make changes, move the plan to active or draft status.  
  Follow these steps to amend a plan:

1. Include any optional fields.
2. In the endpoint path, include the plan ID that you received when you retrieved a list of plans.
3. Send the request to the Recurring Billing endpoint:  
   Production: `PATCH https://api.cybersource.com/rbs/v1/plans/{id}`  
   Test: `PATCH https://apitest.cybersource.test.com/rbs/v1/plans/{id}`
4. Verify that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").{#recur-bill-amending-a-plan_d9e19}

Optional Fields for Amending a Plan {#recur-bill-amend-plan-opt-fields}
=======================================================================

These fields are optional for amending a plan:

orderInformation.amountDetails.billingAmount
:

orderInformation.amountDetails.setupFee
:

planInformation.billingCycles.total
:
Only increases to the number of billing cycles are allowed.

planInformation.code
:

planInformation.description
:

planInformation.name
:

processingInformation.subscriptionBillingOptions.applyTo
:
Default value is `NEW`.

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Amending a Plan {#recur-bill-amend-a-plan-examples}
=================================================================

Request

```
{
    "planInformation": {
        "name": "AmendPlan",
        "description": "Amend Plan 1610394600",
        "billingPeriod":{
            "length": "4",
            "unit": "M"
        },
        "billingCycles":{
            "total": "7"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "billingAmount": "38.00",
            "setupFee": "35"
        }
    },
    "processingInformation": {
        "subscriptionBillingOptions": {
            "applyTo": "all"
        }
    }
}     
```

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/plans/6183561970436023701960",
            "method": "GET"
        },
        "update": {
            "href": "/rbs/v1/plans/6183561970436023701960",
            "method": "PATCH"
        },
        "activate": {
            "href": "/rbs/v1/plans/6183561970436023701960/activate",
            "method": "POST"
        }
    },
    "id": "6183561970436023701960",
    "submitTimeUtc": "2023-04-13T21:39:34.993Z",
    "status": "COMPLETED",
    "planInformation": {
        "code": "1616024773",
        "status": "DRAFT"
    }
}           
```

Error Response

```
{
    "status": "NOT_FOUND",
    "reason": "INVALID_DATA",
    "message": "One or more fields in the request contains invalid data.",
    "details": [
        {
            "field": "subscriptionInformation.planId",
            "reason": "NOT_FOUND"
        }
    ]
}          
```

Activating a Plan {#recur-bill-activating-a-plan}
=================================================

You can activate a plan that has a draft or inactive status and that has never been assigned to any subscriptions.  
Follow these steps to activate a plan:

1. In the endpoint path, include the plan ID that you received when you retrieved a list of plans.
2. Send the request to the Recurring Billing endpoint:  
   Production: `POST https://api.cybersource.com/rbs/v1/plans/{id}/activate`  
   Test: `POST https://apitest.cybersource.test.com/rbs/v1/plans/{id}/activate`
3. Verify that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").{#recur-bill-activating-a-plan_d9e19}

REST Example: Activating a Plan {#recur-bill-activate-a-plan-examples}
======================================================================

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/plans/1619214189",
            "method": "GET"
        },
        "update": {
            "href": "/rbs/v1/plans/1619214189",
            "method": "PATCH"
        },
        "deactivate": {
            "href": "/rbs/v1/plans/1619214189/deactivate",
            "method": "POST"
        }
    },
    "id": "1619214189",
    "status": "COMPLETED",
    "planInformation": {
        "code": "1619214189",
        "status": "ACTIVE"
    }
}
```

Error Response

```
{
    "status": "NOT_FOUND",
    "reason": "INVALID_DATA",
    "message": "One or more fields in the request contains invalid data.",
    "details": [
        {
            "field": "subscriptionInformation.planId",
            "reason": "NOT_FOUND"
        }
    ]
}
```

Deactivating a Plan {#recur-bill-deactivating-a-plan}
=====================================================

You can deactivate a specific plan that has an active status.  
Follow these steps to deactivate a plan:

1. In the endpoint path, include the plan ID that you received when you retrieved a list of plans.
2. Send the request to the Recurring Billing endpoint:  
   Production: `POST https://api.cybersource.com/rbs/v1/plans/{id}/deactivate`  
   Test: `POST https://apitest.cybersource.test.com/rbs/v1/plans/{id}/deactivate`
3. Verify that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").{#recur-bill-deactivating-a-plan_d9e19}

REST Example: Deactivating a Plan {#recur-bill-deactivate-a-plan-examples}
==========================================================================

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/plans/1619214189",
            "method": "GET"
        },
        "activate": {
            "href": "/rbs/v1/plans/1619214189/activate",
            "method": "POST"
        }
    },
    "id": "1619214189",
    "status": "COMPLETED",
    "planInformation": {
        "code": "1619214189",
        "status": "INACTIVE"
    }
}
```

Error Response

```
{
    "status": "INVALID_REQUEST",
    "reason": "INVALID_DATA",
    "message": "One or more fields in the request contains invalid data.",
    "details": [
        {
            "field": "planInformation.status",
            "reason": "INVALID_DATA"
        }
    ]
}
```

Deleting a Plan {#recur-bill-deleting-a-plan}
=============================================

You can delete a standard plan that has a draft status. You can also delete a plan that has an active or inactive status and has never been assigned to any subscriptions.  
Follow these steps to delete a plan:

1. In the endpoint path, include the plan ID that you received when you retrieved a list of plans.
2. Send the request to the Recurring Billing endpoint:  
   Production: `DELETE https://api.cybersource.com/rbs/v1/plans/{id}`  
   Test: `DELETE https://apitest.cybersource.test.com/rbs/v1/plans/{id}`
3. Verify that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").{#recur-bill-deleting-a-plan_d9e19}

REST Example: Deleting a Plan {#recur-bill-delete-a-plan-examples}
==================================================================

Response to a Successful Request

```
{
  "status": "COMPLETED"
}
```

Error Response

```
{
    "status": "NOT_FOUND",
    "reason": "NOT_FOUND",
    "message": "One or more fields in the request contains invalid data.",
    "details": [
        {
            "field": "subscriptionInformation.planId",
            "reason": "INVALID_DATA"
        }
    ]
}
```

Subscriptions {#recur-bill-subscriptions}
=========================================

Subscriptions store customer details by using a Token Management Service (TMS) token. You must have an assigned payment plan. Subscriptions consist of this information:

* Subscription code
* Subscription name
* Start date
* TMS token
* Plan: standard or one-time
* (Optional) Merchant Reference Number: the specified value will be used as the merchant reference number for all subscription payments. If no value is provided, the system will automatically generate a random number for each subsequent payment.  
  Subscriptions can be updated, activated, suspended, or canceled.

Subscription Prerequisites {#recur-bill-subscription-prereq}
============================================================

Before creating a subscription, you must create a customer token.  
For more information about creating a customer token, see the see the [*Token Management Service Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms/tms-overview.md "").  
When you create a subscription, use these fields to include the values you received in the response to your request:

* tokenInformation.customer.id
* processorInformation.networkTransactionId
* orderInformation.amountDetails.authorizedAmount
  {#recur-bill-subscription-prereq_ul_scx_5d2_t2c}  
  See the table below for the payments to Recurring Billing subscription field mapping:

|-------------------------------------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Payments API Response Field**                 | **Recurring Billing Create Subscription Request Field**     | **Required Value Information**                                                                                                                                                  |
| tokenInformation.customer.id                    | paymentInformation.customer.id                              | Customer token ID                                                                                                                                                               |
| processorInformation.networkTransactionId       | subscriptionInformation.originalTransactionId               | Network token for the transaction initializing the subscription. For EFTPOS cards, a network token is not generated. In this case, provide the transaction request ID or use 0. |
| orderInformation.amountDetails.authorizedAmount | subscriptionInformation.originalTransactionAuthorizedAmount | Authorized amount for the transaction initializing the subscription. Required only for Diners or Discover cards.                                                                |

Subscription Statuses {#recur-bill-subscriptions-statuses}
==========================================================

This diagram illustrates the statuses of a subscription from creation to completion.

#### Figure:

Subscription Flow ![Diagram of the statuses of a subscription.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/recurring-billing/images/subscription-status-flow-600x450.svg/jcr:content/renditions/original)  
A subscription has one of these statuses:

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

{#recur-bill-subscriptions-statuses_dl_v53_cdm_y1c}

Zero-Amount Authorizations {#recur-bill-zero-auths}
===================================================

When you create a subscription before the subscription start date, `Cybersource` verifies the account with a zero-amount authorization to ensure that the stored card details are valid.  
When you create a subscription on the subscription start date, `Cybersource` does not perform a zero-amount authorization because the first recurring payment is processed immediately.

> IMPORTANT
> **Deprecated flow:** This behavior occurs only when you do not provide the value for subscriptionInformation.originalTransactionId and application performs the initial authorization. This flow does not ensure Strong Customer Authentication (SCA) compliance.

Assigning a Subscription Code {#recur-bill-assign-sub-code}
===========================================================

When you create a subscription, you can supply a subscription code that relates to your business and that is used for reference to the subscription. This code can be numeric or alphanumeric with dash (-) and dot (.) characters and can be up to 10 characters long.  
If you do not supply a subscription code, the recurring billing system automatically assigns a code.

Subscription ID {#recur-bill-sub-id}
====================================

When you create a subscription, the system assigns an ID to the subscription that you can use for these actions:

* Retrieving a subscription
* Amending a subscription
* Canceling a subscription
* Re-activating a subscription
* Suspending a subscription
  {#recur-bill-sub-id_ul_k25_q5w_xxb}
  IMPORTANT The interval between subscription payments cannot exceed 12 months.

Overriding a Plan {#recur-bill-plan-overrides}
==============================================

When assigning a plan to a subscription or amending a subscription, you can amend standard plan details for individual subscriptions. For example, such changes might include an amendment to the billing amount, plan duration (billing cycles) amendment.
IMPORTANT Plan overrides apply only to the individual subscription and do not amend the standard plan details used for other subscriptions.

Creating a Subscription with an Existing Plan {#rb-cre-subs-w-exist-plan}
=========================================================================

Basic Steps {#rb-cre-subs-w-exist-plan_section_ghg_vxq_fdc}
-----------------------------------------------------------

Follow these steps to create a subscription:

1. Create the request with the required API fields.
2. Send the request to one of these endpoints:
   * **Production:** `POST https://api.cybersource.com/rbs/v1/subscriptions`
   * **Test:** `POST https://apitest.cybersource.test.com/rbs/v1/subscriptions`
3. Verify the response messages to make sure that the request was successful. A 200-level HTTP response code indicates success. See [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

Required Fields {#rb-cre-subs-w-exist-plan-reqd-fields}
=======================================================

These fields are required for creating a subscription with an existing plan:

paymentInformation.customer.id
:

subscriptionInformation.name
:

subscriptionInformation.planId
:
Required when you are using a standard plan.

subscriptionInformation.startDate
:

Optional Field
--------------

These fields are optional:

subscriptionInformation.originalTransactionId
:
Network token identifying the transaction that initialized the subscription. Including this field ensures better authorization rates and Strong Customer Authentication (SCA) compliance where necessary.
:
This value is returned in the Payments response as processorInformation.networkTransactionId.
:
For EFTPOS cards, a network token is not generated. In this case, provide the transaction request ID or use 0.

subscriptionInformation.code
:

clientReferenceInformation.code
:
Merchant reference number.

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Creating a Subscription with an Existing Plan {#rb-cre-subs-w-exist-plan-ex}
==========================================================================================

This example shows how to create a subscription with an existing plan.  
Request

```
{
    "clientReferenceInformation":{
      "code":"ORDER123"
    },
    "subscriptionInformation": {
        "planId":"1619214515",
        "name": "Daily Gym Subscription",
        "startDate": "2023-04-15T17:01:42Z",
        "originalTransactionId”: “016153570198200"
    },
    "paymentInformation": {
        "customer": {
            "id": "C09F227C54F94951E0533F36CF0A3D91"
        }
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/subscriptions/1619214690",
            "method": "GET"
        },
        "update": {
            "href": "/rbs/v1/subscriptions/1619214690",
            "method": "PATCH"
        },
        "cancel": {
            "href": "/rbs/v1/subscriptions/1619214690/cancel",
            "method": "POST"
        }
    },
    "id": "1619214690",
    "status": "COMPLETED",
    "subscriptionInformation": {
        "code": "AWC-47",
        "status": "PENDING"
    }
}
```

Response to a Failed Request

```
{
    "status": "INVALID_REQUEST",
    "reason": "INVALID_DATA",
    "message": "One or more fields in the request contains invalid data.",
    "details": [
        {
            "field": "subscriptionInformation.startDate",
            "reason": "INVALID_DATA"
        }
    ]
}
```

Creating a Subscription with Plan Overrides {#rb-cre-subs-w-subs-overrides}
===========================================================================

You can create a subscription with a plan overrides.

Basic Steps {#rb-cre-subs-w-subs-overrides_section_ghg_vxq_fdc}
---------------------------------------------------------------

Follow these steps to create a subscription:

1. Create the request with the required API fields.
2. Send the request to one of these endpoints:
   * **Production:** `POST https://api.cybersource.com/rbs/v1/subscriptions`
   * **Test:** `POST https://apitest.cybersource.test.com/rbs/v1/subscriptions`
3. Verify the response messages to make sure that the request was successful. A 200-level HTTP response code indicates success. See [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

Required Fields {#rb-cre-subs-w-subs-overrides-reqd-fields}
===========================================================

These fields are required for creating a subscription with plan overrides:

paymentInformation.customer.id
:

subscriptionInformation.name
:

subscriptionInformation.planId
:

subscriptionInformation.startDate
:

Optional Field
--------------

subscriptionInformation.originalTransactionId
:
Network token identifying the transaction that initialized the subscription. Including this field ensures better authorization rates and Strong Customer Authentication (SCA) compliance where necessary.
:
This value is returned in the Payments response as processorInformation.networkTransactionId.
:
For EFTPOS cards, a network token is not generated. In this case, provide the transaction request ID or use 0.

subscriptionInformation.code
:

clientReferenceInformation.code
:
Merchant reference number.

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Creating a Subscription with Plan Overrides {#rb-cre-subs-w-subs-overrides-ex}
============================================================================================

Request

```
{
    "clientReferenceInformation":{
      "code":"ORDER123"
    },
    "subscriptionInformation": {
        "planId": "1619214515",
        "name": "SubName With Overrides",
        "startDate": "2023-04-16T17:01:42Z",
        "originalTransactionId”: “016153570198200"
    },
    "planInformation": {
        "billingCycles": {
            "total": "3"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "billingAmount": "13.14",
            "setupFee": "1.27"
        }
    },
    "paymentInformation": {
        "customer": {
            "id": "C09F227C54F94951E0533F36CF0A3D91"
        }
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/subscriptions/1619214795",
            "method": "GET"
        },
        "update": {
            "href": "/rbs/v1/subscriptions/1619214795",
            "method": "PATCH"
        },
        "cancel": {
            "href": "/rbs/v1/subscriptions/1619214795/cancel",
            "method": "POST"
        }
    },
    "id": "1619214795",
    "status": "COMPLETED",
    "subscriptionInformation": {
        "code": "AWC-48",
        "status": "PENDING"
    }
}
```

Error Response to a Failed Request

```
{
    "status": "INVALID_REQUEST",
    "reason": "DUPLICATE_REQUEST",
    "message": "Duplicate requests are not supported within 15 minutes.",
    "details": [
        {
            "field": "subscriptionInformation.planId or paymentInformation.customer.id or subscriptionInformation.startDate or subscriptionInformation.name",
            "subscriptionId": "1619214795",
            "reason": "INVALID_DATA"
        }
    ]
}
```

Creating a Fully Customized Subscription with a One-Time Plan {#rb-cre-subs-fully-cust-w-otp}
=============================================================================================

You can create a subscription with a one-time plan.  
The start date must be in coordinated universal time (UTC) in this format: `YYYY-MM-DDThh:mm:ssZ`. The T separates the date and the time. The `Z` indicates UTC. For example, `2023-08-11T22:47:57Z` indicates August 11, 2023, at 22:47:57 (10:47:57PM). For subscriptions created on the start date, set the time to the current time and day in your time zone.

Fields Specific to This Use Case
--------------------------------

These REST API request fields and values are specific to this use case:

* orderInformation.amountDetails.billingAmount
* orderInformation.amountDetails.currency
* orderInformation.amountDetails.setupFee
* planInformation.billingCycles.total
* planInformation.billingPeriod.length
* planInformation.billingPeriod.unit
* subscriptionInformation.startDate

Basic Steps {#rb-cre-subs-fully-cust-w-otp_section_ghg_vxq_fdc}
---------------------------------------------------------------

Follow these steps to create a subscription:

1. Create the request with the required API fields.
2. Send the request to one of these endpoints:
   * **Production:** `POST https://api.cybersource.com/rbs/v1/subscriptions`
   * **Test:** `POST https://apitest.cybersource.test.com/rbs/v1/subscriptions`
3. Verify the response messages to make sure that the request was successful. A 200-level HTTP response code indicates success. See [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

Required Fields {#rb-cre-subs-fully-cust-w-otp-reqd-fields}
===========================================================

These fields are required for creating a subscription with subscription one-time plan:

orderInformation.amountDetails.billingAmount
:

orderInformation.amountDetails.currency
:

orderInformation.amountDetails.setupFee
:

paymentInformation.customer.id
:

planInformation.billingPeriod.length
:

planInformation.billingPeriod.unit
:

subscriptionInformation.name
:

subscriptionInformation.startDate
:

Optional Field
--------------

subscriptionInformation.originalTransactionId
:
Network token identifying the transaction that initialized the subscription. Including this field ensures better authorization rates and Strong Customer Authentication (SCA) compliance where necessary.
:
This value is returned in the Payments response as processorInformation.networkTransactionId.
:
For EFTPOS cards, a network token is not generated. In this case, provide the transaction request ID or use 0.

subscriptionInformation.code
:

clientReferenceInformation.code
:
Merchant reference number.

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Creating a Fully Customized Subscription with a One-Time Plan {#rb-cre-subs-fully-cust-w-otp-ex}
==============================================================================================================

Request

```
{
    "clientReferenceInformation":{
      "code":"ORDER123"
    },
    "subscriptionInformation": {
        "name": "SubName Testing",
        "startDate": "2023-04-18T17:01:42Z",
        "originalTransactionId”: “016153570198200"
    },
    "planInformation": {
        "billingCycles": {
            "total":"5"
        },
         "billingPeriod": {
            "length": "3",
            "unit":"D"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "billingAmount": "1.21",
            "setupFee": "1.44",
            "currency":"USD"
        }
    },
    "paymentInformation": {
        "customer": {
            "id": "C09F227C54F94951E0533F36CF0A3D91"
        }
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/subscriptions/1619214861",
            "method": "GET"
        },
        "update": {
            "href": "/rbs/v1/subscriptions/1619214861",
            "method": "PATCH"
        },
        "cancel": {
            "href": "/rbs/v1/subscriptions/1619214861/cancel",
            "method": "POST"
        }
    },
    "id": "1619214861",
    "status": "COMPLETED",
    "subscriptionInformation": {
        "code": "AWC-49",
        "status": "PENDING"
    }
}
```

Response to a Failed Request

```
{
    "status": "INVALID_REQUEST",
    "reason": "INVALID_DATA",
    "message": "One or more fields in the request contains invalid data.",
    "details": [
        {
            "field": "planInformation.billingPeriod.length",
            "reason": "MAX_LENGTH"
        }
    ]
}
```

Creating a Follow-on Subscription from an Existing Transaction {#rb-cre-follow-on-subs-w-exist-trans}
=====================================================================================================

You can create a subscription using an existing successful transaction by specifying its request ID in the path. This method eliminates the need to provide a customer token.  
You can use an existing or one-time plan.  
Follow these steps to create a subscription from an existing transaction:

1. Create the request with the required API fields.

2. Send the request to one of these endpoints:  
   Production: `POST https://api.cybersource.com/rbs/v1/subscriptions/follow-ons/{requestId}`  
   Test: `POST https://apitest.cybersource.test.com/rbs/v1/subscriptions/follow-ons/{requestId}`

3. Verify the responses to make sure that the request was successful. A 200-level HTTP response code indicates success. See the [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

   #### ADDITIONAL INFORMATION

   The start date must be in coordinated universal time (UTC) in this format: YYYY-MM-DDThh:mm:ssZ. The T separates the date and the time. The Z indicates UTC. For example, `2023-08-11T22:47:57Z` indicates August 11, 2023, at 22:47:57 (10:47:57 p.m.). For subscriptions created on the start date, set the time to the current time and day in your time zone.
   {#rb-cre-follow-on-subs-w-exist-trans_steps_d12_ssd_t2c}

Required Fields {#rb-cre-follow-on-subs-w-exist-trans-reqd-fields}
==================================================================

These fields are required for creating a subscription from an existing transaction:

subscriptionInformation.name
:

subscriptionInformation.startDate
:
{#rb-cre-follow-on-subs-w-exist-trans-reqd-fields_ul_sk1_13d_t2c}

Optional Fields
---------------

subscriptionInformation.code
:

clientReferenceInformation.code
:
Merchant reference number.

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Creating a Follow-on Subscription from an Existing Transaction {#rb-cre-follow-on-subs-w-exist-trans-ex}
======================================================================================================================

Request

```
{
    "clientReferenceInformation":{
      "code":"ORDER123"
    },
    "subscriptionInformation": {
        "planId":"1619214515",
        "name": "SubNameFOOTPTesting",
        "startDate": "2023-04-15T17:01:42Z"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/subscriptions/1619214861",
            "method": "GET"
        },
        "update": {
            "href": "/rbs/v1/subscriptions/1619214861",
            "method": "PATCH"
        },
        "cancel": {
            "href": "/rbs/v1/subscriptions/1619214861/cancel",
            "method": "POST"
        }
    },
    "id": "1619214861",
    "status": "COMPLETED",
    "subscriptionInformation": {
        "code": "AWC-49",
        "status": "PENDING"
    }
}
```

Response to a Failed Request

```
{
    "status": "NOT_FOUND",
    "reason": "INVALID_DATA"
}
```

Retrieving the Details of a Follow-on Subscription Based on an Existing Transaction {#recur_bill_getting_dets_fo_subscriptions}
===============================================================================================================================

This operation enables you to verify the payment instrument, billing, and shipping address information from an existing transaction before creating a new subscription.  
Follow these steps to retrievethe details of a follow-on subscription based on an existing transaction:

1. In the endpoint path, include the request ID of an existing transaction.
2. Send the request to one of these endpoints:  
   Production: `POST https://api.cybersource.com/rbs/v1/subscriptions/follow-ons/{requestId}`  
   Test: `POST https://apitest.cybersource.test.com/rbs/v1/subscriptions/follow-ons/{requestId}`
3. Verify the response messages to make sure that the request was successful. A 200-level HTTP response code indicates success. See the [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").
   {#recur_bill_getting_dets_fo_subscriptions_steps_tnh_ttd_t2c}

REST Examples: Retrieving Details for Follow-on Subscription Creation based on Existing Transaction {#recur_bill_get_dets_fo_subscriptions_examples}
====================================================================================================================================================

Successful Response

```
{
  "_links": {
    "self":  {
	"href": "rbs/v1/subscriptions/follow-ons/7216512479796378604957",
	"method": "GET"
	},
	"create":  {
	"href": "rbs/v1/subscriptions/follow-ons/7216512479796378604957",
	"method": "POST"
	}
  },
  "buyerInformation": {
    "merchantCustomerId": "1234",
    "email": ""
  },
  "paymentInstrument": {
    "card": {
      "number": "411111XXXXXX1111",
      "expirationMonth": "11",
      "expirationYear": "2037",
      "type": "001"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "123 Street",
      "locality": "Bellevue",
      "administrativeArea": "AL",
      "postalCode": "12345",
      "email": "test@relay.com",
      "country": "US"
    }
  },
  "shippingAddress": {
    "shipTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "123 Street",
      "locality": "Bellevue",
      "administrativeArea": "AL",
      "postalCode": "12345",
      "country": "US"
    }
  }
}
```

{#recur_bill_get_dets_fo_subscriptions_examples_codeblock_gft_ntd_t2c}  
Error Response

```
{
  "status": "NOT_FOUND",
  "reason": "INVALID_DATA"
}
```

Retrieving a List of Subscriptions {#recur-bill-getting-all-subscriptions}
==========================================================================

When you retrieve a list of subscriptions, these details are included for each subscription:

* Subscription ID: you can use this ID in subsequent requests to retrieve, amend, activate, suspend, or cancel an individual subscription.
* Subscription code
* Subscription status
* Subscription name
* Subscription Merchant Reference Number
* Customer ID
* Plan ID
* Plan code
* Plan name
* Plan description
* Plan status
* Billing period unit
* Billing period length
* Billing cycles total
* Billing cycles current
* Currency
* Billing amount
* Set-up fee

{#recur-bill-getting-all-subscriptions_ul_k1c_kqp_r4b}  
Follow these steps to retrieve a list of subscriptions:

1. Filter the list of subscriptions by these query string parameters:
   * `planName`: Name of the plan.
   * `customerId`: Customer token ID.
   * `status`: Subscription status (for example, ACTIVE or CANCELLED).
   * `customerFirstName`: Customer's first name.
   * `customerLastName`: Customer's last name.
   * `code`: Specific subscription code.
   * `plancode`: Specific plan code.
   * `offset`: Page offset number.
   * `limit`: Number of items to be returned. The default is 20, maximum is 100.
     {#recur-bill-getting-all-subscriptions_ul_ij4_1fj_r4b}
2. Send the request message to one of these endpoints:  
   Production: `GET https://api.cybersource.com/rbs/v1/subscriptions`  
   Test: `GET https://apitest.cybersource.test.com/rbs/v1/subscriptions`
3. Verify that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").{#recur-bill-getting-all-subscriptions_d9e19}
   {#recur-bill-getting-all-subscriptions_steps_u35_r4p_r4b}

REST Examples: Retrieving a List of Subscriptions {#recur-bill-get-all-subscriptions-examples}
==============================================================================================

Successful Response

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/subscriptions?status=ACTIVE&limit=2",
            "method": "GET"
        },
        "next": {
            "href": "/rbs/v1/subscriptions?status=ACTIVE&offset=2&limit=2",
            "method": "GET"
        }
    },
    "totalCount": 29,
    "subscriptions": [
        {
            "_links": {
                "self": {
                    "href": "/rbs/v1/subscriptions/6192112872526176101960",
                    "method": "GET"
                },
                "update": {
                    "href": "/rbs/v1/subscriptions/6192112872526176101960",
                    "method": "PATCH"
                },
                "cancel": {
                    "href": "/rbs/v1/subscriptions/6192112872526176101960/cancel",
                    "method": "POST"
                },
                "suspend": {
                    "href": "/rbs/v1/subscriptions/6192112872526176101960/suspend",
                    "method": "POST"
                }
            },
            "clientReferenceInformation":{
                "code":"ORDER123"
            },
            "id": "6192112872526176101960",
            "planInformation": {
                "code": "34873819306413101960",
                "name": "RainTree Books Daily Plan",
                "billingPeriod": {
                    "length": "1",
                    "unit": "D"
                },
                "billingCycles": {
                    "total": "2",
                    "current": "1"
                }
            },
            "subscriptionInformation": {
                "code": "AWC-44",
                "planId": "6034873819306413101960",
                "name": "Test",
                "startDate": "2023-04-13T17:01:42Z",
                "status": "ACTIVE"
            },
            "paymentInformation": {
                "customer": {
                    "id": "C09F227C54F94951E0533F36CF0A3D91"
                }
            },
            "orderInformation": {
                "amountDetails": {
                    "currency": "USD",
                    "billingAmount": "2.00",
                    "setupFee": "1.00"
                },
                "billTo": {
                    "firstName": "JENNY",
                    "lastName": "AUTO"
                }
            }
        },
        {
            "_links": {
                "self": {
                    "href": "/rbs/v1/subscriptions/6192115800926177701960",
                    "method": "GET"
                },
                "update": {
                    "href": "/rbs/v1/subscriptions/6192115800926177701960",
                    "method": "PATCH"
                },
                "cancel": {
                    "href": "/rbs/v1/subscriptions/6192115800926177701960/cancel",
                    "method": "POST"
                },
                "suspend": {
                    "href": "/rbs/v1/subscriptions/6192115800926177701960/suspend",
                    "method": "POST"
                }
            },
                "clientReferenceInformation": { 
                "code": "ORDER123" 
                          }, 
            "id": "6192115800926177701960",
            "planInformation": {
                "code": "SITPlanCode6",
                "name": "Jan11DeployPlan1",
                "billingPeriod": {
                    "length": "1",
                    "unit": "W"
                },
                "billingCycles": {
                    "total": "6",
                    "current": "1"
                }
            },
            "subscriptionInformation": {
                "code": "AWC-45",
                "planId": "6104313186846711501956",
                "name": "Testsub1",
                "startDate": "2023-04-13T17:01:42Z",
                "status": "ACTIVE"
            },
            "paymentInformation": {
                "customer": {
                    "id": "C09F227C54F94951E0533F36CF0A3D91"
                }
            },
            "orderInformation": {
                "amountDetails": {
                    "currency": "USD",
                    "billingAmount": "1.00",
                    "setupFee": "5.00"
                },
                "billTo": {
                    "firstName": "JENNY",
                    "lastName": "AUTO"
                }
            }
        }
    ]
}
```

Error Response

```
{
  "status": "NOT_FOUND",
  "reason": "INVALID_DATA"
}
```

Retrieving a Subscription {#recur-bill-getting-a-subscription}
==============================================================

You can retrieve the details of a specific subscription. The subscription details returned in the response include:

* Subscription ID
* Subscription code
* Subscription status
* Subscription name
* Subscription Merchant Reference Number
* Customer ID
* Plan ID
* Plan code
* Plan name
* Plan description
* Plan status
* Billing period unit
* Billing period length
* Billing cycles total
* Billing cycles current
* Currency
* Billing amount
* Set-up fee
* Missed payments count: only if the subscription is in a suspended state.
* Missed payments total amount: only if the subscription is in a suspended state.

Follow these steps to retrieve a subscription:

1. In the endpoint path, include the subscription ID that you received from your list of subscriptions.
2. Send the request to one of these endpoints:  
   Production: `GET https://api.cybersource.com/rbs/v1/subscriptions/{id}`  
   Test: `GET https://apitest.cybersource.test.com/rbs/v1/subscriptions/{id}`
3. Verify that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").{#recur-bill-getting-a-subscription_d9e19}

REST Examples: Retrieving a Subscription {#recur-bill-update-a-subscription-examples}
=====================================================================================

Successful Response

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/subscriptions/6192115800926177701960",
            "method": "GET"
        },
        "update": {
            "href": "/rbs/v1/subscriptions/6192115800926177701960",
            "method": "PATCH"
        },
        "cancel": {
            "href": "/rbs/v1/subscriptions/6192115800926177701960/cancel",
            "method": "POST"
        },
        "suspend": {
            "href": "/rbs/v1/subscriptions/6192115800926177701960/suspend",
            "method": "POST"
    },
    "clientReferenceInformation":{
        "code":"ORDER123"
    },
    "id": "6192115800926177701960",
    "planInformation": {
        "code": "SITPlanCode6",
        "name": "Jan11DeployPlan1",
        "billingPeriod": {
            "length": "1",
            "unit": "W"
        },
        "billingCycles": {
            "total": "6",
            "current": "1"
        }
    },
    "subscriptionInformation": {
        "code": "AWC-45",
        "planId": "6104313186846711501956",
        "name": "Testsub1",
        "startDate": "2023-04-13T17:01:42Z",
        "status": "ACTIVE"
    },
    "paymentInformation": {
        "customer": {
            "id": "C09F227C54F94951E0533F36CF0A3D91"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "currency": "USD",
            "billingAmount": "1.00",
            "setupFee": "5.00"
        },
        "billTo": {
            "firstName": "JENNY",
            "lastName": "AUTO"
        }
    }
}
```

Error Response

```
{
    "status": "NOT_FOUND",
    "reason": "INVALID_DATA",
    "details": []
}
```

Retrieving the Next Subscription Code {#recur-bill-getting-a-subscription-code}
===============================================================================

When you specify your subscription code, you can request the next consecutive alphabetical or numeric subscription code based on the last subscription code you specified. For example, if the last subscription code that you specified was `24B`, the system returns the code `24C`.  
Follow these steps to retrieve the next subscription code:

1. Send the request to the recurring billing endpoint:  
   Production: `GET https://api.cybersource.com/rbs/v1/subscriptions/code`  
   Test: `GET https://apitest.cybersource.test.com/rbs/v1/subscriptions/code`
2. Verify that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").{#recur-bill-getting-a-subscription-code_d9e19}

REST Examples: Retrieving the Next Subscription Code {#recur-bill-get-a-subscription-code-examples}
===================================================================================================

Response to a Successful Request

```
{
    "code": "AWC-50",
}
```

Error Response

```
{
  "status": "NOT_FOUND",
  "reason": "INVALID_DATA"
}
```

Amending a Subscription {#rb-amend-subs}
========================================

Subscriptions store customer details using a Token Management Service (TMS) token and have an assigned payment plan. Subscriptions consist of this information:

Subscription code
:
Use the subscriptionInformation.code REST API field to specify an amended value.

Subscription name
:
Use the subscriptionInformation.name REST API field to specify an amended value.

Start date
:
Use the subscriptionInformation.startDate REST API field to specify an amended value.

Token Management Service (TMS) token
:
You cannot change this information.

Plan: standard or one-time
:
A **standard plan** is created and stored within the recurring billing service for re-use. You can assign these plans to multiple subscriptions.
:
A **one-time plan** is created specifically for a single subscription, and you create the plan when you create the subscription. A one-time plan does not include a plan code, plan name, or plan description.

> IMPORTANT The subscription information that you can amend depends on the status of the subscription. Note the limitations described in in the paragraphs that follow.
> IMPORTANT
> When you change the plan ID ( subscriptionInformation.planId field) assigned to a subscription, the first payment is processed immediately. If proration is required after the change, it must be managed outside of the recurring billing service.

Basic Steps {#rb-amend-subs_section_ht1_mjt_fdc}
------------------------------------------------

Follow these steps to amend a subscription.

1. Create the request with the API fields that contain new values.

2. Send the request to one of these endpoints. In the endpoint path, replace the `{id}` portion of the URL with the subscription ID that you received when you retrieved a list of subscriptions:

   * **Production:** `PATCH https://api.cybersource.com/rbs/v1/subscriptions/{id}`
   * **Test:** `PATCH https://apitest.cybersource.test.com/rbs/v1/subscriptions/{id}`

3. Verify the response messages to make sure that the request was successful. A 200-level HTTP response code indicates success. See the [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

Amendable Fields {#rb-amend-subs-amend-fields}
==============================================

The status of the subscription determines which fields you can amend.

Subscriptions That Are Delinquent, Suspended, Canceled, or Completed
--------------------------------------------------------------------

For a subscription in one of these states, you can *modify only these fields:*

subscriptionInformation.code
:

subscriptionInformation.name
:

clientReferenceInformation.code
:
Merchant reference number.

Pending Subscriptions
---------------------

You *cannot modify* these fields when the subscription is in the **pending** state:

orderInformation.amountDetails.currency
:

paymentInformation.customer.id
:

planInformation.billingPeriod.length
:

planInformation.billingPeriod.unit
:

Active Subscriptions
--------------------

You *cannot modify* these fields when the subscription is in the **active** state:

orderInformation.amountDetails.currency
:

orderInformation.amountDetails.setupFee
:

paymentInformation.customer.id
:

planInformation.billingPeriod.length
:

planInformation.billingPeriod.unit
:

subscriptionInformation.startDate
:
Payment processing time starts at 2:00 a.m. in your time zone.

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Switching a Subscription to a Different Plan {#rb-amend-subs-ex}
==============================================================================

Request

```
{
    "subscriptionInformation": {
        "planId": 7379850138646475304951,
        "name": "Update Sub Name - Switch Plan 6192115800926177701960",
        "code":"1619215852Code"
    },
    "orderInformation": {
        "amountDetails": {
            "billingAmount": "13.23"
        }
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/subscriptions/1619215852",
            "method": "GET"
        },
        "update": {
            "href": "/rbs/v1/subscriptions/1619215852",
            "method": "PATCH"
        },
        "cancel": {
            "href": "/rbs/v1/subscriptions/1619215852/cancel",
            "method": "POST"
        }
    },
    "id": "1619215852",
    "status": "COMPLETED",
    "subscriptionInformation": {
        "code": "1619215852Code",
        "status": "PENDING"
    }
}
```

Error Response to a Failed Request

```
{
    "status": "INVALID_REQUEST",
    "reason": "INVALID_DATA",
    "message": "One or more fields in the request contains invalid data.",
    "details": [
        {
            "field": "subscriptionInformation.code",
            "reason": "DUPLICATE"
        }
    ]
}
```

Reactivating a Suspended Subscription {#recur-bill-activating-a-subscription}
=============================================================================

You can reactivate a suspended subscription for the next billing cycle. You cannot reactivate a canceled or completed subscription.  
You can specify whether you want to process missed payments for the period during which the subscription was suspended by setting the `processMissedPayments` query parameter to `true` or `false`. If no value is specified, the system will default to `true`.

> IMPORTANT
> The ` processMissedPayments ` query parameter is only effective when the *Ask each time before reactivating* option is selected in the reactivation settings. If any other option is chosen, the value provided in the request will be ignored by the system. For more information, see the [*Recurring Billing User Guide*](https://developer.cybersource.com/docs/cybs/en-us/recurring-billing/user/all/rest/recurring-billing-user/recurring-billing-user-about-guide.md "").  
> You can check how many payments were missed and the total amount by retrieving the subscription details, where you will find the reactivationInformation object. See [Retrieving a Subscription](/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev/recur-bill-subscriptions/recur-bill-getting-a-subscription.md "").  
> Follow these steps to re-activate a subscription:

1. In the endpoint path, include the subscription ID that you received when you retrieved a list of subscriptions.
2. (Optional) Specify whether you want to process skipped payments by setting the processMissedPayments query parameter to `true` or `false`. By default it is set to true. When any option other than **Ask each time before reactivating** is selected in the reactivation settings, the value that you enter will be ignored.
3. Send the request to the recurring billing endpoint:  
   Production: `POST https://api.cybersource.com/rbs/v1/subscriptions/{id}/activateactivate?processMissedPayments={true|false}`  
   Test: `POST https://apitest.cybersource.test.com/rbs/v1/subscriptions/{id}/activate?processMissedPayments={true|false}`
4. Verify that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").{#recur-bill-activating-a-subscription_d9e19}

REST Examples: Reactivating a Suspended Subscription {#recur-bill-activate-a-subscription-examples}
===================================================================================================

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/subscriptions/6149715492756032001956",
            "method": "GET"
        },
        "update": {
            "href": "/rbs/v1/subscriptions/6149715492756032001956",
            "method": "PATCH"
        },
        "cancel": {
            "href": "/rbs/v1/subscriptions/6149715492756032001956/cancel",
            "method": "POST"
        },
        "suspend": {
            "href": "/rbs/v1/subscriptions/6149715492756032001956/suspend",
            "method": "POST"
        }
    },
    "id": "6149715492756032001956",
    "status": "COMPLETED",
    "subscriptionInformation": {
        "code": "AWC-35",
        "status": "ACTIVE"
    }
}
```

Response to an Unsuccessful Request

```
{
    "status": "INVALID_REQUEST",
    "reason": "INVALID_DATA",
    "message": "The subscription cannot be reactivated at this time.",
    "details": [
        {
            "field": "subscriptionInformation.status",
            "reason": "INVALID_FOR_ACTIVATION"
        }
    ]
}
```

Suspending a Subscription {#recur-bill-suspending-a-subscription}
=================================================================

You can suspend a pending, active, or delinquent subscription. Subscriptions cannot be suspended 10 minutes before or after a payment begins processing.  
Follow these steps to suspend a subscription:

1. In the endpoint path, include the subscription ID that you received when you retrieved a list of subscriptions.
2. Send the request to the recurring billing endpoint:  
   Production: `POST https://api.cybersource.com/rbs/v1/subscriptions/{id}/suspend`  
   Test: `POST https://apitest.cybersource.test.com/rbs/v1/subscriptions/{id}/suspend`
3. Verify that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").{#recur-bill-suspending-a-subscription_d9e19}

REST Examples: Suspending a Subscription {#recur-bill-suspend-a-subscription-examples}
======================================================================================

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/subscriptions/6192112872526176101960",
            "method": "GET"
        },
        "update": {
            "href": "/rbs/v1/subscriptions/6192112872526176101960",
            "method": "PATCH"
        },
        "cancel": {
            "href": "/rbs/v1/subscriptions/6192112872526176101960/cancel",
            "method": "POST"
        },
        "suspend": {
            "href": "/rbs/v1/subscriptions/6192112872526176101960/suspend",
            "method": "POST"
        }
    },
    "id": "6192112872526176101960",
    "status": "ACCEPTED",
    "subscriptionInformation": {
        "code": "AWC-44",
        "status": "ACTIVE"
    }
}
```

Response to an Unsuccessful Request

```
{
    "status": "NOT_FOUND",
    "reason": "INVALID_DATA",
    "details": []
}
```

Canceling a Subscription {#recur-bill-canceling-a-subscription}
===============================================================

You can cancel a pending, active, suspended, or delinquent subscription. Subscriptions cannot be canceled within 10 minutes before or after a payment begins processing.  
Follow these steps to cancel a subscription:

1. In the endpoint path, include the subscription ID that you received when you retrieved a list of subscriptions.
2. Send the request to the recurring billing endpoint:  
   Production: `POST https://api.cybersource.com/rbs/v1/subscriptions/{id}/cancel`  
   Test: `POST https://apitest.cybersource.test.com/rbs/v1/subscriptions/{id}/cancel`
3. Verify that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").{#recur-bill-canceling-a-subscription_d9e19}

REST Examples: Canceling a Subscription {#recur-bill-cancel-a-subscription-examples}
====================================================================================

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/subscriptions/6192115800926177701960",
            "method": "GET"
        },
        "update": {
            "href": "/rbs/v1/subscriptions/6192115800926177701960",
            "method": "PATCH"
        },
        "cancel": {
            "href": "/rbs/v1/subscriptions/6192115800926177701960/cancel",
            "method": "POST"
        },
        "suspend": {
            "href": "/rbs/v1/subscriptions/6192115800926177701960/suspend",
            "method": "POST"
        }
    },
    "id": "6192115800926177701960",
    "status": "ACCEPTED",
    "subscriptionInformation": {
        "code": "6192177701960Code",
        "status": "ACTIVE"
    }
}
```

Error Response

```
{
    "status": "NOT_FOUND",
    "reason": "INVALID_DATA",
    "details": []
}
```

Retrieving a List of Payments in a Subscription {#retrieve-list-payments-in-sub}
================================================================================

When you retrieve a list of all past and future payments, the following details are included:

* **Total count** : Total number of payments retrieved in the subscriptionPayment object, including scheduled payments.
* **Cycles completed count**: Count of completed cycles grouped by their statuses.
* **Billing cycles to skip**: List of billing cycle numbers that are marked to be skipped.
* **Subscription payment** : List of details for each payment returned based on the applied filters:
  * **Payment ID**: Unique identifier generated by Recurring Billing.
  * **Payment status**: The current status of the payment.
  * **Payment type**: The type of payment.
  * **Transaction ID** : A unique identification number generated by `Cybersource` to identify the submitted request. Returned by all services.
  * **Payment date**: The date and time when the payment is processed.
  * **Payment currency**: Currency used for the order.
  * **Billing cycle start date**: The start date of the billing period associated with this payment.
  * **Billing cycle end date**: The end date of the billing period associated with this payment.
  * **Billing cycle number**: The billing cycle number.
  * **Payment number**: The sequential number of the payment within the subscription.
  * **Billing amount**: The amount billed for this payment.
  * **Setup fee**: The setup fee associated with the payment, if any.
  * **Surcharge amount**: The surcharge amount, if any.
  * **Surcharge description**: Description of the surcharge, if applicable.
  * **Modifiable**: Indicates whether the payment can be modified, skipped, or restored.
    {#retrieve-list-payments-in-sub_ul_xnz_2hs_cjc}

{#retrieve-list-payments-in-sub_ul_z4y_dhs_cjc}  
Follow these steps to retrieve a list of payments:

1. In the endpoint path, include the subscription ID.
2. Filter the list of subscriptions by using these query string parameters:
   1. `offset`: Number of items to be offset.
   2. `limit`: Number of items to be returned. Default is `20`, maximum is `100`.
   3. `scheduledPaymentsCount`: Number of existing scheduled payments to be returned. Default is `5`, maximum is `9999`. If the number of scheduled payments is lower than the specified value, the system returns only the existing ones.
      {#retrieve-list-payments-in-sub_ol_syx_f3s_cjc}
3. Send the request message to one of these endpoints:

{#retrieve-list-payments-in-sub_ol_l1z_lhs_cjc}  
Test: `GET https://``apitest.cybersource.com``/rbs/v1/subscriptions/{id}/payments`  
Production: `GET https://``api.cybersource.com``/rbs/v1/subscriptions/{id}/payments`  
4. Verify that the request was successful. A 200-level HTTP response code indicates success. For more information, see See [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

REST Examples: Retrieving a List of Payments in a Subscription {#retrieve-list-payments-in-sub-ex}
==================================================================================================

Successful Response

```
{
    "_links": {
        "self": {
            "href": "/rbs/v1/subscriptions/7713669249636014301951/payments",
            "method": "GET"
        },
        "update": {
            "href": "/rbs/v1/subscriptions/7713669249636014301951/payments",
            "method": "PUT"
        }
    },
    "submitTimeUtc": "2026-02-25T15:34:38.057Z",
    "totalCount": 6,
    "cyclesCompletedCount": {
        "paid": 1
    },
    "billingCyclesToSkip": [
        4,
        5
    ],
    "subscriptionPayment": [
        {
            "id": "20000214748364800000010011771366925290",
            "status": "SCHEDULED",
            "paymentType": "STANDARD",
            "date": "2026-07-17T09:00:00.000Z",
            "currency": "GBP",
            "billingStartDate": "2026-07-17T07:00:00.000Z",
            "billingEndDate": "2026-08-17T06:59:59.000Z",
            "billingCycle": "6",
            "paymentNumber": "6",
            "billingAmount": "250.00",
            "surchargeAmount": "0.00",
            "surchargeDescription": "Surcharge Description",
            "modifiable": true
        },
        {
            "id": "20000214748364800000010011771366925290",
            "status": "SCHEDULED_SKIPPED",
            "paymentType": "STANDARD",
            "date": "2026-06-17T09:00:00.000Z",
            "currency": "GBP",
            "billingStartDate": "2026-06-17T07:00:00.000Z",
            "billingEndDate": "2026-07-17T06:59:59.000Z",
            "billingCycle": "5",
            "paymentNumber": "5",
            "billingAmount": "250.00",
            "surchargeAmount": "0.00",
            "surchargeDescription": "Surcharge Description",
            "modifiable": true
        },
        {
            "id": "20000214748364800000010011771366925290",
            "status": "SCHEDULED_SKIPPED",
            "paymentType": "STANDARD",
            "date": "2026-05-17T09:00:00.000Z",
            "currency": "GBP",
            "billingStartDate": "2026-05-17T07:00:00.000Z",
            "billingEndDate": "2026-06-17T06:59:59.000Z",
            "billingCycle": "4",
            "paymentNumber": "4",
            "billingAmount": "250.00",
            "surchargeAmount": "0.00",
            "surchargeDescription": "Surcharge Description",
            "modifiable": true
        },
        {
            "id": "20000214748364800000010011771366925290",
            "status": "SCHEDULED",
            "paymentType": "STANDARD",
            "date": "2026-04-17T09:00:00.000Z",
            "currency": "GBP",
            "billingStartDate": "2026-04-17T07:00:00.000Z",
            "billingEndDate": "2026-05-17T06:59:59.000Z",
            "billingCycle": "3",
            "paymentNumber": "3",
            "billingAmount": "250.00",
            "surchargeAmount": "0.00",
            "surchargeDescription": "Surcharge Description",
            "modifiable": true
        },
        {
            "id": "20000214748364800000010011771366925290",
            "status": "SCHEDULED",
            "paymentType": "STANDARD",
            "date": "2026-03-17T09:00:00.000Z",
            "currency": "GBP",
            "billingStartDate": "2026-03-17T07:00:00.000Z",
            "billingEndDate": "2026-04-17T06:59:59.000Z",
            "billingCycle": "2",
            "paymentNumber": "2",
            "billingAmount": "250.00",
            "surchargeAmount": "0.00",
            "surchargeDescription": "Surcharge Description",
            "modifiable": true
        },
        {
            "id": "20000214748364800000010011771366925292",
            "status": "PAID",
            "paymentType": "STANDARD",
            "transactionID": "7713669249636014301951",
            "date": "2026-02-17T22:22:07.895Z",
            "currency": "GBP",
            "billingStartDate": "2026-02-17T08:00:00.000Z",
            "billingEndDate": "2026-03-17T06:59:59.000Z",
            "billingCycle": "1",
            "paymentNumber": "1",
            "billingAmount": "250.00",
            "setupFee": "10.00",
            "surchargeAmount": "0.00",
            "surchargeDescription": "Surcharge Description",
            "modifiable": false
        }
    ]
}
```

Error Response

```
{
    "submitTimeUtc": "2026-02-25T14:29:19.160Z",
    "status": "NOT_FOUND",
    "reason": "INVALID_DATA",
    "message": "Subscription with given ID not found."
}
```

Skipping or Restoring Payments Within a Subscription {#skip-restore-payment}
============================================================================

You can skip or restore a previously skipped payment for a specific billing cycle.
IMPORTANT Payment modification is only possible if the payment processing date has not yet been reached. Typically, this means up to 2 hours before the scheduled processing time.  
Follow these steps to skip or restore a payment for a specific billing cycle:

1. In the endpoint path, include the subscription ID.
2. In the request body, specify the billingCyclesToSkip array. This array is a list of future billing cycles that should be marked as skipped. These restrictions apply:
   1. A *retry* payment cannot be added to the list.
   2. A payment cannot be added (skipped) or removed (restored) if it is within two hours of its scheduled processing time.
      {#skip-restore-payment_ol_h5m_5ns_cjc}
3. Send the request to the Recurring Billing endpoint:

Production: `POST https://``api.cybersource.com``/rbs/v1/subscriptions/{id}/payments`  
Test: `POST https://``apitest.cybersource.com``/rbs/v1/subscriptions/{id}/payments`  
4. Verify that the request was successful. A 200-level HTTP response code indicates success. For more information, see See [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

REST Example: Skipping or Restoring a Payment in a Subscription {#skip-restore-payment-ex}
==========================================================================================

Request

```
{
  "billingCyclesToSkip": [
    4,
    5
  ]
}
```

Response to a Successful Request

```
{
  "_links": {
    "self": {
      "href": "/rbs/v1/subscriptions/7713669249636014301951/payments",
      "method": "GET"
    },
    "update": {
      "href": "/rbs/v1/subscriptions/7713669249636014301951/payments",
      "method": "PUT"
    }
  },
  "submitTimeUtc": "2026-02-25T15:34:05.337Z",
  "status": "COMPLETED",
  "billingCyclesToSkip": [
    4,
    5
  ]
}
```

Response to an Unsuccessful Request

```
{
  "submitTimeUtc": "2026-02-25T14:27:42.216Z",
  "status": "INVALID_REQUEST",
  "reason": "INVALID_DATA",
  "message": "One or more fields in the request contains invalid data.",
  "details": [
    {
      "field": "billingCyclesToSkip",
      "reason": "UNMODIFIABLE_PAYMENT_SKIP_ATTEMPT_CYCLE: 1"
    }
  ]
}
```

Error Response

```
{
  "submitTimeUtc": "2026-02-25T14:29:19.160Z",
  "status": "NOT_FOUND",
  "reason": "INVALID_DATA",
  "message": "Subscription with given ID not found."
}
```

Additional Features {#recur-bill-addl-feat}
===========================================

Recurring Billing includes these additional features.

System Retry Logic {#recur-bill-sys-retry}
==========================================

`Cybersource` automatically retries failed recurring payments based on the type of decline received from the service. The service retries the internal and external payment declines.  
If the Recurring Billing service encounters an internal processing error without sending the request out to the banking network, the service retries the payment until the error is resolved.  
If the recurring billing service encounters an external processing error when the request is sent out to the banking network, `Cybersource` retries the payment before changing the subscription status to suspended.  
If the issuer provides a reason code like Do Not Retry, `Cybersource` stops all retry attempts. `Cybersource` immediately updates the subscription status to suspended.  
The maximum number of retries is five times and is based on the billing frequency. During the retry period, `Cybersource` changes the subscription status to delinquent.  
This example shows the system retry logic based on the billing frequency:

* **Daily**: retry 1 hour later, 1 time
* **Monthly**: retry every 2 days, 5 times
* **Weekly**: retry every 1 day, 3 times
* **Yearly**: retry every 15 days, 3 times  
  For a recurring payment that has a custom billing frequency, the Recurring Billing service retries a failed payment based on the billing frequency. As an example, suppose a payment fails for a recurring billing on a 14-day cycle. The Recurring Billing Service uses the Daily retry logic and every 2 weeks uses the Weekly retry logic, even if the duration is the same.

Merchant-Initiated Transactions {#recur-bill-mit}
=================================================

For information about merchant-initiated transactions, see [Support for Merchant-Initiated Transactions and Credential-on-File for Relay, Mastercard, and Discover](https://support.example.com/s/article/Support-for-Merchant-Initiated-Transactions-and-Credential-on-File-for-Relay-Mastercard-and-Discover "").

Customer Notifications {#recur-bill-cust-not}
=============================================

The Recurring Billing service sends email notifications to customers using the email address stored on the customer token. The system sends notifications for three defined payment events:

* Prepayment notification: notification of an upcoming recurring payment.
* Successful payment notification: notification of a successful recurring payment.
* Failed payment notification: notification of recurring payment failure.  
  `Cybersource` sends email notifications from a `Cybersource` email address.
  IMPORTANT Some mandates require that customers are notified. If notifications are disabled, the merchant is responsible for sending notifications to satisfy any mandates requirements.  
  You can disable notifications in the Recurring Billing settings in the `Business Center`. For more information, see the [*Recurring Billing User Guide*](https://developer.cybersource.com/docs/cybs/en-us/recurring-billing/user/all/rest/recurring-billing-user/recurring-billing-user-about-guide.md "").

Example: Notification of Upcoming Subscription Payment
------------------------------------------------------

Hello,  
Your recurring subscription will be charged to your payment card on file on `${paymentDate}`.  
**Subscription ID** : `${subscriptionId}`  
**Subscription Name** : `${subscriptionName}`  
**Billing Amount** : `${billingAmount} ${currency}`  
**Set-up Fee** : `${setupFee} ${currency}`  
Thank you,  
`${merchantName}`

Example: Notification of Successful Subscription Payment
--------------------------------------------------------

Hello,  
Your recurring subscription has been successfully charged to your payment card on file.  
**Subscription ID** : `${subscriptionId}`  
**Subscription Name** : `${subscriptionName}`  
**Billing Amount** : `${billingAmount} ${currency}`  
**Set-up Fee** : `${setupFee} ${currency}`  
**Transaction ID** : `${transactionId}`  
**Transaction Date** : `${paymentDate}`  
Thank you,  
`${merchantName}`

Example: Notification of Failed Subscription Payment
----------------------------------------------------

Hello,  
Your recurring subscription has failed to charge to your payment card on file.  
**Subscription ID** : `${subscriptionId}`  
**Subscription Name** : `${subscriptionName}`  
**Billing Amount** : `${billingAmount} ${currency}`  
**Setup Fee** : `${setupFee} ${currency}`  
**Transaction ID** : `${transactionId}`  
**Transaction Date** : `${paymentDate}`  
Thank you,  
`${merchantName}`

`Decision Manager` Integration {#recur-bill-dm-int}
===================================================

Recurring transactions are considered low risk compared to unscheduled payments. Therefore, when the `Decision Manager` fraud detection system is enabled on your account, `Cybersource` does not submit recurring billing transactions to `Decision Manager` for fraud screening.  
For more information about the `Decision Manager`, you can access the documentation by logging in to the `Business Center`.

Account Updater Integration {#recur-bill-au}
============================================

Account Updater is integrated with the Recurring Billing functionality so that your customer subscriptions can be kept current with credit card data changes. These changes can include a new expiration date, a new credit card number, or a brand change such as a change from Relay to Mastercard.  
For more information relating to Account Updater, contact your `Cybersource` representative.

Related Information
-------------------

* [Account Updater Developer Guide](https://developer.cybersource.com/library/documentation/dev_guides/Account_Updater_UG/Account_Updater.pdf "")

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.
