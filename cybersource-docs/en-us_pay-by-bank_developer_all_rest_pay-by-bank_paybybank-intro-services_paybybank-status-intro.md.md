Check Status {#paybybank-status-intro}
======================================

Send a check status request to retrieve status updates for either a pending sale or refund. A check status request requires the request ID from the sale response or the refund response, which is the id field value. `Cybersource` recommends using the check status service only when you do not receive a webhook notification. To set up a webhook subscription, see [Webhook Subscriptions](/docs/cybs/en-us/pay-by-bank/developer/all/rest/pay-by-bank/paybybank-intro-services/paybybank-webhook-intro.md "").

Endpoints
---------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*{#paybybank-status-intro_d17e193}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*{#paybybank-status-intro_d17e205}  
Set the *`{id}`* to the request ID of the API service you are retrieving.

Response Statuses {#paybybank-status-intro_section_jgq_qxp_jdc}
---------------------------------------------------------------

`Cybersource` responds to your check sale status request with one of these statuses in the status field:

Check Status for a Sale
:
* `ABANDONED`: The customer did not complete checkout within the allotted time, and the redirect URL has expired.
* `COMPLETED`: The customer completed the checkout process.
* `PENDING`: The sale request is accepted but is not complete. Request the check status service to retrieve status updates.
* `REJECT`: The sale request failed. A failed request can be due to either Pay by Bank rejecting the transaction or due to a technical error.
* `SETTLED`: The sale request is settled for the requested amount.

Check Status for a Refund
:
* `PENDING`: The refund request is accepted but is not complete. Request the check status service to retrieve status updates.
* `REFUNDED`: The settled amount is successfully refunded.
* `REJECT`: The refund request failed. A failed request can be due to either Pay by Bank rejecting the transaction or due to a technical error.

The check status service also responds with a reason code in the processorInformation.responseCode field. For more information about reason codes, see [Reason Codes and Pay by Bank Response Codes](/docs/cybs/en-us/pay-by-bank/developer/all/rest/pay-by-bank/paybybank-reference-codes.md "").

Required Fields for a Check Status Request {#paybybank-status-req-fields}
=========================================================================

clientReferenceInformation.code
:

paymentInformation.paymentType.method.name
:
Set to `bofaPayByBank`.

paymentInformation.paymentType.name
:
Set to `bankTransfer`.

processingInformation.actionList
:
Set to `AP_STATUS`.
{#paybybank-status-req-fields_dl_ztt_4ft_fgc}

`REST` Example: Requesting a Check Status {#paybybank-status-ex-rest}
=====================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "TC84100-1"
  },
  "paymentInformation": {
    "paymentType": {
      "name": "bankTransfer",
      "method": {
        "name": "bofaPayByBank"
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
        "responseCode": "00004"
    },
    "clientReferenceInformation": {
        "code": "TC84100-1"
    },
    "reconciliationId": "KPEPKDMPHGA3",
    "message": "Request was processed successfully.",
    "status": "SETTLED",
    "id": "7545090267166390604807",
    "submitTimeUtc": "2025-08-06T19:37:06Z"
}
```

