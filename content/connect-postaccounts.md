---
title: POST /v1/accounts
generated: true
source: openapi-connect.fixture.json
---

# POST /v1/accounts

**Method:** `POST`  
**Path:** `/v1/accounts`  
**Operation ID:** `PostAccounts`

## Auth

Platform secret key via HTTP Bearer (`sk_test_...` in test mode).
Security: `[{"bearerAuth": []}]`

## Parameters

| Name | In | Required | Type |
| --- | --- | --- | --- |
| Stripe-Version | header | False | string |
| type | body | True | string |
| country | body | True | string |
| email | body | False | string |
| capabilities[card_payments][requested] | body | False | boolean |
| capabilities[transfers][requested] | body | False | boolean |

## Status codes

`200`, `400`, `401`

## Notes

Create a connected account

<!-- section: generated -->
