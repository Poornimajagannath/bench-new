Reason Codes {#boarding-error-codes}
====================================

These tables list the reason codes and the possible status and reason values that are returned with the response from the Boarding Registration Service (BRS) API and the Product Enablement and Configuration Service (PECS) API. `Cybersource` reserves the right to add new reason codes at any time. If your error handler receives a reason code that it does not recognize, it should use the decision field to determine the result.

BRS API Reason Codes
--------------------

| Reason Code | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200         | Successful. Possible status values: * `PROCESSING`: The registration is still in progress. You can get the latest status by calling the `GET` endpoint using the registration ID. * `SUCCESS`: The request was successful. * `FAILURE`: The registration failed before the organization was created. Refer to the details section in the response for more information. * `PARTIAL`: The registration created the organization successfully but failed in at least on step while configuring it. Refer to the details section in the response for more information. |
| 400         | Bad request. Possible reason values: * `INVALID_DATA` * `SYSTEM_ERROR` * `RESOURCE_NOT_FOUND`                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 422         | Business validations failed. Possible reason values: * `INVALID_DATA`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 500         | Internal server error. Possible reason values: * `SYSTEM_ERROR `                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
[Reason Codes]

Example: Partial Processed Response from the BRS API
----------------------------------------------------

```
{
  "id": "87373503001",
  "submitTimeUtc": "2023-11-16T22:15:02Z",
  "status": "PARTIAL",
  "registrationInformation": {
    "mode": "COMPLETE",
    "boardingPackageId": "15118503001"
  },
  "organizationInformation": {
    "organizationId": "davescustomguitars067",
    "parentOrganizationId": "davescustomguitars"
  },
  "message": "Request was processed successfully",
  "productInformationSetups": [
    {
      "organizationId": "davescustomguitars067",
      "setups": {
        "payments": {
          "cardProcessing": {
            "configurationStatus": {
              "status": "FAILURE",
              "reason": "INVALID_REQUEST",
              "details": [
                {
                  "field": "name",
                  "reason": "/configurations/common/merchantDescriptorInformation/name should contain only alphabets and numeric characters."
                }
              ],
              "message": "Field validation errors"
            },
            "subscriptionStatus": {
              "status": "SUCCESS",
              "message": "success"
            }
          },
          "digitalPayments": {
            "subscriptionStatus": {
              "status": "SUCCESS",
              "message": "success"
            }
          }
        },
        "risk": {
          "fraudManagementEssentials": {
            "configurationStatus": {
              "status": "SUCCESS"
            },
            "subscriptionStatus": {
              "status": "SUCCESS",
              "message": "success"
            }
          }
        },
        "valueAddedServices": {
          "transactionSearch": {
            "subscriptionStatus": {
              "status": "SUCCESS",
              "message": "success"
            }
          },
          "reporting": {
            "subscriptionStatus": {
              "status": "SUCCESS",
              "message": "success"
            }
          }
        }
      }
    }
  ]
}
```

PECS API Reason Codes
---------------------

| Reason Code | Description                                                                                                                                                                                                                                                           |
|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200         | Successful Possible status values: * `PROCESSED`: The request was successful. * `PARTIAL_PROCESSED`: An error occurred and the configuration settings were not updated for one or more products. {#boarding-error-codes_ul_yxh_5sm_lzb}                               |
| 400         | Invalid request Possible status value: * `INVALID_REQUEST` {#boarding-error-codes_ul_mcj_wsm_lzb} Possible reason values: * `MANDATORY_FIELD_MISSING` * `BUSINESS_VALIDATION_FAILED` * `INVALID_VALUE` {#boarding-error-codes_ul_xq2_ssm_lzb}                         |
| 401         | Unauthorized Possible status value: * `UN_AUTHENTICATED` {#boarding-error-codes_ul_urd_ysm_lzb} Possible reason values: * `INVALID_API_KEY` * `UNSUPPORTED_ORG` * `INVALID_ORG_HIERARCHY` {#boarding-error-codes_ul_cx1_msm_lzb}                                      |
| 403         | Forbidden Possible status value: * `UN_AUTHENTICATED` {#boarding-error-codes_ul_n45_zsm_lzb} Possible reason values: * `INVALID_API_KEY ` * `UNSUPPORTED_ORG` * `INVALID_ORG_HIERARCHY` {#boarding-error-codes_ul_qjm_3sm_lzb}                                        |
| 404         | Not found Possible status value: * `NOT_FOUND` {#boarding-error-codes_ul_b4s_btm_lzb} Possible reason value: * `NOT_FOUND` {#boarding-error-codes_ul_apq_hsm_lzb}                                                                                                     |
| 502         | Bad gateway Possible status value: * `BAD_GATEWAY` {#boarding-error-codes_ul_aqr_ctm_lzb} Possible reason values: * `SYSTEM_ERROR` * `SERVER_TIMEOUT` * `SERVICE_TIMEOUT ` * `INVALID_OR_MISSING_CONFIG` * `PROCESSOR_TIMEOUT` {#boarding-error-codes_ul_bdj_2sm_lzb} |
[Reason Codes]

Example: Partial Processed Response from the PECS API
-----------------------------------------------------

```
{
  "setups": {
    "payments": {
      "cardProcessing": {
        "configurationStatus": {
          "status": "FAILURE",
          "reason": "INVALID_REQUEST",
          "details": [
            {
              "field": "paymentTypes",
              "reason": "MASTERCARD,VISA are invalid paymentTypes in /configurations/common/processors/amexdirect/paymentTypes"
            }
          ],
          "message": "Field validation errors"
        },
        "subscriptionStatus": {
          "status": "SUCCESS",
          "message": "success"
        }
      }
    }
  },
  "status": "PARTIAL_PROCESSED",
  "submitTimeUtc": "2023-11-14T06:36:44+0000"
}
```

{#boarding-error-codes_codeblock_wlf_bvh_jzb}
