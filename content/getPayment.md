---
title: Retrieve a payment
generated: true
source: doc-cybersource-payments-core-openapi
operation_id: getPayment
lineage_origin: generated_from_spec
---

# Retrieve a payment

<!-- section:prose -->
## Overview

You use this endpoint to retrieve a payment.

<!-- TODO: Add a short customer-facing example once sandbox samples are approved. -->
<!-- /section:prose -->

<!-- section:facts -->
**Method:** `GET`  
**Path:** `/pts/v2/payments/{id}`  
**Operation ID:** `getPayment`

## Auth

Required scheme(s) from the OpenAPI fixture: `httpSignature`.

## Request

### Path parameters

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| id | string | yes | Path parameter id |

### Body fields

_None listed_

## Response

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| id | string | no |  |
| status | string | no |  |

## Errors

- `error_schema`: Error payload shaped by ErrorResponse — recovery: Inspect reason/details; fix request or auth; retry in sandbox only

## Evidence (from spec)

> "Retrieve a payment"

## Related workflows

`microform-payer-auth-state-machine`

## Provenance

- `lineage_origin`: `generated_from_spec`
- `unit_id`: `cybersource-payments-core-openapi:ref:getPayment`
- `api_name`: CyberSource Payments Core (local Relay fixture)

Every fact on this page traces to the OpenAPI-derived reference unit. Sandbox only — do not use production credentials from these docs.

<!-- /section:facts -->
