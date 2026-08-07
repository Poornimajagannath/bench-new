Local Mode Payment Services {#semi-integrated-pymnt-svcs-intro}
===============================================================

Use this information to process payment services available in the Acceptance Devices app when operated in Local mode.  
These are some Local mode features:

* The point-of-sale (POS) system communicates with the Acceptance Devices app on the terminal over a local Wi-Fi network.

* You can retrieve the Root CA certificate to validate the Acceptance Devices app server's certificate.

* You have the option to activate an mTLS connection in the Acceptance Devices app.

* You have the option to implement hostname validation in your client.
  {#semi-integrated-pymnt-svcs-intro_ul_rts_tjh_bbc}  
  For information about other modes available in the Acceptance Devices app, see:

* [Cloud Mode Payment Services](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro.md "")

* [Standalone Mode Payment Services](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-standalone-mode-intro.md "")
  {#semi-integrated-pymnt-svcs-intro_ul_l5b_yqm_3fc}

Communication Protocol Used in Local Mode {#semi-integrated-ad-app-comm-protocol}
=================================================================================

When using the solution in Local mode, the communication protocol used between the Acceptance Devices app and the point-of-sale (POS) system is a single WebSocket channel. Through this channel, simultaneous, two-way communication occurs between the Acceptance Devices app and the POS system.

Retrieving the Root CA Certificate {#semi-integrated-ad-app-retrieve-rootca-cert-intro}
=======================================================================================

When the app is operating in Local mode, you can validate the Acceptance Devices app server's certificate by adding the Root CA certificate to your trust store. This action is required if you want to use an mTLS connection. For more information, see [Activating a Secure mTLS Connection](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-activate-mtls-connection-intro.md "").  
You can retrieve the Root CA certificate in the `Business Center` or by using a REST API request.

Retrieve the Root CA Certificate in the `Business Center` {#sis-ad-app-retrieve-rootca-cert-ebc}
================================================================================================

Follow these steps to retrieve the Root CA certificate in the Business Center:

1. In the `Business Center`, go to the left navigation panel and choose Acceptance Devices \&gt; Activation Codes. The Activation Codes page appears.
2. Click Download Root CA Certificate. When the download is complete, the browser window shows a download completion message.
3. In the local folder directory of your computer, navigate to the Download folder to access the Root CA certificate file.

Retrieve the Root CA Certificate Using a REST API Request {#semi-integrated-ad-app-retrieve-rootca-cert-task}
=============================================================================================================

You can use a REST API request to retrieve the Acceptance Devices app server's Root CA certificate when the app is operating in Local mode. You would then add the certificate to your trust store.  
You must authenticate each API request you send to a `Cybersource` API by using a REST shared secret key or a REST certificate. For more information about authentication requirements, see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md "").

Endpoints
---------

**Test:** `GET ``https://apitest.cybersource.com``/dms/v2/devices/certificates/rootca`  
**Production:** `GET ``https://api.cybersource.com``/dms/v2/devices/certificates/rootca`

Required Fields to Retrieve the Root CA Certificate Using a REST API Request {#semi-integrated-ad-app-retrieve-rootca-cert-api-reqfields}
=========================================================================================================================================

The body of the API request is empty.

REST Example: Retrieve the Root CA Certificate Using a REST API Request {#semi-integrated-ad-app-retrieve-rootca-cert-api-ex-rest}
==================================================================================================================================

Request  
The body of the request is empty.

```
{
}
```

Response to a Successful Request  
The response includes a PEM--encoded certificate chain.

```
{
    "certificateChain": "-----BEGIN CERTIFICATE-----Your certificate response data appears here.-----END CERTIFICATE-----"
}
```

Activating a Secure mTLS Connection {#sis-activate-mtls-connection-intro}
=========================================================================

When the app is operating in Local mode, using a Mutual Transport Layer Security (mTLS) connection creates an additional layer of security for communication between the Acceptance Devices app running on your PAX terminal and point-of-sale (POS) system.  
Using the mTLS protocol is recommended because it employs two-way verification. The minimum requirement for providing end-to-end data security is using the Transport Layer Security (TLS) protocol.  
Before activating an mTLS connection, you must retrieve the Root CA certificate. For more information, see [Retrieving the Root CA Certificate](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/semi-integrated-ad-app-retrieve-rootca-cert-intro.md "").

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** `POST https://{terminal IP address:port number}/ or wss://{terminal IP address:port number}/`  
**Production:** `POST https://{terminal IP address:port number}/ or wss://{terminal IP address:port number}/`

Generate a POS Connection Code for the Point-of-Sale System {#sis-activate-mtls-pos-setup-code}
===============================================================================================

Before you can sync the terminal with the point-of-sale (POS) system to establish a secure connection, you must activate the terminal. For more information, see [Activating a Terminal in the Acceptance Devices App](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-get-started-intro/semi-integrated-solution-ad-app-activate-terminal-.md ""). To ensure the security of the data sent over the internet between your POS system and the PAX terminal, you must establish a secure connection (sync) between your system and the terminal. You must complete this procedure one time only for each POS system you are using.  
If Mutual Transport Layer Security (mTLS) is enabled, and terminal activation is complete, the Generate Code screen appears during terminal set up.  
Follow these steps to generate a POS connection code for a POS system in the Acceptance Devices app:

1. On the Generate Code screen, tap Generate Code.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-activating-secure-mtls-connection-1.png/jcr:content/renditions/original)
2. Record the eight-character code that appears on the screen. You will use this code to request a certificate from the POS system. The screen shows an expiration timer for the code, which refreshes every 300 seconds.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-activating-secure-mtls-connection-2.png/jcr:content/renditions/original)

Request Certificates for the Point-of-Sale System {#sis-activate-mtls-pos-setup-request-cert}
=============================================================================================

Before you can request certificates, you must generate a set-up code for the POS system. To finish activating the secure mTLS connection, request certificates for the POS system by sending a request to the PAX terminal through the POS system.

1. On the Generate Code screen, tap the Details arrow. The Details section expands to show the HTTP and WSS (WebSocket) addresses and the port number.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-activating-secure-mtls-connection-3.png/jcr:content/renditions/original)
2. Record the HTTP and WSS addresses and port number shown in the Details section. You will use this information to request a certificate through the POS system, using the HTTPS or WSS address.
3. To request the certificates, send an API request through the POS system to the HTTP or WSS address and port number, along with the POS connection code shown on the terminal and a unique POS ID.
4. After the certificates are retrieved by the POS system and the sync between your POS system and the PAX terminal is complete, the *POS Activation Successful* message appears. Tap Close. The next set-up screen appears.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-activating-secure-mtls-connection-4.png/jcr:content/renditions/original)

Required Fields to Request Certificates for the Point-of-Sale System {#sis-activate-mtls-pos-setup-request-cert-api-reqfields}
==============================================================================================================================

posId
:
Set the value to a unique, user-defined ID for the POS system.

setupCode
:
Set the value to the POS connection code shown on the Generate POS Connection Code screen in the Acceptance Devices app.

REST Example: Request Certificates for the Point-of-Sale System {#sis-activate-mtls-pos-setup-request-cert-api-ex-rest}
=======================================================================================================================

Request

```
{
  "posId" : "123",
  "setupCode" : "8QW1YS1D"
}
```

Response to a Successful Request  
The response includes the private key and certificates required to establish the secure Mutual Transport Layer Security (mTLS) connection between the PAX terminal and the POS system. For security reasons, this example does not show actual private key and certificate response data.

```
-----BEGIN RSA PRIVATE KEY-----
Your RSA private key response data appears here.
-----END RSA PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
Your certificate response data appears here.
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
Your certificate response data appears here.
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
Your certificate response data appears here.
-----END CERTIFICATE-----
```

Implementing Hostname Validation in Local Mode {#sis-local-ad-app-hostname-validate}
====================================================================================

When operating in Local mode, your app can optionally perform hostname validation for enhanced security. When the terminal is activated, a certificate is generated on the device. The certificate includes a Subject Alternative Name (SAN). This SAN appears as a Domain Name System (DNS) entry for the Acceptance Devices app server.  
This is the SAN format:

```
{terminal-serial-number}.cybs.seclib.io
```

To enable hostname validation or connect to the terminal using the SAN instead of its IP address, update your system's `hosts` file to include both the terminal's IP address and its corresponding SAN.

Sale {#semi-integrated-pax-pymnt-svcs-sale-api-intro}
=====================================================

Use this information to process a sale transaction when the app is in Local mode. This type of transaction combines an authorization and a capture into a single transaction.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Sale {#semi-integrated-pax-pymnt-svcs-sale-api-reqfields}
===============================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

REST Example: Sale {#semi-integrated-pax-pymnt-svcs-sale-api-ex-rest}
=====================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
      "amountDetails" : {
        "amount" : "1.00",
        "currency" : "GBP"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Refund {#sis-pymnt-svcs-refund-api-intro}
=========================================

Use this information to process a refund when the app is in Local Mode mode. This type of refund includes a reference to the original transaction for a full or partial transaction amount. Stand-alone credits are also supported in this Acceptance Devices solution. For more information, see [Stand-Alone Credit](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-local-standalone-credit-api-intro.md "").

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Refund {#sis-pymnt-svcs-refund-api-reqfields}
===================================================================

type
:
Set the value to `LinkedRefundRequest`.

transactionId
:
Set the value to the `id` field value from the original transaction.

Optional Fields for a Refund {#sis-pymnt-svcs-refund-api-optfields}
===================================================================

Use the optional amount and currency fields to process a partial refund. Otherwise, the full amount will be refunded.

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

REST Example: Refund {#sis-pymnt-svcs-refund-api-ex-rest}
=========================================================

Request

```
{
      "type": "LinkedRefundRequest",
      "transactionId": "8fe5fa21d0814424bcec4997c9dc89c4",
      "amountDetails": {
        "amount": "1.00",
        "currency": "GBP"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Stand-Alone Credit {#sis-local-standalone-credit-api-intro}
===========================================================

Use this information to process a stand-alone credit when the app is in Local mode. This type of transaction is used to process a credit without reference to the original transaction. The customer is required to present their card for this type of transaction.

> WARNING
> When processing a stand-alone credit, there is no limit on the credit amount because there is no reference to the original transaction amount. The recommendation is to use a refund transaction whenever possible. For more information, see [Refund](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-pymnt-svcs-refund-api-intro.md "").

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Stand-Alone Credit {#sis-local-standalone-credit-api-reqfields}
=====================================================================================

type
:
Set the value to `StandaloneRefundRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

REST Example: Stand-Alone Credit {#sis-local-standalone-credit-api-ex-rest}
===========================================================================

Request

```
{
      "type": "StandaloneRefundRequest",
      "merchantReferenceCode": "2490c8ec0e2f4b509526815714313e33",
      "amountDetails": {
        "amount": "1.00",
        "currency": "GBP"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Request a Check Transaction Status {#semi-integrated-pax-pymnt-svcs-txn-status-api-intro}
=========================================================================================

Use this information to request a check transaction status when the app is in Local mode. This transaction is used to obtain response data for a transaction that was lost or timed out.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields to Request a Check Transaction Status {#semi-integrated-pax-pymnt-svcs-txn-status-api-reqfields}
================================================================================================================

type
:
Set the value to `TransactionLookupRequest`.

idType
:
Set the value to `TRANSACTION_ID` or `MERCHANT_REFERENCE_CODE`.

id
:
Set the value to the `id` or merchantReferenceCode field value from the original transaction.

REST Example: Request a Check Transaction Status {#semi-integrated-pax-pymnt-svcs-txn-status-api-ex-rest}
=========================================================================================================

Request

```
{
      "type": "TransactionLookupRequest",
      "idType": "TRANSACTION_ID",
      "id": "1541387b383d456aabb81cdf558b4e8e"
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Cancel Transaction {#semi-integrated-pax-pymnt-svcs-cancel-txn-api-intro}
=========================================================================

Use this information to process a cancel transaction request in Local mode. This request is sent to interrupt an in-process transaction.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** `wss://{terminal IP address:port number}/`  
**Production:** `wss://{terminal IP address:port number}/`

Required Fields to Cancel Transaction {#semi-integrated-pax-pymnt-svcs-cancel-txn-api-reqfields}
================================================================================================

type
:
Set the value to `CancelRequest`.

REST Example: Cancel Transaction {#semi-integrated-pax-pymnt-svcs-cancel-txn-api-ex-rest}
=========================================================================================

Request

```
{
      "type": "CancelRequest"
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Sale with On-Reader Tipping {#sis-local-sale-on-reader-tip-api-intro}
=====================================================================

Use this information to process a sale with on-reader tipping in Local mode. At the start of each transaction, the terminal prompts the customer to add a tip by showing suggested tip amounts. The customer selects or enters a tip amount on the terminal before presenting their payment card.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Sale with On-Reader Tipping {#sis-local-sale-on-reader-tip-api-reqfields}
===============================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

askForTip
:
Set the value to `ON_DEVICE`.

REST Example: Sale with On-Reader Tipping {#sis-local-sale-on-reader-tip-api-ex-rest}
=====================================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "adf0fa5ca70d462ba5fc0249436b656c",
      "amountDetails" : {
        "amount" : "5.00",
        "currency" : "GBP"
      },
      "askForTip" : "ON_DEVICE"
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Sale with On-Receipt Tipping {#sis-pymnt-svcs-sale-on-receipt-tip-intro}
========================================================================

Use this information to process a sale with on-receipt tipping when the app is in Local mode. After the original transaction is pre-authorized, the customer writes the tip or total amount on the printed receipt. A follow-on tip adjust request must be sent within 24 hours to capture the transaction. For more information, see [Tip Adjust](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-pymnt-svcs-sale-on-receipt-tip-intro/sis-pymnt-svcs-tip-adjust-on-receipt-sale-intro.md "").

> WARNING
> By using this feature, you assume the risk of overcaptures being declined and increased chargebacks, so use it only when necessary. Process sales with on-reader tipping, whenever possible. For more information, see [Sale with On-Reader Tipping](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-local-sale-on-reader-tip-api-intro.md "").

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Sale with On-Receipt Tipping {#sis-pymnt-svcs-sale-on-receipt-tip-api-reqfields}
======================================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

capture
:
Set the value to `false`.

askForTip
:
Set the value to `ON_RECEIPT`.

REST Example: Sale with On-Receipt Tipping {#sis-pymnt-svcs-sale-on-receipt-tip-api-ex-rest}
============================================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "1ce594be142142f4913cca805830a176",
      "amountDetails" : {
        "amount" : "20.00",
        "currency" : "USD"
      },
      "capture" : false,
      "askForTip" : "ON_RECEIPT"
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Tip Adjust {#sis-pymnt-svcs-tip-adjust-on-receipt-sale-intro}
=============================================================

Use this information to process a tip adjust when the app is in Local Mode mode. This follow-on transaction is required when processing an on-receipt tipping transaction. The tip adjust request must be sent within 24 hours to capture the transaction.  
After the original transaction is pre-authorized, the customer writes the tip or total amount on the printed receipt. A follow-on tip adjust request is then sent to capture the additional tip amount. This transaction is also referred to as an *overcapture* . For more information, see [Sale with On-Receipt Tipping](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-pymnt-svcs-sale-on-receipt-tip-intro.md "").

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Tip Adjust {#sis-pymnt-svcs-tip-adjust-on-receipt-sale-api-reqfields}
===========================================================================================

type
:
Set the value to `TipAdjustRequest`.

transactionId
:
Set the value to the id field value from the original transaction.

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

REST Example: Tip Adjust {#sis-pymnt-svcs-tip-adjust-on-receipt-sale-api-ex-rest}
=================================================================================

Request

```
{
      "type": "TipAdjustRequest",
      "transactionId": "c6174c80b81f4413a4b9f2065c5431c7",
      "amountDetails": {
        "amount": "4.00",
        "currency": "USD"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Token Refund {#semi-integrated-pax-pymnt-svcs-token-refund-api-intro}
=====================================================================

Use this information to process a token refund when the app is in Local mode. A token refund transaction enables you to process a stand-alone credit against a tokenized card. To process a credit through a token, you must have the `Token Management Service` product enabled and an existing (saved) token from a tokenized transaction. For more information, see [Token Management Service](https://developer.cybersource.com/docs/cybs/en-us/tms/developer/ctv/rest/tms/tms-overview.md "").

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Token Refund {#semi-integrated-pax-pymnt-svcs-token-refund-api-reqfields}
===============================================================================================

type
:
Set the value to `TokenRefundRequest`.

instrumentId
:
Set the value to the Instrument Identifier token.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

REST Example: Token Refund {#semi-integrated-pax-pymnt-svcs-token-refund-api-ex-rest}
=====================================================================================

Request

```
{
      "type": "TokenRefundRequest",
      "instrumentId": "7030000000022690119",
      "merchantReferenceCode": "30ed45dc7b3f4fb9905413940ac30363",
      "amountDetails": {
        "amount": "1.00",
        "currency": "GBP"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Pre-Authorization {#semi-integrated-pax-pymnt-svcs-pre-auth-api-intro}
======================================================================

Use this information to process a pre-authorization for an initial amount in Local mode. A pre-authorization transaction places a temporary hold on the customer's payment card. The transaction amount can be captured at a later time.  
Most authorizations expire in 5 to 7 days. The issuing bank sets the length of time before expiration. When an authorization expires with the issuing bank, your bank or processor might require you to re-submit an authorization request and include a request for capture in the same message. For more information, see [Capture](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/semi-integrated-pax-pymnt-svcs-capture-api-intro.md "").

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Pre-Authorization {#semi-integrated-pax-pymnt-svcs-pre-auth-api-reqfields}
================================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

capture
:
Set the value to `false`.

REST Example: Pre-Authorization {#semi-integrated-pax-pymnt-svcs-pre-auth-api-ex-rest}
======================================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "47bd9ed54f3f4bfabb9d3ee94cfa3008",
      "amountDetails" : {
        "amount" : "1.00",
        "currency" : "GBP"
      },
      "capture" : false
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
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

Incremental Authorization {#semi-integrated-pax-pymnt-svcs-increm-auth-api-intro}
=================================================================================

Use this information to process an incremental authorization in Local mode. This type of request can be made on a pre-authorization transaction to increase the authorized amount before it is captured.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for an Incremental Authorization {#semi-integrated-pax-pymnt-svcs-increm-auth-api-reqfields}
============================================================================================================

type
:
Set the value to `IncrementalAuthorizationRequest`.

transactionId
:
Set the value to the `id` field value from the original transaction.

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

REST Example: Incremental Authorization {#semi-integrated-pax-pymnt-svcs-increm-auth-api-ex-rest}
=================================================================================================

Request

```
{
      "type": "IncrementalAuthorizationRequest",
      "transactionId": "e43069fbf85543659e478edd8d50f244",
      "amountDetails": {
        "amount": "2.00",
        "currency": "GBP"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Capture {#semi-integrated-pax-pymnt-svcs-capture-api-intro}
===========================================================

Use this information to capture a pre-authorized transaction in Local mode. The capture request references the approved pre-authorization request.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Capture {#semi-integrated-pax-pymnt-svcs-capture-api-reqfields}
=====================================================================================

type
:
Set the value to `CaptureRequest`.

transactionId
:
Set the value to the `id` field value from the original transaction.

Optional Fields for a Capture {#sis-pymnt-svcs-capture-api-optfields}
=====================================================================

Use the optional amount and currency fields to process a partial capture. Otherwise, the full amount will be captured.

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

REST Example: Capture {#semi-integrated-pax-pymnt-svcs-capture-api-ex-rest}
===========================================================================

Request

```
{
      "type": "CaptureRequest",
      "transactionId": "cb6475bafbb94d03b0f984629c63c294",
      "amountDetails": {
        "amount": "3.00",
        "currency": "GBP"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Mail Order or Telephone Order {#sis-local-moto-trxns-intro}
===========================================================

Use this information to process a mail order or telephone order (MOTO) sale and other transactions in Local mode. The payment card is not presented physically at the terminal for a MOTO transaction because it is a card-not-present transaction.  
You can also process these MOTO transactions in Local mode:

Account Verification
:
A MOTO account verification request submits a zero-amount authorization request to validate the payment card.

Pre-authorization
:
A MOTO pre-authorization request places a temporary hold on the customer's payment card, enabling the transaction to be captured at a later time. Most authorizations expire within 5 to 7 days. However, the exact duration is determined by the issuing bank.

    When an authorization expires, your bank, the payment processor, or issuing bank might require you to re-submit the authorization request. In such cases, you might be required to include the capture instructions in the same message to ensure successful processing.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for Mail Order or Telephone Order {#sis-local-moto-trxns-reqfields}
===================================================================================

type
:
Set the value to `PaymentRequest` for a sale or to `AccountVerificationRequest` for an account verification.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

paymentMode
:
Set the value to `MOTO`.

Optional Fields for Mail Order or Telephone Order {#sis-local-moto-trxns-optfields}
===================================================================================

capture
:
Set the value to `false` for a pre-authorization.

REST Example: Mail Order or Telephone Order Sale {#sis-local-moto-trxns-sale-ex-rest}
=====================================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "a7fbcdc92425456fa0db29c8670a3150",
      "amountDetails" : {
        "amount" : "1.00",
        "currency" : "GBP"
      },
      "paymentMode": "MOTO"
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Account Verification {#sis-local-acct-verif-api-intro}
======================================================

Use this information to process an account verification when the app is in Local mode. The account verification transaction submits a zero-amount authorization request to validate the payment card.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** `wss://{terminal IP address:port number}/`  
**Production:** `wss://{terminal IP address:port number}/`

Required Fields for an Account Verification {#sis-local-acct-verif-api-reqfields}
=================================================================================

type
:
Set the value to `AccountVerificationRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.currency
:
Set the value to the currency code.

REST Example: Account Verification {#sis-local-acct-verif-api-ex-rest}
======================================================================

Request

```
{
      "type": "AccountVerificationRequest",
      "merchantReferenceCode": "ec119c3b377542b09132867d236dc834",
      "amountDetails": {
        "currency": "GBP"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Offline Transactions {#sis-pymnt-svcs-offline-txn-intro}
========================================================

Offline mode is an optional feature that you can use to process offline sale and refund transactions when an internet connection is not available. The device must be operating in Local mode to enable or disable this feature. The default setting is `Disabled`.  
You can enable or disable Offline mode in the Acceptance Devices app, through a REST API request, or in the `Business Center`, where you can also customize settings. For more information, see [Customizing the Acceptance Devices App](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-get-started-intro/sis-ad-app-customize-intro.md "").

> WARNING
> By using this feature, you assume the risk of failed transactions and the possibility of increased fraud and chargebacks. Process transactions offline only when required, such as during an internet outage. Whenever possible, process transactions online instead. For more information, see [Sale](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/semi-integrated-pax-pymnt-svcs-sale-api-intro.md "").  
> When an internet connect is available, you must submit the offline transactions batch for authorization while the app is in Offline mode. For more information, see [Submit an Offline Transactions Batch for Authorization](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-pymnt-svcs-offline-txn-intro/sis-pymnt-svcs-offline-txn-batch-auth.md "").

Enable or Disable Offline Mode in the Acceptance Device App {#sis-pymnt-svcs-offline-txn-ad-app}
================================================================================================

IMPORTANT The recommendation is to resume operating in online mode as soon as an internet connection is available. To do so, you must first disable Offline mode.  
Follow these steps to enable or disable Offline mode in the Acceptance Device App:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Offline Mode.
4. Toggle Enable Offline Mode to ON or OFF.
5. Tap the back navigation arrow to return to the home screen.

Enable or Disable Offline Mode Using a REST API Request {#sis-pymnt-svcs-offline-txn-api-intro}
===============================================================================================

Use this information to enable or disable Offline mode in your POS system by using a REST API request.  
When Offline mode is disabled, the offline transactions batch is automatically submitted for authorization. Make sure that an internet connection is available before disabling Offline mode.

> IMPORTANT The recommendation is to resume operating in online mode as soon as an internet connection is available. To do so, you must first disable Offline mode.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields to Enable or Disable Offline Mode Using a REST API Request {#sis-pymnt-svcs-offline-txn-api-reqfields}
======================================================================================================================

type
:
Set the value to `OfflineModeRequest`.

enabled
:
Set the value to `true` to enable Offline mode or to `false` to disable Offline mode.

REST Example: Enable or Disable Offline Mode Using a REST API Request {#sis-pymnt-svcs-offline-txn-apii-ex-rest}
================================================================================================================

Request

```
{
  "type": "OfflineModeRequest",
  "enabled": true
}
```

Mid-Transaction Status Updates  
During the operation, you might receive one or more update responses indicating the current status of the operation. You can choose to display these updates on your point-of-sale (POS) system.

```
{
  "type": "OperationStatusResponse",
  "message": "Status update to display."
}
```

Response to a Successful Request

```
{
  "type": "OfflineModeResponse",
  "message": "Offline mode enabled."
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

Offline Sale {#sis-pymnt-svcs-offline-txn-sale-intro}
=====================================================

Use this information to process an offline sale when the app is in Local mode and Offline mode is enabled to process transactions. This type of transaction combines an authorization and a capture into a single transaction.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for an Offline Sale {#sis-pymnt-svcs-offline-txn-sale-api-reqfields}
====================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

REST Example: Offline Sale {#sis-pymnt-svcs-offline-txn-sale-api-ex-rest}
=========================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
      "amountDetails" : {
        "amount" : "1.00",
        "currency" : "GBP"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment accepted",
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
        "status" : "ACCEPTED",
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

Offline Refund {#sis-pymnt-svcs-offline-txn-refund}
===================================================

Follow these steps to process an offline refund when the app is in Local mode and Offline mode is enabled to process transactions.

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Offline Mode.
4. Tap the transaction you want to refund.
5. Tap Refund.
6. Enter the transaction amount.
7. Tap Refund to start the transaction.

Submit an Offline Transactions Batch for Authorization {#sis-pymnt-svcs-offline-txn-batch-auth}
===============================================================================================

IMPORTANT The recommendation is to submit the batch for authorization as soon as an internet connection is available. To submit a batch, Offline mode must be enabled.  
Follow these steps to submit an offline transactions batch for authorization when Offline mode is enabled.

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Offline Mode.
4. Tap Submit Offline Batch.

Cashback {#semi-integrated-pymnt-svcs-cashback-intro}
=====================================================

Use this information to process a cashback transaction when the app is in Local mode. This type of transaction enables customers to request that a specified amount of cash to be given to them as part of the transaction. A cashback transaction can be processed with or without a purchase.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Cashback {#semi-integrated-pymnt-svcs-cashback-api-reqfields}
===================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

amountDetails.cashbackAmount
:
Set the value to the cashback amount.

REST Example: Cashback {#semi-integrated-pymnt-svcs-cashback-api-ex-rest}
=========================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "bd74d30930e349548fd9d125f88291bc",
      "amountDetails" : {
        "amount" : "20.00",
        "currency" : "GBP",
        "cashbackAmount" : "5.00"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Sale with Installment Details {#sis-pymnt-svcs-semi-sale-installment-details-intro}
===================================================================================

Use this information to process a sale transaction with installment details when the app is in Local mode. This type of transaction can be used to include the required installment details as part of the sale transaction.  
This transaction is available only in the Latin American and Caribbean (LAC) region.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Sale with Installment Details {#sis-pymnt-svcs-semi-sale-installment-details-reqfields}
=============================================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

Optional Fields for a Sale with Installment Details {#sis-pymnt-svcs-semi-sale-installment-details-optfields}
=============================================================================================================

Use one or more of the optional installmentDetails fields to provide additional installment details.

installmentDetails.numberOfInstallments
:
Set the value to the number of installments.

installmentDetails.planType
:
Set the value to `MERCHANT_FUNDED` or `ISSUER_FUNDED`.

installmentDetails.interestPlan
:
Set the value to `true` or `false`.

installmentDetails.governmentPlan
:
Set the value to `true` or `false`.

REST Example: Sale with Installment Details {#sis-pymnt-svcs-semi-sale-installment-details-ex-rest}
===================================================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
      "amountDetails" : {
        "amount" : "20.00",
        "currency" : "USD"
      },
      "installmentDetails": {
        "numberOfInstallments": 5,
        "planType": "MERCHANT_FUNDED",
        "interestPlan": true,
        "governmentPlan": true
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Sale with Payment Facilitator Details {#sis-pymnt-svcs-semi-sale-pymnt-facil-details-intro}
===========================================================================================

Use this information to process a sale transaction with payment facilitator details when the app is in Local mode. This type of transaction can be used to include the required payment facilitator details as part of the sale transaction.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Sale with Payment Facilitator Details {#sis-pymnt-svcs-semi-sale-pymnt-facil-details-reqfields}
=====================================================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

Optional Fields for a Sale with Payment Facilitator Details {#sis-pymnt-svcs-semi-sale-pymnt-facil-details-optfields}
=====================================================================================================================

Use one or more of the optional merchantDetails fields to provide additional payment facilitator details.

merchantDetails.salesOrganizationId
:
Set the value to the sales organization identifier.

merchantDetails.subMerchantId
:
Set the value to the sub-merchant identifier.

merchantDetails.descriptorName
:
Set the value to the descriptor name.

REST Example: Sale with Payment Facilitator Details {#sis-pymnt-svcs-semi-sale-pymnt-facil-details-ex-rest}
===========================================================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
      "amountDetails" : {
        "amount" : "1.00",
        "currency" : "USD"
      },
      "merchantDetails": {
        "salesOrganizationId": "12345",
        "subMerchantId": "SM67890",
        "descriptorName": "ExampleMerchant"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Sale with Tax Details {#sis-pymnt-svcs-semi-sale-tax-details-intro}
===================================================================

Use this information to process a sale transaction with tax details when the app is in Local mode. This type of transaction can be used to include the required tax details as part of the sale transaction.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Sale with Tax Details {#sis-pymnt-svcs-semi-sale-tax-details-reqfields}
=============================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

Optional Fields for a Sale with Tax Details {#sis-pymnt-svcs-semi-sale-tax-details-optfields}
=============================================================================================

Use one or more of the optional taxDetails fields to provide additional tax details.

taxDetails.taxId
:
Set the value to the merchant tax identifier.

taxDetails.salesSlipNumber
:
Set the value to the sales slip number.

taxDetails.includedTaxAmount
:
Set the value to the tax amount.

taxDetails.includedLocalTaxAmount
:
Set the value to the local tax amount.

taxDetails.includedNationalTaxAmount
:
Set the value to the national tax amount.

REST Example: Sale with Tax Details {#sis-pymnt-svcs-semi-sale-tax-details-ex-rest}
===================================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
      "amountDetails" : {
        "amount" : "20.00",
        "currency" : "USD"
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

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Sale with Lodging Details {#sis-pymnt-svcs-semi-sale-lodging-intro}
===================================================================

Use this information to process a sale transaction with lodging details in Local mode. This transaction includes required lodging details as part of the sale transaction.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Sale with Lodging Details {#sis-pymnt-svcs-semi-sale-lodging-reqfields}
=============================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

Optional Fields for a Sale with Lodging Details {#sis-pymnt-svcs-semi-sale-lodging-optfields}
=============================================================================================

Use one or more of the optional fields to include additional details in the transaction.

lodgingDetails.duration
:
Set this field to the number of nights of the lodging stay.

lodgingDetails.checkInDate
:
Set this field to the check-in date in MMDDYY format.

lodgingDetails.checkOutDate
:
Set this field to the check-out date in MMDDYY format.

lodgingDetails.guestSmokingPreference
:
Set this field to Y or N to indicate the guest's smoking preference.

lodgingDetails.numberOfGuests
:
Set this field to the number of guests.

lodgingDetails.numberOfRoomsBooked
:
Set this field to the number of rooms booked.

lodgingDetails.guestName
:
Set this field to the name of the guest.

lodgingDetails.roomLocation
:
Set this field to the room location description.

lodgingDetails.roomTaxElements
:
Set this field to the applicable room tax elements.

lodgingDetails.roomBedType
:
Set this field to the type of bed in the room.

lodgingDetails.roomRateType
:
Set this field to the room rate type.

lodgingDetails.specialProgramCode
:
Set this field to the special program code.

lodgingDetails.dailyRoomRate1
:
Set this field to the daily room rate for the first rate tier.

lodgingDetails.dailyRoomRate2
:
Set this field to the daily room rate for the second rate tier.

lodgingDetails.dailyRoomRate3
:
Set this field to the daily room rate for the third rate tier.

lodgingDetails.roomNights1
:
Set this field to the number of nights at the first rate tier.

lodgingDetails.roomNights2
:
Set this field to the number of nights at the second rate tier.

lodgingDetails.roomNights3
:
Set this field to the number of nights at the third rate tier.

lodgingDetails.corporateClientCode
:
Set this field to the corporate client code.

lodgingDetails.promotionalCode
:
Set this field to the promotional code.

lodgingDetails.additionalCoupon
:
Set this field to an additional coupon code.

lodgingDetails.travelAgencyCode
:
Set this field to the travel agency code.

lodgingDetails.travelAgencyName
:
Set this field to the name of the travel agency.

lodgingDetails.customerServicePhoneNumber
:
Set this field to the customer service phone number.

lodgingDetails.tax
:
Set this field to the total tax amount.

lodgingDetails.prepaidCost
:
Set this field to the prepaid cost amount.

lodgingDetails.foodAndBeverageCost
:
Set this field to the food and beverage cost.

lodgingDetails.roomTax
:
Set this field to the room tax amount.

lodgingDetails.adjustmentAmount
:
Set this field to the adjustment amount.

lodgingDetails.phoneCost
:
Set this field to the phone cost.

lodgingDetails.restaurantCost
:
Set this field to the restaurant cost.

lodgingDetails.roomServiceCost
:
Set this field to the room service cost.

lodgingDetails.miniBarCost
:
Set this field to the mini bar cost.

lodgingDetails.laundryCost
:
Set this field to the laundry cost.

lodgingDetails.miscellaneousCost
:
Set this field to the miscellaneous cost.

lodgingDetails.giftShopCost
:
Set this field to the gift shop cost.

lodgingDetails.movieCost
:
Set this field to the movie cost.

lodgingDetails.healthClubCost
:
Set this field to the health club cost.

lodgingDetails.valetParkingCost
:
Set this field to the valet parking cost.

lodgingDetails.cashDisbursementCost
:
Set this field to the cash disbursement cost.

lodgingDetails.nonRoomCost
:
Set this field to the non-room cost.

lodgingDetails.businessCenterCost
:
Set this field to the business center cost.

lodgingDetails.loungeBarCost
:
Set this field to the lounge or bar cost.

lodgingDetails.transportationCost
:
Set this field to the transportation cost.

lodgingDetails.gratuityCost
:
Set this field to the gratuity cost.

lodgingDetails.conferenceRoomCost
:
Set this field to the conference room cost.

lodgingDetails.audioVisualCost
:
Set this field to the audio/visual equipment cost.

lodgingDetails.banquetCost
:
Set this field to the banquet cost.

lodgingDetails.internetAccessCost
:
Set this field to the internet access cost.

lodgingDetails.earlyCheckOutCost
:
Set this field to the early check-out cost.

lodgingDetails.nonRoomTax
:
Set this field to the non-room tax amount.

REST Example: Sale with Lodging Details {#sis-pymnt-svcs-semi-sale-lodging-ex-rest}
===================================================================================

Request

```
{
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
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
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

Electronic Benefits Transfer {#sis-pymnt-svcs-local-ebt-intro}
==============================================================

Public assistance programs in the United States use Electronic Benefits Transfer (EBT) payment cards to issue monthly food and cash benefits to eligible people. EBT cards function like prepaid debit cards that can be used at authorized retailers. Food benefits are issued through the Supplemental Nutrition Assistance Program (SNAP), which helps people with low incomes purchase eligible food items.  
Use this information to process EBT SNAP (food benefits) and EBT Cash transactions when the app is in Local mode.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for Electronic Benefits Transfer {#sis-pymnt-svcs-local-ebt-reqfields}
======================================================================================

type
:
Set the value to `PaymentRequest` for a sale or to `StandaloneRefundRequest` for a stand-alone credit.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

paymentMode
:
Set the value to `EBT`.

ebtDetails.category
:
Set the value to `FOOD` for EBT SNAP (food benefits) and `CASH` for EBT Cash.

Optional Fields for Electronic Benefits Transfer {#sis-pymnt-svcs-local-ebt-optfields}
======================================================================================

ebtDetails.isBalanceInquiry
:
Set the value to `true` for a balance inquiry. The transaction amount must be set to `0`.

ebtDetails.isVoucher
:
Set the value to `true` for a voucher transaction.

amountDetails.cashbackAmount
:
Set the value to the cashback amount for a cashback transaction.

REST Example: Electronic Benefits Transfer SNAP Sale {#sis-pymnt-svcs-local-ebt-ex-rest}
========================================================================================

Request

```
{
  "type": "PaymentRequest",
  "merchantReferenceCode": "82910b8b430a414dbe224e4494545b02",
  "paymentMode": "EBT",
  "amountDetails": {
    "amount": "1.00",
    "currency": "USD"
  },
  "ebtDetails": {
    "category": "FOOD"
  }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
  "type": "TransactionStatusResponse",
  "message": "Status update to display.",
  "canBeAborted": true
}
```

Response to a Successful Request

```
{
  "type": "PaymentResponse",
  "message": "Payment approved",
  "transactionDetails": {
    "id": "bd9c4ddd5bb84aafa42f16f2660f76c7",
    "merchantReferenceCode": "82910b8b430a414dbe224e4494545b02",
    "submitTimeUtc": "2025-09-29T09:04:02+0000",
    "captured": true,
    "amountDetails": {
      "currency": "USD",
      "amount": "1.00",
      "capturedAmount": "1.00",
      "refundableAmount": "1.00"
    }
  },
  "processingDetails": {
    "status": "APPROVED",
    "verificationMethod": "PIN",
    "entryMode": "MAGNETIC_STRIPE",
    "card": {
      "expirationMonth": "00",
      "expirationYear": "00",
      "type": "EBT",
      "maskedPan": "507719XXXXXX4720"
    }
  },
  "additionalInformation": {
    "requestId": "7591366618376609904603"
  },
  "linkedOperations": [],
  "tipAdjustStatus": "NOT_ADJUSTABLE",
  "receipts": {
    "merchantReceipt": {
      "preformattedReceipt": "Merchant Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n555555555\n\nPayment\n$1.00\n\nPlease retain receipt!\n\nCard: EBT\nAccount: **** **** **** 4720\nEntry Mode: Magstripe\nVerification: Verified by PIN\n\nTransaction: 673579\nAuthorization: 831000\nMerchant ID: ******************nt001\nTerminal ID: ****1459\n\n\nbd9c4ddd5bb84aafa42f16f2660f76c7\n\n2:34:22 PM: 9/29/2025\n\n\n",
      "receiptData": {
        "lines": {
          "MERCHANT_DETAILS_PUBLIC_NAME": {
            "label": "Name",
            "value": "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS": {
            "label": "Address",
            "value": "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP": {
            "label": "Zip",
            "value": "55555"
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
            "value": "555555555"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
            "label": "Additional Information",
            "value": ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
            "label": "Card",
            "value": "EBT"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT": {
            "label": "Account",
            "value": "**** **** **** 4720"
          },
          "PAYMENT_DETAILS_SOURCE": {
            "label": "Entry Mode",
            "value": "Magstripe"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
            "label": "Verification",
            "value": "Verified by PIN"
          },
          "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
            "label": "Transaction",
            "value": "673579"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE": {
            "label": "Authorization",
            "value": "831000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
            "label": "Merchant ID",
            "value": "******************nt001"
          },
          "CLEARING_DETAILS_TERMINAL_ID": {
            "label": "Terminal ID",
            "value": "****1459"
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
            "value": "bd9c4ddd5bb84aafa42f16f2660f76c7"
          },
          "AMOUNT_AND_CURRENCY": {
            "label": "Amount",
            "value": "$1.00"
          },
          "DATE": {
            "label": "Date",
            "value": "9/29/2025"
          },
          "TIME": {
            "label": "Time",
            "value": "2:34:22 PM"
          },
          "STATUS_TEXT": {
            "label": "Information",
            "value": "Please retain receipt!"
          }
        },
        "signatureLineRequired": false,
        "tipLineRequired": false,
        "totalLineRequired": false
      }
    },
    "customerReceipt": {
      "preformattedReceipt": "Cardholder Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n555555555\n\nPayment\n$1.00\n\nPlease retain receipt!\n\nCard: EBT\nAccount: **** **** **** 4720\nEntry Mode: Magstripe\nVerification: Verified by PIN\n\nTransaction: 673579\nAuthorization: 831000\nMerchant ID: ******************nt001\nTerminal ID: ****1459\n\n\nbd9c4ddd5bb84aafa42f16f2660f76c7\n\n2:34:22 PM: 9/29/2025\n\n\n",
      "receiptData": {
        "lines": {
          "MERCHANT_DETAILS_PUBLIC_NAME": {
            "label": "Name",
            "value": "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS": {
            "label": "Address",
            "value": "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP": {
            "label": "Zip",
            "value": "55555"
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
            "value": "555555555"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
            "label": "Additional Information",
            "value": ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
            "label": "Card",
            "value": "EBT"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT": {
            "label": "Account",
            "value": "**** **** **** 4720"
          },
          "PAYMENT_DETAILS_SOURCE": {
            "label": "Entry Mode",
            "value": "Magstripe"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
            "label": "Verification",
            "value": "Verified by PIN"
          },
          "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
            "label": "Transaction",
            "value": "673579"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE": {
            "label": "Authorization",
            "value": "831000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
            "label": "Merchant ID",
            "value": "******************nt001"
          },
          "CLEARING_DETAILS_TERMINAL_ID": {
            "label": "Terminal ID",
            "value": "****1459"
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
            "value": "bd9c4ddd5bb84aafa42f16f2660f76c7"
          },
          "AMOUNT_AND_CURRENCY": {
            "label": "Amount",
            "value": "$1.00"
          },
          "DATE": {
            "label": "Date",
            "value": "9/29/2025"
          },
          "TIME": {
            "label": "Time",
            "value": "2:34:22 PM"
          },
          "STATUS_TEXT": {
            "label": "Information",
            "value": "Please retain receipt!"
          }
        },
        "signatureLineRequired": false,
        "tipLineRequired": false,
        "totalLineRequired": false
      }
    }
  },
  "ebtDetails": {
    "category": "FOOD"
  }
}
```

Custom Card Read {#sis-pymnt-svcs-local-custom-card-card-intro}
===============================================================

Use this information to obtain data from custom cards such as gift cards, loyalty program cards, and employee cards when the app is in Local mode. This service cannot be used to perform payment functions.
IMPORTANT Custom Card Read is supported for non-PCI cards only. To use this service, the card type must be on your allowlist. To add a card type to your allowlist, contact your implementation manager.  
To retrieve the card data, swipe the card's magnetic stripe through the payment device. The custom card read-only function reads and returns the raw card identifier to your app or point-of-sale (POS) system. You can then use the raw data within your app or POS system.  
These are examples of how you might use the Custom Card Read feature:

* **Custom gift card:** Use the card number to check a balance or process a payment in your private gift card network.
* **Employee card:** Use the card number to look up an employee's profile or account.
  {#sis-pymnt-svcs-local-custom-card-card-intro_ul_snq_dyx_xgc}

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields to Perform a Custom Card Read {#sis-pymnt-svcs-local-custom-card-read-reqfields}
================================================================================================

type
:
Set the value to `ReadCardRequest`.

REST Example: Custom Card Read {#sis-pymnt-svcs-local-custom-card-read-ex-rest}
===============================================================================

Request

```
{
   "type" : "ReadCardRequest"
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
   "type": "OperationStatusResponse",
   "message": "Status update to display."
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

Printing a Customer or Merchant Receipt {#sis-pymnt-svcs-receipt-print-intro}
=============================================================================

Use this information to print a customer or merchant receipt from a previous transaction when the app is in Local mode. This feature can only be used with terminals that have integrated printers.

Endpoint
--------

The endpoint is the same for the test and production environments.  
**Test:** `wss://{terminal IP address:port number}/`  
**Production:** `wss://{terminal IP address:port number}/`

Required Fields to Print a Customer or Merchant Receipt {#sis-pymnt-svcs-receipt-print-reqfields}
=================================================================================================

type
:
Set the value to `PrintReceiptRequest`.

transactionId
:
Set the value to the ID field value from the original transaction.

receiptType
:
Set the value to CUSTOMER or MERCHANT.

REST Example: Print a Customer or Merchant Receipt {#sis-pymnt-svcs-receipt-print-ex-rest}
==========================================================================================

Request

```
{
    "type": "PrintReceiptRequest",
    "transactionId": "8fe5fa21d0814424bcec4997c9dc89c4",
    "receiptType": "CUSTOMER"
}
```

Mid-Operation Status Updates  
During the operation, you might receive one or more update responses indicating the current status of the operation. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "OperationStatusResponse",
      "message": "Status update to display."
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

Custom Printing {#sis-pymnt-svcs-semi-custom-print-intro}
=========================================================

Use this information to send a custom print request in Local mode. This feature enables you to print custom content directly to the integrated printer of a PAX terminal, including text, label-value pairs, images, barcodes, and QR codes.

> IMPORTANT  
> The Custom Printing feature does not affect your configuration for printing standard customer or merchant receipts.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for Custom Printing {#sis-pymnt-svcs-semi-custom-print-reqfields}
=================================================================================

type
:
Set this field to `CustomPrintRequest`.

printLayout.sections
:
Set this field to a list of one or more print sections. Each section must include a sectionType field to identify the type of custom content to print.

Required Fields for Custom Printing by Section Type {#sis-pymnt-svcs-semi-custom-print-sec-type-reqfields}
==========================================================================================================

Use these fields to define the required content for each custom print section in the printLayout.sections field. Each section in this field must include a sectionType field that identifies the type of content to print. The printLayout.sections field supports these sectionType values: `TEXT`, `SPACER`, `BARCODE`, and `IMAGE`. These values are case sensitive.

TEXT Section
------------

printLayout.sections\[n\].sectionType
:
Set this field to `TEXT`.

printLayout.sections\[n\].textContent.textType
:
Set this field to identify the type of text content. Supported values are `PARAGRAPH`, `LABEL_VALUE`, and `NO_LINE`.

TEXT Section: PARAGRAPH Text Content Required Fields
----------------------------------------------------

printLayout.sections\[n\].textContent.lines
:
Set this field to a list of one or more strings to print as paragraph lines.

TEXT Section: LABEL_VALUE Text Content Required Fields
------------------------------------------------------

printLayout.sections\[n\].textContent.content
:
Set this field to a list of one or more label-value pairs.

printLayout.sections\[n\].textContent.content\[n\].label.labelText
:
Set this field to the label text string.

printLayout.sections\[n\].textContent.content\[n\].value.valueText
:
Set this field to the value text string.

BARCODE Section
---------------

printLayout.sections\[n\].sectionType
:
Set this field to `BARCODE`.

printLayout.sections\[n\].content
:
Set this field to the data to encode in the barcode.

printLayout.sections\[n\].barcodeType
:
Set this field to the barcode format. Supported values are `CODE39`, `CODE128`, `EAN13`, `EAN128`, `PDF417`, and `QRCODE`.

IMAGE Section
-------------

printLayout.sections\[n\].sectionType
:
Set this field to `IMAGE`.

printLayout.sections\[n\].imageData
:
Set this field to a Base64-encoded image. Supported formats are `PNG`, `JPEG`, and `BMP`. The maximum image width and height is 384 pixels.

SPACER Section
--------------

printLayout.sections\[n\].sectionType
:
Set this field to `SPACER`.

Optional Fields for Custom Printing {#sis-pymnt-svcs-semi-custom-print-optfields}
=================================================================================

Use these fields to define optional content and formatting for custom print sections in the printLayout.sections field. Optional fields are supported for `TEXT` and `SPACER` sections.

> IMPORTANT  
> If you do not specify the value for an optional field, the default value is used.

TEXT Section: PARAGRAPH Optional Fields
---------------------------------------

printLayout.sections\[n\].textContent.align
:
Set this field to `LEFT`, `CENTER`, or `RIGHT`. The default value is `LEFT`.

printLayout.sections\[n\].textContent.textStyle.size
:
Set this field to `SMALL`, `MEDIUM`, or `LARGE`. The default value is `MEDIUM`.

printLayout.sections\[n\].textContent.textStyle.style
:
Set this field to `NORMAL` or `EMPHASIZE`. The default value is `NORMAL`.

TEXT Section: LABEL_VALUE Optional Fields
-----------------------------------------

printLayout.sections\[n\].textContent.content\[n\].label.textStyle.size
:
Set this field to `SMALL`, `MEDIUM`, or `LARGE`. The default value is `MEDIUM`.

printLayout.sections\[n\].textContent.content\[n\].label.textStyle.style
:
Set this field to `NORMAL` or `EMPHASIZE`. The default value is `NORMAL`.

printLayout.sections\[n\].textContent.content\[n\].value.textStyle.size
:
Set this field to `SMALL`, `MEDIUM`, or `LARGE`. The default value is `MEDIUM`.

printLayout.sections\[n\].textContent.content\[n\].value.textStyle.style
:
Set this field to `NORMAL` or `EMPHASIZE`. The default value is `NORMAL`.

SPACER Section Optional Fields
------------------------------

printLayout.sections\[n\].lines
:
Set this field to the number of blank lines to insert. The default value is `1`.

REST Example: Custom Printing {#sis-pymnt-svcs-semi-custom-print-ex-rest}
=========================================================================

Request

```
{
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
```

Mid-Transaction Status Updates  
During the operation, you might receive one or more update responses indicating the current status of the operation. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "OperationStatusResponse",
      "message": "Status update to display."
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

Custom Screens {#sis-pymnt-svcs-semi-custom-screens-intro}
==========================================================

Use this information to send a custom screen request in Local mode. This feature enables you to show one or more customized screens on the payment terminal. Custom screen can show informational text, collect text input, or capture a digital signature.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for Custom Screens {#sis-pymnt-svcs-semi-custom-screens-reqfields}
==================================================================================

type
:
Set this field to `CustomScreenRequest`.

screens
:
Set this field to a list of one or more screen objects. Each screen must include a screenType field to identify the type of custom screens to show on the payment terminal.

Required Fields for Custom Screens by Screen Type {#sis-pymnt-svcs-semi-custom-screens-type-reqfields}
======================================================================================================

Use these fields to define the required content for each custom screen in the screens field. Each screen in this field must include a screenType field that identifies the type of custom screen to show on the payment terminal. The screens field supports these screenType values: `textDisplay`, `textInput`, and `signatureCapture`.

textDisplay Screen
------------------

screens\[n\].screenType
:
Set this field to `textDisplay`.

screens\[n\].title
:
Set this field to the screen title. The title cannot exceed 20 characters.

textInput Screen
----------------

screens\[n\].screenType
:
Set this field to `textInput`.

screens\[n\].title
:
Set this field to the screen title. The title cannot exceed 20 characters.

screens\[n\].textInputs
:
Set this field to a list of one or more text input fields.

screens\[n\].textInputs\[n\].textInputLabel
:
Set this field to the label for the input field. The label cannot exceed 25 characters.

screens\[n\].textInputs\[n\].textInputConfig.textInputType
:
Set this field to the type of input to accept. Supported values are `NUMERIC`, `ALPHANUMERIC`, `EMAIL`, and `PHONE`.

signatureCapture Screen
-----------------------

screens\[n\].screenType
:
Set this field to `signatureCapture`.

screens\[n\].title
:
Set this field to the screen title. The title cannot exceed 20 characters.

Optional Fields for Custom Screens {#sis-pymnt-svcs-semi-custom-screens-optfields}
==================================================================================

Use these fields to define optional content and formatting for custom screens in the screens field. Optional fields are available for all screen types, with additional optional fields supported for textDisplay and textInput screens.

> IMPORTANT  
> If you do not specify the value for an optional field, the default value is used.

Optional Fields Available on All Screen Types
---------------------------------------------

screens\[n\].description
:
Set this field to a descriptive message displayed below the title.

screens\[n\].isSkippable
:
Set this field to `true` to allow the cardholder to skip the screen. The default value is `false`.

textDisplay Screen Optional Fields
----------------------------------

screens\[n\].toggles
:
Set this field to a list of toggle items for the cardholder to accept or decline.

screens\[n\].toggles\[n\].label
:
Set this field to the label displayed next to the toggle. The label cannot exceed 40 characters.

screens\[n\].toggles\[n\].required
:
Set this field to `true` to require the cardholder to enable the toggle before proceeding. The default value is `false`.

textInput Screen Optional Fields
--------------------------------

screens\[n\].textInputs\[n\].textInputHint
:
Set this field to placeholder hint text displayed inside the input field.

screens\[n\].textInputs\[n\].textInputConfig.masked
:
Set this field to `true` to mask the input characters as the cardholder types. The default value is `false`.

screens\[n\].textInputs\[n\].textInputConfig.length.min
:
Set this field to the minimum number of characters required. Must be greater than zero.

screens\[n\].textInputs\[n\].textInputConfig.length.max
:
Set this field to the maximum number of characters allowed. Must be greater than zero and not less than the defined minimum number of characters.

screens\[n\].textInputs\[n\].textInputConfig.patternConfig.pattern
:
Set this field to a regular expression that the input value must match.

screens\[n\].textInputs\[n\].textInputConfig.patternConfig.patternError
:
Set this field to the error message displayed when the input does not match the pattern.

screens\[n\].toggles
:
Set this field to a list of toggle items for the cardholder to accept or decline.

screens\[n\].toggles\[n\].label
:
Set this field to the label displayed next to the toggle. The label cannot exceed 40 characters.

screens\[n\].toggles\[n\].required
:
Set this field to `true` to require the cardholder to enable the toggle before proceeding. The default value is `false`.

REST Example: Custom Screens {#sis-pymnt-svcs-semi-custom-screens-ex-rest}
==========================================================================

Request

```
{
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
```

Mid-Transaction Status Updates  
During the operation, you might receive one or more update responses indicating the current status of the operation. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "OperationStatusResponse",
      "message": "Status update to display."
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

