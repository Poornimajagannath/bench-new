REST Example: Enabling `TMS` and Enrolling in Network Tokenization Using the PECS API {#boarding-pecs-tms-enable-ex-rest}
=========================================================================================================================

Request

```
{
  "organizationId": "ergaergaerg001",
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
            }
          },
          "networkTokenEnrollment": {
            "businessInformation": {
              "name": "TokenMerchant",
              "doingBusinessAs": "NetworkTokenCo1",
              "address": {
                "country": "US",
                "locality": "ORMOND BEACH"
              },
              "websiteUrl": "https://www.MerchantUrlHere.com",
              "acquirer": {
                "acquirerId": "40010052242",
                "acquirerMerchantId": "yourmerchantorgidhere"
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
          },
          "networkTokenServices": {
            "notifications": {
              "enabled": true
            },
            "paymentCredentials": {
              "enabled": true
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
        }
      }
    }
  }
}
```

Response to Successful Request

```
{
  "setups": {
    "commerceSolutions": {
      "tokenManagement": {
        "configurationStatus": {
          "status": "SUCCESS",
          "message": "Profile Assigned Successfully"
        },
        "subscriptionStatus": {
          "status": "SUCCESS",
          "message": "success"
        }
      }
    }
  },
  "status": "PROCESSED",
  "submitTimeUtc": "2022-06-03T08:46:13+0000"
}
```

