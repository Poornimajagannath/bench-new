Sale {#paybybank-sale-intro}
============================

Send a sale request to begin processing a payment. A response to a successful request includes a `PENDING` status and a URL in the processorInformation.paymentURL field. Redirect the customer to the URL to allow the customer to complete the payment on their bank's website.  
After sending a successful request, you can send a follow-on check status request or a refund request. These follow-on services require the request ID from the sale response, which is the id field value.  
Pay by Bank requires that you include line items in your sale request. [Line items](# "") are used to include information about the goods and services that your customers purchase, such as product name, quantity, and price.

Endpoints
---------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#paybybank-sale-intro_d17e345}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#paybybank-sale-intro_d17e355}

Response Statuses {#paybybank-sale-intro_status-response}
---------------------------------------------------------

`Cybersource` responds to your sale request with one of these statuses in the status field:
* `PENDING`: The sale request is accepted but the customer has not completed checkout. A webhook notification informs you when the customer completes checking out and the sale settles. See [Webhook Subscriptions](/docs/cybs/en-us/pay-by-bank/developer/all/rest/pay-by-bank/paybybank-intro-services/paybybank-webhook-intro.md ""). If you do not receive a webhook notification, send a check status request. See [Check Status](/docs/cybs/en-us/pay-by-bank/developer/all/rest/pay-by-bank/paybybank-intro-services/paybybank-status-intro.md "").
* `REJECT`: The sale is not successful. Send a new sale request.
  {#paybybank-sale-intro_statuses-sale}  
  `Cybersource` also responds with a reason code in the processorInformation.responseCode field. For more information about reason codes, see [Reason Codes and Pay by Bank Response Codes](/docs/cybs/en-us/pay-by-bank/developer/all/rest/pay-by-bank/paybybank-reference-codes.md "").  
  If you send a check status request to retrieve the current sale status, these are the possible responses:
* `ABANDONED`: The customer did not complete checkout before the redirect URL expired.
* `COMPLETED`: The customer completed the checkout process and the sale is currently under review. You can send the check status request in 60-minute intervals to retrieve the current status.
* `PENDING`: The sale request is accepted but is not complete. You can send the check status request in 60-minute intervals until the status updates.
* `REJECT`: The sale request is not successful. An unsuccessful request can be due to either Pay by Bank rejecting the transaction or a technical error.
* `SETTLED`: The sale is complete for the requested amount.
  {#paybybank-sale-intro_statuses-sale-check}

Processing a Sale {#paybybank-sale-req-fields-rest}
===================================================

You redirect the customer to a website in order to complete the checkout. Follow these steps to process a sale.

1. Send a `POST` request to the `https://api.cybersource.com``/pts/v2/payments`{#paybybank-sale-req-fields-rest_sale-test-rest} endpoint and include these required fields:

   #### ADDITIONAL INFORMATION

   clientReferenceInformation.code
   :

   merchantInformation.merchantDescriptor.name
   :

   orderInformation.amountDetails.currency
   :
   Set to `GBP`.

   orderInformation.amountDetails.totalAmount
   :

   orderInformation.billTo.email
   :

   orderInformation.billTo.firstName
   :

   orderInformation.billTo.lastName
   :

   orderInformation.lineItems.productName
   :

   orderInformation.lineItems.quantity
   :

   orderInformation.lineItems.totalAmount
   :

   orderInformation.lineItems.unitPrice
   :

   paymentInformation.paymentType.method.name
   :
   Set to `bofaPayByBank`.

   paymentInformation.paymentType.name
   :
   Set to `bankTransfer`.

   processingInformation.actionList
   :
   Set to `AP_SALE`.
   {#paybybank-sale-req-fields-rest_dl_nsd_xys_fgc}

2. If needed, include any of these optional line item fields in the request:

   #### ADDITIONAL INFORMATION

   merchantInformation.merchantDescriptor.administrativeArea
   :

   merchantInformation.merchantDescriptor.country
   :

   orderInformation.amountDetails.discountAmount
   :

   orderInformation.amountDetails.dutyAmount
   :

   orderInformation.amountDetails.exchangeRate
   :

   orderInformation.amountDetails.taxAmount
   :

   orderInformation.billTo.address1
   :

   orderInformation.billTo.address2
   :

   orderInformation.billTo.administrativeArea
   :

   orderInformation.billTo.company.name
   :

   orderInformation.billTo.country
   :

   orderInformation.billTo.county
   :

   orderInformation.billTo.district
   :

   orderInformation.billTo.locality
   :

   orderInformation.billTo.middleName
   :

   orderInformation.billTo.phoneNumber
   :

   orderInformation.billTo.postalCode
   :

   orderInformation.billTo.title
   :

   orderInformation.invoiceDetails.productDescription
   :

   orderInformation.lineItems.discountAmount
   :

   orderInformation.lineItems.discountRate
   :

   orderInformation.lineItems.taxAmount
   :

   orderInformation.lineItems.taxRate
   :

   orderInformation.shippingDetails.shippingMethod
   :

   orderInformation.shipTo.address1
   :

   orderInformation.shipTo.address2
   :

   orderInformation.shipTo.administrativeArea
   :

   orderInformation.shipTo.company
   :

   orderInformation.shipTo.country
   :

   orderInformation.shipTo.county
   :

   orderInformation.shipTo.district
   :

   orderInformation.shipTo.email
   :

   orderInformation.shipTo.firstName
   :

   orderInformation.shipTo.lastName
   :

   orderInformation.shipTo.locality
   :

   orderInformation.shipTo.middleName
   :

   orderInformation.shipTo.phoneNumber
   :

   orderInformation.shipTo.postalCode
   :
   {#paybybank-sale-req-fields-rest_dl_k3f_h1t_fgc}

3. Direct the customer to the URL in the processorInformation.paymentURL response field.

   #### ADDITIONAL INFORMATION

   ```
   "paymentUrl": "https://checkout.b.banked.com/eu/527057ed-d48c-4333-a252-03c36d2132db?token=eyJhbGciOiJIUz"
   ```
4. When the customer validates the purchase on their bank's website, they are redirected to the merchant's website that you provided in the processorInformation.completeUrl request field.

   #### ADDITIONAL INFORMATION

   ```
   "completeUrl": "https://www.merchant.redirect.url.from.request.html?actionsuccess"
   ```

#### AFTER COMPLETING THE TASK

When the sale amount is successfully processed, `Cybersource` sends a `SETTLED` webhook notification. See [Webhook Subscriptions](/docs/cybs/en-us/pay-by-bank/developer/all/rest/pay-by-bank/paybybank-intro-services/paybybank-webhook-intro.md ""). If you do not receive a webhook notification, send a check status request. See [Check Status](/docs/cybs/en-us/pay-by-bank/developer/all/rest/pay-by-bank/paybybank-intro-services/paybybank-status-intro.md "").

`REST` Example: Processing a Sale {#paybybank-sale-ex-rest}
===========================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TC84100-1"
    },
    "processingInformation": {
        "actionList": [
            "AP_SALE"
        ]
    },
    "orderInformation": {
        "lineItems": [
            {
                "unitPrice": "14.16",
                "totalAmount": "70.80",
                "quantity": 5,
                "productName": "Skirt on the sky"
            }
        ],
        "billTo": {
            "lastName": "Bowditch",
            "firstName": "Comet",
            "email": "srbuyeroffice@cybs.com"
        },
        "amountDetails": {
            "totalAmount": "1999.99",
            "currency": "GBP"
        }
    },
    "merchantInformation": {
        "merchantDescriptor": {
            "name": "BofA Merchant"
        }
    },
    "paymentInformation": {
        "paymentType": {
            "name": "bankTransfer",
            "method": {
                "name": "bofaPayByBank"
            }
        }
    }
}
```

Response to a Successful Request

```
{
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "70.80",
            "currency": "GBP"
        }
    },
    "processorInformation": {
        "transactionId": "527057ed-d48c-4333-a252-03c36d2132db",
        "paymentUrl": "https://checkout.b.banked.com/eu/527057ed-d48c-4333-a252-03c36d2132db?token=eyJhbGciOiJIUz",
        "responseCode": "00001",
        "completeUrl": "https://www.merchant.redirect.url.from.request.html?actionsuccess"
    },
    "message": "Request was processed successfully.",
    "clientReferenceInformation": {
        "code": "TC84100-1"
    },
    "reconciliationId": "KOZX0DMQKX17",
    "status": "PENDING",
    "id": "7545074870976150504806",
    "submitTimeUtc": "2025-08-06T19:11:27Z"
}
```

