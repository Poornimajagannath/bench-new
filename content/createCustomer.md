---
title: Create a TMS customer
generated: true
source: doc-cybersource-payments-core-openapi
operation_id: createCustomer
lineage_origin: generated_from_spec
---

# Create a TMS customer

<!-- section:prose -->
## Overview

You use this endpoint to create a TMS customer.

<!-- TODO: Add a short customer-facing example once sandbox samples are approved. -->
<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/tms/v2/customers`  
**Operation ID:** `createCustomer`

## Auth

Required scheme(s) from the OpenAPI fixture: `httpSignature`.

## Request

### Body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| buyerInformation | object | yes |  |
| clientReferenceInformation | object | no |  |

## Response

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| id | string | no |  |
| buyerInformation | object | no |  |

## Errors

- `error_schema`: Error payload shaped by ErrorResponse — recovery: Inspect reason/details; fix request or auth; retry in sandbox only

## Evidence (from spec)

> "Create a TMS customer"

## Related workflows

`microform-payer-auth-state-machine`

## Provenance

- `lineage_origin`: `generated_from_spec`
- `unit_id`: `cybersource-payments-core-openapi:ref:createCustomer`
- `api_name`: CyberSource Payments Core (local Relay fixture)

Every fact on this page traces to the OpenAPI-derived reference unit. Sandbox only — do not use production credentials from these docs.

<!-- /section:facts -->
