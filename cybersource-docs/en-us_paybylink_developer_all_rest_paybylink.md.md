`Pay by Link` Developer Guide {#paybylink-about-guide}
======================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This guide is written for merchants who want to use the `Pay by Link` services. It describes tasks that a merchant must complete in order to create, send, and manage payment links and donation links using the `Pay by Link` API. It also describes how to set up automated webhook notifications when a payment link is used by a customer to make a payment. It is intended to help the merchant provide a seamless customer payment experience.

Conventions
:
This special statement is used in this document:

    > IMPORTANT
    > An *Important* statement contains information essential to successfully completing a task or learning a concept.

Customer Support
:
For support information about any service, visit the Support Center:

<http://support.example.com>

Recent Revisions to This Document {#paybylink-revisions}
========================================================

26.02.01
--------

Added new fields and values to customize the payment link payment page settings. See [Update Payment Link Settings](/docs/cybs/en-us/paybylink/developer/all/rest/paybylink/paybylink-services/paybylink-services-update-settings-intro.md "").

26.01.01
--------

This revision contains only editorial changes and no technical updates.

25.11.01
--------

Added a note about personally identifying information in `Pay by Link` fields. See [Introduction to Pay by Link](/docs/cybs/en-us/paybylink/developer/all/rest/paybylink/paybylink-intro.md "").

25.04.02
--------

Added information about how to deactivate and activate a payment link using the status request field. See [Update a Fixed-Price Link](/docs/cybs/en-us/paybylink/developer/all/rest/paybylink/paybylink-services/paybylink-update-intro.md "") and [Update a Customer-Set Link](/docs/cybs/en-us/paybylink/developer/all/rest/paybylink/paybylink-services/paybylink-update-customer-intro.md "").  
Added information about how to create Token Management Service (TMS) tokens from `Pay by Link` transactions using Transaction Management in the `Business Center`. See [Introduction to Pay by Link](/docs/cybs/en-us/paybylink/developer/all/rest/paybylink/paybylink-intro.md "").

25.04.01
--------

This revision contains only editorial changes and no technical updates.

24.08.01
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

Introduction to `Pay by Link` {#paybylink-intro}
================================================

`Pay by Link` is an easy and fast way to securely sell products or receive donations online. You can send and display a secure payment link across physical and digital marketing. This solution is ideal for distributing the same payment link to multiple customers.  
Integrate `Pay by Link` APIs into your own system to automate the creation and management of payment links. Links for making purchases are referred to as *fixed-price links* , and links for making donations are referred to as *customer-set price links*.

**Benefits**
:
`Pay by Link` enables you to:

    * Get started with a fast and easy setup.
    * Grow your business and revenue through multiple sales channels.
    * Offer customers the convenience of popular payment options.
    * Get paid from any connected device: mobile, tablet, and desktop.
    * Reduce chargebacks and fraud through easy integration with Decision Manager or Fraud Management Essentials.
    * Maintain PCI security and compliance, and minimize future PCI scoping.

**Requirements**
:
Before you can begin using `Pay by Link`, your merchant account must be enabled for Unified Checkout. If you are a merchant, contact your sales representative for more information.

    If you are a portfolio user, you can use the `Business Center` to board and enable your merchants for Unified Checkout and `Pay by Link`. For more information, see the [`Pay by Link`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/templates-matrix-intro/templates-matrix-pay-by-link.md "") section in the *Boarding User Guide*.

    To access `Pay by Link` in the `Business Center`, see [Using the Business Center](/docs/cybs/en-us/paybylink/developer/all/rest/paybylink/paybylink-ebc-intro.md "").

    > IMPORTANT  
    > ` Pay by Link ` fields are strictly designated for non-personal data and must not be used to capture personally identifying information. You are prohibited from capturing, obtaining, or transmitting any personally identifying information in or through any ` Pay by Link ` fields, including merchant-defined data fields.  
    > Personally identifying information includes, but is not limited to, address, payment card number, social security number, driver's license number, state-issued identification number, passport number, and card verification numbers (CVV, CVC2, CVV2, CID, CVN). In the event it is discovered that a merchant is capturing and/or transmitting personally identifying information, whether or not intentionally, the merchant's account is immediately suspended, which results in a rejection of any and all transaction requests submitted by the merchant after the point of suspension.

Tokenization for Merchant-Initiated Transactions
------------------------------------------------

You can create Token Management Service (TMS) tokens from `Pay by Link` transactions using Transaction Management in the `Business Center`.

> IMPORTANT
> If you create and use TMS tokens for merchant-initiated transactions (MITs), you must comply with the **Consent Agreement Provisions** as stated in the [*Improving Authorization Management for Transactions with Stored Credentials*](https://usa.relay.com/dam/VCOM/global/support-legal/documents/stored-credential-transaction-framework-vbs-10-may-17.pdf "") guide.

`Pay by Link` API Requests {#paybylink-services}
================================================

This section describes how to create and manage payment links using the `REST API`.

Create a Fixed-Price Link {#paybylink-create-intro}
===================================================

Use the information in this section to create fixed-price links that you can send or display to your customers. Your customers can then use the links to pay on a secure `Cybersource` hosted website.  
Fixed-price links are typically used by customers to make purchases. To create a link for donations, see [Create a Customer-Set Link](/docs/cybs/en-us/paybylink/developer/all/rest/paybylink/paybylink-services/paybylink-create-customer-intro.md "").

Partner Information {#paybylink-create-intro_partner-info}
----------------------------------------------------------

If your merchant account is associated with a `Cybersource` partner, you can include your partner solution ID (PSID) in the request for tracking and reporting purposes. To submit your PSID, include the clientReferenceInformation.partner.solutionId request field, and set its field value to your PSID.

Endpoints {#paybylink-create-intro_endpoint}
--------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/ipl/v2/payment-links/`{#paybylink-create-intro_endpoint-create-prod}  
**Test:** `POST ``https://apitest.cybersource.com``/ipl/v2/payment-links/`{#paybylink-create-intro_endpoint-create-test}  
**India Production:** `POST ``https://api.in.cybersource.com``/ipl/v2/payment-links/`{#paybylink-create-intro_endpoint-create-india}

Required Fields for Creating a Fixed-Price Link {#paybylink-create-req-fields}
==============================================================================

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

processingInformation.linkType
:
Set to `PURCHASE`.

purchaseInformation.purchaseNumber
:
Set to a unique identifier for the fixed-price link.
{#paybylink-create-req-fields_payment-link}

Optional Fields for Creating a Fixed-Price Link {#paybylink-create-opt-fields}
==============================================================================

[clientReferenceInformation.partner.developerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
Set to your developer ID.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
Set to your partner solution ID (PSID).

orderInformation.amountDetails.maxAmount
:

orderInformation.amountDetails.minAmount
:

[orderInformation.lineItems\[\].productDescription](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-description.md "")
:

[orderInformation.lineItems\[\].productSku](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-sku.md "")
:

[orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

processingInformation.requestPhone
:

processingInformation.requestShipping
:

{#paybylink-create-opt-fields_opt-fields}

`REST` Example: Creating a Fixed-Price Link {#paybylink-create-ex-rest}
=======================================================================

Request

```
{
    "processingInformation": {
        "linkType": "PURCHASE"
    },
    "purchaseInformation": {
        "purchaseNumber": "78759658468578"
    },
    "orderInformation": {
        "amountDetails": {
            "currency": "USD",
            "totalAmount": "60"
        },
        "lineItems": [
            {
                "productName": "Birthday Cake",
                "unitPrice": "60"
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
      "href": "/ipl/v2/payment-links/78795658468578",
      "method": "GET"
    },
    "update": {
      "href": "/ipl/v2/payment-links/78795658468578",
      "method": "PATCH"
    }
  },
  "id": "78795658468578",
  "submitTimeUtc": "2024-08-08T02:27:28.287601279Z",
  "status": "ACTIVE",
  "processingInformation": {
    "linkType": "PURCHASE",
    "requestPhone": false,
    "requestShipping": false
  },
  "purchaseInformation": {
    "purchaseNumber": "78795658468578",
    "createdDate": "2024-08-08T02:27:28.370",
    "paymentLink": "https://businesscenter.cybersource.com/payByLink/pay/IXBls1OJVqRiiv0SL8XjHit0InRBW844eEou2EWBCNP7WIGDdd8tjKN07Ep3MaQD"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 60,
      "currency": "USD"
    },
    "lineItems": [
      {
        "productName": "Birthday Cake",
        "unitPrice": 60,
        "quantity": 1
      }
    ]
  }
}
```

Create a Customer-Set Link {#paybylink-create-customer-intro}
=============================================================

Use the information in this section to create customer-set price links that you can send or display to your customers. Your customers can then use the link to pay on a secure `Cybersource`-hosted website.  
Customer-set links are typically used to make donations. To create a link for customers to make purchases, see [Create a Fixed-Price Link](/docs/cybs/en-us/paybylink/developer/all/rest/paybylink/paybylink-services/paybylink-create-intro.md "").

Partner Information
-------------------

If your merchant account is associated with a `Cybersource` partner, you can include your partner solution ID (PSID) in the request for tracking and reporting purposes. To submit your PSID, include the clientReferenceInformation.partner.solutionId request field, and set its field value to your PSID.

Endpoints
---------

**Production:** `POST ``https://api.cybersource.com``/ipl/v2/payment-links/`{#paybylink-create-customer-intro_d15e58}  
**Test:** `POST ``https://apitest.cybersource.com``/ipl/v2/payment-links/`{#paybylink-create-customer-intro_d15e68}  
**India Production:** `POST ``https://api.in.cybersource.com``/ipl/v2/payment-links/`{#paybylink-create-customer-intro_d15e78}

Required Fields for Creating a Customer-Set Link {#paybylink-create-customer-req-fields}
========================================================================================

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

orderInformation.amountDetails.minAmount
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

processingInformation.linkType
:
Set to `DONATION`.

purchaseInformation.purchaseNumber
:
Set to a unique identifier for the customer-set price link.
{#paybylink-create-customer-req-fields_rest-customer-set-fields}

Optional Fields for Creating a Customer-Set Link {#paybylink-create-opt-customer-fields}
========================================================================================

[clientReferenceInformation.partner.developerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
Set to your developer ID.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
Set to your partner solution ID (PSID).

orderInformation.amountDetails.maxAmount
:

orderInformation.amountDetails.minAmount
:

[orderInformation.lineItems\[\].productDescription](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-description.md "")
:

[orderInformation.lineItems\[\].productSku](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-sku.md "")
:

[orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

processingInformation.requestPhone
:

processingInformation.requestShipping
:

`REST` Example: Creating a Customer-Set Price Link {#paybylink-create-don-ex-rest}
==================================================================================

Request

```
{
    "processingInformation": {
        "linkType": "DONATION"
    },
    "purchaseInformation": {
        "purchaseNumber": "68435461384354384836"
    },
    "orderInformation": {
        "amountDetails": {
            "minAmount": "1",
            "currency": "USD",
            "totalAmount": "1"
        },
        "lineItems": [
            {
                "productName": "Fundraiser",
                "unitPrice": "1"
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
      "href": "/ipl/v2/payment-links/68435461384354384836",
      "method": "GET"
    },
    "update": {
      "href": "/ipl/v2/payment-links/68435461384354384836",
      "method": "PATCH"
    }
  },
  "id": "68435461384354384836",
  "submitTimeUtc": "2024-08-08T14:51:16.505077155Z",
  "status": "ACTIVE",
  "processingInformation": {
    "linkType": "DONATION",
    "requestPhone": false,
    "requestShipping": false
  },
  "purchaseInformation": {
    "purchaseNumber": "68435461384354384836",
    "createdDate": "2024-08-08T14:51:16.523",
    "paymentLink": "https://businesscenter.cybersource.com/payByLink/pay/nQpuAeme4aRwucfJtAq8AyLwdUjcWRGdhGAyPrLmIh0LGDaW4hvdnHCqf1lSRUJV"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 1,
      "currency": "USD",
      "minAmount": 1
    },
    "lineItems": [
      {
        "productName": "123654"
      }
    ]
  }
}
```

Update a Fixed-Price Link {#paybylink-update-intro}
===================================================

Use the information in this section to update a fixed-price link, such as modifying the billing information for your customers if their billing information changes. When sending an update request, include all of the fields from the original request to create the link. If you exclude a field, the information corresponding to that field is removed from the updated payment page.

Deactivate a Payment Link {#paybylink-update-intro_deactive}
------------------------------------------------------------

You can deactivate a payment link to no longer allow your customers to use the link. To do this, include the status field in your update request and set it to `INACTIVE`. If you want to activate the payment link again, you can send your update request with the status field set to `ACTIVE`.

Endpoints {#paybylink-update-intro_endpoint}
--------------------------------------------

**Production:** `PATCH ``https://api.cybersource.com``/ipl/v2/payment-links/`*{id}*  
**Test:** `PATCH ``https://apitest.cybersource.com``/ipl/v2/payment-links/`*{id}*  
**India Production:** `PATCH ``https://api.in.cybersource.com``/ipl/v2/payment-links/`*{id}*  
Set the *{id}* to the payment number ID contained in the create payment link response.

Required Fields for Updating a Fixed-Price Link {#paybylink-update-req-fields}
==============================================================================

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

processingInformation.linkType
:
Set to `PURCHASE`.

Optional Fields for Updating a Fixed-Price Link {#paybylink-update-opt-fields}
==============================================================================

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
Set to your partner solution ID (PSID).

orderInformation.amountDetails.maxAmount
:

orderInformation.amountDetails.minAmount
:

[orderInformation.lineItems\[\].productDescription](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-description.md "")
:

[orderInformation.lineItems\[\].productSku](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-sku.md "")
:

[orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

processingInformation.requestPhone
:

processingInformation.requestShipping
:

purchaseInformation.purchaseNumber
:
Set to a unique identifier for the payment link.

[status](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/status-a.md "")
:
Include this field to activate or deactivate a payment link.
:
Set to one of these values:

    * `ACTIVE`: The payment link is usable to complete a payment.
    * `INACTIVE`: The payment link is not usable to complete a payment.

`REST` Example: Updating a Fixed-Price Link {#paybylink-update-ex-rest}
=======================================================================

Request

```
{
    "processingInformation": {
        "linkType": "PURCHASE"
    },
    "orderInformation": {
        "amountDetails": {
            "currency": "USD",
            "totalAmount": "75"
        },
        "lineItems": [
            {
                "productName": "Birthday Cake",
                "unitPrice": "75"
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
      "href": "/ipl/v2/payment-links/78759658968978",
      "method": "GET"
    },
    "update": {
      "href": "/ipl/v2/payment-links/78759658968978",
      "method": "PATCH"
    }
  },
  "id": "78759658968978",
  "submitTimeUtc": "2024-08-15T21:11:46.163224519Z",
  "status": "ACTIVE",
  "processingInformation": {
    "linkType": "PURCHASE",
    "requestPhone": false,
    "requestShipping": false
  },
  "purchaseInformation": {
    "purchaseNumber": "78759658968978",
    "createdDate": "2024-08-15T21:08:24.593",
    "paymentLink": "https://businesscenter.cybersource.com/payByLink/pay/e1PxwGdhJWtz3MBXCE7DvuXoYlT7G0I2kyb3gRrQY6bLWbH5769guEPlUri2z7Kc"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 75,
      "currency": "USD"
    },
    "lineItems": [
      {
        "productName": "Birthday Cake",
        "unitPrice": 75,
        "quantity": 1
      }
    ]
  }
}
```

Update a Customer-Set Link {#paybylink-update-customer-intro}
=============================================================

Use the information in this section to update customer-set links to modify the information set in the original link, such as the price amount. When sending an update request, include all of the fields from the original request to create the link. If you exclude a field, the information corresponding to that field is removed from the updated payment page.

Deactivate a Payment Link
-------------------------

You can deactivate a payment link to no longer allow your customers to use the link. To do this, include the status field in your update request and set it to `INACTIVE`. If you want to activate the payment link again, you can send your update request with the status field set to `ACTIVE`.

Endpoints
---------

**Production:** `PATCH ``https://api.cybersource.com``/ipl/v2/payment-links/`*{id}*  
**Test:** `PATCH ``https://apitest.cybersource.com``/ipl/v2/payment-links/`*{id}*  
**India Production:** `PATCH ``https://api.in.cybersource.com``/ipl/v2/payment-links/`*{id}*  
Set the *{id}* to the payment number ID contained in the create payment link response.

Required Fields for Updating a Customer-Set Link {#paybylink-update-customer-req-fields}
========================================================================================

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

orderInformation.amountDetails.minAmount
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

processingInformation.linkType
:
Set to `DONATION`.

purchaseInformation.purchaseNumber
:
Set to a unique identifier for the customer-set price link.

Optional Fields for Updating a Customer-Set Link {#paybylink-update-customer-opt-fields}
========================================================================================

[clientReferenceInformation.partner.developerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
Set to your developer ID.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
Set to your partner solution ID (PSID).

orderInformation.amountDetails.maxAmount
:

orderInformation.amountDetails.minAmount
:

[orderInformation.lineItems\[\].productDescription](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-description.md "")
:

[orderInformation.lineItems\[\].productSku](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-sku.md "")
:

[orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

processingInformation.requestPhone
:

processingInformation.requestShipping
:

[status](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/status-a.md "")
:
Include this field to activate or deactivate a payment link.
:
Set to one of these values:

    * `ACTIVE`: The payment link is usable to complete a payment.
    * `INACTIVE`: The payment link is not usable to complete a payment.

`REST` Example: Updating a Customer-Set Price Link {#paybylink-update-don-ex-rest}
==================================================================================

Request

```
{
    "processingInformation": {
        "linkType": "DONATION"
    },
    "orderInformation": {
        "amountDetails": {
            "minAmount": "1",
            "currency": "USD",
            "totalAmount": "5"
        },
        "lineItems": [
            {
                "productName": "Fundraiser",
                "unitPrice": "5"
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
      "href": "/ipl/v2/payment-links/78759658968978",
      "method": "GET"
    },
    "update": {
      "href": "/ipl/v2/payment-links/78759658968978",
      "method": "PATCH"
    }
  },
  "id": "78759658968978",
  "submitTimeUtc": "2024-08-15T21:11:46.163224519Z",
  "status": "ACTIVE",
  "processingInformation": {
    "linkType": "DONATION",
    "requestPhone": false,
    "requestShipping": false
  },
  "purchaseInformation": {
    "purchaseNumber": "78759658968978",
    "createdDate": "2024-08-15T21:08:24.593",
    "paymentLink": "https://businesscenter.cybersource.com/payByLink/pay/e1PxwGdhJWtz3MBXCE7DvuXoYlT7G0I2kyb3gRrQY6bLWbH5769guEPlUri2z7Kc"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 5,
      "currency": "USD"
    },
    "lineItems": [
      {
        "productName": "Fundraiser",
        "unitPrice": 5,
        "quantity": 1
      }
    ]
  }
}
```

Get Link {#paybylink-get-intro}
===============================

Use the information in this section to retrieve a payment link. Send a request with the purchase number included in the endpoint. The purchase number was the field value used in the purchaseInformation.purchaseNumber request field to create the link.

Endpoints
---------

**Production:** `GET ``https://api.cybersource.com``/ipl/v2/payment-links/`*{id}*  
**Test:** `GET ``https://apitest.cybersource.com``/ipl/v2/payment-links/`*{id}*  
**India Production:** `GET ``https://api.in.cybersource.com``/ipl/v2/payment-links/`*{id}*  
Set the *{id}* to the payment number ID contained in the create payment link response.

`REST` Example: Retrieving a Payment Link {#paybylink-get-ex-rest}
==================================================================

Request

```
{}
```

Response to a Successful Request

```keyword
{
  "_links": {
    "self": {
      "href": "/ipl/v2/payment-links/787596584685788",
      "method": "GET"
    },
    "update": {
      "href": "/ipl/v2/payment-links/787596584685788",
      "method": "PATCH"
    }
  },
  "id": "787596584685788",
  "submitTimeUtc": "2024-08-09T19:57:03.694276330Z",
  "status": "ACTIVE",
  "processingInformation": {
    "linkType": "PURCHASE",
    "requestPhone": false,
    "requestShipping": false
  },
  "purchaseInformation": {
    "purchaseNumber": "787596584685788",
    "createdDate": "2024-08-09T19:56:02.463",
    "paymentLink": "https://businesscenter.cybersource.com/payByLink/pay/DpabIRBmi5nGTQEFMAjBhSHUg2o0VMy0Hde2QxMGZ6PUmTZt6HzEElcuweu6pTre"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": 60,
      "currency": "USD"
    },
    "lineItems": [
      {
        "productName": "Birthday Cake",
        "unitPrice": 60,
        "quantity": 1
      }
    ]
  }
}
```

Get All Links {#paybylink-all-intro}
====================================

Use the information in this section to retrieve all of the payment links you have created by sending a *get all links* request.

Endpoints
---------

**Production:** `GET ``https://api.cybersource.com``/ipl/v2/payment-links/`{#paybylink-all-intro_endpoint-getall-prod}  
**Test:** `GET ``https://apitest.cybersource.com``/ipl/v2/payment-links/`{#paybylink-all-intro_endpoint-getall-test}  
**India Production:** `GET ``https://api.in.cybersource.com``/ipl/v2/payment-links/`{#paybylink-all-intro_endpoint-getall-india}  
Set the *{id}* to the payment number ID contained in the create payment link response.

`REST` Example: Retrieving All Payment Links {#paybylink-all-ex-rest}
=====================================================================

Request

```
{}
```

Response to a Successful Request

```keyword
{
  "_links": {
    "self": {
      "href": "/ipl/v2/payment-links/?offset=0&limit=5",
      "method": "GET"
    },
    "next": {
      "href": "/ipl/v2/payment-links/?offset=5&limit=5",
      "method": "GET"
    }
  },
  "submitTimeUtc": "2024-08-09T19:58:08.823333768Z",
  "totalLinks": 87,
  "links": [
    {
      "_links": {
        "self": {
          "href": "/ipl/v2/payment-links/787596584685788",
          "method": "GET"
        },
        "update": {
          "href": "/ipl/v2/payment-links/787596584685788",
          "method": "PATCH"
        }
      },
      "id": "787596584685788",
      "status": "ACTIVE",
      "createdDate": "2024-08-09 19:56:02.463",
      "processingInformation": {
        "linkType": "PURCHASE"
      },
      "purchaseInformation": {
        "purchaseNumber": "787596584685788",
        "paymentLink": "https://businesscenter.cybersource.com/payByLink/pay/DpabIRBmi5nGTQEFMAjBhSHUg2o0VMy0Hde2QxMGZ6PUmTZt6HzEElcuweu6pTre"
      },
      "orderInformation": {
        "amountDetails": {
          "totalAmount": 60,
          "currency": "USD"
        },
        "lineItems": [
          {
            "productName": "Birthday Cake",
            "unitPrice": 60
          }
        ]
      }
    },
    {
      "_links": {
        "self": {
          "href": "/ipl/v2/payment-links/78759658468578",
          "method": "GET"
        },
        "update": {
          "href": "/ipl/v2/payment-links/78759658468578",
          "method": "PATCH"
        }
      },
      "id": "78759658468578",
      "status": "ACTIVE",
      "createdDate": "2024-08-09 18:14:32.213",
      "processingInformation": {
        "linkType": "PURCHASE"
      },
      "purchaseInformation": {
        "purchaseNumber": "78759658468578",
        "paymentLink": "https://businesscenter.cybersource.com/payByLink/pay/BirhSluHrqS7Dz76lXP6t3OmfyQ12fNRObUPvqb9ByH1UrbekMaQK18qdX9XubBS"
      },
      "orderInformation": {
        "amountDetails": {
          "totalAmount": 60,
          "currency": "USD"
        },
        "lineItems": [
          {
            "productName": "Birthday Cake",
            "unitPrice": 60
          }
        ]
      }
    },
    {
      "_links": {
        "self": {
          "href": "/ipl/v2/payment-links/516531358",
          "method": "GET"
        },
        "update": {
          "href": "/ipl/v2/payment-links/516531358",
          "method": "PATCH"
        }
      },
      "id": "516531358",
      "status": "ACTIVE",
      "createdDate": "2024-08-09 18:03:56.96",
      "processingInformation": {
        "linkType": "DONATION"
      },
      "purchaseInformation": {
        "purchaseNumber": "516531358",
        "paymentLink": "https://businesscenter.cybersource.com/payByLink/pay/JqfexFItwZuyGaz2Lkp5sUnhaRasnoyCcnMdVU2pi97XJ6OaDbtXWxI1krn8oGFe"
      },
      "orderInformation": {
        "amountDetails": {
          "totalAmount": 1,
          "currency": "USD",
          "minAmount": 1
        },
        "lineItems": [
          {
            "productName": "Fundraiser"
          }
        ]
      }
    },
    {
      "_links": {
        "self": {
          "href": "/ipl/v2/payment-links/09900",
          "method": "GET"
        },
        "update": {
          "href": "/ipl/v2/payment-links/09900",
          "method": "PATCH"
        }
      },
      "id": "09900",
      "status": "ACTIVE",
      "createdDate": "2024-08-08 15:03:29.21",
      "processingInformation": {
        "linkType": "PURCHASE"
      },
      "purchaseInformation": {
        "purchaseNumber": "09900",
        "paymentLink": "https://businesscenter.cybersource.com/payByLink/pay/xhEU2aewcbmM8Hi2wKJVmGnJZ3FWBQJpXXjJsC5E3ZZa9Y61ISdHm9ak6su6t887"
      },
      "orderInformation": {
        "amountDetails": {
          "totalAmount": 100,
          "currency": "USD"
        },
        "lineItems": [
          {
            "productName": "Pre Order",
            "productDescription": "Pre Order for Christmas",
            "unitPrice": 100
          }
        ]
      }
    },
    {
      "_links": {
        "self": {
          "href": "/ipl/v2/payment-links/68435461384354384836",
          "method": "GET"
        },
        "update": {
          "href": "/ipl/v2/payment-links/68435461384354384836",
          "method": "PATCH"
        }
      },
      "id": "68435461384354384836",
      "status": "ACTIVE",
      "createdDate": "2024-08-08 14:51:16.523",
      "processingInformation": {
        "linkType": "DONATION"
      },
      "purchaseInformation": {
        "purchaseNumber": "68435461384354384836",
        "paymentLink": "https://businesscenter.cybersource.com/payByLink/pay/nQpuAeme4aRwucfJtAq8AyLwdUjcWRGdhGAyPrLmIh0LGDaW4hvdnHCqf1lSRUJV"
      },
      "orderInformation": {
        "amountDetails": {
          "totalAmount": 1,
          "currency": "USD",
          "minAmount": 1
        },
        "lineItems": [
          {
            "productName": "123654"
          }
        ]
      }
    }
  ]
}
```

Update Payment Link Settings {#paybylink-services-update-settings-intro}
========================================================================

Use payment link settings to configure and manage the behavior and appearance of your payment page. You can update these payment link settings:  
![Branding Identity: Customize the checkout experience of your payment page to match your
branding, such as Brand colors, Business name, Logo, VAT tax number. Redirect URLs: Set
custom redirect URLs that display after a customer completes a payment.](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/paybylink/images/paybylink-update-settings-600x160.svg/jcr:content/renditions/original)

Reset to Default Settings {#paybylink-services-update-settings-intro_reset-settings}
------------------------------------------------------------------------------------

To reset your payment link settings to their default values, send the corresponding fields you want to reset with no value.

Endpoints
---------

Send your API request message to one of these endpoints:  
**Production:** `PUT ``https://api.cybersource.com``/invoicing/v2/invoiceSettings?productType=PAYBYLINK`  
**Test:** `PUT ``https://apitest.cybersource.com``/invoicing/v2/invoiceSettings?productType=PAYBYLINK`  
**India Production:** `PUT https://api.in,cybersource.com/invoicing/v2/invoiceSettings?productType=PAYBYLINK`

Required Fields for Update Settings {#paybylink-services-update-settings-req-fields}
====================================================================================

The update payment link settings request does not require a specific set of fields. Instead, you can choose the fields to include in your request based on aspects of your checkout experience, email communications, and payer authentication enablement that you want to update.

|           Name           |                    API Request Field                    |                                                                                                                                                                                     Description                                                                                                                                                                                      |
|--------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Business Name            | invoiceSettingsInformation. merchantDisplayName         | The business name displayed on the payment page.                                                                                                                                                                                                                                                                                                                                     |
| Currency                 | invoiceSettingsInformation. defaultCurrencyCode         | The currency of the billed amount. The currency code default value is set to `USD` when this field is not specified. Only three-character ISO Standard Currency Codes are accepted. For more information, see [ISO Standard Currency Codes](https://developer.cybersource.com/docs/cybs/en-us/currency-codes/reference/all/na/currency-codes/currency-codes.md "") reference guide.. |
| Header Background Color  | invoiceSettingsInformation. headerStyle.backgroundColor | The background color of the displayed payment page. Only hexadecimal code values with a prefixed `#` are accepted. Example: `#000000`                                                                                                                                                                                                                                                |
| Logo                     | invoiceSettingsInformation. merchantLogo                | The binary format of your logo that determines the image displayed to your customers. Image files are restricted to 1 MB and must be encoded in Base64 format. These are the supported file types: * gif * jpg * png                                                                                                                                                                 |
| VAT Tax Number           | invoiceSettingsInformation. vatRegistrationNumber       | The government-assigned tax identification number.                                                                                                                                                                                                                                                                                                                                   |
| VAT Tax Number Displayed | invoiceSettingsInformation. showVatNumber               | The toggle for displaying the VAT tax number on the payment page. Possible values: * `false`: Do not display the VAT tax number. * `true`: Display the VAT tax number.                                                                                                                                                                                                               |
[Branding Identity Settings]

|                Name                 |                        API Request Field                        |                                                       Description                                                       |
|-------------------------------------|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Successful Transaction Redirect URL | invoiceSettingsInformation. customRedirectUrls. paymentAccepted | The URL that the customer is redirected to after completing a successful transaction in which the payment is processed. |
| Pending Transaction Redirect URL    | invoiceSettingsInformation. customRedirectUrls. paymentPending  | The URL that the customer is redirected to after completing checkout and the payment is pending.                        |
| Failed Transaction Redirect URL     | invoiceSettingsInformation. customRedirectUrls. paymentRejected | The URL that the customer is redirected to after a transaction is rejected.                                             |
[Payment Page Redirect URL Settings]

Example: Update Payment Link Settings {#paybylink-services-update-settings-ex-rest}
===================================================================================

Request

```
{
  "invoiceSettingsInformation": {
    "merchantLogo": "/9j/4AWFhYW",
    "merchantDisplayName": "Custom Merchant Display Name",
    "headerStyle": {
      "fontColor": "#000001",
      "backgroundColor": "#FFFFFF"
    },
    "defaultCurrencyCode": "USD",
    "showVatNumber": false,
    "vatRegistrationNumber": "Inv1234",
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

Response Statuses for Updating Payment Link Settings {#paybylink-services-update-settings-resp-status}
======================================================================================================

| Status |                           Description                           |
|--------|-----------------------------------------------------------------|
| `200`  | The request is successful.                                      |
| `400`  | The request not successful due to field validation errors.      |
| `502`  | The request not successful due to an unexpected error occurred. |
[Response Statuses for Updating Payment Link Settings]

Webhook Subscriptions for `Pay by Link` {#paybylink-webhooks-intro}
===================================================================

Webhooks are automated notifications generated by system events that occur in your organization. You can subscribe to these event types to receive a notification when a customer makes a payment. Set the eventTypes request field to one of the values shown in these tables.

| Event Type Field Value       | Description                                                                                                              |
|:-----------------------------|:-------------------------------------------------------------------------------------------------------------------------|
| `payByLink.merchant.payment` | Merchants can subscribe to this event type to automate how their system is informed when a customer completes a payment. |
[Merchant Webhook Event]

| Event Type Field Value       | Description                                                                                                                                          |
|:-----------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `payByLink.customer.payment` | Partner resellers can subscribe to this event type to control the distribution of the payment confirmation email sent to their merchants' customers. |
[Partner Reseller Webhook Event]

Use the example in this section only to reference how to format the eventTypes request field and its values.  
You can designate a destination URL for the webhook notifications.  
Notifications that contain sensitive, personally identifiable information such as account numbers are sent using message-level encryption.

Prerequisite
:
Transport Layer Security is required in order to ensure data integrity.

Additional Requirements
-----------------------

There are additional requirements for implementing webhooks that are not discussed in this guide. To subscribe to `Pay by Link` webhook notifications, see the [*Webhooks Implementation Guide for the REST API*](https://developer.cybersource.com/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro.md "").

`REST` Example: Create `Pay by Link` Webhook Subscription {#paybylink-webhooks-ex-rest}
=======================================================================================

Request

```
{
  "name": "PBL Webhook Subscription",
  "description": "PBL Webhook for Digital Accept",
  "organizationId": "digital_accept_lab",
  "productId": "payByLink",
  "eventTypes": [
    "payByLink.customer.payment",
    "payByLink.merchant.payment"
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
  "organizationId": "digital_accept_lab",
  "productId": "payByLink",
  "eventTypes": [
    "payByLink.customer.payment",
    "payByLink.merchant.payment"
  ],
  "webhookId": "1928667e-f9f7-8a37-e063-9c588e0a7e3b",
  "name": "PBL Webhook Subscription",
  "webhookUrl": "https://test.com:443/test",
  "healthCheckUrl": "https://test.com:443/test",
  "createdOn": "2024-05-23T23:27:54.268Z",
  "status": "INACTIVE",
  "description": "PBL Webhook for Digital Accept",
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

Using the `Business Center` {#paybylink-ebc-intro}
==================================================

You can create and manage payment links using the `Business Center`:

* **Test:** [`https://businesscentertest.cybersource.com`](https://businesscentertest.cybersource.com/ebc2/ "")
* **Production:** [`https://businesscenter.cybersource.com`](https://businesscenter.cybersource.com/ebc2/ "")

After logging in to the `Business Center`, choose ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-paybylink-balance.svg/jcr:content/renditions/original) **Pay by Link** on the left navigation bar.  
For documentation about how to create payment links in the `Business Center`, choose ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-support.svg/jcr:content/renditions/original) **Support \&gt; Help** on the top right of the `Business Center` home screen.
