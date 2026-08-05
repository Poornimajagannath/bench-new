Account Funding Transactions Developer Guide {#payouts-aft-about-guide}
=======================================================================

This section provides you with information about the `REST API` guide for `Visa Platform Connect`.

Audience and Purpose
--------------------

This document is written for developers who want to use the `Cybersource` `REST API` to integrate `Cybersource` Account Funding Transaction services into their transaction management system.

Conventions
-----------

This special statement is used in this document:

> IMPORTANT
> An *Important* statement contains information essential to successfully completing a task or learning a concept.

Related Documentation
---------------------

For further technical documentation, visit the `Cybersource` Technical Documentation Portal:  
[https://docs.cybersource.com/en/index.html](https://docs.cybersource.com/en/index.md "")

Customer Support
----------------

For support information about any service, visit the Support Center:  
<http://support.visaacceptance.com>

Recent Revisions to This Document {#aft-dev-doc-revs}
=====================================================

24.02
-----

Added new fields to the list of required fields.

24.01
-----

Initial release.

VISA Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Visa Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Visa/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER VISA NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE VISA PLATFORM CONNECT ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER VISA NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT VISA PLATFORM CONNECT ACQUIRER.

AFT Transactions {#payouts-services-intro}
==========================================

The Account Funding Transaction (AFT) allows the transfer of funds between a payment card and another account, including payment cards. When used independently, an AFT can only be used to transfer funds between accounts owned by the same individual or business entity. An AFT is not intended for the payment of goods and services, funding a merchant account, or for debt repayment.

Dual Message Account Funding Transactions (AFTs) {#payouts-services-auth-dual-message-aft-intro}
================================================================================================

Account Funding Transactions allow a payment service provider to debit funds from a cardholder's Mastercard or Visa account to fund a non-merchant account. This is typically used to load funds onto prepaid cards and electronic wallets.  
Dual Message Account Funding Transactions (AFTs) provide the following benefits:

* Enables customers to identify Mastercard and Visa transactions during the authorization and settlement.
* Allows acquiring partners to use Dual Message BINs when performing a payout transaction.

> IMPORTANT
> You must receive prior approval from ` Visa Platform Connect ` before using the AFT services. Contact ` Visa Platform Connect ` to register in the AFT program.

Endpoint {#payouts-services-auth-dual-message-aft-intro_d7e16}
--------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-intro_d7e35}

Required Fields for a Dual-Message AFT Request {#payouts-services-auth-dual-message-aft-reqfields}
==================================================================================================

These fields are required to process a dual-message AFT request:

[acquirerInformation.merchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-merchant-id.md "")
:

[aggregatorInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-name.md "")
:

captureOptions.dateToCapture
:

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

:

[merchantInformation.merchantDescriptor.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-admin-area.md "")
:

[merchantInformation.merchantDescriptor.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-locality.md "")
:

[merchantInformation.merchantDescriptor.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[merchantInformation.merchantDescriptor.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-postalcode.md "")
:

[merchantInformation.vatRegistrationNumber](https://developer.cybersource.com/docs/ctv/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[orderInformation.amountDetails.anticipatedAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-anticipated-amount.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.surcharge.amount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-surcharge-amount.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.securityCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-security-code-a.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[processingInformation.authorizationOptions.aftIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-aft-ind.md "")
:

[processingInformation.authorizationOptions.initiator.storedCredentialUsed](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")
:

[processingInformation.authorizationOptions.initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:

[processingInformation.businessApplicationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-business-appl-id.md "")

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:

[processingInformation.fundingOptions.initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-funding-ops-initiator-type.md "")
:

[processingInformation.purposeOfPayment](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purpose-of-payment.md "")
:

[recipientInformation.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address1.md "")
:

[recipientInformation.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-country.md "")
:

[recipientInformation.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-first-name.md "")
:

[recipientInformation.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-last-name.md "")
:

[senderInformation.account.fundsSource](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-funds-source.md "")
:

[senderInformation.account.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-num.md "")
:

[senderInformation.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-address1.md "")
:

[senderInformation.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-administrative-area.md "")
:

[senderInformation.countryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-country-code.md "")
:

[senderInformation.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-first-name.md "")
:

[senderInformation.identificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-identification-num.md "")
:

[senderInformation.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-last-name.md "")
:

[senderInformation.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-locality.md "")
:

[senderInformation.middleName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-middle-name.md "")
:

[senderInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-name.md "")
:

[senderInformation.personalIdType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-personal-id-type.md "")
:

[senderInformation.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-phone-number.md "")
:

[senderInformation.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-postal-code.md "")
:

[senderInformation.referenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-reference-number.md "")
:

[senderInformation.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-type.md "")
:
{#payouts-services-auth-dual-message-aft-reqfields_dl_wyl_mhh_2cc}

Related Information
-------------------

* [REST API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Dual-Message AFT {#payouts-services-auth-dual-message-aft-ex-rest}
================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "processingInformation": {
        "businessApplicationId": "AA",
        "commerceIndicator": "internet",
        "authorizationOptions": {
            "initiator": {
                "type": "customer",
                "storedCredentialUsed": "false"
            },
            "aftIndicator": "true",
            "fundingOptions": {
                "initiator": {
                    "type": "S"
                }
            }
        },
        "purposeOfPayment": "16"
    },
    "paymentInformation": {
        "card": {
            "number": "4111111111111111",
            "expirationMonth": "12",
            "expirationYear": "2031",
            "type": "001",
            "securityCode": "123"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100",
            "currency": "USD",
            "anticipatedAmount": "123.45",
            "surcharge": {
                "amount": "5"
            }
        },
        "billTo": {
            "firstName": "John",
            "lastName": "Doe",
            "address1": "1 Market St",
            "locality": "san francisco",
            "administrativeArea": "CA",
            "postalCode": "94105",
            "country": "US",
            "email": "test@cybs.com",
            "phoneNumber": "4158880000"
        }
    },
    "acquirerInformation": {
        "merchantId": "pa_ctv_sg101"
    },
    "aggregatorInformation.name": "test",
    "recipientInformation": {
        "accountId": "987654321",
        "accountType": "99",
        "address1": "Alpine Eco Road",
        "firstName": "recFirstname",
        "lastName": "resLastname",
        "locality": "recipient_city",
        "country": "GBR",
        "postalCode": "571216",
        "streetName": "Alpine eco road",
        "senderInformation": {
            "account": {
                "number": "154264765376576126571652675176",
                "fundsSource": "02"
            },
            "firstName": "senderfirstname",
            "lastName": "senderLastname",
            "postalCode": "654321",
            "phoneNumber": "01234567892",
            "address1": "Colorful street 123",
            "locality": "Rotterdam",
            "countryCode": "GBR",
            "identificationNumber": "12345678910111213223",
            "personalIdType": "TXIN",
            "administrativeArea": "KA",
            "type": "B",
            "name": "Thomas Smith",
            "referenceNumber": "15426476537657"
        },
        "merchantInformation": {
            "vatRegistrationNumber": "15426476537657",
            "merchantDescriptor": {
                "name": "utf8_merchant_descriptor",
                "locality": "Mountain View",
                "postalCode": "94044",
                "administrativeArea": "CA"
            }
        },
        "captureOptions": {
            "dateToCapture": "1231"
        }
    }
}
```

Response

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/7322307726266013203955/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7322307726266013203955"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/7322307726266013203955/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "id": "7322307726266013203955",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "100.00",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "001"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "type": "001"
    },
    "card": {
      "type": "001"
    }
  },
  "processorInformation": {
    "systemTraceAuditNumber": "992005",
    "approvalCode": "831000",
    "cardVerification": {
      "resultCodeRaw": "M",
      "resultCode": "M"
    },
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "432623992005",
    "consumerAuthenticationResponse": {
      "code": "2",
      "codeRaw": "2"
    },
    "transactionId": "016153570198200",
    "responseCode": "00",
    "avs": {
      "code": "Y",
      "codeRaw": "Y"
    }
  },
  "reconciliationId": "7322307726266013203955",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2024-11-21T23:12:52Z"
}
```

Dual Message Account Funding Transactions (AFTs) with Visa Secure {#payouts-services-auth-dual-message-aft-vs-intro}
====================================================================================================================

Account Funding Transactions allow a payment service provider to debit funds from a cardholder's Mastercard or Visa account to fund a non-merchant account. This is typically used to load funds onto prepaid cards and electronic wallets.  
Dual Message Account Funding Transactions (AFTs) provide the following benefits:

* Enables customers to identify Mastercard and Visa transactions during the authorization and settlement.
* Allows acquiring partners to use Dual Message BINs when performing a payout transaction.
* Enables users to safely validate their identity and safely store their personal identity.

Endpoint {#payouts-services-auth-dual-message-aft-vs-intro_d7e16}
-----------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-vs-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-vs-intro_d7e35}

Required Fields for a Dual-Message AFT with Visa Secure Request {#payouts-services-auth-aft-vs-reqfields}
=========================================================================================================

These fields are required to process a dual-message AFT with Visa Secure request:

[acquirerInformation.merchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-merchant-id.md "")
:

[aggregatorInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-name.md "")
:

captureOptions.dateToCapture
:

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation.cavv](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-cavv-a.md "")
:

[consumerAuthenticationInformation.xid](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-xid.md "")
:
This field is only required when you have received an XID value in a previous transaction.

[merchantInformation.merchantDescriptor.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-admin-area.md "")
:

[merchantInformation.merchantDescriptor.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-locality.md "")
:

[merchantInformation.merchantDescriptor.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[merchantInformation.merchantDescriptor.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-postalcode.md "")
:

[merchantInformation.vatRegistrationNumber](https://developer.cybersource.com/docs/ctv/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[orderInformation.amountDetails.anticipatedAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-anticipated-amount.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.surcharge.amount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-surcharge-amount.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.securityCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-security-code-a.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[processingInformation.authorizationOptions.aftIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-aft-ind.md "")
:

[processingInformation.authorizationOptions.initiator.storedCredentialUsed](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")
:

[processingInformation.authorizationOptions.initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:

[processingInformation.businessApplicationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-business-appl-id.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:

[processingInformation.fundingOptions.initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-funding-ops-initiator-type.md "")
:

[processingInformation.purposeOfPayment](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purpose-of-payment.md "")
:

[recipientInformation.accountId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-id.md "")
:

[recipientInformation.accountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-type.md "")
:

[recipientInformation.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address1.md "")
:

[recipientInformation.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address2.md "")
:

[recipientInformation.buildingNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-building-num.md "")
:

[recipientInformation.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-country.md "")
:

[recipientInformation.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-first-name.md "")
:

[recipientInformation.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-last-name.md "")
:

[recipientInformation.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-locality.md "")
:

[recipientInformation.middleName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-middle-name.md "")
:

[recipientInformation.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-postal-code.md "")
:

[recipientInformation.streetName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-street-name.md "")
:

[senderInformation.account.fundsSource](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-funds-source.md "")
:

[senderInformation.account.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-number.md "")
:

[senderInformation.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-address1.md "")
:

[senderInformation.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-administrative-area.md "")
:

[senderInformation.countryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-country-code.md "")
:

[senderInformation.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-first-name.md "")
:

[senderInformation.identificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-identification-num.md "")
:

[senderInformation.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-last-name.md "")
:

[senderInformation.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-locality.md "")
:

[senderInformation.middleName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-middle-name.md "")
:

[senderInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-name.md "")
:

[senderInformation.personalIdType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-personal-id-type.md "")
:

[senderInformation.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-phone-number.md "")
:

[senderInformation.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-postal-code.md "")
:

[senderInformation.referenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-reference-number.md "")
:

[senderInformation.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-type.md "")
:

Related Information
-------------------

* [REST API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Dual-Message AFT with Visa Secure {#payouts-services-auth-dual-message-aft-vs-ex-rest}
====================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "processingInformation": {
    "businessApplicationId": "WT",
    "commerceIndicator": "vbv",
    "authorizationOptions": {
      "initiator": {
        "type": "customer",
        "storedCredentialUsed": "false"
      },
      "aftIndicator": "true",
      "fundingOptions":{
        "initiator": {
          "type":"S"
        }
      }
    }
  },
        "purposeOfPayment": "16"
    },
  "paymentInformation": {
    "card": {
      "number": "4111111111111111",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "type": "001",
      "securityCode": "123"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "100",
      "currency": "USD",
      "anticipatedAmount": "123.45",
      "surcharge": {
        "amount": "5"
      }
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "1 Market St",
      "locality": "san francisco",
      "administrativeArea": "CA",
      "postalCode": "94105",
      "country": "US",
      "email": "test@cybs.com",
      "phoneNumber": "4158880000"
    }
  },
  "acquirerInformation": {
    "merchantId": "pa_ctv_sg101"
  },
    "aggregatorInformation.name": "test",
  "recipientInformation": {
    "accountId": "987654321",
    "accountType": "99",
    "address1": "Alpine Eco Road",
    "address2": "Address2 value",
    "firstName": "recFirstname",
    "lastName": "resLastname",
    "middleName": "recMiddletname",
    "locality": "recipient_city",
    "country": "GBR",
    "postalCode": "571216",
    "streetName": "Alpine eco road",
    "dateOfBirth": "",
    "beneficiaryId": "",
    "beneficiaryName": "",
    "buildingNumber":"Tulip Appartment",
    "beneficiaryAddress": ""
  },
  "senderInformation": {
    "account": {
      "number": "154264765376576126571652675176",
      "fundsSource": "02"
    },
    "firstName": "senderfirstname",
    "middleName": "sendermiddlename",
    "lastName": "senderLastname",
    "postalCode": "654321",
    "phoneNumber": "01234567892",
    "address1": "Colorful street 123",
    "locality": "Rotterdam",
    "countryCode": "GBR",
    "identificationNumber": "12345678910111213223",
    "personalIdType": "TXIN",
    "administrativeArea": "KA",
    "type": "B",
    "name": "Thomas Smith",
    "referenceNumber": "15426476537657"
  },
  "merchantInformation": {
    "vatRegistrationNumber": "15426476537657",
    "merchantDescriptor": {
      "name": "utf8_merchant_descriptor",
      "alternateName": "",
      "contact": "",
      "address1": "",
      "locality": "Mountain View",
      "country": "",
      "postalCode": "94044",
      "administrativeArea": "CA",
      "phone": "",
      "url": "",
      "countryOfOrigin": "",
      "storeId": "",
      "storeName": "",
      "customerServicePhoneNumber": ""
    }
  },
  "captureOptions": {
    "dateToCapture": "1231"
  },
  "consumerAuthenticationInformation": {
    "cavv": "ABCDEabcde12345678900987654321abcdeABCDE",
    "xid": "12345678909876543210ABCDEabcdeABCDEF1234"
  }
}
```

Response

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7193080414227102940072/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7193080414227102940072"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7193080414227102940072/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "id": "7193080414227102940072",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "100.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "816645",
        "approvalCode": "831000",
        "cardVerification": {
            "resultCodeRaw": "M",
            "resultCode": "M"
        },
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networkTransactionId": "016153570198200",
        "retrievalReferenceNumber": "417709816645",
        "consumerAuthenticationResponse": {
            "code": "2",
            "codeRaw": "2"
        },
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "Y",
            "codeRaw": "Y"
        }
    },
    "reconciliationId": "7193080414227102940072",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2024-06-25T09:34:02Z"
}
```

Dual Message Account Funding Transactions (AFTs) with Visa Secure for Merchant Aggregators {#payouts-services-auth-dual-message-aft-vs-agg-intro}
=================================================================================================================================================

Account Funding Transactions allow a payment service provider to debit funds from a cardholder's Mastercard or Visa account to fund a non-merchant account. This is typically used to load funds onto prepaid cards and electronic wallets.  
Dual Message Account Funding Transactions (AFTs) provide the following benefits:

* Enables customers to identify Mastercard and Visa transactions during the authorization and settlement.
* Allows acquiring partners to use Dual Message BINs when performing a payout transaction.
* Enables users to safely validate their identity and safely store their personal identity.

Endpoint {#payouts-services-auth-dual-message-aft-vs-agg-intro_d7e16}
---------------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-vs-agg-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-vs-agg-intro_d7e35}

Required Fields for a Dual-Message AFT with Visa Secure for Merchant Aggregators Request {#payouts-services-auth-dual-message-aft-vs-agg-reqfields}
===================================================================================================================================================

These fields are required to process a dual-message AFT with Visa Secure for merchant aggregators request:

[acquirerInformation.merchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-merchant-id.md "")
:

[aggregatorInformation.aggregatorId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-agg-id.md "")
:

[aggregatorInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-name.md "")
:

[aggregatorInformation.subMerchant.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-add1.md "")
:

[aggregatorInformation.subMerchant.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-admin-area.md "")
:

[aggregatorInformation.subMerchant.cardAcceptorId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-card-accept-id.md "")
:

[aggregatorInformation.subMerchant.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-country.md "")
:

[aggregatorInformation.subMerchant.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-email.md "")
:

[aggregatorInformation.subMerchant.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-id.md "")
:

[aggregatorInformation.subMerchant.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-locality.md "")
:

[aggregatorInformation.subMerchant.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-name.md "")
:

[aggregatorInformation.subMerchant.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-phone-number.md "")
:

[aggregatorInformation.subMerchant.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-postal-code.md "")
:

[aggregatorInformation.subMerchant.region](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-region.md "")
:

captureOptions.dateToCapture
:

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation.cavv](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-cavv-a.md "")
:

[consumerAuthenticationInformation.xid](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-xid.md "")
:
This field is only required when you have received an XID value in a previous transaction.

[merchantInformation.merchantDescriptor.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-admin-area.md "")
:

[merchantInformation.merchantDescriptor.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-locality.md "")
:

[merchantInformation.merchantDescriptor.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[merchantInformation.merchantDescriptor.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-postalcode.md "")
:

[merchantInformation.vatRegistrationNumber](https://developer.cybersource.com/docs/ctv/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[orderInformation.amountDetails.anticipatedAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-anticipated-amount.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.surcharge.amount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-surcharge-amount.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.securityCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-security-code-a.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[processingInformation.authorizationOptions.aftIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-aft-ind.md "")
:

[processingInformation.authorizationOptions.initiator.storedCredentialUsed](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")
:

[processingInformation.authorizationOptions.initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:

[processingInformation.businessApplicationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-business-appl-id.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:

[processingInformation.fundingOptions.initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-funding-ops-initiator-type.md "")
:

[processingInformation.purposeOfPayment](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purpose-of-payment.md "")
:

[recipientInformation.accountId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-id.md "")
:

[recipientInformation.accountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-type.md "")
:

[recipientInformation.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address1.md "")
:

[recipientInformation.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address2.md "")
:

[recipientInformation.buildingNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-building-num.md "")
:

[recipientInformation.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-country.md "")
:

[recipientInformation.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-first-name.md "")
:

[recipientInformation.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-last-name.md "")
:

[recipientInformation.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-locality.md "")
:

[recipientInformation.middleName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-middle-name.md "")
:

[recipientInformation.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-postal-code.md "")
:

[recipientInformation.streetName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-street-name.md "")
:

[senderInformation.account.fundsSource](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-funds-source.md "")
:

[senderInformation.account.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-number.md "")
:

[senderInformation.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-address1.md "")
:

[senderInformation.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-administrative-area.md "")
:

[senderInformation.countryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-country-code.md "")
:

[senderInformation.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-first-name.md "")
:

[senderInformation.identificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-identification-num.md "")
:

[senderInformation.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-last-name.md "")
:

[senderInformation.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-locality.md "")
:

[senderInformation.middleName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-middle-name.md "")
:

[senderInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-name.md "")
:

[senderInformation.personalIdType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-personal-id-type.md "")
:

[senderInformation.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-phone-number.md "")
:

[senderInformation.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-postal-code.md "")
:

[senderInformation.referenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-reference-number.md "")
:

[senderInformation.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-type.md "")
:

Related Information
-------------------

* [REST API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Dual-Message AFT with Visa Secure for Merchant Aggregators {#payouts-services-auth-dual-message-aft-vs-agg-ex-rest}
=================================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "processingInformation": {
        "businessApplicationId": "AA",
        "commerceIndicator": "vbv",
        "authorizationOptions": {
            "initiator": {
                "type": "customer",
                "storedCredentialUsed": "false"
            },
            "aftIndicator": "true",
            "fundingOptions": {
                "initiator": {
                    "type": "S"
                }
            }
        }
    },
        "purposeOfPayment": "16"
    },
    "paymentInformation": {
        "card": {
            "number": "4111111111111111",
            "expirationMonth": "12",
            "expirationYear": "2031",
            "type": "001",
            "securityCode": "123"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100",
            "currency": "USD",
            "anticipatedAmount": "123.45",
            "surcharge": {
                "amount": "5"
            }
        },
        "billTo": {
            "firstName": "John",
            "lastName": "Doe",
            "address1": "1 Market St",
            "locality": "san francisco",
            "administrativeArea": "CA",
            "postalCode": "94105",
            "country": "US",
            "email": "test@cybs.com",
            "phoneNumber": "4158880000"
        }
    },
    "acquirerInformation": {
        "merchantId": "pa_ctv_sg101"
    },
    "aggregatorInformation.name": "test",
    "recipientInformation": {
        "accountId": "987654321",
        "accountType": "99",
        "address1": "Alpine Eco Road",
        "address2": "Address2 value",
        "firstName": "recFirstname",
        "lastName": "resLastname",
        "middleName": "recMiddletname",
        "locality": "recipient_city",
        "country": "GBR",
        "postalCode": "571216",
        "streetName": "Alpine eco road",
        "dateOfBirth": "",
        "beneficiaryId": "",
        "beneficiaryName": "",
        "buildingNumber": "Tulip Appartment",
        "beneficiaryAddress": ""
    },
    "senderInformation": {
        "account": {
            "number": "154264765376576126571652675176",
            "fundsSource": "02"
        },
        "firstName": "senderfirstname",
        "middleName": "sendermiddlename",
        "lastName": "senderLastname",
        "postalCode": "654321",
        "phoneNumber": "01234567892",
        "address1": "Colorful street 123",
        "locality": "Rotterdam",
        "countryCode": "GBR",
        "identificationNumber": "12345678910111213223",
        "personalIdType": "TXIN",
        "administrativeArea": "KA",
        "type": "B",
        "name": "Thomas Smith",
        "referenceNumber": "15426476537657"
    },
    "merchantInformation": {
        "vatRegistrationNumber": "15426476537657",
        "merchantDescriptor": {
            "name": "utf8_merchant_descriptor",
            "alternateName": "",
            "contact": "",
            "address1": "",
            "locality": "Mountain View",
            "country": "",
            "postalCode": "94044",
            "administrativeArea": "CA",
            "phone": "",
            "url": "",
            "countryOfOrigin": "",
            "storeId": "",
            "storeName": "",
            "customerServicePhoneNumber": ""
        }
    },
    "captureOptions": {
        "dateToCapture": "1231"
    },
    "consumerAuthenticationInformation": {
        "cavv": "ABCDEabcde12345678900987654321abcdeABCDE",
        "xid": "12345678909876543210ABCDEabcdeABCDEF1234"
    },
    "aggregatorInformation": {
        "aggregatorId": "987654321",
        "name": "Aggregator name",
        "subMerchant": {
            "cardAcceptorId": "4321923",
            "id": "572126",
            "name": "sub merchant name",
            "address1": "Tower Plaza 123",
            "locality": "NewJersey",
            "administrativeArea": "NJ",
            "region": "",
            "postalCode": "22102",
            "country": "US",
            "email": "test@test.com",
            "phoneNumber": "987344334112"
        }
    }
}
```

Response

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7193091579347103140072/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7193091579347103140072"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7193091579347103140072/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "id": "7193091579347103140072",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "100.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "816668",
        "approvalCode": "831000",
        "cardVerification": {
            "resultCodeRaw": "M",
            "resultCode": "M"
        },
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networkTransactionId": "016153570198200",
        "retrievalReferenceNumber": "417709816668",
        "consumerAuthenticationResponse": {
            "code": "2",
            "codeRaw": "2"
        },
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "Y",
            "codeRaw": "Y"
        }
    },
    "reconciliationId": "7193091579347103140072",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2024-06-25T09:52:39Z"
}
```

Dual Message Account Funding Transactions (AFTs) with Network Tokens {#payouts-services-auth-dual-message-aft-token-intro}
==========================================================================================================================

Account Funding Transactions allow a payment service provider to debit funds from a cardholder's Mastercard or Visa account to fund a non-merchant account. This is typically used to load funds onto prepaid cards and electronic wallets.  
Dual Message Account Funding Transactions (AFTs) with Network Tokens provide the following benefits:

* Enables customers to identify Mastercard and Visa transactions during the authorization and settlement.
* Allows acquiring partners to use Dual Message BINs when performing a payout transaction.
* Increases the security with payout transactions.
* Decreases the chances of fraudulent transactions

Endpoint {#payouts-services-auth-dual-message-aft-token-intro_d7e16}
--------------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-token-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-token-intro_d7e35}

Required Fields for a Dual-Message AFT with Network Tokens Request {#payouts-services-auth-dual-message-aft-token-reqfields}
============================================================================================================================

These fields are required to process a dual-message AFT with network tokens request:

[acquirerInformation.merchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-merchant-id.md "")
:

[aggregatorInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-name.md "")
:

captureOptions.dateToCapture
:

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation.cavv](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-cavv-a.md "")
:

[consumerAuthenticationInformation.xid](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-xid.md "")
:
This field is only required when you have received an XID value in a previous transaction.

[merchantInformation.merchantDescriptor.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-admin-area.md "")
:

[merchantInformation.merchantDescriptor.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-locality.md "")
:

[merchantInformation.merchantDescriptor.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[merchantInformation.merchantDescriptor.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-postalcode.md "")
:

[merchantInformation.vatRegistrationNumber](https://developer.cybersource.com/docs/ctv/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[orderInformation.amountDetails.anticipatedAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-anticipated-amount.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.surcharge.amount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-surcharge-amount.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.tokenizedCard.card.cryptogram](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-cryptogram.md "")
:

[paymentInformation.tokenizedCard.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-exp-month.md "")
:

[paymentInformation.tokenizedCard.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-exp-year.md "")
:

[paymentInformation.tokenizedCard.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-num.md "")
:

[paymentInformation.tokenizedCard.securityCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-security-code.md "")
:

[paymentInformation.tokenizedCard.transactionType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-txn-type.md "")
:

[paymentInformation.tokenizedCard.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-type-a.md "")
:
{#payouts-services-auth-dual-message-aft-token-reqfields_dl_ntn_5xh_2cc}

[processingInformation.authorizationOptions.aftIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-aft-ind.md "")
:

[processingInformation.authorizationOptions.initiator.storedCredentialUsed](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")
:

[processingInformation.authorizationOptions.initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:

[processingInformation.businessApplicationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-business-appl-id.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:

[processingInformation.fundingOptions.initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-funding-ops-initiator-type.md "")
:

[processingInformation.purposeOfPayment](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purpose-of-payment.md "")
:

[recipientInformation.accountId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-id.md "")
:

[recipientInformation.accountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-type.md "")
:

[recipientInformation.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address1.md "")
:

[recipientInformation.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address2.md "")
:

[recipientInformation.buildingNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-building-num.md "")
:

[recipientInformation.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-country.md "")
:

[recipientInformation.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-first-name.md "")
:

[recipientInformation.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-last-name.md "")
:

[recipientInformation.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-locality.md "")
:

[recipientInformation.middleName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-middle-name.md "")
:

[recipientInformation.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-postal-code.md "")
:

[recipientInformation.streetName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-street-name.md "")
:

[senderInformation.account.fundsSource](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-funds-source.md "")
:

[senderInformation.account.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-number.md "")
:

[senderInformation.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-address1.md "")
:

[senderInformation.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-administrative-area.md "")
:

[senderInformation.countryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-country-code.md "")
:

[senderInformation.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-first-name.md "")
:

[senderInformation.identificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-identification-num.md "")
:

[senderInformation.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-last-name.md "")
:

[senderInformation.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-locality.md "")
:

[senderInformation.middleName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-middle-name.md "")
:

[senderInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-name.md "")
:

[senderInformation.personalIdType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-personal-id-type.md "")
:

[senderInformation.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-phone-number.md "")
:

[senderInformation.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-postal-code.md "")
:

[senderInformation.referenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-reference-number.md "")
:

[senderInformation.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-type.md "")
:
{#payouts-services-auth-dual-message-aft-token-reqfields_dl_otn_5xh_2cc}

Related Information
-------------------

* [REST API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Dual-Message AFT with Network Tokens {#payouts-services-auth-dual-message-aft-token-ex-rest}
==========================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "processingInformation": {
        "businessApplicationId": "WT",
        "commerceIndicator": "vbv",
        "authorizationOptions": {
            "initiator": {
                "type": "customer",
                "storedCredentialUsed": "false"
            },
            "aftIndicator": "true",
            "fundingOptions": {
                "initiator": {
                    "type": "S"
                }
            }
        }
    },
        "purposeOfPayment": "16"
    },
    "paymentInformation": {
        "tokenizedCard": {
            "cryptogram": "ABCDE12345ABCED12345ABCDE123",
            "number": "4111111111111111",
            "expirationMonth": "12",
            "expirationYear": "2031",
            "type": "001",
            "securityCode": "123",
            "transactionType": "1"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100",
            "currency": "USD",
            "anticipatedAmount": "123.45",
            "surcharge": {
                "amount": "5"
            }
        },
        "billTo": {
            "firstName": "John",
            "lastName": "Doe",
            "address1": "1 Market St",
            "locality": "san francisco",
            "administrativeArea": "CA",
            "postalCode": "94105",
            "country": "US",
            "email": "test@cybs.com",
            "phoneNumber": "4158880000"
        }
    },
    "acquirerInformation": {
        "merchantId": "pa_ctv_sg101"
    },
    "aggregatorInformation.name": "test",
    "recipientInformation": {
        "accountId": "987654321",
        "accountType": "99",
        "address1": "Alpine Eco Road",
        "address2": "Address2 value",
        "firstName": "recFirstname",
        "lastName": "resLastname",
        "middleName": "recMiddletname",
        "locality": "recipient_city",
        "country": "GBR",
        "postalCode": "571216",
        "streetName": "Alpine eco road",
        "dateOfBirth": "",
        "beneficiaryId": "",
        "beneficiaryName": "",
        "buildingNumber": "Tulip Appartment",
        "beneficiaryAddress": ""
    },
    "senderInformation": {
        "account": {
            "number": "154264765376576126571652675176",
            "fundsSource": "02"
        },
        "firstName": "senderfirstname",
        "middleName": "sendermiddlename",
        "lastName": "senderLastname",
        "postalCode": "654321",
        "phoneNumber": "01234567892",
        "address1": "Colorful street 123",
        "locality": "Rotterdam",
        "countryCode": "GBR",
        "identificationNumber": "12345678910111213223",
        "personalIdType": "TXIN",
        "administrativeArea": "KA",
        "type": "B",
        "name": "Thomas Smith",
        "referenceNumber": "15426476537657"
    },
    "merchantInformation": {
        "vatRegistrationNumber": "15426476537657",
        "merchantDescriptor": {
            "name": "utf8_merchant_descriptor",
            "alternateName": "",
            "contact": "",
            "address1": "",
            "locality": "Mountain View",
            "country": "",
            "postalCode": "94044",
            "administrativeArea": "CA",
            "phone": "",
            "url": "",
            "countryOfOrigin": "",
            "storeId": "",
            "storeName": "",
            "customerServicePhoneNumber": ""
        }
    },
    "captureOptions": {
        "dateToCapture": "1231"
    },
    "consumerAuthenticationInformation": {
        "cavv": "ABCDEabcde12345678900987654321abcdeABCDE",
        "xid": "12345678909876543210ABCDEabcdeABCDEF1234"
    }
}
```

Response

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7193101615227103440072/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7193101615227103440072"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7193101615227103440072/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "id": "7193101615227103440072",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "100.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "816692",
        "approvalCode": "831000",
        "cardVerification": {
            "resultCodeRaw": "M",
            "resultCode": "M"
        },
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networkTransactionId": "016153570198200",
        "retrievalReferenceNumber": "417710816692",
        "consumerAuthenticationResponse": {
            "code": "2",
            "codeRaw": "2"
        },
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "Y",
            "codeRaw": "Y"
        }
    },
    "reconciliationId": "7193101615227103440072",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2024-06-25T10:09:22Z"
}
```

Dual Message Account Funding Transactions (AFTs) to Establish a Recurring Payout Transaction (CIT) {#payouts-services-auth-dual-message-aft-cit-intro}
======================================================================================================================================================

Account Funding Transactions allow a payment service provider to debit funds from a cardholder's Mastercard or Visa account to fund a non-merchant account. This is typically used to load funds onto prepaid cards and electronic wallets.  
Dual Message Account Funding Transactions (AFTs) provide the following benefits:

* Enables customers to identify Mastercard and Visa transactions during the authorization and settlement.
* Allows acquiring partners to use Dual Message BINs when performing a payout transaction.

Using the credential-on-file transactions, customers can set up recurring transfers, for example transferring $50 to the customer's wallet each month. To set up such a transaction, the customer needs to create a Customer Inititated Transaction (CIT) that establishes the frequency, amount and duration of the recurring transfer. This information is then saved so that follow on Merchant Initiated Transactions (MITs) can occur on the customer's behalf.

Endpoint {#payouts-services-auth-dual-message-aft-cit-intro_d7e16}
------------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-cit-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-cit-intro_d7e35}

Required Fields for a Dual-Message AFT with a CIT Request {#payouts-services-auth-dual-message-aft-cit-reqfields}
=================================================================================================================

These fields are required to process a dual-message AFT with a CIT request:

[acquirerInformation.merchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-merchant-id.md "")
:

[aggregatorInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-name.md "")
:

captureOptions.dateToCapture
:

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation.cavv](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-cavv-a.md "")
:

[consumerAuthenticationInformation.xid](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-xid.md "")
:
This field is only required when you have received an XID value in a previous transaction.

[merchantInformation.merchantDescriptor.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-address1.md "")
:

[merchantInformation.merchantDescriptor.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-admin-area.md "")
:

[merchantInformation.merchantDescriptor.alternateName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-alt-name.md "")
:

[merchantInformation.merchantDescriptor.contact](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-contact.md "")
:

[merchantInformation.merchantDescriptor.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-county.md "")
:

[merchantInformation.merchantDescriptor.countryOfOrigin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-of-origin.md "")
:

[merchantInformation.merchantDescriptor.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-locality.md "")
:

[merchantInformation.merchantDescriptor.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[merchantInformation.merchantDescriptor.phone](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-phone.md "")
:

[merchantInformation.merchantDescriptor.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-postalcode.md "")
:

[orderInformation.amountDetails.anticipatedAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-anticipated-amount.md "")
:

[merchantInformation.vatRegistrationNumber](https://developer.cybersource.com/docs/ctv/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.surcharge.amount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-surcharge-amount.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.securityCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-security-code-a.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[paymentInformation.tokenizedCard.card.cryptogram](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-cryptogram.md "")
:

[paymentInformation.tokenizedCard.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-num.md "")
:

[paymentInformation.tokenizedCard.transactionType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-txn-type.md "")
:

[processingInformation.authorizationOptions.aftIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-aft-ind.md "")
:

[processingInformation.authorizationOptions.initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:

[processingInformation.businessApplicationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-business-appl-id.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:

[processingInformation.fundingOptions.initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-funding-ops-initiator-type.md "")
:

[processingInformation.purposeOfPayment](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purpose-of-payment.md "")
:

[recipientInformation.accountId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-id.md "")
:

[recipientInformation.accountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-type.md "")
:

[recipientInformation.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address1.md "")
:

[recipientInformation.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address2.md "")
:

[recipientInformation.buildingNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-building-num.md "")
:

[recipientInformation.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-country.md "")
:

[recipientInformation.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-first-name.md "")
:

[recipientInformation.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-last-name.md "")
:

[recipientInformation.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-locality.md "")
:

[recipientInformation.middleName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-middle-name.md "")
:

[recipientInformation.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-postal-code.md "")
:

[recipientInformation.streetName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-street-name.md "")
:

[senderInformation.account.fundsSource](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-funds-source.md "")
:

[senderInformation.account.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-number.md "")
:

[senderInformation.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-address1.md "")
:

[senderInformation.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-administrative-area.md "")
:

[senderInformation.countryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-country-code.md "")
:

[senderInformation.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-first-name.md "")
:

senderInformation.fundSource
:

[senderInformation.identificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-identification-num.md "")
:

[senderInformation.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-last-name.md "")
:

[senderInformation.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-locality.md "")
:

[senderInformation.middleName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-middle-name.md "")
:

[senderInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-name.md "")
:

[senderInformation.personalIdType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-personal-id-type.md "")
:

[senderInformation.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-phone-number.md "")
:

[senderInformation.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-postal-code.md "")
:

[senderInformation.referenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-reference-number.md "")
:

[senderInformation.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-type.md "")
:

Related Information
-------------------

* [REST API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Dual-Message AFT with a CIT {#payouts-services-auth-dual-message-aft-cit-ex-rest}
===============================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "processingInformation": {
        "businessApplicationId": "WT",
        "commerceIndicator": "vbv",
        "authorizationOptions": {
            "initiator": {
                "type": "customer"
            },
            "aftIndicator": "true",
            "fundingOptions": {
                "initiator": {
                    "type": "S"
                }
            }
        }
    },
        "purposeOfPayment": "16"
    },
    "paymentInformation": {
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2031",
            "type": "001",
            "securityCode": "123"
        },
        "tokenizedCard": {
            "number": "4111111111111111",
            "cryptogram": "ABCDE12345ABCED12345ABCDE123",
            "transactionType": "1"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100",
            "currency": "USD",
            "anticipatedAmount": "123.45",
            "surcharge": {
                "amount": "5"
            }
        },
        "billTo": {
            "firstName": "John",
            "lastName": "Doe",
            "address1": "1 Market St",
            "locality": "san francisco",
            "administrativeArea": "CA",
            "postalCode": "94105",
            "country": "US",
            "email": "test@cybs.com",
            "phoneNumber": "4158880000"
        }
    },
    "acquirerInformation": {
        "merchantId": "pa_ctv_sg101"
    },
    "aggregatorInformation.name": "test",
    "recipientInformation": {
        "accountId": "987654321",
        "accountType": "99",
        "address1": "Alpine Eco Road",
        "address2": "Address2 value",
        "firstName": "recFirstname",
        "lastName": "resLastname",
        "middleName": "recMiddletname",
        "locality": "recipient_city",
        "country": "GBR",
        "postalCode": "571216",
        "streetName": "Alpine eco road",
        "dateOfBirth": "",
        "beneficiaryId": "",
        "beneficiaryName": "",
        "buildingNumber": "Tulip Appartment",
        "beneficiaryAddress": ""
    },
    "senderInformation": {
        "account": {
            "number": "154264765376576126571652675176",
            "fundsSource": "02"
        },
        "firstName": "senderfirstname",
        "middleName": "sendermiddlename",
        "lastName": "senderLastname",
        "postalCode": "654321",
        "phoneNumber": "9876543210",
        "address1": "senderAddress",
        "locality": "Rotterdam",
        "fundsSource": "card",
        "countryCode": "GBR",
        "identificationNumber": "12345678910111213223",
        "personalIdType": "TXIN",
        "administrativeArea": "US",
        "type": "B",
        "name": "Thomas Smith",
        "referenceNumber": "15426476537657"
    },
    "captureOptions": {
        "dateToCapture": "1231"
    },
    "consumerAuthenticationInformation": {
        "cavv": "ABCDEabcde12345678900987654321abcdeABCDE",
        "xid": "12345678909876543210ABCDEabcdeABCDEF1234"
    },
    "merchantDescriptor": {
        "name": "utf8_merchant_descriptor",
        "alternateName": "merchant alternatename",
        "contact": "9995555444",
        "address1": "merchant address",
        "locality": "Mountain View",
        "country": "US",
        "postalCode": "94044",
        "administrativeArea": "CA",
        "phone": "99955554441",
        "url": "",
        "countryOfOrigin": "US",
        "storeId": "",
        "storeName": "",
        "customerServicePhoneNumber": ""
    }
}
```

Response

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7193118915937104040072/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7193118915937104040072"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7193118915937104040072/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "id": "7193118915937104040072",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "100.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "816726",
        "approvalCode": "831000",
        "cardVerification": {
            "resultCodeRaw": "M",
            "resultCode": "M"
        },
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networkTransactionId": "016153570198200",
        "retrievalReferenceNumber": "417710816726",
        "consumerAuthenticationResponse": {
            "code": "2",
            "codeRaw": "2"
        },
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "Y",
            "codeRaw": "Y"
        }
    },
    "reconciliationId": "7193118915937104040072",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2024-06-25T10:38:12Z"
} 
```

Dual Message Account Funding Transactions (AFTs) for a Recurring Payout Transaction (MIT) {#payouts-services-auth-dual-message-aft-mit-intro}
=============================================================================================================================================

Account Funding Transactions allow a payment service provider to debit funds from a cardholder's Mastercard or Visa account to fund a non-merchant account. This is typically used to load funds onto prepaid cards and electronic wallets.  
Dual Message Account Funding Transactions (AFTs) provide the following benefits:

* Enables customers to identify Mastercard and Visa transactions during the authorization and settlement.
* Allows acquiring partners to use Dual Message BINs when performing a payout transaction.

Using the credential-on-file transactions, customers can set up recurring transfers, for example transferring $50 to the customer's wallet each month. To set up such a transaction, the customer needs to create a Customer Inititated Transaction (CIT) that establishes the frequency, amount and duration of the recurring transfer. This information is then saved so that follow on Merchant Initiated Transactions (MITs) can occur on the customer's behalf.

Endpoint {#payouts-services-auth-dual-message-aft-mit-intro_d7e16}
------------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-mit-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-mit-intro_d7e35}

Required Fields for a Dual-Message AFT with an MIT Request {#payouts-services-auth-dual-message-aft-mit-reqfields}
==================================================================================================================

These fields are required to process a dual-message AFT with an MIT request:

[acquirerInformation.merchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-merchant-id.md "")
:

[aggregatorInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-name.md "")
:

captureOptions.dateToCapture
:

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[merchantInformation.merchantDescriptor.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-admin-area.md "")
:

[merchantInformation.merchantDescriptor.alternateName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-alt-name.md "")
:

[merchantInformation.merchantDescriptor.contact](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-contact.md "")
:

[merchantInformation.merchantDescriptor.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-county.md "")
:

[merchantInformation.merchantDescriptor.countryOfOrigin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-of-origin.md "")
:

[merchantInformation.merchantDescriptor.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-locality.md "")
:

[merchantInformation.merchantDescriptor.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[merchantInformation.merchantDescriptor.phone](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-phone.md "")
:

[merchantInformation.merchantDescriptor.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-postalcode.md "")
:

[merchantInformation.vatRegistrationNumber](https://developer.cybersource.com/docs/ctv/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[orderInformation.amountDetails.anticipatedAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-anticipated-amount.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.surcharge.amount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-surcharge-amount.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.securityCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-security-code-a.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[paymentInformation.tokenizedCard.cryptogram](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-cryptogram.md "")
:

[paymentInformation.tokenizedCard.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-num.md "")
:

[paymentInformation.tokenizedCard.transactionType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-txn-type.md "")
:

[processingInformation.authorizationOptions.aftIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-aft-ind.md "")
:

[processingInformation.authorizationOptions.initiator.storedCredentialUsed](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")
:

[processingInformation.authorizationOptions.initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:

[processingInformation.authorizationOptions.initiator.merchantInitiatedTransaction.previousTransactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-txn.md "")
:
Set this value to `true`

[processingInformation.businessApplicationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-business-appl-id.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:

[processingInformation.fundingOptions.initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-funding-ops-initiator-type.md "")
:

[processingInformation.purposeOfPayment](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purpose-of-payment.md "")
:

[recipientInformation.accountId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-id.md "")
:

[recipientInformation.accountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-type.md "")
:

[recipientInformation.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address1.md "")
:

[recipientInformation.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address2.md "")
:

[recipientInformation.buildingNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-building-num.md "")
:

[recipientInformation.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-country.md "")
:

[recipientInformation.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-first-name.md "")
:

[recipientInformation.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-last-name.md "")
:

[recipientInformation.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-locality.md "")
:

[recipientInformation.middleName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-middle-name.md "")
:

[recipientInformation.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-postal-code.md "")
:

[recipientInformation.streetName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-street-name.md "")
:

[senderInformation.account.fundsSource](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-funds-source.md "")
:

[senderInformation.account.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-number.md "")
:

[senderInformation.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-address1.md "")
:

[senderInformation.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-administrative-area.md "")
:

[senderInformation.countryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-country-code.md "")
:

[senderInformation.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-first-name.md "")
:

senderInformation.fundSource
:

[senderInformation.identificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-identification-num.md "")
:

[senderInformation.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-last-name.md "")
:

[senderInformation.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-locality.md "")
:

[senderInformation.middleName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-middle-name.md "")
:

[senderInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-name.md "")
:

[senderInformation.personalIdType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-personal-id-type.md "")
:

[senderInformation.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-phone-number.md "")
:

[senderInformation.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-postal-code.md "")
:

[senderInformation.referenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-reference-number.md "")
:

[senderInformation.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-type.md "")
:

Related Information
-------------------

* [REST API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Dual-Message AFT with an MIT {#payouts-services-auth-dual-message-aft-mit-ex-rest}
================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "processingInformation": {
        "businessApplicationId": "AA",
        "commerceIndicator": "recurring",
        "authorizationOptions": {
            "initiator": {
                "type": "merchant",
                "storedCredentialUsed": "true"
            },
            "merchantInitiatedTransaction": {
                "previousTransactionID": "1234567890"
            },
            "aftIndicator": "true",
            "fundingOptions": {
                "initiator": {
                    "type": "S"
                }
            }
        }
    },
        "purposeOfPayment": "16"
    },
    "paymentInformation": {
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2031",
            "type": "001",
            "securityCode": "123"
        },
        "tokenizedCard": {
            "number": "4111111111111111",
            "cryptogram": "ABCDE12345ABCED12345ABCDE123",
            "transactionType": "3"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100",
            "currency": "USD",
            "anticipatedAmount": "123.45",
            "surcharge": {
                "amount": "5"
            }
        },
        "billTo": {
            "firstName": "John",
            "lastName": "Doe",
            "address1": "1 Market St",
            "locality": "san francisco",
            "administrativeArea": "CA",
            "postalCode": "94105",
            "country": "US",
            "email": "test@test.com",
            "phoneNumber": "4158880000"
        }
    },
    "acquirerInformation": {
        "merchantId": "pa_ctv_sg101"
    },
    "aggregatorInformation.name": "test",
    "recipientInformation": {
        "accountId": "987654321",
        "accountType": "99",
        "address1": "Alpine Eco Road",
        "address2": "Address2 value",
        "firstName": "recFirstname",
        "lastName": "resLastname",
        "middleName": "recMiddletname",
        "locality": "recipient_city",
        "country": "GBR",
        "postalCode": "571216",
        "streetName": "Alpine eco road",
        "dateOfBirth": "",
        "beneficiaryId": "",
        "beneficiaryName": "",
        "buildingNumber": "Tulip Appartment",
        "beneficiaryAddress": ""
    },
    "senderInformation": {
        "account": {
            "number": "154264765376576126571652675176",
            "fundsSource": "02"
        },
        "firstName": "senderfirstname",
        "middleName": "sendermiddlename",
        "lastName": "senderLastname",
        "postalCode": "654321",
        "phoneNumber": "9876543210",
        "address1": "senderAddress",
        "locality": "Rotterdam",
        "fundsSource": "card",
        "countryCode": "GBR",
        "identificationNumber": "12345678910111213223",
        "personalIdType": "TXIN",
        "administrativeArea": "KA",
        "type": "B",
        "name": "Thomas Smith",
        "referenceNumber": "15426476537657"
    },
    "captureOptions": {
        "dateToCapture": "1231"
    },
    "merchantInformation": {
        "vatRegistrationNumber": "15426476537657",
        "merchantDescriptor": {
            "name": "utf8_merchant_descriptor",
            "alternateName": "merchant alternatename",
            "contact": "9995555444",
            "address1": "merchant address",
            "locality": "Mountain View",
            "country": "US",
            "postalCode": "94044",
            "administrativeArea": "CA",
            "phone": "99955554441",
            "url": "",
            "countryOfOrigin": "US",
            "storeId": "",
            "storeName": "",
            "customerServicePhoneNumber": ""
        }
    }
}
```

Response

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7193111028367103640072/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7193111028367103640072"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7193111028367103640072/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "id": "7193111028367103640072",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "100.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "816710",
        "approvalCode": "831000",
        "cardVerification": {
            "resultCodeRaw": "M",
            "resultCode": "M"
        },
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networkTransactionId": "016153570198200",
        "retrievalReferenceNumber": "417710816710",
        "consumerAuthenticationResponse": {
            "code": "2",
            "codeRaw": "2"
        },
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "Y",
            "codeRaw": "Y"
        }
    },
    "reconciliationId": "7193111028367103640072",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2024-06-25T10:25:03Z"
}
```

Appendix A: Business Application Identifier Values {#payouts-appendix-bai}
==========================================================================

The Business Application Identifier (BAI) is used to identify the category of the Account Funding Transaction (AFT). Provide one of the values when you send field `processingInformation.businessApplicationId`.  
All acquirers, service providers, and merchants are required to submit a valid BAI value when submitting AFTs.

| BAI Value | Category                                                                                                                        | Requirements                                                                                                                                                                                                                                                                                                                                                                    |
|:----------|:--------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AA`      | Account-to-Account Money Transfer. The funding of the cardholder's own account at the same or a different financial institution | Both accounts must be owned by the same person/entity. > NOTE > If you are funding a prepaid account, use the ` TU ` value. Do not use the ` AA ` value.                                                                                                                                                                                                                        |
| `BI`      | Financial Institution offered Bank-Initiated P2P Money Transfer                                                                 | P2P (person-to-person) Money Transfer is initiated from an online banking system, making it a bank-initiated transaction. This category is only used for specific scenarios and only available in limited markets. For more information, contact your Visa representative.                                                                                                      |
| `FD`      | Funds Disbursement                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                 |
| `FT`      | Funds Transfer                                                                                                                  | If the funds will be used for a high-brand risk transaction, the applicable high-brand risk MCC must be used. If a wallet is used to purchase liquid and cryptocurrency assets, the applicable special condition indicator must be used.                                                                                                                                        |
| `PD`      | Payroll Disbursement                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                 |
| `PP`      | Person-to-Person (P2P) Money Transfer                                                                                           | P2P Money Transfer is initiated from an online banking system, making it a bank-initiated transaction. This category is only used when both AFTs and OCTs are supported. When only AFT is supported, use the **FT** category.                                                                                                                                                   |
| `TU`      | Prepaid Card Load or Top-Up                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                 |
| `WT`      | Staged Digital Wallet (SDW) Transfer                                                                                            | If the funds will be used for a high-brand risk transaction, the applicable high-brand risk MCC must be used. If the funds are used for a gambling transaction, the applicable gambling MCC must be used. If a wallet is used to purchase liquid and cryptocurrency assets, the applicable special condition indicator must be used. An AFT is not intended for debt repayment. |
[Business Application Identifier Values]

Appendix B: Sender Source {#payouts-appendix-sender-source}
===========================================================

The Sender Source identifies the source of funds. Provide one of the values when you send field `senderInformation.account.fundsSource`.  
All acquirers, service providers, and merchants are required to submit a valid sender source value when submitting AFTs.

| Value | Definition                                                                                                                                                                                                                              |
|:------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `01`  | Credit Card                                                                                                                                                                                                                             |
| `02`  | Debit Card                                                                                                                                                                                                                              |
| `03`  | Prepaid Card                                                                                                                                                                                                                            |
| `04`  | Cash                                                                                                                                                                                                                                    |
| `05`  | Debit or deposit account that is not linked to a Visa card. This includes checking accounts, savings accounts, proprietary Cybersource `senderInformation.account.fundsSource` debit or ATM card accounts, and digital wallet accounts. |
| `06`  | Credit account that is not linked to a Visa card. This includes credit cards and proprietary lines of credit.                                                                                                                           |
[Sender Source Values]

Appendix C: Visa BAI to Mastercard TTI Mapping {#payouts-appendix-mapping}
==========================================================================

These are the Visa BAI to Mastercard TTI mapping and their descriptions for different regions and transaction types.

Handling Wallet Transfer MCC Across All Regions
-----------------------------------------------

**Visa Business Application Identifier (BAI)** : `WT`: Wallet transfer  
**Mastercard Transaction Type Indicator (TTI)** : `F61`  
**Description**:  
Mastercard specifies Merchant Category Codes (MCC) to retain Account Funding Wallet Transfers.  
These are the MCCs:

* `6051` (Quasi-Cash: Merchant): The account provider's primary activity is buying and selling cryptocurrency.

* `6211` (Securities-Brokers/Dealers): The account provider's primary activity is purchasing, selling, or brokering high-risk securities.

* `7800`/`7801`/`7994`/`7995`/`9406` (gaming and gambling): The account provider's primary activity is gaming or gambling.

* `6540` (Default `WT` MCC): Participants use the mentioned MCC for all other use cases for Transfers to Own Staged Digital Wallet Accounts.
  {#payouts-appendix-mapping_ul_q53_q1l_rdc}
  NOTE Acquirers must adjust the mapping accordingly to clear the file to align with the Auth MCC, and ensure accurate clearing and compliance.  
  The system will automatically overwrite the MCC in these scenarios if mapping is not adjusted:

* When the client includes BAI as `WT` and MCC as `6051`, and the Transaction Purpose is `16` (securities), the system will set the TTI to `F61` and the MCC to `6211`.

* When the client includes BAI as `WT` and MCC as `6051`, and the Transaction Purpose is `11` (cryptocurrency), the system will set the TTI to `F61` and retain the MCC as `6051`.

* When the merchant sends `6051` for any other transaction purpose, the system will replace the MCC with `6540`.

* When you send MCCs other than the ones mentioned above, the system will overwrite them to `6540`.

Handling Account to Account and Funds Transfer MCC for Non-Asia Pacific Region {#payouts-appendix-mapping_section_ltn_y1l_rdc}
------------------------------------------------------------------------------------------------------------------------------

**Visa Business Application Identifier (BAI)** : `FT`: Funds Transfer  
**Mastercard Transaction Type Indicator (TTI)** : `F52`  
**Description**:  
Mastercard specifies MCCs to retain for Account to Account and Funds Transfer for the Non-Asia Pacific region.  
These are the MCCs:

* `6051` (Quasi-Cash: Merchant): The account provider's primary activity is buying and selling cryptocurrency.
* `6211` (Securities-Brokers/Dealers): The account provider's primary activity is purchasing, selling, or brokering high-risk securities.
* `7800`/`7801`/`7994`/`7995`/`9406` (Gaming and Gambling): The account provider's primary activity is gaming or gambling.
* `4829` (Default Funding Transactions): Participants use the mentioned MCC for all other use cases for Account to Account and Funds Transfer.
  {#payouts-appendix-mapping_ul_gmy_cbl_rdc}
  NOTE Acquirers must adjust the mapping accordingly to clear the file to align with the Auth MCC, and ensure accurate clearing and compliance.  
  The system will automatically overwrite the MCC if mapping is not adjusted when you send MCCs other than the ones mentioned above. The system will overwrite them to `4829`.

Handling Account to Account and Funds Transfer MCC for Asia Pacific Region {#payouts-appendix-mapping_section_iwt_gbl_rdc}
--------------------------------------------------------------------------------------------------------------------------

**Visa Business Application Identifier (BAI)** : `FT`: Funds Transfer  
**Mastercard Transaction Type Indicator (TTI)** : `F52`  
**Description**:  
Mastercard specifies MCCs to retain for Account to Account and Funds Transfer for the Asia Pacific region.  
These are:

* `4829` (Money Transfer): Customers transfer funds via an electronic funds transfer/wire transfer/remittance to a named entity (both card-present and card-absent locations, including on the premises of the Merchant and third-party agents).
* `6540` (Fund Transfer): Participants use the mentioned MCC for all other use cases for fund transfer.
  {#payouts-appendix-mapping_ul_sbj_jbl_rdc}
  NOTE Acquirers must adjust the mapping accordingly to clear the file to align with the Auth MCC, and ensure accurate clearing and compliance.  
  The system will automatically overwrite the MCC if mapping is not adjusted when you send MCCs other than the ones mentioned above. The system will overwrite them to `6540`.

Handling Person to Person Funding Transactions MCC Across Regions {#payouts-appendix-mapping_section_e5t_kbl_rdc}
-----------------------------------------------------------------------------------------------------------------

**Visa Business Application Identifier (BAI)** : `PP`: Person-to-Person Money Transfer  
**Mastercard Transaction Type Indicator (TTI)** : `F07`  
**Description**:  
Mastercard specifies MCCs to retain for general Person to Person funding transactions.  
These are the MCCs:

* `4829` (Money Transfer): Customers transfer funds via electronic funds transfer/wire transfer/remittance to a named entity (both card-present and card-absent locations including on the premises of the Merchant and third-party agents).
* `6540` (Fund Transfer): Participants use this MCC for all other fund transfer use cases.
  {#payouts-appendix-mapping_ul_nld_4bl_rdc}
  NOTE Acquirers must adjust the mapping accordingly to clear the file to align with the Auth MCC, and ensure accurate clearing and compliance.  
  The system will automatically overwrite the MCC if mapping is not adjusted when you send MCCs other than the ones mentioned above. The system will overwrite them to `6540`.

Handling Person to Person to Card Account Transactions MCC Across Regions {#payouts-appendix-mapping_section_rfl_pbl_rdc}
-------------------------------------------------------------------------------------------------------------------------

**Visa Business Application Identifier (BAI)** : `PP`: Person-to-Person Money Transfer  
**Mastercard Transaction Type Indicator (TTI)** : `F08`  
**Description**:  
Mastercard specifies MCCs to retain for general person-to-person to card account transactions.  
**Person-to-person to card account**: When a merchant conducts a person-to-person transaction and provides both the recipient's account type and account ID, the system classifies the transaction as a Person-to-Person to Card Account transaction. Then the system will apply the specified MCC.  
This is the MCC:

* `4829` (Money Transfer): Customers transfer funds via electronic funds transfer/wire transfer/remittance to a named entity (both card-present and card-absent locations, including on-premises of the merchant and third-party agents).
  {#payouts-appendix-mapping_ul_a3d_rbl_rdc}
  NOTE Acquirers must adjust the mapping accordingly to clear the file to align with the Auth MCC, and ensure accurate clearing and compliance.  
  The system will automatically overwrite the MCC if mapping is not adjusted when you send MCCs other than the ones mentioned above, the system will overwrite them to `6540`.

> NOTE
> Account Identifier Type and value are required for TTI ` F08 `. If the you send the transaction without this data, the system will map it as general person-to-person with TTI ` F07 ` (MCC ` 4829 ` will be sent as is to Mastercard, and all others will map to ` 6540 `).

Appendix D: Test Card Numbers {#payouts_aft_app_test_cards}
===========================================================

| Request                                                                                                                                                                                                                                                                               | Test Card Number |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| [Dual Message Account Funding Transactions (AFTs)](/docs/cybs/en-us/payouts-aft/developer/ctv/rest/payouts-aft-dev/payouts-services-intro/payouts-services-auth-dual-message-aft-intro.md "")                                                       | 4111111111111111 |
| [Dual Message Account Funding Transactions (AFTs) with Visa Secure](/docs/cybs/en-us/payouts-aft/developer/ctv/rest/payouts-aft-dev/payouts-services-intro/payouts-services-auth-dual-message-aft-vs-intro.md "")                                   | 4111111111111111 |
| [Dual Message Account Funding Transactions (AFTs) with Visa Secure for Merchant Aggregators](/docs/cybs/en-us/payouts-aft/developer/ctv/rest/payouts-aft-dev/payouts-services-intro/payouts-services-auth-dual-message-aft-vs-agg-intr.md "")       | 4111111111111111 |
| [Dual Message Account Funding Transactions (AFTs) with Network Tokens](/docs/cybs/en-us/payouts-aft/developer/ctv/rest/payouts-aft-dev/payouts-services-intro/payouts-services-auth-dual-message-aft-token-intro.md "")                             | 4111111111111111 |
| [Dual Message Account Funding Transactions (AFTs) to Establish a Recurring Payout Transaction (CIT)](/docs/cybs/en-us/payouts-aft/developer/ctv/rest/payouts-aft-dev/payouts-services-intro/payouts-services-auth-dual-message-aft-cit-intro.md "") | 4111111111111111 |
| [Dual Message Account Funding Transactions (AFTs) for a Recurring Payout Transaction (MIT)](/docs/cybs/en-us/payouts-aft/developer/ctv/rest/payouts-aft-dev/payouts-services-intro/payouts-services-auth-dual-message-aft-mit-intro.md "")          | 4111111111111111 |
[Test Card Numbers for Dual Message AFTs]

