Example: Updating a Batch Group Using the API {#pecs-update-batch-ex}
=====================================================================

Request

```
{
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
            "processors": {
              "barclayshiso": {
                "paymentTypes": {
                  "VISA": {
                    "enabled": true
                  }
                },
                "batchGroup": "barclays_hiso_03"
              }
            }
          }
        }
      }
    }
  },
  "organizationId": "davestestguitarsaad009"
}
```

{#pecs-update-batch-ex_codeblock_ulf_bvh_jzb}  
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
  "submitTimeUtc": "2023-11-14T06:33:34+0000"
}
```

{#pecs-update-batch-ex_codeblock_wlf_bvh_jzb}
