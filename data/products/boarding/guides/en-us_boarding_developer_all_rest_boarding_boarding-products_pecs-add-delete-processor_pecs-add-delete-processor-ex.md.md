Example: Adding and Deleting a Processor Using the PECS API {#pecs-add-delete-processor-ex}
===========================================================================================

Request

```
{
    "payments": {
        "cardProcessing": {
            "subscriptionInformation": {
                "enabled": true,
                "features": {
                    "cardNotPresent": {
                        "enabled": true
                    },
                    "cardPresent": {
                        "enabled": false
                    }
                }
            },
            "configurationInformation": {
                "configurations": {
                    "common": {
                        "processors": {
                            "amexdirect": {
                                "paymentTypes": {
                                    "VISA": {
                                        "enabled": false
                                    },
                                     "MASTERCARD": {
                                        "enabled": false
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "organizationId": "amextestajtxmid1013"
}
```

{#pecs-add-delete-processor-ex_codeblock_ulf_bvh_jzb}  
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
  "submitTimeUtc": "2023-11-14T06:40:15+0000"
}
```

{#pecs-add-delete-processor-ex_codeblock_wtf_m4g_lzb}
