---
title: POST /v1/account_links
generated: true
source: openapi-connect.fixture.json
---

# POST /v1/account_links

**Method:** `POST`  
**Path:** `/v1/account_links`  
**Operation ID:** `PostAccountLinks`

## Auth

Platform secret key via HTTP Bearer (`sk_test_...` in test mode).
Security: `[{"bearerAuth": []}]`

## Parameters

| Name | In | Required | Type |
| --- | --- | --- | --- |
| account | body | True | string |
| refresh_url | body | True | string |
| return_url | body | True | string |
| type | body | True | string |

## Status codes

`200`, `400`, `401`

## Notes

Create an Account Link for onboarding

<!-- section: generated -->
