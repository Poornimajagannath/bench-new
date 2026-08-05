Process a Sale {#pay-by-bank-payto-sale-intro}
==============================================

This section describes how to send a sale request to process a payment.  
A sale request authorizes and captures a payment in the same request. A successful sale response includes a redirect URL and a `PENDING` status. Redirect the customer to the PayTo URL to allow the customer to complete the checkout using their bank information. When the customer completes the checkout, the customer is redirected to your website.  
When you receive a successful response, save the sale request ID in the id response field to perform a follow-on check status request or refund request.

Calculating the Grand Total {#pay-by-bank-payto-sale-intro_grand-total}
-----------------------------------------------------------------------

Include the grand total in the request by using the orderInformation.amountDetails.totalAmount field.

Endpoints {#pay-by-bank-payto-sale-intro_section_l3f_xrs_fgc}
-------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#pay-by-bank-payto-sale-intro_d7e345}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#pay-by-bank-payto-sale-intro_d7e355}

Processing a Sale {#pay-by-bank-payto-sale-req-fields-rest}
===========================================================

Processing a sale requires you to use information from the API response message to redirect the customer to a website where the customer can complete the checkout. Follow these steps to process a sale.

1. Send a POST request to the `https://api.cybersource.com``/pts/v2/payments` endpoint and include these required fields:

   #### ADDITIONAL INFORMATION

   [clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
   :
   Set to an 18-character value or less.

   [orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
   :
   Set to `AUD`.

   [orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
   :

   orderInformation.invoiceDetails.productDescription
   :

   [paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
   :
   Set to `payToPayByBank`.

   [paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
   :
   Set to `bankTransfer`.

   [processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
   :
   Set to `AP_SALE`.
   {#pay-by-bank-payto-sale-req-fields-rest_dl_g3p_jnl_fgc}

2. If needed, include any of these optional line item fields in the request:

   #### ADDITIONAL INFORMATION

   [merchantInformation.merchantDescriptor.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-admin-area.md "")
   :

   [merchantInformation.merchantDescriptor.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
   :

   [orderInformation.amountDetails.discountAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-discount-amount.md "")
   :

   [orderInformation.amountDetails.dutyAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-duty-amount.md "")
   :

   [orderInformation.amountDetails.exchangeRate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-exchange-rate-a.md "")
   :

   [orderInformation.amountDetails.taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-tax-amount.md "")
   :

   [orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
   :

   [orderInformation.billTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address2.md "")
   :

   [orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
   :

   [orderInformation.billTo.company.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-company-name.md "")
   :

   [orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
   :

   [orderInformation.billTo.county](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-county.md "")
   :

   [orderInformation.billTo.district](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-district.md "")
   :

   [orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
   :

   [orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
   :

   [orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
   :

   [orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
   :

   [orderInformation.billTo.middleName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-middle-name.md "")
   :

   [orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
   :

   [orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
   :

   [orderInformation.billTo.title](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-title.md "")
   :

   [orderInformation.shippingDetails.shippingMethod](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipping-details-shipping-method.md "")
   :

   [orderInformation.shipTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-street1.md "")
   :

   [orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-street2.md "")
   :

   [orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-county.md "")
   :

   [orderInformation.shipTo.company](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-company.md "")
   :

   [orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
   :

   [orderInformation.shipTo.district](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-district.md "")
   :

   [orderInformation.shipTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-email.md "")
   :

   [orderInformation.shipTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-first-name.md "")
   :

   [orderInformation.shipTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-last-name.md "")
   :

   [orderInformation.shipTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-locality.md "")
   :

   [orderInformation.shipTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-phone-num.md "")
   :

   [orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
   :
   {#pay-by-bank-payto-sale-req-fields-rest_dl_wd1_5yk_fgc}

3. Redirect the customer to the URL in the processorInformation.paymentUrl response field.

   ```
   "paymentUrl": "https://checkout.banked.com/au/3645bd90-7625-4202-8cc3-a1cb58358899?token=eyJhbGciOiJI"
   ```
4. Save the request ID in the id field from the sale response. Include the request ID in a check status request to confirm that the payment is complete.

   ```
   "id": "7544094135706957804805"
   ```

   {#pay-by-bank-payto-sale-req-fields-rest_codeblock_zqw_lbl_fgc}

#### AFTER COMPLETING THE TASK

When the sale amount is successfully processed, Cybersource sends a `SETTLED` webhook notification. See [Introduction to Webhooks](/docs/cybs/en-us/pay-by-bank-payto/developer/all/rest/pay-by-bank-payto/pay-by-bank-payto-process-trxn/pay-by-bank-payto-webhooks-intro.md ""). If you do not receive a webhook notification, send a check status request. See [Check a Status](/docs/cybs/en-us/pay-by-bank-payto/developer/all/rest/pay-by-bank-payto/pay-by-bank-payto-process-trxn/pay-by-bank-payto-checkstatus-intro.md "").

Example: Processing a Sale {#pay-by-bank-payto-sale-ex-rest}
============================================================

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
        "invoiceDetails": {
            "productDescription": "test description"
        },
        "amountDetails": {
            "totalAmount": "1999.99",
            "currency": "AUD"
        }
    },
    "paymentInformation": {
        "paymentType": {
            "name": "bankTransfer",
            "method": {
                "name": "payToPayByBank"
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
            "totalAmount": "1999.99",
            "currency": "AUD"
        }
    },
    "processorInformation": {
        "transactionId": "3645bd90-7625-4202-8cc3-a1cb58358899",
        "paymentUrl": "https://checkout.banked.com/au/3645bd90-7625-4202-8cc3-a1cb58358899?token=eyJhbGciOiJI",
        "responseCode": "00001",
        "completeUrl": "merchant_success_url.com"
    },
    "message": "Request was processed successfully.",
    "clientReferenceInformation": {
        "code": "TC84100-1"
    },
    "reconciliationId": "KOZX0DMQKX0A",
    "status": "PENDING",
    "id": "7544094135706957804805",
    "submitTimeUtc": "2025-08-05T15:56:53Z"
}
```

