Transient Tokens {#ctp-tokens-intro}
====================================

The response to a successful customer interaction with `Unified Checkout` is a transient token. This is returned in the response from the checkout.mount() function. The transient token is a reference to the payment data collected on your behalf. Transient tokens allow secure card payments to occur without risk of exposure to sensitive payment information. The transient token is a short-term token that expires after 15 minutes. This reduces your PCI burden/responsibility and ensures that sensitive information is not exposed to your back-end systems.  
Transient tokens can be included requests sent to the Payment Details API for the customer payment data that is collected.

Transient Token Format {#ctp-tokens-format}
===========================================

The transient token is issued as a JSON Web Token (JWT) ([RFC 7519](https://tools.ietf.org/html/rfc7519 "")). The payload portion of the token is a Base64URL-encoded JSON string and contains various claims. For more information, see [JSON Web Tokens](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/Appendix/ctp-appendix-jwts.md "").

Example: Transient Token Format {#uc-trans-tkn-ex}
==================================================

Encrypted Transient Token JWT

```
eyJraWQiOiIwMEl1NWJDT2NINVpPWjFNYldsQktodzFZeFFjSkVlZSIsImFsZyI6IlJTMjU2In0.eyJtZXRhZGF0YSI6eyJzZXF1ZW5jZU51bWJlciI6IjEiLCJjYXJkaG9sZGVyQXV0aGVudGljYXRpb25TdGF0dXMiOmZhbHNlLCJwYXltZW50VHlwZSI6IlNSQ01BU1RFUkNBUkQifSwiaXNzIjoiRmxleC8wMCIsInBheW1lbnRDcmVkZW50aWFsc1JlZmVyZW5jZSI6eyJ1Y19hZ25vc3RpY19wb3J0Zm9saW9fdmFsaWQiOiJXaWUyM2NBS3RGblFlSXpqeDRFUXgifSwiZXhwIjoxNzY1ODg1MDcyLCJ0eXBlIjoiZ2RhLTAuMTAuMCIsImlhdCI6MTc2NTg4NDE3MywianRpIjoiMUQwMlk4Q09FQURYS1k5VjRHTjRNUDJOSVNMVjNQM1dSUUNEV0VZNDJHUjNBRzIzTUI3WjY5NDE0NDkwQkI1MSIsImNvbnRlbnQiOnsiZGV2aWNlSW5mb3JtYXRpb24iOnsiZmluZ2VycHJpbnRTZXNzaW9uSWQiOnt9fSwicHJvY2Vzc2luZ0luZm9ybWF0aW9uIjp7InBheW1lbnRTb2x1dGlvbiI6eyJ2YWx1ZSI6IjAyNyJ9fSwib3JkZXJJbmZvcm1hdGlvbiI6eyJiaWxsVG8iOnsiY291bnRyeSI6e30sImxhc3ROYW1lIjp7fSwiZmlyc3ROYW1lIjp7fSwicGhvbmVOdW1iZXIiOnt9LCJhZGRyZXNzMSI6e30sInBvc3RhbENvZGUiOnt9LCJsb2NhbGl0eSI6e30sImFkbWluaXN0cmF0aXZlQXJlYSI6e30sImVtYWlsIjp7fX0sImFtb3VudERldGFpbHMiOnsidG90YWxBbW91bnQiOnt9LCJjdXJyZW5jeSI6e319LCJzaGlwVG8iOnsiZmlyc3ROYW1lIjp7fSwiY291bnRyeSI6e30sImxhc3ROYW1lIjp7fSwiYWRkcmVzczEiOnt9LCJwb3N0YWxDb2RlIjp7fSwibG9jYWxpdHkiOnt9LCJhZG1pbmlzdHJhdGl2ZUFyZWEiOnt9fX0sInBheW1lbnRJbmZvcm1hdGlvbiI6eyJjYXJkIjp7ImV4cGlyYXRpb25ZZWFyIjp7InZhbHVlIjoiMjAyNyJ9LCJudW1iZXIiOnsibWFza2VkVmFsdWUiOiJYWFhYWFhYWFhYWFg5OTA4IiwiYmluIjoiNTE4NjAwIn0sImV4cGlyYXRpb25Nb250aCI6eyJ2YWx1ZSI6IjAzIn0sInR5cGUiOnsidmFsdWUiOiIwMDIifSwidHlwZVNlbGVjdGlvbkluZGljYXRvciI6eyJ2YWx1ZSI6IjEifX19fSwiXyI6IkwrYnlQL2FIRnhEUDRPc0NGNFI5RkhjbElkZkFXR0g4VkF3NGdta0NubGRyZzQ3WDdnR1hseUZRTWM4aU5KWjBzSlNhTlFOTzM5RHVCVWdWaW1SeC9zRUJJS2VQYXFvRVRoWDZpRjFrWWs1ZkxjWDRqU1gvTmtzb1U0bGQzU0RNTnJHcS8ybDRoM0laTjd1WEVON1g5azA5K3FaRFNaWVk3S1dzaVJXeXNwcHpFZE5uQy9ORGYxY1ZqNUJHZTZnN3Jjckt0THYyT1VzYUIyb3hicVkwL2VuUFY4N0JHakMrUk9lSmFYa3VGeml0RDVrQ0paZHdoYnorRStRVmtnejdBVTZnNG5pa0dsWDFNUklkeXVVNnY4QlJsWG42ZEF3c252TW5pZ3Yvc05NUE4zV0hSaUhZWHZubTdramVOd2k2YW1EbkdTSzVqY3RFMmJPWDZUU0RmWG5RSE01eVhWcFdMRHZxa0VQOVZzM2NBNmhTbTlZcHFaaXRSSjZ5OWtMSGFNemsydm9TWlhUV1JQU210UkZ2TWdcdTAwM2RcdTAwM2QifQ.M1ttoaMyKz9NjQ7nYfhGqrt7Gga1YvUph8FH4-0aV98tNbZilEqF4ANQHKFjNQavJ5_EKB_4cDayuwa7xyZzrz2WNXSlRS97EJYfvFAYza8cq2SpvHlR1DvJdMuYsyui-fZafdkxqTudsAUUYJErWezliWOvCw2gi18hb3bS3V_evt8zznRdgbwd7Q1BgSmQwgnIDI-H4wdZMByMbpG1zC8UjbvyPB5OUQxOTCljmbsiAquSI_8LFJoasRUK9txVjezO49E_DX1ClETbnzuiUlJ6MzBlTNAtdbxGB5ELjuf8-SSj4ojlZZTMWARllskZsx_DUtqLBUdNXKpPKEJtzg
```

{#uc-trans-tkn-ex_codeblock_bagt_cfz_hjc}  
Decoded Transient Token JWT - Visa PAN

```
{
  "metadata": {
    "sequenceNumber": "1",
    "ccJti": "onNpuEB7TmCjcga2",
    "cardholderAuthenticationStatus": false,
    "paymentType": "PANENTRY"
  },
  "iss": "Flex/08",
  "paymentCredentialsReference": {
    "na_partner_ctp2": "P6RXHH8Lc79oT1DKS1_Rs"
  },
  "exp": 1778665181,
  "type": "uc-1.0.0",
  "iat": 1778664281,
  "jti": "1E3QZQ85MKIWE5EU8QUT4AVC2Y4J0Z8ZEQ4C7QDKZ28171QG12DD6A0446DD7118",
  "content": {
    "clientReferenceInformation": {
      "applicationVersion": {},
      "applicationUser": {},
      "code": {},
      "applicationName": {}
    },
    "deviceInformation": {
      "fingerprintSessionId": {}
    },
    "orderInformation": {
      "billTo": {
        "country": {},
        "lastName": {},
        "firstName": {},
        "phoneNumber": {},
        "address2": {},
        "address1": {},
        "postalCode": {},
        "locality": {},
        "buildingNumber": {},
        "administrativeArea": {},
        "email": {}
      },
      "amountDetails": {
        "totalAmount": {},
        "currency": {}
      },
      "shipTo": {
        "firstName": {},
        "lastName": {},
        "country": {},
        "address1": {},
        "postalCode": {},
        "locality": {},
        "buildingNumber": {},
        "administrativeArea": {}
      }
    },
    "paymentInformation": {
      "card": {
        "expirationYear": {
          "value": "2029"
        },
        "number": {
          "maskedValue": "XXXXXXXXXXXX1111",
          "bin": "411111"
        },
        "securityCode": {},
        "expirationMonth": {
          "value": "12"
        },
        "typeSelectionIndicator": {
          "value": "1"
        },
        "type": {
          "value": "001"
        }
      }
    }
  }
}
```

{#uc-trans-tkn-ex_codeblock_bgt_cfz_hjc}  
Decoded Transient Token JWT - Visa Network Token

```
{
  "metadata": {
    "sequenceNumber": "1",
    "tokenizedCard": {
      "card": {
        "expirationYear": "2033",
        "maskedValue": "XXXXXXXXXXXX2700",
        "prefix": "462294",
        "expirationMonth": "08"
      }
    },
    "ccJti": "9M2EooZC767DNhvC",
    "cardholderAuthenticationStatus": false,
    "paymentType": "SRCVISA"
  },
  "iss": "Flex/08",
  "paymentCredentialsReference": {
    "na_partner_ctp2": "U3lO1Flys1fcQmAWLzchn"
  },
  "exp": 1778665930,
  "type": "uc-1.0.0",
  "iat": 1778665030,
  "jti": "1E0T0CPF4S96D8P30Y89ID69U51WRHRWCTW896BX7K75ROSI6TMV6A0449CA2D1B",
  "content": {
    "clientReferenceInformation": {
      "applicationVersion": {},
      "applicationUser": {},
      "code": {},
      "applicationName": {}
    },
    "deviceInformation": {
      "fingerprintSessionId": {}
    },
    "processingInformation": {
      "paymentSolution": {
        "value": "027"
      }
    },
    "orderInformation": {
      "billTo": {
        "lastName": {},
        "country": {},
        "firstName": {},
        "phoneNumber": {},
        "address2": {},
        "address1": {},
        "postalCode": {},
        "locality": {},
        "buildingNumber": {},
        "administrativeArea": {},
        "email": {}
      },
      "amountDetails": {
        "totalAmount": {},
        "currency": {}
      },
      "shipTo": {
        "country": {},
        "firstName": {},
        "lastName": {},
        "address1": {},
        "postalCode": {},
        "locality": {},
        "buildingNumber": {},
        "administrativeArea": {}
      }
    },
    "paymentInformation": {
      "tokenizedCard": {
        "expirationYear": {
          "value": "2033"
        },
        "transactionType": {},
        "number": {
          "maskedValue": "XXXXXXXXXXXX3278",
          "bin": "432312"
        },
        "expirationMonth": {
          "value": "08"
        },
        "type": {
          "value": "001"
        },
        "cryptogram": {}
      },
      "card": {
        "typeSelectionIndicator": {
          "value": "1"
        },
        "useAs": {
          "value": "D"
        }
      }
    }
  }
}
```

{#uc-trans-tkn-ex_codeblock_bgat_cfz_hjc}  
Authentication Status in metadata Object  
The `cardholderAuthenticationStatus` object is included in the `metadata` and enables you to determine if the payload is fully authenticated. When `cardholderAuthenticationStatus` is set to `true`, the payload is fully authenticated. When `cardholderAuthenticationStatus` is set to `false`, the transaction is not authenticated.

```
"metadata": {
  "cardholderAuthenticationStatus": "true"
  }
}
```

{#uc-trans-tkn-ex_codeblock_fgt_cfz_hjc}

Token Verification {#ctp-tokens-verification}
=============================================

When you receive the transient token, you should cryptographically verify its integrity using the public key embedded within the capture context. Doing so verifies that `Cybersource` issued the token and that the data has not been tampered with in transit. Verifying the transient token JWT involves verifying the signature and various claims within the token. Programming languages each have their own specific libraries to assist. For an example in Java, see: [Java Example in Github](https://github.com/CyberSource/cybersource-unified-checkout-sample-java/blob/main/src/main/java/com/cybersource/example/service/JwtProcessorService.java "").

PAN BIN in metadata Object
--------------------------

The `cardDetails` object, including the PAN BIN, is included in the transient token `metadata` when a `Click to Pay` network token is used as a payment method. This allows you to display information about the card on invoices and see the BIN details that are linked to the underlying card.

```
"metadata": {
  "cardDetails": {
    "suffix": "9876",
    "prefix": "123456",
    "expirationMonth": "MM",
    "expirationYear": "YYYY"
  }
}
```

The `cardholderAuthenticationStatus` object is included in the `metadata` and enables you to determine if the payload is fully authenticated. When `cardholderAuthenticationStatus` is set to `true`, the payload is fully authenticated. When `cardholderAuthenticationStatus` is set to `false`, the transaction is not authenticated.

```
"metadata": {
  "cardholderAuthenticationStatus": "true"
  }
}
```

Dual-Branded Cards {#dual-co-brand-card-support}
================================================

`Unified Checkout` accepts dual-branded cards. To use this feature, you must include the card networks that have overlapping BIN ranges in the capture context request. For example:

```
"allowedCardNetworks": ["VISA", "MASTERCARD", "AMEX", "CARTESBANCAIRES"]
```

When a card number within an overlapping BIN range is entered, the network that is listed first in the value array for the allowedCardNetworks field is used. Based on the previous example, if the card number 403550XXXXXXXXXX is entered, the payment network for payment processing is Visa.  
During the transaction, the card type is populated with the first network in the list, and the detectedCardTypes field returned in the transient token includes all of the detected card types in the transient token.  
The detectedCardTypes field is returned in the transient token response only when more than one card type is detected.  
If you include Cartes Bancaires as a supported dual-branded card type, `Unified Checkout` displays a radio button with Visa and Mastercard options at checkout. This enables the customer to select which payment scheme they want to use to process the payment. The radio button defaults to the card type that you specify in the capture context request, but the payment is processed using the option that the customer selects during checkout.

Dual-Branded Cards {#ctp-dual-co-brand-card-support}
====================================================

`Unified Checkout` accepts dual-branded cards. To use this feature, you must include the card networks that have overlapping BIN ranges in the capture context request. For example:

```
"allowedCardNetworks": ["VISA", "MASTERCARD", "AMEX", "CARTESBANCAIRES"]
```

When a card number within an overlapping BIN range is entered, the network that is listed first in the value array for the allowedCardNetworks field is used. Based on the previous example, if the card number 403550XXXXXXXXXX is entered, the payment network for payment processing is Visa.  
During the transaction, the card type is populated with the first network in the list, and the detectedCardTypes field returned in the transient token includes all of the detected card types in the transient token.  
The detectedCardTypes field is returned in the transient token response only when more than one card type is detected.  
If you include Cartes Bancaires as a supported dual-branded card type, `Unified Checkout` displays a radio button with Visa and Mastercard options at checkout. This enables the customer to select which payment scheme they want to use to process the payment. The radio button defaults to the card type that you specify in the capture context request, but the payment is processed using the option that the customer selects during checkout.
