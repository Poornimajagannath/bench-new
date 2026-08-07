---
title: Process a Pull Funds Reversal
generated: true
source: doc-cybersource-payments-openapi
operation_id: createPullFundsReversal
lineage_origin: generated_from_spec
---

# Process a Pull Funds Reversal

<!-- section:prose -->
## Overview

You use this endpoint to process a Pull Funds Reversal.

<!-- TODO: Add a short customer-facing example once sandbox samples are approved. -->
<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v1/pull-funds-transfer/{id}/reversal`  
**Operation ID:** `createPullFundsReversal`

## Auth

This OpenAPI document does not declare `security` / `securityDefinitions` for the operation. Authenticate with HTTP Signature or JWT per CyberSource REST getting started (sandbox: `apitest.cybersource.com`).

## Request

### Path parameters

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| id | string | yes | Path parameter id |

### Body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| clientReferenceInformation.code | string | no | Originator-generated order reference or tracking number. It is recommended that you send a unique value for each transaction so that you can perform meaningful searches for the transaction.
 |
| clientReferenceInformation.applicationName | string | no | The name of the Connection Method that the originator uses to send a transaction request to CyberSource.
 |
| clientReferenceInformation.applicationVersion | string | no | Version of the CyberSource application or integration used for a transaction.
 |
| clientReferenceInformation.applicationUser | string | no | The entity that is responsible for running the transaction and submitting the processing request to CyberSource. This could be a person, a system, or a connection method.
 |
| reversalInformation.amountDetails.totalAmount | string | yes | Length: <=12. Up to 3 decimal places.  
Type: String, with a non-negative double format.

The total amount of the AFT reversal including all fees.  
a. an amount that is <= the totalAmount of the original AFT  
b. The amount of the transaction, inclusive of all fees assessed for the transaction, including currency conversion fees.  
    Minimum Value: Field must be greater than zero: minimum value is the smallest amount in any given currency.  
c. Multiple successful reversals & refunds of the original AFT transaction are allowed but the sum of the transaction amounts must not total more than the original AFT totalAmount.
 |

## Response

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| id | string | no | A unique identification number to identify the submitted request. It is also appended to the endpoint of the resource.
 |
| submitTimeUtc | string | no | Time of request in UTC.
Format: `YYYY-MM-DDThh:mm:ssZ`

**Example**
`2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.).
The `T` separates the date and the time.
The `Z` indicates UTC.
 |
| status | string | no | The status of the submitted transaction.

Possible values:
- REVERSED
- DECLINED
- INVALID_REQUEST
 |
| errorInformation.reason | string | no | The reason of the status.

Possible values:
- EXPIRED_CARD
- PROCESSOR_DECLINED
- STOLEN_LOST_CARD
- UNAUTHORIZED_CARD
- CVN_NOT_MATCH
- INVALID_CVN
- BLACKLISTED_CUSTOMER
- INVALID_ACCOUNT
- GENERAL_DECLINE
- RISK_CONTROL_DECLINE
- PROCESSOR_RISK_CONTROL_DECLINE
- DEBIT_CARD_USAGE_EXCEEDED_LIMIT
 |
| errorInformation.message | string | no | The detail message related to the status and reason listed above.
 |
| errorInformation.details | array | no |  |
| processorInformation.systemTraceAuditNumber | string | no | This field is returned by authorization and incremental authorization services.
System trace number that must be printed on the customer’s receipt.
 |
| processorInformation.approvalCode | string | no | Issuer-generated approval code for the transaction.
 |
| processorInformation.responseCode | string | no | Transaction status from the processor.
 |
| processorInformation.transactionId | string | no | Network transaction identifier (TID). This value can be used to identify a specific transaction when you are discussing the transaction with your processor.
 |
| _links.self.href | string | no | This is the endpoint of the resource that was created by the successful request. |
| _links.self.method | string | no | `method` refers to the HTTP method that you can send to the `self` endpoint to retrieve details of the resource. |

## Errors

- `unspecified`: No explicit error schema in fixture — recovery: Treat non-2xx as failure; do not log secrets

## Evidence (from spec)

> "Process a Pull Funds Reversal"

> "Reverse an Account Funding Transaction (AFT).
"

## Provenance

- `lineage_origin`: `generated_from_spec`
- `unit_id`: `cybersource-payments-openapi:ref:createPullFundsReversal`
- `api_name`: CyberSource Payments API (/pts)

Every fact on this page traces to the OpenAPI-derived reference unit. Sandbox only — do not use production credentials from these docs.

<!-- /section:facts -->
