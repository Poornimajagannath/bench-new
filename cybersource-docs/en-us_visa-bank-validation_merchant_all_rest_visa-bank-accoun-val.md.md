Visa Bank Account Validation Merchant Guide {#visa-bank-acc-val-about-guide}
============================================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This guide is written for merchants who want to implement the Visa Bank Account Validation product with the `REST API`.

Prohibited Uses
:
Merchants are prohibited from using the Visa Bank Account Validation (1) alone or in connection with other data or information, to determine a consumer's eligibility for products, services, credit, insurance, housing or employment, and/or engage in any other actions that could give rise to adverse action requirements under the US Fair Credit Reporting Act, the Equal Credit Opportunity Act, and/or other similar federal, state, or local regulations; (2) alone or in connection with other data or information, in any way that would cause Visa or `Cybersource` to be a "consumer reporting agency"; or (3) alone or in connection with other data or information, to discriminate based on race, gender, or other protected characteristics.

Conventions
:
These statements appear in this document:

    > IMPORTANT
    > An *Important* statement contains information essential to successfully completing a task or learning a concept.

    > WARNING
    > A *Warning* contains information or instructions, which, if not heeded, can result in a security risk, irreversible loss of data, or significant cost in time or revenue or both.

Related Documentation
:
Visit the [`Cybersource` documentation hub](https://developer.cybersource.com/docs.md "") to find additional technical documentation.
:

Customer Support
:
For support information about any service, visit the Support Center:

<http://support.visaacceptance.com>

Recent Revisions to This Document {#visa-bank-acc-val-doc-revisions}
====================================================================

26.06.01
--------

This revision contains only editorial changes and no technical updates.

26.05.01
--------

Validating New Accounts Using Tokens
:
Added information on how to validate accounts using transient tokens and TMS tokens. For more information, see [Validating an Account Using Transient Tokens](/docs/cybs/en-us/visa-bank-validation/merchant/all/rest/visa-bank-accoun-val/visa-bank-acc-val-process-intro-intro/visa-bank-acc-val-validate-transient-token.md "") and [Validating an Account Using TMS Tokens](/docs/cybs/en-us/visa-bank-validation/merchant/all/rest/visa-bank-accoun-val/visa-bank-acc-val-process-intro-intro/visa-bank-acc-val-validate-reg-tms-token.md "").

25.11.01
--------

Enhanced Search Information
:
Added information on how to search for account validation transactions. For more information, see[Transaction Search](/docs/cybs/en-us/visa-bank-validation/merchant/all/rest/visa-bank-accoun-val/visa-bank-acc-val-view-tranx-details-ebc/visa-bank-acc-val-tranx-search-ebc.md "") and [Transaction Details](/docs/cybs/en-us/visa-bank-validation/merchant/all/rest/visa-bank-accoun-val/visa-bank-acc-val-view-tranx-details-ebc/visa-bank-acc-val-tranx-details-ebc.md "").

Enhanced Reporting
:
Added information on how to include account validation transactions in the Transaction Request Report. For more information, see [Reporting](/docs/cybs/en-us/visa-bank-validation/merchant/all/rest/visa-bank-accoun-val/visa-bank-acc-val-reporting.md "").

Editorial Updates
:
Editorial updates were made throughout the guide.

25.06.01
--------

This revision contains only editorial changes and no technical updates.

25.05.01
--------

This revision contains only editorial changes and no technical updates.

25.04.01
--------

Initial release.

Introduction to Visa Bank Account Validation {#visa-bank-acc-val-topic-intro}
=============================================================================

`Cybersource` offers the Visa Bank Account Validation product, which helps validate your customer's routing and bank account information as a standalone service through secure REST-based API prior to generating an ACH transaction with your existing processor. This product also helps you comply with the National Automated Clearing House Association (Nacha) Web Debit Account Validation Rule for ACH web transactions.  
This product helps reduce the number of administrative returns, enhances the security and reliability of ACH transactions, and protects your business from the costly repercussions of invalid ACH transactions.  
The Visa Bank Account Validation product validates both the routing and bank account number based on the ACH history of the account. The responses on this validation will let you know whether the customer's account is validated, not validated, low risk, medium risk, or high risk for processing ACH transactions. The product validates a routing and bank account number combination using format checks and historical information based on more than 100 million accounts.

Requirements for Visa Bank Account Validation {#visa-bank-acc-val-reqs}
=======================================================================

In the US, Visa Bank Account Validation enables you to validate your customer's routing and bank account information based on their ACH history. Before you can start using it, you must meet these requirements:

* Verify that you have the capability to use the REST API.
* Contact the `Cybersource` sales team or your contracting partner to request onboarding for the Visa Bank Account Validation product.
* Generate a `REST` key P12 certificate for your merchant ID (MID) so that you can send requests. For more information, see [Generating a P12 Certificate](/docs/cybs/en-us/visa-bank-validation/merchant/all/rest/visa-bank-accoun-val/visa-bank-acc-val-config.md "").
* Enable Message-Level Encryption (MLE) so that you can send all Visa Bank Account Validation API requests, including requests submitted using tokenized data to `Cybersource`. For more information, see [Enabling Message-Level Encryption](/docs/cybs/en-us/visa-bank-validation/merchant/all/rest/visa-bank-accoun-val/visa-bank-acc-val-enable-mle.md "").
  {#visa-bank-acc-val-reqs_ul_a1g_yvv_52c}

Generating a P12 Certificate {#visa-bank-acc-val-config}
========================================================

You can use this validation product only through a REST API integration.  
You must create a `REST` key for your merchant ID. If you already have a `REST` key for other `Cybersource` `REST` services with the same merchant ID, you can use that key to access the Visa Bank Account Validation Service. Ensure that the key is a P12 certificate. For more details, see [Create a P12 Certificate](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-security-p12-intro.md "") in the *Getting Started with REST Developer Guide*.

Enabling Message-Level Encryption {#visa-bank-acc-val-enable-mle}
=================================================================

You must enable Message-Level Encryption (MLE) to send Visa Bank Account Validation API requests to `Cybersource`. For more information, see [Enable Message-Level Encryption](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-mle-intro.md "") in the *Getting Started with REST Developer Guide*.

Validating a Bank Account {#visa-bank-acc-val-process-intro-intro}
==================================================================

Visa Bank Account Validation supports multiple invocation methods as explained in the following sub-sections.

> IMPORTANT  
> Each request can validate either the routing and bank account number combination or one of the types of token can be validated. You cannot combine multiple tokens or routing/bank account information in a single request.

Validate an Account Using Routing and Account Numbers {#visa-bank-acc-val-process-intro}
========================================================================================

This section describes how to validate using direct routing and bank account details submitted through the REST API. Follow these steps to request a bank account validation:

1. Create a request with the required and any optional REST API fields. Refer to the request and response examples, if needed.
2. Send the completed request to one of these endpoints:
   * **Production:** `POST ``api.cybersource.com``/bavs/v1/account-validations`
   * **Test:** `POST ``apitest.cybersource.com``/bavs/v1/account-validations`
     {#visa-bank-acc-val-process-intro_ul_c3w_2jw_52c}
3. Verify the response messages to make sure that the request succeeded. For more information, see the [Transaction response codes](https://developer.cybersource.com/api/reference/response-codes.md "").
   {#visa-bank-acc-val-process-intro_ol_b3w_2jw_52c}

Required Fields for Validating an Account Using Routing and Account Numbers {#visa-bank-acc-val-req-fields}
===========================================================================================================

[processingInformation.validationLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-val-lev.md "")
:
Set the value to `1`.

[paymentInformation.bank.routingNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-bank-routing-number.md "")
:
Set the value to the routing number for your customer's bank. This field accepts a non‑negative string containing only digits.

[paymentInformation.bank.account.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-bank-account-num.md "")
:
Set the value to the bank account number for your customer's bank account. This field accepts a non‑negative string containing only digits and must be exactly nine-digits long.

Optional Fields for Validating an Account {#visa-bank-acc-val-optional-fields}
==============================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:
Set the value to any reference code that you choose to associate with the validation request. This code is returned in the response exactly as provided.

REST Example: Validating an Account Using Routing and Account Numbers {#visa-bank-acc-val-ex-rest}
==================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "processingInformation": {
        "validationLevel": 1
            },
    "paymentInformation": {
        "bank": {
            "routingNumber": "041210163",
            "account": {
                "number": "1234567"
            }
        }
    }
}
```

Response to a Successful Request

```
{
    "clientReferenceInformation": {
       "code": "TC50171_3"
    },
    "requestId": "string",
    "submitTimeUtc": "string",
    "bankAccountValidation": {
        "rawValidationCode": 0,
        "resultCode": 0,
        "resultMessage": "string"
    }
}
```

Response to an Unsuccessful Request

```
{
    "submitTimeUtc": "string",
    "status": "string",
    "message": "string",
    "reason": "string",
    "details": [
        {
            "field": "string",
            "reason": "string"
        }
    ]
}
```

Validating an Account Using Transient Tokens {#concept_nt2_ymx_z3c}
===================================================================

Transient tokens are one-time, short-lived tokens, Merchants can use them for validations without having to transmit raw routing and account number data in the API request call. This option is intended for session-based validations, such as initial account verification or checkout flows. There are several types of transient tokens that can be used when validating routing and bank account information.  
All transient token-based account validation requests must be submitted using REST APIs secured with mandatory Message‑Level Encryption (MLE).  
The validation response returned for transient token requests is the same as for other Visa Bank Account Validation request types.

Validating an Account Using a Transient Token: JSON Web Token (JWT) {#visa-bank-acc-val-validate-transient-token-jwt}
=====================================================================================================================

This section describes how to validate using a JWT type of transient token submitted through the REST API. Follow these steps to request a bank account validation:

1. Create a request with the required and any optional REST API fields. Refer to the request and response examples, if needed.
2. Send the completed request to one of these endpoints:
   * **Production:** `POST ``api.cybersource.com``/bavs/v1/account-validations`
   * **Test:** `POST ``apitest.cybersource.com``/bavs/v1/account-validations`
     {#visa-bank-acc-val-validate-transient-token-jwt_ul_c3w_2jw_52c}
3. Verify the response messages to make sure that the request succeeded. For more information, see the [Transaction response codes](https://developer.cybersource.com/api/reference/response-codes.md "").
   {#visa-bank-acc-val-validate-transient-token-jwt_ol_b3w_2jw_52c}

Required Fields for Validating an Account Using a JSON Web Token {#visa-bank-acc-val-req-fields-transient-token-jwt}
====================================================================================================================

[processingInformation.validationLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-val-lev.md "")
:
Set the value to `1`.

[tokenInformation.transientTokenJwt](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-transient-token-jwt.md "")
:
The transient token encoded as JWT.

Optional Fields for Validating an Account {#visa-bank-acc-val-optional-conref}
==============================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:
Set the value to any reference code that you choose to associate with the validation request. This code is returned in the response exactly as provided.

REST Example: Validating an Account Using a JSON Web Token {#visa-bank-acc-val-jwt-ex-rest}
===========================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
     "processingInformation": {
        "validationLevel": 1
        },
    "tokenInformation": {
        "transientTokenJwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE3NzA2NTY5OTYsImV4cCI6MTgwMjE5Mjk5NiwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSIsIkdpdmVuTmFtZSI6IkpvaG5ueSIsIlN1cm5hbWUiOiJSb2NrZXQiLCJFbWFpbCI6Impyb2NrZXRAZXhhbXBsZS5jb20iLCJSb2xlIjpbIk1hbmFnZXIiLCJQcm9qZWN0IEFkbWluaXN0cmF0b3IiXSwianRpIjoiMUQ0TENTOE5SME5LVUJLMzFZRzNBN1oyQjFZQ0ZVM0tDSjgxSlRRTThXVFNBSDI1SkdBRDY5OEEyRkQ2MzcyRCJ9.0cWjVLp1yacVm8ozW4yn2-LQklnQU7Ws44lvr16mpdI"
    }
}
```

Response to a Successful Request

```
{ 
    "clientReferenceInformation": { 
        "code": "TC50171_3" 
    }, 
    "requestId": "string", 
    "submitTimeUtc": "string", 
    "bankAccountValidation": { 
        "rawValidationCode": integer, 
        "resultCode": integer, 
        "resultMessage": "string" 
    } 
} 
```

Validating an Account Using a Transient Token: JSON Token ID {#visa-bank-acc-val-validate-transient-token-json}
===============================================================================================================

This section describes how to validate using a JSON token ID type of transient token submitted through the REST API. Follow these steps to request a bank account validation:

1. Create a request with the required and any optional REST API fields. Refer to the request and response examples, if needed.
2. Send the completed request to one of these endpoints:
   * **Production:** `POST ``api.cybersource.com``/bavs/v1/account-validations`
   * **Test:** `POST ``apitest.cybersource.com``/bavs/v1/account-validations`
     {#visa-bank-acc-val-validate-transient-token-json_ul_c3w_2jw_52c}
3. Verify the response messages to make sure that the request succeeded. For more information, see the [Transaction response codes](https://developer.cybersource.com/api/reference/response-codes.md "").
   {#visa-bank-acc-val-validate-transient-token-json_ol_b3w_2jw_52c}

Required Fields for Validating an Account Using a JSON Token ID {#visa-bank-acc-val-req-fields-transient-token-json}
====================================================================================================================

[processingInformation.validationLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-val-lev.md "")
:
Set the value to `1`.

[tokenInformation.jti](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-jti.md "")
:
The value is the TMS transient token ID. A 64-hexadecimal character identifier representing capture payment credentials.

Optional Fields for Validating an Account {#visa-bank-acc-val-optional-conref}
==============================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:
Set the value to any reference code that you choose to associate with the validation request. This code is returned in the response exactly as provided.

REST Example: Validating an Account Using a JSON Token ID {#visa-bank-acc-val-json-ex-rest}
===========================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "processingInformation": {
        "validationLevel": 1
    },
    "tokenInformation": {
        "jti": "1D4LCS8NR0NKUBK31YG3A7Z2B1YCFU3KCJ81JTQM8WTSAH25JGAD698A2FD6372D"
    }
}
```

Response to a Successful Request

```
{ 
    "clientReferenceInformation": { 
        "code": "TC50171_3" 
    }, 
    "requestId": "string", 
    "submitTimeUtc": "string", 
    "bankAccountValidation": { 
        "rawValidationCode": integer, 
        "resultCode": integer, 
        "resultMessage": "string" 
    } 
} 
```

Validating an Account Using Regular TMS Tokens {#visa-bank-acc-val-validate-reg-tms-token}
==========================================================================================

Several types of regular Transaction Management Systems (TMS) tokens can be used to validate routing and bank account information:

* Customer Identifier
* Instrument Identifier
* Payment Instrument Identifier
  {#visa-bank-acc-val-validate-reg-tms-token_ul_dsx_sny_z3c}

Validating an Account Using a TMS Token: Customer Identifier {#visa-bank-acc-val-validate-reg-tms-customer-ident-intro}
=======================================================================================================================

A customer identifier is a type of token created by the Token Management Systems (TMS) to retrieve customer-associated data. It can be used to validate a customer's routing and bank account information.  
This section describes how to validate using a customer identifier type of TMS token submitted through the REST API. Follow these steps to request a bank account validation:

1. Create a request with the required and any optional REST API fields. Refer to the request and response examples, if needed.
2. Send the completed request to one of these endpoints:
   * **Production:** `POST ``api.cybersource.com``/bavs/v1/account-validations`
   * **Test:** `POST ``apitest.cybersource.com``/bavs/v1/account-validations`
     {#visa-bank-acc-val-validate-reg-tms-customer-ident-intro_ul_c3w_2jw_52c}
3. Verify the response messages to make sure that the request succeeded. For more information, see the [Transaction response codes](https://developer.cybersource.com/api/reference/response-codes.md "").
   {#visa-bank-acc-val-validate-reg-tms-customer-ident-intro_ol_b3w_2jw_52c}

Required Fields for Validating an Account Using a Customer Identifier {#visa-bank-acc-val-req-fields-tms-customer-ident}
========================================================================================================================

[processingInformation.validationLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-val-lev.md "")
:
Set the value to `1`.

[paymentInformation.customer.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-customer-id.md "")
:
The unique identifier for the Customer token. This value is a non-negative string with 12-32 characters.

Optional Fields for Validating an Account {#visa-bank-acc-val-optional-conref}
==============================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:
Set the value to any reference code that you choose to associate with the validation request. This code is returned in the response exactly as provided.

REST Example: Validating an Account Using a Customer Identifier {#visa-bank-acc-val-tms-customer-ident-ex-rest}
===============================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "processingInformation": {
        "validationLevel": 1
        },
    "paymentInformation": {
        "customer": {
            "id": "4A1B5976688BAD2EE0633F36CF0A054E"
        }
    }
}
```

Response to a Successful Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "requestId": "string",
    "submitTimeUtc": "string",
    "bankAccountValidation": {
        "rawValidationCode": integer,
        "resultCode": integer,
        "resultMessage": "string"
    }
}
```

Validating an Account Using a TMS Token: Instrument Identifier {#visa-bank-acct-val-validate-reg-tms-instrument-ident-intro}
============================================================================================================================

An instrument identifier is a type of token created by Token Management Systems (TMS) to identify the bank or payment account to use for payment. It can be used to validate a customer's routing and bank account information.  
This section describes how to validate using an instrument identifier type of TMS token submitted through the REST API. Follow these steps to request a bank account validation:

1. Create a request with the required and any optional REST API fields. Refer to the request and response examples, if needed.
2. Send the completed request to one of these endpoints:
   * **Production:** `POST ``api.cybersource.com``/bavs/v1/account-validations`
   * **Test:** `POST ``apitest.cybersource.com``/bavs/v1/account-validations`
     {#visa-bank-acct-val-validate-reg-tms-instrument-ident-intro_ul_c3w_2jw_52c}
3. Verify the response messages to make sure that the request succeeded. For more information, see the [Transaction response codes](https://developer.cybersource.com/api/reference/response-codes.md "").
   {#visa-bank-acct-val-validate-reg-tms-instrument-ident-intro_ol_b3w_2jw_52c}

Required Fields for Validating an Account Using an Instrument Identifier {#visa-bank-acc-val-req-fields-tms-instrument-ident}
=============================================================================================================================

[processingInformation.validationLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-val-lev.md "")
:
Set the value to `1`.

[paymentInformation.instrumentIdentifier.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-instrument-identifier-id.md "")
:
The unique identifier for the Instrument Identifier token. This value is a non-negative string with 12-32 characters.

Optional Fields for Validating an Account {#visa-bank-acc-val-optional-conref}
==============================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:
Set the value to any reference code that you choose to associate with the validation request. This code is returned in the response exactly as provided.

REST Example: Validating an Account Using an Instrument Identifier {#visa-bank-acc-val-tms-instrument-ident-ex-rest}
====================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "processingInformation": {
        "validationLevel": 1
    },
    "paymentInformation": {
        "instrumentIdentifier": {
            "id": "4A1A21D4431F45A4E0633F36CF0A2293"
        }
    }
}
```

Response to a Successful Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "requestId": "string",
    "submitTimeUtc": "string",
    "bankAccountValidation": {
        "rawValidationCode": integer,
        "resultCode": integer,
        "resultMessage": "string"
    }
}
```

Validating an Account Using a TMS Token: Payment Instrument Identifier {#visa-bank-acc-val-validate-reg-tms-payment-instrument-ident-intro}
===========================================================================================================================================

A payment instrument identifier is a type of token created by Token Management Systems (TMS) that refers to specific payment account information. It can be used to validate a customer's routing and bank account information.  
This section describes how to validate using a payment instrument identifier type of TMS token submitted through the REST API. Follow these steps to request a bank account validation:

1. Create a request with the required and any optional REST API fields. Refer to the request and response examples, if needed.
2. Send the completed request to one of these endpoints:
   * **Production:** `POST ``api.cybersource.com``/bavs/v1/account-validations`
   * **Test:** `POST ``apitest.cybersource.com``/bavs/v1/account-validations`
     {#visa-bank-acc-val-validate-reg-tms-payment-instrument-ident-intro_ul_c3w_2jw_52c}
3. Verify the response messages to make sure that the request succeeded. For more information, see the [Transaction response codes](https://developer.cybersource.com/api/reference/response-codes.md "").
   {#visa-bank-acc-val-validate-reg-tms-payment-instrument-ident-intro_ol_b3w_2jw_52c}

Required Fields for Validating an Account Using a Payment Instrument Identifier {#visa-bank-acc-val-req-fields-tms-payment-instrument-ident}
============================================================================================================================================

[processingInformation.validationLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-val-lev.md "")
:
Set the value to `1`.

[paymentInformation.paymentInstrument.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-instrument-id.md "")
:
The unique identifier for the Payment Instrument token. This value is a non-negative string with 12-32 characters.

Optional Fields for Validating an Account {#visa-bank-acc-val-optional-conref}
==============================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:
Set the value to any reference code that you choose to associate with the validation request. This code is returned in the response exactly as provided.

REST Example: Validating an Account Using a Payment Instrument Identifier {#visa-bank-acc-val-tms-payment-instrument-ident-ex-rest}
===================================================================================================================================

Request

```
{ 
    "clientReferenceInformation": { 
        "code": "TC50171_3" 
    }, 
    "processingInformation": { 
        "validationLevel": 1 
    }, 
    "paymentInformation": { 
        "paymentInstrument": { 
            "id": "4A1A57E9AF81861BE0633F36CF0A5937" 
        } 
    } 
}
```

Response to a Successful Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "requestId": "string",
    "submitTimeUtc": "string",
    "bankAccountValidation": {
        "rawValidationCode": integer,
        "resultCode": integer,
        "resultMessage": "string"
    }
}
```

Response to a Successful Request {#visa-bank-acc-val-resp-fields-exp}
=====================================================================

These fields appear in a successful response. These fields track and reference your validation requests:

* clientReferenceInformation.code: This field appears when you include it in the request. It holds any reference code you want to associate with the specific validation request. The code returns in the response exactly as you provide it.
* requestID: This unique ID identifies the validation request and can be used for future reference. You can use this request ID to search for the validation request in the Transaction Search module.
* submitTimeUtc: This field records the timestamp of the validation request.
* bankAccountValidation: This section contains three different fields: rawValidationCode, resultCode, and resultMessage. Refer to the [Result Message Explanation](/docs/cybs/en-us/visa-bank-validation/merchant/all/rest/visa-bank-accoun-val/visa-bank-acc-val-resp-fields-exp/visa-bank-acc-val-suc-response-codes.md#visa-bank-acc-val-suc-response-codes_table_okx_nkv_52c "") table to understand the possible codes.
  {#visa-bank-acc-val-resp-fields-exp_ul_tmp_xcn_w2c}

API Response Codes for a Successful Request {#visa-bank-acc-val-suc-response-codes}
===================================================================================

You can receive these response code values from **rawValidationCode** , **resultCode** , and **resultMessage**:

| Raw Validation Code | Result Code | Result Message                            |
|:--------------------|:------------|:------------------------------------------|
| `12`                | `00`        | Validated                                 |
| `13`                | `00`        | Low risk                                  |
| `14`                | `00`        | Medium risk                               |
| `15`                | `04`        | High risk                                 |
| `16`                | `04`        | Not validated                             |
| `-1`                | `98`        | Unable to validate; no information found. |
| `-2`                | `99`        | Service unavailable.                      |
[Values Returned for Successful Responses]

| Result Code   | Explanation                                                                                                      |
|:--------------|:-----------------------------------------------------------------------------------------------------------------|
| Validated     | Account is in good standing.                                                                                     |
| Low risk      | Some positive data is available for the account, and no negative information was found.                          |
| Medium risk   | New account for which there is no negative information.                                                          |
| High risk     | One or more information points indicate that there is an extremely low probability of payment from this account. |
| Not validated | Account closing or closed based on their ACH history.                                                            |
[Result Message Explanation]

| Result Code | Explanation                                                                         |
|:------------|:------------------------------------------------------------------------------------|
| `00`        | Validated and can be used for ACH transactions.                                     |
| `04`        | Should not be used for ACH transaction as there is a higher probability for return. |
| `98`        | Unable to validate; no information found.                                           |
| `99`        | Service unavailable.                                                                |
[Result Code Explanation]

Response to an Unsuccessful Request {#visa-bank-acc-val-uns-resp-fields-exp}
============================================================================

It is important to understand the fields that are contained in a response to an unsuccessful request. These fields provide information that identify and resolve unsuccessful requests.  
The response to an unsuccessful request contains these fields:

* v-c-correlationid: The response header includes a unique identifier for this validation request.
* submitTimeUtc: The timestamp of the validation request. The format is `YYYY-MM-DDThhmmssZ`.
* message: The detailed message related to the status and reason for the response.

For more information about response codes, see [Transaction response codes](https://developer.cybersource.com/api/reference/response-codes.md "").

HTTP Status Codes for an Unsuccessful Request {#visa-bank-acc-val-unsuc-response-codes}
=======================================================================================

These are the possible values you can receive for a status, reason, and details block depending on the HTTP status code:

| HTTP Status Code (part of HTTP header) | Status            | Reason                                                                  | Details (an array with 0 to many blocks)                                                                 |
|:---------------------------------------|:------------------|:------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| `400`                                  | INVALID_ REQUEST  | INVALID_REQUEST                                                         | Field contains the name of the field that is missing or incorrect: Reason -- MISSING_FIELD, INVALID_DATA |
| `403`                                  | UNAUTHORIZED      | UNAUTHORIZED                                                            | ---                                                                                                      |
| `404`                                  | NOT_FOUND         | NOT_FOUND                                                               | ---                                                                                                      |
| `422`                                  | VALIDATION_ ERROR | PRODUCT_INACTIVE INVALID_MERCHANT_ CONFIGURATION PRODUCT_NOT_CONFIGURED | ---                                                                                                      |
| `502`                                  | SERVER_ERROR      | SYSTEM_ERROR SERVER_TIMEOUT SERVICE_TIMEOUT                             | ---                                                                                                      |
[HTTP Status Codes]

Viewing a Transaction in `Business Center` {#visa-bank-acc-val-view-tranx-details-ebc}
======================================================================================

You can search for transaction validations in the `Business Center` using the request ID or by using the REST API.  
The details of a bank account validation transaction are available in the `Business Center`. From the Transaction Management module, you can view and examine in detail any of the transactions you process.

Transaction Search {#visa-bank-acc-val-tranx-search-ebc}
========================================================

You can use the Transactions page in the `Business Center` to search for transactions processed by your account or the account of one or more of your merchants in your portfolio. The Transactions page displays details for each transaction matching your search criteria. Use the search toolbar to limit the results and apply filters to refine which transactions are returned. Your search can include up to 13 months of transactions.  
Follow these steps to search your transactions:

1. In the left navigation panel, choose the Transaction Management \&gt; Transactions.
2. In the search toolbar, click the Date Range filter and choose an option.
3. Click Add filter. A New Filter drop-down menu appears.
4. Click the down arrow to view a list of filter options. Browse the list or start typing `application` in the filter field.
5. Click Application to create an Application filter.
6. In the Application filter field, start typing `bank` and click Bank Account Validation when it appears. (You can save this filter for future searches by clicking the arrow in the Actions field and choosing Save New.)
7. Click Search. The result of the search appears in the Search Results section.

{#visa-bank-acc-val-tranx-search-ebc_ol_pd3_pxm_hhc}

#### Figure: {#visa-bank-acc-val-tranx-search-ebc_fig_zlb_k4v_3hc}

Bank Account Validation filter ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/visa-bank-account-val/images/bank-acc-valid-tranx-search-filter.png/jcr:content/renditions/original)

Transaction Details {#visa-bank-acc-val-tranx-details-ebc}
==========================================================

On the Transaction Details page, you can view information about bank account validation, but the page must be configured to display the details. You must add a card to the page as a place for the bank account validation details to appear.
1. In the left navigation panel, choose the Transaction Management \&gt; Transactions.
2. In the search toolbar, use the filters to list the bank account validations. For information about creating a bank account validation filter, see [Bank Account Validation filter](/docs/cybs/en-us/visa-bank-validation/merchant/all/rest/visa-bank-accoun-val/visa-bank-acc-val-view-tranx-details-ebc/visa-bank-acc-val-tranx-search-ebc.md "").
3. Click the request ID of one of the listed transactions to display the Transaction Details page for that transaction.
4. Click the Actions drop-down menu at the top of the page and choose Edit Layout \&gt; Add Card \&gt; Bank Account Validation. A Bank Account Validation Service card appears on the Transaction Details page.

#### Figure: {#visa-bank-acc-val-tranx-details-ebc_fig_dby_1wv_3hc}

Transaction Details Page Showing Bank Account Validation Card ![Transaction Details page showing Bank Account Validation card](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/visa-bank-account-val/images/bank-acc-valid-tranx-details.png/jcr:content/renditions/original)  
IMPORTANT For transaction details, the Bank Account Validation card is created only once. After you create and save the card, the Transaction Management module saves your preference and provides it for future transactions.

Testing Data {#visa-bank-acc-val-reference-test}
================================================

You can use the data below to test each validation result in the sandbox environment.  
**Test endpoint** : `POST ``apitest.cybersource.com``/bavs/v1/account-validations`

| Routing Number | Account Number | Raw Validation Code | Result Code |
|:---------------|:---------------|:--------------------|:------------|
| 111000614      | 99970          | `12`                | `00`        |
| 111000614      | 99971          | `13`                | `00`        |
| 111000614      | 99973          | `14`                | `00`        |
| 111000614      | 99915          | `15`                | `04`        |
| 111000614      | 99941          | `16`                | `04`        |
| 111000614      | 99950          | `-1`                | `98`        |
| 111000614      | 99980          | `-2`                | `99`        |
| 011401533      | 99970          | `12`                | `00`        |
[Validation Mode Examples]

Reporting {#visa-bank-acc-val-reporting}
========================================

The Account Validation requests are available in the Transaction Request Report (TRR) standard report. For more information about the TRR, see the [*Reporting User Guide*](https://developer.cybersource.com/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Reports_Available_in_the_Business_Center/c_Transaction_Request.md "").  
To help merchants view validation responses for transactions, four new fields are available in the TRR report:

* RawValidationCode
* ResultCode
* ValidationLevel
* ValidationMessage
  {#visa-bank-acc-val-reporting_ul_jds_sbn_hhc}

