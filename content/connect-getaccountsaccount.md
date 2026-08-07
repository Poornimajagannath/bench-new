---
title: GET /v1/accounts/{account}
generated: true
source: openapi-connect.fixture.json
---

# GET /v1/accounts/{account}

**Method:** `GET`  
**Path:** `/v1/accounts/{account}`  
**Operation ID:** `GetAccountsAccount`

## Auth

Platform secret key via HTTP Bearer (`sk_test_...` in test mode).
Security: `[{"bearerAuth": []}]`

## Parameters

| Name | In | Required | Type |
| --- | --- | --- | --- |
| account | path | True | string |

## Status codes

`200`, `401`, `404`

## Notes

Retrieve a connected account

<!-- section: generated -->
