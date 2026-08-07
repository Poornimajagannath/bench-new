---
title: GET /v1/accounts
generated: true
source: openapi-connect.fixture.json
---

# GET /v1/accounts

**Method:** `GET`  
**Path:** `/v1/accounts`  
**Operation ID:** `GetAccounts`

## Auth

Platform secret key via HTTP Bearer (`sk_test_...` in test mode).
Security: `[{"bearerAuth": []}]`

## Parameters

| Name | In | Required | Type |
| --- | --- | --- | --- |
| limit | query | False | integer |

## Status codes

`200`, `401`

## Notes

List connected accounts

<!-- section: generated -->
