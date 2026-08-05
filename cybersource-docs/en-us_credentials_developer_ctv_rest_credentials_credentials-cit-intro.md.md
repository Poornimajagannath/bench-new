Customer-Initiated Transactions with Credentials on File {#credentials-cit-intro}
=================================================================================

A customer-initiated transaction (CIT) is a transaction initiated by the customer. There are two types of CITs:

* Customer transactions during which the credentials are stored for future **customer**-initiated transactions.
* Customer transactions during which the credentials are stored for future **merchant**-initiated transactions.

Customers can initiate a CIT at a merchant payment terminal, through an online purchase transaction, or by making a purchase using a previously stored credential. When storing cardholder data for a CIT, you must also include 3-D Secure authentication credentials to ensure that the CIT can successfully process. Authentication credentials can be stored for future use with the card credentials by doing a non-payment authentication (NPA).

`Business Center`
-----------------

You can create a new customer-initiated transaction in the `Business Center` by going to the One-Time Payments section and requesting a new authorization. When you have entered the customer's information, you can store the customer's credentials with the customer's permission in the Payment Information section. By doing so, you can perform merchant-initiated transactions for payments that the customer has pre-approved. For more information on how to perform a MIT in the `Business Center`, see [Merchant-Initiated No-Show Transactions with PAN](/docs/cybs/en-us/credentials/developer/ctv/rest/credentials/credentials-noshow-intro/credentials-mit-noshow-intro.md "").
