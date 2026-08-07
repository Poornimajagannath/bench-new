REST Example: Creating a Transacting Organization {#boarding-reg-create-new-transacting-api-example}
====================================================================================================

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

Response to a Successful Request

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

