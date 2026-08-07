Add a New Product to an Existing Organization {#boarding-update-product-api}
============================================================================

To add a product, you must subscribe to it, and if there are configurations available, configure it.

Endpoint {#boarding-update-product-api_d7e638}
----------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/products/v1/product-setups`{#boarding-update-product-api_d7e645}  
**Test:** `POST ``https://apitest.cybersource.com``/products/v1/product-setups`{#boarding-update-product-api_d7e655}

Subscribing to a Product {#boarding-update-product-api_section_r3n_f3r_y5b}
---------------------------------------------------------------------------

Product fields are in the selectedProducts object. Include the field for the product you are adding, and set `subscriptionInformation.enabled` field for that product to `true`  
***Product Features***  
Some products also have a `features` block within the `subscriptionInformation` object that gives you the ability to enable features of a product.

```
"subscriptionInformation": { 
  "enabled": true, 
  "features": { 
    "cardNotPresent": { 
      "enabled": true 
      }, 
    "cardPresent": { 
      "enabled": true 
      } 
```

Configuring a Product {#boarding-update-product-api_section_s3n_f3r_y5b}
------------------------------------------------------------------------

Some products have a `configurationInformation` object that contains a `templateId` field and a `configurations` object.  
The `templateId` field refers to a product configuration template that is already created in the `Business Center` and is required to configure a product using the Boarding API. If the `templateId` field is not submitted or is left blank, the default template for the account is used. For more information about templates, see [Product Templates](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro-templat-0.md "").  
You can override product template values by submitting the `configurations` object.  
***Configurations Object Example***

```
"configurationInformation": {
 "templateId": "A57EB750-6543-46A5-83BE-CCA38D9C9083",
 "configurations": {
   "common": {
     "defaultAuthTypeCode": "final",
     "foodAndConsumerServiceId": "1234",
     "enablePartialAuth": true,
     "useParentTransactionAmountForFollowOn": false,
     "merchantCategoryCode": "1234",
     "processors": {
       "processorName": {
         "batchGroup": "processorname_batch_00",
         "acquirer": {
           "interbankCardAssociationId": "20490",
           "discoverInstitutionId": "666666",
           "institutionId": "432870",
           "fileDestinationBin": "432870",
           "countryCode": "840_usa"    
           },
         "merchantId": "20003791",
         "terminalId": "yD9mP42e",
         "sicCode": "1234",
         "allowMultipleBills": true,
         "fireSafetyIndicator":false,
         "quasiCash":false,
         "paymentTypes":{
           "VISA": {"enabled": true}, "MASTERCARD": {"enabled": true},"AMERICAN_EXPRESS": {"enabled": true},"CUP": {"enabled": true},"JCB": {"enabled": true},"DISCOVER": {"enabled": true},"FALABELLA_PLCC": {"enabled": true},"COSTCO_PLCC": {"enabled": true},"DINERS_CLUB": {"enabled": true}
           },
         "currencies": {
           "USD": {"enabled": true }
         }
         }
       }
     },
     "features": {
       "cardNotPresent": {
         "ignoreAddressVerificationSystem": true,
         "processors": {
           "gpx": {
             "relaxAddressVerificationSystem":true,
             "relaxAddressVerificationSystemAllowZipWithoutCountry":true,
             "relaxAddressVerificationSystemAllowExpiredCard":false,
             "visaSTPOnly":false,
             "enableEmsTransactionRiskScore":false
             }
```

