Check a Status {#pay-by-bank-payto-checkstatus-intro}
=====================================================

Request a check status to retrieve the current status of a transaction request. The check status request is helpful when know when a pending status updates. The check status request requires the request ID from the response of the corresponding request you are attempting to retrieve.

Endpoints {#pay-by-bank-payto-checkstatus-intro_section_l3f_xrs_fgc}
--------------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#pay-by-bank-payto-checkstatus-intro_d7e345}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#pay-by-bank-payto-checkstatus-intro_d7e355}

Response Statuses {#pay-by-bank-payto-checkstatus-intro_check-status-response}
------------------------------------------------------------------------------

If you send a check status request to retrieve the current sale status, these are the possible responses:
* `FAILED`: The sale request failed. A failed request can be due to either Pay by Bank rejecting the transaction or due to a technical error.
* `FUNDED`: The sale request is funded for the requested amount.
* `PENDING`: The sale request is accepted but is not complete. Request the check status service to retrieve status updates.
* `SETTLED`: The sale request is settled for the requested amount.
  {#pay-by-bank-payto-checkstatus-intro_status-sale-check}  
  If you send a check status request to retrieve the current refund status, these are the possible responses:
* `FAILED`: The refund request failed. A failed request can be due to PayTo Pay by Bank rejecting the transaction or due to a technical error.
* `PENDING`: The sale request is accepted but is not complete. Request the check status service to retrieve status updates.
* `REFUNDED`: The settled amount is successfully refunded.
  {#pay-by-bank-payto-checkstatus-intro_status-refund-check}

Required Fields for Checking a Status {#pay-by-bank-payto-checkstatus-req-fields}
=================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:
Set to an 18-character value or less.

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to `payToPayByBank`.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `bankTransfer`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_STATUS`.
{#pay-by-bank-payto-checkstatus-req-fields_dl_pvj_hhl_fgc}

Example: Checking a Status {#pay-by-bank-payto-checkstatus-ex-rest}
===================================================================

Request

```
{
  "paymentInformation": {
    "paymentType": {
      "name": "bankTransfer",
      "method": {
        "name": "payToPayByBank"
      }
    }
  },
  "processingInformation": {
    "actionList": ["AP_STATUS"]
  }
}
```

Response to a Successful Request

```
{
    "processorInformation": {
        "responseCode": "00005"
    },
    "reconciliationId": "KOZX0DMQKX0C",
    "message": "Request was processed successfully.",
    "status": "FUNDED",
    "id": "7544157383456089204805",
    "submitTimeUtc": "2025-08-05T17:42:18Z"
}
```

