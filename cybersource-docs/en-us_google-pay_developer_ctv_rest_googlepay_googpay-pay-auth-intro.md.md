Google Pay Authorizations {#googpay-pay-auth-intro}
===================================================

This section shows you how to make a successful authorization request.  
After you send the request, check the response messages to make sure that the request was successful. A 200-level HTTP response code indicates success.  
For information about response codes, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md ""). .

Follow-on Transactions
----------------------

After the initial transaction is complete, additional follow-on transactions can be made as Merchant-Initiated Transactions (MITs).  
For more information on how to process MITs, see [Merchant-Initiated Transactions](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/credentials/credentials-mit-intro.md "").

Endpoint {#googpay-pay-auth-intro_d9e16}
----------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#googpay-pay-auth-intro_d9e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#googpay-pay-auth-intro_d9e35}
