---
title: Get a List of Batch Files
generated: true
source: doc-cybersource-payments-openapi
operation_id: getTransactionBatches
lineage_origin: generated_from_spec
---

# Get a List of Batch Files

<!-- section:prose -->
## Overview

You use this endpoint to get a List of Batch Files.

<!-- TODO: Add a short customer-facing example once sandbox samples are approved. -->
<!-- /section:prose -->

<!-- section:facts -->
**Method:** `GET`  
**Path:** `/pts/v1/transaction-batches`  
**Operation ID:** `getTransactionBatches`

## Auth

This OpenAPI document does not declare `security` / `securityDefinitions` for the operation. Authenticate with HTTP Signature or JWT per CyberSource REST getting started (sandbox: `apitest.cybersource.com`).

## Request

### Body fields

_None listed_

## Response

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| transactionBatches | array | no |  |
| _links.self.href | string | no |  |
| _links.self.method | string | no |  |
| submitTimeUtc | string | no | Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ`
**Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.).
The `T` separates the date and the time. The `Z` indicates UTC.

Returned by Cybersource for all services.
 |

## Errors

- `unspecified`: No explicit error schema in fixture — recovery: Treat non-2xx as failure; do not log secrets

## Evidence (from spec)

> "Get a List of Batch Files"

> "Provide the date and time search range to get a list of Batch Files ready for settlement"

## Provenance

- `lineage_origin`: `generated_from_spec`
- `unit_id`: `cybersource-payments-openapi:ref:getTransactionBatches`
- `api_name`: CyberSource Payments API (/pts)

Every fact on this page traces to the OpenAPI-derived reference unit. Sandbox only — do not use production credentials from these docs.

<!-- /section:facts -->
