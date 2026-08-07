REST Example: Creating a Structural Organization {#boarding-reg-create-structural-api-example}
==============================================================================================

Request

```
{
    "registrationInformation": {
        "boardingFlow": "ENTERPRISE"
    },
    "organizationInformation": {
        "organizationId": "yourstructuralorgidhere",
        "status": "LIVE",
        "parentOrganizationId": "yourmercahntorgidhere",
        "type": "STRUCTURAL",
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
        }
    }
}
```

Response to a Successful Request

```
{
    "id": "1695804002",
    "submitTimeUtc": "2022-04-13T20:58:28Z",
    "status": "SUCCESS",
    "registrationInformation": {
        "mode": "COMPLETE",
        "boardingPackageId": "123456789012"
    },
    "organizationInformation": {
        "organizationId": "yourstructuralorgidhere",
        "parentOrganizationId": "yourmercahntorgidhere"
    },
    "message": "Request was processed successfully"
}
```

