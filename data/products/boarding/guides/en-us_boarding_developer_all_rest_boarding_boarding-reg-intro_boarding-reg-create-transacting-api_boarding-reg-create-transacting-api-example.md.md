REST Example: Creating a Transacting Organization {#boarding-reg-create-transacting-api-example}
================================================================================================

Request

```
{
    "registrationInformation": {
        "boardingFlow": "ENTERPRISE"
    },
    "organizationInformation": {
        "organizationId": "yourtransactingorgidhere",
        "status": "LIVE",
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
            "technicalContact": {
                "firstName": "Jane",
                "lastName": "Smith",
                "phoneNumber": "5551234567",
                "email": "email@domain.com"
            },
            "emergencyContact": {
                "firstName": "Jane",
                "lastName": "Smith",
                "phoneNumber": "5551234567",
                "email": "email@domain.com"
            },
            "name": "Test Merchant",
            "websiteUrl": "https://www.MerchantUrlHere.com",
            "phoneNumber": "5551234567",
            "timeZone": "America/Los_Angeles",
            "merchantCategoryCode": "5999"
        },
        "parentOrganizationId": "yourmercahntorgidhere",
        "type": "TRANSACTING",
        "configurable": false
    },
    "productInformation": {
        "selectedProducts": {
            "payments": {
                "customerInvoicing": {
                    "subscriptionInformation": {
                        "enabled": true,
                        "selfServiceability": "NOT_SELF_SERVICEABLE"
                    }
                }
            },
            "risk": {
                "fraudManagementEssentials": {
                    "subscriptionInformation": {
                        "enabled": true,
                        "selfServiceability": "NOT_SELF_SERVICEABLE"
                    }
                }
            },
            "commerceSolutions": {
                "tokenManagement": {
                    "subscriptionInformation": {
                        "enabled": true,
                        "selfServiceability": "NOT_SELF_SERVICEABLE"
                    }
                }
            },
            "valueAddedServices": {
                "transactionSearch": {
                    "subscriptionInformation": {
                        "enabled": true,
                        "selfServiceability": "NOT_SELF_SERVICEABLE"
                    }
                },
                "reporting": {
                    "subscriptionInformation": {
                        "enabled": true,
                        "selfServiceability": "NOT_SELF_SERVICEABLE"
                    }
                }
            }
        }
    }
}
```

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
        "solutionId": "wrqgaz3e"
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
                    "acquirer": {acq123
                    },
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
      }
    }
  }
}
```

Response to Successful Request

```
{
    "id": "1696604001",
    "submitTimeUtc": "2022-04-13T21:03:02Z",
    "status": "SUCCESS",
    "registrationInformation": {
        "mode": "COMPLETE",
        "boardingPackageId": "123456789012"
    },
    "organizationInformation": {
        "organizationId": "yourtransactingorgidhere",
        "parentOrganizationId": "yourmercahntorgidhere"
    },
    "message": "Request was processed successfully"
}
```

