Refund {#paybybank-refund-intro}
================================

Send a refund request to issue a full or partial refund to the customer's bank account. Refunds can be requested only when the sale is settled. A refund request requires the request ID from the sale response.

> IMPORTANT You can only refund payments processed with GBP currency.

Endpoints
---------

**Production:** `POST ``https://api.example.com``/pts/v2/payments/`*{id}*`/refunds`{#paybybank-refund-intro_d17e372}  
**Test:** `POST ``https://apitest.example.com``/pts/v2/payments/`*{id}*`/refunds`{#paybybank-refund-intro_d17e385}  
The *{id}* is the request ID contained in the original transaction request.

Response Statuses
-----------------

`Payment Gateway` responds to your refund request with one of these statuses in the status field:
* `PENDING`: The refund request is accepted and is processing. A webhook notification informs you when the refund is complete. See [Webhook Subscriptions](/docs/gateway/en-us/pay-by-bank/developer/all/rest/pay-by-bank/paybybank-intro-services/paybybank-webhook-intro.md ""). If you do not receive a webhook notification, send a check status request. See [Check Status](/docs/gateway/en-us/pay-by-bank/developer/all/rest/pay-by-bank/paybybank-intro-services/paybybank-status-intro.md "").
* `REJECT`: The refund request is not successful. Send a new refund request.
  {#paybybank-refund-intro_status-refund}  
  `Payment Gateway` also responds with a reason code in the processorInformation.responseCode field. For more information about reason codes, see [Reason Codes and Pay by Bank Response Codes](/docs/gateway/en-us/pay-by-bank/developer/all/rest/pay-by-bank/paybybank-reference-codes.md "").  
  If you send a check status request to retrieve the current refund status, these are the possible responses:
* `PENDING`: The refund request is accepted but is not complete. Continue to request the check status service in 60-minute intervals until the status updates.
* `REFUNDED`: The settled amount is successfully refunded back to the customer's account.
* `REJECT`: The refund request is not successful. An unsuccessful request can be due to either Pay by Bank rejecting the transaction or a technical error.
  {#paybybank-refund-intro_status-refund-check}

Required Fields for Processing a Refund {#paybybank-refund-req-fields}
======================================================================

clientReferenceInformation.code
:

orderInformation.amountDetails.currency
:
Set to `GBP`.

orderInformation.amountDetails.totalAmount
:

paymentInformation.paymentType.method.name
:
Set to `bofaPayByBank`.

paymentInformation.paymentType.name
:
Set to `bankTransfer`.

processingInformation.actionList
:
Set to `AP_REFUND`.
{#paybybank-refund-req-fields_dl_gk2_4ft_fgc}

`REST` Example: Issuing a Refund {#paybybank-refund-ex-rest}
============================================================

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
    "actionList": ["AP_REFUND"]
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "1999.00",
      "currency": "GBP"
    }
  }
}
```

Response to a Successful Request

```
{
    "processorInformation": {
        "responseCode": "00001",
        "transactionId": "1a043850-322b-2e06-334e-0c4b0c41083f"
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "1999.00",
            "currency": "LOgGSXjNbVmXgvrhXlFMaablr"
        }
    },
    "clientReferenceInformation": {
        "code": "TC84100-1"
    },
    "reconciliationId": "KOZX0DMQKX18",
    "message": "Request was processed successfully.",
    "status": "PENDING",
    "id": "7545091091436400404807",
    "submitTimeUtc": "2025-08-06T19:38:29Z"
}
```

