---
title: Create a payment authorization
generated: true
source: doc-cybersource-payments-core-openapi
operation_id: createPayment
lineage_origin: generated_from_spec
---

# Create a payment authorization

<!-- section:prose -->
## Overview

You use this endpoint to create a payment authorization.

<!-- TODO: Add a short customer-facing example once sandbox samples are approved. -->
<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**Operation ID:** `createPayment`

## Auth

Required scheme(s) from the OpenAPI fixture: `httpSignature`.

## Request

### Body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| clientReferenceInformation.code | string | yes | Merchant reference code for the transaction |
| orderInformation.amountDetails.totalAmount | string | yes | Order total amount |
| orderInformation.amountDetails.currency | string | yes | ISO 4217 currency code |
| orderInformation.billTo.firstName | string | no |  |
| orderInformation.billTo.lastName | string | no |  |
| paymentInformation.card.number | string | no | Tokenized instrument or test card id — do not send raw PAN |
| paymentInformation.card.expirationMonth | string | no |  |
| paymentInformation.card.expirationYear | string | no |  |
| paymentInformation.card.type | string | no | Card type code |

## Response

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| id | string | no |  |
| status | string | no |  |

## Errors

- `error_schema`: Error payload shaped by ErrorResponse — recovery: Inspect reason/details; fix request or auth; retry in sandbox only

## Evidence (from spec)

> "Create a payment authorization"

> "Authorize a payment in sandbox using tokenized or instrument identifiers. Do not send raw PAN."

## Related workflows

`microform-payer-auth-state-machine`

## Provenance

- `lineage_origin`: `generated_from_spec`
- `unit_id`: `cybersource-payments-core-openapi:ref:createPayment`
- `api_name`: CyberSource Payments Core (local Relay fixture)

Every fact on this page traces to the OpenAPI-derived reference unit. Sandbox only — do not use production credentials from these docs.

<!-- /section:facts -->
