Invoicing Developer Guide {#invoicing-about-guide}
==================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This guide is written for merchants who want to use the invoicing services. It describes tasks that a merchant performs to create, send, and manage invoices using the invoicing API. It also describes how to include extra security for your invoices with payer authentication and how to set up automated webhook notifications when an invoice is updated. It is intended to help the merchant provide a seamless customer payment experience.

Conventions
:
This statement appears in this document:

    > IMPORTANT
    > An *Important* statement contains information essential to successfully completing a task or learning a concept.

Related Documentation
:
Visit the [`Payment Gateway` documentation hub](https://developer.example.com/docs.md "") to find additional processor-specific versions of this guide and additional technical documentation.
:
Visit the [`Payment Gateway` documentation hub](https://developer.example.com/docs.md "") to find additional technical documentation.

Customer Support
:
For support information about any service, visit the Support Center:

<http://support.example.com>

Recent Revisions to This Document {#invoicing-doc-rev}
======================================================

26.04.01
--------

Added new section to support Amount Only Invoices. See [Create an Amount Only Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-simple-invoice-intro.md "").  
Added new optional fields for creating and sending invoices. See [Optional Fields for Invoice Creation](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-draft-intro/invoicing-services-create-opt-fields.md "").

26.02.02
--------

This revision contains only editorial changes and no technical updates.

26.02.01
--------

Added new fields and values to customize an invoice payment page settings. Request endpoints are also updated. See [Invoicing Settings API Requests](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-settings-intro.md "").

25.11.02
--------

Added a note about personally identifying information in Invoicing fields. See [Introduction to Invoicing](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/Introduction.md "").

25.11.01
--------

Added new overview graphic of invoice API requests. See [Invoicing API Requests](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro.md "").  
Removed the section Add Invoicing Add-In to Outlook.

25.06.02
--------

Updated the list of webhook event types that you can subscribe to receive notifications. See [Webhook Notifications for Invoicing](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-webhooks-intro.md "").

25.06.01
--------

This revision contains only editorial changes and no technical updates.

25.04.01
--------

This revision contains only editorial changes and no technical updates.

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Payment Gateway for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Payment Gateway.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.

Introduction to Invoicing {#Introduction}
=========================================

The Invoicing API enables you to create and send invoices as well as track outstanding invoices. Your customers can pay using their preferred payment method from any device on a secure `Payment Gateway` hosted website. Automated reminders are available to help you remind customers of upcoming due dates or overdue invoices. For more information, see [Invoicing API Requests](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro.md "").  
You can also customize your invoice payment page to display your brand logo and color, as well as add custom messages to your invoice emails. Shipping information and phone numbers can also be collected at the time of payment. For more information, see [Invoicing Settings API Requests](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-settings-intro.md "").  
The Invoicing API uses Payment Gateway's `Unified Checkout` to securely process payments so that you do not have to handle confidential payment data. Fraud and risk management tools are incorporated into `Unified Checkout` to prevent fraud and reduce chargebacks. For additional security, you can add payer authentication to your invoice payment processing. For more information, see [Add Payer Authentication to Invoicing](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-features-intro.md "").  
To receive notifications when an invoice is paid, sent, or cancelled, you can create a subscription to receive invoicing webhook notifications. For more information, see [Webhook Notifications for Invoicing](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-webhooks-intro.md "").

> IMPORTANT
> The merchant is responsible for complying with any legal and tax requirements when issuing invoices to clients. ` Payment Gateway ` does not certify that the invoicing tool meets any such client requirements.
> IMPORTANT
> Invoicing fields are strictly designated for non-personal data and must not be used to capture personally identifying information. You are prohibited from capturing, obtaining, or transmitting any personally identifying information in or through any invoicing fields, including merchant-defined data fields.  
> Personally identifying information includes, but is not limited to, address, payment card number, social security number, driver's license number, state-issued identification number, passport number, and card verification numbers (CVV, CVC2, CVV2, CID, CVN). In the event it is discovered that a merchant is capturing and/or transmitting personally identifying information, whether or not intentionally, the merchant's account is immediately suspended, which results in a rejection of any and all transaction requests submitted by the merchant after the point of suspension.

Requirements
------------

The Invoicing API requires a transaction MID account and API authentication before you can begin sending API messages to `Payment Gateway`. For more information, see the [REST Getting Started User Guide](https://developer.example.com/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md "") .

Configure `Unified Checkout`
----------------------------

Invoicing supports `Unified Checkout`, which enables you to accept numerous types of digital payments, such as Apple Pay, `Click to Pay`, and Google Pay.  
For more information about enabling these digital payments using `Unified Checkout`, see the [Enable Digital Payments](https://developer.example.com/docs/gateway/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro.md "") section in the *Digital Accept Secure Integration Developer Guide*.

Tokenization for Merchant-Initiated Transactions {#Introduction_mits}
---------------------------------------------------------------------

You can create Token Management Service (TMS) tokens from invoice transactions using Transaction Management in the `Business Center`.

> IMPORTANT
> If you create and use TMS tokens for merchant-initiated transactions (MITs), you must comply with the **Consent Agreement Provisions** as stated in the [*Improving Authorization Management for Transactions with Stored Credentials*](https://usa.relay.com/dam/VCOM/global/support-legal/documents/stored-credential-transaction-framework-vbs-10-may-17.pdf "") guide.

Sandbox Testing {#Introduction_invoice-settings-toc}
----------------------------------------------------

You can test invoicing API requests using the [Invoicing API Reference](https://developer.example.com/api-reference-assets/index.md#invoicing "") in the `Payment Gateway` developer center.

Invoicing API Requests {#invoicing-services-intro}
==================================================

When creating a new invoice, you can choose to create a *draft* invoice or *published* invoice. If you create a published invoice, you can specify whether the invoice is immediately emailed to the customer or not. This graphic illustrates the different types of invoice creation requests and the follow-on requests that you can send.

#### Figure:

Overview of Invoicing Requests ![invoice creation requests and follow-on requests](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/invoicing/images/invoicing-request-flow-660x600.svg/jcr:content/renditions/original)  
This table describes the different invoicing creation requests.

|             Invoice Method             |                                                                                                                                                                                                                                                         Description                                                                                                                                                                                                                                                          |                                  Field Values Specific to this Method                                  |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Create a Draft Invoice                 | Create an invoice draft that is only viewable by you. To share the invoice with the customer, you must first publish it by sending a *send invoice* request. When published, you can send your customer the generated invoice URL. This method gives you control over the distribution of your invoices. For more information, see [Create a Draft Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-draft-intro.md ""). | invoiceInformation.deliveryMode : Set to `none`. invoiceInformation.sendImmediately : Set to `false`.  |
| Create a Deliverable Draft Invoice     | Create a draft invoice that is only viewable by you, and will be emailed to your customer when you publish it. To publish it, you must send a *send invoice* request. For more information, see [Create a Deliverable Draft Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-draft-dlvr-intro.md "").                                                                                                                   | invoiceInformation.deliveryMode : Set to `email`. invoiceInformation.sendImmediately : Set to `false`. |
| Create and Send an Invoice Immediately | Create a published invoice that is immediately emailed to the customer by Payment Gateway. Your customer can view and pay the invoice when they receive the invoice email. For more information, see [Create and Send an Invoice Immediately](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-send-intro.md "").                                                                                                                    | invoiceInformation.deliveryMode : Set to `email`. invoiceInformation.sendImmediately : Set to `true`.  |
| Create an Invoice without Sending it   | Create a published invoice that you can share with the customer by sending the customer the generated URL. This method gives you control over the distribution of your invoices. For more information, see [Create an Invoice without Sending it](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-intro.md "").                                                                                                                 | invoiceInformation.deliveryMode : Set to `none`. invoiceInformation.sendImmediately : Set to `true`.   |
[Invoice Creation Requests]

The Invoicing API also enables you to send these follow-on requests to manage the invoice:

* [Send or resend an invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-send-intro.md "")
* [Get an invoice's details](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-get-details-intro.md "")
* [Get lists of invoices](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-get-list-intro.md "")
* [Update an invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-update-intro.md "")
* [Cancel an invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-cancel-intro.md "")  
  You can also customize your invoices to align with your brand. For more information about customizing your invoice settings, see [Invoicing Settings API Requests](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-settings-intro.md "").

Create a Draft Invoice {#invoicing-services-create-draft-intro}
===============================================================

Drafting an invoice creates an unpublished invoice that is viewable only by you. When sending the draft invoice request, set the invoiceInformation.deliveryMode field to `none` to ensure that the invoice draft is not automatically sent in an email message to the customer when the invoice is published. When you are ready to publish the draft invoice, you can send a *send invoice* request. After publishing the drafted invoice, the invoice's status updates from `DRAFT` to `CREATED`. The created invoice is then shareable with the customer.

**Itemized Invoices**
:
An invoice can display a single billed amount or list up to 30 billed items. To list the billed items in the invoice, include the items in the request using the line item array fields. An invoice with line items is known as an *itemized* invoice. For more information about how to include line items in your request, see [Including Line Items in an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-line-items.md "").

**Invoice Numbers**
:
You can assign a unique invoice number in the invoiceInformation.invoiceNumber request field. The invoice number is required for follow-on API requests and tracking. You should store the invoice number in your system so that you can optimally perform the follow-on requests. If you do not include a unique invoice number when creating an invoice, `Payment Gateway` generates a unique invoice number for you in the invoiceInformation.invoiceNumber response field. IMPORTANT You cannot update the invoice number after it is generated.

**Installment Payments**
:
Invoices can be paid in installment payments when these fields and values are included in the request. If an invoice is payable in installments, multiple customers can make payments towards the same invoice.

    invoiceInformation.allowPartialPayments
    :
        Set to `true`.


    orderInformation.amountDetails.minimumPartialAmount
    :
        Set to the minimum amount allowed for a partial payment.

**Partner Information**
:
If your merchant account is associated with a `Payment Gateway` partner, you can include your partner solution ID (PSID) in the request message for tracking and reporting purposes. To include your PSID, use the clientReferenceInformation.partner.solutionId request field and set its field value to your PSID.

**Alternative Methods to Create an Invoice**
:
To create a *draft* invoice that is sent in an email message to the customer when you publish it, see [Create a Draft Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-draft-intro.md "").

    To create a new invoice that is **not** immediately sent in an email to the customer, see [Create an Invoice without Sending it](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-intro.md "").

    To create **and send** a new invoice at the same time, see [Create and Send an Invoice Immediately](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-send-intro.md "").

Endpoint
--------

Send an API POST request message to one of these endpoints:  
**Test:** `POST ``https://apitest.example.com``/invoicing/v2/invoices`  
**Production:** `POST ``https://api.example.com``/invoicing/v2/invoices`  
**India Production:** `POST https://api.in.example.com/invoicing/v2/invoices`

Response to a Successful Request
--------------------------------

A successfully drafted invoice is indicated by the `DRAFT` status in the status response field.  
The redirect URL generated in the invoiceInformation.paymentLink response field is usable only by you and not the customer.  
Additional invoice details are included in the response message for you to review.

Follow-On API Requests
----------------------

After successfully drafting an invoice, you can send these follow-on API requests.

**Send an Invoice**
:
After drafting an invoice, you can publish and send an invoice using the send invoice request. For more information, see [Send an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-send-intro.md "").

**Update an Invoice**
:
To update customer information or item details in an already drafted invoice, send an update invoice request. For more information, see [Update an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-update-intro.md "").

**Cancel an Invoice**
:
To cancel a drafted invoice, send the a cancel invoice request. For more information, see [Cancel an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-cancel-intro.md "").

**Get Invoice Details**
:
To retrieve a drafted invoice's details, send a get invoice details request. For more information, see [Get Invoice Details](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-get-details-intro.md "").

Required Fields for Drafting an Invoice {#invoicing-services-create-draft-req-fields}
=====================================================================================

This section lists the required fields necessary to create these types of invoices:
* In-person draft invoice
* Email draft invoice
* Itemized email draft invoice

The invoice created using these fields and specified values is not immediately sent to the customer.

Required Fields for Drafting an In-Person Invoice
-------------------------------------------------

invoiceInformation.deliveryMode
:
Set to one of these possible values to determine whether or not the invoice is emailed to the customer when you send a send invoice request:

    * `email`: An invoice email is sent to the customer when you send the follow-on send invoice request for this invoice draft. The invoice status updates to `SENT`.
    * `none`: When you process a follow-on send invoice request to publish the drafted invoice, the invoice is not sent in an email to the customer. To share the invoice with the customer, send the customer the redirect URL in the invoiceInformation.paymentLink response field. The invoice updates change to `CREATED`.

invoiceInformation.description
:

invoiceInformation.dueDate
:

invoiceInformation.sendImmediately
:
Set to `false`.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

Required Fields for Drafting an Email Invoice {#invoicing-services-create-draft-req-fields_customer-fields}
-----------------------------------------------------------------------------------------------------------

customerInformation.email
:

customerInformation.name
:

invoiceInformation.deliveryMode
:
Set to `email`.

invoiceInformation.dueDate
:

invoiceInformation.sendImmediately
:
Set to `false`.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

Required Fields for Drafting an Invoice with Line Items {#invoicing-services-create-draft-req-fields_line-item-fields}
----------------------------------------------------------------------------------------------------------------------

customerInformation.email
:

customerInformation.name
:

invoiceInformation.deliveryMode
:
Set to one of these possible values to determine whether or not the invoice will be emailed to the customer when you send a send invoice request:

    * `email`: An invoice email is sent to the customer when you send the follow-on send invoice request for this invoice draft. The invoice status will change to `SENT`.
    * `none`: When you process a follow-on send invoice request to publish the drafted invoice, the invoice is not sent in an email to the customer. To share the invoice with the customer, send the customer the redirect URL in the invoiceInformation.paymentLink response field. The invoice status will change to `CREATED`.

invoiceInformation.dueDate
:

invoiceInformation.sendImmediately
:
Set to `false`.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.lineItems\[\].productName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

orderInformation.lineItems\[\].productSku
:

[orderInformation.lineItems\[\].quantity](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

[orderInformation.lineItems\[\].totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

Optional Fields for Invoice Creation {#invoicing-services-create-opt-fields}
============================================================================

You can include these optional fields when sending create invoice requests:

[clientReferenceInformation.partner.developerId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
Set to your developer ID.

[clientReferenceInformation.partner.solutionId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
Set to your partner solution ID (PSID).

customerInformation.company.name
:

customerInformation.email
:

customerInformation.merchantCustomerId
:

customerInformation.name
:

invoiceInformation.allowPartialPayments
:
Set to one of these possible values:

    * `false`: The invoice must be paid in a single payment.
    * `true`: The invoice is payable in installments.

invoiceInformation.deliveryMode
:

invoiceInformation.description
:
This field becomes optional when either one of these conditions is met:

    * The line item fields are present in the request message.
    * When drafting a deliverable invoice, the invoiceInformation.deliveryMode request field is set to `email`.

invoiceInformation.expirationDate
:
Set to the expiration date. Format: `DD-MM-YYYY`
:
The invoice expires on this date at 00:00 GMT

invoiceInformation.invoiceNumber
:
Set to a unique number to create an invoice number.

    If you do not include this field and a unique value, the invoicing API automatically generates an invoice number for the new invoice.

    > IMPORTANT You cannot update this invoice number after sending the API request.

merchantDefinedFieldValues.definition.id\[\].value
:

orderInformation.amountDetails.freight.amount
:

orderInformation.amountDetails.freight.taxable
:

orderInformation.amountDetails.freight.taxRate
:

orderInformation.amountDetails.minimumPartialAmount
:

orderInformation.amountDetails.subAmount
:

Optional Fields for Discounts and Taxes {#invoicing-services-opt-details-tax-fields}
====================================================================================

You can include discounts and taxes to either the total billed amount or to billed line items in an invoice.

> IMPORTANT You cannot include discounts or taxes to both the total billed amount and line items in the same request.
> IMPORTANT
> The merchant is responsible for complying with any legal and tax requirements when issuing invoices to clients. ` Payment Gateway ` does not certify that the invoicing tool meets any such client requirements.

Discount Fields for the Invoice Total
-------------------------------------

[orderInformation.amountDetails.discountAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-discount-amount.md "")
:

orderInformation.amountDetails.discountPercent
:

Discount Fields for Line Items
------------------------------

[orderInformation.lineItems\[\].discountAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-discount-amount.md "")
:

[orderInformation.lineItems\[\].discountRate](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-discount-rate.md "")
:

Tax Fields for the Invoice Total
--------------------------------

orderInformation.amountDetails.taxDetails.amount
:

orderInformation.amountDetails.taxDetails.rate
:

orderInformation.amountDetails.taxDetails.type
:

Tax Fields for Line Items
-------------------------

[orderInformation.lineItems\[\].taxAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-amount-request.md "")
:

[orderInformation.lineItems\[\].taxRate](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-rate.md "")
:

Example: Drafting an Invoice {#invoicing-services-create-draft-done-ex-rest}
============================================================================

Request

```
{
  "invoiceInformation": {
    "description": "Food",
    "dueDate": "2019-07-11",
    "sendImmediately": false,
    "deliveryMode": "none"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "2623.64",
      "currency": "USD"
    }
  }
}
```

Response to a Successful Request

```keyword
{
  "_links": {
    "self": {
      "href": "/v2/invoices/98762",
      "method": "GET"
    },
    "update": {
      "href": "/v2/invoices/98762",
      "method": "PUT"
    },
    "deliver": {
      "href": "/v2/invoices/98762/delivery",
      "method": "POST"
    },
    "cancel": {
      "href": "/v2/invoices/98762/cancelation",
      "method": "POST"
    }
  },
  "id": "98762",
  "submitTimeUtc": "2024-08-02T19:24:06.184293960Z",
  "status": "CREATED",
  "processingInformation": {
    "requestPhone": false,
    "requestShipping": false
  },
  "invoiceInformation": {
    "invoiceNumber": "98762",
    "description": "Food",
    "dueDate": "2019-07-11",
    "allowPartialPayments": false,
    "paymentLink": "https://businesscenter.example.com/ebc2/invoicing/payInvoice/NyvghJCpsrrZAjkvZNxelqUrI7iyOdLXFXWS8e5MLXyLYbifinsuYfBk6kaYo3co?version=v2.1",
    "deliveryMode": "None"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 2623.64,
      "currency": "USD",
      "balanceAmount": 2623.64
    }
  }
}
```

Request

```
{
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "tanya.lee@my-email.world"
  },
  "invoiceInformation": {
    "dueDate": "2019-07-11",
    "sendImmediately": false,
    "deliveryMode": "none"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "293.50",
      "currency": "USD"
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "quantity": "20",
        "unitPrice": "12.05",
        "totalAmount": "241.00"
      },
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "quantity": "10",
        "unitPrice": "5.25",
        "totalAmount": "52.50"
      }
    ]
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "self": {
      "href": "/v2/invoices/98764",
      "method": "GET"
    },
    "update": {
      "href": "/v2/invoices/98764",
      "method": "PUT"
    },
    "deliver": {
      "href": "/v2/invoices/98764/delivery",
      "method": "POST"
    },
    "cancel": {
      "href": "/v2/invoices/98764/cancelation",
      "method": "POST"
    }
  },
  "id": "98764",
  "submitTimeUtc": "2024-08-02T22:14:13.000671718Z",
  "status": "DRAFT",
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "tanya.lee@my-email.world"
  },
  "processingInformation": {
    "requestPhone": false,
    "requestShipping": false
  },
  "invoiceInformation": {
    "invoiceNumber": "98764",
    "dueDate": "2019-07-11",
    "allowPartialPayments": false,
    "deliveryMode": "None"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 293.5,
      "currency": "USD"
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 12.05,
        "quantity": 20,
        "totalAmount": 241
      },
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 5.25,
        "quantity": 10,
        "totalAmount": 52.5
      }
    ]
  }
}
```

REST Interactive Example: Create an Invoice Draft {#invoicing-services-create-draft-ex-live}
============================================================================================

Click this image to access the interactive code example for creating a invoice draft.

#### Figure: {#invoicing-services-create-draft-ex-live_cybs-create-invoice}

Interactive Code [![Image and link to the interactive code example for creating a new
invoice.](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/invoicing/images/invoicing-services-create.png/jcr:content/renditions/original)](https://developer.example.com/api-reference-assets/index.md#invoicing_invoices_create-a-new-invoice "")

Create a Deliverable Draft Invoice {#invoicing-services-create-draft-dlvr-intro}
================================================================================

Drafting an invoice creates an unpublished invoice that is viewable only by you. To draft an invoice that will be delivered to the customer in an email message when you publish it, set the invoiceInformation.deliveryMode request field to `email`. When you are ready to publish and share the invoice with a customer, you can send the follow-on *send invoice* request. The customer will then receive an email with the invoice and the invoice's status will update from `DRAFT` to `SENT`.

**Itemized Invoices**
:
An invoice can display a single billed amount or list up to 30 billed items. To list the billed items in the invoice, include the items in the request using the line item array fields. An invoice with line items is known as an *itemized* invoice. For more information about how to include line items in your request, see [Including Line Items in an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-line-items.md "").

**Invoice Numbers**
:
You can assign a unique invoice number in the invoiceInformation.invoiceNumber request field. The invoice number is required for follow-on API requests and tracking. You should store the invoice number in your system so that you can optimally perform the follow-on requests. If you do not include a unique invoice number when creating an invoice, `Payment Gateway` generates a unique invoice number for you in the invoiceInformation.invoiceNumber response field. IMPORTANT You cannot update the invoice number after it is generated.

**Installment Payments**
:
Invoices can be paid in installment payments when these fields and values are included in the request. If an invoice is payable in installments, multiple customers can make payments towards the same invoice.

    invoiceInformation.allowPartialPayments
    :
        Set to `true`.


    orderInformation.amountDetails.minimumPartialAmount
    :
        Set to the minimum amount allowed for a partial payment.

**Partner Information**
:
If your merchant account is associated with a `Payment Gateway` partner, you can include your partner solution ID (PSID) in the request message for tracking and reporting purposes. To include your PSID, use the clientReferenceInformation.partner.solutionId request field and set its field value to your PSID.

**Alternative Methods to Create an Invoice**
:
To create a *draft* invoice that is **not** sent in an email message to the customer when you publish it, see [Create a Draft Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-draft-intro.md "").

    To create a new invoice that is **not** immediately sent in an email message to the customer, see [Create an Invoice without Sending it](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-intro.md "").

    To create **and send** a new invoice at the same time, see [Create and Send an Invoice Immediately](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-send-intro.md "").

Endpoint
--------

Send an API POST request message to one of these endpoints:  
**Test:** `POST ``https://apitest.example.com``/invoicing/v2/invoices`  
**Production:** `POST ``https://api.example.com``/invoicing/v2/invoices`  
**India Production:** `POST https://api.in.example.com/invoicing/v2/invoices`

Response to a Successful Request
--------------------------------

A successfully drafted invoice is indicated by the `DRAFT` status in the status response field.  
The redirect URL generated in the invoiceInformation.paymentLink response field is usable only by you and not the customer.  
Additional invoice details are included in the response message for you to review.

Follow-On API Requests
----------------------

After successfully drafting an invoice, you can send these follow-on API requests.

**Send an Invoice**
:
After drafting an invoice, you can publish and send an invoice using the send invoice request. For more information, see [Send an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-send-intro.md "").

**Update an Invoice**
:
To update customer information or item details in an already drafted invoice, send an update invoice request. For more information, see [Update an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-update-intro.md "").

**Cancel an Invoice**
:
To cancel a drafted invoice, send the a cancel invoice request. For more information, see [Cancel an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-cancel-intro.md "").

**Get Invoice Details**
:
To retrieve a drafted invoice's details, send a get invoice details request. For more information, see [Get Invoice Details](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-get-details-intro.md "").

Required Fields for Drafting an Invoice {#invoicing-services-create-draft-dlvr-req-fields}
==========================================================================================

This section lists the required fields necessary to create these types of invoices:
* In-person draft invoice
* Email draft invoice
* Itemized email draft invoice

The invoice created using these fields and specified values is not immediately sent to the customer.

Required Fields for Drafting an In-Person Invoice
-------------------------------------------------

invoiceInformation.deliveryMode
:
Set to one of these possible values to determine whether or not the invoice is emailed to the customer when you send a send invoice request:

    * `email`: An invoice email is sent to the customer when you send the follow-on send invoice request for this invoice draft. The invoice status updates to `SENT`.
    * `none`: When you process a follow-on send invoice request to publish the drafted invoice, the invoice is not sent in an email to the customer. To share the invoice with the customer, send the customer the redirect URL in the invoiceInformation.paymentLink response field. The invoice updates change to `CREATED`.

invoiceInformation.description
:

invoiceInformation.dueDate
:

invoiceInformation.sendImmediately
:
Set to `false`.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

Required Fields for Drafting an Email Invoice {#invoicing-services-create-draft-dlvr-req-fields_customer-fields}
----------------------------------------------------------------------------------------------------------------

customerInformation.email
:

customerInformation.name
:

invoiceInformation.deliveryMode
:
Set to `email`.

invoiceInformation.dueDate
:

invoiceInformation.sendImmediately
:
Set to `false`.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

Required Fields for Drafting an Invoice with Line Items {#invoicing-services-create-draft-dlvr-req-fields_line-item-fields}
---------------------------------------------------------------------------------------------------------------------------

customerInformation.email
:

customerInformation.name
:

invoiceInformation.deliveryMode
:
Set to one of these possible values to determine whether or not the invoice will be emailed to the customer when you send a send invoice request:

    * `email`: An invoice email is sent to the customer when you send the follow-on send invoice request for this invoice draft. The invoice status will change to `SENT`.
    * `none`: When you process a follow-on send invoice request to publish the drafted invoice, the invoice is not sent in an email to the customer. To share the invoice with the customer, send the customer the redirect URL in the invoiceInformation.paymentLink response field. The invoice status will change to `CREATED`.

invoiceInformation.dueDate
:

invoiceInformation.sendImmediately
:
Set to `false`.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.lineItems\[\].productName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

orderInformation.lineItems\[\].productSku
:

[orderInformation.lineItems\[\].quantity](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

[orderInformation.lineItems\[\].totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

Optional Fields for Invoice Creation {#invoicing-services-create-dlvr-opt-fields}
=================================================================================

You can include these optional fields when sending create invoice requests:

[clientReferenceInformation.partner.developerId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
Set to your developer ID.

[clientReferenceInformation.partner.solutionId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
Set to your partner solution ID (PSID).

customerInformation.company.name
:

customerInformation.email
:

customerInformation.merchantCustomerId
:

customerInformation.name
:

invoiceInformation.allowPartialPayments
:
Set to one of these possible values:

    * `false`: The invoice must be paid in a single payment.
    * `true`: The invoice is payable in installments.

invoiceInformation.deliveryMode
:

invoiceInformation.description
:
This field becomes optional when either one of these conditions is met:

    * The line item fields are present in the request message.
    * When drafting a deliverable invoice, the invoiceInformation.deliveryMode request field is set to `email`.

invoiceInformation.expirationDate
:
Set to the expiration date. Format: `DD-MM-YYYY`
:
The invoice expires on this date at 00:00 GMT

invoiceInformation.invoiceNumber
:
Set to a unique number to create an invoice number.

    If you do not include this field and a unique value, the invoicing API automatically generates an invoice number for the new invoice.

    > IMPORTANT You cannot update this invoice number after sending the API request.

merchantDefinedFieldValues.definition.id\[\].value
:

orderInformation.amountDetails.freight.amount
:

orderInformation.amountDetails.freight.taxable
:

orderInformation.amountDetails.freight.taxRate
:

orderInformation.amountDetails.minimumPartialAmount
:

orderInformation.amountDetails.subAmount
:

Optional Fields for Discounts and Taxes {#invoicing-services-opt-details-dlvr-tax-fields}
=========================================================================================

You can include discounts and taxes to either the total billed amount or to billed line items in an invoice.

> IMPORTANT You cannot include discounts or taxes to both the total billed amount and line items in the same request.
> IMPORTANT
> The merchant is responsible for complying with any legal and tax requirements when issuing invoices to clients. ` Payment Gateway ` does not certify that the invoicing tool meets any such client requirements.

Discount Fields for the Invoice Total
-------------------------------------

[orderInformation.amountDetails.discountAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-discount-amount.md "")
:

orderInformation.amountDetails.discountPercent
:

Discount Fields for Line Items
------------------------------

[orderInformation.lineItems\[\].discountAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-discount-amount.md "")
:

[orderInformation.lineItems\[\].discountRate](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-discount-rate.md "")
:

Tax Fields for the Invoice Total
--------------------------------

orderInformation.amountDetails.taxDetails.amount
:

orderInformation.amountDetails.taxDetails.rate
:

orderInformation.amountDetails.taxDetails.type
:

Tax Fields for Line Items
-------------------------

[orderInformation.lineItems\[\].taxAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-amount-request.md "")
:

[orderInformation.lineItems\[\].taxRate](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-rate.md "")
:

Example: Drafting a Deliverable Invoice {#invoicing-services-create-draft-ex-rest}
==================================================================================

Request

```
{
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "tanya.lee@my-email.world"
  },
  "invoiceInformation": {
    "dueDate": "2019-07-11",
    "sendImmediately": false,
    "deliveryMode": "email"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "247.86",
      "currency": "USD"
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "quantity": "20",
        "unitPrice": "12.05",
        "totalAmount": "247.86"
      }
    ]
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "self": {
      "href": "/v2/invoices/2669",
      "method": "GET"
    },
    "update": {
      "href": "/v2/invoices/2669",
      "method": "PUT"
    },
    "deliver": {
      "href": "/v2/invoices/2669/delivery",
      "method": "POST"
    },
    "cancel": {
      "href": "/v2/invoices/2669/cancelation",
      "method": "POST"
    }
  },
  "id": "2669",
  "submitTimeUtc": "2024-07-24T18:24:36.153361386Z",
  "status": "DRAFT",
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "tanya.lee@my-email.world"
  },
  "processingInformation": {
    "requestPhone": false,
    "requestShipping": false
  },
  "invoiceInformation": {
    "invoiceNumber": "2669",
    "dueDate": "2019-07-11",
    "allowPartialPayments": false,
    "deliveryMode": "Email"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 247.86,
      "currency": "USD",
      "balanceAmount": 247.86
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 12.05,
        "quantity": 20,
        "totalAmount": 247.86
      }
    ]
  }
}
```

Request

```
{
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "tanya.lee@my-email.world"
  },
  "invoiceInformation": {
    "dueDate": "2019-07-11",
    "sendImmediately": false,
    "deliveryMode": "email"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 293.5,
      "currency": "USD"
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 12.05,
        "quantity": 20,
        "totalAmount": 241
      },
      {
        "productSku": "P653727383",
        "productName": "Second line item's name",
        "unitPrice": 5.25,
        "quantity": 10,
        "totalAmount": 52.5
      }
    ]
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "self": {
      "href": "/v2/invoices/98765",
      "method": "GET"
    },
    "update": {
      "href": "/v2/invoices/98765",
      "method": "PUT"
    },
    "deliver": {
      "href": "/v2/invoices/98765/delivery",
      "method": "POST"
    },
    "cancel": {
      "href": "/v2/invoices/98765/cancelation",
      "method": "POST"
    }
  },
  "id": "98765",
  "submitTimeUtc": "2024-08-02T22:18:24.341304588Z",
  "status": "DRAFT",
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "tanya.lee@my-email.world"
  },
  "processingInformation": {
    "requestPhone": false,
    "requestShipping": false
  },
  "invoiceInformation": {
    "invoiceNumber": "98765",
    "dueDate": "2019-07-11",
    "allowPartialPayments": false,
    "deliveryMode": "Email"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 293.5,
      "currency": "USD",
      "balanceAmount": 293.5
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 12.05,
        "quantity": 20,
        "totalAmount": 241
      },
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 5.25,
        "quantity": 10,
        "totalAmount": 52.5
      }
    ]
  }
}
```

REST Interactive Example: Create an Invoice Draft {#invoicing-services-create-draft-dlvr-ex-live}
=================================================================================================

Click this image to access the interactive code example for creating a invoice draft.

#### Figure: {#invoicing-services-create-draft-dlvr-ex-live_d11e20}

Interactive Code [![Image and link to the interactive code example for creating a new
invoice.](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/invoicing/images/invoicing-services-create.png/jcr:content/renditions/original)](https://developer.example.com/api-reference-assets/index.md#invoicing_invoices_create-a-new-invoice "")

Create and Send an Invoice Immediately {#invoicing-services-create-send-intro}
==============================================================================

Creating and sending an invoice publishes a payable invoice that is automatically emailed to the customer. In addition to the sent email, you can also share the invoice by sending the customer the redirect URL generated in the invoiceInformation.paymentLink response field.

**Itemized Invoices**
:
An invoice can display a single billed amount or list up to 30 billed items. To list the billed items in the invoice, include the items in the request using the line item array fields. An invoice with line items is known as an *itemized* invoice. For more information about how to include line items in your request, see [Including Line Items in an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-line-items.md "").

**Invoice Numbers**
:
You can assign a unique invoice number in the invoiceInformation.invoiceNumber request field. The invoice number is required for follow-on API requests and tracking. You should store the invoice number in your system so that you can optimally perform the follow-on requests. If you do not include a unique invoice number when creating an invoice, `Payment Gateway` generates a unique invoice number for you in the invoiceInformation.invoiceNumber response field. IMPORTANT You cannot update the invoice number after it is generated.

**Installment Payments**
:
Invoices can be paid in installment payments when these fields and values are included in the request. If an invoice is payable in installments, multiple customers can make payments towards the same invoice.

    invoiceInformation.allowPartialPayments
    :
        Set to `true`.


    orderInformation.amountDetails.minimumPartialAmount
    :
        Set to the minimum amount allowed for a partial payment.

**Partner Information**
:
If your merchant account is associated with a `Payment Gateway` partner, you can include your partner solution ID (PSID) in the request message for tracking and reporting purposes. To include your PSID, use the clientReferenceInformation.partner.solutionId request field and set its field value to your PSID.

**Alternative Methods to Create an Invoice**
:
To create a new invoice that is **not** immediately sent in an email to the customer, see [Create an Invoice without Sending it](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-intro.md "").

    To create an invoice **draft** that is not payable or viewable to the customer, see [Create a Draft Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-draft-intro.md "").

Endpoint
--------

Send an API POST request message to one of these endpoints:  
**Test:** `POST ``https://apitest.example.com``/invoicing/v2/invoices`  
**Production:** `POST ``https://api.example.com``/invoicing/v2/invoices`  
**India Production:** `POST https://api.in.example.com/invoicing/v2/invoices`

Successful Response
-------------------

A successfully created and sent invoice is indicated by the `SENT` status in the status response field. The response message also includes the newly created invoice's details.

Follow-On API Requests
----------------------

After creating an invoice, you can send these follow-on API requests.

**Update an Invoice**
:
To update customer information or item details in an invoice, send an update invoice request. For more information, see [Update an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-update-intro.md "").

**Cancel an Invoice**
:
To cancel an invoice, send a cancel invoice request. For more information, see [Cancel an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-cancel-intro.md "").

**Get Invoice Details**
:
You can retrieve an invoice's details by sending a get invoice details request. For more information, see [Get Invoice Details](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-get-details-intro.md "").

**Get List of Invoices**
:
After creating multiple invoices, you might want to search for certain invoices. To retrieve a filtered list of invoices, send a get list of invoices request. For more information, see [Get a List of Invoices](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-get-list-intro.md "").

Required Fields for Creating and Sending an Invoice {#invoicing-services-create-send-req-fields}
================================================================================================

This section lists the required fields necessary to create and send these types of invoices:
* Email invoice
* Itemized email invoice

Required Fields for an Email Invoice {#invoicing-services-create-send-req-fields_customer-fields}
-------------------------------------------------------------------------------------------------

customerInformation.email
:

customerInformation.name
:

invoiceInformation.deliveryMode
:
Set to `email`.

invoiceInformation.description
:

invoiceInformation.dueDate
:

invoiceInformation.sendImmediately
:
Set to `true`.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

Required Fields for an Email Invoice with Line Items {#invoicing-services-create-send-req-fields_line-item-fields}
------------------------------------------------------------------------------------------------------------------

customerInformation.email
:

customerInformation.name
:

invoiceInformation.deliveryMode
:
Set to `email`.

invoiceInformation.dueDate
:

invoiceInformation.sendImmediately
:
Set to `true`.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.lineItems\[\].productName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

orderInformation.lineItems\[\].productSku
:

[orderInformation.lineItems\[\].quantity](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

[orderInformation.lineItems\[\].totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

Optional Fields for Invoice Creation {#invoicing-services-create-send-opt-fields}
=================================================================================

You can include these optional fields when sending create invoice requests:

[clientReferenceInformation.partner.developerId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
Set to your developer ID.

[clientReferenceInformation.partner.solutionId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
Set to your partner solution ID (PSID).

customerInformation.company.name
:

customerInformation.email
:

customerInformation.merchantCustomerId
:

customerInformation.name
:

invoiceInformation.allowPartialPayments
:
Set to one of these possible values:

    * `false`: The invoice must be paid in a single payment.
    * `true`: The invoice is payable in installments.

invoiceInformation.deliveryMode
:

invoiceInformation.description
:
This field is optional when the line item fields are present in the request message.

invoiceInformation.expirationDate
:
Set to the expiration date. Format: `DD-MM-YYYY`
:
The invoice expires on this date at 00:00 GMT

invoiceInformation.invoiceNumber
:
Set to a unique number to create an invoice number.

    If you do not include this field and a unique value, the invoicing API automatically generates an invoice number for the new invoice.

    > IMPORTANT You cannot update this invoice number after sending the API request.

merchantDefinedFieldValues.definition id\[\].value
:

orderInformation.amountDetails.freight.amount
:

orderInformation.amountDetails.freight.taxable
:

orderInformation.amountDetails.freight.taxRate
:

orderInformation.amountDetails.minimumPartialAmount
:

orderInformation.amountDetails.subAmount
:

Example: Creating and Sending an Invoice {#invoicing-services-create-send-ex-rest}
==================================================================================

Request

```
{
  "customerInformation": {
    "email": "test@email.com"
  },
  "invoiceInformation": {
    "description": "This is a test invoice",
    "dueDate": "2019-07-11",
    "sendImmediately": true,
    "deliveryMode": "email"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "2623.64",
      "currency": "USD"
    }
  }
}
```

Response to a Successful Request

```keyword
{
  "_links": {
    "self": {
      "href": "/v2/invoices/98768",
      "method": "GET"
    },
    "update": {
      "href": "/v2/invoices/98768",
      "method": "PUT"
    },
    "deliver": {
      "href": "/v2/invoices/98768/delivery",
      "method": "POST"
    },
    "cancel": {
      "href": "/v2/invoices/98768/cancelation",
      "method": "POST"
    }
  },
  "id": "98768",
  "submitTimeUtc": "2024-08-03T00:40:31.143121084Z",
  "status": "SENT",
  "customerInformation": {
    "email": "test@email.com"
  },
  "processingInformation": {
    "requestPhone": false,
    "requestShipping": false
  },
  "invoiceInformation": {
    "invoiceNumber": "98768",
    "description": "This is a test invoice",
    "dueDate": "2019-07-11",
    "allowPartialPayments": false,
    "paymentLink": "https://businesscenter.example.com/ebc2/invoicing/payInvoice/2AgCNHLrUtD7hfFR5SVh5DSxISAbFD9zybhUjpxpZuXKLQVyuLttP78uWWLRSSNX?version=v2.1",
    "deliveryMode": "Email"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 2623.64,
      "currency": "USD",
      "balanceAmount": 2623.64
    }
  }
}
```

Request

```
{
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "tanya.lee@my-email.world"
  },
  "invoiceInformation": {
    "dueDate": "2019-07-11",
    "sendImmediately": true,
    "deliveryMode": "email"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 293.5,
      "currency": "USD"
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 12.05,
        "quantity": 20,
        "totalAmount": 241
      },
      {
        "productSku": "P653727383",
        "productName": "Second line item's name",
        "unitPrice": 5.25,
        "quantity": 10,
        "totalAmount": 52.5
      }
    ]
  }
}
```

Response to a Successful Request

```keyword
{
  "_links": {
    "self": {
      "href": "/v2/invoices/98769",
      "method": "GET"
    },
    "update": {
      "href": "/v2/invoices/98769",
      "method": "PUT"
    },
    "deliver": {
      "href": "/v2/invoices/98769/delivery",
      "method": "POST"
    },
    "cancel": {
      "href": "/v2/invoices/98769/cancelation",
      "method": "POST"
    }
  },
  "id": "98769",
  "submitTimeUtc": "2024-08-03T00:43:05.320320438Z",
  "status": "SENT",
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "test@email.com"
  },
  "processingInformation": {
    "requestPhone": false,
    "requestShipping": false
  },
  "invoiceInformation": {
    "invoiceNumber": "98769",
    "dueDate": "2019-07-11",
    "allowPartialPayments": false,
    "paymentLink": "https://businesscenter.example.com/ebc2/invoicing/payInvoice/XvgrhdaVUbBJb466S9nxqXpp1e2UHoFEUlhye9gtiwgi7gzv5fwqV8YgfP6xep0D?version=v2.1",
    "deliveryMode": "Email"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 293.5,
      "currency": "USD",
      "balanceAmount": 293.5
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 12.05,
        "quantity": 20,
        "totalAmount": 241
      },
      {
        "productSku": "P653727383",
        "productName": "Second line item's name",
        "unitPrice": 5.25,
        "quantity": 10,
        "totalAmount": 52.5
      }
    ]
  }
}
```

REST Interactive Example: Create and Send an Invoice {#invoicing-services-create-send-ex-live}
==============================================================================================

Click this image to access the interactive code example for creating and sending a new invoice.

#### Figure:

Interactive Code [![Image and link to the interactive code example for creating a new
invoice.](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/invoicing/images/invoicing-services-create.png/jcr:content/renditions/original)](https://developer.example.com/api-reference-assets/index.md#invoicing_invoices_create-a-new-invoice "")

Create an Invoice without Sending it {#invoicing-services-create-intro}
=======================================================================

Creating a new invoice publishes a payable invoice. To share the created invoice with a customer, send the customer the redirect URL generated in the invoiceInformation.paymentLink response field.

**Itemized Invoices**
:
An invoice can display a single billed amount or list up to 30 billed items. To list the billed items in the invoice, include the items in the request using the line item array fields. An invoice with line items is known as an *itemized* invoice. For more information about how to include line items in your request, see [Including Line Items in an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-line-items.md "").

**Invoice Numbers**
:
You can assign a unique invoice number in the invoiceInformation.invoiceNumber request field. The invoice number is required for follow-on API requests and tracking. You should store the invoice number in your system so that you can optimally perform the follow-on requests. If you do not include a unique invoice number when creating an invoice, `Payment Gateway` generates a unique invoice number for you in the invoiceInformation.invoiceNumber response field. IMPORTANT You cannot update the invoice number after it is generated.

**Installment Payments**
:
Invoices can be paid in installment payments when these fields and values are included in the request. If an invoice is payable in installments, multiple customers can make payments towards the same invoice.

    invoiceInformation.allowPartialPayments
    :
        Set to `true`.


    orderInformation.amountDetails.minimumPartialAmount
    :
        Set to the minimum amount allowed for a partial payment.

**Partner Information**
:
If your merchant account is associated with a `Payment Gateway` partner, you can include your partner solution ID (PSID) in the request message for tracking and reporting purposes. To include your PSID, use the clientReferenceInformation.partner.solutionId request field and set its field value to your PSID.

**Alternative Methods to Create an Invoice**
:
To create **and send** a new invoice at the same time, see [Create and Send an Invoice Immediately](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-send-intro.md "").

    To create an invoice **draft** that is not payable or viewable to the customer, see [Create a Draft Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-draft-intro.md "").

Endpoint {#invoicing-services-create-intro_endpoint-create-invoice}
-------------------------------------------------------------------

Send an API POST request message to one of these endpoints:  
**Test:** `POST ``https://apitest.example.com``/invoicing/v2/invoices`  
**Production:** `POST ``https://api.example.com``/invoicing/v2/invoices`  
**India Production:** `POST https://api.in.example.com/invoicing/v2/invoices`

Successful Response
-------------------

A successfully created invoice is indicated by the `CREATED` status in the status response field. The response message also includes the newly created invoice's details for the new invoice.

Follow-On API Requests
----------------------

After creating an invoice, you can send these follow-on API requests.

**Send or Resend an Invoice**
:
After creating an invoice, you can send the invoice using the send invoice request. For more information, see [Send an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-send-intro.md "").

**Update an Invoice**
:
To update customer information or item details in an invoice, send an update invoice request. For more information, see [Update an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-update-intro.md "").

**Cancel an Invoice**
:
To cancel an invoice, send a cancel invoice request. For more information, see [Cancel an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-cancel-intro.md "").

**Get Invoice Details**
:
You can retrieve an invoice's details by sending a get invoice details request. For more information, see [Get Invoice Details](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-get-details-intro.md "").

**Get List of Invoices**
:
After creating multiple invoices, you might want to search for certain invoices. To retrieve a filtered list of invoices, send a get list of invoices request. For more information, see [Get a List of Invoices](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-get-list-intro.md "").

Required Fields for Creating an Invoice {#invoicing-services-create-req-fields}
===============================================================================

This section lists the required fields necessary to create these types of invoices:
* In-person invoice
* Email invoice
* Itemized email invoice

The invoice created using these fields and specified values is not immediately sent to the customer.

Required Fields for Creating an In-Person Invoice
-------------------------------------------------

invoiceInformation.deliveryMode
:
Set to `none`.

invoiceInformation.description
:

invoiceInformation.dueDate
:

invoiceInformation.sendImmediately
:
Set to `true`.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

Required Fields for Creating an Email Invoice {#invoicing-services-create-req-fields_customer-fields}
-----------------------------------------------------------------------------------------------------

customerInformation.email
:

customerInformation.name
:

invoiceInformation.deliveryMode
:
Set to `none`.

invoiceInformation.dueDate
:

invoiceInformation.sendImmediately
:
Set to `true`.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

Required Fields for Creating an Itemized Email Invoice {#invoicing-services-create-req-fields_line-item-fields}
---------------------------------------------------------------------------------------------------------------

customerInformation.email
:

customerInformation.name
:

invoiceInformation.deliveryMode
:
Set to `none`.

invoiceInformation.dueDate
:

invoiceInformation.sendImmediately
:
Set to `true`.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.lineItems\[\].productName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:
Include for each item listed in the invoice.

orderInformation.lineItems\[\].productSku
:
Include for each item listed in the invoice.

[orderInformation.lineItems\[\].quantity](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:
Include for each item listed in the invoice.

[orderInformation.lineItems\[\].totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
:
Include for each item listed in the invoice.

[orderInformation.lineItems\[\].unitPrice](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:
Include for each item listed in the invoice.

Example: Creating an Invoice {#invoicing-services-create-ex-rest}
=================================================================

Request

```
{
  "invoiceInformation": {
    "description": "Food",
    "dueDate": "2019-07-11",
    "sendImmediately": true,
    "deliveryMode": "none"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "2623.64",
      "currency": "USD"
    }
  }
}
```

Response to a Successful Request

```keyword
{
  "_links": {
    "self": {
      "href": "/v2/invoices/98761",
      "method": "GET"
    },
    "update": {
      "href": "/v2/invoices/98761",
      "method": "PUT"
    },
    "deliver": {
      "href": "/v2/invoices/98761/delivery",
      "method": "POST"
    },
    "cancel": {
      "href": "/v2/invoices/98761/cancelation",
      "method": "POST"
    }
  },
  "id": "98761",
  "submitTimeUtc": "2024-08-02T18:39:57.548314337Z",
  "status": "CREATED",
  "processingInformation": {
    "requestPhone": false,
    "requestShipping": false
  },
  "invoiceInformation": {
    "invoiceNumber": "98761",
    "description": "Food",
    "dueDate": "2019-07-11",
    "allowPartialPayments": false,
    "paymentLink": "https://businesscenter.example.com/ebc2/invoicing/payInvoice/wzvrzUssiXFLJ2RcJcmbuQEoHSrlcQudy9dL91Jxo8n4VcoRhNWRp8wvVDz8xtlD?version=v2.1",
    "deliveryMode": "None"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 2623.64,
      "currency": "USD",
      "balanceAmount": 2623.64
    }
  }
}
```

Request

```
{
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "tanya.lee@my-email.world"
  },
  "invoiceInformation": {
    "dueDate": "2019-07-11",
    "sendImmediately": true,
    "deliveryMode": "none"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 293.5,
      "currency": "USD"
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 12.05,
        "quantity": 20,
        "totalAmount": 241
      },
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 5.25,
        "quantity": 10,
        "totalAmount": 52.5
      }
    ]
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "self": {
      "href": "/v2/invoices/98766",
      "method": "GET"
    },
    "update": {
      "href": "/v2/invoices/98766",
      "method": "PUT"
    },
    "deliver": {
      "href": "/v2/invoices/98766/delivery",
      "method": "POST"
    },
    "cancel": {
      "href": "/v2/invoices/98766/cancelation",
      "method": "POST"
    }
  },
  "id": "98766",
  "submitTimeUtc": "2024-08-03T00:02:49.453695409Z",
  "status": "CREATED",
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "tanya.lee@my-email.world"
  },
  "processingInformation": {
    "requestPhone": false,
    "requestShipping": false
  },
  "invoiceInformation": {
    "invoiceNumber": "98766",
    "dueDate": "2019-07-11",
    "allowPartialPayments": false,
    "paymentLink": "/ebc2/invoicing/payInvoice/JBOA7CQeoSFuUluwLqw2c6n8rf0KCO0cgJz19uQmxO9rF5tT8FdNGRTL9OHapjlr?version=v2.1",
    "deliveryMode": "None"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 293.5,
      "currency": "USD",
      "balanceAmount": 293.5
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 12.05,
        "quantity": 20,
        "totalAmount": 241
      },
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 5.25,
        "quantity": 10,
        "totalAmount": 52.5
      }
    ]
  }
}
```

REST Interactive Example: Create a New Invoice {#invoicing-services-create-ex-live}
===================================================================================

Click this image to access the interactive code example for creating a new invoice.

#### Figure:

Interactive Code [![Image and link to the interactive code example for creating a new
invoice.](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/invoicing/images/invoicing-services-create.png/jcr:content/renditions/original)](https://developer.example.com/api-reference-assets/index.md#invoicing_invoices_create-a-new-invoice "")

Get a List of Invoices {#invoicing-services-get-list-intro}
===========================================================

You can retrieve a list of your invoices by sending a get invoice list request. To filter the list results, you can add an optional string of query parameters to the endpoint. Filtering list results can help you retrieve specific invoices faster.  
You can filter invoices by:

* Number of invoices retrieved
* Order of invoices
* Status

Endpoints
---------

Send your API request to one of these endpoints:  
**Test:** `GET ``https://apitest.example.com``/invoicing/v2/invoices`  
**Production:** `GET ``https://api.example.com``/invoicing/v2/invoices`  
**India Production:** `GET https://api.in.example.com/invoicing/v2/invoices`

Generate an Endpoint with Query Parameters {#invoicing-services-get-list-req-fields}
====================================================================================

You can filter your search results by appending an optional string of query parameters to the endpoint. A query parameter is also known as a *query-string*.  
Begin each string with a question mark (`?`) to designate the start of the query parameters, and include an ampersand (`&`) at the beginning of each consecutive query parameter.  
Use this format for appending a string of query parameters as name-value pairs:  
`?name1=value&name2=value&nameN=value`  
These are the query parameters to filter the retrieved list results:

| Query Parameter |                                                                                                                                                                                                                                                     Description                                                                                                                                                                                                                                                      |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| offset          | The page offset number. This determines the order in which the invoices are retrieved, beginning with the consecutive number from the string value. For example, an offset of `3` results in a filtered list that begins with the fourth listed invoice. Set to a whole number.                                                                                                                                                                                                                                      |
| limit           | The maximum number of items being retrieved. Set to a whole number.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| status          | The status of the invoice. Set to one of these possible values: * `CANCELED` * `CREATED` * `DRAFT` * `PAID` * `PARTIAL` * `PENDING`: The customer has initiated a payment for an invoice that is in the `CREATED`, `SENT`, or `PARTIAL` status. The invoice can no longer be edited, and the customer can no longer initiate an payment in order to avoid a double payment. If the invoice payment requires a fraud review, the invoice will remain in the `PENDING` status until you approve or reject it. * `SENT` |
[Query Parameters]

In this example, up to 100 draft invoices are retrieved beginning with the fourth listed invoice:

```keyword
GET https://apitest.example.com/invoicing/v2/invoices?offset=3&limit=100&status=DRAFT
```

Example: Get a List of Invoices {#invoicing-services-get-list-ex-rest}
======================================================================

Endpoint with Optional Query Parameters

```keyword
GET https://apitest.example.com/invoicing/v2/invoices?offset=0&limit=5&status=DRAFT
```

Request

```
{}
```

Response to a Successful Request

```
{
  "_links": {
    "self": {
      "href": "/v2/invoices/?offset=0&limit=5",
      "method": "GET"
    },
    "next": {
      "href": "/v2/invoices/?offset=5&limit=5",
      "method": "GET"
    }
  },
  "submitTimeUtc": "2024-07-24T18:44:11.469054445Z",
  "totalInvoices": 38449,
  "invoices": [
    {
      "_links": {
        "self": {
          "href": "/v2/invoices/2670",
          "method": "GET"
        },
        "update": {
          "href": "/v2/invoices/2670",
          "method": "PUT"
        },
        "deliver": {
          "href": "/v2/invoices/2670/delivery",
          "method": "POST"
        },
        "cancel": {
          "href": "/v2/invoices/2670/cancelation",
          "method": "POST"
        }
      },
      "id": "2670",
      "status": "SENT",
      "customerInformation": {
        "name": "Tanya Lee"
      },
      "invoiceInformation": {
        "dueDate": "2019-07-11",
        "paymentLink": "https://developer.example.com/ebc2/invoicing/payInvoice/W447tdnINi5t5wu6QA0KUE2HYWY2rQQ0zXL5b5z6M50w4Ea9FFlcYrEmp09pFlzl?version=v2.1"
      },
      "orderInformation": {
        "amountDetails": {
          "totalAmount": 247.86,
          "currency": "USD"
        }
      }
    },
    {
      "_links": {
        "self": {
          "href": "/v2/invoices/2669",
          "method": "GET"
        },
        "update": {
          "href": "/v2/invoices/2669",
          "method": "PUT"
        },
        "deliver": {
          "href": "/v2/invoices/2669/delivery",
          "method": "POST"
        },
        "cancel": {
          "href": "/v2/invoices/2669/cancelation",
          "method": "POST"
        }
      },
      "id": "2669",
      "status": "DRAFT",
      "customerInformation": {
        "name": "Tanya Lee"
      },
      "invoiceInformation": {
        "dueDate": "2019-07-11"
      },
      "orderInformation": {
        "amountDetails": {
          "totalAmount": 247.86,
          "currency": "USD"
        }
      }
    },
    {
      "_links": {
        "self": {
          "href": "/v2/invoices/2668",
          "method": "GET"
        },
        "update": {
          "href": "/v2/invoices/2668",
          "method": "PUT"
        },
        "deliver": {
          "href": "/v2/invoices/2668/delivery",
          "method": "POST"
        },
        "cancel": {
          "href": "/v2/invoices/2668/cancelation",
          "method": "POST"
        }
      },
      "id": "2668",
      "status": "DRAFT",
      "customerInformation": {
        "name": "Tanya Lee"
      },
      "invoiceInformation": {
        "dueDate": "2019-07-11"
      },
      "orderInformation": {
        "amountDetails": {
          "totalAmount": 2623.64,
          "currency": "USD"
        }
      }
    },
    {
      "_links": {
        "self": {
          "href": "/v2/invoices/2667",
          "method": "GET"
        },
        "update": {
          "href": "/v2/invoices/2667",
          "method": "PUT"
        },
        "deliver": {
          "href": "/v2/invoices/2667/delivery",
          "method": "POST"
        },
        "cancel": {
          "href": "/v2/invoices/2667/cancelation",
          "method": "POST"
        }
      },
      "id": "2667",
      "status": "DRAFT",
      "customerInformation": {
        "name": "Tanya Lee"
      },
      "invoiceInformation": {
        "dueDate": "2019-07-11"
      },
      "orderInformation": {
        "amountDetails": {
          "totalAmount": 2623.64,
          "currency": "USD"
        }
      }
    },
    {
      "_links": {
        "self": {
          "href": "/v2/invoices/2666",
          "method": "GET"
        },
        "update": {
          "href": "/v2/invoices/2666",
          "method": "PUT"
        },
        "deliver": {
          "href": "/v2/invoices/2666/delivery",
          "method": "POST"
        },
        "cancel": {
          "href": "/v2/invoices/2666/cancelation",
          "method": "POST"
        }
      },
      "id": "2666",
      "status": "CREATED",
      "customerInformation": {
        "name": "Tanya Lee"
      },
      "invoiceInformation": {
        "dueDate": "2019-07-11",
        "paymentLink": "https://developer.example.com/ebc2/invoicing/payInvoice/i0wUKECHxctWAjRPKFgyEtZiSWxwgtZljBVSrxfFjbBVGgLpET8ROvOPdnhwCJTC?version=v2.1"
      },
      "orderInformation": {
        "amountDetails": {
          "totalAmount": 2623.64,
          "currency": "USD"
        }
      }
    }
  ]
}
```

REST Interactive Example: Get a List of Invoices {#invoicing-services-get-list-ex-live}
=======================================================================================

Click this image to access the interactive code example for retrieving a list of invoices.

#### Figure:

Interactive Code [![Image and link to the interactive code example for creating a new
invoice.](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/invoicing/images/invoicing-services-create.png/jcr:content/renditions/original)](https://developer.example.com/api-reference-assets/index.md#invoicing_invoices_get-a-list-of-invoices "")

Get Invoice Details {#invoicing-services-get-details-intro}
===========================================================

Retrieve an invoice's details to check its current status and payment history. Retrieving an invoice's details requires the unique invoice number assigned when the invoice was created.  
If you need more information about the payment history, you can also use the transaction details API. For more information, see the [Transaction Details API](https://developer.example.com/docs/gateway/en-us/txn-search/developer/all/rest/txn-search/txn-details-intro.md "") section in the *Transaction Search and Details API Developer Guide*.

Endpoints
---------

Send your API request to one of these endpoints:  
**Test:** `GET https://``https://apitest.example.com``/invoicing/v2/invoices/`*{id}*  
**Production:** `GET https://``https://api.example.com``/invoicing/v2/invoices/`*{id}*  
**India Production:** `GET https://api.in.example.com/invoicing/v2/invoices/`*{id}*  
The *`{id}`* is the invoice number from the invoice creation response message.

Successful Response
-------------------

A response contains this invoice information:

|           Response Field           |                                                                                                                                                                                                                                                                                                                                                                                Description                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| submitTimeUtc                      | The date and time that the invoice was sent, in UTC format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| status                             | The invoice status. Possible values: * `CANCELED`: The invoice is cancelled. * `CREATED`: The invoice is created. * `DRAFT`: The invoice is drafted and not published. * `PAID`: The invoice is fully paid. The customer is notified that the payment is successful. * `PARTIAL`: The invoice is partially paid. * `PENDING`: Fraud management is reviewing the invoice and you must accept or reject the payment. The customer is also notified that the payment is processing. When you accept the payment, the invoice updates to the `PAID` status. If you reject the payment, the invoice updates to the `SENT` status. > IMPORTANT This status is only retrievable for merchants with fraud management enabled. * `SENT`: The invoice is delivered to the customer. |
| customerInformation (field object) | The customer's information, such as name and email.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| invoiceInformation (field object)  | The `paymentLink` field contains the direct URL to the invoice.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| orderInformation (field object)    | The itemized amount charged for the billed goods and services.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| invoiceHistory (field object)      | An array of invoice status changes and the date and time stamp of each invoice status changed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
[Response Fields to a Successful Request]

Example: Get Invoice Details {#invoicing-services-get-details-ex-rest}
======================================================================

Endpoint with an Invoice Number

```keyword
GET https://https://api.example.com/invoicing/v2/invoices/2670
```

Request

```
{}
```

Response to a Successful Request

```keyword
{
  "_links": {
    "self": {
      "href": "/v2/invoices/2670",
      "method": "GET"
    },
    "update": {
      "href": "/v2/invoices/2670",
      "method": "PUT"
    },
    "deliver": {
      "href": "/v2/invoices/2670/delivery",
      "method": "POST"
    },
    "cancel": {
      "href": "/v2/invoices/2670/cancelation",
      "method": "POST"
    }
  },
  "id": "2670",
  "submitTimeUtc": "2024-07-24T18:36:18.863175539Z",
  "status": "SENT",
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "tanya.lee@my-email.world"
  },
  "processingInformation": {
    "requestPhone": false,
    "requestShipping": false
  },
  "invoiceInformation": {
    "invoiceNumber": "2670",
    "dueDate": "2019-07-11",
    "allowPartialPayments": false,
    "paymentLink": "https://businesscenter.example.com/ebc2/invoicing/payInvoice/W447tdnINi5t5wu6QA0KUE2HYWY2rQQ0zXL5b5z6M50w4Ea9FFlcYrEmp09pFlzl?version=v2.1",
    "deliveryMode": "Email"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 247.86,
      "currency": "USD",
      "balanceAmount": 247.86
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 12.05,
        "quantity": 20,
        "totalAmount": 247.86
      }
    ]
  },
  "invoiceHistory": [
    {
      "event": "SEND",
      "date": "2024-07-24T18:35:23.320Z"
    },
    {
      "event": "DRAFT",
      "date": "2024-07-24T18:35:22.960Z"
    }
  ]
}
```

REST Interactive Example: Get Invoice Details {#invoicing-services-get-details-ex-live}
=======================================================================================

Click this image to access the interactive code example for retrieving invoice details.

#### Figure:

Interactive Code [![Image and link to the interactive code example for creating a new
invoice.](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/invoicing/images/invoicing-services-create.png/jcr:content/renditions/original)](https://developer.example.com/api-reference-assets/index.md#invoicing_invoices_get-invoice-details "")

Update an Invoice {#invoicing-services-update-intro}
====================================================

You can update an invoice if no payment has been made. Include all of the fields that were contained in the original request message in the update request. If you do not include a field that was in the original request message, the field information associated with it will be removed in the updated invoice.  
If you update the customer's email in the customerInformation.email request field, the generated redirect URL in the invoiceInformation.paymentLink response field changes and the previous URL becomes invalid. You can either share the new redirect URL with the customer, or resend the updated invoice using the send invoice request. For more information about how to resend an invoice, see [Send an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-send-intro.md "").

Itemized Invoices
:
An invoice can display a single billed amount or list up to 30 billed items. To list the billed items in the invoice, include the items in the request using the line item array fields. An invoice with line items is known as an *itemized* invoice. For more information about how to include line items in your request, see [Including Line Items in an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-line-items.md "").

**Installment Payments**
:
Invoices can be paid in installment payments when these fields and values are included in the request. If an invoice is payable in installments, multiple customers can make payments towards the same invoice.

    invoiceInformation.allowPartialPayments
    :
        Set to `true`.


    orderInformation.amountDetails.minimumPartialAmount
    :
        Set to the minimum amount allowed for a partial payment.

**Partner Information**
:
If your merchant account is associated with a `Payment Gateway` partner, you can include your partner solution ID (PSID) in the request message for tracking and reporting purposes. To include your PSID, use the clientReferenceInformation.partner.solutionId request field and set its field value to your PSID.

Endpoints
---------

Send your API request message to one of these endpoints:  
**Test:** `PUT ``https://apitest.example.com``/invoicing/v2/invoices/`*{id}*  
**Production:** `PUT ``https://api.example.com``/invoicing/v2/invoices/`*{id}*  
**India Production:** `PUT https://api.in.example.com/invoicing/v2/invoices/`*{id}*  
The *`{id}`* is the invoice number from the response to the create invoice request.

Required Fields for Updating an Invoice {#invoicing-services-update-req-fields}
===============================================================================

Include these fields and any additional fields contained in the original request to create the invoice.

invoiceInformation.description
:
This field becomes optional if the line item fields are present in the request message.

invoiceInformation.dueDate
:

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

orderInformation.lineItems\[\].productSku
:

Optional Fields for Updating an Invoice {#invoicing-services-update-opt-fields}
===============================================================================

Include all of the fields contained in the original request. If you do not include a field that was in the original request, the field information associated with it is removed in the updated invoice.

[clientReferenceInformation.partner.solutionId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
Set to your partner solution ID (PSID).

[clientReferenceInformation.partner.developerId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
Set to your developer ID.

customerInformation.company.name
:

customerInformation.email
:

customerInformation.merchantCustomerId
:

customerInformation.name
:

invoiceInformation.allowPartialPayments
:

invoiceInformation.deliveryMode
:

invoiceInformation.description
:
This field is optional when either of these conditions is met:

    * The invoiceInformation.deliveryMode request field is set to `email`.
    * The line item fields are present in the request message.

invoiceInformation.expirationDate
:
Set to the expiration date. Format: `DD-MM-YYYY`.
:
The invoice expires on this date at 00:00 GMT.

invoiceInformation.invoiceNumber
:
Set to a unique number to create an invoice number.

    If you do not include this field and a unique value, the invoicing API automatically generates an invoice number for the new invoice.

    > IMPORTANT You cannot update this invoice number after sending the API request.

invoiceInformation.sendImmediately
:

[orderInformation.amountDetails.discountAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-discount-amount.md "")
:

orderInformation.amountDetails.discountPercent
:

orderInformation.amountDetails.freight.amount
:

orderInformation.amountDetails.freight.taxable
:

orderInformation.amountDetails.freight.taxRate
:

orderInformation.amountDetails.minimumPartialAmount
:

orderInformation.amountDetails.subAmount
:

orderInformation.amountDetails.taxDetails.amount
:

orderInformation.amountDetails.taxDetails.rate
:

orderInformation.amountDetails.taxDetails.type
:

[orderInformation.lineItems\[\].discountAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-discount-amount.md "")
:

orderInformation.lineItems\[\].discountRate
:

[orderInformation.lineItems\[\].taxAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-amount-request.md "")
:

[orderInformation.lineItems\[\].taxRate](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-rate.md "")
:

[orderInformation.lineItems\[\].productName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

orderInformation.lineItems\[\].productSku
:

[orderInformation.lineItems\[\].quantity](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

[orderInformation.lineItems\[\].totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

Example: Updating an Invoice {#invoicing-services-update-ex-rest}
=================================================================

Endpoint to Update an Invoice

```keyword
https://api.example.com/invoicing/v2/invoices/98761
```

Request

```
{
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "tanya.lee@my-email.world"
  },
  "invoiceInformation": {
    "dueDate": "2019-07-15"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "2623.64",
      "currency": "USD"
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "quantity": "20",
        "unitPrice": "12.05",
        "totalAmount": "247.86"
      }
    ]
  }
}
```

Response to a Successful Request

```keyword
{
  "_links": {
    "self": {
      "href": "/v2/invoices/2670",
      "method": "GET"
    },
    "update": {
      "href": "/v2/invoices/2670",
      "method": "PUT"
    },
    "deliver": {
      "href": "/v2/invoices/2670/delivery",
      "method": "POST"
    },
    "cancel": {
      "href": "/v2/invoices/2670/cancelation",
      "method": "POST"
    }
  },
  "id": "2670",
  "submitTimeUtc": "2024-07-24T19:40:37.289869220Z",
  "status": "SENT",
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "tanya.lee@my-email.world"
  },
  "processingInformation": {
    "requestPhone": false,
    "requestShipping": false
  },
  "invoiceInformation": {
    "invoiceNumber": "2670",
    "dueDate": "2019-07-15",
    "allowPartialPayments": false,
    "paymentLink": "https://businesscenter.example.com/ebc2/invoicing/payInvoice/W447tdnINi5t5wu6QA0KUE2HYWY2rQQ0zXL5b5z6M50w4Ea9FFlcYrEmp09pFlzl?version=v2.1",
    "deliveryMode": "Email"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 2623.64,
      "currency": "USD",
      "balanceAmount": 2623.64
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 12.05,
        "quantity": 20,
        "totalAmount": 247.86
      }
    ]
  }
}
```

Request with Optional Fields

```
{
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "tanya.lee@my-email.world",
    "merchantCustomerId": "1234",
    "company": {
      "name": "ABC"
    }
  },
  "invoiceInformation": {
    "description": "This is an updated test invoice",
    "dueDate": "2019-07-15",
    "allowPartialPayments": true,
    "deliveryMode": "none"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "2623.64",
      "currency": "USD",
      "discountAmount": "126.08",
      "discountPercent": 5,
      "subAmount": 2749.72,
      "minimumPartialAmount": 200,
      "taxDetails": {
        "type": "State Tax",
        "amount": "208.00",
        "rate": "8.25"
      },
      "freight": {
        "amount": "20.00",
        "taxable": true,
        "taxRate": "0.01"
      }
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "quantity": "20",
        "unitPrice": "12.05",
        "discountAmount": "13.04",
        "discountRate": "0.0",
        "taxAmount": "0.0",
        "taxRate": "0.0",
        "totalAmount": "247.86"
      }
    ]
  }
}
```

Response to a Successful Request with Optional Fields

```keyword
{
  "_links": {
    "self": {
      "href": "/v2/invoices/2670",
      "method": "GET"
    },
    "update": {
      "href": "/v2/invoices/2670",
      "method": "PUT"
    },
    "deliver": {
      "href": "/v2/invoices/2670/delivery",
      "method": "POST"
    },
    "cancel": {
      "href": "/v2/invoices/2670/cancelation",
      "method": "POST"
    }
  },
  "id": "2670",
  "submitTimeUtc": "2024-07-24T19:46:18.914132825Z",
  "status": "SENT",
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "tanya.lee@my-email.world",
    "merchantCustomerId": "1234",
    "company": {
      "name": "ABC"
    }
  },
  "processingInformation": {
    "requestPhone": false,
    "requestShipping": false
  },
  "invoiceInformation": {
    "invoiceNumber": "2670",
    "description": "This is an updated test invoice",
    "dueDate": "2019-07-15",
    "allowPartialPayments": true,
    "paymentLink": "https://businesscenter.example.com/ebc2/invoicing/payInvoice/W447tdnINi5t5wu6QA0KUE2HYWY2rQQ0zXL5b5z6M50w4Ea9FFlcYrEmp09pFlzl?version=v2.1",
    "deliveryMode": "None"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 2623.64,
      "currency": "USD",
      "balanceAmount": 2623.64,
      "discountAmount": 126.08,
      "discountPercent": 5,
      "subAmount": 2749.72,
      "minimumPartialAmount": 200,
      "taxDetails": {
        "type": "State Tax",
        "amount": 208,
        "rate": 8.25
      },
      "freight": {
        "amount": 20,
        "taxable": true,
        "taxRate": 0.01
      }
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 12.05,
        "quantity": 20,
        "discountAmount": 13.04,
        "taxAmount": 0,
        "taxRate": 0,
        "totalAmount": 247.86
      }
    ]
  }
}
```

REST Interactive Example: Update an Invoice {#invoicing-services-update-ex-live}
================================================================================

Click this image to access the interactive code example for updating an invoice.

#### Figure:

Interactive Code [![Image and link to the interactive code example for creating a new
invoice.](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/invoicing/images/invoicing-services-create.png/jcr:content/renditions/original)](https://developer.example.com/api-reference-assets/index.md#invoicing_invoices_update-an-invoice "")

Send an Invoice {#invoicing-services-send-intro}
================================================

If you created an invoice that was not immediately delivered to the customer, you can use the *send an invoice* request to have `Payment Gateway` email the invoice to the customer. You can also use this request to resend an updated, unpaid, or a partially paid invoice. Fully paid or cancelled invoices cannot be resent.

Endpoints
---------

Send your API request message to one of these endpoints. The *`{id}`* is the invoice number from the response to the create invoice request.  
**Test:** `POST ``https://apitest.example.com``/invoicing/v2/invoices/`*{id}*`/delivery`  
**Production:** `POST ``https://api.example.com``/invoicing/v2/invoices/`*{id}*`/delivery`  
**India Production:** `POST https://api.in.example.com/invoicing/v2/invoices/`*{id}*`/delivery`

Successful Response
-------------------

A successful request is indicated by an updated submit time in the submitTimeUtc response field.  
The invoice status in the status response field might update to a new status depending on the field value that was set in the invoiceInformation.deliveryMode request field when the invoice was initially created.  
Use this table to determine how an invoice's status will change when you send or resend it. The Initial Status column indicates the invoice's initial status, which was in the status response field. The Delivery Method column indicates whether or not the customer was immediately emailed when the invoice was created, which was determined by the invoiceInformation.deliveryMode field value. The Notification Description column explains what happens to an invoice when you submit a send invoice request, which is the result of the invoice's initial status and whether or not it was emailed to the customer. The New Status column indicates the new status of the invoice after you submit a send invoice request, which can be found in the status response field.

| Initial Status | Delivery Method |                                                                                        Notification Description                                                                                         | New Status |
|----------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| `DRAFT`        | `email`         | An invoice email is sent to the customer.                                                                                                                                                               | `SENT`     |
| `DRAFT`        | `none`          | The customer is **not** sent an invoice email. To share the newly created invoice with the customer, send the customer the redirect URL generated in the invoiceInformation.paymentLink response field. | `CREATED`  |
| `CREATED`      | `email`         | An invoice email is sent to the customer.                                                                                                                                                               | `SENT`     |
| `SENT`         | `email`         | An invoice email is resent to the customer.                                                                                                                                                             | `SENT`     |
| `PARTIAL`      | `email`         | An invoice email is sent to the customer.                                                                                                                                                               | `PARTIAL`  |
[New Invoice Statuses]

Example: Send an Invoice {#invoicing-services-send-ex-rest}
===========================================================

Endpoint with an Invoice Number

```keyword
https://api.example.com/invoicing/v2/invoices/2675/delivery
```

Request

```
{}
```

Response to a Successful Request

```
{
  "_links": {
    "self": {
      "href": "/v2/invoices/2675",
      "method": "GET"
    },
    "update": {
      "href": "/v2/invoices/2675",
      "method": "PUT"
    },
    "deliver": {
      "href": "/v2/invoices/2675/delivery",
      "method": "POST"
    },
    "cancel": {
      "href": "/v2/invoices/2675/cancelation",
      "method": "POST"
    }
  },
  "id": "2675",
  "submitTimeUtc": "2024-07-24T19:54:06.665139633Z",
  "status": "CREATED",
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "tanya.lee@my-email.world",
    "merchantCustomerId": "1234",
    "company": {
      "name": "ABC"
    }
  },
  "processingInformation": {
    "requestPhone": false,
    "requestShipping": false
  },
  "invoiceInformation": {
    "invoiceNumber": "2675",
    "description": "This is a test invoice",
    "dueDate": "2019-07-11",
    "allowPartialPayments": true,
    "paymentLink": "https://developer.example.com/ebc2/invoicing/payInvoice/9fO0CogtSMJiDO3VKR4GYijUSYHtKV4kjS6u0ENZpY9iq2pkdKJmwTTSlGCDOVHJ?version=v2.1",
    "deliveryMode": "None"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 2623.64,
      "currency": "USD",
      "balanceAmount": 2623.64,
      "discountAmount": 126.08,
      "discountPercent": 5,
      "subAmount": 2749.72,
      "minimumPartialAmount": 20,
      "taxDetails": {
        "type": "State Tax",
        "amount": 208,
        "rate": 8.25
      },
      "freight": {
        "amount": 20,
        "taxable": true
      }
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 12.05,
        "quantity": 20,
        "discountAmount": 13.04,
        "taxAmount": 0,
        "taxRate": 0,
        "totalAmount": 247.86
      }
    ]
  }
}
```

REST Interactive Example: Send an Invoice {#invoicing-services-send-ex-live}
============================================================================

Click this image to access the interactive code example for sending or resending an invoice.

#### Figure:

Interactive Code [![Image and link to the interactive code example for creating a new
invoice.](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/invoicing/images/invoicing-services-create.png/jcr:content/renditions/original)](https://developer.example.com/api-reference-assets/index.md#invoicing_invoices_send-an-invoice "")

Cancel an Invoice {#invoicing-services-cancel-intro}
====================================================

You can cancel an unpaid invoice. Partially paid or fully paid invoices cannot be cancelled.  
Cancelling an invoice requires the invoice number that was assigned when the invoice was created.

Endpoints
---------

Send your API request message to one of these endpoints:  
**Production:** `POST ``https://api.example.com``/invoicing/v2/invoices/`*{id}*`/cancelation`  
**Test:** `POST ``https://apitest.example.com``/invoicing/v2/invoices/`*{id}*`/cancelation`  
**India Production:** `POST https://api.in.example.com/invoicing/v2/invoices/`*{id}*`/cancelation`  
The *`{id}`* is the invoice number from the response to the create invoice request.

Successful Response
-------------------

A successful request is indicated by the `canceled` status in the status response field and an updated time in the submitTimeUtc response field.

Example: Cancelling an Invoice {#invoicing-services-cancel-ex-rest}
===================================================================

Endpoint with an Invoice Number

```keyword
https://apitest.example.com/invoicing/v2/invoices/2675/cancelation
```

Request

```
{}
```

Response to a Successful Request

```
{
  "_links": {
    "self": {
      "href": "/v2/invoices/2675",
      "method": "GET"
    }
  },
  "id": "2675",
  "submitTimeUtc": "2024-07-24T19:56:06.410896558Z",
  "status": "CANCELED",
  "customerInformation": {
    "name": "Tanya Lee",
    "email": "tanya.lee@my-email.world",
    "merchantCustomerId": "1234",
    "company": {
      "name": "ABC"
    }
  },
  "processingInformation": {
    "requestPhone": false,
    "requestShipping": false
  },
  "invoiceInformation": {
    "invoiceNumber": "2675",
    "description": "This is a test invoice",
    "dueDate": "2019-07-11",
    "allowPartialPayments": true,
    "deliveryMode": "None"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 2623.64,
      "currency": "USD",
      "balanceAmount": 2623.64,
      "discountAmount": 126.08,
      "discountPercent": 5,
      "subAmount": 2749.72,
      "minimumPartialAmount": 20,
      "taxDetails": {
        "type": "State Tax",
        "amount": 208,
        "rate": 8.25
      },
      "freight": {
        "amount": 20,
        "taxable": true
      }
    },
    "lineItems": [
      {
        "productSku": "P653727383",
        "productName": "First line item's name",
        "unitPrice": 12.05,
        "quantity": 20,
        "discountAmount": 13.04,
        "taxAmount": 0,
        "taxRate": 0,
        "totalAmount": 247.86
      }
    ]
  }
}
```

REST Interactive Example: Cancel an Invoice {#invoicing-services-cancel-ex-live}
================================================================================

Click this image to access the interactive code example for cancelling an invoice.

#### Figure:

Interactive Code [![Image and link to the interactive code example for creating a new
invoice.](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/invoicing/images/invoicing-services-create.png/jcr:content/renditions/original)](https://developer.example.com/api-reference-assets/index.md#invoicing_invoices_cancel-an-invoice "")

Including Line Items in an Invoice {#invoicing-services-line-items}
===================================================================

You can itemize invoices by including the line item fields in your request when you create, draft, and update an invoice.  
*Line items* are used to include information about your customers' purchases. Information can include product name, quantity, and price.  
Line items are included in a request in the lineItem\[\] array request field.  
You can include the line item fields in these requests:

* [Create a Draft Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-draft-intro.md "")
* [Create a Deliverable Draft Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-draft-dlvr-intro.md "")
* [Create and Send an Invoice Immediately](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-send-intro.md "")
* [Create an Invoice without Sending it](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-create-intro.md "")
* [Update an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-update-intro.md "")

These fields are required for each line item in your request:

[orderInformation.lineItems\[\].productName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

orderInformation.lineItems\[\].productSku
:

[orderInformation.lineItems\[\].quantity](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

[orderInformation.lineItems\[\].totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

These fields are optional for each line item in your request:

[orderInformation.lineItems\[\].discountAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-discount-amount.md "")
:

orderInformation.lineItems\[\].discountRate
:

[orderInformation.lineItems\[\].taxAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-amount-request.md "")
:

[orderInformation.lineItems\[\].taxRate](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-rate.md "")
:

Example: Including Line Items  
This excerpt from a request shows three valid line items.

```
{ 
  "orderInformation": {
    "lineItems": [
      {
        "productSku": "ABCD1234",
        "productName": "First line item's name",
        "quantity": "20",
        "unitPrice": "12.05",
        "discountAmount": "13.04",
        "taxAmount": "0.0",
        "taxRate": "0.0",
        "totalAmount": "247.86"
      },
      {
        "productSku": "EFGH5678",
        "productName": "Second line item's name",
        "quantity": "20",
        "unitPrice": "12.05",
        "discountAmount": "13.04",
        "taxAmount": "0.0",
        "taxRate": "0.0",
        "totalAmount": "247.86"
      },
      {
        "productSku": "IJKL9999",
        "productName": "Third line item's name",
        "quantity": "20",
        "unitPrice": "12.05",
        "discountAmount": "13.04",
        "taxAmount": "0.0",
        "taxRate": "0.0",
        "totalAmount": "247.86"
      }
    ]
  }
}
```

Create an Amount Only Invoice {#invoicing-services-create-draft-intro}
======================================================================

Create an amount only invoice to send to a customer without listing each line item. An amount only invoice includes the total amount for the invoice as well as branding, checkout, email, security, and custom label settings. An existing invoice cannot be changed into an amount only invoice, but you can cancel the invoice and create a new one.

**Invoice Numbers**
:
You can assign a unique invoice number in the invoiceInformation.invoiceNumber request field. The invoice number is required for follow-on API requests and tracking. You should store the invoice number in your system so that you can optimally perform the follow-on requests. If you do not include a unique invoice number when creating an invoice, `Payment Gateway` generates a unique invoice number for you in the invoiceInformation.invoiceNumber response field. IMPORTANT You cannot update the invoice number after it is generated.

**Partner Information**
:
If your merchant account is associated with a `Payment Gateway` partner, you can include your partner solution ID (PSID) in the request message for tracking and reporting purposes. To include your PSID, use the clientReferenceInformation.partner.solutionId request field and set its field value to your PSID.

Endpoint
--------

Send an API POST request message to one of these endpoints:  
**Test:** `POST ``https://apitest.example.com``/invoicing/v2/invoices`  
**Production:** `POST ``https://api.example.com``/invoicing/v2/invoices`  
**India Production:** `POST https://api.in.example.com/invoicing/v2/invoices`

Response to a Successful Request
--------------------------------

A successfully drafted invoice is indicated by the status in the status response field.  
The redirect URL generated in the invoiceInformation.paymentLink response field is usable only by you and not the customer.  
Additional invoice details are included in the response message for you to review.

Follow-On API Requests
----------------------

After successfully drafting an invoice, you can send these follow-on API requests.

**Send an Invoice**
:
After drafting an invoice, you can publish and send an invoice using the send invoice request. For more information, see [Send an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-send-intro.md "").

**Update an Invoice**
:
To update customer information or item details in an already drafted invoice, send an update invoice request. For more information, see [Update an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-update-intro.md "").

**Cancel an Invoice**
:
To cancel a drafted invoice, send the a cancel invoice request. For more information, see [Cancel an Invoice](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-cancel-intro.md "").

**Get Invoice Details**
:
To retrieve a drafted invoice's details, send a get invoice details request. For more information, see [Get Invoice Details](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro/invoicing-services-get-details-intro.md "").

Required Fields for Drafting an Amount Only Invoice {#invoicing-services-create-draft-req-fields}
=================================================================================================

This section lists the required fields necessary to create an amount only invoice.
The invoice created using these fields and specified values is not immediately sent to the customer.

Required Fields for Drafting an Email Invoice {#invoicing-services-create-draft-req-fields_customer-fields}
-----------------------------------------------------------------------------------------------------------

customerInformation.email
:

customerInformation.name
:

invoiceInformation.deliveryMode
:
Set to `email` when drafting a deliverable invoice.

invoiceInformation.description
:
This field becomes optional when line item fields are present in the request message.

invoiceInformation.dueDate
:

invoiceInformation.sendImmediately
:
Set to `false`.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

Optional Fields for Amount Only Invoice Creation {#invoicing-services-create-opt-fields}
========================================================================================

You can include these optional fields when sending amount only invoice requests:

[clientReferenceInformation.partner.developerId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
Set to your developer ID.

[clientReferenceInformation.partner.solutionId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
Set to your partner solution ID (PSID).

customerInformation.company.name
:

customerInformation.merchantCustomerId
:

customerInformation.name
:

invoiceInformation.deliveryMode
:

invoiceInformation.expirationDate
:
Set to the expiration date. Format: `DD-MM-YYYY`.
:
The invoice expires on this date at 00:00 GMT.

invoiceInformation.invoiceNumber
:
Set to a unique number to create an invoice number.

    If you do not include this field and a unique value, the invoicing API automatically generates an invoice number for the new invoice.

    > IMPORTANT You cannot update this invoice number after sending the API request.

merchantDefinedFieldValues.definition.id\[\].value
:

orderInformation.amountDetails.subAmount
:

Example: Drafting an Amount Only Invoice {#invoicing-services-create-draft-done-ex-rest}
========================================================================================

Request

```
{ 
  "clientReferenceInformation": { 
    "partner": { 
      "developerId": "3435", 
      "solutionId": "83745" 
    } 
  }, 
  "customerInformation": { 
    "name": "Tanya Lee", 
    "email": "tanya.lee@my-email.world" 
  }, 
  "processingInformation": { 
    "requestPhone": false, 
    "requestShipping": false 
  }, 
  "invoiceInformation": { 
    "description": "This is a test invoice", 
    "dueDate": "2019-07-11", 
    "expirationDate": "2028-08-11", 
    "sendImmediately": true, 
    "deliveryMode": "email" 
  }, 
  "orderInformation": { 
    "amountDetails": { 
      "totalAmount": "2623.64", 
      "currency": "USD", 
      "subAmount": "2749.72" 
    } 
  } 
} 
```

Response to a Successful Request

```
{ 
  "_links": { 
    "self": { 
      "href": "/v2/invoices/15", 
      "method": "GET" 
    }, 
    "update": { 
      "href": "/v2/invoices/15", 
      "method": "PUT" 
    }, 
    "deliver": { 
      "href": "/v2/invoices/15/delivery", 
      "method": "POST" 
    }, 
    "cancel": { 
      "href": "/v2/invoices/15/cancelation", 
      "method": "POST" 
    } 
  }, 
  "id": "15", 
  "submitTimeUtc": "2026-04-02T13:11:12.109758358Z", 
  "status": "SENT", 
  "customerInformation": { 
    "name": "Tanya Lee", 
    "email": "tanya.lee@my-email.world" 
  }, 
  "processingInformation": { 
    "requestPhone": false, 
    "requestShipping": false 
  }, 
  "invoiceInformation": { 
    "invoiceNumber": "15", 
    "description": "This is a test invoice", 
    "dueDate": "2019-07-11", 
    "expirationDate": "2028-08-11", 
    "paymentLink": "https://ebc2test.example.com/ebc2/invoicing/payInvoice/1vkESfV2lLy8M2qkDFH0aUYZUOTasbrkOZvXf9ShjW3VJKVxvkLw2OUzMp1bihov?version=v2.1", 
    "deliveryMode": "Email", 
    "customLabels": [ 
      { 
        "key": "billTo", 
        "value": "Payee name" 
      } 
    ] 
  }, 
  "orderInformation": { 
    "amountDetails": { 
      "totalAmount": 2623.64, 
      "currency": "USD", 
      "balanceAmount": 2623.64, 
      "subAmount": 2749.72 
    } 
  } 
} 
 
```

Invoicing Settings API Requests {#invoicing-settings-intro}
===========================================================

The Invoicing Settings API enables you to customize your invoice checkout experience, add a custom message to your email communications, and enable payer authentication. You can also retrieve the invoice settings for your payment page.

* [Update Invoice Settings](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-settings-intro/invoicing-settings-update.md "")
* [Get Invoice Settings](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-settings-intro/invoicing-settings-get.md "")

Update Invoice Settings {#invoicing-settings-update}
====================================================

Use invoice settings to configure and manage the behavior, appearance, and security of your invoice payments and payment page. You can update these settings:  
![Branding Identity: Customize the checkout experience of your payment page to match your
branding, such as Brand colors, Business name, Logo, VAT tax number. Payment Page Label
Controls: Rename certain labels that display on the payment page and disable certain
labels from displaying. Customer Data and Redirect URLs: Enable the capture of customer
billing information as well as set custom redirect URLs after transaction completion.
Email Notification Behavior: Customize your email message, frequency of payment reminders,
successful transaction notifications, and language settings. Payer Authentication
Enablement: If you are using Payer Authentication, you must send this request to enable
it. Include the
invoiceSettingsInformation.payerAuthenticationInInvoicing field in
your request and set it to enable.](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/invoicing/images/invoicing-update-settings-600x375.svg/jcr:content/renditions/original)  
For additional information about using payer authentication for invoicing, see [Add Payer Authentication to Invoicing](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-features-intro.md "").

Reset to Default Settings {#invoicing-settings-update_reset-settings}
---------------------------------------------------------------------

To reset your invoice settings to their default values, send the corresponding fields you want to reset with no value. This does not apply to the payment page label controls.

Endpoints
---------

Send your API request message to one of these endpoints:  
**Production:** `PUT ``https://api.example.com``/invoicing/v2/invoiceSettings?productType=INVOICING`  
**Test:** `PUT ``https://apitest.example.com``/invoicing/v2/invoiceSettings?productType=INVOICING`  
**India Production:** `PUT https://api.in,example.com/invoicing/v2/invoiceSettings?productType=INVOICING`

Fields for Updating Invoice Settings {#invoicing-settings-update-fields}
========================================================================

The update invoice settings request does not require a specific set of fields. Instead, you can choose the fields to include in your request based on aspects of your checkout experience, email communications, and payer authentication enablement that you want to update.

|           Name           |                    API Request Field                    |                                                                                                                                                                                     Description                                                                                                                                                                                      |
|--------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Business Name            | invoiceSettingsInformation. merchantDisplayName         | The business name displayed on the invoice.                                                                                                                                                                                                                                                                                                                                          |
| Currency                 | invoiceSettingsInformation. defaultCurrencyCode         | The currency of the billed amount. The currency code default value is set to `USD` when this field is not specified. Only three-character ISO Standard Currency Codes are accepted. For more information, see [ISO Standard Currency Codes](https://developer.example.com/docs/gateway/en-us/currency-codes/reference/all/na/currency-codes/currency-codes.md "") reference guide.. |
| Header Background Color  | invoiceSettingsInformation. headerStyle.backgroundColor | The background color of the displayed invoice. Only hexadecimal code values with a prefixed `#` are accepted. Example: `#000000`                                                                                                                                                                                                                                                     |
| Logo                     | invoiceSettingsInformation. merchantLogo                | The binary format of your logo that determines the image displayed to your customers. Image files are restricted to 1 MB and must be encoded in Base64 format. These are the supported file types: * gif * jpg * png                                                                                                                                                                 |
| VAT Tax Number           | invoiceSettingsInformation. vatRegistrationNumber       | The government-assigned tax identification number.                                                                                                                                                                                                                                                                                                                                   |
| VAT Tax Number Displayed | invoiceSettingsInformation. showVatNumber               | The toggle for displaying the VAT tax number in the invoice. Possible values: * `false`: Do not display the VAT tax number. * `true`: Display the VAT tax number.                                                                                                                                                                                                                    |
[Branding Identity Settings]

|     Name     |                 API Request Field                 |                                                                                                                                                                                                                                           Description                                                                                                                                                                                                                                            |
|--------------|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Label        | invoiceSettingsInformation. customLabels\[\]key   | The label that you can edit to display a custom text on the invoice creation page and the payment page. Possible values: * `billTo`: billed customer name * `companyName`: company name * `customerId`: customer identifier * `description`: invoice description * `discount`: discount value * `invoiceNumber`: invoice number * `partialPayment`: partial payment amount * `shipping`: shipping amount * `tax`: tax amount Including this field set to no value does not update your settings. |
| Custom Label | invoiceSettingsInformation. customLabels\[\]value | The custom text you want to display instead of the default label text. Set this field to the text you want to display instead of the label you set in the invoiceSettingsInformation.customLabels\[\]key field. Including this field set to no value does not update your settings.                                                                                                                                                                                                              |
[Payment Page Label Control Settings: Rename Label]

|       Name        |                 API Request Field                  |                                                                                                                                                        Description                                                                                                                                                         |
|-------------------|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Label             | invoiceSettingsInformation. customLabels\[\]key    | The label on the payment page that can be removed. Possible values: * `customerId`: customer identifier * `description`: invoice description * `discount`: discount value * `invoiceNumber`: invoice number * `partialPayment`: partial payment amount Including this field set to no value does not update your settings. |
| Hide Label Toggle | invoiceSettingsInformation. customLabels\[\]hidden | The toggle that determines if the label included in the invoiceSettingsInformation.customLabels\[\]key field can display on the payment page. Possible values: * `true`: label is removed from payment page * `false`: label displays on payment page Including this field set to no value does not update your settings.  |
[Payment Page Label Control Settings: Remove Label]

|            Name             |                       API Request Field                       |                                                                                                                                                                                 Description                                                                                                                                                                                 |
|-----------------------------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Label                       | invoiceSettingsInformation. customLabels\[\]key               | The label on the payment page that can be removed. Possible values: * `discount`: invoice discount amount * `tax`: invoice tax amount Including this field set to no value does not update your settings.                                                                                                                                                                   |
| Hide Label for Invoices     | invoiceSettingsInformation. customLabels\[\] hiddenForInvoice | The toggle that determines if the label included in the invoiceSettingsInformation.customLabels\[\]key field can display on the payment page. Possible values: * `true`: label is removed from invoice payment page * `false`: label displays on invoice payment page Including this field set to no value does not update your settings.                                   |
| Hide Label for Invoice Item | invoiceSettingsInformation. customLabels\[\] hiddenForItem    | The toggle that determines if the label included in the invoiceSettingsInformation.customLabels\[\]key field can display on an itemized invoice payment page. Possible values: * `true`: label is removed from itemized invoice payment page * `false`: label displays on itemized invoice payment page Including this field set to no value does not update your settings. |
[Payment Page Label Control Settings: Remove Label by Product]

|                Name                 |                        API Request Field                        |                                                                                            Description                                                                                             |
|-------------------------------------|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Customer Shipping Address           | invoiceSettingsInformation.shipTo                               | Enables the invoice payment page to save the customer's shipping address. Possible values: * `false`: Does not save the customer's shipping address * `true`: Save the customer's shipping address |
| Customer Phone Number               | invoiceSettingsInformation.phoneNumber                          | Enables the invoice payment page to save the customer's phone number. Possible values: * `false`: Does not save the customer's phone number * `true`: Save the customer's phone number             |
| Customer Email                      | invoiceSettingsInformation.email                                | Enables the invoice payment page to save the customer's email address. Set to `true`.                                                                                                              |
| Successful Transaction Redirect URL | invoiceSettingsInformation. customRedirectUrls. paymentAccepted | The URL that the customer is redirected to after completing a successful transaction in which the payment is processed.                                                                            |
| Pending Transaction Redirect URL    | invoiceSettingsInformation. customRedirectUrls. paymentPending  | The URL that the customer is redirected to after completing checkout and the payment is pending.                                                                                                   |
| Failed Transaction Redirect URL     | invoiceSettingsInformation. customRedirectUrls. paymentRejected | The URL that the customer is redirected to after a transaction is rejected.                                                                                                                        |
[Payment Page Behavior Settings]

|            Name             |                      API Request Field                       |                                                                                                                                                                                                                    Description                                                                                                                                                                                                                    |
|-----------------------------|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Email Message               | invoiceSettingsInformation. customEmailMessage               | The custom message in the invoice email.                                                                                                                                                                                                                                                                                                                                                                                                          |
| Email Reminder              | invoiceSettingsInformation. enableReminders                  | The toggle for sending an email reminder to the customer five days before the invoice due and one day after it is past due. Possible values: * `False`: No email reminder is sent. * `True`: Email reminders are sent.                                                                                                                                                                                                                            |
| Merchant Email Notification | invoiceSettingsInformation. enableMerchantEmailNotifications | The toggle for the merchant receiving an email notification that a transaction is complete. Possible values: * `False`: No email notification sent * `True`: Email notification sent                                                                                                                                                                                                                                                              |
| Language                    | invoiceSettingsInformation. deliveryLanguage                 | The language of the email message sent to the customer. Set to one of these possible values: * `de-DE`: German (Germany) * `en-US`: English (United States) * `es-419`: Spanish as used in Latin America and the Caribbean * `fr-FR`: French (France) * `ja-JP`: Japanese (Japan) * `pt-BR`: Portuguese (Brazil) * `ru-RU`: Russian (Russia) * `zh-CN`: Chinese (Simplified, People's Republic of China) * `zh-TW`: Chinese (Traditional, Taiwan) |
[Email Notification Settings]

|              Name               |                     API Request Field                      |                                                                                                                                                                                                Description                                                                                                                                                                                                |
|---------------------------------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Payer Authentication Enablement | invoiceSettingsInformation. payerAuthenticationInInvoicing | The indicator for payer authentication enablement. Possible values: * `disable`: Disable 3-D Secure * `enable`: Enable 3-D Secure payer authentication For more information about including payer authentication to your invoices, see [Add Payer Authentication to Invoicing](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-features-intro.md ""). |
[Payer Authentication Enablement Settings]

Example: Update Invoice Settings {#invoicing-settings-update-ex}
================================================================

Request

```
{
  "invoiceSettingsInformation": {
    "merchantLogo": "/9j/4AWFhYW",
    "merchantDisplayName": "Custom Merchant Display Name",
    "customEmailMessage": "Custom merchant email message",
    "enableReminders": true,
    "headerStyle": {
      "fontColor": "#000001",
      "backgroundColor": "#FFFFFF"
    },
    "deliveryLanguage": "en-US",
    "defaultCurrencyCode": "USD",
    "payerAuthenticationInInvoicing": "enable",
    "showVatNumber": false,
    "vatRegistrationNumber": "Inv1234",
    "shipTo": false,
    "phoneNumber": false,
    "email": false,
    "enableMerchantEmailNotifications": false,
    "customLabels": [
      {
        "key": "billTo",
        "value": "Payee name"
      }
    ],
    "customRedirectUrls": {
      "paymentAccepted": "https://example.com/success",
      "paymentRejected": "https://example.com/fail",
      "paymentPending": "https://example.com/pending"
    }
  }
}
```

Response to a Successful Request

```
{
  "submitTimeUtc": "2026-02-03T20:48:27.917947446Z",
  "invoiceSettingsInformation": {
    "merchantLogo": "data:image/JPEG;base64,/9j/4AWFhYW",
    "merchantDisplayName": "Custom Merchant Display Name",
    "customEmailMessage": "Custom merchant email message",
    "enableReminders": true,
    "headerStyle": {
      "fontColor": "#000001",
      "backgroundColor": "#FFFFFF"
    },
    "deliveryLanguage": "en-US",
    "defaultCurrencyCode": "USD",
    "payerAuthentication3DSVersion": "True",
    "showVatNumber": false,
    "phoneNumber": false,
    "shipTo": false,
    "email": true,
    "enableMerchantEmailNotifications": false,
    "customLabels": [
      {
        "key": "billTo",
        "value": "Payee name"
      }
    ],
    "customRedirectUrls": {
      "paymentAccepted": "https://example.com/success",
      "paymentRejected": "https://example.com/fail",
      "paymentPending": "https://example.com/pending"
    }
  },
  "merchantInformation": {
    "name": "API Ref Sandbox",
    "phone": "4251231234",
    "addressDetails": {
      "address1": "123 Main St",
      "city": "Bellevue",
      "state": "WA",
      "country": "us",
      "postalCode": "98005"
    }
  }
} 
```

REST Interactive Example: Update Invoice Settings {#invoicing-settings-update-ex-live}
======================================================================================

Click this image to access the interactive code example for updating invoice settings.

#### Figure:

Update Invoice Settings in the Developer Center Sandbox [![Image and link to the interactive code example for updating invoice
settings.](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/invoicing/images/invoicing-settings-pgw.png/jcr:content/renditions/original)](https://developer.example.com/api-reference-assets/index.md#invoicing_invoice-settings_update-invoice-settings "")

Get Invoice Settings {#invoicing-settings-get}
==============================================

You can retrieve the invoice settings for your payment page by sending a get invoice request.

Endpoints
---------

Send the API request to one of these endpoints:  
**Production:** `GET ``https://api.example.com``/invoicing/v2/invoiceSettings?productType=INVOICING`  
**Test:** `GET ``https://apitest.example.com``/invoicing/v2/invoiceSettings?productType=INVOICING`  
**India Production:** `GET https://api.in.example.com/invoicing/v2/invoiceSettings`

Successful Response
-------------------

A successful request is indicated by a response message that includes this information:

* Logo
* Business name
* Customized email message
* Email reminder indicator
* Color and font of the invoice
* Language used in the invoice
* Currency of the invoiced amount
* Payer authentication enablement indicator
* VAT value and visibility
* Customer data saved indicator (shipping address, phone number, or email)
* Custom labels
* Redirect URLs
* Merchant information

Example: Get Invoice Settings {#invoicing-settings-get-ex}
==========================================================

Endpoint

```keyword
GET https://api.example.com/invoicing/v2/invoiceSettings
```

Request

```
{}
```

Response to a Successful Request

```
{
  "submitTimeUtc": "2026-02-03T20:48:27.917947446Z",
  "invoiceSettingsInformation": {
    "merchantLogo": "data:image/JPEG;base64,/9j/4AWFhYW",
    "merchantDisplayName": "Custom Merchant Display Name",
    "customEmailMessage": "Custom merchant email message",
    "enableReminders": true,
    "headerStyle": {
      "fontColor": "#000001",
      "backgroundColor": "#FFFFFF"
    },
    "deliveryLanguage": "en-US",
    "defaultCurrencyCode": "USD",
    "payerAuthentication3DSVersion": "True",
    "showVatNumber": false,
    "phoneNumber": false,
    "shipTo": false,
    "email": true,
    "enableMerchantEmailNotifications": false,
    "customLabels": [
      {
        "key": "billTo",
        "value": "Payee name"
      }
    ],
    "customRedirectUrls": {
      "paymentAccepted": "https://example.com/success",
      "paymentRejected": "https://example.com/fail",
      "paymentPending": "https://example.com/pending"
    }
  },
  "merchantInformation": {
    "name": "API Ref Sandbox",
    "phone": "4251231234",
    "addressDetails": {
      "address1": "123 Main St",
      "city": "Bellevue",
      "state": "WA",
      "country": "us",
      "postalCode": "98005"
    }
  }
} 
```

REST Interactive Example: Get Invoice Settings {#invoicing-settings-get-ex-live}
================================================================================

Click this image to access the interactive code example for updating invoice settings.

#### Figure:

Update Invoice Settings in the Developer Center Sandbox [![Image and link to the interactive code example for updating invoice
settings.](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/invoicing/images/invoicing-settings-pgw.png/jcr:content/renditions/original)](https://developer.example.com/api-reference-assets/index.md#invoicing_invoice-settings_get-invoice-settings "")

Add Payer Authentication to Invoicing {#invoicing-features-intro}
=================================================================

You can enable Payer Authentication in your invoices.  
Payer Authentication, also known as 3-D Secure, helps to minimize costly fraudulent transactions by adding an extra layer of protection to the payment process. The solution enables issuers to authenticate the cardholder using various available methods, such as one-time passwords and biometrics.  
Invoicing supports these Payer Authentication services:

* American Express SafeKey
* JCB J/Secure
* Mastercard Identity Check
* Relay Secure

Card Types
:
Payer Authentication supports these card types:

    * American Express
    * Discover
    * JCB
    * Mastercard
    * Relay

Prerequisites for Payer Authentication
--------------------------------------

To sign-up and enable Payer Authentication, you must complete these tasks.

1. Contact your `Payment Gateway` account representative and provide your:
   * `Payment Gateway` test merchant ID
   * [Merchant information](#invoicing-features-intro_pa-required-merchant-info-table "")
2. Contact your acquirer, also known as the merchant bank, to establish the Payer Authentication service.
3. If you are using an API, your software developer should become familiar with the API fields and technical details of this service.

Required Merchant Information {#invoicing-features-intro_merch-info}
--------------------------------------------------------------------

To enable Payer Authentication services, contact customer support and provide this information about your company and acquiring bank.

| Information                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                   |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| About your company                                                                                                                                                        | * Your `Payment Gateway` merchant ID. * URL of your company's website, for example: *http://www.example.com*. * Two-character ISO code for your country. * 3-D Secure requestor ID. * 3-D Secure requestor name. * Merchant category code. {#invoicing-features-intro_ul-company}                 |
| Bank information                                                                                                                                                          | * Name of your bank acquirer. * Complete name and address of your bank contact, including email address. {#invoicing-features-intro_ul-bank}                                                                                                                                                  |
| Payment card information Supported card types: * American Express * Diners Club * Discover * JCB * Mastercard * Maestro * Relay {#invoicing-features-intro_ul_ydn_sfk_byb} | Information provided by your acquirer about each payment card company for which you are configured, including: * Six-digit BIN numbers. * Acquirer merchant ID: the merchant ID assigned by your acquirer. * All currencies that you can process. {#invoicing-features-intro_ul-card-company} |
[Required Merchant Information for Payer Authentication Services]

Enable Payer Authentication
---------------------------

After completing the above requirements, you must enable Payer Authentication using either the invoicing API or the `Business Center`.

API Enablement
:
To enable Payer Authentication using the invoicing API, send an *update invoice settings* request and set the invoiceSettingsInformation.payerAuthenticationInInvoicing request field to `enable`.

    For more information, see [Update Invoice Settings](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/invoicing-settings-intro/invoicing-settings-update.md "").

`Business Center` Enablement
:
1. Log in to the `Business Center`.
* **Test:**  
[`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
* **Production:**  
**Production:** [`https://businesscenter.example.com`](https://businesscenter.example.com/ebc2/ "")
2. On the `Business Center`'s left navigation bar, navigate to ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-invoicing.svg/jcr:content/renditions/original) Invoicing \&gt; Manage Invoices.
3. Click ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-accnt-mgmt.svg/jcr:content/renditions/original) **Settings**.  
![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/invoicing/images/invoicing-payerauth-ebc-settings.png/jcr:content/renditions/original)
4. Click the **Security** tab.
5. Select the **Enable** option.
6. Click **Save** when done.  
![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/invoicing/images/invoicing-settings-enable.png/jcr:content/renditions/original)

Webhook Notifications for Invoicing {#invoicing-webhooks-intro}
===============================================================

Webhooks are automated notifications generated by system events that occur in your organization. You can create a webhook subscription for invoicing events to receive a notification when an invoice is:

* Cancelled
* Five-day early reminder
* Fully paid
* Overdue reminder
* Partially paid
* Sent

You must have a URL for the webhook notifications to be sent to.  
Notifications that contain sensitive, personally identifiable information (PII), such as account numbers, are sent using message-level encryption. Transport Layer Security is required in order to ensure data integrity.  
There are additional requirements for implementing webhooks that are not discussed in this guide. To create to webhook subscription to receive invoicing related notifications, see the [*Webhooks Implementation Guide for the REST API*](https://developer.example.com/docs/gateway/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro.md "").

Invoicing Product ID and Event Types
------------------------------------

When you send a *create a webhook subscription* request, set the products.productId field to `customerInvoicing` and set the products.eventTypes field to one or more of the values listed in the Event Type Field Value column in the table below. If you include multiple event types in your request, separate each event type field value with the comma character (`,`).

|     Product ID      |             Event Type Field Value             |                                                                  Description                                                                   |
|---------------------|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `customerInvoicing` | `invoicing.customer.invoice.cancel`            | Merchants can subscribe to this event type to automate how their system is informed when an invoice is cancelled.                              |
| `customerInvoicing` | `invoicing.customer.invoice.overdue-reminder ` | Notifies you 1 day after the invoice payment is due. This event is triggered if you have invoice reminders enabled in your invoice settings.   |
| `customerInvoicing` | `invoicing.customer.invoice.paid`              | Merchants can subscribe to this event type to automate how their system is informed when an invoice is fully paid.                             |
| `customerInvoicing` | `invoicing.customer.invoice.partial-payment`   | Merchants can subscribe to this event type to automate how their system is informed when an invoice is partially paid.                         |
| `customerInvoicing` | `invoicing.customer.invoice.reminder`          | Notifies you 5 days before the invoice payment is due. This event is triggered if you have invoice reminders enabled in your invoice settings. |
| `customerInvoicing` | `invoicing.customer.invoice.send`              | Merchants can subscribe to this event type to automate how their system is informed when an invoice is sent to the customer.                   |
[Invoicing Webhook Product ID and Event Types]

Example: Creating an Invoice Webhook Subscription {#x-ex-rest}
==============================================================

> IMPORTANT  
> There are additional requirements for implementing webhooks that are not discussed in this guide. To create to webhook subscription to receive invoicing related notifications, see the [*Webhooks Implementation Guide for the REST API*](https://developer.example.com/docs/gateway/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro.md "").  
> Only use this example to reference how to format the eventTypes request field and its values.
> Request

```
{
  "name": "Invoicing Webhooks",
  "description": "Webhooks for Invoicing Events",
  "organizationId": "organizationId",
  "productId": "customerInvoicing",
  "eventTypes": [
    "invoicing.customer.invoice.cancel",
    "invoicing.customer.invoice.paid",
    "invoicing.customer.invoice.partial-payment",
    "invoicing.customer.invoice.send"
  ],
  "webhookUrl": "https://test.com:443/test",
  "healthCheckUrl": "https://test.com:443/test",
  "notificationScope": "SELF",
  "retryPolicy": {
    "algorithm": "ARITHMETIC",
    "firstRetry": 1,
    "interval": 1,
    "numberOfRetries": 3,
    "deactivateFlag": "false",
    "repeatSequenceCount": 0,
    "repeatSequenceWaitTime": 0
  },
  "securityPolicy": {
    "securityType": "KEY",
    "proxyType": "external"
  }
}
```

Response to a Successful Request

```
{
  "organizationId": "invoicetest",
  "productId": "customerInvoicing",
  "eventTypes": [
    "invoicing.customer.invoice.cancel",
    "invoicing.customer.invoice.paid",
    "invoicing.customer.invoice.partial-payment",
    "invoicing.customer.invoice.send"
  ],
  "webhookId": "fc880f5a-2145-44db-e053-9e588e0a6a26",
  "name": "Invoicing Webhooks",
  "webhookUrl": "https://test.com:443/test",
  "healthCheckUrl": "https://test.com:443/test",
  "createdOn": "2023-05-25T16:24:51.886Z",
  "status": "INACTIVE",
  "description": "Webhooks for Invoicing Events",
  "retryPolicy": {
    "algorithm": "ARITHMETIC",
    "firstRetry": 1,
    "interval": 1,
    "numberOfRetries": 3,
    "deactivateFlag": false,
    "repeatSequenceCount": 0,
    "repeatSequenceWaitTime": 0
  },
  "securityPolicy": {
    "securityType": "KEY",
    "proxyType": "external",
    "digitalSignatureEnabled": "yes"
  },
  "version": "3",
  "deliveryType": "nrtdCentral",
  "notificationScope": "SELF"
}
```

Using the `Business Center` {#invoicing-ebc-intro}
==================================================

You can create and manage invoices using the `Business Center`:

* **Test:** [`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
* **Production:** [`https://businesscenter.example.com`](https://businesscenter.example.com/ebc2/ "")

After logging in to the `Business Center`, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-invoicing.svg/jcr:content/renditions/original) **Invoicing** on the left navigation bar.  
For documentation about how to create invoices in the `Business Center`, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-support.svg/jcr:content/renditions/original) **Support \&gt; Help** on the top right of the `Business Center` home screen.

Manage Invoices Using the `Business Center` {#invoicing-ebc}
============================================================

This section describes how to log in and perform these invoicing tasks in the `Business Center`:

* Enable 3-D secure for your invoices
* Manage your invoices
* Apply fraud management detection to your invoices
* Filter invoice transactions using transaction management
* Generate reports with invoice data
* Create custom fields and messages in an invoice

For additional documentation about how to perform other invoicing tasks in the `Business Center`, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-support.svg/jcr:content/renditions/original) **Support \&gt; Help** on the top right of the `Business Center` home screen.

Logging in to the `Business Center`
-----------------------------------

You can create, send, and manage invoices using the `Business Center`:

* **Test:** [`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
* **Production:** [`https://businesscenter.example.com`](https://businesscenter.example.com/ebc2/ "")

After logging in to the `Business Center`, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-invoicing.svg/jcr:content/renditions/original) **Invoicing** on the left navigation panel to access the Invoicing menu.

Enabling 3-D Secure for Invoices {#invoicing-3ds}
=================================================

3-D Secure helps to minimize costly fraudulent transactions by adding an extra layer of protection to the payment process.  
Follow these steps to enable 3-D Secure for your invoice transactions. You must have Payer Authentication already enabled for your account. If you do not, or you do not know, contact your Payment Gateway account representative to enable it.

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://businesscenter.example.com/ebc2/ "")
     {#invoicing-3ds_step-ebc-login}
     {#invoicing-3ds_step-ebc-login}
2. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-invoicing.svg/jcr:content/renditions/original) **Invoicing \&gt; Manage Invoices**.  
   The Manage Invoices page appears.
3. Click **Settings**.  
   ![](/content/dam/documentation/pgw/en-us/olh/Invoicing/images/invoice-3DS-settings.png/jcr:content/renditions/original)
4. Click the **Security** tab.  
   The 3-D Secure section appears.
5. Choose **Enable**.
6. When done, click **Save**.  
   ![](/content/dam/documentation/pgw/en-us/olh/Invoicing/images/invoice-3DS-enable.png/jcr:content/renditions/original)

Fraud Management for Invoices {#invoicing-decision-manager}
===========================================================

This section describes how to use `Decision Manager` to apply fraud detection to invoice transactions.
Follow these steps to create a profile and a corresponding profile selector rule for your invoice transactions.

1. Log in to the `Business Center`:

   * **Test:** [`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://businesscenter.example.com/ebc2/ "")
2. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-dm.svg/jcr:content/renditions/original) **`Decision Manager` \&gt; Configuration \&gt; Profiles**.  
   The Profiles page appears.

3. In the Order Profiles section, click **ADD EMPTY PROFILE**.  
   The Profile Editor page appears.

4. Enter the relevant information for these sections and their corresponding fields:

   #### ADDITIONAL INFORMATION

   * Profile Definition
   * Queue Selection
   * Fraud Score Threshold Rule Generator  
     ![](/content/dam/documentation/pgw/en-us/olh/Invoicing/images/invoice-profile.png/jcr:content/renditions/original)
5. In the Rules section, select only Accept and Reject rules, and enter any relevant information into the **Priority** and **Execution Timing** fields.

6. When done, click **APPLY** . You can click **SAVE** instead if you do not want the new profile to be immediately active.  
   The Profiles page appears.

7. In the Profile Selectors section, click **ADD SELECTOR RULE**.  
   The Rule Definition page appears.

8. In the Rule Definition section, enter this field information:

   |      Field      |                         Definition                         |
   |-----------------|------------------------------------------------------------|
   | **Name**        | The name of the profile selector rule.                     |
   | **Description** | The description that explains the profile selector rule.   |
   | **Profile**     | Choose the profile you created on the Profile Editor page. |
   [Rule Definition Fields and Values]

9. In the Rule Conditions section, choose these options:

   1. Select **All conditions below are true**. By default, it should already be selected.
   2. Set Order Elements to **Connection Method**.
   3. Set Comparison Operator to **is equal to**.
   4. Set Comparison Values to **Custom Value**.
   5. In the Custom Value(s) field, enter Invoicing.  
      ![](/content/dam/documentation/pgw/en-us/olh/Invoicing/images/invoice-profile-conditions.png/jcr:content/renditions/original)
10. When done, click **APPLY** . You can click **SAVE** instead if you do not want the new profile selector to be immediately active.  
    ![](/content/dam/documentation/pgw/en-us/olh/Invoicing/images/invoice-profile-selector.png/jcr:content/renditions/original)

#### RESULT

The new profile selector now appears as an active selector.

Approving Payment Flagged for Fraud {#invoicing-fraud-review}
=============================================================

This section describes how to approve an invoice payment that is flagged for fraud.  
When the customer completes an invoice payment, this message may display to them: "Success. Your transaction is being processed. We will notify you when it is completed."  
This message indicates that the payment is flagged for fraud. The customer must now wait until you accept or reject the payment using `Decision Manager` in the `Business Center`. Until you accept or reject the payment, the customer can no longer make the payment. If the customer reloads the payment screen, this message displays: "Information: A payment is pending completion."  
Follow these steps to approve a payment flagged for fraud:

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://businesscenter.example.com/ebc2/ "")
2. On the left navigation panel choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-dm.svg/jcr:content/renditions/original) **`Decision Manager` \&gt; Case Management \&gt; Cases**.  
   The Case Management page appears.
3. Click the order number of the pending invoice payment.  
   A decision window appears.
4. To approve the flagged invoice payment, click ![](/content/dam/documentation/pgw/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) (approve).
5. After reviewing the comments and reason codes, click **ACCEPT**.  
   The settlement information displays.
6. Click **SETTLE**.  
   The payment is now settled.
7. (Optional) You can enable automatic settlement and reversals for accepted and rejected payments. This expedites the review process.
   1. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-dm.svg/jcr:content/renditions/original) **`Decision Manager` \&gt; Configurations \&gt; Extended Settings**.  
      The Extended Settings page opens.
8. In the Payment Processing section, use the Description drop-down menu to choose **Enable with Settlement Selected**. This option enables payments that you accept to automatically settle.

Rejecting Payment Flagged for Fraud {#invoicing-fraud-review-reject}
====================================================================

This section describes how to reject an invoice payment that is flagged for fraud.  
When the customer completes an invoice payment, this message may display to them: "Success. Your transaction is being processed. We will notify you when it is completed."  
This message indicates that the payment is flagged for fraud. The customer must now wait until you accept or reject the payment using `Decision Manager` in the `Business Center`. Until you accept or reject the payment, the customer can no longer make the payment. If the customer reloads the payment screen, this message displays: "Information: A payment is pending completion."  
Follow these steps to reject a payment flagged for fraud:

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://businesscenter.example.com/ebc2/ "")
2. On the left navigation panel choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-dm.svg/jcr:content/renditions/original) **Decision Manager \&gt; Case Management \&gt; Cases**.  
   The Case Management page appears.
3. Click the order number of the pending invoice payment.  
   A decision window appears.
4. To reject the flagged invoice payment, click ![](/content/dam/documentation/pgw/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original) (reject).
5. After reviewing the comments and reason codes, click **Select**.  
   The successful rejection message displays.
6. (Optional) You can enable automatic settlement and reversals for accepted and rejected payments. This expedites the review process, making a seamless review experience.
   1. On the left navigation panel choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-dm.svg/jcr:content/renditions/original) **Decision Manager \&gt; Configurations \&gt; Extended Settings**.  
      The Extended Settings page opens.
   2. In the Decision Reject section, use the Description drop-down menu to choose **Enable with authorization reversal selected by default**. This option enables payments that you reject to automatically reverse.  
      ![](/content/dam/documentation/pgw/en-us/olh/Invoicing/images/invoice-enable-auto-settle.png/jcr:content/renditions/original)

Filtering Invoice Transactions in Transaction Management {#invoicing-trxn-mgmt-filter}
======================================================================================

This task describes how to view only your invoice transactions by using the filter tool in Transaction Management.

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://businesscenter.example.com/ebc2/ "")
2. On the left navigation panel, click ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-trxn-mgmt.svg/jcr:content/renditions/original) **Transaction Management** **\&gt;** **Transactions**.  
   The Transaction page appears.
3. Click **Add filter**.  
   The **New Filter** field appears.
4. Click the **New Filter** field and enter Client Application or choose **Client Application** from the drop-down menu.
5. Click the **New Filter** field again and enter Invoicing or choose **Invoicing** from the drop-down menu.
6. When done, click **Search**.  
   The Search Results table displays only your invoice transactions.  
   ![](/content/dam/documentation/pgw/en-us/olh/Invoicing/images/invoice-trxn-mgmt-filter.png/jcr:content/renditions/original)
7. (Optional) To verify that the transactions listed in the Search Results table are invoicing transactions, click **Edit columns**.  
   The Edit Table Layout section appears.
8. Click **Add item**.  
   The Add Table Column page appears.
9. In the **Select Table Column** field, enter Client Application or choose **Client Application** from the drop-down menu, and then click **Save**.  
   The Edit Table Layout section appears.
10. Click **Save**.  
    The Search Results table appears with your filtered transactions and the new Client Application column. Each entry in the Client Application column should contain the Invoicing value, indicating that the transaction is an invoice.  
    ![](/content/dam/documentation/pgw/en-us/olh/Invoicing/images/invoice-trxn-mgmt-filter-column-1.png/jcr:content/renditions/original)

Generating a Report with Invoice Data {#invoicing-ebc-reports}
==============================================================

This task describes how to use the Reports feature in the `Business Center` to generate a report that contains only your invoicing data.

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://businesscenter.example.com/ebc2/ "")
2. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-reports.svg/jcr:content/renditions/original) **Reports \&gt; Downloadable Reports \&gt; Available Reports**.  
   The Available Reports page appears.
3. Click the **Create custom report**.  
   The Create Report Subscription page appears.  
   ![](/content/dam/documentation/pgw/en-us/olh/Invoicing/images/invoice-report-1.png/jcr:content/renditions/original)
4. In the Advanced Report Features section, click the Connection Method drop-down menu and choose **Invoicing**.  
   There is additional required information you must enter before you can generate a report.  
   ![](/content/dam/documentation/pgw/en-us/olh/Invoicing/images/invoice-report-2.png/jcr:content/renditions/original)
5. When done, click **Create**.  
   The Report Subscription Management page appears.  
   Click the **Custom Report Subscriptions** tab to view your new custom report that includes invoicing data.  
   ![](/content/dam/documentation/pgw/en-us/olh/Invoicing/images/invoice-report-3.png/jcr:content/renditions/original)

Create a Custom Text Field for an Invoice {#invoicing-mdf-textbox}
==================================================================

You can create a custom text field to display to your customers or merchants on your invoice checkout page. This text field enables users to enter information in the text field, or read a custom message. For example, you can give your customers the option to enter any specifications for their order in the text field. Follow these steps to create a custom text field.

1. Log in to the `Business Center`:

   * **Test:** [`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://businesscenter.example.com/ebc2/ "")
2. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-invoicing.svg/jcr:content/renditions/original) **Invoicing \&gt; Manage Invoices**.

3. Click the **Custom Fields** tab.  
   The Custom Fields options displays.

4. Click **Text field**.

5. Enter this information in the fields:

   |     Field Name      |                                       Description                                       |
   |---------------------|-----------------------------------------------------------------------------------------|
   | Label               | The title of the new custom text field.                                                 |
   | Min character limit | The minimum number of characters the customer or merchant must enter in the text field. |
   | Max character limit | The maximum number of characters the customer or merchant must enter in the text field. |
   | Default text        | The text that displays by default in the text field.                                    |
   [Text Field Information]

6. Check the **Customer visible** box to make the text field viewable by the customer.  
   You can check the **Customer Read Only** box to prevent the customer from entering text in the text field. Choose this option if you want to display a message to the customer.

7. Click **Add Field** when done.  
   ![](/content/dam/documentation/pgw/en-us/olh/Invoicing/images/invoice-mdf-text-field.png/jcr:content/renditions/original)

#### RESULT

The new custom text field is listed under the Custom Fields tab, and its corresponding drop-down menu appears in the invoice preview.  
![](/content/dam/documentation/pgw/en-us/olh/Invoicing/images/invoice-mdf-text-field-2.png/jcr:content/renditions/original)

Creating New Custom Report Subscriptions {#create_new_subscription}
===================================================================

A recurring report subscription is a template that describes the attributes of a report, including how often it runs and the period of time it spans. After your recurring report is generated, it is available for download on the [`Available Reports`](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/available_reports.md "") page. You can maintain up to 20 report subscriptions at any time.  
In addition to choosing from [available fields](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/app_fields.md ""), you can customize the following attributes of a recurring subscription:

* **Name**: a unique name for the report. The name cannot be changed after a report is created.
* **Report type**: a set of reports that can be customized. The report type cannot be changed after a report is created.
* **Format**: the format of a generated report (XML or CSV).
* **Frequency**: the frequency at which a report runs: daily, weekly, or monthly.
* **Start time**: the time of day at which a report runs.

The process for creating a report subscription is the same as for creating a one-time report. The steps listed below focus on creating recurring subscriptions.  
To create a report subscription:

1. On the left navigation pane, click the **`Reports`** icon.

2. Under Downloadable Reports, click **`Report Subscription Management`** . The `Report Subscription Management` page appears.

3. Click the **Custom Report Subscriptions** tab. The Custom Reports Subscriptions List appears.

4. Click **Create Subscription**. The Create Report Subscription page appears.

5. Under Account Setup, select whether to base the report on data from a specific merchant, or a group of merchants, and then choose an available value in the Merchants or Groups list.

   #### ADDITIONAL INFORMATION

   This option is only available for partners and account level users. To create a report that includes all merchants or groups, use the default value.

6. Under Basic Report Setup, enter the following:

   1. In the **Report Name** field, enter the name for your report that best reflects the data you want to capture. Each report must have a unique name containing up to 250 characters.
   2. In the **Report Type** field, select the type of report that most closely represents the data or process you want to include. The `Business Center` automatically includes the most commonly used fields in your report based on this selection. See the next step for more information on how to customize these values.
   3. In the **File Format** field, choose whether the `Business Center` creates the report in XLS or XML format.
   4. In the **Frequency** field, choose **Recurring subscription** to automatically generates daily, weekly, or monthly reports. You can also create a [One-time report](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/generate_one-time_report.md "").
7. To change any of the default fields included in your report, click the **Arrow** icon to expand the Advanced Report Features section, and then perform one or more of the following actions (available actions are based on the services you use):

   | In this field or tab |                                                                                                                                                                                                      Do this                                                                                                                                                                                                       |
   |----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | Credit Amounts       | Check the box if you want credits to appear as negative amounts (for example: -1390.00)                                                                                                                                                                                                                                                                                                                            |
   | Naming Convention    | Select how you want the field names to appear in the report: * **SOAPI** displays most field names in camel case (for example: FirstName) * **SCMP** displays most field names with underscores (for example: first_name)                                                                                                                                                                                          |
   | Application          | Select one or more types of applications you want to include in the report. Leave blank to include all types.                                                                                                                                                                                                                                                                                                      |
   | Connection Method    | Select one or more connection methods used to perform the transaction that you want to include in the report. Leave blank to include all types. Available only for reports that include the Source field.                                                                                                                                                                                                          |
   | Payment Channel      | Select one or more payment channels to include in the report. After you make a selection, an information alert lists the [payment report fields](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/payment_method_fields.md "") associated with the selected payment channels. Leave blank to include all types.                                                           |
   | Field Selection      | One or more of the following: * Enter text matching a field name you want to find in the **Search** field. * Check the box for one or more fields or field types to include or remove from the report; check the **Select All** box to add or remove all fields. Click the **\^** in a section to expand or collapse it. * In the Selected column, click the **X** to remove a field or field type from the report |
   | Field Ordering       | To change the field order, click the up and down arrows or select a number in the Order drop-down menu. You can add or remove fields by clicking the plus and minus buttons. This option is only available for CSV output.                                                                                                                                                                                         |

8. When you are done, click **Create**. The Manage Report Subscription page appears, and the new subscription appears in the Custom Reports Subscriptions List.

Downloading Available Reports {#available_reports}
==================================================

The following types of downloadable reports are available in the `Business Center`, depending on your reporting history and usage:

* **Standard Reports**: contains reports based on pre-defined report subscriptions.
* **Custom Reports**: contains reports that the user has created or customized using a pre-defined report.
* **Classic Reports**: contains new reports that have been configured for you based on your legacy subscriptions.
* **Third-Party Reports**: contains any files from a third-party, typically your payment processor.
* **Legacy Reports**: contains an archive of your legacy reports.

A tab may be empty if there are no reports in that category to display.  
Refer to the "Classic Versus Legacy Reports" section in the [Reporting Migration Guide](https://developer.example.com/library/documentation/dev_guides/reporting_and_reconciliation/Reporting_Migration.pdf "") for more information.  
To download available reports:

1. On the left navigation pane, click the **`Reports`** icon.{#available_reports_avail-reports-step1}
   {#available_reports_avail-reports-step1}
2. Under Downloadable Reports, click **`Available Reports`** . The `Available Reports` page appears.{#available_reports_avail-reports-step2}
   {#available_reports_avail-reports-step2}
3. Under Downloadable Reports, click **`Available Reports`** . The `Available Reports` page appears.{#available_reports_avail-reports-step3}
   {#available_reports_avail-reports-step3}
4. In the Download column, click the file format link. Only reports that have successfully finished generating and that contain data include links.{#available_reports_avail-reports-step4}
   {#available_reports_avail-reports-step4}
5. Follow your browser's instructions to open and save the file.{#available_reports_avail-reports-step5}
   {#available_reports_avail-reports-step5}

Generating Custom Reports {#generate_custom_report}
===================================================

The `Business Center` enables you to create your own reports based on the type of data you want to track (for example, transaction requests or invoice summaries). When you create a report subscription, the `Business Center` provides a set of fields for you to choose from; you can also add and remove additional fields based on your needs, and choose the order in which they appear and how they display in the report. You can also set how often you want to generate the report (or if you want to just run it once). Successfully generated reports appear in the [`Available Reports`](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/available_reports.md "") section.  
To create a custom report subscription, create a brand [new subscription](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/create.md ""), or [save an existing](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/save_existing_as_new.md "") standard or custom report as a new report.  
Refer to [Application Fields](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/app_fields.md "") for a complete list of fields and descriptions.

Supported Time Zones {#time-zones}
==================================

This table lists the supported values for specifying a time zone. When using the `Business Center`, select the applicable time zone from the values listed in the `Business Center` column. When sending an API request, set the field to a value listed in the API column.

| `Business Center`                                                    | API                     |
|:---------------------------------------------------------------------|:------------------------|
| Africa/Cairo - (GMT+02:00) Eastern European Time                     | `Africa/Cairo`          |
| Africa/Johannesburg - (GMT+02:00) South Africa Standard Time         | `Africa/Johannesburg`   |
| Africa/Tripoli - (GMT+02:00) Eastern European Time                   | `Africa/Tripoli`        |
| Africa/Tunis - (GMT+01:00) Central European Time                     | `Africa/Tunis`          |
| America/Anchorage - (GMT-09:00) Alaska Standard Time                 | `America/Anchorage`     |
| America/Bogota - (GMT-05:00) Colombia Time                           | `America/Bogota`        |
| America/Buenos_Aires - (GMT-03:00) Argentine Time                    | `America/Buenos_Aires`  |
| America/Chicago - (GMT-06:00) Central Standard Time                  | `America/Chicago`       |
| America/Denver - (GMT-07:00) Mountain Standard Time                  | `America/Denver`        |
| America/Edmonton - (GMT-07:00) Mountain Standard Time                | `America/Edmonton`      |
| America/Godthab - (GMT-03:00) Western Greenland Time                 | `America/Godthab`       |
| America/Halifax - (GMT-04:00) Atlantic Standard Time                 | `America/Halifax`       |
| America/Indianapolis - (GMT-05:00) Eastern Standard Time             | `America/Indianapolis`  |
| America/La_Paz - (GMT-04:00) Bolivia Time                            | `America/La_Paz`        |
| America/Los_Angeles - (GMT-08:00) Pacific Standard Time              | `America/Los_Angeles`   |
| America/Mexico_City - (GMT-06:00) Central Standard Time              | `America/Mexico_City`   |
| America/New_York - (GMT-05:00) Eastern Standard Time                 | `America/New_York`      |
| America/Noronha - (GMT-02:00) Fernando de Noronha Time               | `America/Noronha`       |
| America/Phoenix - (GMT-07:00) Mountain Standard Time                 | `America/Phoenix`       |
| America/Sao_Paulo - (GMT-03:00) Brasilia Time                        | `America/Sao_Paulo`     |
| America/St_Johns - (GMT-03:30) Newfoundland Standard Time            | `America/St_Johns`      |
| America/Vancouver - (GMT-08:00) Pacific Standard Time                | `America/Vancouver`     |
| America/Winnipeg - (GMT-06:00) Central Standard Time                 | `America/Winnipeg`      |
| Asia/Baku - (GMT+04:00) Azerbaijan Time                              | `Asia/Baku`             |
| Asia/Bangkok - (GMT+07:00) Indochina Time                            | `Asia/Bangkok`          |
| Asia/Calcutta - (GMT+05:30) India Standard Time                      | `Asia/Calcutta`         |
| Asia/Dacca - (GMT+06:00) Bangladesh Time                             | `Asia/Dacca`            |
| Asia/Dubai - (GMT+04:00) Gulf Standard Time                          | `Asia/Dubai`            |
| Asia/Hong_Kong - (GMT+08:00) Hong Kong Time                          | `Asia/Hong_Kong`        |
| Asia/Jakarta - (GMT+07:00) West Indonesia Time                       | `Asia/Jakarta`          |
| Asia/Jerusalem - (GMT+02:00) Israel Standard Time                    | `Asia/Jerusalem`        |
| Asia/Katmandu - (GMT+05:45) Nepal Time                               | `Asia/Katmandu`         |
| Asia/Kuala_Lumpur - (GMT+08:00) Malaysia Time                        | `Asia/Kuala_Lumpur`     |
| Asia/Macao - (GMT+08:00) China Standard Time                         | `Asia/Macao`            |
| Asia/Magadan - (GMT+11:00) Magadan Time                              | `Asia/Magadan`          |
| Asia/Manila - (GMT+08:00) Philippines Time                           | `Asia/Manila`           |
| Asia/Rangoon - (GMT +06:30) Myanmar Standard Time                    | `Asia/Rangoon`          |
| Asia/Riyadh - (GMT+03:00) Arabia Standard Time                       | `Asia/Riyadh`           |
| Asia/Saigon - (GMT+07:00) Indochina Time                             | `Asia/Saigon`           |
| Asia/Seoul - (GMT+09:00) Korea Standard Time                         | `Asia/Seoul`            |
| Asia/Shanghai - (GMT+08:00) China Standard Time                      | `Asia/Shanghai`         |
| Asia/Singapore - (GMT+08:00) Singapore Time                          | `Asia/Singapore`        |
| Asia/Taipei - (GMT+08:00) China Standard Time                        | `Asia/Taipei`           |
| Asia/Tbilisi - (GMT+04:00) Georgia Time                              | `Asia/Tbilisi`          |
| Asia/Tokyo - (GMT+09:00) Japan Standard Time                         | `Asia/Tokyo`            |
| Asia/Yakutsk - (GMT+09:00) Yakutsk Time                              | `Asia/Yakutsk`          |
| Atlantic/Cape_Verde - (GMT-01:00) Cape Verde Time                    | `Atlantic/Cape_Verde`   |
| Australia/Adelaide - (GMT+09:30) Australian Central Standard Time    | `Australia/Adelaide`    |
| Australia/Brisbane - (GMT+10:00) Australian Eastern Standard Time    | `Australia/Brisbane`    |
| Australia/Broken_Hill - (GMT+09:30) Australian Central Standard Time | `Australia/Broken_Hill` |
| Australia/Darwin - (GMT+09:30) Australian Central Standard Time      | `Australia/Darwin`      |
| Australia/Eucla - (GMT+08:45) Australian Western Standard Time       | `Australia/Eucla`       |
| Australia/Hobart - (GMT+10:00) Australian Eastern Standard Time      | `Australia/Hobart`      |
| Australia/Lindeman - (GMT+10:00) Australian Eastern Standard Time    | `Australia/Lindeman`    |
| Australia/Lord_Howe - (GMT+10:30) Lord Howe Standard Time            | `Australia/Lord_Howe`   |
| Australia/Melbourne - (GMT+10:00) Australian Eastern Standard Time   | `Australia/Melbourne`   |
| Australia/Perth - (GMT+08:00) Australian Western Standard Time       | `Australia/Perth`       |
| Australia/Sydney - (GMT+10:00) Australian Eastern Standard Time      | `Australia/Sydney`      |
| Europe/Amsterdam - (GMT+01:00) Central European Time                 | `Europe/Amsterdam`      |
| Europe/Athens - (GMT+02:00) Eastern European Time                    | `Europe/Athens`         |
| Europe/Belgrade - (GMT+01:00) Central European Time                  | `Europe/Belgrade`       |
| Europe/Berlin - (GMT+01:00) Central European Time                    | `Europe/Berlin`         |
| Europe/Brussels - (GMT+01:00) Central European Time                  | `Europe/Brussels`       |
| Europe/Bucharest - (GMT+02:00) Eastern European Time                 | `Europe/Bucharest`      |
| Europe/Budapest - (GMT+01:00) Central European Time                  | `Europe/Budapest`       |
| Europe/Copenhagen - (GMT+01:00) Central European Time                | `Europe/Copenhagen`     |
| Europe/Dublin - (GMT+00:00) Greenwich Mean Time                      | `Europe/Dublin`         |
| Europe/Helsinki - (GMT+02:00) Eastern European Time                  | `Europe/Helsinki`       |
| Europe/Istanbul - (GMT+02:00) Eastern European Time                  | `Europe/Istanbul`       |
| Europe/Lisbon - (GMT+00:00) Western European Time                    | `Europe/Lisbon`         |
| Europe/London - (GMT+00:00) Greenwich Mean Time                      | `Europe/London`         |
| Europe/Madrid - (GMT+01:00) Central European Time                    | `Europe/Madrid`         |
| Europe/Malta - (GMT+01:00) Central European Time                     | `Europe/Malta`          |
| Europe/Minsk - (GMT+03:00) Moscow Standard Time                      | `Europe/Minsk`          |
| Europe/Monaco - (GMT+01:00) Central European Time                    | `Europe/Monaco`         |
| Europe/Moscow - (GMT+03:00) Moscow Standard Time                     | `Europe/Moscow`         |
| Europe/Oslo - (GMT+01:00) Central European Time                      | `Europe/Oslo`           |
| Europe/Paris - (GMT+01:00) Central European Time                     | `Europe/Paris`          |
| Europe/Prague - (GMT+01:00) Central European Time                    | `Europe/Prague`         |
| Europe/Riga - (GMT+02:00) Eastern European Time                      | `Europe/Riga`           |
| Europe/Rome - (GMT+01:00) Central European Time                      | `Europe/Rome`           |
| Europe/Stockholm - (GMT+01:00) Central European Time                 | `Europe/Stockholm`      |
| Europe/Vienna - (GMT+01:00) Central European Time                    | `Europe/Vienna`         |
| Europe/Warsaw - (GMT+01:00) Central European Time                    | `Europe/Warsaw`         |
| Europe/Zurich - (GMT+01:00) Central European Time                    | `Europe/Zurich`         |
| GMT - (GMT+00:00) Greenwich Mean Time                                | `GMT`                   |
| Pacific/Auckland - (GMT+12:00) New Zealand Standard Time             | `Pacific/Auckland`      |
| Pacific/Honolulu - (GMT-10:00) Hawaii Standard Time                  | `Pacific/Honolulu`      |
| Pacific/Norfolk - (GMT+11:00) Norfolk Time                           | `Pacific/Norfolk`       |
| Pacific/Pago_Pago - (GMT-11:00) Samoa Standard Time                  | `Pacific/Pago_Pag`      |
[Time Zones]

Saving Existing Reports as New Subscriptions {#save_existing_as_new}
====================================================================

You can choose to save any existing custom report as a new one; this enables you to copy over all the existing values, and change as much as you need to create a new report with a new name.  
To create a new report or subscription based on an existing report:

1. On the left navigation pane, click the **`Reports`** icon.

2. Under Downloadable Reports, click **`Report Subscription Management`** . The `Report Subscription Management` page appears.

3. Click the **Custom Report Subscriptions** tab. The Custom Reports Subscriptions List appears.

4. Next to the report you want to copy, click the **Save As** ( ![](/content/dam/documentation/pgw/en-us/olh/Reports/images/saveas.png/jcr:content/renditions/original) ) icon. The Save New Subscription page appears.

5. Under Account Setup, select whether to base the report on data from a specific merchant, or a group of merchants, and then choose an available value in the Merchants or Groups list.

   #### ADDITIONAL INFORMATION

   To create a report that includes all merchants or groups, use the default value.

6. Under Basic Report Setup, enter a unique name for the report.

   #### ADDITIONAL INFORMATION

   All reports must have a unique name.

7. Use the steps in [Creating New Custom Report Subscriptions](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/create.md "") as a guideline for modifying report values.

   #### ADDITIONAL INFORMATION

   > IMPORTANT You must change at least value to save the new report.

8. When you are done, click **Save As**. The Manage Report Subscription page appears, and the new subscription appears in the Custom Reports Subscriptions List.

Generating One-Time Reports {#generate_one-time_report}
=======================================================

The `Business Center` enables you to create your own reports when your needs don't require an ongoing subscription. A one-time report might be useful when:

* You need information about transactions that happened before you set up your recurring subscription.
* You want to test a report before [setting up a recurring subscription](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/generate_custom_report.md "").
* You need a particular type of information only one time, so a recurring subscription is unnecessary.

When you need past information that spans more than 31 days, you can create multiple one-time reports. In order to protect system performance, each user is able to generate up to three one-time reports concurrently. Additional one-time reports can be scheduled after the first three reports complete.  
After your one-time report is generated, it is available for download on the [`Available Reports`](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/available_reports.md "") page. Depending on the size of the report, it might take longer than 6 hours to generate.  
The process for creating a report subscription is the same as for creating a one-time report. The steps listed below focus on creating a one-time report; to follow steps specifically for creating custom subscriptions, see [Creating New Custom Report Subscriptions](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/create.md "")  
To generate a one-time report:

1. On the left navigation pane, click the **`Reports`** icon.

2. Under Downloadable Reports, click **`Available Reports`** . The `Available Reports` page appears.

3. On the Custom Reports tab, click **Create Report**. The Create Report Subscription page appears.

4. Under Account Setup, select whether to base the report on data from a specific merchant, or a group of merchants, and then choose an available value in the Merchants or Groups list.

   #### ADDITIONAL INFORMATION

   This option is only available for partners and account level users. To create a report that includes all merchants or groups, use the default value.

5. Under Basic Report Setup, enter the following:

   1. In the **Report Name** field, enter the name for your report that best reflects the data you want to capture. Each report must have a unique name containing up to 250 characters.
   2. In the **Report Type** field, select the type of report that most closely represents the data or process you want to include. The `Business Center` automatically includes the most commonly used fields in your report based on this selection. See the next step for more information on how to customize these values
   3. In the **File Format** field, choose whether the `Business Center` creates the report in XLS or XML format.
   4. In the **Frequency** field, choose **One-time report** to create a single report covering the date range (and time zone) you choose. You can also select a [Recurring subscription](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/create.md ""). For information about supported time zones, see [Supported Time Zones](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/time-zones.md "").
6. To change any of the default fields included in your report, click the **Arrow** icon to expand the Advanced Report Features section, and then perform one or more of the following actions (available actions are based on the services you use):

   | In this field or tab |                                                                                                                                                                                                      Do this                                                                                                                                                                                                      |
   |----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | Credit Amounts       | Check the box if you want credits to appear as negative amounts (for example: -1390.00)                                                                                                                                                                                                                                                                                                                           |
   | Naming Convention    | Select how you want the field names to appear in the report: * **SOAPI** displays most field names in camel case (for example: FirstName) * **SCMP** displays most field names with underscores (for example: first_name)                                                                                                                                                                                         |
   | Application          | Select one or more types of applications you want to include in the report. Leave blank to include all types.                                                                                                                                                                                                                                                                                                     |
   | Field Selection      | One or more of the following: * Enter text matching a field name you want to find in the **Search** field * Check the box for one or more fields or field types to include or remove from the report; check the **Select All** box to add or remove all fields. Click the **\^** in a section to expand or collapse it. * In the Selected column, click the **X** to remove a field or field type from the report |
   | Field Ordering       | Click and hold the **Handle** icon to rearrange fields (in the **Selected** column on the Field Selection tab) into the order in which you want them to appear in the report. This option is only available for CSV output.                                                                                                                                                                                       |

7. When you are done, click **Create**. The Available Reports page appears, and the new report appears in the Custom Reports List.

Application Fields {#app_fields}
================================

Fields in this group prepend the field name with "Application:"

| Field Name | Description                                                          |
|------------|:---------------------------------------------------------------------|
| Name       | Name of application used.                                            |
| Rcode      | One-digit code indicating whether the entire request was successful. |
| Rflag      | One-word description of the result of the entire request.            |
| Rmsg       | Message that explains the \&lt;ics_flag\&gt; value.                  |
| ReasonCode | ---                                                                  |

Appendix: Application Types and ICS Services {#app_types_services}
==================================================================

|                 Application Type                 | ICS Service                       |
|--------------------------------------------------|:----------------------------------|
| Advanced Fraud Screen                            | ics_score                         |
| Alt Pay Sale                                     | ics_ap_sale                       |
| Credit Card Authorization                        | ics_auth                          |
| Credit Card Auto Full Authorization Reversal     | ics_auto_full_auth_reversal       |
| Credit Card System Authorization                 | ics_auth_refresh                  |
| Decision Manager                                 | ics_decision                      |
| Credit Card Decline                              | ics_decline                       |
| Credit Card Credit                               | ics_credit                        |
| Credit Card Settlement                           | ics_bill                          |
| Electronic Check Authenticate                    | ics_ecp_authenticate              |
| Electronic Check Credit                          | ics_ecp_debit                     |
| Electronic License Issue                         | ics_elc_reissue                   |
| Electronic License Revocation                    | ics_elc_revoke                    |
| FH Notification                                  | ics_notify                        |
| Gift Certificate Creation                        | ics_create_isv                    |
| Gift Certificate History                         | ics_create_history                |
| Gift Certificate Increase                        | ics_add_value_to_isv              |
| Gift Certificate Information                     | ics_get_isv_info                  |
| Gift Certificate Modification                    | ics_modify_isv                    |
| Gift Certificate Policies                        | ics_get_isv_profiles              |
| Gift Certificate Redemption                      | ics_redeem_isv                    |
| IP Geolocation                                   | ics_ipgeo                         |
| Customer List Modification                       | ics_risk_update                   |
| Product Export Verification                      | ics_export                        |
| Shipping Address Verification                    | ics_dav                           |
| Software Download URL                            | ics_download                      |
| Tax Calculation                                  | ics_tax                           |
| V.me Authorization                               | ics_vme_auth                      |
| V.me Payment                                     | ics_vme_bill                      |
| V.me Credit                                      | ics_vme_credit                    |
| V.me Auth Reversal                               | ics_vme_auth_reversal             |
| Denied Parties Check                             | ics_dpc                           |
| Download                                         | ics_get                           |
| SmartCert Download                               | ics_grover                        |
| Bank Transfer                                    | ics_bankxfr                       |
| Certificate Generation                           | ics_certgen                       |
| Rate Check                                       | ics_fxrates                       |
| Hotlist Check                                    | ics_hotlist                       |
| IFS Setup                                        | ics_ifs_setup                     |
| IFS Update                                       | ics_ifs_update                    |
| Payer Authentication Enrollment                  | ics_pa_enroll                     |
| Payer Authentication Validation                  | ics_pa_validate                   |
| Voided Transactions                              | ics_void                          |
| Alt Pay Initiate                                 | ics_ap_initiate                   |
| Alt Pay Service Status                           | ics_ap_check_status               |
| Alt Pay Refund                                   | ics_ap_refund                     |
| Get Checkout Details                             | ics_ap_checkout_details           |
| Get Transaction Details                          | ics_ap_transaction_details        |
| Confirm Purchase                                 | ics_ap_confirm_purchase           |
| Alt Pay Authorization                            | ics_ap_auth                       |
| Alt Pay Authorization Reversal                   | ics_ap_auth_reversal              |
| Alt Pay Capture                                  | ics_ap_capture                    |
| Alt Pay Refund                                   | ics_ap_vme_refund                 |
| Alt Pay Session                                  | ics_ap_sessions                   |
| Alt Pay Order                                    | ics_ap_order                      |
| Alt Pay Billing Agreement                        | ics_ap_billing_agreement          |
| Alt Pay Cancel                                   | ics_ap_cancel                     |
| Alt Pay Options                                  | ics_ap_options                    |
| Service Fee Authorization                        | ics_sfee_auth                     |
| Service Fee Bill                                 | ics_sfee_bill                     |
| Service Fee Calculation                          | ics_service_fee_calculate         |
| Service Fee Electronic Check Debit               | ics_sfee_ecp_debit                |
| Service Fee Authorization Rversal                | ics_sfee_auth_reversal            |
| V.me Europe Authorization                        | ics_auth_vme_eu                   |
| V.me Europe Authorization Reversal               | ics_auth_reversal_vme_eu          |
| Decrypt `Relay Click to Pay` Data                 | ics_decrypt_card_checkout_data    |
| Apple Pay Authorization                          | ics_auth_apple_pay                |
| Service Fee Authorization                        | ics_service_fee_auth              |
| Service Fee Authorization Reversal               | ics_service_fee_auth_reversal     |
| Service Fee Settlement                           | ics_service_fee_bill              |
| Service Fee Credit Card Credit                   | ics_service_fee_credit            |
| Service Fee eCheck Credit                        | ics_service_fee_ecp_credit        |
| Service Fee eCheck Debit                         | ics_service_fee_ecp_debit         |
| DCC Lookup                                       | ics_dcc                           |
| DCC Update                                       | ics_dcc_update                    |
| Direct Debit                                     | ics_direct_debit                  |
| Direct Debit Refund                              | ics_direct_debit_refund           |
| Direct Debit Mandate                             | ics_direct_debit_mandate          |
| Bank Transfer                                    | ics_bank_transfer                 |
| Bank Transfer Real Time                          | ics_bank_transfer_real_time       |
| Bank Transfer Refund                             | ics_bank_transfer_refund          |
| Subscription Creation                            | ics_pay_subscription_create       |
| Subscription Modification                        | ics_pay_subscription_update       |
| Subscription Delete                              | ics_pay_subscription_delete       |
| PayPal Payment Request                           | ics_paypal_payment                |
| PayPal Credit                                    | ics_paypal_credit                 |
| Direct Debit Validation                          | ics_direct_debit_validate         |
| PIN-less Debit                                   | ics_pinless_debit                 |
| PIN-less Debit Validation                        | ics_pinless_debit_validate        |
| PIN-less Debit Reversal                          | ics_pinless_debit_reversal        |
| PayPal Preapproved Payment                       | ics_paypal_preapproved_payment    |
| PayPal Button Create                             | ics_paypal_button_create          |
| PayPal Preapproved Update                        | ics_paypal_preapproved_update     |
| Subscription Payment Modification                | ics_pay_subscription_event_upd    |
| Subscription Payment Modification                | ics_pay_subscription_event_update |
| Subscription Retrieval                           | ics_pay_subscription_retrieve     |
| PayPal Express Checkout Do Payment               | ics_paypal_ec_do_payment          |
| PayPal Express Checkout Settlement               | ics_paypal_ec_do_capture          |
| PayPal Express Checkout Auth Reversal            | ics_paypal_auth_reversal          |
| PayPal Express Checkout Settlement               | ics_paypal_do_capture             |
| PayPal Express Checkout Set                      | ics_paypal_ec_set                 |
| PayPal Express Checkout Refund                   | ics_paypal_refund                 |
| PayPal Express Checkout Get Details              | ics_paypal_ec_get_details         |
| PayPal Express Checkout Order Setup              | ics_paypal_ec_order_setup         |
| PayPal Express Checkout Authorization            | ics_paypal_authorization          |
| PayPal Express Checkout Billing Agreement Create | ics_paypal_create_agreement       |
| PayPal Express Checkout Billing Agreement Update | ics_paypal_update_agreement       |
| PayPal Express Checkout Do Reference             | ics_paypal_do_ref_transaction     |
| PayPal Settlement                                | paypal_settlement                 |
| PayPal Get Transaction Details                   | ics_paypal_get_txn_details        |
| PayPal Transaction Search                        | ics_paypal_transaction_search     |
| PayPal Payment                                   | paypal_ipn                        |
| China Payment                                    | ics_china_payment                 |
| China Refund                                     | ics_china_refund                  |
| Boleto Payment                                   | ics_boleto_payment                |
| Case Management Action                           | ics_cm_action                     |
| Original Credit Transaction                      | ics_oct                           |
| Timeout OCT Reversal                             | ics_timeout_oct_reversal          |
| Apple Pay Authorization                          | ics_auth\|001                     |
| V.me Authorization                               | ics_ap_auth\|vme                  |
| V.me Authorization Reversal                      | ics_ap_auth_reversal\|vme         |
| V.me Payment                                     | ics_ap_capture\|vme               |
| V.me Refund                                      | ics_ap_refund\|vme                |
| V.me Europe Authorization                        | ics_auth\|vmeeu                   |
| V.me Europe Authorization Reversal               | ics_auth_reversal\|vmeeu          |
| Decision Manager Events                          | ics_dm_event                      |
| Timeout Auth Reversal                            | ics_timeout_auth_reversal         |
| PayPal Billing Agreement                         | paypal_mip_agreement_ipn          |
| Subscription Creation Duplicates                 | ics_pay_subscription_create_dup   |
| Acquirer Risk Controls                           | ics_arc                           |
| Android Pay Authorization                        | ics_auth\|006                     |
| Chase Pay Authorization                          | ics_auth\|007                     |
| Samsung Pay Authorization                        | ics_auth\|008                     |
| Recurring Payment                                | ics_recurring_payment             |
| Automatic Authorization Reversal                 | ics_auto_auth_reversal            |
| Get `Relay Click to Pay` Data                     | ics_get_card_checkout_data        |
| Get Masterpass Data                              | ics_get_masterpass_data           |
| PIN Debit Purchase                               | ics_pin_debit_purchase            |
| PIN Debit Credit                                 | ics_pin_debit_credit              |
| PIN Debit Reversal                               | ics_pin_debit_reversal            |
| PIN Debit Timeout Reversal                       | ics_timeout_pin_debit_reversal    |

Payment Method Fields {#payment_method_fields}
==============================================

Fields in this group prepend the field name with "PaymentMethod:"

| Field Name                     | Description                                                                                                                                                          |
|:-------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AccountSuffix                  | Last four digits of the customer's payment account number.                                                                                                           |
| PaymentMethod. BankAccountName | Bank's account name.                                                                                                                                                 |
| PaymentMethod.BankCode         | Bank's code. Used for some countries when you are not using the IBAN. Contact `Payment Gateway` customer support for required country-specific bank account information. |
| BoletoBarCodeNumber            | Numeric representation of the boleto barcode.                                                                                                                        |
| BoletoNumber                   | Boleto Bancário payment number.                                                                                                                                      |
| CardCategory                   | Type of card used.                                                                                                                                                   |
| CardCategoryCode               | Code for card type used.                                                                                                                                             |
| CardType                       | Type of card to authorize.                                                                                                                                           |
| CheckNumber                    | Check number.                                                                                                                                                        |
| ExpirationMonth                | Two-digit month in which the credit card expires.                                                                                                                    |
| ExpirationYear                 | Four-digit year in which the credit card expires.                                                                                                                    |
| IssueNumber                    | Number of times a Maestro (UK Domestic) card has been issued to the account holder.                                                                                  |
| MandateId                      | Identification reference for the direct debit mandate.                                                                                                               |
| MandateType                    | Type of mandate.                                                                                                                                                     |
| SignatureDate                  | Date of signature.                                                                                                                                                   |
| StartMonth                     | Month of the start of the Maestro (UK Domestic) card validity period.                                                                                                |
| StartYear                      | Year of the start of the Maestro (UK Domestic) card validity period.                                                                                                 |
| WalletType                     | Type of wallet.                                                                                                                                                      |

Creating New Custom Report Subscriptions {#create}
==================================================

A recurring report subscription is a template that describes the attributes of a report, including how often it runs and the period of time it spans. After your recurring report is generated, it is available for download on the [`Available Reports`](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/available_reports.md "") page. You can maintain up to 20 report subscriptions at any time.  
In addition to choosing from [available fields](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/app_fields.md ""), you can customize the following attributes of a recurring subscription:

* **Name**: a unique name for the report. The name cannot be changed after a report is created.
* **Report type**: a set of reports that can be customized. The report type cannot be changed after a report is created.
* **Format**: the format of a generated report (XML or CSV).
* **Frequency**: the frequency at which a report runs: daily, weekly, or monthly.
* **Start time**: the time of day at which a report runs.

The process for creating a report subscription is the same as for creating a one-time report. The steps listed below focus on creating recurring subscriptions.  
To create a report subscription:

1. On the left navigation pane, click the **`Reports`** icon.

2. Under Downloadable Reports, click **`Report Subscription Management`** . The `Report Subscription Management` page appears.

3. Click the **Custom Report Subscriptions** tab. The Custom Reports Subscriptions List appears.

4. Click **Create Subscription**. The Create Report Subscription page appears.

5. Under Account Setup, select whether to base the report on data from a specific merchant, or a group of merchants, and then choose an available value in the Merchants or Groups list.

   #### ADDITIONAL INFORMATION

   This option is only available for partners and account level users. To create a report that includes all merchants or groups, use the default value.

6. Under Basic Report Setup, enter the following:

   1. In the **Report Name** field, enter the name for your report that best reflects the data you want to capture. Each report must have a unique name containing up to 250 characters.
   2. In the **Report Type** field, select the type of report that most closely represents the data or process you want to include. The `Business Center` automatically includes the most commonly used fields in your report based on this selection. See the next step for more information on how to customize these values.
   3. In the **File Format** field, choose whether the `Business Center` creates the report in XLS or XML format.
   4. In the **Frequency** field, choose **Recurring subscription** to automatically generates daily, weekly, or monthly reports. You can also create a [One-time report](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/generate_one-time_report.md "").
7. To change any of the default fields included in your report, click the Arrow ( ![](/content/dam/documentation/pgw/en-us/olh/Reports/images/arrow.png/jcr:content/renditions/original) ) icon to expand the Advanced Report Features section, and then perform one or more of the following actions (available actions are based on the services you use):

   1. In the **Credit Amounts** field, check the box if you want credits to appear as negative amounts (for example: -1390.00)
   2. In the **Naming Convention** field, select how you want the field names to appear in the report: **SOAPI** displays most field names in camel case (for example: FirstName); **SCMP** displays most field names with underscores (for example: first_name).
   3. In the **Application** field, select one or more [types of applications](/docs/gateway/en-us/invoicing/developer/all/rest/invoicing/app_types_services.md "") you want to include in the report. Leave blank to include all types.
   4. In the **Field Selection** field, enter text matching a field name you want to find in the **Search** field, check the box for one or more fields or field types to include or remove from the report; check the **Select All** box to add or remove all fields. (Click the **\^** in a section to expand or collapse it.); and/or in the **Selected** column, click the **X** to remove a field or field type from the report
   5. In the **Field Ordering** field, click and hold the **Handle** icon to rearrange fields (in the **Selected** column on the Field Selection tab) into the order in which you want them to appear in the report
8. When you are done, click **Create**. The Manage Report Subscription page appears, and the new subscription appears in the Custom Reports Subscriptions List.

