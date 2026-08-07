REST Example: Enabling `TMS` Using a Template {#boarding-tms-enable-ex-rest}
============================================================================

Request

```
{
  "registrationInformation": {
    "boardingFlow": "ADDPRODUCT"
  },
  "organizationInformation": {
    "parentOrganizationId": "3b2bwnhbm7cdzath0qcn0luhkpvb",
    "type": "TRANSACTING",
    "configurable": false,
    "businessInformation": {
      "name": "Test Merchant",
      "address": {
        "country": "US",
        "address1": "123 Main",
        "locality": "Seattle",
        "administrativeArea": "WA",
        "postalCode": "99999"
      },
      "businessContact": {
        "firstName": "Jane",
        "lastName": "Smith",
        "phoneNumber": "5551234567",
        "email": "email@domain.com"
      }
    }
  },
  "productInformation": {
    "selectedProducts": {
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

