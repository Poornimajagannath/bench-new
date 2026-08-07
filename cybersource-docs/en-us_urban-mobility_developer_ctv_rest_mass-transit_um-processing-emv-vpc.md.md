Mass Transit Payment Services Using EMV and Card Data {#um-processing-emv-vpc}
==============================================================================

You can request these payment services for mass transit with EMV and card data:

* Authorization for account verification and debt recovery.
* Sale for aggregated fares and debt recovery.
* Stand-alone credit.  
  The EMV Data Elements and Tags table lists details about EMV tags that are mandatory (M), prohibited (P), optional (O), or conditional (C) for the processor. Send a conditional tag when it is present in the card and terminal.

|                 Data Element                 | EMV Tag | American Express | Discover PAYG  |       Mastercard PAYG        |    Relay MTT    |
|----------------------------------------------|---------|------------------|----------------|------------------------------|----------------|
| Transaction Date                             | 9A      | M                | M              | M                            | M              |
| Transaction Type                             | 9C      | M                | M              | M                            | M              |
| Transaction Currency Code                    | 5F2A    | M                | M              | M                            | M              |
| Terminal Country Code                        | 9F1A    | M                | M              | M                            | M              |
| Amount Authorized                            | 9F02    | M                | M              | M                            | M              |
| Amount Other                                 | 9F03    | M                | M              | M                            | M              |
| Application PAN Sequence Number              | 5F34    | M                | P              | C                            | O              |
| Application Transaction Counter (ATC)        | 9F36    | M                | M              | M                            | M              |
| Application Interchange Profile (AIP)        | 82      | M                | M              | M                            | M              |
| Dedicated File (DF) Name                     | 84      | M                | M              | M                            | M              |
| Terminal Verification Results (TVR)          | 95      | M                | M              | M                            | M              |
| Issuer Application Data                      | 9F10    | M                | M              | M                            | M              |
| Application Cryptogram                       | 9F26    | M                | M              | M                            | M              |
| Cryptogram Information Data (CID)            | 9F27    | M                | O              | M                            | O              |
| Terminal Capabilities                        | 9F33    | M                | M              | M                            | M              |
| Cardholder Verification Method (CVM) Results | 9F34    | O                | O              | M                            | O              |
| Unpredictable Number (UN)                    | 9F37    | M                | M              | M                            | M              |
| Form Factor Indicator                        | 9F6E    | C\*              | C              | O (Authorization) P (Refund) | C              |
| Mastercard Authenticated Application Data    | 9F60    | Does not apply   | Does not apply | O                            | Does not apply |
| Mastercard Kernel Identifier‐Terminal        | 96      | Does not apply   | Does not apply | O                            | Does not apply |
[EMV Data Elements and Tags]

\***Contactless American Express transactions**: If the Form Factor Indicator data is available on the card, then the merchant, acquirer, or processor must forward this information to the issuer.
