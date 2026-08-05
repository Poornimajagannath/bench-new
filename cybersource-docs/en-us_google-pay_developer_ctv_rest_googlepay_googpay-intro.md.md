Introduction {#googpay-intro}
=============================

You can use the `Cybersource` platform to process and manage Google Pay transactions.

Google Pay Overview
-------------------

Google Pay is a simple, secure in-app mobile and Web payment solution. You can choose `Cybersource` to process Google Pay transactions through all e-commerce channels.  
You can simplify your payment processing by allowing `Cybersource` to decrypt the payment data for you during processing.  
This method integrates simply and enables you to process transactions without seeing the payment network token and transaction data.

1. Using the Google API, request the customer's encrypted payment data.
2. Using the `Cybersource` API, construct and submit the authorization request, and include the encrypted payment data from the Google Pay callback.
3. `Cybersource` decrypts the encrypted payment data to create the payment network token and processes the authorization request.

