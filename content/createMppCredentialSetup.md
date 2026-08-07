---
title: Create payer authentication / MPP credential setup
generated: true
source: doc-cybersource-payments-core-openapi
operation_id: createMppCredentialSetup
lineage_origin: generated_from_spec
---

# Create payer authentication / MPP credential setup

<!-- section:prose -->
## Overview

You use this endpoint to create payer authentication / MPP credential setup.

<!-- TODO: Add a short customer-facing example once sandbox samples are approved. -->
<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/risk/v1/authentication-setups`  
**Operation ID:** `createMppCredentialSetup`

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

> "Create payer authentication / MPP credential setup"

> "Payer Authentication setup prerequisite before enrollment. Microform tokenize alone is not 3DS completion."

## Related workflows

`microform-payer-auth-state-machine`

## Provenance

- `lineage_origin`: `generated_from_spec`
- `unit_id`: `cybersource-payments-core-openapi:ref:createMppCredentialSetup`
- `api_name`: CyberSource Payments Core (local Relay fixture)

Every fact on this page traces to the OpenAPI-derived reference unit. Sandbox only — do not use production credentials from these docs.

<!-- /section:facts -->
