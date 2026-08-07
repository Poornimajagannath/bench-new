REST Example: Enabling `TMS` with a Template Using the PECS API {#boarding-pecs-tms-enable-ex-rest}
===================================================================================================

Request

```
{
  "organizationId": "ergaergaerg001",
  "commerceSolutions": {
    "tokenManagement": {
      "subscriptionInformation": {
        "enabled": true,
        "selfServiceability": "NOT_SELF_SERVICEABLE"
      },
      "configurationInformation": {
        "templateId": "43107BC1-E3DA-4019-9306-4510AD4DE05F"
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

