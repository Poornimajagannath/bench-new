Installments Developer Guide {#install-plan-about-guide}
========================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
--------------------

This guide is for application developers integrating the Installments APIs to make use of the Relay Installments product. The Installments product has three `REST API`s that together enable the merchant to make a request for the installment plans available to a cardholder, confirm an installment plan selection by a cardholder, and cancel an active installment plan.

Conventions
-----------

These special statements are used in this document:

> IMPORTANT
> An *Important* statement contains information essential to successfully completing a task or learning a concept.

Customer Support
----------------

For support information about any service, visit the Support Center:  
<http://support.example.com>

Recent Revisions to This Document {#install-plan-doc-revisions}
===============================================================

25.09.01
--------

Added support for these new response fields for a Get Installments Plans request. For more information, see the response examples in [Get Installment Plans](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-get-plan.md "") and the field descriptions in [Installments REST API Fields](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro.md "").

* installmentInformation.planDetails. amountDetails.totalAmountExcluding UpfrontFee
* installmentInformation. planDetails.amountDetails.currency
* installmentInformation. planDetails.fundedBy
* installmentInformation. planDetails.isIslamicPlan
* installmentInformation. planDetails.amountDetails.fees.monthlyRatePercentage

24.12.03
--------

Corrected the endpoint for the select installment plan request to:  
**Production** : `POST ``https://api.cybersource.com``/fin/v1/plan-acceptance/`  
**Test** : `POST ``https://apitest.cybersource.com``/fin/v1/plan-acceptance/`  
For more information, see [Select Installment Plan](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-select-plan.md "").

24.04.02
--------

Updated the description for the installmentInformation.planDetails\[\].identifier field. See [installmentInformation.planDetails\[\].identifier](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-plan-details-id.md "").

24.02.01
--------

Added the installment refund workflow. See [How to Refund an Installment Payment](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/installment-plans-overview/installment-plan-refund-flow.md "").  
Updated the get installment plans section to include information about the installmentInformation.planDetails\[\].identifier response field. See [Get Installment Plans](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-get-plan.md "") and [installmentInformation.planDetails\[\].identifier](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-plan-details-id.md "").  
Updated the cancel installment plan section to include information about the requirements for cancelling a plan. See [Cancel Installment Plan](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-cancel-plan-intro.md "").

23.03.01
--------

Initial release.

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.

Introduction to Installments {#installment-plans-overview}
==========================================================

The Installments API enables you to offer card-based installment plans to your customers. These installment payments are provided by participating issuing banks to their customers.  
An installment payment is one in a series of payments that constitute a single purchase of goods or services. They are billed to a customer in multiple transactions over a period of time agreed to by you and the customer. The agreement enables you to charge a specific amount at specified intervals. For example, a single purchase can be paid over a 3, 6, or 12-month period depending on the plan's set up by the issuing banks. The customer's credit or debit card statement reflect the installment amount instead of the full purchase amount.  
Installments services are processed using one of these payment identifiers:

* Primary Account Number (PAN)
* Payment Account Reference (PAR)
* Token

In addition to the customer's payment information, choosing and cancelling an installment plan also requires one of these authorization transaction IDs:

* Authorization code
* Network Transaction ID (NTID)

{#installment-plans-overview_ul_p2k_kv4_jyb}

Requirements
------------

You must complete these requirements before you can begin using the Installments API:

**`Cybersource` Merchant ID**
:
To sign up for a sandbox account, see the [Sandbox Account Sign Up](https://developer.example.com/hello-world/sandbox.md "") page.

REST API Key
:
To create a REST API key with an existing organization or merchant account, see the [*Creating and Using Security Keys User Guide*](https://developer.example.com/docs/vas/en-us/security-keys/user/all/ada/security-keys/keys-intro.md ""). If you sign up for a sandbox account, the sign up process creates a test key.

Getting Started with the REST API
:
To begin implementing the Installments API, you must set up your system to be REST compliant. When using REST, you must set up secure communications between your client and server using a **JSON Web Token** or an **HTTP signature** . For more information, see the [*Getting Started with the REST API*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md ""). If you need to set up your system to be REST compliant, the set up process creates a sandbox account and a test key.

Authentication {#install-plan-authentication}
=============================================

Two forms of authentication are available:

* **JSON Web Token** : Requires that you sign a P12 Certificate. See [Creating a P12 Certificate](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-security-p12-intro.md "").
* **HTTP Signature** : Hash-based method that uses a shared secret key. See [Creating a Shared Secret Key Pair](https://developer.cybersource.com/docs/cybs/en-us/platform/get-started/all/rest/get-started-rest/authentication/createSharedKey.md "") for HTTP Signature Authentication.
  {#install-plan-authentication_ul_gxt_hmt_z5b}

How to Process a Installment Payment {#installment-plan-workflow}
=================================================================

This workflow describes the sequence of events that comprise a successful installment payment.

#### Figure:

Installments Payment Workflow  
![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/installment-plans/images/installments-flow.svg/jcr:content/renditions/original)

1. The customer begins to checkout on the merchant website and inputs their payment credentials in one of three ways:
   * Enters their primary account number (PAN) information.
   * Enters their primary account reference (PAR) information.
   * Chooses a credential-on-file (COF).
     {#installment-plan-workflow_ul_lg3_rz3_kxb}
2. The merchant sends a get installment plans API request to `Cybersource` with the customer's PAN, PAR, or token information. See [Get Installment Plans](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-get-plan.md "").
3. `Cybersource` sends the merchant a list of installment plan options that include plan IDs.
4. The merchant displays the list of installment plan options to the customer.
5. The customer selects an installment plan.
6. The merchant sends an authorization API request for the full amount of the customer's purchase using the payment information that the customer provided.
7. `Cybersource` sends the merchant an `AUTHORIZED` status and either an authorization code or an NTID.
8. The merchant sends a select installment plan API request to `Cybersource` to link the authorization to the chosen installment plan. The merchant includes either the authorization code or NTID from the authorization response and the chosen installment plan ID in the request. See [Select Installment Plan](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-select-plan.md "").
9. `Cybersource` sends an `ACCEPTED` status to the merchant as confirmation that the selected plan was approved.
10. The merchant sends a capture API request to `Cybersource` to complete the payment.
11. `Cybersource` sends a `PENDING` status to the merchant.

How to Refund an Installment Payment {#installment-plan-refund-flow}
====================================================================

This workflow describes the sequence of events that comprise a successful installment refund. Before you can refund an installment payment, you must complete a payment using an installment plan. See [How to Process a Installment Payment](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/installment-plans-overview/installment-plan-workflow.md "").

#### Figure:

Installments Refund Workflow ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/installment-plans/images/installments-refund-flow.svg/jcr:content/renditions/original)

1. The customer returns the purchased goods to the merchant.
2. The merchant sends a refund API request to `Cybersource`.
3. `Cybersource` sends a `PENDING` status to the merchant.
4. The merchant sends a cancel installment plan API request to `Cybersource`. See [Cancel Installment Plan](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-cancel-plan-intro.md "").
5. `Cybersource` sends an `ACCEPTED` status to the merchant.
6. The merchant displays a confirmation to the customer that the refund and installment plan cancellation are complete.

Get Installment Plans {#install-plan-get-plan}
==============================================

You can request the retrieval of the available installment plans when the customer has selected their payment method during checkout. The payment method that the customer chooses determines the fields in the API request.  
You can get installment plans using one of these payment identifiers:

* [PAN](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-get-plan/install-plan-get-plan-intro.md "")
* [PAR](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-get-plan/install-plan-get-plan-par-intro.md "")
* [Token](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-get-plan/install-plan-get-plan-token-intro.md "")
  {#install-plan-get-plan_ul_jb2_ztf_gyb}

PAN {#install-plan-get-plan-intro}
==================================

The *get installment plans* API request provides a complete list of eligible installment offers to a customer during checkout. This request validates the eligibility of a payment transaction for installment plans and verifies participating issuer conditions for eligibility. For example, the request verifies the minimum and maximum plan amount.  
When you retrieve installment plans, these conditions apply:

* A successful response includes one or more eligible installment plans.
* If no active plans match the set of criteria, the response returns an empty array.
* Plans that are expired or plans that expire within the next 24 hours are not returned in the response.

PAN Information {#install-plan-get-plan-intro_pan}
--------------------------------------------------

To include the customer's PAN in the request, set the paymentInformation.card.number field to the customer's card number.

Endpoint {#install-plan-get-plan-intro_get-plan-endpoint-section}
-----------------------------------------------------------------

**Production** : `POST ``https://api.cybersource.com``/fin/v1/plans/`  
**Test** : `POST ``https://apitest.cybersource.com``/fin/v1/plans/`

Successful Response {#install-plan-get-plan-intro_success-response}
-------------------------------------------------------------------

A successful response includes these fields and values that you will need to store for follow-on API requests:

[installmentInformation.planDetails\[\].identifier](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-plan-details-id.md "")
:
The field value is the *plan registration system identifier* . Certain countries require you to include the plan registration system identifier in the installmentInformation.planDetails\[\].identifier field when you send the initial authorization request. Contact your `Cybersource` account manager for more information.

installmentInformation.planDetails.planId
:
The field value is the plan ID. Include the plan ID in the installmentInformation.planId field when you send a select installment plan API request.

Required Fields for Getting Installment Plans with a PAN {#install-plan-get-plan-reqfields}
===========================================================================================

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[processingInformation.installmentServiceProvider](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-instal-serv-prdr.md "")
:
Set to `Relay`.

Optional Field for Installment Services {#install-plan-opt-fields}
==================================================================

[merchantInformation.categoryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-category-code-a.md "")
:

`REST API` Example: Get Installment Plans with a PAN {#install-plan-get-plan-ex-rest}
=====================================================================================

Request

```
{
  "processingInformation": {
    "installmentServiceProvider": "Relay"
  },
  "paymentInformation": {
    "card": {
      "number": "XX5180126342040"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "3000",
      "currency": "QAR"
    }
  }
}
```

Response to Successful Request

```
{
  "id": "7519136615676057303812",
  "submitTimeUtc": "2025-07-07T18:41:01Z",
  "status": "ACCEPTED",
  "processorInformation": {
    "responseCode": "200"
  },
  "installmentInformation": {
    "planDetails": [
      {
        "planId": "7014ef25-54db-7286-b693-1874fe665002",
        "identifier": "000000015D",
        "planName": "6MonthsIslamicPlan",
        "planType": "ISSUER_DEFAULT",
        "totalCount": "6",
        "frequency": "MONTHLY",
        "shariaLawPlan": true,
        "fundedBy": [
          "CONSUMER"
        ],
        "amountDetails": {
          "lastInstallmentAmount": "500.00",
          "totalFeeAmount": "100.00",
          "totalUpfrontFeeAmount": "100.00",
          "totalRecurringFeeAmount": "0.00",
          "totalPlanAmount": "3100.00",
          "interestRate": "0.00",
          "fees": [
            {
              "type": "CONSUMER_UPFRONT",
              "ratePercentage": "0.00",
              "flatFeeAmount": "100.00"
            },
            {
              "type": "CONSUMER",
              "ratePercentage": "0.00",
              "flatFeeAmount": "0.00",
              "monthlyRatePercentage": "0.00"
            }
          ],
          "firstInstallment": {
            "feeAmount": "0.00",
            "amount": "500.00",
            "upfrontFeeAmount": "100.00",
            "totalAmountExcludingUpfrontFee": "500.00"
          },
          "lastInstallment": {
            "feeAmount": "0.00",
            "amount": "500.00"
          },
          "currency": "QAR"
        },
        "termsAndConditions": [
          {
            "tncUrl": https://www.relay.com/,
            "version": "1",
            "text": "بنك الاختبار هذا نص الشروط والأحكام الذي يحكم خدمات تقسيط التأشيرة\n\nالأهلية: لكي تكون مؤهلاً للحصول على مدفوعات التقسيط بالفيزا، يجب أن تمتلك بطاقة ائتمان فيزا صالحة ونشطة صادرة عن بنك معتمد. سيحدد حدك الائتماني وقدرتك على السداد مدى أهليتك لخطط التقسيط\n\nخطة التقسيط: يمكن الاستفادة من الأقساط لمدة ثلاثة أشهر للمشتريات لدى التجار المشاركين، مع مراعاة الحد الأدنى لمبلغ المعاملة. سيتم تحديد تفاصيل خطة التقسيط المحددة في وقت الشراء\n\nالفوائد والرسوم: لا توجد رسوم مطبقة على خطة التقسيط لمدة ثلاثة أشهر. إذا فشلت في سداد أي قسط في الموعد المحدد، لن يتم فرض رسوم التأخر في السداد\n\nالدفع المسبق والإلغاء: يمكنك اختيار الدفع المسبق لكامل المبلغ المستحق في أي وقت دون أي رسوم. يمكن إلغاء خطة التقسيط إذا تم إلغاء بطاقة فيزا الخاصة بك أو إذا تخلفت عن السداد\n\nتغييرات على الشروط: تحتفظ Relay بالحق في تغيير هذه الشروط والأحكام في أي وقت. سيتم إبلاغك بأي تغييرات عبر البريد الإلكتروني أو من خلال موقعنا. تقع على عاتقك مسؤولية إبقاء نفسك على اطلاع بأحدث الشروط والأحكام\n\nيرجى ملاحظة أن هذه الشروط عرضة للتغيير ويوصى دائمًا بقراءة الشروط والأحكام الفعلية المقدمة من جهة إصدار البطاقة\n\n\n\n\n",
            "languageCode": "ara"
          },
          {
            "tncUrl": https://www.relay.com/,
            "version": "1",
            "text": " [Test Bank] This is a sample T&C text containing Special Ch@racters that govern the Relay Installment services. Refer to https://www.relay.com for more information. 1) Eligibility: To be eligible for \"Relay installment\" payments, you must hold a valid and active Relay credit card issued by an authorized bank. Your credit limit and repayment capacity will determine your eligibility for installment plans. 2) Installment Plan: Installments can be availed for purchases at participating merchants, subject to a minimum transaction amount. The specific installment plan (number of months, interest rate, etc.) will be determined at the time of purchase. 3) Interest &amp; Fees: 20% Interest will be charged on the unpaid principal amount. If you fail to pay any installment by the due date, a late payment fee will be charged. All fees/charges are non-refundable and subject to change. 4) Prepayment &amp; Cancellation: You may choose to prepay the entire outstanding amount at any time. However, prepayment may attract a fee. The installment plan can be cancelled if your Relay card is cancelled &lt;or if you default on payment&gt;. 5) Changes to Terms: Relay reserves the right to change these terms and conditions at any time. Any changes will be communicated to you via email or through our website. It is your responsibility to keep yourself updated with the latest terms and conditions. Please note that these terms are subject to change and it's always recommended to read the actual terms and conditions provided by the card issuer.\n",
            "languageCode": "eng"
          }
        ]
      },
      {
        "planId": "8c7cbb0f-b860-0d68-f06d-1fafb6375102",
        "identifier": "000000015E",
        "planName": "3MonthsIslamicPlan",
        "planType": "ISSUER_DEFAULT",
        "totalCount": "3",
        "frequency": "MONTHLY",
        "shariaLawPlan": true,
        "fundedBy": [
          "CONSUMER"
        ],
        "amountDetails": {
          "lastInstallmentAmount": "1000.00",
          "totalFeeAmount": "0.00",
          "totalUpfrontFeeAmount": "0.00",
          "totalRecurringFeeAmount": "0.00",
          "totalPlanAmount": "3000.00",
          "interestRate": "0.00",
          "fees": [
            {
              "type": "CONSUMER_UPFRONT",
              "ratePercentage": "0.00",
              "flatFeeAmount": "0.00"
            },
            {
              "type": "CONSUMER",
              "ratePercentage": "0.00",
              "flatFeeAmount": "0.00",
              "monthlyRatePercentage": "0.00"
            }
          ],
          "firstInstallment": {
            "feeAmount": "0.00",
            "amount": "1000.00",
            "upfrontFeeAmount": "0.00",
            "totalAmountExcludingUpfrontFee": "1000.00"
          },
          "lastInstallment": {
            "feeAmount": "0.00",
            "amount": "1000.00"
          },
          "currency": "QAR"
        },
        "termsAndConditions": [
          {
            "tncUrl": https://www.relay.com/,
            "version": "1",
            "text": " [Test Bank] This is a sample T&amp;C text containing Special Ch@racters that govern the Relay Installment services. Refer to https://www.relay.com for more information. 1) Eligibility: To be eligible for \"Relay installment\" payments, you must hold a valid and active Relay credit card issued by an authorized bank. Your credit limit and repayment capacity will determine your eligibility for installment plans. 2) Installment Plan: Installments can be availed for purchases at participating merchants, subject to a minimum transaction amount. The specific installment plan (number of months, interest rate, etc.) will be determined at the time of purchase. 3) Interest &amp; Fees: 20% Interest will be charged on the unpaid principal amount. If you fail to pay any installment by the due date, a late payment fee will be charged. All fees/charges are non-refundable and subject to change. 4) Prepayment &amp; Cancellation: You may choose to prepay the entire outstanding amount at any time. However, prepayment may attract a fee. The installment plan can be cancelled if your Relay card is cancelled &lt;or if you default on payment&gt;. 5) Changes to Terms: Relay reserves the right to change these terms and conditions at any time. Any changes will be communicated to you via email or through our website. It is your responsibility to keep yourself updated with the latest terms and conditions. Please note that these terms are subject to change and it's always recommended to read the actual terms and conditions provided by the card issuer.",
            "languageCode": "eng"
          },
          {
            "tncUrl": https://www.relay.com/,
            "version": "1",
            "text": " [بنك الاختبار] هذا نموذج لنص الشروط والأحكام الذي يحتوي على فروع خاصة تحكم خدمات تقسيط التأشيرة.\n\n1) الأهلية: لكي تكون مؤهلاً للحصول على مدفوعات \"التقسيط بالفيزا\"، يجب أن تمتلك بطاقة ائتمان فيزا صالحة ونشطة صادرة عن بنك معتمد. سيحدد حدك الائتماني وقدرتك على السداد مدى أهليتك لخطط التقسيط.\n\n2) خطة التقسيط: يمكن الاستفادة من الأقساط للمشتريات لدى التجار المشاركين، مع مراعاة الحد الأدنى لمبلغ المعاملة. سيتم تحديد خطة التقسيط المحددة (عدد الأشهر، وسعر الفائدة، وما إلى ذلك) في وقت الشراء.\n\n3) الفوائد والرسوم: سيتم فرض فائدة بنسبة 20% على المبلغ الأصلي غير المدفوع. إذا فشلت في سداد أي قسط في الموعد المحدد، سيتم فرض رسوم التأخر في السداد. جميع الرسوم/المصاريف غير قابلة للاسترداد وقابلة للتغيير.\n\n4) الدفع المسبق والإلغاء: يمكنك اختيار الدفع المسبق لكامل المبلغ المستحق في أي وقت. ومع ذلك، قد يجذب الدفع المسبق رسومًا. يمكن إلغاء خطة التقسيط إذا تم إلغاء بطاقة فيزا الخاصة بك &lt;أو إذا تخلفت عن السداد&gt;.\n\n5) تغييرات على الشروط: تحتفظ Relay بالحق في تغيير هذه الشروط والأحكام في أي وقت. سيتم إبلاغك بأي تغييرات عبر البريد الإلكتروني أو من خلال موقعنا. تقع على عاتقك مسؤولية إبقاء نفسك على اطلاع بأحدث الشروط والأحكام.\n\nيرجى ملاحظة أن هذه الشروط عرضة للتغيير ويوصى دائمًا بقراءة الشروط والأحكام الفعلية المقدمة من جهة إصدار البطاقة.",
            "languageCode": "ara"
          }
        ]
      }
    ]
  }
}
```

PAR {#install-plan-get-plan-par-intro}
======================================

The *get installment plans* API request provides a complete list of eligible installment offers to a customer during checkout. This request validates the eligibility of a payment transaction for installment plans and verifies participating issuer conditions for eligibility. For example, the request verifies the minimum and maximum plan amount.  
When you retrieve installment plans, these conditions apply:

* A successful response includes one or more eligible installment plans.
* If no active plans match the set of criteria, the response returns an empty array.
* Plans that are expired or plans that expire within the next 24 hours are not returned in the response.

PAR Information {#install-plan-get-plan-par-intro_par}
------------------------------------------------------

Include the customer's PAR in the service request with the paymentInformation.paymentAccountReference.id field.

Endpoint
--------

**Production** : `POST ``https://api.cybersource.com``/fin/v1/plans/`  
**Test** : `POST ``https://apitest.cybersource.com``/fin/v1/plans/`

Successful Response
-------------------

A successful response includes these fields and values that you will need to store for follow-on API requests:

[installmentInformation.planDetails\[\].identifier](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-plan-details-id.md "")
:
The field value is the *plan registration system identifier* . Certain countries require you to include the plan registration system identifier in the installmentInformation.planDetails\[\].identifier field when you send the initial authorization request. Contact your `Cybersource` account manager for more information.

installmentInformation.planDetails.planId
:
The field value is the plan ID. Include the plan ID in the installmentInformation.planId field when you send a select installment plan API request.

Required Fields for Getting Installment Plans with a PAR {#install-plan-get-plan-par-reqfields}
===============================================================================================

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.paymentAccountReference.id](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/payment-info-pay-acct-ref-id.md "")
:

[processingInformation.installmentServiceProvider](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-instal-serv-prdr.md "")
:
Set to `Relay`.

`REST API` Example: Get Installment Plans with a PAR {#install-plan-get-plan-par-ex-rest}
=========================================================================================

Use this example request when using a PAR to retrieve installment plans.  
Request

```
{
  "processingInformation": {
    "installmentServiceProvider": "Relay"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "500",
      "currency": "USD"
    }
  }
}
```

Response

```
{
  "id": "7557015952466642304806",
  "submitTimeUtc": "2025-08-20T14:53:15Z",
  "status": "ACCEPTED",
  "processorInformation": {
    "responseCode": "200"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  },
  "installmentInformation": {
    "planDetails": [
      {
        "planId": "49ae7aa2-68ec-5f33-fd51-12fd51a2a601",
        "planName": "WithManyFees",
        "planType": "ISSUER_PROMOTION",
        "totalCount": "2",
        "frequency": "BIWEEKLY",
        "fundedBy": [
          "CONSUMER"
        ],
        "amountDetails": {
          "lastInstallmentAmount": "250.00",
          "totalFeeAmount": "18.00",
          "totalUpfrontFeeAmount": "6.00",
          "totalRecurringFeeAmount": "12.00",
          "totalPlanAmount": "518.00",
          "interestRate": "0.00",
          "fees": [
            {
              "type": "CONSUMER",
              "ratePercentage": "2.00",
              "flatFeeAmount": "2.00",
              "monthlyRatePercentage": "2.00"
            },
            {
              "type": "CONSUMER_UPFRONT",
              "ratePercentage": "0.00",
              "flatFeeAmount": "6.00"
            }
          ],
          "firstInstallment": {
            "feeAmount": "6.00",
            "amount": "250.00",
            "upfrontFeeAmount": "6.00",
            "totalAmountExcludingUpfrontFee": "256.00"
          },
          "lastInstallment": {
            "feeAmount": "6.00",
            "amount": "250.00"
          },
          "currency": "USD"
        },
        "termsAndConditions": [
          {
            "version": "1",
            "text": "This is just another Test",
            "languageCode": "eng"
          }
        ]
      },
      {
        "planId": "a811fe1f-2627-cde9-29b7-1a19577f0901",
        "planName": "ConsumerTestPlan1",
        "planType": "ISSUER_PROMOTION",
        "totalCount": "12",
        "frequency": "MONTHLY",
        "fundedBy": [
          "CONSUMER"
        ],
        "amountDetails": {
          "lastInstallmentAmount": "41.63",
          "totalFeeAmount": "0.00",
          "totalUpfrontFeeAmount": "0.00",
          "totalRecurringFeeAmount": "0.00",
          "totalPlanAmount": "500.00",
          "interestRate": "10.00",
          "fees": [
            {
              "type": "CONSUMER",
              "ratePercentage": "0.00",
              "flatFeeAmount": "0.00",
              "monthlyRatePercentage": "0.00"
            },
            {
              "type": "CONSUMER_UPFRONT",
              "ratePercentage": "0.00",
              "flatFeeAmount": "0.00"
            }
          ],
          "firstInstallment": {
            "feeAmount": "0.00",
            "amount": "41.67",
            "upfrontFeeAmount": "0.00",
            "totalAmountExcludingUpfrontFee": "41.67"
          },
          "lastInstallment": {
            "feeAmount": "0.00",
            "amount": "41.63"
          },
          "currency": "USD"
        },
        "termsAndConditions": [
          {
            "version": "1",
            "text": "You are selecting a 12 month installment plan. The total purchase amount will be deducted from your available credit limit. As set forth in your terms, your installment fee will be 10% APR for 12 months. If you miss an installment payment, the standard rate for purchases will apply to the remaining installment balance.",
            "languageCode": "eng"
          }
        ]
      },
      {
        "planId": "9b6a2573-f532-2779-1cd2-1f054fdf9001",
        "identifier": "000000002K",
        "planName": "BilarterConsumerPlan1",
        "planType": "ISSUER_PROMOTION",
        "totalCount": "12",
        "frequency": "MONTHLY",
        "promotionId": "123",
        "fundedBy": [
          "CONSUMER"
        ],
        "amountDetails": {
          "lastInstallmentAmount": "41.63",
          "totalFeeAmount": "55.00",
          "totalUpfrontFeeAmount": "30.00",
          "totalRecurringFeeAmount": "25.00",
          "totalPlanAmount": "555.00",
          "interestRate": "0.00",
          "fees": [
            {
              "type": "CONSUMER",
              "ratePercentage": "5.00",
              "flatFeeAmount": "0.00",
              "monthlyRatePercentage": "0.42"
            },
            {
              "type": "CONSUMER_UPFRONT",
              "ratePercentage": "6.00",
              "flatFeeAmount": "0.00"
            }
          ],
          "firstInstallment": {
            "feeAmount": "2.08",
            "amount": "41.67",
            "upfrontFeeAmount": "30.00",
            "totalAmountExcludingUpfrontFee": "43.75"
          },
          "lastInstallment": {
            "feeAmount": "2.12",
            "amount": "41.63"
          },
          "currency": "USD"
        },
        "termsAndConditions": [
          {
            "version": "1",
            "text": "blah blah",
            "languageCode": "tel"
          }
        ]
      },
      {
        "planId": "23e950ef-021b-ca06-a797-11c7456c5201",
        "identifier": "00000000RN",
        "planName": "CybersourcePlanArabic",
        "planType": "ISSUER_DEFAULT",
        "totalCount": "12",
        "frequency": "MONTHLY",
        "fundedBy": [
          "MERCHANT"
        ],
        "amountDetails": {
          "lastInstallmentAmount": "41.63",
          "totalFeeAmount": "0.00",
          "totalUpfrontFeeAmount": "0.00",
          "totalRecurringFeeAmount": "0.00",
          "totalPlanAmount": "500.00",
          "interestRate": "0.00",
          "fees": [
            {
              "type": "CONSUMER_UPFRONT",
              "ratePercentage": "0.00",
              "flatFeeAmount": "0.00"
            },
            {
              "type": "CONSUMER",
              "ratePercentage": "0.00",
              "flatFeeAmount": "0.00",
              "monthlyRatePercentage": "0.00"
            }
          ],
          "firstInstallment": {
            "feeAmount": "0.00",
            "amount": "41.67",
            "upfrontFeeAmount": "0.00",
            "totalAmountExcludingUpfrontFee": "41.67"
          },
          "lastInstallment": {
            "feeAmount": "0.00",
            "amount": "41.63"
          },
          "currency": "USD"
        },
        "termsAndConditions": [
          {
            "version": "2",
            "text": "أنت تختار خطة التقسيط لمدة 12 شهرًا مع رسوم أو رسوم تمويل تبلغ 13.99% من إجمالي مبلغ الشراء - تم الكشف عنها على أنها \"رسوم\" أعلاه. دفعة خطة التقسيط الشهرية هي إجمالي مبلغ الشراء بالإضافة إلى الرسوم، وكلها مقسمة بالتساوي على عدد x من دورات الفوترة. سيتم تضمين أول دفعة شهرية لخطة التقسيط كجزء من الحد الأدنى للدفعة في كشف حسابك التالي. يرجى الرجوع إلى اتفاقية حامل البطاقة الخاصة بك لمعرفة عواقب عدم سداد دفعات خطة التقسيط. إذا تم سداد أي خطة تقسيط مبكرًا، فلن يتم تقييم جزء الرسوم المرتبط بالأشهر التالية للدفع",
            "languageCode": "ara"
          }
        ]
      }
    ]
  }
}
```

Token {#install-plan-get-plan-token-intro}
==========================================

The *get installment plans* API request provides a complete list of eligible installment offers to a customer during checkout. This request validates the eligibility of a payment transaction for installment plans and verifies participating issuer conditions for eligibility. For example, the request verifies the minimum and maximum plan amount.  
When you retrieve installment plans, these conditions apply:

* A successful response includes one or more eligible installment plans.
* If no active plans match the set of criteria, the response returns an empty array.
* Plans that are expired or plans that expire within the next 24 hours are not returned in the response.

Token Information {#install-plan-get-plan-token-intro_token}
------------------------------------------------------------

Include the token information in the service request with one of these token identifier fields:

* Flex API transient token: tokenInformation.transientTokenJwt
* `TMS` customer token: paymentInformation.customer.id
* `TMS` instrument identifier token: paymentInformation.instrumentIdentifier.id
* `TMS` payment instrument token: paymentInformation.paymentInstrument.id
* `TMS` transient token: tokenInformation.jti

{#install-plan-get-plan-token-intro_ul_cls_pmx_fyb}  
For more information about token types, see the [Token Types](https://developer.cybersource.com/docs/cybs/en-us/tms/developer/ctv/rest/tms/tms-overview/tms-token-types.md "") section in the *`Token Management Service` Developer Guide*.

Endpoint
--------

**Production** : `POST ``https://api.cybersource.com``/fin/v1/plans/`  
**Test** : `POST ``https://apitest.cybersource.com``/fin/v1/plans/`

Successful Response
-------------------

A successful response includes these fields and values that you will need to store for follow-on API requests:

[installmentInformation.planDetails\[\].identifier](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-plan-details-id.md "")
:
The field value is the *plan registration system identifier* . Certain countries require you to include the plan registration system identifier in the installmentInformation.planDetails\[\].identifier field when you send the initial authorization request. Contact your `Cybersource` account manager for more information.

installmentInformation.planDetails.planId
:
The field value is the plan ID. Include the plan ID in the installmentInformation.planId field when you send a select installment plan API request.

Required Fields for Getting Installment Plans with a Token {#install-plan-get-plan-token-reqfields}
===================================================================================================

Include these fields to retrieve a list of installment plans.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[processingInformation.installmentServiceProvider](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-instal-serv-prdr.md "")
:
Set to `Relay`.

Required Token Fields {#install-plan-get-plan-token-reqfields_token-fields}
---------------------------------------------------------------------------

Include only one of these token identifier fields:

[paymentInformation.customer.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-customer-id.md "")
:

[paymentInformation.instrumentIdentifier.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-instrument-identifier-id.md "")
:

[paymentInformation.paymentInstrument.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-instrument-id.md "")
:

[tokenInformation.jti](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-jti.md "")
:

[tokenInformation.transientTokenJwt](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-transient-token-jwt.md "")
:

`REST API` Example: Get Installment Plans with a Token {#install-plan-get-plan-token-ex-rest}
=============================================================================================

Request

```
{
  "processingInformation": {
    "installmentServiceProvider": "Relay"
  },
  "paymentInformation": {
    "instrumentIdentifier": {
      "id": "7030000000012249793"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "500",
      "currency": "USD"
    }
  }
}
```

Response

```
{
  "id": "7557016618136534704807",
  "submitTimeUtc": "2025-08-20T14:54:21Z",
  "status": "ACCEPTED",
  "processorInformation": {
    "responseCode": "200"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  },
  "installmentInformation": {
    "planDetails": [
      {
        "planId": "49ae7aa2-68ec-5f33-fd51-12fd51a2a601",
        "planName": "WithManyFees",
        "planType": "ISSUER_PROMOTION",
        "totalCount": "2",
        "frequency": "BIWEEKLY",
        "fundedBy": [
          "CONSUMER"
        ],
        "amountDetails": {
          "lastInstallmentAmount": "250.00",
          "totalFeeAmount": "18.00",
          "totalUpfrontFeeAmount": "6.00",
          "totalRecurringFeeAmount": "12.00",
          "totalPlanAmount": "518.00",
          "interestRate": "0.00",
          "fees": [
            {
              "type": "CONSUMER",
              "ratePercentage": "2.00",
              "flatFeeAmount": "2.00",
              "monthlyRatePercentage": "2.00"
            },
            {
              "type": "CONSUMER_UPFRONT",
              "ratePercentage": "0.00",
              "flatFeeAmount": "6.00"
            }
          ],
          "firstInstallment": {
            "feeAmount": "6.00",
            "amount": "250.00",
            "upfrontFeeAmount": "6.00",
            "totalAmountExcludingUpfrontFee": "256.00"
          },
          "lastInstallment": {
            "feeAmount": "6.00",
            "amount": "250.00"
          },
          "currency": "USD"
        },
        "termsAndConditions": [
          {
            "version": "1",
            "text": "This is just another Test",
            "languageCode": "eng"
          }
        ]
      },
      {
        "planId": "a811fe1f-2627-cde9-29b7-1a19577f0901",
        "planName": "ConsumerTestPlan1",
        "planType": "ISSUER_PROMOTION",
        "totalCount": "12",
        "frequency": "MONTHLY",
        "fundedBy": [
          "CONSUMER"
        ],
        "amountDetails": {
          "lastInstallmentAmount": "41.63",
          "totalFeeAmount": "0.00",
          "totalUpfrontFeeAmount": "0.00",
          "totalRecurringFeeAmount": "0.00",
          "totalPlanAmount": "500.00",
          "interestRate": "10.00",
          "fees": [
            {
              "type": "CONSUMER",
              "ratePercentage": "0.00",
              "flatFeeAmount": "0.00",
              "monthlyRatePercentage": "0.00"
            },
            {
              "type": "CONSUMER_UPFRONT",
              "ratePercentage": "0.00",
              "flatFeeAmount": "0.00"
            }
          ],
          "firstInstallment": {
            "feeAmount": "0.00",
            "amount": "41.67",
            "upfrontFeeAmount": "0.00",
            "totalAmountExcludingUpfrontFee": "41.67"
          },
          "lastInstallment": {
            "feeAmount": "0.00",
            "amount": "41.63"
          },
          "currency": "USD"
        },
        "termsAndConditions": [
          {
            "version": "1",
            "text": "You are selecting a 12 month installment plan. The total purchase amount will be deducted from your available credit limit. As set forth in your terms, your installment fee will be 10% APR for 12 months. If you miss an installment payment, the standard rate for purchases will apply to the remaining installment balance.",
            "languageCode": "eng"
          }
        ]
      },
      {
        "planId": "9b6a2573-f532-2779-1cd2-1f054fdf9001",
        "identifier": "000000002K",
        "planName": "BilarterConsumerPlan1",
        "planType": "ISSUER_PROMOTION",
        "totalCount": "12",
        "frequency": "MONTHLY",
        "promotionId": "123",
        "fundedBy": [
          "CONSUMER"
        ],
        "amountDetails": {
          "lastInstallmentAmount": "41.63",
          "totalFeeAmount": "55.00",
          "totalUpfrontFeeAmount": "30.00",
          "totalRecurringFeeAmount": "25.00",
          "totalPlanAmount": "555.00",
          "interestRate": "0.00",
          "fees": [
            {
              "type": "CONSUMER",
              "ratePercentage": "5.00",
              "flatFeeAmount": "0.00",
              "monthlyRatePercentage": "0.42"
            },
            {
              "type": "CONSUMER_UPFRONT",
              "ratePercentage": "6.00",
              "flatFeeAmount": "0.00"
            }
          ],
          "firstInstallment": {
            "feeAmount": "2.08",
            "amount": "41.67",
            "upfrontFeeAmount": "30.00",
            "totalAmountExcludingUpfrontFee": "43.75"
          },
          "lastInstallment": {
            "feeAmount": "2.12",
            "amount": "41.63"
          },
          "currency": "USD"
        },
        "termsAndConditions": [
          {
            "version": "1",
            "text": "blah blah",
            "languageCode": "tel"
          }
        ]
      },
      {
        "planId": "23e950ef-021b-ca06-a797-11c7456c5201",
        "identifier": "00000000RN",
        "planName": "CybersourcePlanArabic",
        "planType": "ISSUER_DEFAULT",
        "totalCount": "12",
        "frequency": "MONTHLY",
        "fundedBy": [
          "MERCHANT"
        ],
        "amountDetails": {
          "lastInstallmentAmount": "41.63",
          "totalFeeAmount": "0.00",
          "totalUpfrontFeeAmount": "0.00",
          "totalRecurringFeeAmount": "0.00",
          "totalPlanAmount": "500.00",
          "interestRate": "0.00",
          "fees": [
            {
              "type": "CONSUMER_UPFRONT",
              "ratePercentage": "0.00",
              "flatFeeAmount": "0.00"
            },
            {
              "type": "CONSUMER",
              "ratePercentage": "0.00",
              "flatFeeAmount": "0.00",
              "monthlyRatePercentage": "0.00"
            }
          ],
          "firstInstallment": {
            "feeAmount": "0.00",
            "amount": "41.67",
            "upfrontFeeAmount": "0.00",
            "totalAmountExcludingUpfrontFee": "41.67"
          },
          "lastInstallment": {
            "feeAmount": "0.00",
            "amount": "41.63"
          },
          "currency": "USD"
        },
        "termsAndConditions": [
          {
            "version": "2",
            "text": "أنت تختار خطة التقسيط لمدة 12 شهرًا مع رسوم أو رسوم تمويل تبلغ 13.99% من إجمالي مبلغ الشراء - تم الكشف عنها على أنها \"رسوم\" أعلاه. دفعة خطة التقسيط الشهرية هي إجمالي مبلغ الشراء بالإضافة إلى الرسوم، وكلها مقسمة بالتساوي على عدد x من دورات الفوترة. سيتم تضمين أول دفعة شهرية لخطة التقسيط كجزء من الحد الأدنى للدفعة في كشف حسابك التالي. يرجى الرجوع إلى اتفاقية حامل البطاقة الخاصة بك لمعرفة عواقب عدم سداد دفعات خطة التقسيط. إذا تم سداد أي خطة تقسيط مبكرًا، فلن يتم تقييم جزء الرسوم المرتبط بالأشهر التالية للدفع",
            "languageCode": "ara"
          }
        ]
      }
    ]
  }
}
```

Select Installment Plan {#install-plan-select-plan}
===================================================

Send a select installment plan API request to confirm the customer's selected plan. This service requires either an authorization code or an NTID from a successful authorization. The payment method by which the customer uses also determines the required API fields.  
You can request the select an installment plan service using these payment methods:

* Authorization Code
  * [PAN and Authorization Code](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-select-plan/install-plan-select-plan-intro.md "")
  * [PAR and Authorization Code](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-select-plan/install-plan-select-par-plan-intro.md "")
  * [Token and Authorization Code](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-select-plan/install-plan-select-plan-token-intro.md "")
    {#install-plan-select-plan_ul_rwg_yvf_gyb}
* Network Transaction ID
  * [PAN and NTID](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-select-plan/install-plan-select-plan-ntid-intro.md "")
  * [PAR NTID](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-select-plan/install-plan-select-par-plan-ntid-intro.md "")
  * [Token and NTID](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-select-plan/install-plan-select-plan-token-intro.md "")
    {#install-plan-select-plan_ul_lv5_bwf_gyb}
    {#install-plan-select-plan_ul_odb_qvf_gyb}

PAN and Authorization Code {#install-plan-select-plan-intro}
============================================================

When the customer selects an installment plan from the eligible plan options and accepts the terms and conditions for that plan, you must confirm the selection by requesting the Select Installment Plan service. A successful response includes an `ACCEPTED` status.
IMPORTANT You must get the customer's consent on the terms and conditions for the installment plan that they selected.  
The Select Installment Plan service requires you to include one of the plan IDs listed in the Get Installment Plans response. The plan IDs are located in the installmentInformation.planDetails.planId fields.

PAN Information {#install-plan-select-plan-intro_section_isd_txp_cyb}
---------------------------------------------------------------------

To include the customer's PAN in the request, set the paymentInformation.card.number field to the customer's card number.

Authorization Code {#install-plan-select-plan-intro_auth-code}
--------------------------------------------------------------

To link an installment plan to an authorization, set the processingInformation.authorizationOptions.authorizationCode field in the select installment plan request to the authorization code from the authorization request. The authorization code is located in the processorInformation.approvalCode field from the authorization response.

Endpoint {#install-plan-select-plan-intro_select-endpoint-section}
------------------------------------------------------------------

**Production** : `POST ``https://api.cybersource.com``/fin/v1/plan-acceptance/`  
**Test** : `POST ``https://apitest.cybersource.com``/fin/v1/plan-acceptance/`

Required Fields for Selecting an Installment Plan with a PAN {#install-plan-select-plan-reqfields}
==================================================================================================

Include these required fields when you request the select an installment plan service with a PAN.

[installmentInformation.planId](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-plan-id.md "")
:
Set to the plan ID shown in the get installment plans response as the planDetails.planId field.

[installmentInformation.tcVersion](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-tc-vrsn.md "")
:
Set to the terms and conditions version number shown in the get installment plans response as the planDetails.termsAndConditions.version field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[processingInformation.authorizationOptions.authorizationCode](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-code.md "")
:
Set to the authorization code shown in the initial authorization response as the processorInformation.approvalCode field.

[processingInformation.authorizationOptions.authorizationDateTime](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-date-time.md "")
:

[processingInformation.installmentServiceProvider](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-instal-serv-prdr.md "")
:
Set to `Relay`.

`REST API` Example: Select an Installment Plan with a PAN {#install-plan-select-plan-ex-rest}
=============================================================================================

Request

```
{
  "processingInformation": {
    "installmentServiceProvider": "Relay",
    "authorizationOptions": {
      "authorizationCode": "888889",
      "authorizationDateTime": "2020-09-02T16:40:45.827Z"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "500",
      "currency": "USD"
    }
  },
  "installmentInformation": {
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201",
    "tcVersion": "1"
  },
  "paymentInformation": {
    "card": {
      "number": "4622943127019793"
    }
  }
}
```

Response

```
{
  "id": "6892602156176450603955",
  "submitTimeUtc": "2023-07-13T14:56:55Z",
  "status": "ACCEPTED",
  "processorInformation": {
    "responseCode": "200"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  },
  "installmentInformation": {
    "id": "e9a14fc4-bc73-e711-bbc0-112debc39d02",
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201"
  }
}
```

PAN and NTID {#install-plan-select-plan-ntid-intro}
===================================================

When the customer selects an installment plan from the eligible plan options and accepts the terms and conditions for that plan, you must confirm the selection by requesting the Select Installment Plan service.
IMPORTANT You must get the customer's consent on the terms and conditions for the installment plan that they selected.  
The Select Installment Plan request requires you to use one of the plan IDs listed in the Get Installment Plans response. The plan IDs are shown as the values of the installmentInformation.planDetails.planId fields.

PAN Information {#install-plan-select-plan-ntid-intro_section_isd_txp_cyb}
--------------------------------------------------------------------------

To include the customer's PAN in the request, set the paymentInformation.card.number field to the customer's card number.

Endpoint
--------

**Production** : `POST ``https://api.cybersource.com``/fin/v1/plan-acceptance/`  
**Test** : `POST ``https://apitest.cybersource.com``/fin/v1/plan-acceptance/`

Required Fields for Selecting an Installment Plan with a PAN {#install-plan-select-plan-ntid-reqfields}
=======================================================================================================

Include these required fields when you request the select an installment plan service with a PAN.

[installmentInformation.planId](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-plan-id.md "")
:
Set to plan ID shown in the get installment plans response as the planDetails.planId field.

[installmentInformation.tcVersion](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-tc-vrsn.md "")
:
Set to the terms and conditions version number shown in the get installment plans response as the planDetails.termsAndConditions.version field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[processingInformation.authorizationOptions.authorizationDateTime](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-date-time.md "")
:

[processingInformation.authorizationOptions.networkTransactionId](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-ntwk-trans-id.md "")
:
Set to the identifier from the processorInformation.networkTransactionId field in the authorization response.

[processingInformation.installmentServiceProvider](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-instal-serv-prdr.md "")
:
Set to `Relay`.
{#install-plan-select-plan-ntid-reqfields_dl_l5x_vr4_jyb}

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info.md "")
  {#install-plan-select-plan-ntid-reqfields_ul_qmr_hrz_sxb}

`REST API` Example: PAN and NTID {#install-plan-select-plan-ntid-ex-rest}
=========================================================================

Request

```
{
  "processingInformation": {
    "installmentServiceProvider": "Relay",
    "authorizationOptions": {
      "networkTransactionId": "178896882917673",
      "authorizationDateTime": "2020-09-02T16:40:45.827Z"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "500",
      "currency": "USD"
    }
  },
  "installmentInformation": {
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201",
    "tcVersion": "1"
  },
  "paymentInformation": {
    "card": {
      "number": "4622943127019793"
    }
  }
}
```

Response

```
{
  "id": "6914382220606141503954",
  "submitTimeUtc": "2023-08-07T19:57:02Z",
  "status": "ACCEPTED",
  "processorInformation": {
    "responseCode": "200"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  },
  "installmentInformation": {
    "id": "ed1c20e5-6967-2947-122b-198054157f02",
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201"
  }
}
```

PAR and Authorization Code {#install-plan-select-par-plan-intro}
================================================================

When the customer selects an installment plan from the eligible plan options and accepts the terms and conditions for that plan, you must confirm the selection by requesting the Select Installment Plan service.
IMPORTANT You must get the customer's consent on the terms and conditions for the installment plan that they selected.  
The Select Installment Plan request requires you to use one of the plan IDs listed in the Get Installment Plans response. The plan IDs are shown as the values of the installmentInformation.planDetails.planId fields.

PAR Information {#install-plan-select-par-plan-intro_section_ktk_4hq_fyb}
-------------------------------------------------------------------------

Include the customer's PAR in the service request with the paymentInformation.paymentAccountReference.id field.

Endpoint
--------

**Production** : `POST ``https://api.cybersource.com``/fin/v1/plan-acceptance/`  
**Test** : `POST ``https://apitest.cybersource.com``/fin/v1/plan-acceptance/`

Required Fields for Selecting an Installment Plan with a PAR {#install-plan-select-par-plan-reqfields}
======================================================================================================

Include these required fields when you request the select an installment plan service with a PAR.

[installmentInformation.planId](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-plan-id.md "")
:
Set to plan ID shown in the get installment plans response as the planDetails.planId field.

[installmentInformation.tcVersion](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-tc-vrsn.md "")
:
Set to the terms and conditions version number shown in the get installment plans response as the planDetails.termsAndConditions.version field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.paymentAccountReference.id](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/payment-info-pay-acct-ref-id.md "")
:

[processingInformation.authorizationOptions.authorizationCode](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-code.md "")
:
Set to the authorization code shown in the initial authorization response as the processorInformation.approvalCode field.

[processingInformation.authorizationOptions.authorizationDateTime](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-date-time.md "")
:

[processingInformation.installmentServiceProvider](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-instal-serv-prdr.md "")
:
Set to `Relay`.

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info.md "")
  {#install-plan-select-par-plan-reqfields_ul_qmr_hrz_sxb}

`REST API` Example: Select an Installment Plan with a PAR {#install-plan-par-select-plan-ex-rest}
=================================================================================================

Request

```
{
  "processingInformation": {
    "installmentServiceProvider": "Relay",
    "authorizationOptions": {
      "authorizationCode": "888887",
      "authorizationDateTime": "2020-09-02T16:40:45.827Z"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "500",
      "currency": "USD"
    }
  },
  "installmentInformation": {
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201",
    "tcVersion": "1"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  }
}
```

Response

```
{
  "id": "6902128410766769403954",
  "submitTimeUtc": "2023-07-24T15:34:01Z",
  "status": "ACCEPTED",
  "processorInformation": {
    "responseCode": "200"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  },
  "installmentInformation": {
    "id": "4d3e3e73-034d-e37e-aa4b-1f55e173e302",
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201"
  }
}
```

PAR and NTID {#install-plan-select-par-plan-ntid-intro}
=======================================================

When the customer selects an installment plan from the eligible plan options and accepts the terms and conditions for that plan, you must confirm the selection by requesting the Select Installment Plan service.
IMPORTANT You must get the customer's consent on the terms and conditions for the installment plan that they selected.  
The Select Installment Plan request requires you to use one of the plan IDs listed in the Get Installment Plans response. The plan IDs are shown as the values of the installmentInformation.planDetails.planId fields.

PAR Information {#install-plan-select-par-plan-ntid-intro_section_ktk_4hq_fyb}
------------------------------------------------------------------------------

Include the customer's PAR in the service request with the paymentInformation.paymentAccountReference.id field.

Endpoint
--------

**Production** : `POST ``https://api.cybersource.com``/fin/v1/plan-acceptance/`  
**Test** : `POST ``https://apitest.cybersource.com``/fin/v1/plan-acceptance/`

Required Fields for Selecting an Installment Plan with a PAR {#install-plan-select-par-plan-ntid-reqfields}
===========================================================================================================

Include these required fields when you request the select an installment plan service with a PAR.

[installmentInformation.planId](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-plan-id.md "")
:
Set to plan ID shown in the get installment plans response as the planDetails.planId field.

[installmentInformation.tcVersion](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-tc-vrsn.md "")
:
Set to the terms and conditions version number shown in the get installment plans response as the planDetails.termsAndConditions.version field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.paymentAccountReference.id](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/payment-info-pay-acct-ref-id.md "")
:

[processingInformation.authorizationOptions.authorizationDateTime](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-date-time.md "")
:

[processingInformation.authorizationOptions.networkTransactionId](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-ntwk-trans-id.md "")
:
Set to the identifier from the processorInformation.networkTransactionId field in the authorization response.

[processingInformation.installmentServiceProvider](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-instal-serv-prdr.md "")
:
Set to `Relay`.
{#install-plan-select-par-plan-ntid-reqfields_dl_skg_vr4_jyb}

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info.md "")
  {#install-plan-select-par-plan-ntid-reqfields_ul_qmr_hrz_sxb}

`REST API` Example: Select an Installment Plan with a PAR {#install-plan-par-select-plan-ntid-ex-rest}
======================================================================================================

Request

```
{
  "processingInformation": {
    "installmentServiceProvider": "Relay",
    "authorizationOptions": {
      "networkTransactionId": "178896882917659",
      "authorizationDateTime": "2020-09-02T16:40:45.827Z"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "500",
      "currency": "USD"
    }
  },
  "installmentInformation": {
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201",
    "tcVersion": "1"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  }
}
```

Response

```
{
  "id": "6914402619366789403955",
  "submitTimeUtc": "2023-08-07T20:31:02Z",
  "status": "ACCEPTED",
  "processorInformation": {
    "responseCode": "200"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  },
  "installmentInformation": {
    "id": "adf6c81e-d6e1-dd36-7ba5-10d0f39ee102",
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201"
  }
}
```

Token and Authorization Code {#install-plan-select-plan-token-intro}
====================================================================

When the customer selects an installment plan from the eligible plan options and accepts the terms and conditions for that plan, you must confirm the selection by requesting the Select Installment Plan service.
IMPORTANT You must get the customer's consent on the terms and conditions for the installment plan that they selected.  
The Select Installment Plan request requires you to use one of the plan IDs listed in the Get Installment Plans response. The plan IDs are shown as the values of the installmentInformation.planDetails.planId fields.

Token Information {#install-plan-select-plan-token-intro_section_hwm_pjx_fyb}
-----------------------------------------------------------------------------

Include the token information in the service request with one of these token identifier fields:

* Flex API transient token: tokenInformation.transientTokenJwt
* `TMS` customer token: paymentInformation.customer.id
* `TMS` instrument identifier token: paymentInformation.instrumentIdentifier.id
* `TMS` payment instrument token: paymentInformation.paymentInstrument.id
* `TMS` transient token: tokenInformation.jti

{#install-plan-select-plan-token-intro_d14e35}  
For more information about token types, see the [Token Types](https://developer.cybersource.com/docs/cybs/en-us/tms/developer/ctv/rest/tms/tms-overview/tms-token-types.md "") section in the *`Token Management Service` Developer Guide*.

Endpoint
--------

**Production** : `POST ``https://api.cybersource.com``/fin/v1/plan-acceptance/`  
**Test** : `POST ``https://apitest.cybersource.com``/fin/v1/plan-acceptance/`

Required Fields for Selecting an Installment Plan with a Token {#install-plan-select-plan-token-reqfields}
==========================================================================================================

Include these required fields when you request the select an installment plan service with a token.

[installmentInformation.planId](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-plan-id.md "")
:
Set to plan ID shown in the get installment plans response as the planDetails.planId field.

[installmentInformation.tcVersion](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-tc-vrsn.md "")
:
Set to the terms and conditions version number shown in the get installment plans response as the planDetails.termsAndConditions.version field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[processingInformation.authorizationOptions.authorizationCode](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-code.md "")
:
Set to the authorization code shown in the initial authorization response as the processorInformation.approvalCode field.

[processingInformation.authorizationOptions.authorizationDateTime](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-date-time.md "")
:

[processingInformation.installmentServiceProvider](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-instal-serv-prdr.md "")
:
Set to `Relay`.

Required Token Fields {#install-plan-select-plan-token-reqfields_section_ug4_qhx_fyb}
-------------------------------------------------------------------------------------

Include only one of these token identifier fields:

[paymentInformation.customer.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-customer-id.md "")
:

[paymentInformation.instrumentIdentifier.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-instrument-identifier-id.md "")
:

[paymentInformation.paymentInstrument.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-instrument-id.md "")
:

[tokenInformation.jti](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-jti.md "")
:

[tokenInformation.transientTokenJwt](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-transient-token-jwt.md "")
:

`REST API` Example: Select an Installment Plan with a Token {#install-plan-select-plan-token-ex-rest}
=====================================================================================================

Request with Authorization Code

```
{
  "processingInformation": {
    "installmentServiceProvider": "Relay",
    "authorizationOptions": {
      "authorizationCode": "888884",
      "authorizationDateTime": "2020-09-02T16:40:45.827Z"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "500",
      "currency": "USD"
    }
  },
  "installmentInformation": {
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201",
    "tcVersion": "1"
  },
  "paymentInformation": {
    "instrumentIdentifier": {
      "id": "7030000000012249793"
    }
  }
}
```

Response with Authorization Code

```
{
  "id": "6903067597896924403955",
  "submitTimeUtc": "2023-07-25T17:39:19Z",
  "status": "ACCEPTED",
  "processorInformation": {
    "responseCode": "200"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  },
  "installmentInformation": {
    "id": "2af69dac-670d-b035-44d6-162559d0a302",
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201"
  }
}
```

Token and NTID {#install-plan-select-plan-token-ntid-intro}
===========================================================

When the customer selects an installment plan from the eligible plan options and accepts the terms and conditions for that plan, you must confirm the selection by requesting the Select Installment Plan service.
IMPORTANT You must get the customer's consent on the terms and conditions for the installment plan that they selected.  
The Select Installment Plan request requires you to use one of the plan IDs listed in the Get Installment Plans response. The plan IDs are shown as the values of the installmentInformation.planDetails.planId fields.

Token Information {#install-plan-select-plan-token-ntid-intro_section_hwm_pjx_fyb}
----------------------------------------------------------------------------------

Include the token information in the service request with one of these token identifier fields:

* Flex API transient token: tokenInformation.transientTokenJwt
* `TMS` customer token: paymentInformation.customer.id
* `TMS` instrument identifier token: paymentInformation.instrumentIdentifier.id
* `TMS` payment instrument token: paymentInformation.paymentInstrument.id
* `TMS` transient token: tokenInformation.jti

{#install-plan-select-plan-token-ntid-intro_d19e35}  
For more information about token types, see the [Token Types](https://developer.cybersource.com/docs/cybs/en-us/tms/developer/ctv/rest/tms/tms-overview/tms-token-types.md "") section in the *`Token Management Service` Developer Guide*.

Endpoint
--------

**Production** : `POST ``https://api.cybersource.com``/fin/v1/plan-acceptance/`  
**Test** : `POST ``https://apitest.cybersource.com``/fin/v1/plan-acceptance/`

Required Fields for Selecting an Installment Plan with a Token {#install-plan-select-plan-token-ntid-reqfields}
===============================================================================================================

Include these required fields when you request the select an installment plan service with a token.

[installmentInformation.planId](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-plan-id.md "")
:
Set to plan ID shown in the get installment plans response as the planDetails.planId field.

[installmentInformation.tcVersion](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-tc-vrsn.md "")
:
Set to the terms and conditions version number shown in the get installment plans response as the planDetails.termsAndConditions.version field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[processingInformation.authorizationOptions.authorizationDateTime](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-date-time.md "")
:

[processingInformation.authorizationOptions.networkTransactionId](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-ntwk-trans-id.md "")
:
Set to the identifier from the processorInformation.networkTransactionId field in the authorization response.

[processingInformation.installmentServiceProvider](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-instal-serv-prdr.md "")
:
Set to `Relay`.
{#install-plan-select-plan-token-ntid-reqfields_dl_ujb_5r4_jyb}

Required Token Fields {#install-plan-select-plan-token-ntid-reqfields_section_ug4_qhx_fyb}
------------------------------------------------------------------------------------------

Include only one of these token identifier fields:

[paymentInformation.customer.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-customer-id.md "")
:

[paymentInformation.instrumentIdentifier.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-instrument-identifier-id.md "")
:

[paymentInformation.paymentInstrument.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-instrument-id.md "")
:

[tokenInformation.jti](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-jti.md "")
:

[tokenInformation.transientTokenJwt](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-transient-token-jwt.md "")
:

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info.md "")
  {#install-plan-select-plan-token-ntid-reqfields_ul_qmr_hrz_sxb}

`REST API` Example: Select an Installment Plan with a Token {#install-plan-select-plan-token-ntid-ex-rest}
==========================================================================================================

Request

```
{
  "processingInformation": {
    "installmentServiceProvider": "Relay",
    "authorizationOptions": {
      "networkTransactionId": "178896882917745",
      "authorizationDateTime": "2020-09-02T16:40:45.827Z"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "500",
      "currency": "USD"
    }
  },
  "installmentInformation": {
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201",
    "tcVersion": "1"
  },
  "paymentInformation": {
    "instrumentIdentifier": {
      "id": "7030000000012249793"
    }
  }
}
```

Response

```
{
  "id": "6903019542136782103955",
  "submitTimeUtc": "2023-07-25T16:19:14Z",
  "status": "ACCEPTED",
  "processorInformation": {
    "responseCode": "200"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  },
  "installmentInformation": {
    "id": "4be11ad6-d0a8-c59a-1a57-1235d7f79302",
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201"
  }
}
```

Cancel Installment Plan {#install-plan-cancel-plan-intro}
=========================================================

Request the cancellation of an installment plan if:

* The initial authorization that utilized the installment plan is refunded.
* The initial authorization that utilized the installment plan is reversed after a select installment plan request has been sent.

Both full and partial refunds are supported. Refunds cannot exceed the total captured amount.
IMPORTANT It is required to cancel an installment plan after the initial authorization is either refunded or reversed after a select installment plan request has been sent. This ensures the customer does not receive any future installment plan charges.  
You can cancel an installment plan using one of these identifiers:

* Authorization Code
  * [Authorization Code with a PAN](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-cancel-plan-intro/install-plan-cancel-auth-code-intro.md "")
  * [Authorization Code with a PAR](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-cancel-plan-intro/install-plan-cancel-auth-code-token-intro.md "")
  * [Authorization Code with a Token](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-cancel-plan-intro/install-plan-cancel-auth-code-token-intro.md "")
    {#install-plan-cancel-plan-intro_ul_k4p_gy3_twb}
* Network Transaction ID
  * [Network Transaction ID with a PAN](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-cancel-plan-intro/install-plan-cancel-network-id-intro.md "")
  * [Network Transaction ID with a PAR](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-cancel-plan-intro/install-plan-cancel-network-id-token-intro.md "")
  * [Network Transaction ID with a Token](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-cancel-plan-intro/install-plan-cancel-network-id-token-intro.md "")
    {#install-plan-cancel-plan-intro_ul_otp_gy3_twb}
    {#install-plan-cancel-plan-intro_ol_m1d_3l3_twb}

PAN and Authorization Code {#install-plan-cancel-auth-code-intro}
=================================================================

You can cancel an installment plan with the authorization code from the initial authorization. The authorization code is included in the cancellation request with the processorInformation.approvalCode field value. Cancelling an installment plan with an authorization code also requires you to have already included the authorization code in the select an installment plan request.

> IMPORTANT It is required to cancel an installment plan after the initial authorization is either refunded or reversed after a select installment plan request has been sent. This ensures the customer does not receive any future installment plan charges.

PAN Information {#install-plan-cancel-auth-code-intro_section_w41_jyp_cyb}
--------------------------------------------------------------------------

To include the customer's PAN in the request, set the paymentInformation.card.number field to the customer's card number.

Endpoint {#install-plan-cancel-auth-code-intro_section_k5r_qzp_cyb}
-------------------------------------------------------------------

**Production** : `POST ``https://api.cybersource.com``/fin/v1/plan-acceptance/cancel/`  
**Test** : `POST ``https://apitest.cybersource.com``/fin/v1/plan-acceptance/cancel/`

Required Fields for Cancelling with an Authorization Code and a PAN {#install-plan-cancel-plan-auth-code-reqfields}
===================================================================================================================

Include these fields when you are using an authorization code to cancel the installment plan.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[processingInformation.authorizationOptions.authorizationCode](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-code.md "")
:
Set to the authorization code shown in the initial authorization response as the processorInformation.approvalCode field.

[processingInformation.authorizationOptions.authorizationDateTime](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-date-time.md "")
:

[processingInformation.installmentServiceProvider](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-instal-serv-prdr.md "")
:
Set to `Relay`.
{#install-plan-cancel-plan-auth-code-reqfields_dl_t5r_lkv_cyb}

Required Field for a Partial Refund {#install-plan-cancel-plan-auth-code-reqfields_section_m1b_fyq_fyb}
-------------------------------------------------------------------------------------------------------

For a partial refund, include this required field in addition to the other required fields.

[processingInformation.refundOptions.refundAmount](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/refund-ops-refund-amnt.md "")
:
Include this field for a partial refund. The amount of the refund must be less than the total order amount. The value should include a decimal with two places, for example, `60.01`.

Optional Fields for Cancel Installment Plan {#install-plan-cancel-opt-fields}
=============================================================================

These fields are optional when cancelling an installment plan.

[installmentInformation.id](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/install-info-id.md "")
:

[merchantInformation.categoryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-category-code-a.md "")
:

`REST API` Example: Cancel an Installment Plan using an Authorization Code {#install-plan-cancel-plan-ex-rest}
==============================================================================================================

Request

```
{
  "processingInformation": {
    "installmentServiceProvider": "Relay",
    "authorizationOptions": {
      "authorizationCode": "888888",
      "authorizationDateTime": "2020-09-02T16:40:45.827Z"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "500",
      "currency": "USD"
    }
  },
  "paymentInformation": {
    "card": {
      "number": "4622943127019793"
    }
  }
}
```

Response

```
{
  "id": "6892602156176450603955",
  "submitTimeUtc": "2023-07-13T14:56:55Z",
  "status": "ACCEPTED",
  "processorInformation": {
    "responseCode": "200"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  },
  "installmentInformation": {
    "id": "e9a14fc4-bc73-e711-bbc0-112debc39d02",
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201"
  }
}      
```

PAN and NTID {#install-plan-cancel-network-id-intro}
====================================================

You can cancel an installment plan with the network transaction ID from the initial authorization. Include the network transaction ID in the cancellation request with the processingInformation.authorizationOptions.networkTransactionId field value.  
Cancelling an installment plan with a network transaction ID also requires you to have included the network transaction ID in the select an installment plan request.

> IMPORTANT It is required to cancel an installment plan after the initial authorization is either refunded or reversed after a select installment plan request has been sent. This ensures the customer does not receive any future installment plan charges.

PAN Information {#install-plan-cancel-network-id-intro_section_lhj_3yp_cyb}
---------------------------------------------------------------------------

To include the customer's PAN in the request, set the paymentInformation.card.number field to the customer's card number.

Endpoint {#install-plan-cancel-network-id-intro_section_sck_pzp_cyb}
--------------------------------------------------------------------

**Production** : `POST ``https://api.cybersource.com``/fin/v1/plan-acceptance/cancel/`  
**Test** : `POST ``https://apitest.cybersource.com``/fin/v1/plan-acceptance/cancel/`

Required Fields for Cancelling with a Network Transaction ID {#install-plan-cancel-net-txn-id-reqfields}
========================================================================================================

Include these fields when you are using a network transaction ID to cancel the installment plan.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[processingInformation.authorizationOptions.authorizationDateTime](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-date-time.md "")
:

[processingInformation.authorizationOptions.networkTransactionId](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-ntwk-trans-id.md "")
:
Set to the identifier from the processorInformation.networkTransactionId field in the authorization response.

[processingInformation.installmentServiceProvider](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-instal-serv-prdr.md "")
:
Set to `Relay`.
{#install-plan-cancel-net-txn-id-reqfields_dl_bwd_kkv_cyb}

Required Field for a Partial Refund {#install-plan-cancel-net-txn-id-reqfields_partial-refund}
----------------------------------------------------------------------------------------------

For a partial refund, include this required field in addition to the other required fields.

[processingInformation.refundOptions.refundAmount](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/refund-ops-refund-amnt.md "")
:
Include this field for a partial refund. The amount of the refund must be less than the total order amount. The value should include a decimal with two places, for example, `60.01`.

`REST API` Example: Cancel an Installment Plan using a Network Transaction ID {#install-plan-cancel-network-id-ex-rest}
=======================================================================================================================

Request

```
{
  "processingInformation": {
    "installmentServiceProvider": "Relay",
    "authorizationOptions": {
      "networkTransactionId": "178896882917784",
      "authorizationDateTime": "2020-09-02T16:40:45.827Z"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "500",
      "currency": "USD"
    }
  },
  "paymentInformation": {
    "card": {
      "number": "4622943127019793"
    }
  }
}
```

Response

```
{
  "id": "6892596521746405203955",
  "submitTimeUtc": "2023-07-13T14:47:32Z",
  "status": "ACCEPTED",
  "processorInformation": {
    "responseCode": "200"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  },
  "installmentInformation": {
    "id": "00d531c8-ad93-71a5-f53a-1737c58cd202",
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201"
  }
}       
```

PAR and Authorization Code {#install-plan-cancel-auth-code-par-intro}
=====================================================================

You can cancel an installment plan with the authorization code from the initial authorization. The authorization code is included in the cancellation request with the processorInformation.approvalCode field value. Cancelling an installment plan with an authorization code also requires you to have already included the authorization code in the select an installment plan request.

> IMPORTANT It is required to cancel an installment plan after the initial authorization is either refunded or reversed after a select installment plan request has been sent. This ensures the customer does not receive any future installment plan charges.

PAR Information
---------------

Include the customer's PAR in the service request with the paymentInformation.paymentAccountReference.id field.

Endpoint {#install-plan-cancel-auth-code-par-intro_section_k5r_qzp_cyb}
-----------------------------------------------------------------------

**Production** : `POST ``https://api.cybersource.com``/fin/v1/plan-acceptance/cancel/`  
**Test** : `POST ``https://apitest.cybersource.com``/fin/v1/plan-acceptance/cancel/`

Required Fields for Cancelling with an Authorization Code and a PAR {#install-plan-cancel-plan-auth-code-par-reqfields}
=======================================================================================================================

Include these required fields to cancel a plan with an authorization code and a PAR.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.paymentAccountReference.id](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/payment-info-pay-acct-ref-id.md "")
:

[processingInformation.authorizationOptions.authorizationDateTime](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-date-time.md "")
:

[processingInformation.authorizationOptions.authorizationCode](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-code.md "")
:
Set to the authorization code shown in the initial authorization response as the processorInformation.approvalCode field.

[processingInformation.installmentServiceProvider](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-instal-serv-prdr.md "")
:
Set to `Relay`.

Required Field for a Partial Refund {#install-plan-cancel-plan-auth-code-par-reqfields_section_m1b_fyq_fyb}
-----------------------------------------------------------------------------------------------------------

For a partial refund, include this required field in addition to the other required fields.

[processingInformation.refundOptions.refundAmount](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/refund-ops-refund-amnt.md "")
:
Include this field for a partial refund. The amount of the refund must be less than the total order amount. The value should include a decimal with two places, for example, `60.01`.

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info.md "")
  {#install-plan-cancel-plan-auth-code-par-reqfields_ul_qmr_hrz_sxb}

`REST API` Example: Cancelling with an Authorization Code and a PAR {#install-plan-cancel-plan-par-ex-rest}
===========================================================================================================

Request

```
{
  "processingInformation": {
    "installmentServiceProvider": "Relay",
    "authorizationOptions": {
      "authorizationCode": "888881",
      "authorizationDateTime": "2023-07-24T16:42:52Z"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "500",
      "currency": "USD"
    }
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  }
}
```

Response

```
{
  "id": "6902173767896334503954",
  "submitTimeUtc": "2023-07-24T16:49:36Z",
  "status": "ACCEPTED",
  "processorInformation": {
    "responseCode": "200"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  },
  "installmentInformation": {
    "id": "6b6f6ddf-4619-b9ca-2469-16a49db52e02",
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201"
  }
}
```

PAR and NTID {#install-plan-cancel-network-id-par-intro}
========================================================

You can cancel an installment plan with the network transaction ID from the initial authorization. Include the network transaction ID in the cancellation request with the processingInformation.authorizationOptions.networkTransactionId field value.  
Cancelling an installment plan with a network transaction ID also requires you to have included the network transaction ID in the select an installment plan request.  
Cancelling an installment plan with a network transaction ID also requires you to have included the network transaction ID in the select an installment plan request.

> IMPORTANT It is required to cancel an installment plan after the initial authorization is either refunded or reversed after a select installment plan request has been sent. This ensures the customer does not receive any future installment plan charges.

PAR Information
---------------

Include the customer's PAR in the service request with the paymentInformation.paymentAccountReference.id field.

Endpoint {#install-plan-cancel-network-id-par-intro_section_sck_pzp_cyb}
------------------------------------------------------------------------

**Production** : `POST ``https://api.cybersource.com``/fin/v1/plan-acceptance/cancel/`  
**Test** : `POST ``https://apitest.cybersource.com``/fin/v1/plan-acceptance/cancel/`

Required Fields for Cancelling with a Network Transaction ID and a PAR {#install-plan-cancel-net-txn-id-par-reqfields}
======================================================================================================================

Include these required fields to cancel a plan with a network transaction ID and a PAR.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.paymentAccountReference.id](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/payment-info-pay-acct-ref-id.md "")
:

[processingInformation.authorizationOptions.authorizationDateTime](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-date-time.md "")
:

[processingInformation.authorizationOptions.networkTransactionId](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-ntwk-trans-id.md "")
:
Set to the identifier from the processorInformation.networkTransactionId field in the authorization response.

[processingInformation.installmentServiceProvider](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-instal-serv-prdr.md "")
:
Set to `Relay`.
{#install-plan-cancel-net-txn-id-par-reqfields_dl_btt_lyp_fyb}

Required Field for a Partial Refund {#install-plan-cancel-net-txn-id-par-reqfields_section_m1b_fyq_fyb}
-------------------------------------------------------------------------------------------------------

For a partial refund, include this required field in addition to the other required fields.

[processingInformation.refundOptions.refundAmount](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/refund-ops-refund-amnt.md "")
:
Include this field for a partial refund. The amount of the refund must be less than the total order amount. The value should include a decimal with two places, for example, `60.01`.

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info.md "")
  {#install-plan-cancel-net-txn-id-par-reqfields_ul_qmr_hrz_sxb}

`REST API` Example: Cancelling with a Network Transaction ID and a PAR {#install-plan-cancel-network-id-par-ex-rest}
====================================================================================================================

Request

```
{
  "processingInformation": {
    "installmentServiceProvider": "Relay",
    "authorizationOptions": {
      "networkTransactionId": "178896882917423",
      "authorizationDateTime": "2023-07-24T16:56:12Z"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "500",
      "currency": "USD"
    }
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  }
}
```

Response

```
{
  "id": "6902178969776507703954",
  "submitTimeUtc": "2023-07-24T16:58:17Z",
  "status": "ACCEPTED",
  "processorInformation": {
    "responseCode": "200"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  },
  "installmentInformation": {
    "id": "6f4d375c-885d-625e-f30f-1aad7bbc9e02",
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201"
  }
}
```

Token and Authorization Code {#install-plan-cancel-auth-code-token-intro}
=========================================================================

You can cancel an installment plan with the authorization code from the initial authorization. The authorization code is included in the cancellation request with the processorInformation.approvalCode field value. Cancelling an installment plan with an authorization code also requires you to have already included the authorization code in the select an installment plan request.

> IMPORTANT It is required to cancel an installment plan after the initial authorization is either refunded or reversed after a select installment plan request has been sent. This ensures the customer does not receive any future installment plan charges.

PAR Information
---------------

Include the customer's PAR in the service request with the paymentInformation.paymentAccountReference.id field.

Token Information {#install-plan-cancel-auth-code-token-intro_section_hwm_pjx_fyb}
----------------------------------------------------------------------------------

Include the token information in the service request with one of these token identifier fields:

* Flex API transient token: tokenInformation.transientTokenJwt
* `TMS` customer token: paymentInformation.customer.id
* `TMS` instrument identifier token: paymentInformation.instrumentIdentifier.id
* `TMS` payment instrument token: paymentInformation.paymentInstrument.id
* `TMS` transient token: tokenInformation.jti

{#install-plan-cancel-auth-code-token-intro_d19e35}  
For more information about token types, see the [Token Types](https://developer.cybersource.com/docs/cybs/en-us/tms/developer/ctv/rest/tms/tms-overview/tms-token-types.md "") section in the *`Token Management Service` Developer Guide*.

Endpoint
--------

`https://api.cybersource.com``/fin/v1/plan-acceptance/cancel/`

Required Fields for Cancelling with an Authorization Code and a Token {#install-plan-cancel-plan-auth-code-token-reqfields}
===========================================================================================================================

Include these fields if you are using an authorization code to cancel the installment plan.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[processingInformation.authorizationOptions.authorizationCode](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-code.md "")
:
Only include this field if the processorInformation.approvalCode response field is present in the authorization response.

[processingInformation.authorizationOptions.authorizationDateTime](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-date-time.md "")
:

[processingInformation.installmentServiceProvider](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-instal-serv-prdr.md "")
:
Set to `Relay`.

Required Token Fields {#install-plan-cancel-plan-auth-code-token-reqfields_section_ug4_qhx_fyb}
-----------------------------------------------------------------------------------------------

Include only one of these token identifier fields:

[paymentInformation.customer.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-customer-id.md "")
:

[paymentInformation.instrumentIdentifier.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-instrument-identifier-id.md "")
:

[paymentInformation.paymentInstrument.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-instrument-id.md "")
:

[tokenInformation.jti](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-jti.md "")
:

[tokenInformation.transientTokenJwt](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-transient-token-jwt.md "")
:

Required Field for a Partial Refund {#install-plan-cancel-plan-auth-code-token-reqfields_section_m1b_fyq_fyb}
-------------------------------------------------------------------------------------------------------------

For a partial refund, include this required field in addition to the other required fields.

[processingInformation.refundOptions.refundAmount](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/refund-ops-refund-amnt.md "")
:
Include this field for a partial refund. The amount of the refund must be less than the total order amount. The value should include a decimal with two places, for example, `60.01`.

`REST API` Example: Cancel an Installment Plan using an Authorization Code and a Token {#install-plan-cancel-plan-token-ex-rest}
================================================================================================================================

Request

```
{
  "processingInformation": {
    "installmentServiceProvider": "Relay",
    "authorizationOptions": {
      "authorizationCode": "888884",
      "authorizationDateTime": "2020-09-02T16:40:45.827Z"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "500",
      "currency": "USD"
    }
  },
  "paymentInformation": {
    "instrumentIdentifier": {
      "id": "7030000000012249793"
    }
  }
}
```

Response

```
{
  "id": "6903070348706958703955",
  "submitTimeUtc": "2023-07-25T17:43:54Z",
  "status": "ACCEPTED",
  "processorInformation": {
    "responseCode": "200"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  },
  "installmentInformation": {
    "id": "2af69dac-670d-b035-44d6-162559d0a302",
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201"
  }
}
```

Token and NTID {#install-plan-cancel-network-id-token-intro}
============================================================

You can cancel an installment plan with the network transaction ID from the initial authorization. Include the network transaction ID in the cancellation request with the processingInformation.authorizationOptions.networkTransactionId field value.  
Cancelling an installment plan with a network transaction ID also requires you to have included the network transaction ID in the select an installment plan request.  
Cancelling an installment plan with a network transaction ID also requires you to have included the network transaction ID in the select an installment plan request.

> IMPORTANT It is required to cancel an installment plan after the initial authorization is either refunded or reversed after a select installment plan request has been sent. This ensures the customer does not receive any future installment plan charges.

Token Information {#install-plan-cancel-network-id-token-intro_section_hwm_pjx_fyb}
-----------------------------------------------------------------------------------

Include the token information in the service request with one of these token identifier fields:

* Flex API transient token: tokenInformation.transientTokenJwt
* `TMS` customer token: paymentInformation.customer.id
* `TMS` instrument identifier token: paymentInformation.instrumentIdentifier.id
* `TMS` payment instrument token: paymentInformation.paymentInstrument.id
* `TMS` transient token: tokenInformation.jti

{#install-plan-cancel-network-id-token-intro_d14e35}  
For more information about token types, see the [Token Types](https://developer.cybersource.com/docs/cybs/en-us/tms/developer/ctv/rest/tms/tms-overview/tms-token-types.md "") section in the *`Token Management Service` Developer Guide*.

Endpoint
--------

`https://api.cybersource.com``/fin/v1/plan-acceptance/cancel/`

Required Fields for Cancelling with a Network Transaction ID and a Token {#install-plan-cancel-net-txn-id-token-reqfields}
==========================================================================================================================

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[processingInformation.authorizationOptions.authorizationDateTime](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-auth-date-time.md "")
:

[processingInformation.authorizationOptions.networkTransactionId](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-auth-ops-ntwk-trans-id.md "")
:
Set to the identifier from the processorInformation.networkTransactionId field in the authorization response.

[processingInformation.installmentServiceProvider](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/processing-info-instal-serv-prdr.md "")
:
Set to `Relay`.

Required Token Fields {#install-plan-cancel-net-txn-id-token-reqfields_section_ug4_qhx_fyb}
-------------------------------------------------------------------------------------------

Include only one of these token identifier fields:

[paymentInformation.customer.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-customer-id.md "")
:

[paymentInformation.instrumentIdentifier.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-instrument-identifier-id.md "")
:

[paymentInformation.paymentInstrument.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-instrument-id.md "")
:

[tokenInformation.jti](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-jti.md "")
:

[tokenInformation.transientTokenJwt](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-transient-token-jwt.md "")
:

Required Field for a Partial Refund {#install-plan-cancel-net-txn-id-token-reqfields_section_m1b_fyq_fyb}
---------------------------------------------------------------------------------------------------------

For a partial refund, include this required field in addition to the other required fields.

[processingInformation.refundOptions.refundAmount](/docs/cybs/en-us/installment-plans/developer/all/rest/installment-plans/install-plan-reference-intro/refund-ops-refund-amnt.md "")
:
Include this field for a partial refund. The amount of the refund must be less than the total order amount. The value should include a decimal with two places, for example, `60.01`.

`REST API` Example: Cancel an Installment Plan using a Network Transaction ID and a Token {#install-plan-cancel-network-id-token-ex-rest}
=========================================================================================================================================

Request

```
{
  "processingInformation": {
    "installmentServiceProvider": "Relay",
    "authorizationOptions": {
      "networkTransactionId": "178896882917745",
      "authorizationDateTime": "2023-07-25T16:19:14Z"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "500",
      "currency": "USD"
    }
  },
  "paymentInformation": {
    "instrumentIdentifier": {
      "id": "7030000000012249793"
    }
  }
}
```

Response

```
{
  "id": "6903020670086847503954",
  "submitTimeUtc": "2023-07-25T16:21:07Z",
  "status": "ACCEPTED",
  "processorInformation": {
    "responseCode": "200"
  },
  "paymentInformation": {
    "paymentAccountReference": {
      "id": "V0010013020261601352183794986"
    }
  },
  "installmentInformation": {
    "id": "4be11ad6-d0a8-c59a-1a57-1235d7f79302",
    "planId": "1cc80cb6-866d-0a3e-7c52-18f6aced3201"
  }
}
```

Installment Plan Response Codes {#install-plan-resp-codes}
==========================================================

The installment plan service returns these response codes:

| Code | Description                                |
|:-----|:-------------------------------------------|
| 201  | Successful response.                       |
| 400  | Invalid request.                           |
| 502  | Unexpected system error or system timeout. |
[Response Codes]

Installments `REST API` Fields {#install-plan-reference-intro}
==============================================================

This section contains field descriptions for the fields used in the Installments API.

installmentInformation. planDetails.amountDetails. currency {#install-info-plan-details-amount-details-crncy}
=============================================================================================================

The currency code for the installment plan payments.  
For all possible values, use the ISO 4217 standard.

Specifications {#install-info-plan-details-amount-details-crncy_Specifications}
-------------------------------------------------------------------------------

* **Data Type:** Integer
* **Data Length:** 3---4

Mapping {#install-info-plan-details-amount-details-crncy_Mapping}
-----------------------------------------------------------------

* **REST Field Name:** installmentInformation.planDetails.amountDetails.currency
* **Simple Order Field Name:** No corresponding field.

installmentInformation. planDetails. amountDetails. fees. monthlyRatePercentage {#install-info-plan-details-amount-details-fees-monthly-rate-percent}
=====================================================================================================================================================

The monthly percentage interest fee applied to an installment payment.  
The fee rate cannot be set to a negative value. Fees are only present when the installmentInformation.planDetails.fundedBy field is set to `CONSUMER`.  
To calculate the percentage value, use this formula:  
`actualPercentageValue = ratePercentage / 100.00`

Specifications {#install-info-plan-details-amount-details-fees-monthly-rate-percent_Specifications}
---------------------------------------------------------------------------------------------------

* **Data Type:** Integer
* **Data Length:** 0---10000

Mapping {#install-info-plan-details-amount-details-fees-monthly-rate-percent_Mapping}
-------------------------------------------------------------------------------------

* **REST Field Name:** installmentInformation.planDetails.amountDetails.fees.monthlyRatePercentage
* **Simple Order Field Name:** No corresponding field.

installmentInformation. planDetails. amountDetails. totalAmountExcluding UpfrontFee {#install-info-plan-details-amount-details-total-amount-exclude-upfront-fee}
================================================================================================================================================================

The total payable amount for the installment period.  
The payable amount includes the installment payment and the customer interest fee. No other fee amounts are included, such as an upfront fee.  
Format: `XXXX.XX`

Specifications {#install-info-plan-details-amount-details-total-amount-exclude-upfront-fee_Specifications}
----------------------------------------------------------------------------------------------------------

* **Data Type:** Integer
* **Data Length:** 1---999999999999999

Mapping {#install-info-plan-details-amount-details-total-amount-exclude-upfront-fee_Mapping}
--------------------------------------------------------------------------------------------

* **REST Field Name:** installmentInformation.planDetails. amountDetails. totalAmountExcludingUpfrontFee
* **Simple Order Field Name:** No corresponding field.

installmentInformation. planDetails. fundedBy {#install-info-plan-details-fund-by}
==================================================================================

The indicator of which party is responsible for the service fees associated with the installment plan.  
These are the possible values:

* `CONSUMER`: The customer pays the fees.
* `MERCHANT`: The merchant pays the fees.

Specifications {#install-info-plan-details-fund-by_Specifications}
------------------------------------------------------------------

* **Data Type:** Array of string
* **Data Length:** 8

Mapping {#install-info-plan-details-fund-by_Mapping}
----------------------------------------------------

* **REST Field Name:** installmentInformation.planDetails.fundedBy
* **Simple Order Field Name:** No corresponding field.

installmentInformation. planDetails\[\]. identifier {#install-info-plan-details-id}
===================================================================================

The *plan registration system identifier* is the unique Relay-generated name of the Installment Plan. It consists of alphanumerical characters and is intended to be easily readable by you and your customers.  
Some processors and countries require that the plan registration system identifier be included in the initial authorization request for an installment plan. For more information about whether this requirement applies to your organization, contact your `Cybersource` account manager.

`Platform Connect`
:
* Authorizations:
* Field: 104
* Base II Clearing System
* Record: TCR D
* Position: 43-52
* SMS Raw Data Financial Transaction
* Record: 5-V22226

Specifications {#install-info-plan-details-id_Specifications}
-------------------------------------------------------------

* **Data Type:** String
* **Data Length:** 10

Mapping Information {#install-info-plan-details-id_Mapping}
-----------------------------------------------------------

* **REST API Field:** installmentInformation.planDetails\[\].identifier
* **Simple Order API Field:** No corresponding field.

installmentInformation. planDetails. isIslamicPlan {#install-info-plan-details-isIslamic-plan}
==============================================================================================

The indicator of whether the installment plan is an Islamic plan or not.  
These are the possible values:

* `true`: The plan should display text according to Shariah banking principles, such as using the term *profit* instead of *interest*.
* No value: The plan is not an Islamic plan and should not display text according to Shariah Banking principles.

Specifications {#install-info-plan-details-isIslamic-plan_Specifications}
-------------------------------------------------------------------------

* **Data Type:** Boolean
* **Data Length:** 5

Mapping {#install-info-plan-details-isIslamic-plan_Mapping}
-----------------------------------------------------------

* **REST Field Name:** installmentInformation.planDetails.isIslamicPlan
* **Simple Order Field Name:** No corresponding field.

**installmentInformation. id** {#install-info-id}
=================================================

Plan acceptance identifier is a unique confirmation identifier for the accepted installment plan.

Specifications {#install-info-id_Specifications}
------------------------------------------------

* **Data Type:** String
* **Data Length:** 50

Mapping Information {#install-info-id_Mapping}
----------------------------------------------

* **REST API Field:** installmentInformation.id
* **SCMP API Field:** No corresponding field.
* **Simple Order API Field:** No corresponding field.

installmentInformation. planId {#install-info-plan-id}
======================================================

Installment plan ID used to identify a specific installment plan for the installment services.

Specifications {#install-info-plan-id_Specifications}
-----------------------------------------------------

* **Data Type:** String
* **Data Length:** 50

Mapping Information {#install-info-plan-id_Mapping}
---------------------------------------------------

* **REST API Field:** installmentInformation.planId
* **SCMP API Field:** No corresponding field.
* **Simple Order API Field:** No corresponding field.

**installmentInformation. tcVersion** {#install-info-tc-vrsn}
=============================================================

Version of the Terms \& Conditions accepted by the consumer.  
The version is increased automatically every time the issuer updates the plans in the `Business Center`. The field value corresponds to the value of the plan.termsAndConditions\[\].version field from the get installment plans response.

Specifications {#install-info-tc-vrsn_Specifications}
-----------------------------------------------------

* **Data Type:** 36
* **Data Length:** String

Mapping Information {#install-info-tc-vrsn_Mapping}
---------------------------------------------------

* **REST API Field:** installmentInformation.tcVersion
* **SCMP API Field:** No corresponding field.
* **Simple Order API Field:** No corresponding field.

**paymentInformation. paymentAccountReference.id** {#payment-info-pay-acct-ref-id}
==================================================================================

Payment account reference (PAR) is a unique reference value associated with a specific card holder PAN.  
A PAR identifies the card account, not just a card. PAR is a non-payment identifier that can be associated to PANs and tokens, as defined by EMVCo. PAR allows all participants in the payments chain to have a single, non-sensitive value assigned to a consumer. This value can be used in place of sensitive card holder identification fields, and transmitted across the payments ecosystem to facilitate card holder identification.

Specifications {#payment-info-pay-acct-ref-id_Specifications}
-------------------------------------------------------------

* **Data Type:** String
* **Data Length:** 29

Mapping Information {#payment-info-pay-acct-ref-id_Mapping}
-----------------------------------------------------------

* **REST API Field:** paymentInformation.paymentAccountReference.id
* **SCMP API Field:** No corresponding field.
* **Simple Order API Field:** No corresponding field.

**processingInformation. authorizationOptions. authorizationCode** {#processing-info-auth-ops-auth-code}
========================================================================================================

Authorization code returned in an authorization response as the processorInformation.approvalCode field value. The authorization code is used to link follow-on services to the initial authorization.

Specifications {#processing-info-auth-ops-auth-code_Specifications}
-------------------------------------------------------------------

* **Data Type:** String
* **Data Length:** 6

Mapping Information {#processing-info-auth-ops-auth-code_Mapping}
-----------------------------------------------------------------

* **REST API Field:** processingInformation.authorizationOptions.authorizationCode
* **SCMP API Field:** No corresponding field.
* **Simple Order API Field:** No corresponding field.

**processingInformation. authorizationOptions. authorizationDateTime** {#processing-info-auth-ops-auth-date-time}
=================================================================================================================

Original transaction date and time of the initial authorization.  
The authorization date and time help to accurately retrieve a previous transaction when the processingInformation. authorizationOptions.networkTransactionId is not present.

Format:
:
`YYYY-MM-DDThh:mm:ssZ`

Format example:
:
`2016-08-11T22:47:57Z`

Date of example:
:
August 11, 2016, at 22:47:57 (10:47:57 pm)

Specifications {#processing-info-auth-ops-auth-date-time_Specifications}
------------------------------------------------------------------------

* **Data Type:** String
* **Data Length:** 20

Mapping Information {#processing-info-auth-ops-auth-date-time_Mapping}
----------------------------------------------------------------------

* **REST API Field:** processingInformation.authorizationOptions.authorizationDateTime
* **SCMP API Field:** No corresponding field.
* **Simple Order API Field:** No corresponding field.

**processingInformation. authorizationOptions. networkTransactionId** {#processing-info-auth-ops-ntwk-trans-id}
===============================================================================================================

Network transaction identifier (NTID) used to identify a previous transaction for the processor.  
The NTID is returned in the authorization response as the `processorInformation.networkTransactionId` field value. NTID is used in follow-services to link to the initial authorization.

Specifications {#processing-info-auth-ops-ntwk-trans-id_Specifications}
-----------------------------------------------------------------------

* **Data Type:** String
* **Data Length:** 20

Mapping Information {#processing-info-auth-ops-ntwk-trans-id_Mapping}
---------------------------------------------------------------------

* **REST API Field:** processingInformation.authorizationOptions.networkTransactionId
* **SCMP API Field:** No corresponding field.
* **Simple Order API Field:** No corresponding field.

**processingInformation. installmentServiceProvider** {#processing-info-instal-serv-prdr}
=========================================================================================

Service provider for the installment services.

Possible value:
:
`Relay`

Specifications {#processing-info-instal-serv-prdr_Specifications}
-----------------------------------------------------------------

* **Data Type:** String
* **Data Length:** 20

Mapping Information {#processing-info-instal-serv-prdr_Mapping}
---------------------------------------------------------------

* **REST API Field:** processingInformation.installmentServiceProvider
* **SCMP API Field:** No corresponding field.
* **Simple Order API Field:** No corresponding field.

**processingInformation. refundOptions.refundAmount** {#refund-ops-refund-amnt}
===============================================================================

Refund amount usually to specify an amount that is not the total captured amount, such as for a partial refund.  
The value cannot be negative. If multiple partial refunds are issued for the same capture, the values of the refund amounts cannot exceed the original captured amount.

Specifications {#refund-ops-refund-amnt_Specifications}
-------------------------------------------------------

* **Data Type:** String
* **Data Length:** 19

Mapping Information {#refund-ops-refund-amnt_Mapping}
-----------------------------------------------------

* **REST API Field:** processingInformation.refundOptions.refundAmount
* **SCMP API Field:** No corresponding field.
* **Simple Order API Field:** No corresponding field.

