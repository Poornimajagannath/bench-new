AVS Codes {#avs-codes-intro}
============================

The AVS code is returned in the following field in the authorization response message:

* REST API: processorInformation.avs.code
* SCMP API: auth_auth_avs
* Simple Order API: ccAuthReply_avsCode
  {#avs-codes-intro_ul_vt1_fdv_rqb}

AVS Codes for `Cielo` 3.0 and `Payment Gateway Latin American Processing` {#avs-codes-cielo-latinamcc}
==================================================================================================

*`Payment Gateway Latin American Processing`* is the name of a specific processing connection that `Payment Gateway` supports. In the `Payment Gateway` API documentation, *`Payment Gateway Latin American Processing`* does not refer to the general topic of processing in Latin America.  
**Important Note About AVS Codes for `Cielo` 3.0 and `Payment Gateway Latin American Processing`:** CPF (Cadastro de Pessoas Fisicas) is required only for Redecard in Brazil.

| Code | Description                                                                                                                             |
|:-----|:----------------------------------------------------------------------------------------------------------------------------------------|
| D    | Partial match: postal code and address match.                                                                                           |
| E    | Not supported: AVS is not supported for this card type. `or` Invalid: the acquirer returned an unrecognized value for the AVS response. |
| F    | Partial match: postal code matches, but CPF and address do not match.                                                                   |
| G    | Not supported: AVS not supported or not verified.                                                                                       |
| I    | No match: AVS information is not available.                                                                                             |
| K    | Partial match: CPF matches, but postal code and address do not match.                                                                   |
| L    | Partial match: postal code and CPF match, but address does not match.                                                                   |
| N    | No match: postal code, CPF, and address do not match.                                                                                   |
| O    | Partial match: CPF and address match, but postal code does not match.                                                                   |
| R    | Not supported: your implementation does not support AVS. `or` System unavailable.                                                       |
| T    | Partial match: address matches, but postal code and CPF do not match.                                                                   |
| V    | Match: postal code, CPF, and address match.                                                                                             |
[AVS Codes for `Cielo` 3.0 and `Payment Gateway Latin American Processing`]

AVS Codes for `Platform Connect` {#avs-codes-ctv}
======================================================

> When you populate billing street address 1 and billing street address 2, ` Platform Connect ` concatenates the two values. If the concatenated value exceeds 40 characters, ` Platform Connect ` truncates the value at 40 characters before sending it to Relay and the issuing bank. Truncating this value affects AVS results and therefore might also affect risk decisions and chargebacks.

| Type of Codes               | Codes            |                                                                                                                                              Description                                                                                                                                              |
|:----------------------------|:-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| American Express Card Codes | --               | The American Express AVS codes are converted to Relay AVS codes before they are returned to you. As a result, you will not receive American Express AVS codes for the American Express card type.                                                                                                      |
| Domestic Relay Codes         | A, N, R, U, Y, Z | The alphabetic AVS codes is the Relay standard AVS codes. The standard AVS return codes for other types of payment cards, including American Express cards, are mapped to the Relay standard AVS codes. AVS is considered domestic when the bank that issued the customer's payment card is in the U.S. |
[Types of AVS Codes]

| Code | Description                                                                                                                                                                               |
|:-----|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A    | Partial match: street address matches, but 5-digit and 9-digit postal codes do not match.                                                                                                 |
| N    | No match: street address and postal code do not match.                                                                                                                                    |
| R    | System unavailable.                                                                                                                                                                       |
| U    | System unavailable: address information unavailable for one of these reasons: * The U.S. bank does not support AVS outside the U.S. * The AVS in a U.S. bank is not functioning properly. |
| Y    | Match: street address and 5-digit postal code match.                                                                                                                                      |
| Z    | Partial match: street address does not match, but 5-digit postal code matches.                                                                                                            |
[AVS Codes for `Platform Connect`]

AVS Codes for Other Processors {#avs-codes-other-processors}
============================================================

| Type of Codes                    | Codes                        |                                                                                                                                                                                                                                                                                                                                                                                    Description                                                                                                                                                                                                                                                                                                                                                                                    |
|:---------------------------------|:-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Codes for American Express Cards | F, H, K, L, O, T, V          | For American Express cards only. For American Express cards, you can receive Relay and `Payment Gateway` AVS codes in addition to the American Express AVS codes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| International Relay Codes         | B, C, D, G, I, M, P          | The international and domestic alphabetic AVS codes are the Relay standard AVS codes. The standard AVS return codes for other types of payment cards, including American Express cards, are mapped to the Relay standard AVS codes. AVS is considered either domestic or international, depending on the location of the bank that issued the customer's payment card: * The AVS is domestic when the bank is in the U.S. * The AVS is international when the bank is outside the U.S. You should be prepared to handle domestic and international AVS result codes: * For international cards, you can receive domestic AVS codes in addition to the international AVS codes. * For domestic cards, you can receive international AVS codes in addition to the domestic AVS codes. |
| Domestic Relay Codes              | A, E, N, R, S, U, W, X, Y, Z | The international and domestic alphabetic AVS codes are the Relay standard AVS codes. The standard AVS return codes for other types of payment cards, including American Express cards, are mapped to the Relay standard AVS codes. AVS is considered either domestic or international, depending on the location of the bank that issued the customer's payment card: * The AVS is domestic when the bank is in the U.S. * The AVS is international when the bank is outside the U.S. You should be prepared to handle domestic and international AVS result codes: * For international cards, you can receive domestic AVS codes in addition to the international AVS codes. * For domestic cards, you can receive international AVS codes in addition to the domestic AVS codes. |
| Payment Gateway Codes                | 1, 2, 3, 4                   | The numeric AVS codes are created by `Payment Gateway` and are not standard Relay codes. These AVS codes can be returned for any card type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
[Types of AVS Codes]

| Code   | Description                                                                                                                                                                                          |
|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A      | Partial match: street address matches, but five-digit and nine-digit postal codes do not match.                                                                                                      |
| B      | Partial match: street address matches, but postal code is not verified. Returned only for Relay cards not issued in the US.                                                                           |
| C      | No match: street address and postal code do not match. Returned only for Relay cards not issued in the US.                                                                                            |
| D \& M | Match: street address and postal code match. Returned only for Relay cards not issued in the US.                                                                                                      |
| E      | Invalid: AVS data is invalid, or AVS is not allowed for this card type.                                                                                                                              |
| F      | Partial match: card member's name does not match, but billing postal code matches.                                                                                                                   |
| G      | Not supported: issuing bank outside the US does not support AVS.                                                                                                                                     |
| H      | Partial match: card member's name does not match, but street address and postal code match. Returned only for the American Express card type.                                                        |
| I      | No match: address not verified. Returned only for Relay cards not issued in the US.                                                                                                                   |
| K      | Partial match: card member's name matches, but billing address and billing postal code do not match. Returned only for the American Express card type.                                               |
| L      | Partial match: card member's name and billing postal code match, but billing address does not match. Returned only for the American Express card type.                                               |
| M      | See the entry for D \& M.                                                                                                                                                                            |
| N      | No match: one of the following: * Street address and postal code do not match. * Card member's name, street address, and postal code do not match. Returned only for the American Express card type. |
| O      | Partial match: card member's name and billing address match, but billing postal code does not match. Returned only for the American Express card type.                                               |
| P      | Partial match: postal code matches, but street address not verified. Returned only for Relay cards not issued in the US.                                                                              |
| R      | System unavailable.                                                                                                                                                                                  |
| S      | Not supported: issuing bank in the US does not support AVS.                                                                                                                                          |
| T      | Partial match: card member's name does not match, but street address matches. Returned only for the American Express card type.                                                                      |
| U      | System unavailable: address information unavailable for one of these reasons: * The US bank does not support AVS outside the US. * The AVS in a US bank is not functioning properly.                 |
| V      | Match: card member's name, billing address, and billing postal code match. Returned only for the American Express card type.                                                                         |
| W      | Partial match: street address does not match, but nine-digit postal code matches.                                                                                                                    |
| X      | Match: street address and nine-digit postal code match.                                                                                                                                              |
| Y      | Match: street address and five-digit postal code match.                                                                                                                                              |
| Z      | Partial match: street address does not match, but five-digit postal code matches.                                                                                                                    |
| 1      | Not supported: one of the following: * AVS is not supported for this processor or card type. * AVS is disabled for your account. To enable AVS, contact customer support.                            |
| 2      | Unrecognized: the processor returned an unrecognized value for the AVS response.                                                                                                                     |
| 3      | Match: address is confirmed. Returned only for PayPal Express Checkout.                                                                                                                              |
| 4      | No match: address is not confirmed. Returned only for PayPal Express Checkout.                                                                                                                       |
| 5      | No match: no AVS code was returned by the processor.                                                                                                                                                 |
[AVS Codes]

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Payment Gateway for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Payment Gateway.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE CARD PLATFORM CONNECT ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT CARD PLATFORM CONNECT ACQUIRER.
