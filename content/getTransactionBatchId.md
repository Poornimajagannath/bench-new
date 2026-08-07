---
title: Get Individual Batch File
generated: true
source: doc-cybersource-payments-openapi
operation_id: getTransactionBatchId
lineage_origin: generated_from_spec
---

# Get Individual Batch File

<!-- section:prose -->
## Overview

You use this endpoint to get Individual Batch File.

<!-- TODO: Add a short customer-facing example once sandbox samples are approved. -->
<!-- /section:prose -->

<!-- section:facts -->
**Method:** `GET`  
**Path:** `/pts/v1/transaction-batches/{id}`  
**Operation ID:** `getTransactionBatchId`

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

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| id | string | no | Unique identifier assigned to the batch file. |
| uploadDate | string | no | Date when the batch template was update. |
| completionDate | string | no | The date when the batch template processing completed. |
| transactionCount | integer | no | Number of transactions in the transaction. |
| acceptedTransactionCount | integer | no | Number of transactions accepted. |
| rejectedTransactionCount | string | no | Number of transactions rejected. |
| status | string | no | The status of you batch template processing. |
| _links.transactions | array | no |  |

## Errors

- `unspecified`: No explicit error schema in fixture — recovery: Treat non-2xx as failure; do not log secrets

## Evidence (from spec)

> "Get Individual Batch File"

> "This API provides details like upload date, completion date, transaction count and accepted and rejected transaction count of the individual batch file using the batch id"

## Provenance

- `lineage_origin`: `generated_from_spec`
- `unit_id`: `cybersource-payments-openapi:ref:getTransactionBatchId`
- `api_name`: CyberSource Payments API (/pts)

Every fact on this page traces to the OpenAPI-derived reference unit. Sandbox only — do not use production credentials from these docs.

<!-- /section:facts -->
