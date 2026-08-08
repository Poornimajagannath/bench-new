---
title: Marketplace Capture with Foreign Retailers
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_foreign_capture_intro
lineage_origin: generated_from_endpoint_fact
---

# Marketplace Capture with Foreign Retailers

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments/`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments/`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-foreign-capture-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-foreign-capture-intro)  

## Request body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| aggregatorInformation.subMerchant.country |  | yes | Set this field to the retailer country. |
| clientReferenceInformation.code |  | yes | This field value maps from the original authorization, sale, or credit transaction. |
| clientReferenceInformation.partner.thirdPartyCertificationNumber |  | yes | `Cybersource` provides the value for this field. |
| merchantInformation.merchantDescriptor.country |  | yes | Set this field to the marketplace country. |
| orderInformation.amountDetails.currency |  | yes |  |
| orderInformation.amountDetails.totalAmount |  | yes |  |

## Example request

```json
{
    "aggregatorInformation" : {
        "subMerchant" : {
            "country" : "AU"
        }
    },{
    "clientReferenceInformation": {
        "code": "ABC123",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    {
    "merchantInformation" : {
        "merchantDescriptor" : {
            "country" : "GB"
        }
    },    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100.00",
            "currency": "GBP"
    }
}
```

## Example response

```json
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/captures/6662994431376681303954/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/captures/6662994431376681303954"
        }
    },
    "clientReferenceInformation": {
        "code": "1666299443215"
    },
    "id": "6662994431376681303954",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100.00",
            "currency": "GBP"
        }
    },
    "reconciliationId": "66535942B9CGT52U",
    "status": "PENDING",
    "submitTimeUtc": "2024-10-20T20:57:23Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:781be423`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
