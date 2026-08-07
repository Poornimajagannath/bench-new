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

