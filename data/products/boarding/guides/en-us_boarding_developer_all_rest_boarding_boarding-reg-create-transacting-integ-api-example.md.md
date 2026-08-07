REST Example: Creating a Transacting Organization with Integration Information {#boarding-reg-create-transacting-integ-api-example}
===================================================================================================================================

Request with Integration Information

```
{
  "registrationInformation": {
    "boardingFlow": "ENTERPRISE",
    "mode": "COMPLETE",
    "boardingPackageId": "16885604124"
  },
  "organizationInformation": {
    "status": "LIVE",
    "businessInformation": {
      "address": {
        "country": "GB",
        "address1": "Sample Street 1234",
        "locality": "London",
        "postalCode": "98765"
      },
      "businessContact": {
        "firstName": "Test",
        "lastName": "Test",
        "phoneNumber": "123456789",
        "email": "test@test.com"
      },
      "technicalContact": {
        "firstName": "Test",
        "lastName": "Test",
        "phoneNumber": "123456789",
        "email": "test@test.com"
      },
      "emergencyContact": {
        "firstName": "Test",
        "lastName": "Test",
        "phoneNumber": "123456789",
        "email": "test@test.com"
      },
      "name": "Test 4",
      "websiteUrl": "",
      "phoneNumber": "123456789",
      "timeZone": "GMT",
      "merchantCategoryCode": "5399"
    },
    "parentOrganizationId": "cptesting06",
    "type": "TRANSACTING",
    "configurable": false
  },
  "integrationInformation": {
    "tenantConfigurations": [
      {
        "solutionId": "wrqgaz3e",
      }
    ]
  },
  "productInformation": {
    "selectedProducts": {
      "payments": {
        "cardProcessing": {
          "subscriptionInformation": {
            "enabled": true,
            "features": {
              "cardNotPresent": {
                "enabled": false
              },
              "cardPresent": {
                "enabled": true
              }
            }
          },
          "configurationInformation": {
            "configurations": {
              "common": {
                "merchantCategoryCode": "5399",
                "defaultAuthTypeCode": "FINAL",
                "processors": {
                  "barclayshiso": {
                    "acquirer": {},
                    "paymentTypes": {
                      "MAESTRO": {
                        "enabled": true
                      },
                      "MASTERCARD": {
                        "enabled": true
                      },
                      "DISCOVER": {
                        "enabled": true
                      },
                      "JCB": {
                        "enabled": true
                      },
                      "VISA": {
                        "enabled": true
                      },
                      "VISA_ELECTRON": {
                        "enabled": true
                      },
                      "DINERS_CLUB": {
                        "enabled": true
                      },
                      "CUP": {
                        "enabled": true
                      }
                    },
                    "batchGroup": "barclayshiso_test",
                    "merchantId": "1234567",
                    "terminalId": null
                  }
                }
              },
              "features": {
                "cardNotPresent": {
                  "processors": {
                    "barclayshiso": {
                      "relaxAddressVerificationSystem": true,
                      "relaxAddressVerificationSystemAllowExpiredCard": true,
                      "relaxAddressVerificationSystemAllowZipWithoutCountry": true
                    }
                  }
                }
              }
            },
            "templateId": "F4EEFE3C-ED8C-4937-A48A-C013B228488E"
          }
        },
        "cybsReadyTerminal": {
          "subscriptionInformation": {
            "enabled": true,
            "selfServiceability": "NOT_SELF_SERVICEABLE"
          }
        }
      },
      "risk": {},
      "commerceSolutions": {},
      "valueAddedServices": {}
    }
  }
}
```

Response to a Successful Request

```
{
  "id": "12351234",
  "submitTimeUtc": "2023-06-11T22:47:57.000Z",
  "status": "SUCCESS",
  "registrationInformation": {
    "mode": "COMPLETE",
    "boardingPackageId": "16885604124"
  },
  "organizationInformation": {
    "organizationId": "cptesting061830",
    "parentOrganizationId": "cptesting06"
  },
  "integrationInformation": {
    "tenantConfigurations": [
      {
        "solutionId": "YumSolution1",
        "tenantConfigurationId": "id1234",
        "status": "LIVE",
        "submitTimeUtc": "2019-08-24T14:15:22Z"
      }
    ]
  },
  "message": "Request was processed succesfully.",
  "details": {}
}
```

