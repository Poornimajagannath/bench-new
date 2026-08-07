---
title: Get Transaction Details for a given Batch Id
generated: true
source: doc-cybersource-payments-openapi
operation_id: getTransactionBatchDetails
lineage_origin: generated_from_spec
---

# Get Transaction Details for a given Batch Id

<!-- section:prose -->
## Overview

You use this endpoint to get Transaction Details for a given Batch Id.

<!-- TODO: Add a short customer-facing example once sandbox samples are approved. -->
<!-- /section:prose -->

<!-- section:facts -->
**Method:** `GET`  
**Path:** `/pts/v1/transaction-batch-details/{id}`  
**Operation ID:** `getTransactionBatchDetails`

## Auth

This OpenAPI document does not declare `security` / `securityDefinitions` for the operation. Authenticate with HTTP Signature or JWT per CyberSource REST getting started (sandbox: `apitest.cybersource.com`).

## Request

### Path parameters

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| id | string | yes | Path parameter id |

### Body fields

_None listed_

## Response

_None listed_

## Errors

- `unspecified`: No explicit error schema in fixture — recovery: Treat non-2xx as failure; do not log secrets

## Evidence (from spec)

> "Get Transaction Details for a given Batch Id"

> "Provides real-time detailed status information about the transactions that you previously uploaded in the Business Center or processed with the Offline Transaction File Submission "

## Provenance

- `lineage_origin`: `generated_from_spec`
- `unit_id`: `cybersource-payments-openapi:ref:getTransactionBatchDetails`
- `api_name`: CyberSource Payments API (/pts)

Every fact on this page traces to the OpenAPI-derived reference unit. Sandbox only — do not use production credentials from these docs.

<!-- /section:facts -->
