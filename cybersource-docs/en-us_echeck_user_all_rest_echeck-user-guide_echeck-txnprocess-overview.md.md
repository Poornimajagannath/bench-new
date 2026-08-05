Overview of eCheck Transaction Processing {#echeck-txnprocess-overview}
=======================================================================

This sequence describes eCheck transaction processing.

1. The merchant receives authorization from a customer to charge their bank account. The customer provides all of the required bank account information for the eCheck transaction type. After the transaction is submitted, purchase and payment information is securely transmitted to the Payment Gateway server. The transaction is accepted or rejected based on initial data validation and security criteria defined by `Cybersource`. Reasons for rejection include invalid routing number, inactive account number, and insufficient information.
2. If the transaction is accepted, `Cybersource` formats the transaction information and sends it as an ACH transaction to its bank, the Originating Depository Financial Institution (ODFI), with the rest of the transactions received that day.
3. The ODFI receives the transaction information and passes it to the ACH network for settlement. The ACH network uses the bank account information provided with the transaction to determine the bank that holds the customer's account, the Receiving Depository Financial Institution (RDFI).
4. The ACH network instructs the RDFI to charge the customer's account. The RDFI passes funds from the customer's account to the ACH network. The RDFI also notifies the ACH network of any administrative returns (funds could not be collected from the customer's bank account) or unauthorized returns (the customer disputes the purchase). An eCheck transaction might be returned for not sufficient funds (NSF), invalid account number, account closed, or account frozen. An eCheck transaction might be returned as unauthorized because the customer advised that it was not authorized, payment was stopped, or authorization was revoked. When a transaction is returned, `Cybersource` posts the return to the merchant.
5. The ACH network sends the funds to the ODFI (the bank associated with `Cybersource`).
6. The ODFI sends any returns to `Cybersource`.
7. After the funds holding period, `Cybersource` initiates a separate ACH transaction to deposit eCheck proceeds to the merchant's bank account.

