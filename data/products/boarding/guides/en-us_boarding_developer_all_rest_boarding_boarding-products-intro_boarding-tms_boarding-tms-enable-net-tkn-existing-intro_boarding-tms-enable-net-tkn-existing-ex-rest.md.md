REST Example: Enabling `TMS` and Enrolling in Network Tokenization for an Existing Merchant {#boarding-tms-enable-net-tkn-existing-ex-rest}
===========================================================================================================================================

Request

```
{
   "registrationInformation":{
      "boardingFlow":"ADDPRODUCT"
   },
   "organizationInformation":{
      "organizationId":"yourmerchantorgidhere",
      "parentOrganizationId":"yourportfolioorgidhere",
      "type":"MERCHANT",
      "configurable":true,
      "businessInformation":{
         "name":"TokenMerchant",
         "address":{
            "country":"US",
            "address1":"123456 SandMarket",
            "locality":"ORMOND BEACH",
            "administrativeArea":"FL",
            "postalCode":"32176"
         },
         "websiteUrl":"https://www.MerchantUrlHere.com",
         "businessContact":{
            "firstName":"Token",
            "lastName":"Man",
            "phoneNumber":"6574567813",
            "email":"tokenman@visa.com"
         }
      }
   },
   "productInformation":{
      "selectedProducts":{
         "commerceSolutions":{
            "tokenManagement":{
               "subscriptionInformation":{
                  "enabled":true
               },
               "configurationInformation":{
                  "configurations":{
                        "vault":{
                        "location": "GDC",
                        "defaultTokenType":"CUSTOMER",
                        "tokenFormats":{
                           "customer":"32_HEX",
                           "paymentInstrument":"32_HEX",
                           "instrumentIdentifierCard":"19_DIGIT_LAST_4",
                           "instrumentIdentifierBankAccount":"32_HEX"
                        },
                        "sensitivePrivileges":{
                           "cardNumberMaskingFormat":"FIRST_6_LAST_4"
                        }                     },
                     "networkTokenEnrollment":{
                        "businessInformation":{
                           "name":"TokenMerchant",
                           "doingBusinessAs":"NetworkTokenCo1",
                           "address":{
                              "country":"US",
                              "locality":"ORMOND BEACH"
                           },
                           "websiteUrl":"https://www.MerchantUrlHere.com",
                           "acquirer":{
                              "acquirerId":"40010052242",
                              "acquirerMerchantId":"yourmerchantorgidhere"
                           }
                        },
                        "networkTokenServices":{
                           "visaTokenService":{
                              "enrollment":true
                           },
                           "mastercardDigitalEnablementService":{
                              "enrollment":true
                           }
                        }
                     },
                        "networkTokenServices":{
                           "notifications":{
                              "enabled":true
                           },
                           "paymentCredentials":{
                              "enabled":true
                           },
                           "visaTokenService":{
                              "enableService":true,
                              "enableTransactionalTokens":true
                           },
                           "mastercardDigitalEnablementService":{
                              "enableService":true,
                              "enableTransactionalTokens":true
                           }
                        }
                  }
               }
            }
         }
      }
   }
}
```

Response to Successful Request

```
{
  "id": "94498504004",
  "submitTimeUtc": "2024-07-01T16:25:20Z",
  "status": "SUCCESS",
  "registrationInformation": {
    "mode": "COMPLETE",
    "boardingPackageId": "1168704004"
  },
  "organizationInformation": {
    "organizationId": "{MerchantAccountOrgId}",
    "parentOrganizationId": "{PortfolioOrgId}"
  },
  "message": "Request was processed successfully"
}

```

