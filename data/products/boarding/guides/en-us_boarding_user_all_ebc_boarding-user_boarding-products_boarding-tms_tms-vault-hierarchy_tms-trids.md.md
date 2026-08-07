Token Requestor IDs {#tms-trids}
================================

A token requestor ID (TRID) is a unique identifier that entities such as merchants use to request network tokens from token providers. Having a TRID is a prerequisite for enabling network tokenization.  
Each entity must register with the token provider to get a TRID. Contact a `Cybersource` representative to enroll a merchant as a token requestor.

Visa and Mastercard TRIDs
-------------------------

An internal user can enroll a merchant as a VISA or Mastercard token requestor through the `Business Center`.  
Follow these steps to enroll a merchant as a token requestor in the `Business Center`:
1. Navigate to Token Management.

2. Click Vault Management.

3. Use the Vault Owner filter to search for the merchant account that has `TMS` enabled.

4. Choose the merchant account to view the `TMS` vaults that are configured for the merchant.

5. Click Network Tokenization.

6. Click Enroll to VISA/Mastercard token services.

7. Enter the required information for each card type:

   Mastercard
   :
   Business entity name

   Visa
   :
   Merchant name
   :
   Merchant website URL
   :
   Merchant country code

8. Click Onboard with Acquirer ID.

9. Enter the required information:

   Acquirer ID
   :
   Set the value to `40010052242`. It is a static acquirer ID that is used for `TMS`.

   Acquirer Merchant ID
   :
   Enter your organization ID.

10. Click Enroll to Network Token Services to complete enrollment.
    When the enrollment is submitted, the relationship ID and token requestor ID appear on the page for Visa Token Service (VTS) and the token requestor ID appears for Mastercard.  
    In order to request a TRID from the token provider, `Cybersource` uses merchant business details already stored. If any of the details are not present, a dialog form should appear prompting you to complete the missing information.

American Express TRIDs
----------------------

Enrollment as a token requestor for American Express is a manual process. Contact your `Cybersource` representative to request the TRID for American Express.  
Allow 2 to 3 days for the completion of your request.

> IMPORTANT
> **Service establishment (SE) Numbers** are required in order to process American Express card transactions.

