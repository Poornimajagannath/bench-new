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

