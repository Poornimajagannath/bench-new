---
title: Create a credit
generated: true
source: doc-cybersource-payments-core-openapi
operation_id: createCredit
lineage_origin: generated_from_spec
---

# Create a credit

<!-- section:prose -->
## Overview

You use this endpoint to create a credit.

<!-- TODO: Add a short customer-facing example once sandbox samples are approved. -->
<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/credits`  
**Operation ID:** `createCredit`

## Auth

Required scheme(s) from the OpenAPI fixture: `httpSignature`.

## Request

### Body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| clientReferenceInformation.code | string | no |  |
| orderInformation.amountDetails.totalAmount | string | yes |  |
| orderInformation.amountDetails.currency | string | no |  |

## Response

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| id | string | no |  |
| status | string | no |  |

## Errors

- `error_schema`: Error payload shaped by ErrorResponse — recovery: Inspect reason/details; fix request or auth; retry in sandbox only

## Evidence (from spec)

> "Create a credit"

## Related workflows

`microform-payer-auth-state-machine`

## Provenance

- `lineage_origin`: `generated_from_spec`
- `unit_id`: `cybersource-payments-core-openapi:ref:createCredit`
- `api_name`: CyberSource Payments Core (local Relay fixture)

Every fact on this page traces to the OpenAPI-derived reference unit. Sandbox only — do not use production credentials from these docs.

<!-- /section:facts -->
