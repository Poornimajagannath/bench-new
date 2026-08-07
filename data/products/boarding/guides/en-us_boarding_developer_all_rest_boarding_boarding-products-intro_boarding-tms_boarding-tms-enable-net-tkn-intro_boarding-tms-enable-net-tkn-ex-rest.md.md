REST Example: Enabling `TMS` and Enrolling in Network Tokenization for a New Merchant {#boarding-tms-enable-net-tkn-ex-rest}
============================================================================================================================

Request

```
{
  "registrationInformation": {
    "boardingFlow": "ENTERPRISE"
  },
  "organizationInformation": {
    "organizationId": "yourmerchantorgidhere",
    "parentOrganizationId": "yourportfolioorgidhere",
    "type": "MERCHANT",
    "configurable": true,
    "businessInformation": {
      "name": "NetworkTokenMerchant",
      "address": {
        "country": "US",
        "address1": "123456 SandMarket",
        "locality": "ORMOND BEACH",
        "administrativeArea": "FL",
        "postalCode": "32176"
      },
      "websiteUrl": "https://www.NetworkTokenMerchant.com",
      "businessContact": {
        "firstName": "Token",
        "lastName": "Man",
        "phoneNumber": "6574567813",
        "email": "networktokenman@visa.com"
      }
    }
  },
  "productInformation": {
    "selectedProducts": {
      "commerceSolutions": {
        "tokenManagement": {
          "subscriptionInformation": {
            "enabled": true
          },
          "configurationInformation": {
            "configurations": {
              "vault": {
                "location": "GDC",
                "defaultTokenType": "CUSTOMER",
                "tokenFormats": {
                  "customer": "32_HEX",
                  "paymentInstrument": "32_HEX",
                  "instrumentIdentifierCard": "19_DIGIT_LAST_4",
                  "instrumentIdentifierBankAccount": "32_HEX"
                },
                "sensitivePrivileges": {
                  "cardNumberMaskingFormat": "FIRST_6_LAST_4"
                },
                "networkTokenServices": {
                  "notifications": {
                    "enabled": true
                  },
                  "paymentCredentials": {
                    "enabled": true
                  },
                  "synchronousProvisioning": {
                    "enabled": false
                  },
                  "visaTokenService": {
                    "enableService": true,
                    "enableTransactionalTokens": true
                  },
                  "mastercardDigitalEnablementService": {
                    "enableService": true,
                    "enableTransactionalTokens": true
                  }
                }
              },
              "networkTokenEnrollment": {
                "businessInformation": {
                  "name": "NetworkTokenMerchant",
                  "doingBusinessAs": "NetworkTokenCo1",
                  "address": {
                    "country": "US",
                    "locality": "ORMOND BEACH"
                  },
                  "websiteUrl": "https://www.NetworkTokenMerchant.com",
                  "acquirer": {
                    "acquirerId": "40010052242",
                    "acquirerMerchantId": "MerchantOrgID"
                  }
                },
                "networkTokenServices": {
                  "visaTokenService": {
                    "enrollment": true
                  },
                  "mastercardDigitalEnablementService": {
                    "enrollment": true
                  }
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

