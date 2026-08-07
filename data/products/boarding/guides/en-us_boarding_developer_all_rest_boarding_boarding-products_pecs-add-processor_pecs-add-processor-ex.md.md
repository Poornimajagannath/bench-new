Example: Adding a Processor Using the PECS API {#pecs-add-processor-ex}
=======================================================================

Request

```
{
  "organizationId": "cp_transacting1",
  "payments": {
    "cardProcessing": {
      "subscriptionInformation": {
        "enabled": true,
        "features": {
          "cardPresent": {
            "enabled": true
          }
        }
      },
      "configurationInformation": {
        "configurations": {
          "common": {
            "merchantCategoryCode": "5399",
            "merchantDescriptorInformation": {
              "city": "London",
              "country": "GBR",
              "name": "BCTest1",
              "phone": "1234567",
              "zip": "RG1 4BB",
              "state": "LN",
              "street": "Sample Street"
            },
            "processors": {
              "amexdirect": {
                "currencies": {
                  "GBP": {
                    "serviceEnablementNumber": "1234567891"
                  }
                }
              }
            }
          },
          "features": {
            "cardNotPresent": {
              "processors": {
                "amexdirect": {
                  "relaxAddressVerificationSystem": true,
                  "relaxAddressVerificationSystemAllowZipWithoutCountry": true,
                  "relaxAddressVerificationSystemAllowExpiredCard": true
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

{#pecs-add-processor-ex_codeblock_ulf_bvh_jzb}  
Response to a Successful Request

```
{
    "setups": {
        "payments": {
            "cardProcessing": {
                "configurationStatus": {
                    "status": "SUCCESS",
                    "message": "Configuration Instance updated successfully"
                },
                "subscriptionStatus": {
                    "status": "SUCCESS",
                    "message": "success"
                }
            }
        }
    },
    "status": "PROCESSED",
    "submitTimeUtc": "2022-04-04T12:58:02+0000"
}
```

{#pecs-add-processor-ex_codeblock_wlf_bvh_jzb}
