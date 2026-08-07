REST Example: Enabling `Payer Authentication` {#boarding-payer-auth-enable-ex-rest}
===================================================================================

Request

```
{
  "registrationInformation": {
    "boardingFlow": "ADDPRODUCT"
  },
  "organizationInformation": {
    "organizationId": "apitester00",
    "parentOrganizationId": "nishtx",
    "type": "TRANSACTING",
    "configurable": false,
    "businessInformation": {
      "address": {
        "country": "US",
        "address1": "123 Main",
        "postalCode": "99999",
        "administrativeArea": "WA",
        "locality": "Seattle"
      },
      "businessContact": {
        "firstName": "Jane",
        "lastName": "Smith",
        "phoneNumber": "5551234567",
        "email": "email@domain.com"
      },
      "name": "Test Merchant",
      "websiteUrl": "https://www.example.com"
    }
  },
  "productInformation": {
    "selectedProducts": {
      "payments": {
        "payerAuthentication": {
          "configurationInformation": {
            "configurations": {
              "cardTypes": {
                "amexSafeKey": {
                  "enabled": true,
                  "currencies": [
                    {
                      "currencyCodes": ["ALL"],
                      "acquirerId": "12345678901-1000",
                      "processorMerchantId": "procmerch123"
                    }
                  ]
                },
                "CB": {
                  "requestorId": "",
                  "enabled": true,
                  "currencies": [
                    {
                      "currencyCodes": ["ALL"],
                      "acquirerId": "211111-1000",
                      "processorMerchantId": "procmerch123"
                    }
                  ]
                },
                "dinersClubInternationalProtectBuy": {
                  "enabled": true,
                  "currencies": [
                    {
                      "currencyCodes": ["ALL"],
                      "acquirerId": "311111-1000",
                      "processorMerchantId": "procmerch123"
                    }
                  ]
                },
                "ELO": {
                  "enabled": true,
                  "currencies": [
                    {
                      "currencyCodes": ["ALL"],
                      "acquirerId": "11111111-1000",
                      "processorMerchantId": "procmerch123"
                    }
                  ]
                },
                "jCBJSecure": {
                  "securePasswordForJCB": "jcbpass",
                  "enabled": true,
                  "currencies": [
                    {
                      "currencyCodes": ["ALL"],
                      "acquirerId": "123456-1000",
                      "processorMerchantId": "procmerch123"
                    }
                  ]
                },
                "masterCardSecureCode": {
                  "enabled": true,
                  "currencies": [
                    {
                      "currencyCodes": ["ALL"],
                      "acquirerId": "522222-1000",
                      "processorMerchantId": "procmerch123"
                    }
                  ]
                },
                "UPI": {
                  "enabled": true,
                  "currencies": [
                    {
                      "currencyCodes": ["ALL"],
                      "acquirerId": "611111-1000",
                      "processorMerchantId": "procmerch123"
                    }
                  ]
                },
                "verifiedByVisa": {
                  "enabled": true,
                  "currencies": [
                    {
                      "currencyCodes": ["ALL"],
                      "acquirerId": "411111-1000",
                      "processorMerchantId": "procmerch123"
                    }
                  ]
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

Response to a Successful Request

```
{
  "id": "87304104004",
  "submitTimeUtc": "2024-05-14T15:53:19Z",
  "status": "PROCESSING",
  "registrationInformation": {
    "mode": "COMPLETE",
    "boardingPackageId": "190303004"
  },
  "organizationInformation": {
    "organizationId": "apitester00",
    "parentOrganizationId": "nishtx"
  },
  "message": "Request is being processed"
}
```

