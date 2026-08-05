PAX All-in-One Payment Services {#pax-aio-payment-txn-intro}
============================================================

Use this information to process PAX All-in-One Solution payment services.

Sale {#pax-aio-payment-txn-sale-task}
=====================================

Use this information to process a sale. This transaction combines an authorization and a capture into a single transaction.  
Follow these steps to process a sale.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
    
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
4. Get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.  
    

   ```
   val transactionObject = mposUi.latestTransaction
   ```

 

Refund {#pax-aio-payment-txn-refund-task}
=========================================

Use this information to process a refund by referencing the original transaction. You can issue refunds for either the full amount or a partial amount of the original transaction.  
Stand-alone credits are also supported and can be processed independently of a previous transaction. For more information, see [Stand-Alone Credit](/docs/cybs/en-us/pax-all-in-one/integration/all/na/pax-all-in-one/pax-aio-payment-txn-intro/pax-aio-payment-txn-standalone-credit-task.md "").  
Follow these steps to process a refund.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder() 
               .refund("transactionIdentifier") 
            // Specify amount and currency for partial refunds 
            // .amountAndCurrency(BigDecimal("1.00"), Currency.EUR)
               .build() 

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters) 
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) { 
       super.onActivityResult(requestCode, resultCode, data) 
     
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) { 
           when (resultCode) { 
               // Result code from a successful transaction 
               MposUi.RESULT_CODE_APPROVED -&gt; { 
           val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRAN
   SACTION_IDENTIFIER) 
           Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier",  
   Toast.LENGTH_LONG).show() 
               } 
              // Result code from a declined, aborted or failed transaction 
             MposUi.RESULT_CODE_FAILED -&gt; { 
           Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed",  
   Toast.LENGTH_LONG).show() 
               } 
           } 
       } 
   }
   ```
4. Get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.  
    

   ```
   val transactionObject = mposUi.latestTransaction
   ```

 

Stand-Alone Credit {#pax-aio-payment-txn-standalone-credit-task}
================================================================

Use this information to process a stand-alone credit. This transaction enables you to issue a credit without referencing a previous transaction. The customer must present their payment card.
When processing a stand-alone credit, there is no limit on the credit amount because the transaction does not reference the original purchase. To help manage risk, it is recommended to use a refund transaction whenever possible. For more information, see [Refund](/docs/cybs/en-us/pax-all-in-one/integration/all/na/pax-all-in-one/pax-aio-payment-txn-intro/pax-aio-payment-txn-refund-task.md "").  
Follow these steps to process a stand-alone credit.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder() 
               .refund(BigDecimal("1.00"), Currency.EUR)     
               .customIdentifier("yourReferenceForTheTransaction")  
               .build() 
    
   val transactionIntent = mposUi.createTransactionIntent(transactionParameters) 
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
       super.onActivityResult(requestCode, resultCode, data)
    
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
              // Result code from a successful transaction
              MposUi.RESULT_CODE_APPROVED -&gt; {    
                 val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                 Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", 
   Toast.LENGTH_LONG).show()
              }
              // Result code from a declined, aborted or failed transaction
              MposUi.RESULT_CODE_FAILED -&gt; {
                 Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", 
   Toast.LENGTH_LONG).show()
              }
           }
       }
   }
   ```
4. Get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.  
    

   ```
   val transactionObject = mposUi.latestTransaction
   ```

 

Check Transaction Status {#pax-aio-payment-txn-check-txn-status-task}
=====================================================================

Use this information to request a check transaction status. This transaction enables you to retrieve response data for a transaction that was lost or timed out. You must have the `transactionIdentifier` value for the transaction that you want to check. When the check transaction status request is complete, the transaction details show on the Summary screen.  
Follow these steps to request a check transaction status.

1. Access the `transactionIdentifier` value in the `onActivityResult` method of the original transaction.

2. Retrieve the transaction `summaryIntent` value from the `mposUi` object.

3. Use the `startActivity` method to initiate the Summary screen.

   ```
   val summaryIntent = mposUi.createTransactionSummaryIntent(transactionIdentifier = "transactionIdentifier")
   startActivityForResult(summaryIntent, MposUi.REQUEST_CODE_SHOW_SUMMARY)
   ```
4. After the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
       // Result code from closing the summary screen
       if (resultCode == MposUi.RESULT_CODE_SUMMARY_CLOSED) {
           // Accessing status from the transaction that was just queried
           val transactionStatus = mposUi.latestTransaction?.status
           Toast.makeText(activity, "Summary closed. Transaction status: $transactionStatus", Toast.LENGTH_SHORT).show()  
       }
   }
   ```
5. Get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.  
    

   ```
   val transactionObject = mposUi.latestTransaction
   ```

 

Token Refund {#pax-aio-payment-txn-token-refund-task}
=====================================================

To process a credit through a token, you must have the `Token Management Service` product enabled and an existing (saved) token from a tokenized transaction. For more information, see [Token Management Service](https://developer.cybersource.com/docs/cybs/en-us/tms/developer/ctv/rest/tms/tms-overview.md ""). Use this information to process a token refund. This transaction enables you to process a stand-alone credit for a tokenized card.  
Follow these steps to process a token refund.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Create an `accountParameters` object and set the `instrumentIdentifierID` from the original transaction's metadata as the `shopperAccountIdentifier`.

3. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .refund(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .build()

   val accountParameters = AccountParameters.Builder().token().cybersource().shopperAccountIdentifier("instrumentIdentifierID").build();

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters, null, accountParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   Override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
    
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. Get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Pre-Authorization {#pax-aio-payment-txn-pre-auth-task}
======================================================

Use this information to process a pre-authorization for an initial amount. A pre-authorization transaction places a temporary hold on the customer's payment card. The transaction amount can be captured at a later time.  
Most authorizations expire within 5 to 7 days, as determined by the issuing bank. When an authorization expires, your bank, the issuing bank, or payment processor might require you to resubmit the authorization request and include a capture request in the same message. For more information, see [Capture](/docs/cybs/en-us/pax-all-in-one/integration/all/na/pax-all-in-one/pax-aio-payment-txn-intro/pax-aio-payment-txn-capture-task.md "").  
To help ensure successful transaction processing, monitor authorization timelines and use combined authorization and capture requests when necessary.  
Follow these steps to process a pre-authorization.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` value from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .autoCapture(false)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   Override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
    
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
4. Get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Incremental Authorization {#pax-aio-payment-txn-incremental-auth-task}
======================================================================

Use this information to process an incremental authorization. An incremental authorization is used after an approved pre-authorization to increase the authorized amount before capture.  
Follow these steps to process an incremental authorization.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` value from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder() 
               .incrementalAuthorization("transactionIdentifier") 
               .amountAndCurrency(BigDecimal("1.00"), Currency.EUR) 
               .build() 

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters) 
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   Override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) { 
       super.onActivityResult(requestCode, resultCode, data) 
     
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) { 
           when (resultCode) { 
               // Result code from a successful transaction 
               MposUi.RESULT_CODE_APPROVED -&gt; { 
                   val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRAN
   SACTION_IDENTIFIER) 
                   Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier",  
   Toast.LENGTH_LONG).show() 
               } 
               // Result code from a declined, aborted or failed transaction 
               MposUi.RESULT_CODE_FAILED -&gt; { 
           Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed",  
   Toast.LENGTH_LONG).show() 
               } 
           } 
       } 
   }
   ```
4. Get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Capture {#pax-aio-payment-txn-capture-task}
===========================================

Use this information to capture a pre-authorized transaction. The capture request references the approved pre-authorization request.  
Follow these steps to process a capture.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
              .capture("transactionIdentifier") 
           // Specify amount and currency for partial captures
           // .amountAndCurrency(BigDecimal("1.00"), Currency.EUR)
              .build() 

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters) 
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information returns information about the last transaction.

   ```
   Override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) { 
       super.onActivityResult(requestCode, resultCode, data) 
     
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) { 
           when (resultCode) { 
               // Result code from a successful transaction 
               MposUi.RESULT_CODE_APPROVED -&gt; { 
           val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRAN
   SACTION_IDENTIFIER) 
           Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier",  
   Toast.LENGTH_LONG).show() 
               } 
               // Result code from a declined, aborted or failed transaction 
               MposUi.RESULT_CODE_FAILED -&gt; {     
           Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed",  
   Toast.LENGTH_LONG).show() 
               } 
           } 
       } 
   }
   ```
4. Get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Account Verification {#pax-aio-payment-txn-acct-verif-task}
===========================================================

Use this information to process an account verification. This transaction submits a zero-amount authorization request to validate the payment card.  
Follow these steps to process an account verification.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .verification(Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered, which returns information about the last transaction.

   ```
   Override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
    
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),”Transaction approved!\nIdentifier: $transactionIdentifier”, Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), “Transaction was declined, aborted, or failed”, Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
4. Get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Mail Order or Telephone Order {#pax-aio-payment-txn-moto-sale-task}
===================================================================

Use this information to process a mail order or telephone order (MOTO) sale and other transactions. This is a card-not-present transaction so the customer does not present the payment card at the terminal.
Instructions for processing various MOTO transaction types are shown in step 2 of the code example.  
Follow these steps to process a MOTO transaction.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               // Use for Sale
               .charge(BigDecimal("1.00"), Currency.EUR)
               // Use for Account Verification
               // .verification(Currency.EUR)      
               .customIdentifier("yourReferenceForTheTransaction")
               // Use for Pre-Authorization
               // .autoCapture(false)
               .workflow(new WorkflowConfiguration.Builder()
                     .moto()
                     // Set to false to toggle CVV as optional
                     .cvvRequired(true)
                     // Set to false to toggle address as optional 
                     .addressRequired(true)
                     // Set to true to show transaction review screen
                     .reviewRequired(false)
                     .build())
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   Override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
    
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),”Transaction approved!\nIdentifier: $transactionIdentifier”, Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), “Transaction was declined, aborted, or failed”, Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
4. Get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Airline Details {#pax-aio-pymnt-txn-sale-airline-details}
===================================================================

Use this information to process a sale with airline details. This transaction includes required airline details and related service details in the payment request.  
Follow these steps to process a sale with airline details.

1. Create an `AdditionalDetails` object and set one or more airline (`airlineDetails`) fields and related service (`ancillaryDetails`) fields.

   ```
   val airlineDetails = AdditionalDetailsBuilder()
           .airlineDetails(
               AirlineDetailsBuilder()
                   .agentCode("AGT12345")
                   .agentName("Visa Travel")
                   .arrivalDate(SimpleDateFormat("MMddyyyy", Locale.US).parse("01202024"))
                   .carrierName("Visa Airways")
                   .clearingCount(1)
                   .clearingSequence("1")
                   .creditReasonIndicator(CreditReasonIndicator.OTHER)
                   .customerCode("CORP12345")
                   .documentType(DocumentType.AIRLINE)
                   .electronicTicket(true)
                   .exchangeTicketAmount(BigDecimal("0.00"))
                   .exchangeTicketFee(BigDecimal("0.00"))
                   .firstName("John")
                   .lastName("Doe")
                   .numberOfPassengers("1")
                   .passengerName("John Doe")
                   .planNumber("01")
                   .purchaseType(PurchaseType.TICKET)
                   .reservationSystem("00001")
                   .restrictedTicketIndicator(RestrictedTicketIndicator.NONREFUNDABLE)
                   .ticketIssueDate(SimpleDateFormat("yyyyMMdd", Locale.US).parse("20240115"))
                   .ticketIssuerAddress("1 Market St")
                   .ticketIssuerCity("San Francisco")
                   .ticketIssuerCode("UA")
                   .ticketNumber("0141234567890")
                   .ticketRestrictionText("00000")
                   .ticketUpdateIndicator(TicketUpdateIndicator.NEW)
                   .totalClearingAmount("450.00")
                   .totalFee(BigDecimal("25.00"))
                   .addLegDetails(
                       listOf(
                           LegDetailsBuilder()
                               .arrivalTime("1230")
                               .arrivalTimeSegment(TimeSegment.PM)
                               .carrierCode("UA")
                               .legClass("Y")
                               .conjunctionTicket("0141234567891")
                               .couponNumber("1")
                               .departureDate(SimpleDateFormat("yyyyMMdd", Locale.US).parse("20240115"))
                               .departureTime("0930")
                               .departureTimeSegment(TimeSegment.AM)
                               .destination("JFK")
                               .endorsementsRestrictions("NONREF")
                               .exchangeTicket("0141234567892")
                               .fare(BigDecimal("450.00"))
                               .fareBasis("Y26")
                               .fee(BigDecimal("25.00"))
                               .flightNumber("1234")
                               .originatingAirportCode("SFO")
                               .stopoverCode(StopoverCode.NO_STOPOVER)
                               .tax(BigDecimal("38.00"))
                       )
                   )
                   .build()
           )
           .ancillaryDetails(
               AncillaryDetailsBuilder()
                   .connectedTicketNumber("0149876543210")
                   .creditReasonIndicator(CreditReasonIndicator.OTHER)
                   .feeDescription("Checked baggage")
                   .passengerName("Jane Doe")
                   .ticketNumber("0141234567890")
                   .addServiceDetails(
                       listOf(
                           ServiceDetailsBuilder()
                               .categoryCode("BAGO")
                               .subcategoryCode("CHKD")
                               .feeAmount(BigDecimal("35.00"))
                               .feeCode("0DB")
                       )
                   )
                   .build()
           )
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)
               .customIdentifier("yourReferenceForTheTransaction")
               .additionalDetails(airlineDetails)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?)
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. Get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Auto Rental Details {#pax-aio-pymnt-txn-sale-auto-rental-details}
===========================================================================

Use this information to process a sale with auto rental details. This transaction includes required auto rental details in the payment request.  
Follow these steps to process a sale with auto rental details.

1. Create an `AdditionalDetails` object and set one or more of the auto rental fields.

   ```
   val autoRentalDetails = AdditionalDetailsBuilder()
           .autoRentalDetails(
               // Set value of the builder to the number of rental days
               AutoRentalDetailsBuilder("5")
                   .pickUpState("CA")
                   .pickUpTime(SimpleDateFormat("HHmmss", Locale.US).parse("093000"))
                   .programCode("01")
                   .ratePerMile(BigDecimal("0.25"))
                   .regularMileageCost(BigDecimal("50.00"))
                   .rentalAddress("1 Market St")
                   .rentalLocationID("LOC001")
                   .renterName("Bob Smith")
                   .returnCity("Los Angeles")
                   .returnCountry("USA")
                   .returnDate(SimpleDateFormat("MMddyyyy", Locale.US).parse("01202024"))
                   .returnLocation("LAX Terminal 1")
                   .returnLocationID("LOC002")
                   .returnState("CA")
                   .specialProgramCode(SpecialProgramCode.NONE)
                   .taxAmount(BigDecimal("18.50"))
                   .taxIndicator(true)
                   .taxRate(BigDecimal("0.08"))
                   .taxStatusIndicator("Y")
                   .taxSummary("18.50")
                   .taxType("VAT")
                   .timePeriod(TimePeriod.DAILY)
                   .towingCharge(BigDecimal("0.00"))
                   .vehicleIdentificationNumber("1FTSW21P34EB12345")
                   .vehicleInsuranceIndicator(true)
                   .vehicleMake("Ford")
                   .vehicleModel("Focus")
                   .weeklyRentalRate(BigDecimal("280.00"))
                   .promotion(
                       PromotionDetailsBuilder()
                           .code("PROMO2024")
                           .additionalCode("WKND10")
                   )
                   .build()
           )
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)
               .customIdentifier("yourReferenceForTheTransaction")
               .additionalDetails(autoRentalDetails)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?)
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. Get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Billing and Shipping Details {#pax-aio-pymnt-txn-sale-bill-ship-details}
==================================================================================

Use this information to process a sale with billing and shipping details. This transaction includes required billing and shipping details in the payment request.  
Follow these steps to process a sale with billing and shipping details.

1. Create an `AdditionalDetails` object and set one or more of the billing and shipping fields.

   ```
   val billingAndShippingDetails = AdditionalDetailsBuilder()
           .billingDetails(
               BillingDetailsBuilder()
                   .firstName("Alice")
                   .middleName("M")
                   .lastName("Smith")
                   .title("Ms.")
                   .company("Visa Inc.")
                   .companyTaxID("123456789")
                   .street1("123 Main St")
                   .city("San Francisco")
                   .state("CA")
                   .postalCode("94105")
                   .country("US")
                   .email("alice@example.com")
                   .phoneNumber("14155550123")
                   .customerID("CUST12345")
                   .personalID("PID1234567890")
                   .ipAddress("192.0.2.1")
                   .hostname("host.example.com")
                   .comments("VIP customer")
                   .build()
           )
           .shippingDetails(
               ShippingDetailsBuilder()
                   .firstName("Bob")
                   .lastName("Jones")
                   .company("Visa Inc.")
                   .street1("500 Market St")
                   .city("New York")
                   .state("NY")
                   .postalCode("10001")
                   .country("US")
                   .phoneNumber("12125550188")
                   .build()
           )
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)
               .customIdentifier("yourReferenceForTheTransaction")
               .additionalDetails(billingAndShippingDetails)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?)
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. Get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Installment Details {#pax-aio-payment-txn-sale-installment-details-task}
==================================================================================

Use this information to process a sale with installment details. This transaction includes the required installment payment details in the payment request.
This transaction is available only in the Latin American and Caribbean (LAC) region.  
Follow these steps to process a sale with installment details.

1. Create an `InstallmentDetails` object and set one ore more of the installment fields.

   ```
   // Set value of the builder to the number of installments
   val installmentDetails = InstallmentDetailsBuilder(5)
           // Set to PlanType.ISSUER_FUNDED for issuer funded plans
           .planType(PlanType.MERCHANT_FUNDED)
           .includesInterest(true)
           .governmentPlan(true)
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .installmentDetails(installmentDetails)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
    
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. Get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Lodging Details {#pax-aio-pymnt-txn-sale-lodging-details}
===================================================================

Use this information to process a sale with lodging details. This transaction includes required lodging details in the payment request.  
Follow these steps to process a sale with lodging details.

1. Create an `AdditionalDetails` object and set one or more lodging fields.

   ```
   val lodgingDetails = AdditionalDetailsBuilder()
           .lodgingDetails(
               // Set value of the builder to the duration of stay
               LodgingDetailsBuilder(3)
                   .checkInDate("030125")
                   .checkOutDate("030425")
                   .guestSmokingPreference("N")
                   .numberOfGuests(2)
                   .numberOfRoomsBooked(1)
                   .guestName("John Doe")
                   .roomLocation("Ocean View")
                   .roomTaxElements("VAT")
                   .roomBedType("KING")
                   .roomRateType("CORPORATE")
                   .specialProgramCode("1")
                   .dailyRoomRate1(BigDecimal("150.00"))
                   .dailyRoomRate2(BigDecimal("160.00"))
                   .dailyRoomRate3(BigDecimal("170.00"))
                   .roomNights1(1)
                   .roomNights2(1)
                   .roomNights3(1)
                   .corporateClientCode("CORP123456")
                   .promotionalCode("PROMO2025")
                   .additionalCoupon("DISCOUNT10")
                   .travelAgencyCode("TA789")
                   .travelAgencyName("Premium Travel Agency")
                   .customerServicePhoneNumber("1-800-555-0199")
                   .tax(BigDecimal("45.00"))
                   .prepaidCost(BigDecimal("200.00"))
                   .foodAndBeverageCost(BigDecimal("125.00"))
                   .roomTax(BigDecimal("30.00"))
                   .adjustmentAmount(BigDecimal("15.00"))
                   .phoneCost(BigDecimal("8.00"))
                   .restaurantCost(BigDecimal("95.00"))
                   .roomServiceCost(BigDecimal("40.00"))
                   .miniBarCost(BigDecimal("25.00"))
                   .laundryCost(BigDecimal("18.00"))
                   .miscellaneousCost(BigDecimal("12.00"))
                   .giftShopCost(BigDecimal("35.00"))
                   .movieCost(BigDecimal("10.00"))
                   .healthClubCost(BigDecimal("20.00"))
                   .valetParkingCost(BigDecimal("30.00"))
                   .cashDisbursementCost(BigDecimal("5.00"))
                   .nonRoomCost(BigDecimal("40.00"))
                   .businessCenterCost(BigDecimal("15.00"))
                   .loungeBarCost(BigDecimal("55.00"))
                   .transportationCost(BigDecimal("75.00"))
                   .gratuityCost(BigDecimal("45.00"))
                   .conferenceRoomCost(BigDecimal("120.00"))
                   .audioVisualCost(BigDecimal("65.00"))
                   .banquetCost(BigDecimal("180.00"))
                   .internetAccessCost(BigDecimal("12.00"))
                   .earlyCheckOutCost(BigDecimal("20.00"))
                   .nonRoomTax(BigDecimal("25.00"))
                   .build()
           )
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)
               .customIdentifier("yourReferenceForTheTransaction")
               .additionalDetails(lodgingDetails)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?)
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. Get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Merchant-Defined Data Details {#pax-aio-pymnt-txn-sale-merch-defined-data-details}
============================================================================================

Use this information to process a sale with merchant-defined data details. This transaction includes required merchant-defined data details in the payment request.  
Follow these steps to process a sale with merchant-defined data details.

1. Create an `AdditionalDetails` object and set one or more merchant-defined data fields.

   ```
   val mddDetails = AdditionalDetailsBuilder()
           .mddDetails(
               MddDetailsBuilder()
                   .field1("value1")
                   .field2("value2")
                   .field3("value3")
                   .field4("value4")
                   .field5("value5")
                   .field6("value6")
                   .field7("value7")
                   .field8("value8")
                   .field9("value9")
                   .field10("value10")
                   .field11("value11")
                   .field12("value12")
                   .field13("value13")
                   .field14("value14")
                   .field15("value15")
                   .field16("value16")
                   .field17("value17")
                   .field18("value18")
                   .field19("value19")
                   .field20("value20")
                   .build()
           )
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)
               .customIdentifier("yourReferenceForTheTransaction")
               .additionalDetails(mddDetails)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?)
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. Get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with On-Reader Tipping {#pax-aio-payment-txn-sale-on-reader-tip-task}
==========================================================================

Use this information to process a sale with on-reader tipping. At the start of each transaction, the terminal prompts the customer to add a tip by showing suggested tip amounts. The customer chooses or enters a tip amount on the terminal before presenting their payment card.  
Follow these steps to process a sale with on-reader tipping.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Create a `TippingProcessStepParameters` object to configure the tipping function. The tipping options are percentage choice, tip amount, and total amount.

3. Create a `TransactionProcessParameters` object to add the tipping step.

4. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)
               .customIdentifier("yourReferenceForTheTransaction")
               .build()
    
   //  Use to display three tipping percentage choices
   val tipStep = TippingProcessStepParameters.Builder()
               .askForPercentageChoice()
           //  Optional to configure tipping percentages | Default values = 10, 15, 20
           //  .percentages(BigDecimal("10"), BigDecimal("20"), BigDecimal("30"))
           //  Optional to show confirmation screen
           //  .showTotalAmountConfirmationScreen(true)
               .build()
    
   //  Use to ask for tip amount
   //  val tipStep = TippingProcessStepParameters.Builder()
           //  .askForTipAmount()
           //  Optional to show confirmation screen
           //  .showTotalAmountConfirmationScreen(true)
           //  .build()
    
   //  Use to ask for total transaction amount including tip
           //  val tipStep = TippingProcessStepParameters.Builder()
           //  .askForTotalAmount()
           //  Optional to show confirmation screen
           //  .showTotalAmountConfirmationScreen(true)
           //  .build()
    
   val processParameters = TransactionProcessParameters.Builder()
       .addStep(tipStep)
       .build()
    
   val transactionIntent = mposUi.createTransactionIntent(transactionParameters, processParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
5. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   Override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
    
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), “Transaction was declined, aborted, or failed”, Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
6. Get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with On-Receipt Tipping {#pax-aio-payment-txn-sale-on-receipt-tip-intro}
=============================================================================

Use this information to process a sale with on-receipt tipping. After the original transaction amount is pre-authorized, the customer writes the tip or total amount on the printed receipt. A follow-on tip adjust request must be sent within 24 hours to capture the transaction. For more information, see [Tip Adjust](/docs/cybs/en-us/pax-all-in-one/integration/all/na/pax-all-in-one/pax-aio-payment-txn-intro/pax-aio-payment-txn-sale-on-receipt-tip-intro/pax-aio-pymnt-txn-tip-adj-onreceipt-sale-intro.md "").
By using this feature, you assume the risk of the overcapture being declined and increased chargebacks. Only use this feature when required. The recommendation is to process a sale with on-reader tipping whenever possible. For more information, see [Sale with On-Reader Tipping](/docs/cybs/en-us/pax-all-in-one/integration/all/na/pax-all-in-one/pax-aio-payment-txn-intro/pax-aio-payment-txn-sale-on-reader-tip-task.md "").

Process a Sale with On-Receipt Tipping {#pax-aio-payment-txn-sale-on-receipt-tip-task}
======================================================================================

After completing a sale with on-receipt tipping transaction, a follow-on tip adjust request must be sent within 24 hours to capture the transaction. For more information, see [Tip Adjust](/docs/cybs/en-us/pax-all-in-one/integration/all/na/pax-all-in-one/pax-aio-payment-txn-intro/pax-aio-payment-txn-sale-on-receipt-tip-intro/pax-aio-pymnt-txn-tip-adj-onreceipt-sale-intro.md ""). Follow these steps to process a sale with on-receipt tipping.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("50.00"), Currency.USD)    
               .customIdentifier("yourReferenceForTheTransaction")
               .autoCapture(false)
               .TipAdjustable(true)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
    
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
4. Get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.  
    

   ```
   val transactionObject = mposUi.latestTransaction
   ```

 

Tip Adjust {#pax-aio-pymnt-txn-tip-adj-onreceipt-sale-intro}
============================================================

Use this information to process a tip adjust. This is a required follow-on transaction after processing a sale with on-receipt tipping. The tip adjust request must be sent within 24 hours to capture the transaction.  
After the original sale transaction is pre-authorized, the customer writes the tip or total amount on the printed receipt. The tip adjust request must be submitted with the tip amount or with `0`, if no tip was provided. The tip adjust amount is limited to 20% of the original transaction amount. Requests for higher amounts will be rejected. A follow-on tip adjust request is then sent to capture the additional tip amount. This transaction is also called an *overcapture*.  
For more information, see [Sale with On-Receipt Tipping](/docs/cybs/en-us/pax-all-in-one/integration/all/na/pax-all-in-one/pax-aio-payment-txn-intro/pax-aio-payment-txn-sale-on-receipt-tip-intro.md "").

Process a Tip Adjust {#pax-aio-pymnt-txn-tip-adj-onreceipt-sale-task}
=====================================================================

Follow these steps to process a tip adjust.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
              .adjustTip("transactionIdentifier", BigDecimal("10.00"), Currency.USD) 
              .build() 

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters) 
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
    
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
4. Get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Payment Facilitator Details {#pax-aio-payment-txn-sale-payment-facilitator-task}
==========================================================================================

Use this information to process a sale with payment facilitator details. This transaction includes the required payment facilitator details in the payment request.  
Follow these steps to process a sale with payment facilitator details.

1. Create a `MerchantDetails` object and set one ore more of the payment facilitator fields.

   ```
   val merchantDetails = MerchantDetailsBuilder()
           .salesOrganizationId("12345")
           .subMerchantId("SM67890")
           .merchantDescriptor("ExampleMerchant")
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .merchantDetails(merchantDetails)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
    
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. Get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Tax Details {#pax-aio-payment-txn-sale-tax-details-task}
==================================================================

Use this information to process a sale with tax details. This type of transaction can be used to include required tax details as part of the transaction.  
Follow these steps to process a sale with tax details.

1. Create a `TaxDetails` object and set one ore more of the tax fields.

   ```
   val taxDetails = TaxDetailsBuilder()
           .merchantTaxId("TaxID1234")
           .salesSlipNumber(12345678)
           .includedTaxAmount(BigDecimal("5.00"))
           .includedLocalTaxAmount(BigDecimal("1.00"))
           .includedNationalTaxAmount(BigDecimal("2.00"))
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .taxDetails(taxDetails)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
    
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. Get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Offline Transactions {#pax-aio-pymnt-txn-offline-intro}
=======================================================

Use this information to process offline sale or refund transactions when internet connectivity is unavailable.
Using offline transaction functionality involves risk. Because these transactions are not authorized in real time, you assume responsibility for potential issues such as failed transactions, increased fraud, and higher chargeback rates. Only use offline transactions when necessary such as during temporary internet outages. Whenever possible, it is recommended to process online sale transactions to ensure secure and immediate authorization. For more information, see [Sale](/docs/cybs/en-us/pax-all-in-one/integration/all/na/pax-all-in-one/pax-aio-payment-txn-intro/pax-aio-payment-txn-sale-task.md "").  
Review these considerations before performing offline transactions:

* Contactless transactions are not supported for offline sales.
* A terminal must have successfully processed at least one online transaction before it can perform offline transactions.
* Offline transactions must be submitted for authorization once internet connectivity is restored. For more information, see [Submit an Offline Transactions Batch for Authorization](/docs/cybs/en-us/pax-all-in-one/integration/all/na/pax-all-in-one/pax-aio-payment-txn-intro/pax-aio-pymnt-txn-offline-intro/pax-aio-pymnt-txn-offline-submit-batch-auth.md "").
  {#pax-aio-pymnt-txn-offline-intro_ul_vs4_5q3_1bc}

Process an Offline Sale {#pax-aio-pymnt-txn-offline-sale}
=========================================================

Use this information to process an offline sale. This transaction is also called a *deferred authorization* or *store-and-forward* transaction.
Offline sales can be performed only on terminals that have successfully processed at least one online transaction.  
When internet connectivity is unavailable, an offline sale enables you to capture transaction details locally. These stored transactions must be submitted for authorization when connectivity is restored. For more information, see [Submit an Offline Transactions Batch for Authorization](/docs/cybs/en-us/pax-all-in-one/integration/all/na/pax-all-in-one/pax-aio-payment-txn-intro/pax-aio-pymnt-txn-offline-intro/pax-aio-pymnt-txn-offline-submit-batch-auth.md "").
Only process offline sales when required. The recommendation is to process online sale transactions whenever possible. For more information, see [Sale](/docs/cybs/en-us/pax-all-in-one/integration/all/na/pax-all-in-one/pax-aio-payment-txn-intro/pax-aio-payment-txn-sale-task.md "").  
Follow these steps to process an offline sale.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   // Use this to configure the maximum amount per offline transaction and maximum amount for an offline batch.
   // MposUI.offlineModule.offlineTransactionConfiguration = OfflineTransactionConfiguration(
   //            maximumAmountPerTransaction = BigDecimal("100.00"),
   //            maximumTotalAmountForBatch = BigDecimal("1000.00")
   //        )


   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .build()

   val transactionIntent = mposUi.offlineModule.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
    
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```

Refund an Offline Sale Pending Submission {#pax-aio-pymnt-txn-offline-sale-refund-pend}
=======================================================================================

Use this information to process a refund for an offline sale before it is submitted for authorization.  
Follow these steps to refund an offline sale pending submission.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder() 
               .refund("transactionIdentifier") 
               .build() 

   val transactionIntent = mposUi.offlineModule.createTransactionIntent(transactionParameters) 
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
    
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```

Request a Check Transaction Status for an Offline Sale Pending Submission {#pax-aio-pymnt-txn-offline-check-status-sale-pend}
=============================================================================================================================

Use this information to request a check transaction status for a single offline sale transaction before it is submitted for authorization. The transaction status shows on the Summary screen.  
Follow these steps to request a check transaction status for an offline sale pending submission.

1. Access the `transactionIdentifier` value in the `onActivityResult` method of the original transaction.

2. Retrieve the transaction `summaryIntent` value from the `mposUi` object.

3. Use the `startActivity` method to initiate the Summary screen.

   ```
   val summaryIntent = mposUi.offlineModule.createTransactionSummaryIntent(transactionIdentifier = "transactionIdentifier")
   startActivityForResult(summaryIntent, MposUi.REQUEST_CODE_SHOW_SUMMARY)
   ```
4. After the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
       if (requestCode == MposUi.REQUEST_CODE_SHOW_SUMMARY) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```

Retrieve a List of Offline Transactions Pending Submission {#pax-aio-pymnt-txn-offline-retrieve-txns-pend}
==========================================================================================================

Use this information to retrieve a list of stored offline transactions before they are submitted for authorization.  
Follow this step to retrieve a list of offline transactions pending submission:

1. Use the `queryTransactions` function from the `mposUi` object to retrieve the list.

   ```
   mposUi.offlineModule.queryTransactions(
                       filterParameters = FilterParameters.Builder().build(),
                       includeReceipts = false,
                       offset = 0,
                       limit = 20
                   ) { _, _, _, _, transactions, mposError -&gt;
                       if (transactions != null && transactions.isNotEmpty()) {
                           // Handle Success scenario
                       } else {
                           // Handle Error Scenario
                       }
                   }
   ```

Submit an Offline Transactions Batch for Authorization {#pax-aio-pymnt-txn-offline-submit-batch-auth}
=====================================================================================================

Use this information to submit an offline transactions batch for authorization. After processing offline sale transactions, you must submit these transactions for authorization. The recommendation is to submit the batch as soon as internet connectivity is available.  
Follow these steps to submit an offline transactions batch for authorization.

1. Retrieve the `batchSubmissionIntent` from the `mposUi` object.

2. Use the `startActivity` method to initiate the offline transactions batch submission.

   ```
   val batchSubmissionIntent = mposUi.offlineModule.submitOfflineTransactionBatchIntent()
   startActivityForResult(batchSubmissionIntent, MposUi.REQUEST_CODE_SUBMIT_BATCH)
   ```
3. After the batch submission result is dismissed, the `onActivityResult` method is triggered. This action returns information about the last batch submission.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?)
   {
       super.onActivityResult(requestCode, resultCode, data)
     
       if (requestCode == MposUi.REQUEST_CODE_SUBMIT_BATCH) {
           when (resultCode) {
               // Result code from a successful batch submission
               MposUi.RESULT_CODE_SUBMIT_BATCH_SUCCESS -&gt; {
                  Toast.makeText(findViewById(android.R.id.content),"Batch submission successful", Toast.LENGTH_LONG).show()
               }
               // Result code from a failed batch submission
               MposUi.RESULT_CODE_SUBMIT_BATCH_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content),"Batch submission failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```

Cashback {#pax-aio-payment-txn-cashback-task}
=============================================

Use this information to process a cashback transaction. This transaction enables a customer to request that a specified amount of cash be given to them as part of the transaction. A cashback transaction can be performed with or without a purchase.  
Follow these steps to process a cashback.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("30.00"), Currency.GBP)
               .withCashback(BigDecimal("10.00"))    
               .customIdentifier("yourReferenceForTheTransaction")
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
    
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
4. Get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.  
    

   ```
   val transactionObject = mposUi.latestTransaction
   ```

 

Electronic Benefits Transfer {#pax-aio-pymnt-txn-ebt-intro}
===========================================================

Public assistance programs in the United States use Electronic Benefits Transfer (EBT) payment cards to issue monthly food and cash benefits to eligible individuals. EBT cards function like prepaid debit cards that can be used at authorized retailers.  
Food benefits are issued through the Supplemental Nutrition Assistance Program (SNAP), which helps individuals with low incomes purchase eligible food items.

Process EBT SNAP and EBT Cash Transactions {#pax-aio-pymnt-txn-ebt-task}
========================================================================

Use this information to process an EBT sale and other transactions for EBT SNAP (food benefit) and EBT cash.
Instructions for processing various EBT transaction types are shown in step 2 of the code example.  
Follow these steps to process an EBT transaction.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
                            // Use for Sale
                           .charge(BigDecimal("1.00"), Currency.USD)
                           // Use for Stand-Alone Credit
                          // .refund(BigDecimal("1.00"), Currency.USD)
                          // Use for Cashback
                          // .withCashback(BigDecimal("10.00"))     
                             .customIdentifier("yourReferenceForTheTransaction")
                             .workflow(new WorkflowConfiguration.Builder()
                                  .ebt()
                                  // Set to CASH for EBT cash
                                 .category(FOOD)
                                 // Set to true for Balance Inquiry and set amount to 0
                                .balanceInquiry(false)
                                // Set to true for Voucher transaction
                               .voucher(false)
                               .build())
                            .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?)
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
              // Result code from a declined, aborted or failed transaction
              MposUi.RESULT_CODE_FAILED -&gt; {
               Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
          }
      }
   }
   ```
4. Get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Custom Card Read {#pax-aio-payment-txn-custom-card-read-intro}
==============================================================

The Custom Card Read feature enables you to obtain data from custom cards such as gift cards, loyalty program cards, and employee cards. This feature cannot be used to perform payment functions.
Custom Card Read is supported for non-PCI cards only. To use this feature, the card type must be on your allowlist. To add a card type to your allowlist, contact your implementation manager.  
To retrieve the card data, swipe the card's magnetic stripe through the payment device. The custom card read-only function reads and returns the raw card identifier to your app or point-of-sale (POS) system. You can then use the raw data within your app or POS system.  
These are examples of how you might use the Custom Card Read feature:

* **Custom gift card:** Use the card number to check a balance or process a payment in your private gift card network.
* **Employee card:** Use the card number to look up an employee's profile or account.
  {#pax-aio-payment-txn-custom-card-read-intro_ul_snq_dyx_xgc}

Process a Custom Card Read {#pax-aio-pymnt-txn-custom-card-read-task}
=====================================================================

Follow these steps to process a custom card read.

1. Retrieve the `ReadCardIntent` value from the `mposUi` object and use the `startActivity` method to initiate the card read flow.

   ```
   val ReadCardIntent = mposUi.createReadCardIntent()
   startActivityForResult(ReadCardIntent, MposUi.REQUEST_CODE_READ_CARD)
   ```
2. After the card read activity is complete, the `onActivityResult` method is triggered. This action returns information about the status of the card read activity and the card details.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
       if (requestCode == MposUi.REQUEST_CODE_READ_CARD) {
           when (resultCode) {
               // Result code from a successful card read
               MposUi.RESULT_CODE_READ_CARD_SUCCESS -&gt; {
                  val cardDetailsObject = (mposUi.lastExecution as ExecutionProcess.ReadCardExecutionProcess.Completed).cardDetails
                  Toast.makeText(findViewById(android.R.id.content), "Card read successful", Toast.LENGTH_LONG).show()
               }
               // Result code from a failed card read
               MposUi.RESULT_CODE_READ_CARD_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Card read failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```

Custom Printing {#pax-aio-pymnt-txn-custom-printing-intro}
==========================================================

Use the Custom Printing feature to print custom content directly to the integrated printer of a PAX terminal. This feature enables you to print text, label-value pairs, images, barcodes, and QR codes. It is not limited to receipts and does not affect standard printed or emailed receipts.  
A label-value pair consists of two related text elements: a label that describes the data and a value that displays the associated information. For example: Card (label): Visa (value) or Amount (label): 10.00 (value).

Use Custom Printing {#pax-aio-pymnt-txn-custom-printing-task}
=============================================================

Follow these steps to use custom printing on a PAX device with an integrated printer.

1. Create a `PrintLayoutFactory` object to set a custom print layout.

   ```
   val customReceipt = PrintLayoutFactory.Builder()
           .addParagraph("This is Custom Receipt")
           .addParagraph("This is centered", AccessoryPrinter.Align.CENTER)
           .addParagraph("This is right", AccessoryPrinter.Align.RIGHT)
           .addParagraph("This is left", AccessoryPrinter.Align.LEFT)
           .addLabelValue("Label", "Value")
           .addImage(prepareImageFile("image.jpg", context))
           .addBarcode(
               type = PrintLayout.Section.Barcode.Type.QRCODE,
               value = "https://www.example.com"
           )
           .addEject()
           .build()

       // Adding an image requires the absolute file path of the image. Use this to refer to an image in your asset folder.
       fun prepareImageFile(imageFileName: String, context: Context): String {
           val inputStream = context.assets.open(imageFileName)
           val file = File(context.cacheDir, imageFileName)
           file.outputStream().use { output -&gt;
               inputStream.copyTo(output)
           }
           return file.absolutePath
       }
   ```
2. Retrieve the `CustomPrintIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the custom printing flow.

   ```
   val CustomPrintIntent = mposUi.createCustomPrintIntent(customReceipt)
       startActivityForResult(CustomPrintIntent, MposUi.REQUEST_CODE_CUSTOM_PRINT)
   ```
3. After the printing activity is complete, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
           super.onActivityResult(requestCode, resultCode, data)

           when (requestCode) {
               MposUi.REQUEST_CODE_CUSTOM_PRINT -&gt; {
                   when (resultCode) {
                       MposUi.RESULT_CODE_PRINT_SUCCESS -&gt; {
                           // Printing was successful
                           Log.d(TAG, "Printing successful.")
                       }
                       MposUi.RESULT_CODE_PRINT_FAILED -&gt; {
                           // Printing failed
                           Log.e(TAG, "Printing failed.")
                       }
                   }
               }
           }
       }
   ```

Print a Customer or Merchant Receipt {#pax-aio-payment-txn-print-receipt-task}
==============================================================================

Follow these steps to print a customer or merchant receipt from a previous transaction.

1. Retrieve the `PrintCustomerReceiptIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the printing a receipt flow.

   ```
   // Use to print a customer receipt
   val PrintCustomerReceiptIntent = mposUi.createPrintCustomerReceiptIntent(transactionIdentifier, false)
   startActivityForResult(PrintCustomerReceiptIntent, MposUi.REQUEST_CODE_PRINT_CUSTOMER_RECEIPT)

   // Use to print a merchant receipt
   val PrintMerchantReceiptIntent = mposUi.createPrintMerchantReceiptIntent(transactionIdentifier, false)
   startActivityForResult(PrintMerchantReceiptIntent, MposUi.REQUEST_CODE_PRINT_MERCHANT_RECEIPT)
   ```
2. After the printing activity is complete, `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
       super.onActivityResult(requestCode, resultCode, data)
       "onActivityResult: $resultCode".logDebug(TAG)

       val parentLayout: View = activity!!.findViewById(android.R.id.content)
    
       if (requestCode == MposUi.REQUEST_CODE_PRINT_CUSTOMER_RECEIPT
           || requestCode == MposUi.REQUEST_CODE_PRINT_MERCHANT_RECEIPT) {

           if (resultCode == MposUi.RESULT_CODE_PRINT_SUCCESS) {
               Snackbar.make(parentLayout, "Printing success", Snackbar.LENGTH_SHORT).show()
           }
           else if (resultCode == MposUi.RESULT_CODE_PRINT_FAILED) {
               Snackbar.make(parentLayout, "Printing failed", Snackbar.LENGTH_SHORT).show()
           }
       }
   ```

Email a Customer Receipt {#pax-aio-payment-txn-email-receipt-task}
==================================================================

Follow these steps to email a customer receipt from a previous transaction.

1. Retrieve the `SendEmailReceiptIntent` value from the `mposUi` object and use the `startActivity` method to initiate the emailing a receipt flow.

   ```
   val SendEmailReceiptIntent = mposUi.createSendEmailReceiptIntent(transactionIdentifier)
   startActivityForResult(SendEmailReceiptIntent, MposUi.REQUEST_CODE_SEND_EMAIL)
   ```
2. After the emailing activity is complete, `onActivityResult` method is triggered, which returns information about the status of the emailing activity.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
       super.onActivityResult(requestCode, resultCode, data)
       "onActivityResult: $resultCode".logDebug(TAG)

       val parentLayout: View = activity!!.findViewById(android.R.id.content)
    
       if (requestCode == MposUi.REQUEST_CODE_SEND_EMAIL) {

           if (resultCode == MposUi.RESULT_CODE_EMAIL_SUCCESS) {
               Snackbar.make(parentLayout, "Receipt sent via email", Snackbar.LENGTH_SHORT).show()
           }
           else if (resultCode == MposUi.RESULT_CODE_EMAIL_FAILED) {
               Snackbar.make(parentLayout, "Fail while sending receipt via email", Snackbar.LENGTH_SHORT).show()
           }
       }
   }
   ```

