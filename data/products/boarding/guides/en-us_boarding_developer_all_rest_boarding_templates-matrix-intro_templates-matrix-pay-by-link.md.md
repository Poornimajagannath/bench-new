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

