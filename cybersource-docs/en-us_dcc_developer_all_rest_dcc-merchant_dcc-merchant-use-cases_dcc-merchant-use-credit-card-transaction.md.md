DCC Credit Card Transaction {#dcc-merchant-use-credit-card-transaction}
=======================================================================

To process a DCC credit card transaction, follow these steps.

1. Send a DCC offer request.

   #### Step Result

   Receive the DCC offer response.

2. Determine if the purchase is eligible for DCC.

   #### ADDITIONAL INFORMATION

   If the purchase is not eligible for DCC or DCC processing is not available, proceed with the order in your local pricing currency. Do not perform the rest of this DCC procedure.  
   If the purchase is eligible for DCC, proceed to the next step.

3. Query the customer about using DCC to pay.

   #### ADDITIONAL INFORMATION

   If the purchase is eligible for DCC, you must get permission from the customer to proceed.  
   In your query, explain that the order is a candidate for DCC. Provide sufficient information for the customer to understand the total cost and make an informed decision. This includes:

   * The price in your local pricing currency and in the customer's billing currency, including currency symbols.
   * The exchange rate used to convert from the local pricing currency to the billing currency.
   * Information about additional commissions and fees that the customer must pay.
     {#dcc-merchant-use-credit-card-transaction_ul_lyf_jz4_vgc}  
     Contact your bank to learn more about the relevant payment card company rules and which information must be included.

   #### ADDITIONAL INFORMATION

   In addition to the information required by payment card company rules and your acquirer, you may also include additional information to help the customer understand DCC. This includes:

   * What DCC is
   * How DCC works
   * How the DCC price is calculated
     {#dcc-merchant-use-credit-card-transaction_ul_nsg_21p_vgc}

   #### ADDITIONAL INFORMATION

   End your query by asking if the customer would like to complete the order in the card's billing currency or in your local pricing currency.  
   To meet payment card company rules, you must present the customer with an active choice. This means that the customer must actively choose DCC. The DCC may not be performed by default.  
   Since the cardholder must explicitly choose to use DCC for the purchase, there are additional requirements you must meet in order to use DCC for recurring or subscription payments. Contact your acquirer for more information.

   #### Step Result

   Customer chooses the currency for the order.

4. Display a confirmation page.

   #### ADDITIONAL INFORMATION

   You can also send a transaction receipt to the customer.  
   The confirmation page and the receipt must include the DCC information required by the payment card company.  
   If the customer declines to use DCC, proceed with the order in your local pricing currency. Do not perform the rest of this DCC procedure.  
   If the customer chooses to use DCC, proceed to the next step.

5. Authorize the DCC payment.

   #### ADDITIONAL INFORMATION

   If you and your acquirer use Platform Connect (VPC) for processing, the orderInformation.amountDetails.originalAmount value must be in your local pricing currency. All other amounts for the order must be in the DCC payment currency. This includes the total DCC payment amount as well as any tax amounts, surcharge amounts, Level II amounts, and airline data amounts that you send to Cybersource.  
   For partial captures and refunds, use the exchange rate that you received in the DCC response to convert these amounts from your local pricing currency to the cardholder's billing currency.

