Cloud Mode Payment Services {#sis-pymnt-svcs-cloud-mode-intro}
==============================================================

Use this information to process payment services available in the Acceptance Devices app when operated in Cloud mode. In this mode, the point-of-sale (POS) system communicates over the cloud with the Acceptance Devices app on the terminal.  
For information about other modes available in the Acceptance Devices app, see:

* [Local Mode Payment Services](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro.md "")
* [Standalone Mode Payment Services](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-standalone-mode-intro.md "")
  {#sis-pymnt-svcs-cloud-mode-intro_ul_l5b_yqm_3fc}

Communication Protocol Used in Cloud Mode {#sis-pymnt-svcs-cloud-mode-comm-protocol}
====================================================================================

When operating the solution in Cloud mode, the communication protocol used between the Acceptance Devices app and the point-of-sale (POS) system is a single HTTPS request to the backend.  
The transaction response can be sent either synchronously or asynchronously:

Synchronously
:
The POS system keeps the connection open until the transaction is completed and the response is provided with the full transaction details. The backend timeout setting is 180 seconds.

Asynchronously
:
The POS system receives a response with an interaction identifier after the transaction is started. The interaction identifier can then be used to check the transaction events. After the transaction is completed, the interaction identifier can be used to get the transaction identifier. The transaction identifier can then be used to get the full transaction and receipt details. For more information, see [Receiving Transaction Responses Asynchronously](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-txn-resp-async-api-intro.md "").
{#sis-pymnt-svcs-cloud-mode-comm-protocol_dl_fc1_kvl_wbc}

Generating a Bearer Token for Authentication {#sis-pymnt-svcs-cloud-mode-bearer-tkn-intro}
==========================================================================================

Use this information to generate a bearer token for authentication. A unique bearer token is required to authenticate each payment transaction request when the app is in Cloud mode.

Generate a Bearer Token for Authentication {#sis-pymnt-svcs-cloud-mode-bearer-token-task}
=========================================================================================

Generate a new bearer token before sending a transaction request.
IMPORTANT Meta keys are not supported for bearer token generation.  
Follow these steps to generate a bearer token:

1. Create a P12 certificate for the transacting merchant ID (MID).
2. Construct a message using a JSON web Token (JWT) by following the steps shown in the [*Getting Started with REST Developer Guide*](https://developer.example.com/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-jwt-const-intro.md "").
3. Set the digest field (message body) in the JWT as blank.
4. Use the JWT as the bearer token to authenticate the payment transaction request.

Sale {#sis-pymnt-svcs-cloud-sale-api-intro}
===========================================

Use this information to process a sale transaction when the app is in Cloud mode. This transaction combines an authorization and a capture into a single transaction.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for a Sale {#sis-pymnt-svcs-cloud-sale-api-reqfields}
=====================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

REST Example: Sale {#sis-pymnt-svcs-cloud-sale-api-ex-rest}
===========================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "PaymentRequest",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "amountDetails": {
            "amount": "1.00",
            "currency": "GBP"
        }
    }
}
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "1541387b383d456aabb81cdf558b4e8e",
        "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc" : "2023-12-01T20:24:47+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "1.00",
          "refundableAmount" : "1.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "CARD",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014622903166318504010"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938238\nMerchant ID: **37599\nTerminal ID: ****0063\n\n1541387b383d456aabb81cdf558b4e8e\n21:24:51: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938238"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "1541387b383d456aabb81cdf558b4e8e"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:24:51"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938238\nMerchant ID: **37599\nTerminal ID: ****0063\n\n1541387b383d456aabb81cdf558b4e8e\n21:24:51: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938238"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "1541387b383d456aabb81cdf558b4e8e"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:24:51"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Refund {#sis-pymnt-svcs-cloud-refund-api-intro}
===============================================

Use this information to process a refund when the app is in Cloud mode. This type of refund includes a reference to the original transaction for a full or partial transaction amount. Stand-alone credits are also supported in this Acceptance Devices solution. For more information, see [Stand-Alone Credit](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-cloud-standalone-credit-api-intro.md "").  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for a Refund {#sis-pymnt-svcs-cloud-refund-api-reqfields}
=========================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `LinkedRefundRequest`.

request.transactionId
:
Set the value to the `id` field value from the original transaction.

Optional Fields for a Refund {#sis-pymnt-svcs-cloud-refund-api-optfields}
=========================================================================

Use the optional amount and currency fields to process a partial refund. Otherwise, the full amount will be refunded.

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

REST Example: Refund {#sis-pymnt-svcs-cloud-refund-api-ex-rest}
===============================================================

Request

```
{ 
    "serialNumber": "1850000000",
    "request": {
        "type": "LinkedRefundRequest",
        "transactionId": "8fe5fa21d0814424bcec4997c9dc89c4",
        "amountDetails": {
            "amount": "1.00",
            "currency": "GBP"
        }
    }
}
```

Response to a Successful Request

```
{
      "type" : "LinkedRefundResponse",
      "message" : "Refund approved",
      "transactionDetails" : {
        "id" : "8fe5fa21d0814424bcec4997c9dc89c4",
        "merchantReferenceCode" : "e94e3aa304514140ae1700ba0959c7c5",
        "submitTimeUtc" : "2023-12-01T20:57:30+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "0.00",
          "refundableAmount" : "0.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "CARD",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014642534986108604008"
      },
      "linkedOperations" : [ {
        "id" : "b383db1aecab46d89f1dbec8b0a9aa90",
        "type" : "REFUND",
        "amount" : "1.00",
        "status" : "APPROVED",
        "submitTimeUtc" : "2023-12-01T20:57:48+0000"
      } ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nVoid\n-£1.00\n\n\nReversal accepted.\n\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Keyed\n\nAuthorization: -\nMerchant ID: **37599\nTerminal ID: ****0063\n\nb383db1aecab46d89f1dbec8b0a9aa90\n21:57:50: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Void"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "b383db1aecab46d89f1dbec8b0a9aa90"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:57:50"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Reversal accepted."
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nVoid\n-£1.00\n\n\nReversal accepted.\n\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Keyed\n\nAuthorization: -\nMerchant ID: **37599\nTerminal ID: ****0063\n\nb383db1aecab46d89f1dbec8b0a9aa90\n21:57:50: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Void"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "b383db1aecab46d89f1dbec8b0a9aa90"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:57:50"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Reversal accepted."
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Stand-Alone Credit {#sis-cloud-standalone-credit-api-intro}
===========================================================

Use this information to process a stand-alone credit in Cloud mode. This type of transaction is used to process a credit without reference to the original transaction. The customer is required to present their card for this type of transaction.

> WARNING
> When processing a stand-alone credit, there is no limit on the credit amount because there is no reference to the original transaction amount. The recommendation is to use a refund transaction whenever possible. For more information, see [Refund](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-refund-api-intro.md "").  
> Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for a Stand-Alone Credit {#sis-cloud-standalone-credit-api-reqfields}
=====================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `StandaloneRefundRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

REST Example: Stand-Alone Credit {#sis-cloud-standalone-credit-api-ex-rest}
===========================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
       "type": "StandaloneRefundRequest",
       "merchantReferenceCode": "2490c8ec0e2f4b509526815714313e33",
       "amountDetails": {
           "amount": "1.00",
           "currency": "GBP"
       }
    }
}
```

Response to a Successful Request

```
{
      "type" : "StandaloneRefundResponse",
      "message" : "Refund approved",
      "transactionDetails" : {
        "id" : "3043e0b61fad4c5483db3d498309460f",
        "merchantReferenceCode" : "2490c8ec0e2f4b509526815714313e33",
        "submitTimeUtc" : "2023-12-01T21:04:19+0000",
        "amountDetails" : {
          "amount" : "1.00",
          "currency" : "GBP"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "AMERICAN_EXPRESS",
          "maskedPan" : "374245XXXXX0001"
        }
      },
      "additionalInformation" : {
        "requestId" : "7014646720206287504012"
      },
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nRefund\n-£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks AMEX\nAccount: *** **** **** 0001\nEntry Mode: Chip\nAID: A0000000250100\n\nTransaction: -\nAuthorization: -\nMerchant ID: *****67890\nTerminal ID: ****0026\n\n3043e0b61fad4c5483db3d498309460f\n10:04:19 PM: 12/1/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks AMEX"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "*** **** **** 0001"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000250100"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Chip"
              },
              "CLEARING_DETAILS_TRANSACTION_IDENTIFIER" : {
                "label" : "Transaction",
                "value" : "-"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "*****67890"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0026"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Refund"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "3043e0b61fad4c5483db3d498309460f"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "12/1/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "10:04:19 PM"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nRefund\n-£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks AMEX\nAccount: *** **** **** 0001\nEntry Mode: Chip\nAID: A0000000250100\n\nTransaction: -\nAuthorization: -\nMerchant ID: *****67890\nTerminal ID: ****0026\n\n3043e0b61fad4c5483db3d498309460f\n10:04:19 PM: 12/1/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks AMEX"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "*** **** **** 0001"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000250100"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Chip"
              },
              "CLEARING_DETAILS_TRANSACTION_IDENTIFIER" : {
                "label" : "Transaction",
                "value" : "-"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "*****67890"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0026"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Refund"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "3043e0b61fad4c5483db3d498309460f"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "12/1/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "10:04:19 PM"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Requesting a Check Transaction Status {#sis-pymnt-svcs-cloud-txn-status-api-intro}
==================================================================================

Use this information to request a check transaction status in Cloud mode. This transaction is used to obtain response data for a transaction that was lost or timed out.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields to Request a Check Transaction Status {#sis-pymnt-svcs-cloud-txn-status-api-reqfields}
======================================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `TransactionLookupRequest`.

request.idType
:
Set the value to `TRANSACTION_ID` or `MERCHANT_REFERENCE_CODE`.

request.id
:
Set the value to the `id` or merchantReferenceCode field value from the original transaction.

REST Example: Request a Check Transaction Status {#sis-pymnt-svcs-cloud-txn-status-api-ex-rest}
===============================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "TransactionLookupRequest",
        "idType": "TRANSACTION_ID",
        "id": "1541387b383d456aabb81cdf558b4e8e"
    }
}
```

Response to a Successful Request

```
{
      "type" : "TransactionLookupResponse",
      "transactionDetails" : {
        "id" : "1541387b383d456aabb81cdf558b4e8e",
        "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc" : "2023-12-01T20:24:47+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "1.00",
          "refundableAmount" : "1.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "CARD",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014622903166318504010"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938238\nMerchant ID: **37599\nTerminal ID: ****0063\n\n1541387b383d456aabb81cdf558b4e8e\n21:24:51: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938238"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "1541387b383d456aabb81cdf558b4e8e"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:24:51"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938238\nMerchant ID: **37599\nTerminal ID: ****0063\n\n1541387b383d456aabb81cdf558b4e8e\n21:24:51: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938238"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "1541387b383d456aabb81cdf558b4e8e"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:24:51"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Cancel Transaction {#sis-pymnt-svcs-cloud-cancel-txn-api-intro}
===============================================================

Use this information to process a cancel transaction request in Cloud mode. This request is sent to interrupt an in-process transaction.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields to Cancel Transaction {#sis-pymnt-svcs-cloud-cancel-txn-api-reqfields}
======================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `CancelRequest`.

REST Example: Cancel Transaction {#sis-pymnt-svcs-cloud-cancel-txn-api-ex-rest}
===============================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "CancelRequest"
    }
}
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment aborted",
      "transactionDetails" : {
        "id" : "b6522aeb9d8d49b386f7c67852581145",
        "merchantReferenceCode" : "50c86aaa02ed4c0bb4b4b596379713f7",
        "submitTimeUtc" : "2023-12-01T20:30:05+0000",
        "captured" : false,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "0.00",
          "refundableAmount" : "0.00"
        }
      },
      "processingDetails" : {
        "status" : "ABORTED",
        "verificationMethod" : "UNKNOWN",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "00",
          "expirationYear" : "00",
          "type" : "UNKNOWN",
          "maskedPan" : ""
        }
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nCanceled transaction.\n\n\nEntry Mode: Contactless\nAID: NULL\n\n\nb6522aeb9d8d49b386f7c67852581145\n21:30:05: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "NULL"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "b6522aeb9d8d49b386f7c67852581145"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:30:05"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Canceled transaction."
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nCanceled transaction.\n\n\nEntry Mode: Contactless\nAID: NULL\n\n\nb6522aeb9d8d49b386f7c67852581145\n21:30:05: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "NULL"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "b6522aeb9d8d49b386f7c67852581145"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:30:05"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Canceled transaction."
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
    }
```

Sale with On-Reader Tipping {#sis-pymnt-svcs-cloud-sale-on-reader-tip-api-intro}
================================================================================

Use this information to process a sale with on-reader tipping in Cloud mode. At the start of each transaction, the terminal prompts the customer to add a tip by showing suggested tip amounts. The customer selects or enters a tip amount on the terminal before presenting their payment card.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for a Sale with On-Reader Tipping {#sis-pymnt-svcs-cloud-sale-on-reader-tip-api-reqfields}
==========================================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

request.askForTip
:
Set the value to `ON_DEVICE`.

REST Example: Sale with On-Reader Tipping {#sis-pymnt-svcs-cloud-sale-on-reader-tip-api-ex-rest}
================================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "adf0fa5ca70d462ba5fc0249436b656c",
      "amountDetails" : {
        "amount" : "5.00",
        "currency" : "GBP"
        },
      "askForTip" : "ON_DEVICE"
    }
}
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "55678c8b152046f7b1d77fd2286ce392",
        "merchantReferenceCode" : "adf0fa5ca70d462ba5fc0249436b656c",
        "submitTimeUtc" : "2023-12-01T21:01:23+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "6.00",
          "capturedAmount" : "6.00",
          "refundableAmount" : "6.00",
          "includedTipAmount" : "1.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "CARD",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014644863036208304012"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\nPurchase Amount: £5.00\nTip Amount: £1.00\nTotal Amount: £6.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938252\nMerchant ID: **37599\nTerminal ID: ****0063\n\n55678c8b152046f7b1d77fd2286ce392\n22:01:27: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938252"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "55678c8b152046f7b1d77fd2286ce392"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£6.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "22:01:27"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\nPurchase Amount: £5.00\nTip Amount: £1.00\nTotal Amount: £6.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938252\nMerchant ID: **37599\nTerminal ID: ****0063\n\n55678c8b152046f7b1d77fd2286ce392\n22:01:27: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938252"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "55678c8b152046f7b1d77fd2286ce392"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£6.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "22:01:27"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Sale with On-Receipt Tipping {#sis-cloud-sale-on-receipt-tip-intro}
===================================================================

Use this information to process a sale with on-receipt tipping when the app is in Cloud mode. After the original transaction is pre-authorized, the customer writes the tip or total amount on the printed receipt. A follow-on tip adjust request must be sent within 24 hours to capture the transaction. For more information, see [Tip Adjust](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-cloud-sale-on-receipt-tip-intro/sis-cloud-sale-on-receipt-tip-adjust-intro.md "").

> WARNING
> By using this feature, you assume the risk of overcaptures being declined and increased chargebacks, so use it only when necessary. Process sales with on-reader tipping, whenever possible. For more information, see [Sale with On-Reader Tipping](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-sale-on-reader-tip-api-intro.md "").  
> Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for a Sale with On-Receipt Tipping {#sis-cloud-sale-on-receipt-tip-api-reqfields}
=================================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

request.capture
:
Set the value to `false`.

request.askForTip
:
Set the value to `ON_RECEIPT`.

REST Example: Sale with On-Receipt Tipping {#sis-cloud-sale-on-receipt-tip-api-ex-rest}
=======================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "1ce594be142142f4913cca805830a176",
      "amountDetails" : {
        "amount" : "20.00",
        "currency" : "USD"
      },
      "capture" : false,
      "askForTip" : "ON_RECEIPT"
      }
}
```

Response to a Successful Request

```
{
  "type" : "PaymentResponse",
  "message" : "Payment approved",
  "transactionDetails" : {
    "id" : "c6174c80b81f4413a4b9f2065c5431c7",
    "merchantReferenceCode" : "1ce594be142142f4913cca805830a176",
    "submitTimeUtc" : "2024-03-20T09:19:41+0000",
    "captured" : false,
    "amountDetails" : {
      "currency" : "USD",
      "amount" : "20.00",
      "capturedAmount" : "20.00",
      "refundableAmount" : "20.00"
    }
  },
  "processingDetails" : {
    "status" : "APPROVED",
    "verificationMethod" : "NONE",
    "entryMode" : "NFC_ICC",
    "card" : {
      "expirationMonth" : "12",
      "expirationYear" : "2025",
      "type" : "CARD",
      "maskedPan" : "476173XXXXXX0119",
      "countryCode" : "840"
    }
  },
  "additionalInformation" : {
    "instrumentId" : "7030000000022690119",
    "requestId" : "7109263864326505004007"
  },
  "linkedOperations" : [ ],
  "tipAdjustStatus" : "ADJUSTABLE",
  "receipts" : {
    "merchantReceipt" : {
      "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n1234567\n\nSale\n$20.00\nPlease retain receipt!\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 002000\nMerchant ID: **37599\nTerminal ID: ****0063\n\n\nc6174c80b81f4413a4b9f2065c5431c7\n\n\n\n10:19:46: 20/03/2024\n\n\n\nTIP:\n___________________\n\nTOTAL:\n___________________\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "55555"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "New York"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United States"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks CARD"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0119"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000031010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Contactless"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "None"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****0063"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Merchant Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Sale"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "c6174c80b81f4413a4b9f2065c5431c7"
          },
          "AMOUNT_AND_CURRENCY" : {
            "label" : "Amount",
            "value" : "$20.00"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "10:19:46"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : true,
        "totalLineRequired" : true
      }
    },
    "customerReceipt" : {
      "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n1234567\n\nSale\n$20.00\nPlease retain receipt!\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 002000\nMerchant ID: **37599\nTerminal ID: ****0063\n\n\nc6174c80b81f4413a4b9f2065c5431c7\n\n\n\n10:19:46: 20/03/2024\n\n\n\nTIP:\n___________________\n\nTOTAL:\n___________________\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "55555"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "New York"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United States"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks CARD"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0119"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000031010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Contactless"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "None"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****0063"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Cardholder Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Sale"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "c6174c80b81f4413a4b9f2065c5431c7"
          },
          "AMOUNT_AND_CURRENCY" : {
            "label" : "Amount",
            "value" : "$20.00"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "10:19:46"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : true,
        "totalLineRequired" : true
      }
    }
  }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Tip Adjust {#sis-cloud-sale-on-receipt-tip-adjust-intro}
========================================================

Use this information to process a tip adjust when the app is in Cloud mode. This follow-on transaction is required when processing an on-receipt tipping transaction. The tip adjust request must be sent within 24 hours to capture the transaction.  
After the original transaction is pre-authorized, the customer writes the tip or total amount on the printed receipt. A follow-on tip adjust request is then sent to capture the additional tip amount. This transaction is also referred to as an *overcapture* . For more information, see [Sale with On-Receipt Tipping](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-cloud-sale-on-receipt-tip-intro.md "").  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Required Fields for a Tip Adjust {#sis-cloud-sale-on-receipt-tip-adjust-api-reqfields}
======================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `TipAdjustRequest`.

request.transactionId
:
Set the value to the id field value from the original transaction.

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

REST Example: Tip Adjust {#sis-cloud-sale-on-receipt-tip-adjust-api-ex-rest}
============================================================================

Endpoints
---------

Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").  
**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions` Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type" : "TipAdjustRequest",
      "transactionId" : "c6174c80b81f4413a4b9f2065c5431c7",
      "amountDetails" : {
        "amount" : "4.00",
        "currency" : "USD"
      }
   }
}
```

Response to a Successful Request

```
{
  "type" : "TipAdjustResponse",
  "message" : "Payment approved",
  "transactionDetails" : {
    "id" : "c6174c80b81f4413a4b9f2065c5431c7",
    "merchantReferenceCode" : "1ce594be142142f4913cca805830a176",
    "submitTimeUtc" : "2024-03-20T09:19:41+0000",
    "captured" : true,
    "amountDetails" : {
      "currency" : "USD",
      "amount" : "24.00",
      "capturedAmount" : "24.00",
      "refundableAmount" : "24.00",
      "includedTipAmount" : "4.00"
    }
  },
  "processingDetails" : {
    "status" : "APPROVED",
    "verificationMethod" : "NONE",
    "entryMode" : "NFC_ICC",
    "card" : {
      "expirationMonth" : "12",
      "expirationYear" : "2025",
      "type" : "CARD",
      "maskedPan" : "476173XXXXXX0119",
      "countryCode" : "840"
    }
  },
  "additionalInformation" : {
    "instrumentId" : "7030000000022690119",
    "requestId" : "7109265975966653104007"
  },
  "linkedOperations" : [ ],
  "tipAdjustStatus" : "ADJUSTED",
  "receipts" : {
    "merchantReceipt" : {
      "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n1234567\n\nCapture\nPurchase Amount: $20.00\nTip Amount: $4.00\nTotal Amount: $24.00\nPlease retain receipt!\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 002000\nMerchant ID: **37599\nTerminal ID: ****7478\n\n\nc6174c80b81f4413a4b9f2065c5431c7\n\n10:23:17: 20/03/2024\n\n\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "55555"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "New York"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United States"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks CARD"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0119"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000031010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Contactless"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "None"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****7478"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Merchant Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Capture"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "c6174c80b81f4413a4b9f2065c5431c7"
          },
          "AMOUNT_AND_CURRENCY" : {
            "label" : "Amount",
            "value" : "$24.00"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "10:23:17"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : false,
        "totalLineRequired" : false
      }
    },
    "customerReceipt" : {
      "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n1234567\n\nCapture\nPurchase Amount: $20.00\nTip Amount: $4.00\nTotal Amount: $24.00\nPlease retain receipt!\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 002000\nMerchant ID: **37599\nTerminal ID: ****7478\n\n\nc6174c80b81f4413a4b9f2065c5431c7\n\n10:23:17: 20/03/2024\n\n\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "55555"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "New York"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United States"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks CARD"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0119"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000031010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Contactless"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "None"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****7478"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Cardholder Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Capture"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "c6174c80b81f4413a4b9f2065c5431c7"
          },
          "AMOUNT_AND_CURRENCY" : {
            "label" : "Amount",
            "value" : "$24.00"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "10:23:17"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : false,
        "totalLineRequired" : false
      }
    }
  }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Token Refund {#sis-pymnt-svcs-cloud-token-refund-api-intro}
===========================================================

Use this information to process a token refund in Cloud mode. A token refund transaction enables you to process a stand-alone credit against a tokenized card. In order to process a credit through a token, you must have the `Token Management Service` product enabled and an existing (saved) token from a tokenized transaction. For more information, see [Token Management Service](https://developer.example.com/docs/gateway/en-us/tms/developer/ctv/rest/tms/tms-overview.md "").  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for a Token Refund {#sis-pymnt-svcs-cloud-token-refund-api-reqfields}
=====================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `TokenRefundRequest`.

request.instrumentId
:
Set the value to the Instrument Identifier token.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

REST Example: Token Refund {#sis-pymnt-svcs-cloud-token-refund-api-ex-rest}
===========================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type": "TokenRefundRequest",
      "instrumentId": "7030000000022690119",
      "merchantReferenceCode": "30ed45dc7b3f4fb9905413940ac30363",
      "amountDetails": {
        "amount": "1.00",
        "currency": "GBP"
      }
   }
}
```

Response to a Successful Request

```
{
      "type" : "TokenRefundResponse",
      "message" : "Refund approved",
      "transactionDetails" : {
        "id" : "596b797178fe45e39ce3a8b8fdf432d6",
        "merchantReferenceCode" : "30ed45dc7b3f4fb9905413940ac30363",
        "submitTimeUtc" : "2023-12-01T21:02:50+0000",
        "amountDetails" : {
          "amount" : "1.00",
          "currency" : "GBP"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "MANUAL",
        "card" : {
          "expirationMonth" : "00",
          "expirationYear" : "00",
          "type" : "CARD",
          "maskedPan" : "703000XXXXXXXXX0119"
        }
      },
      "additionalInformation" : {
        "requestId" : "7014645711206245404009"
      },
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nRefund\n-£1.00\n\n\nPlease retain receipt!\n\n\nCard: CARD\nAccount: *** **** **** **** 0119\nEntry Mode: Keyed\n\nTransaction: -\nAuthorization: -\nMerchant ID: **37599\nTerminal ID: *************L_ID\n\n596b797178fe45e39ce3a8b8fdf432d6\n10:02:50 PM: 12/1/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "*** **** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "CLEARING_DETAILS_TRANSACTION_IDENTIFIER" : {
                "label" : "Transaction",
                "value" : "-"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "*************L_ID"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Refund"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "596b797178fe45e39ce3a8b8fdf432d6"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "12/1/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "10:02:50 PM"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nRefund\n-£1.00\n\n\nPlease retain receipt!\n\n\nCard: CARD\nAccount: *** **** **** **** 0119\nEntry Mode: Keyed\n\nTransaction: -\nAuthorization: -\nMerchant ID: **37599\nTerminal ID: *************L_ID\n\n596b797178fe45e39ce3a8b8fdf432d6\n10:02:50 PM: 12/1/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "*** **** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "CLEARING_DETAILS_TRANSACTION_IDENTIFIER" : {
                "label" : "Transaction",
                "value" : "-"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "*************L_ID"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Refund"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "596b797178fe45e39ce3a8b8fdf432d6"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "12/1/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "10:02:50 PM"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Pre-Authorization {#sis-pymnt-svcs-cloud-pre-auth-api-intro}
============================================================

Use this information to process a pre-authorization for an initial amount in Cloud mode. A pre-authorization transaction places a temporary hold on the customer's payment card. The transaction amount can be captured at a later time.  
Most authorizations expire in 5 to 7 days. The issuing bank sets the length of time before expiration. When an authorization expires with the issuing bank, your bank or processor might require you to re-submit an authorization request and include a request for capture in the same message.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for a Pre-Authorization {#sis-pymnt-svcs-cloud-pre-auth-api-reqfields}
======================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

request.capture
:
Set the value to `false`.

REST Example: Pre-Authorization {#sis-pymnt-svcs-cloud-pre-auth-api-ex-rest}
============================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "47bd9ed54f3f4bfabb9d3ee94cfa3008",
      "amountDetails" : {
        "amount" : "1.00",
        "currency" : "GBP"
      },
      "capture" : false
    }
}ß
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "e43069fbf85543659e478edd8d50f244",
        "merchantReferenceCode" : "47bd9ed54f3f4bfabb9d3ee94cfa3008",
        "submitTimeUtc" : "2023-12-01T20:38:14+0000",
        "captured" : false,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "0.00",
          "refundableAmount" : "1.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "CARD",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014630972006630604008"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nAuth only\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938242\nMerchant ID: **37599\nTerminal ID: ****0063\n\ne43069fbf85543659e478edd8d50f244\n21:38:18: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938242"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Auth only"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "e43069fbf85543659e478edd8d50f244"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:38:18"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nAuth only\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938242\nMerchant ID: **37599\nTerminal ID: ****0063\n\ne43069fbf85543659e478edd8d50f244\n21:38:18: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938242"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Auth only"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "e43069fbf85543659e478edd8d50f244"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:38:18"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Incremental Authorization {#sis-pymnt-svcs-cloud-increm-auth-api-intro}
=======================================================================

Use this information to process an incremental authorization in Cloud mode. This type of request can be made on a pre-authorization transaction to increase the authorized amount before it is captured.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for an Incremental Authorization {#sis-pymnt-svcs-cloud-increm-auth-api-reqfields}
==================================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `IncrementalAuthorizationRequest`.

request.transactionId
:
Set the value to the `id` field value from the original transaction.

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

REST Example: Incremental Authorization {#sis-pymnt-svcs-cloud-increm-auth-api-reqfields-ex-rest}
=================================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type": "IncrementalAuthorizationRequest",
      "transactionId": "e43069fbf85543659e478edd8d50f244",
      "amountDetails": {
        "amount": "2.00",
        "currency": "GBP"
      }
    }
}
```

Response to a Successful Request

```
{
      "type" : "IncrementalAuthorizationResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "6da4aff381e8483ebc65ebf4fbb27ec8",
        "merchantReferenceCode" : "47bd9ed54f3f4bfabb9d3ee94cfa3008",
        "submitTimeUtc" : "2023-12-01T20:39:43+0000",
        "captured" : false,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "2.00",
          "capturedAmount" : "0.00",
          "refundableAmount" : "0.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "MANUAL",
        "card" : {
          "expirationMonth" : "00",
          "expirationYear" : "00",
          "type" : "CARD",
          "maskedPan" : "476173XXXXXX0119"
        }
      },
      "additionalInformation" : {
        "requestId" : "7014631843806649604009"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nTop-up\n£2.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Keyed\nVerification: None\n\nAuthorization: 938243\nMerchant ID: **37599\nTerminal ID: ****0063\n\n6da4aff381e8483ebc65ebf4fbb27ec8\n21:39:45: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938243"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Top-up"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "6da4aff381e8483ebc65ebf4fbb27ec8"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£2.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:39:45"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nTop-up\n£2.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Keyed\nVerification: None\n\nAuthorization: 938243\nMerchant ID: **37599\nTerminal ID: ****0063\n\n6da4aff381e8483ebc65ebf4fbb27ec8\n21:39:45: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938243"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Top-up"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "6da4aff381e8483ebc65ebf4fbb27ec8"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£2.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:39:45"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Capture {#sis-pymnt-svcs-cloud-capture-api-intro}
=================================================

Use this information to capture a pre-authorized transaction in Cloud mode. The capture request references the approved pre-authorization request.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for a Capture {#sis-pymnt-svcs-cloud-capture-api-reqfields}
===========================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `CaptureRequest`.

request.transactionId
:
Set the value to the `id` field value from the original transaction.

Optional Fields for a Capture {#sis-pymnt-svcs-cloud-capture-api-optfields}
===========================================================================

Use the optional amount and currency fields to process a partial capture. Otherwise, the full amount will be captured.

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

REST Example: Capture {#sis-pymnt-svcs-cloud-capture-api-ex-rest}
=================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type": "CaptureRequest",
      "transactionId": "cb6475bafbb94d03b0f984629c63c294",
      "amountDetails": {
        "amount": "3.00",
        "currency": "GBP"
      }
   }
}
```

Response to a Successful Request

```
{
      "type" : "CaptureResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "cb6475bafbb94d03b0f984629c63c294",
        "merchantReferenceCode" : "dd02499055544be18ba7fa0397909d65",
        "submitTimeUtc" : "2023-12-01T20:43:03+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "3.00",
          "capturedAmount" : "3.00",
          "refundableAmount" : "3.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "CARD",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014633860196734504012"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£3.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938244\nMerchant ID: **37599\nTerminal ID: ****0063\n\ncb6475bafbb94d03b0f984629c63c294\n21:43:07: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938244"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "cb6475bafbb94d03b0f984629c63c294"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£3.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:43:07"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£3.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938244\nMerchant ID: **37599\nTerminal ID: ****0063\n\ncb6475bafbb94d03b0f984629c63c294\n21:43:07: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938244"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "cb6475bafbb94d03b0f984629c63c294"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£3.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:43:07"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Mail Order or Telephone Order {#sis-pax-pymnt-svcs-cloud-moto-trxns-intro}
==========================================================================

Use this information to process a mail order or telephone order (MOTO) sale and other transactions in Cloud mode. The payment card is not presented physically at the terminal for a MOTO transaction because it is a card-not-present transaction.  
You can also process these MOTO transactions in Cloud mode:

Account Verification
:
A MOTO account verification request submits a zero-amount authorization request to validate the payment card.

Pre-authorization
:
A MOTO pre-authorization request places a temporary hold on the customer's payment card, enabling the transaction to be captured at a later time. Most authorizations expire within 5 to 7 days. However, the exact duration is determined by the issuing bank.

    When an authorization expires, your bank, the payment processor, or issuing bank might require you to re-submit the authorization request. In such cases, you might be required to include the capture instructions in the same message to ensure successful processing.

{#sis-pax-pymnt-svcs-cloud-moto-trxns-intro_dl_y4k_5p1_bhc}  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for Mail Order or Telephone Order {#sis-pax-pymnt-svcs-cloud-moto-trxns-reqfields}
==================================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest` for a sale or to `AccountVerificationRequest` for an account verification.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

request.paymentMode
:
Set the value to `MOTO`.

Optional Fields for Mail Order or Telephone Order {#sis-pax-pymnt-svcs-cloud-moto-trxns-optfields}
==================================================================================================

capture
:
Set the value to `false` for a pre-authorization.

REST Example: Mail Order or Telephone Order Sale {#sis-pax-pymnt-svcs-cloud-moto-trxns-ex-rest}
===============================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "a7fbcdc92425456fa0db29c8670a3150",
      "amountDetails" : {
        "amount" : "1.00",
        "currency" : "GBP"
      },
      "paymentMode": "MOTO"
   }
}
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "4348c35f258c4f8d8c89b9898e3f1b63",
        "merchantReferenceCode" : "a7fbcdc92425456fa0db29c8670a3150",
        "submitTimeUtc" : "2023-12-01T20:51:09+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "1.00",
          "refundableAmount" : "1.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "MANUAL",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "CARD",
          "maskedPan" : "411111******1111"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7038380000019631111",
        "requestId" : "7014638853776978504011"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nCVV MATCH ONLY\n\n\nCard: CARD\nAccount: **** **** **** 1111\nEntry Mode: Keyed\nVerification: Cardholder Not Present\n\nAuthorization: 938246\nMerchant ID: **37599\nTerminal ID: ****0063\n\n4348c35f258c4f8d8c89b9898e3f1b63\n21:51:27: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 1111"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "Cardholder Not Present"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938246"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "4348c35f258c4f8d8c89b9898e3f1b63"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:51:27"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "CVV MATCH ONLY"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: CARD\nAccount: **** **** **** 1111\nEntry Mode: Keyed\nVerification: Cardholder Not Present\n\nAuthorization: 938246\nMerchant ID: **37599\nTerminal ID: ****0063\n\n4348c35f258c4f8d8c89b9898e3f1b63\n21:51:27: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 1111"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "Cardholder Not Present"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938246"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "4348c35f258c4f8d8c89b9898e3f1b63"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:51:27"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Account Verification {#sis-pymnt-svcs-cloud-acct-verif-api-intro}
=================================================================

Use this information to process an account verification in Cloud mode. The account verification transaction submits a zero-amount authorization request to validate the payment card.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for an Account Verification {#sis-pymnt-svcs-cloud-acct-verif-api-reqfields}
============================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `AccountVerificationRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.currency
:
Set the value to the currency code.

REST Example: Account Verification {#sis-pymnt-svcs-cloud-acct-verif-api-ex-rest}
=================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type": "AccountVerificationRequest",
      "merchantReferenceCode": "ec119c3b377542b09132867d236dc834",
      "amountDetails": {
        "currency": "GBP"
      }
   }
}
```

Response to a Successful Request

```
 {
      "type" : "AccountVerificationResponse",
      "message" : "Verification successful",
      "transactionDetails" : {
        "id" : "2dd6beb00d8d4bb8bf1a4718917a3003",
        "merchantReferenceCode" : "ec119c3b377542b09132867d236dc834",
        "submitTimeUtc" : "2023-12-01T20:27:02+0000",
        "amountDetails" : {
          "currency" : "GBP"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "CARD",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014624258386432804007"
      },
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nAccount Verification\n£0.00\n\n\nAccount Valid.\n\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938239\nMerchant ID: **37599\nTerminal ID: ****0063\n\n2dd6beb00d8d4bb8bf1a4718917a3003\n21:27:07: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938239"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Account Verification"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "2dd6beb00d8d4bb8bf1a4718917a3003"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£0.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:27:07"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Account Valid."
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nAccount Verification\n£0.00\n\n\nAccount Valid.\n\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938239\nMerchant ID: **37599\nTerminal ID: ****0063\n\n2dd6beb00d8d4bb8bf1a4718917a3003\n21:27:07: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks CARD"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938239"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Account Verification"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "2dd6beb00d8d4bb8bf1a4718917a3003"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£0.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:27:07"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Account Valid."
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Cashback {#sis-pymnt-svcs-cloud-cashback-api-intro}
===================================================

Use this information to process a cashback transaction in Cloud mode. This type of transaction enables a customer to request that a specified amount of cash be given to them as part of the transaction. A cashback transaction can be processed with or without a purchase.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for a Cashback {#sis-pymnt-svcs-cloud-cashback-api-reqfields}
=============================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

request.amountDetails.cashbackAmount
:
Set the value to the cashback amount.

REST Example: Cashback {#sis-pymnt-svcs-cloud-cashback-api-ex-rest}
===================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "PaymentRequest",
        "merchantReferenceCode": "bd74d30930e349548fd9d125f88291bc",
        "amountDetails": {
            "amount": "20.00",
            "currency": "GBP",
            "cashbackAmount": "5.00"
        }
    }
}
```

Response to a Successful Request

```
{
  "type" : "PaymentResponse",
  "message" : "Payment approved",
  "transactionDetails" : {
    "id" : "218b28d38bf3424ab4ade95b9be1c75b",
    "merchantReferenceCode" : "bd74d30930e349548fd9d125f88291bc",
    "submitTimeUtc" : "2024-03-20T08:55:37+0000",
    "captured" : true,
    "amountDetails" : {
      "currency" : "GBP",
      "amount" : "20.00",
      "capturedAmount" : "25.00",
      "refundableAmount" : "20.00",
      "cashbackAmount" : "5.00"
    }
  },
  "processingDetails" : {
    "status" : "APPROVED",
    "verificationMethod" : "PIN",
    "entryMode" : "ICC",
    "card" : {
      "expirationMonth" : "12",
      "expirationYear" : "2025",
      "type" : "MASTERCARD",
      "maskedPan" : "541333XXXXXX0011",
      "countryCode" : "276"
    }
  },
  "additionalInformation" : {
    "instrumentId" : "7030000000232230011",
    "requestId" : "7109249459396751504008"
  },
  "linkedOperations" : [ ],
  "tipAdjustStatus" : "NOT_ADJUSTABLE",
  "receipts" : {
    "merchantReceipt" : {
      "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nCashback\n£25.00\nPurchase Amount: £20.00\nCashback: £5.00\nPlease retain receipt!\n\nCard: Payworks MASTER\nAccount: **** **** **** 0011\nEntry Mode: Chip\nAID: A0000000041010\nCard Number: 0\nVerification: PIN\n\nAuthorization: 002500\nMerchant ID: **37599\nTerminal ID: ****0063\n\n\n218b28d38bf3424ab4ade95b9be1c75b\n\n09:55:46: 20/03/2024\n\n\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "UB3 2EA"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "London"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United Kingdom"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks MASTER"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0011"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000041010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Chip"
          },
          "PAYMENT_DETAILS_ACCOUNT_SEQUENCE_NUMBER" : {
            "label" : "Card Number",
            "value" : "0"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "PIN"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002500"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****0063"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Merchant Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Cashback"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "218b28d38bf3424ab4ade95b9be1c75b"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "09:55:46"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : false,
        "totalLineRequired" : false
      }
    },
    "customerReceipt" : {
      "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nCashback\n£25.00\nPurchase Amount: £20.00\nCashback: £5.00\nPlease retain receipt!\n\nCard: Payworks MASTER\nAccount: **** **** **** 0011\nEntry Mode: Chip\nAID: A0000000041010\nCard Number: 0\nVerification: PIN\n\nAuthorization: 002500\nMerchant ID: **37599\nTerminal ID: ****0063\n\n\n218b28d38bf3424ab4ade95b9be1c75b\n\n09:55:46: 20/03/2024\n\n\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "UB3 2EA"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "London"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United Kingdom"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks MASTER"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0011"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000041010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Chip"
          },
          "PAYMENT_DETAILS_ACCOUNT_SEQUENCE_NUMBER" : {
            "label" : "Card Number",
            "value" : "0"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "PIN"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002500"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****0063"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Cardholder Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Cashback"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "218b28d38bf3424ab4ade95b9be1c75b"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "09:55:46"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : false,
        "totalLineRequired" : false
      }
    }
  }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Sale with Installment Details {#sis-pymnt-svcs-cloud-sale-installment-details-intro}
====================================================================================

Use this information to process a sale transaction with installment details when the app is in Cloud mode. This type of transaction can be used to include the required installment details as part of the sale transaction.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").  
This transaction is available only in the Latin America and Caribbean (LAC) region.

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for a Sale with Installment Details {#sis-pymnt-svcs-cloud-sale-installment-details-reqfields}
==============================================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

Optional Fields for a Sale with Installment Details {#sis-pymnt-svcs-cloud-sale-installment-details-optfields}
==============================================================================================================

Use one or more of the optional installmentDetails fields to provide additional installment details.

request.installmentDetails.numberOfInstallments
:
Set the value to the number of installments.

request.installmentDetails.planType
:
Set the value to `MERCHANT_FUNDED` or `ISSUER_FUNDED`.

request.installmentDetails.interestPlan
:
Set the value to `true` or `false`.

request.installmentDetails.governmentPlan
:
Set the value to `true` or `false`.

REST Example: Sale with Installment Details {#sis-pymnt-svcs-cloud-sale-installment-details-ex-rest}
====================================================================================================

Request

```
{
  "serialNumber": "1850000000",
  "request": {
    "type": "PaymentRequest",
    "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
    "amountDetails": {
      "amount": "20.00",
      "currency": "USD"
    },
    "installmentDetails": {
      "numberOfInstallments": 5,
      "planType": "MERCHANT_FUNDED",
      "interestPlan": true,
      "governmentPlan": true
    }
  }
}
```

Response to a Successful Request

```
{
    "type": "PaymentResponse",
    "message": "Payment approved",
    "transactionDetails": {
        "id": "8ccb150a88bd4c6f9a00a687f39ca97d",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc": "2024-09-20T08:15:12+0000",
        "captured": true,
        "amountDetails": {
            "amount": "20.00",
            "currency": "USD",
            "capturedAmount": "20.00",
            "refundableAmount": "20.00"
        }
    },
    "processingDetails": {
        "status": "APPROVED",
        "verificationMethod": "NONE",
        "entryMode": "NFC_ICC",
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2025",
            "type" : "CARD",
            "maskedPan": "476173XXXXXX0119",
            "countryCode": "840"
        }
    },
    "additionalInformation": {
        "requestId": "7268201146336069504011"
    },
    "linkedOperations": [],
    "receipts": {
        "merchantReceipt": {
            "preformattedReceipt": "Merchant Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$20.00\n\nPlease retain receipt!\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 546712\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n8ccb150a88bd4c6f9a00a687f39ca97d\n\n4:15:12 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks CARD"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "546712"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Merchant Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "8ccb150a88bd4c6f9a00a687f39ca97d"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$20.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "4:15:12 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        },
        "customerReceipt": {
            "preformattedReceipt": "Cardholder Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$20.00\n\nPlease retain receipt!\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 546712\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n8ccb150a88bd4c6f9a00a687f39ca97d\n\n4:15:12 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks CARD"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "546712"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Cardholder Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "8ccb150a88bd4c6f9a00a687f39ca97d"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$20.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "4:15:12 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        }
    },
    "installmentDetails": {
        "numberOfInstallments": 5,
        "planType": "MERCHANT_FUNDED",
        "interestPlan": true,
        "governmentPlan": true
    }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Sale with Payment Facilitator Details {#sis-pymnt-svcs-cloud-sale-pymnt-facil-details-intro}
============================================================================================

Use this information to process a sale transaction with payment facilitator details when the app is in Cloud mode. This type of transaction can be used to include the required payment facilitator details as part of the sale transaction.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for a Sale with Payment Facilitator Details {#sis-pymnt-svcs-cloud-sale-pymnt-facil-details-reqfields}
======================================================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

Optional Fields for a Sale with Payment Facilitator Details {#sis-pymnt-svcs-cloud-sale-pymnt-facil-details-optfields}
======================================================================================================================

Use one or more of the optional merchantDetails fields to provide the required payment facilitator details.

request.merchantDetails.salesOrganizationId
:
Set the value to the sales organization identifier.

request.merchantDetails.subMerchantId
:
Set the value to the sub-merchant identifier.

request.merchantDetails.descriptorName
:
Set the value to the descriptor name.

REST Example: Sale with Payment Facilitator Details {#sis-pymnt-svcs-cloud-sale-pymnt-facil-details-ex-rest}
============================================================================================================

Request

```
{
  "serialNumber": "1850000000",
  "request": {
    "type": "PaymentRequest",
    "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
    "amountDetails": {
      "amount": "1.00",
      "currency": "USD"
    },
    "merchantDetails": {
      "salesOrganizationId": "12345",
      "subMerchantId": "SM67890",
      "descriptorName": "ExampleMerchant"
    }
  }
}
```

Response to a Successful Request

```
{
    "type": "PaymentResponse",
    "message": "Payment approved",
    "transactionDetails": {
        "id": "940d49ee94444764acb1c898e2254954",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc": "2024-09-20T07:53:36+0000",
        "captured": true,
        "amountDetails": {
            "amount": "1.00",
            "currency": "USD",
            "capturedAmount": "1.00",
            "refundableAmount": "1.00"
        }
    },
    "processingDetails": {
        "status": "APPROVED",
        "verificationMethod": "NONE",
        "entryMode": "NFC_ICC",
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2025",
            "type" : "CARD",
            "maskedPan": "476173XXXXXX0119",
            "countryCode": "840"
        }
    },
    "additionalInformation": {
        "requestId": "7268188188226629104009"
    },
    "linkedOperations": [],
    "receipts": {
        "merchantReceipt": {
            "preformattedReceipt": "Merchant Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$1.00\n\nPlease retain receipt!\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 545814\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n940d49ee94444764acb1c898e2254954\n\n3:53:36 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks CARD"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "545814"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Merchant Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "940d49ee94444764acb1c898e2254954"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$1.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "3:53:36 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        },
        "customerReceipt": {
            "preformattedReceipt": "Cardholder Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$1.00\n\nPlease retain receipt!\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 545814\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n940d49ee94444764acb1c898e2254954\n\n3:53:36 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks CARD"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "545814"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Cardholder Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "940d49ee94444764acb1c898e2254954"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$1.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "3:53:36 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        }
    },
    "merchantDetails": {
        "salesOrganizationId": "12345",
        "subMerchantId": "SM67890",
        "descriptorName": "ExampleMerchant"
    }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Sale with Tax Details {#sis-pymnt-svcs-cloud-sale-tax-details-intro}
====================================================================

Use this information to process a sale transaction with tax details when the app is in Cloud mode. This type of transaction can be used to include the required tax details as part of the sale transaction.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for a Sale with Tax Details {#sis-pymnt-svcs-cloud-sale-tax-details-reqfields}
==============================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

Optional Fields for a Sale with Tax Details {#sis-pymnt-svcs-cloud-sale-tax-details-optfields}
==============================================================================================

Use one or more of the optional taxDetails fields to provide the required tax details.

request.taxDetails.taxId
:
Set the value to the merchant tax identifier.

request.taxDetails.salesSlipNumber
:
Set the value to the sales slip number.

request.taxDetails.includedTaxAmount
:
Set the value to the tax amount.

request.taxDetails.includedLocalTaxAmount
:
Set the value to the local tax amount.

request.taxDetails.includedNationalTaxAmount
:
Set the value to the national tax amount.

REST Example: Sale with Tax Details {#sis-pymnt-svcs-cloud-sale-tax-details-ex-rest}
====================================================================================

Request

```
{
  "serialNumber": "1850000000",
  "request": {
    "type": "PaymentRequest",
    "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
    "amountDetails": {
      "amount": "20.00",
      "currency": "USD"
    },
    "taxDetails": {
      "taxId": "TaxID1234",
      "salesSlipNumber": 12345678,
      "includedTaxAmount": "5.00",
      "includedLocalTaxAmount": "1.00",
      "includedNationalTaxAmount": "2.00"
    }
  }
}
```

Response to a Successful Request

```
{
    "type": "PaymentResponse",
    "message": "Payment approved",
    "transactionDetails": {
        "id": "4bebd72cf0ff4a9ea212baca0c6d9faf",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc": "2024-09-20T07:15:25+0000",
        "captured": true,
        "amountDetails": {
            "amount": "20.00",
            "currency": "USD",
            "capturedAmount": "20.00",
            "refundableAmount": "20.00"
        }
    },
    "processingDetails": {
        "status": "APPROVED",
        "verificationMethod": "NONE",
        "entryMode": "NFC_ICC",
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2025",
            "type" : "CARD",
            "maskedPan": "476173XXXXXX0119",
            "countryCode": "840"
        }
    },
    "additionalInformation": {
        "requestId": "7268165283576248404007"
    },
    "linkedOperations": [],
    "receipts": {
        "merchantReceipt": {
            "preformattedReceipt": "Merchant Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$20.00\n\nPlease retain receipt!\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 129702\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n4bebd72cf0ff4a9ea212baca0c6d9faf\n\n3:15:25 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks CARD"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "129702"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Merchant Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "4bebd72cf0ff4a9ea212baca0c6d9faf"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$20.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "3:15:25 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        },
        "customerReceipt": {
            "preformattedReceipt": "Cardholder Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$20.00\n\nPlease retain receipt!\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 129702\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n4bebd72cf0ff4a9ea212baca0c6d9faf\n\n3:15:25 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks CARD"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "129702"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Cardholder Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "4bebd72cf0ff4a9ea212baca0c6d9faf"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$20.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "3:15:25 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        }
    },
    "taxDetails": {
        "taxId": "TaxID1234",
        "salesSlipNumber": 12345678,
        "includedTaxAmount": "5.00",
        "includedLocalTaxAmount": "1.00",
        "includedNationalTaxAmount": "2.00"
    }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Sale with Lodging Details {#sis-pymnt-svcs-cloud-sale-lodging-intro}
====================================================================

Use this information to process a sale transaction with lodging details in Cloud mode. This transaction includes required lodging details as part of the sale transaction.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for a Sale with Lodging Details {#sis-pymnt-svcs-cloud-sale-lodging-reqfields}
==============================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

Optional Fields for a Sale with Lodging Details {#sis-pymnt-svcs-cloud-sale-lodging-optfields}
==============================================================================================

Use one or more of the optional fields to include additional details in the transaction.

request.lodgingDetails.duration
:
Set this field to the number of nights of the lodging stay.

request.lodgingDetails.checkInDate
:
Set this field to the check-in date in MMDDYY format.

request.lodgingDetails.checkOutDate
:
Set this field to the check-out date in MMDDYY format.

request.lodgingDetails.guestSmokingPreference
:
Set this field to Y or N to indicate the guest's smoking preference.

request.lodgingDetails.numberOfGuests
:
Set this field to the number of guests.

request.lodgingDetails.numberOfRoomsBooked
:
Set this field to the number of rooms booked.

request.lodgingDetails.guestName
:
Set this field to the name of the guest.

request.lodgingDetails.roomLocation
:
Set this field to the room location description.

request.lodgingDetails.roomTaxElements
:
Set this field to the applicable room tax elements.

request.lodgingDetails.roomBedType
:
Set this field to the type of bed in the room.

request.lodgingDetails.roomRateType
:
Set this field to the room rate type.

request.lodgingDetails.specialProgramCode
:
Set this field to the special program code.

request.lodgingDetails.dailyRoomRate1
:
Set this field to the daily room rate for the first rate tier.

request.lodgingDetails.dailyRoomRate2
:
Set this field to the daily room rate for the second rate tier.

request.lodgingDetails.dailyRoomRate3
:
Set this field to the daily room rate for the third rate tier.

request.lodgingDetails.roomNights1
:
Set this field to the number of nights at the first rate tier.

request.lodgingDetails.roomNights2
:
Set this field to the number of nights at the second rate tier.

request.lodgingDetails.roomNights3
:
Set this field to the number of nights at the third rate tier.

request.lodgingDetails.corporateClientCode
:
Set this field to the corporate client code.

request.lodgingDetails.promotionalCode
:
Set this field to the promotional code.

request.lodgingDetails.additionalCoupon
:
Set this field to an additional coupon code.

request.lodgingDetails.travelAgencyCode
:
Set this field to the travel agency code.

request.lodgingDetails.travelAgencyName
:
Set this field to the name of the travel agency.

request.lodgingDetails.customerServicePhoneNumber
:
Set this field to the customer service phone number.

request.lodgingDetails.tax
:
Set this field to the total tax amount.

request.lodgingDetails.prepaidCost
:
Set this field to the prepaid cost amount.

request.lodgingDetails.foodAndBeverageCost
:
Set this field to the food and beverage cost.

request.lodgingDetails.roomTax
:
Set this field to the room tax amount.

request.lodgingDetails.adjustmentAmount
:
Set this field to the adjustment amount.

request.lodgingDetails.phoneCost
:
Set this field to the phone cost.

request.lodgingDetails.restaurantCost
:
Set this field to the restaurant cost.

request.lodgingDetails.roomServiceCost
:
Set this field to the room service cost.

request.lodgingDetails.miniBarCost
:
Set this field to the mini bar cost.

request.lodgingDetails.laundryCost
:
Set this field to the laundry cost.

request.lodgingDetails.miscellaneousCost
:
Set this field to the miscellaneous cost.

request.lodgingDetails.giftShopCost
:
Set this field to the gift shop cost.

request.lodgingDetails.movieCost
:
Set this field to the movie cost.

request.lodgingDetails.healthClubCost
:
Set this field to the health club cost.

request.lodgingDetails.valetParkingCost
:
Set this field to the valet parking cost.

request.lodgingDetails.cashDisbursementCost
:
Set this field to the cash disbursement cost.

request.lodgingDetails.nonRoomCost
:
Set this field to the non-room cost.

request.lodgingDetails.businessCenterCost
:
Set this field to the business center cost.

request.lodgingDetails.loungeBarCost
:
Set this field to the lounge or bar cost.

request.lodgingDetails.transportationCost
:
Set this field to the transportation cost.

request.lodgingDetails.gratuityCost
:
Set this field to the gratuity cost.

request.lodgingDetails.conferenceRoomCost
:
Set this field to the conference room cost.

request.lodgingDetails.audioVisualCost
:
Set this field to the audio/visual equipment cost.

request.lodgingDetails.banquetCost
:
Set this field to the banquet cost.

request.lodgingDetails.internetAccessCost
:
Set this field to the internet access cost.

request.lodgingDetails.earlyCheckOutCost
:
Set this field to the early check-out cost.

request.lodgingDetails.nonRoomTax
:
Set this field to the non-room tax amount.

REST Example: Sale with Lodging Details {#sis-pymnt-svcs-cloud-sale-lodging-ex-rest}
====================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "PaymentRequest",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "amountDetails": {
            "amount": "500.00",
            "currency": "USD"
        },
        "lodgingDetails": {
            "duration": 3,
            "checkInDate": "030125",
            "checkOutDate": "030425",
            "guestSmokingPreference": "N",
            "numberOfGuests": 2,
            "numberOfRoomsBooked": 1,
            "guestName": "John Doe",
            "roomLocation": "Ocean View",
            "roomTaxElements": "VAT",
            "roomBedType": "KING",
            "roomRateType": "CORPORATE",
            "specialProgramCode": "1",
            "dailyRoomRate1": "150.00",
            "dailyRoomRate2": "160.00",
            "dailyRoomRate3": "170.00",
            "roomNights1": 1,
            "roomNights2": 1,
            "roomNights3": 1,
            "corporateClientCode": "CORP123456",
            "promotionalCode": "PROMO2025",
            "additionalCoupon": "DISCOUNT10",
            "travelAgencyCode": "TA789",
            "travelAgencyName": "Premium Travel Agency",
            "customerServicePhoneNumber": "1-800-555-0199",
            "tax": "45.00",
            "prepaidCost": "200.00",
            "foodAndBeverageCost": "125.00",
            "roomTax": "30.00",
            "adjustmentAmount": "15.00",
            "phoneCost": "8.00",
            "restaurantCost": "95.00",
            "roomServiceCost": "40.00",
            "miniBarCost": "25.00",
            "laundryCost": "18.00",
            "miscellaneousCost": "12.00",
            "giftShopCost": "35.00",
            "movieCost": "10.00",
            "healthClubCost": "20.00",
            "valetParkingCost": "30.00",
            "cashDisbursementCost": "5.00",
            "nonRoomCost": "40.00",
            "businessCenterCost": "15.00",
            "loungeBarCost": "55.00",
            "transportationCost": "75.00",
            "gratuityCost": "45.00",
            "conferenceRoomCost": "120.00",
            "audioVisualCost": "65.00",
            "banquetCost": "180.00",
            "internetAccessCost": "12.00",
            "earlyCheckOutCost": "20.00",
            "nonRoomTax": "25.00"
        }
    }
}
```

Response to a Successful Request

```
{
    "type": "PaymentResponse",
    "message": "Payment approved",
    "transactionDetails": {
        "id": "8ccb150a88bd4c6f9a00a687f39ca97d",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc": "2024-09-20T08:15:12+0000",
        "captured": true,
        "amountDetails": {
            "amount": "500.00",
            "currency": "USD",
            "capturedAmount": "500.00",
            "refundableAmount": "500.00"
        }
    },
    "processingDetails": {
        "status": "APPROVED",
        "verificationMethod": "NONE",
        "entryMode": "NFC_ICC",
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2025",
            "type" : "CARD",
            "maskedPan": "476173XXXXXX0119",
            "countryCode": "840"
        }
    },
    "additionalInformation": {
        "requestId": "7268201146336069504011"
    },
    "linkedOperations": [],
    "receipts": {
        "merchantReceipt": {
            "preformattedReceipt": "Merchant Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$500.00\n\nPlease retain receipt!\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 546712\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n8ccb150a88bd4c6f9a00a687f39ca97d\n\n4:15:12 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks CARD"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "546712"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Merchant Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "8ccb150a88bd4c6f9a00a687f39ca97d"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$500.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "4:15:12 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        },
        "customerReceipt": {
            "preformattedReceipt": "Cardholder Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$500.00\n\nPlease retain receipt!\n\nCard: Payworks CARD\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 546712\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n8ccb150a88bd4c6f9a00a687f39ca97d\n\n4:15:12 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks CARD"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "546712"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Cardholder Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "8ccb150a88bd4c6f9a00a687f39ca97d"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$500.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "4:15:12 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        }
    },
    "lodgingDetails": {
        "duration": 3,
        "checkInDate": "030125",
        "checkOutDate": "030425",
        "guestSmokingPreference": "N",
        "numberOfGuests": 2,
        "numberOfRoomsBooked": 1,
        "guestName": "John Doe",
        "roomLocation": "Ocean View",
        "roomTaxElements": "VAT",
        "roomBedType": "KING",
        "roomRateType": "CORPORATE",
        "specialProgramCode": "1",
        "dailyRoomRate1": "150.00",
        "dailyRoomRate2": "160.00",
        "dailyRoomRate3": "170.00",
        "roomNights1": 1,
        "roomNights2": 1,
        "roomNights3": 1,
        "corporateClientCode": "CORP123456",
        "promotionalCode": "PROMO2025",
        "additionalCoupon": "DISCOUNT10",
        "travelAgencyCode": "TA789",
        "travelAgencyName": "Premium Travel Agency",
        "customerServicePhoneNumber": "1-800-555-0199",
        "tax": "45.00",
        "prepaidCost": "200.00",
        "foodAndBeverageCost": "125.00",
        "roomTax": "30.00",
        "adjustmentAmount": "15.00",
        "phoneCost": "8.00",
        "restaurantCost": "95.00",
        "roomServiceCost": "40.00",
        "miniBarCost": "25.00",
        "laundryCost": "18.00",
        "miscellaneousCost": "12.00",
        "giftShopCost": "35.00",
        "movieCost": "10.00",
        "healthClubCost": "20.00",
        "valetParkingCost": "30.00",
        "cashDisbursementCost": "5.00",
        "nonRoomCost": "40.00",
        "businessCenterCost": "15.00",
        "loungeBarCost": "55.00",
        "transportationCost": "75.00",
        "gratuityCost": "45.00",
        "conferenceRoomCost": "120.00",
        "audioVisualCost": "65.00",
        "banquetCost": "180.00",
        "internetAccessCost": "12.00",
        "earlyCheckOutCost": "20.00",
        "nonRoomTax": "25.00"
    }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Receiving Transaction Responses Asynchronously {#sis-pymnt-svcs-cloud-txn-resp-async-api-intro}
===============================================================================================

Use this information to receive transaction responses asynchronously when the app is in Cloud mode. There is a follow-on service for this type of request. For more information, see [Check Transaction Events](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-txn-resp-async-api-intro/sis-pymnt-svcs-cloud-check-txn-events-intro.md "").  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions/async`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions/async`

Receive Transaction Responses Asynchronously {#sis-pymnt-svcs-cloud-txn-resp-async-api-task}
============================================================================================

Asynchronous endpoints can be used to receive transaction responses for most types of transaction requests when the app is in Cloud mode.  
Follow these steps to receive transaction responses asynchronously:

1. Use the asynchronous endpoints shown in the example to process a transaction and receive an interaction identifier. The example shows how to process a sale asynchronously.
2. After the transaction is completed, use the interaction identifier returned in the response to check the transaction events and to get a transaction identifier.
3. Use the transaction identifier to process a Check Transaction Status request. The response will contain full transaction and receipt details. For more information, see [Requesting a Check Transaction Status](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-txn-status-api-intro.md "").

REST Example: Receive Transaction Responses Asynchronously {#sis-pymnt-svcs-cloud-txn-resp-async-sale-api-ex-rest}
==================================================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "PaymentRequest",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "amountDetails": {
            "amount": "1.00",
            "currency": "GBP"
        }
    }
}
```

Response to a Successful Request

```
{
    "interactionId": "0c292d7f-6bf9-460c-afc3-d75c189f2f99"
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Check Transaction Events {#sis-pymnt-svcs-cloud-check-txn-events-intro}
=======================================================================

Use this information to process a Check Transaction Events request when the app is in Cloud mode. This type of request is a follow-on service for receiving transaction responses asynchronously. For more information, see [Receiving Transaction Responses Asynchronously](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-txn-resp-async-api-intro.md "").  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

The GET request must include the interaction identifier (`interactionId`).  
**Test:** `GET https://terminalstest.example.com/v1/cloud/interactions/{interactionId}/events`  
**Production:** `GET https://terminals.example.com/v1/cloud/interactions/{interactionId}/events`

Required Fields to Check Transaction Events {#sis-pymnt-svcs-cloud-check-txn-events-reqfields}
==============================================================================================

The body of the API request is empty. The GET request must include the information required to return the response. If you want to receive only the latest transaction event, set a query parameter of `limit=1`.

REST Example: Check Transaction Events {#sis-pymnt-svcs-cloud-check-txn-events-api-ex-rest}
===========================================================================================

Request  
The body of the request is empty. The GET request includes the information required to return the response.

```
{
}
```

Response to a Successful Request

```
{
    "interactionId": "0c292d7f-6bf9-460c-afc3-d75c189f2f99",
    "transactionEvents": [
        {
            "type": "PaymentResponse",
            "message": "Payment approved",
            "transactionId": "c9f966ef0e0e4a9186c0cfb75c90841a",
            "createdAt": "2024-05-28 13:11:30:939"
        },
        {
            "type": "TransactionStatusResponse",
            "message": "Payment approved",
            "createdAt": "2024-05-28 13:11:30:556"
        },
        {
            "type": "TransactionStatusResponse",
            "message": "Processing payment...",
            "createdAt": "2024-05-28 13:11:28:928"
        },
        {
            "type": "TransactionStatusResponse",
            "message": "1.00 GBP - Present card",
            "createdAt": "2024-05-28 13:11:28:093"
        },
        {
            "type": "TransactionStatusResponse",
            "message": "1.00 GBP - Present card",
            "createdAt": "2024-05-28 13:11:27:439"
        },
        {
            "type": "TransactionStatusResponse",
            "message": "1.00 GBP - Present card",
            "createdAt": "2024-05-28 13:11:27:217"
        },
        {
            "type": "TransactionStatusResponse",
            "message": "Registering transaction",
            "createdAt": "2024-05-28 13:11:27:022"
        },
        {
            "type": "TransactionStatusResponse",
            "message": "Registering transaction",
            "createdAt": "2024-05-28 13:11:26:485"
        },
        {
            "type": "TransactionStatusResponse",
            "message": "Connecting to card reader",
            "createdAt": "2024-05-28 13:11:24:649"
        },
        {
            "type": "AcknowledgementResponse",
            "createdAt": "2024-05-28 13:11:23:823"
        }
    ]
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Electronic Benefits Transfer {#sis-pymnt-svcs-cloud-ebt-intro}
==============================================================

Public assistance programs in the United States use Electronic Benefits Transfer (EBT) payment cards to issue monthly food and cash benefits to eligible people. EBT cards function like prepaid debit cards that can be used at authorized retailers. Food benefits are issued through the Supplemental Nutrition Assistance Program (SNAP), which helps people with low incomes purchase eligible food items.  
Use this information to process EBT SNAP (food benefits) and EBT Cash transactions when the app is in Cloud mode.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for Electronic Benefits Transfer {#sis-pymnt-svcs-cloud-ebt-reqfields}
======================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest` for a sale or to `StandaloneRefundRequest` for a stand-alone credit.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

request.paymentMode
:
Set the value to `EBT`.

request.ebtDetails.category
:
Set the value to `FOOD` for EBT SNAP and `CASH` for EBT Cash.

Optional Fields for Electronic Benefits Transfer {#sis-pymnt-svcs-cloud-ebt-optfields}
======================================================================================

request.ebtDetails.isBalanceInquiry
:
Set the value to `true` for a balance inquiry. The transaction amount must be set to `0`.

request.ebtDetails.isVoucher
:
Set the value to `true` for a voucher transaction.

request.amountDetails.cashbackAmount
:
Set the value to the cashback amount for a cashback transaction.

REST Example: Electronic Benefits Transfer SNAP Sale {#sis-pymnt-svcs-cloud-ebt-ex-rest}
========================================================================================

Request

```
{
   "serialNumber": "1850000000",
   "request": 
       {
       "type" : "PaymentRequest",
       "merchantReferenceCode" : "82910b8b430a414dbe224e4494545b02",
       "paymentMode" : "EBT",
       "amountDetails" : {
         "amount" : "1.00",
         "currency" : "USD"
       },
       "ebtDetails" : {
         "category" : "FOOD"
       }
    }
}
```

Response to a Successful Request

```
{
  "type" : "PaymentResponse",
  "message" : "Payment approved",
  "transactionDetails" : {
    "id" : "bd9c4ddd5bb84aafa42f16f2660f76c7",
    "merchantReferenceCode" : "82910b8b430a414dbe224e4494545b02",
    "submitTimeUtc" : "2025-09-29T09:04:02+0000",
    "captured" : true,
    "amountDetails" : {
      "currency" : "USD",
      "amount" : "1.00",
      "capturedAmount" : "1.00",
      "refundableAmount" : "1.00"
    }
  },
  "processingDetails" : {
    "status" : "APPROVED",
    "verificationMethod" : "PIN",
    "entryMode" : "MAGNETIC_STRIPE",
    "card" : {
      "expirationMonth" : "00",
      "expirationYear" : "00",
      "type" : "EBT",
      "maskedPan" : "507719XXXXXX4720"
    }
  },
  "additionalInformation" : {
    "requestId" : "7591366618376609904603"
  },
  "linkedOperations" : [ ],
  "tipAdjustStatus" : "NOT_ADJUSTABLE",
  "receipts" : {
    "merchantReceipt" : {
      "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n555555555\n\nPayment\n$1.00\n\nPlease retain receipt!\n\nCard: EBT\nAccount: **** **** **** 4720\nEntry Mode: Magstripe\nVerification: Verified by PIN\n\nTransaction: 673579\nAuthorization: 831000\nMerchant ID: ******************nt001\nTerminal ID: ****1459\n\n\nbd9c4ddd5bb84aafa42f16f2660f76c7\n\n2:34:22 PM: 9/29/2025\n\n\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "55555"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "New York"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United States"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "555555555"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "EBT"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 4720"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Magstripe"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "Verified by PIN"
          },
          "CLEARING_DETAILS_TRANSACTION_IDENTIFIER" : {
            "label" : "Transaction",
            "value" : "673579"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "831000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "******************nt001"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****1459"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Merchant Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Payment"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "bd9c4ddd5bb84aafa42f16f2660f76c7"
          },
          "AMOUNT_AND_CURRENCY" : {
            "label" : "Amount",
            "value" : "$1.00"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "9/29/2025"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "2:34:22 PM"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : false,
        "totalLineRequired" : false
      }
    },
    "customerReceipt" : {
      "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n555555555\n\nPayment\n$1.00\n\nPlease retain receipt!\n\nCard: EBT\nAccount: **** **** **** 4720\nEntry Mode: Magstripe\nVerification: Verified by PIN\n\nTransaction: 673579\nAuthorization: 831000\nMerchant ID: ******************nt001\nTerminal ID: ****1459\n\n\nbd9c4ddd5bb84aafa42f16f2660f76c7\n\n2:34:22 PM: 9/29/2025\n\n\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "55555"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "New York"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United States"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "555555555"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "EBT"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 4720"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Magstripe"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "Verified by PIN"
          },
          "CLEARING_DETAILS_TRANSACTION_IDENTIFIER" : {
            "label" : "Transaction",
            "value" : "673579"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "831000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "******************nt001"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****1459"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Cardholder Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Payment"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "bd9c4ddd5bb84aafa42f16f2660f76c7"
          },
          "AMOUNT_AND_CURRENCY" : {
            "label" : "Amount",
            "value" : "$1.00"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "9/29/2025"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "2:34:22 PM"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : false,
        "totalLineRequired" : false
      }
    }
  },
  "ebtDetails" : {
    "category" : "FOOD"
  }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
   "type": "ErrorResponse",
   "message": "Error message to display.",
   "developerDescription": "Detailed description of error."
   }
```

Custom Card Read {#sis-pymnt-svcs-cloud-custom-card-card-intro}
===============================================================

Use this information to obtain data from custom cards such as gift cards, loyalty program cards, and employee cards when the app is in Cloud mode. This service cannot be used to perform payment functions.
IMPORTANT Custom Card Read is supported for non-PCI cards only. To use this service, the card type must be on your allowlist. To add a card type to your allowlist, contact your implementation manager.  
To retrieve the card data, swipe the card's magnetic stripe through the payment device. The custom card read-only function reads and returns the raw card identifier to your app or point-of-sale (POS) system. You can then use the raw data within your app or POS system.  
These are examples of how you might use the Custom Card Read feature:

* **Custom gift card:** Use the card number to check a balance or process a payment in your private gift card network.
* **Employee card:** Use the card number to look up an employee's profile or account.
  {#sis-pymnt-svcs-cloud-custom-card-card-intro_ul_snq_dyx_xgc}  
  Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for a Custom Card Read {#sis-pymnt-svcs-cloud-custom-card-read-api-reqfields}
=============================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `ReadCardRequest`.

REST Example: Custom Card Read {#sis-pymnt-svcs-cloud-custom-card-read-ex-rest}
===============================================================================

Request

```
{
  "serialNumber": "1850000000",
  "request": {
    "type": "ReadCardRequest"
  }
}
```

Response to a Successful Request

```
{
   "type": "ReadCardResponse",
   "message": "Read Card Successfully",
   "cardDetails": {
     "expiryMonth": 12,
     "expiryYear": 2025,
     "track1": "%B4111111111111111^DOE/JOHN^2512101?",
     "track2": "4111111111111111=25121010000?",
     "cardNumber": "4111111111111111"
   }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
   "type": "ErrorResponse",
   "message": "Error message to display.",
   "developerDescription": "Detailed description of error."
}
```

Printing a Customer or Merchant Receipt {#sis-pymnt-svcs-cloud-receipt-print-intro}
===================================================================================

Use this information to print a customer or merchant receipt from a previous transaction when the app is in Cloud mode. This feature can be used only with terminals that have integrated printers.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields to Print a Customer or Merchant Receipt {#sis-pymnt-svcs-cloud-receipt-print-reqfield}
======================================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PrintReceiptRequest`.

request.transactionId
:
Set the value to the ID field value from the original transaction.

request.receiptType
:
Set the value to CUSTOMER or MERCHANT.

REST Example: Print a Customer or Merchant Receipt {#sis-pymnt-svcs-cloud-receipt-print-ex-rest}
================================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "PrintReceiptRequest",
        "transactionId": "8fe5fa21d0814424bcec4997c9dc89c4",
        "receiptType": "CUSTOMER"
    }
}
```

Response to a Successful Request

```
{
    "type": "PrintReceiptResponse",
    "message": "Receipt printed successfully."
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
    "type": "ErrorResponse",
    "message": "Error message to display.",
    "developerDescription": "Detailed description of error."
}
```

Custom Printing {#sis-pymnt-svcs-cloud-custom-print-intro}
==========================================================

Use this information to send a custom print request in Cloud mode. This feature enables you to print custom content directly to the integrated printer of a PAX terminal, including text, label-value pairs, images, barcodes, and QR codes.

> IMPORTANT  
> The Custom Printing feature does not affect your configuration for printing standard customer or merchant receipts.  
> Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/gateway/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for Custom Printing {#sis-pymnt-svcs-cloud-custom-print-reqfields}
==================================================================================

serialNumber
:
Set this field to the serial number of the terminal.

request.type
:
Set this field to `CustomPrintRequest`.

request.printLayout.sections
:
Set this field to a list of one or more print sections. Each section must include a sectionType field to identify the type of custom content to print.

Required Fields for Custom Printing by Section Type {#sis-pymnt-svcs-cloud-custom-print-sec-type-reqfields}
===========================================================================================================

Use these fields to define the required content for each custom print section in the request.printLayout.sections field. Each section in this field must include a sectionType field that identifies the type of content to print. The request.printLayout.sections field supports these sectionType values: `TEXT`, `BARCODE`, `IMAGE`, and `SPACER`. These values are case sensitive.

TEXT Section
------------

request.printLayout.sections\[n\].sectionType
:
Set this field to `TEXT`.

request.printLayout.sections\[n\].textContent.textType
:
Set this field to identify the type of text content. Supported values are `PARAGRAPH`, `LABEL_VALUE`, and `NO_LINE`.

TEXT Section: PARAGRAPH Text Content Required Fields
----------------------------------------------------

request.printLayout.sections\[n\].textContent.lines
:
Set this field to a list of one or more strings to print as paragraph lines.

TEXT Section: LABEL_VALUE Text Content Required Fields
------------------------------------------------------

request.printLayout.sections\[n\].textContent.content
:
Set this field to a list of one or more label-value pairs.

request.printLayout.sections\[n\].textContent.content\[n\].label.labelText
:
Set this field to the label text string.

request.printLayout.sections\[n\].textContent.content\[n\].value.valueText
:
Set this field to the value text string.

BARCODE Section
---------------

request.printLayout.sections\[n\].sectionType
:
Set this field to `BARCODE`.

request.printLayout.sections\[n\].content
:
Set this field to the data to encode in the barcode.

request.printLayout.sections\[n\].barcodeType
:
Set this field to the barcode format. Supported values are `CODE39`, `CODE128`, `EAN13`, `EAN128`, `PDF417`, and `QRCODE`.

IMAGE Section
-------------

request.printLayout.sections\[n\].sectionType
:
Set this field to `IMAGE`.

request.printLayout.sections\[n\].imageData
:
Set this field to a Base64-encoded image. Supported formats are `PNG`, `JPEG`, and `BMP`. The maximum image width and height is 384 pixels.

SPACER Section
--------------

request.printLayout.sections\[n\].sectionType
:
Set this field to `SPACER`.

Optional Fields for Custom Printing {#sis-pymnt-svcs-cloud-custom-print-optfields}
==================================================================================

Use these fields to define optional content and formatting for custom print sections in the request.printLayout.sections field. Optional fields are supported for `TEXT` and `SPACER` sections.

> IMPORTANT  
> If you do not specify the value for an optional field, the default value is used.

TEXT Section: PARAGRAPH Optional Fields
---------------------------------------

request.printLayout.sections\[n\].textContent.align
:
Set this field to `LEFT`, `CENTER`, or `RIGHT`. The default value is `LEFT`.

request.printLayout.sections\[n\].textContent.textStyle.size
:
Set this field to `SMALL`, `MEDIUM`, or `LARGE`. The default value is `MEDIUM`.

request.printLayout.sections\[n\].textContent.textStyle.style
:
Set this field to `NORMAL` or `EMPHASIZE`. The default value is `NORMAL`.

TEXT Section: LABEL_VALUE Optional Fields
-----------------------------------------

request.printLayout.sections\[n\].textContent.content\[n\].label.textStyle.size
:
Set this field to `SMALL`, `MEDIUM`, or `LARGE`. The default value is `MEDIUM`.

request.printLayout.sections\[n\].textContent.content\[n\].label.textStyle.style
:
Set this field to `NORMAL` or `EMPHASIZE`. The default value is `NORMAL`.

request.printLayout.sections\[n\].textContent.content\[n\].value.textStyle.size
:
Set this field to `SMALL`, `MEDIUM`, or `LARGE`. The default value is `MEDIUM`.

request.printLayout.sections\[n\].textContent.content\[n\].value.textStyle.style
:
Set this field to `NORMAL` or `EMPHASIZE`. The default value is `NORMAL`.

SPACER Section Optional Fields
------------------------------

request.printLayout.sections\[n\].lines
:
Set this field to the number of blank lines to insert. The default value is `1`.

REST Example: Custom Printing {#sis-pymnt-svcs-cloud-custom-print-ex-rest}
==========================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "CustomPrintRequest",
        "printLayout": {
            "sections": [
                {
                    "sectionType": "TEXT",
                    "textContent": {
                        "textType": "PARAGRAPH",
                        "lines": ["ACME STORE", "123 Main St"],
                        "align": "CENTER",
                        "textStyle": {
                            "size": "LARGE",
                            "style": "NORMAL"
                        }
                    }
                },
                {
                    "sectionType": "IMAGE",
                    "imageData": "iVBORw0KGgoAAAANS..."
                },
                {
                    "sectionType": "SPACER",
                    "lines": 1
                },
                {
                    "sectionType": "TEXT",
                    "textContent": {
                        "textType": "LABEL_VALUE",
                        "content": [
                            {
                                "label": {
                                    "labelText": "Subtotal",
                                    "textStyle": { "size": "MEDIUM", "style": "NORMAL" }
                                },
                                "value": {
                                    "valueText": "$23.45",
                                    "textStyle": { "size": "MEDIUM", "style": "NORMAL" }
                                }
                            },
                            {
                                "label": {
                                    "labelText": "Total",
                                    "textStyle": { "size": "LARGE", "style": "NORMAL" }
                                },
                                "value": {
                                    "valueText": "$25.99",
                                    "textStyle": { "size": "LARGE", "style": "NORMAL" }
                                }
                            }
                        ]
                    }
                },
                {
                    "sectionType": "BARCODE",
                    "content": "TXN123456789",
                    "barcodeType": "CODE128"
                }
            ]
        }
    }
}
```

Response to a Successful Request

```
{
    "type": "CustomPrintResponse",
    "message": "Custom Print successfully"
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Custom Screens {#sis-pymnt-svcs-cloud-custom-screens-intro}
===========================================================

Use this information to send a custom screen request in Cloud mode. This feature enables you to show one or more customized screens on the payment terminal. Custom screen can show informational text, collect text input, or capture a digital signature.

Endpoints
---------

**Test:** `POST https://terminalstest.example.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.example.com/v1/cloud/transactions`

Required Fields for Custom Screens {#sis-pymnt-svcs-cloud-custom-screens-reqfields}
===================================================================================

serialNumber
:
Set this field to the serial number of the terminal.

request.type
:
Set this field to `CustomScreenRequest`.

request.screens
:
Set this field to a list of one or more screen objects. Each screen must include a screenType field to identify the type of custom screens to show on the payment terminal.

Required Fields for Custom Screens by Screen Type {#sis-pymnt-svcs-cloud-custom-screens-type-reqfields}
=======================================================================================================

Use these fields to define the required content for each custom screen in the request.screens field. Each screen in this field must include a screenType field that identifies the type of custom screen to show on the payment terminal. The request.screens field supports these screenType values: `textDisplay`, `textInput`, and `signatureCapture`.

textDisplay Screen
------------------

request.screens\[n\].screenType
:
Set this field to `textDisplay`.

request.screens\[n\].title
:
Set this field to the screen title. The title cannot exceed 20 characters.

textInput Screen
----------------

request.screens\[n\].screenType
:
Set this field to `textInput`.

request.screens\[n\].title
:
Set this field to the screen title. The title cannot exceed 20 characters.

request.screens\[n\].textInputs
:
Set this field to a list of one or more text input fields.

request.screens\[n\].textInputs\[n\].textInputLabel
:
Set this field to the label for the input field. The label cannot exceed 25 characters.

request.screens\[n\].textInputs\[n\].textInputConfig.textInputType
:
Set this field to the type of input to accept. Supported values are `NUMERIC`, `ALPHANUMERIC`, `EMAIL`, and `PHONE`.

signatureCapture Screen
-----------------------

request.screens\[n\].screenType
:
Set this field to `signatureCapture`.

request.screens\[n\].title
:
Set this field to the screen title. The title cannot exceed 20 characters.

Optional Fields for Custom Screens {#sis-pymnt-svcs-cloud-custom-screens-optfields}
===================================================================================

Use these fields to define optional content and formatting for custom screens in the request.screens field. Optional fields are available for all screen types, with additional optional fields supported for textDisplay and textInput screens.

> IMPORTANT  
> If you do not specify the value for an optional field, the default value is used.

Optional Fields Available on All Screen Types
---------------------------------------------

request.screens\[n\].description
:
Set this field to a descriptive message displayed below the title.

request.screens\[n\].isSkippable
:
Set this field to `true` to allow the cardholder to skip the screen. The default value is `false`.

textDisplay Screen Optional Fields
----------------------------------

request.screens\[n\].toggles
:
Set this field to a list of toggle items for the cardholder to accept or decline.

request.screens\[n\].toggles\[n\].label
:
Set this field to the label displayed next to the toggle. The label cannot exceed 40 characters.

request.screens\[n\].toggles\[n\].required
:
Set this field to `true` to require the cardholder to enable the toggle before proceeding. The default value is `false`.

textInput Screen Optional Fields
--------------------------------

request.screens\[n\].textInputs\[n\].textInputHint
:
Set this field to placeholder hint text displayed inside the input field.

request.screens\[n\].textInputs\[n\].textInputConfig.masked
:
Set this field to `true` to mask the input characters as the cardholder types. The default value is `false`.

request.screens\[n\].textInputs\[n\].textInputConfig.length.min
:
Set this field to the minimum number of characters required. Must be greater than zero.

request.screens\[n\].textInputs\[n\].textInputConfig.length.max
:
Set this field to the maximum number of characters allowed. Must be greater than zero and not less than the defined minimum number of characters

request.screens\[n\].textInputs\[n\].textInputConfig.patternConfig.pattern
:
Set this field to a regular expression that the input value must match.

request.screens\[n\].textInputs\[n\].textInputConfig.patternConfig.patternError
:
Set this field to the error message displayed when the input does not match the pattern.

request.screens\[n\].toggles
:
Set this field to a list of toggle items for the cardholder to accept or decline.

request.screens\[n\].toggles\[n\].label
:
Set this field to the label displayed next to the toggle. The label cannot exceed 40 characters.

request.screens\[n\].toggles\[n\].required
:
Set this field to `true` to require the cardholder to enable the toggle before proceeding. The default value is `false`.

REST Example: Custom Screens {#sis-pymnt-svcs-cloud-custom-screens-ex-rest}
===========================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "CustomScreenRequest",
        "screens": [
            {
                "screenType": "signatureCapture",
                "title": "Confirm Receipt",
                "description": "I certify that I am the authorized representative to receive these goods...",
                "isSkippable": false
            },
            {
                "screenType": "textDisplay",
                "title": "Liability Waiver",
                "description": "By proceeding, you acknowledge inspection of goods...",
                "isSkippable": false,
                "toggles": [
                    {
                        "label": "I accept the terms",
                        "required": true
                    }
                ]
            },
            {
                "screenType": "textInput",
                "title": "Purchase Order (PO)",
                "description": "Please enter the authorized Purchase Order (PO) number...",
                "isSkippable": false,
                "textInputs": [
                    {
                        "textInputLabel": "Authorized PO Number",
                        "textInputHint": "PO518736",
                        "textInputConfig": {
                            "textInputType": "ALPHANUMERIC",
                            "masked": true,
                            "length": {
                                "min": 5,
                                "max": 10
                            },
                            "patternConfig": {
                                "pattern": "^[a-zA-Z0-9]*$",
                                "patternError": "Only letters and numbers allowed"
                            }
                        }
                    }
                ],
                "toggles": [
                    {
                        "label": "I accept the terms",
                        "required": true
                    }
                ]
            }
        ]
    }
}
```

Response to a Successful Request

```
{
    "type": "CustomScreenResponse",
    "message": "Data capture successful",
    "customScreenDetails": {
        "status": "COMPLETED",
        "screens": [
            {
                "screenType": "signatureCapture",
                "title": "Confirm Receipt",
                "signatureData": "iVBORw0KGgoAAAANSUhEUg....",
                "skipped": false
            },
            {
                "screenType": "textDisplay",
                "title": "Liability Waiver",
                "toggles": [
                    {
                        "label": "I accept the terms",
                        "value": true
                    }
                ],
                "skipped": false
            },
            {
                "screenType": "textInput",
                "title": "Purchase Order (PO)",
                "inputs": [
                    {
                        "label": "Authorized PO Number",
                        "value": "PO518736"
                    }
                ],
                "toggles": [
                    {
                        "label": "I accept the terms",
                        "value": true
                    }
                ],
                "skipped": false
            }
        ]
    }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
          "type": "ErrorResponse",
          "message": "Error message to display.",
          "developerDescription": "Detailed description of error."
    }
```

