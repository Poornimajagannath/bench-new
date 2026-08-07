---
title: Check payer authentication enrollment
generated: true
source: doc-cybersource-payments-core-openapi
operation_id: checkMppEnrollment
lineage_origin: generated_from_spec
---

# Check payer authentication enrollment

<!-- section:prose -->
## Overview

You use this endpoint to check payer authentication enrollment.

<!-- TODO: Add a short customer-facing example once sandbox samples are approved. -->
<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/risk/v1/authentications`  
**Operation ID:** `checkMppEnrollment`

## Auth

Required scheme(s) from the OpenAPI fixture: `httpSignature`.

## Request

### Body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| clientReferenceInformation | object | yes |  |
| processingInformation | object | no |  |

## Response

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| id | string | no |  |
| status | string | no |  |

## Errors

- `error_schema`: Error payload shaped by ErrorResponse — recovery: Inspect reason/details; fix request or auth; retry in sandbox only

## Evidence (from spec)

> "Check payer authentication enrollment"

> "Enrollment may return FRICTIONLESS, CHALLENGE, or UNAVAILABLE paths."

## Related workflows

`microform-payer-auth-state-machine`

## Provenance

- `lineage_origin`: `generated_from_spec`
- `unit_id`: `cybersource-payments-core-openapi:ref:checkMppEnrollment`
- `api_name`: CyberSource Payments Core (local Relay fixture)

Every fact on this page traces to the OpenAPI-derived reference unit. Sandbox only — do not use production credentials from these docs.

<!-- /section:facts -->
