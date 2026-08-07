Tap to Pay on Android Payment Services {#tap-to-phone-payment-txn-intro}
========================================================================

Use this information to process Tap to Pay on Android Solution payment services.

Sale {#tap-to-phone-payment-txn-sale}
=====================================

Use this information to process a sale. This transaction combines an authorization and a capture into a single transaction.  
Follow these steps to process a sale.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` value from the `mposUI` object, and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is completed and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the previous transaction.

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
4. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUI` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Refund {#tap-to-phone-payment-txn-refund}
=========================================

Use this information to process a refund by referencing the original transaction. You can issue refunds for either the full amount or a partial amount of the original transaction.  
Stand-alone credits are also supported and can be processed independently of a previous transaction. For more information, see [Stand-Alone Credit](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-payment-txn-intro/tap-to-phone-payment-txn-standalone-credit.md "").  
Follow these steps to process a refund.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` value from the `mposUI` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder() 
               .refund(“transactionIdentifier”) 
               //Specify amount and currency for partial refunds 
               //.amountAndCurrency(BigDecimal(1.00), Currency.EUR) 
               .build() 

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters) 
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is completed and the Summary screen is dismissed, `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) { 
       super.onActivityResult(requestCode, resultCode, data) 
     
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) { 
           when (resultCode) { 
               // Result code from a successful transaction 
               MposUi.RESULT_CODE_APPROVED -&gt; { 
                   val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRAN
   SACTION_IDENTIFIER) 
                   Toast.makeText(findViewById(android.R.id.content),"Transaction approved!
   \nIdentifier: $transactionIdentifier",  
   Toast.LENGTH_LONG).show() 
               } 
               // Result code from a declined, aborted or failed transaction 
               MposUi.RESULT_CODE_FAILED -&gt; { 
                Toast.makeText(findViewById(android.R.id.content), "Transaction was decline
   d, aborted, or failed",  
   Toast.LENGTH_LONG).show() 
               } 
           } 
       } 
   }
   ```
4. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUI` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Stand-Alone Credit {#tap-to-phone-payment-txn-standalone-credit}
================================================================

Use this information to process a stand-alone credit. This transaction enables you to issue a credit without referencing a previous transaction. The customer must present their payment card.

> WARNING
> When processing a stand-alone credit, there is no limit on the credit amount because the transaction does not reference the original purchase. To help manage risk, it is recommended to use a refund transaction whenever possible. For more information, see [Refund](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-payment-txn-intro/tap-to-phone-payment-txn-refund.md "").  
> Follow these steps to process a stand-alone credit.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` value from the `mposUI` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder() 
               .refund(BigDecimal("1.00"), Currency.EUR)     
               .customIdentifier("yourReferenceForTheTransaction") 
               .build() 

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters) 
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is completed and the Summary screen is dismissed, `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
              // Result code from a successful transaction
              MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", 
   Toast.LENGTH_LONG).show()
              }
              // Result code from a declined, aborted or failed transaction
              MposUi.RESULT_CODE_FAILED -&gt; {
              Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", 
   Toast.LENGTH_LONG).show()
              }
           }
       }
   }
   ```
4. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUI` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Check Transaction Status {#tap-to-phone-payment-txn-check-txn-status}
=====================================================================

Use this information to request a check transaction status. This transaction enables you to retrieve response data for a transaction that was lost or timed out. You must have the `transactionIdentifier` value for the transaction that you want to check. When the check transaction status request is complete, the transaction details show on the Summary screen.  
Follow these steps to request a check transaction status.

1. Obtain the `transactionIdentifier` value in the `onActivityResult` method of the original transaction.

2. Retrieve the transaction `summaryIntent` value from the `mposUI` object.

3. Use the `startActivity` method to initiate the Summary screen.

   ```
   val summaryIntent = mposUi.createTransactionSummaryIntent(transactionIdentifier = "transactionIdentifier")
   startActivityForResult(summaryIntent, MposUi.REQUEST_CODE_SHOW_SUMMARY)
   ```
4. After the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
       // Result code from closing the summary screen
       if (resultCode == MposUi.RESULT_CODE_SUMMARY_CLOSED) {
           // Accessing status from the transaction that was just queried
           val transactionStatus = mposUi.latestTransaction?.status
           Toast.makeText(activity, "Summary closed. Transaction status: $transactionStatus", Toast.LENGTH_SHORT).show()  
       }
   }
   ```
5. You can get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.  
    

   ```
   val transactionObject = mposUi.latestTransaction
   ```

 

Pre-Authorization {#tap-to-phone-payment-txn-pre-auth-task}
===========================================================

Use this information to process a pre-authorization for an initial amount. A pre-authorization transaction places a temporary hold on the customer's payment card. The transaction amount can be captured at a later time.  
Most authorizations expire within 5 to 7 days, as determined by the issuing bank. When an authorization expires, your bank, the issuing bank, or payment processor might require you to resubmit the authorization request and include a capture request in the same message. For more information, see[Capture](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-payment-txn-intro/tap-to-phone-payment-txn-capture-task.md "").  
To help ensure successful transaction processing, monitor authorization timelines and use combined authorization and capture requests when necessary.  
Follow these steps to process a pre-authorization.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` value from the `mposUI` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .autoCapture(false)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is completed and the Summary screen is dismissed, `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   Override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
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
4. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUI` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Incremental Authorization {#tap-to-phone-payment-txn-incremental-auth-task}
===========================================================================

Use this information to process an incremental authorization. An incremental authorization is used after an approved pre-authorization to increase the authorized amount before capture.  
Follow these steps to process an incremental authorization.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` value from the `mposUI` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder() 
               .incrementalAuthorization("transactionIdentifier") 
               .amountAndCurrency(BigDecimal("1.00"), Currency.EUR) 
               .build() 

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters) 
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is completed and the Summary screen is dismissed, `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   Override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) { 
       super.onActivityResult(requestCode, resultCode, data) 
     
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) { 
           when (resultCode) { 
               // Result code from a successful transaction 
               MposUi.RESULT_CODE_APPROVED -&gt; { 
                   val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRAN
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
4. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUI` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Capture {#tap-to-phone-payment-txn-capture-task}
================================================

Use this information to capture a pre-authorized transaction. The capture request references the approved pre-authorization request.  
Follow these steps to process a capture.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` value from the `mposUI` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
              .capture("transactionIdentifier") 
           // Specify amount and currency for partial captures
           // .amountAndCurrency(BigDecimal("1.00"), Currency.EUR)
              .build() 

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters) 
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is completed and the Summary screen is dismissed, `onActivityResult` method is triggered. This action returns information about the previous transaction.

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
4. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUI` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Airline Details {#ttp-payment-txn-sale-airline-details}
=================================================================

Use this information to process a sale with airline details. This transaction includes required airline and related service details in the payment request.  
Follow these steps to process a sale with airline details.

1. Create an `AdditionalDetails` object and set one or more airline (`airlineDetails`) fields and related service (`ancillaryDetails`) fields.

   ```
   val airlineDetails = AdditionalDetailsBuilder()
           .airlineDetails(
               AirlineDetailsBuilder()
                   .agentCode("AGT12345")
                   .agentName("Relay Travel")
                   .arrivalDate(SimpleDateFormat("MMddyyyy", Locale.US).parse("01202024"))
                   .carrierName("Relay Airways")
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

Sale with Auto Rental Details {#ttp-payment-txn-sale-auto-rental-details}
=========================================================================

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

Sale with Billing and Shipping Details {#ttp-payment-txn-sale-bill-ship-details}
================================================================================

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
                   .company("Relay Inc.")
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
                   .company("Relay Inc.")
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

Sale with Lodging Details {#ttp-payment-txn-sale-lodging-details}
=================================================================

Use this information to process a sale with lodging details. This transaction includes the required lodging details in the payment request.  
Follow these steps to process a sale with lodging details.

1. Create a `AdditionalDetails` object and set one or more lodging fields.

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

3. Retrieve the `transactionIntent` from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

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
5. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Installment Details {#ttp-payment-txn-sale-installment-details-task}
==============================================================================

Use this information to process a sale with installment details. This transaction includes the required installment payment details in the payment request.
IMPORTANT This transaction is available only in the Latin American and Caribbean (LAC) region.  
Follow these steps to process a sale with installment details.

1. Create an `InstallmentDetails` object and set one ore more of the installment fields.

   ```
   // Set value of the builder to the number of installments
   val installmentDetails = InstallmentDetailsBuilder(5)
           // Set to PlanType.ISSUER_FUNDED for issuer funded plans
           .planType(PlanType.MERCHANT_FUNDED)
           .includesInterest(true)
           .governmentPlan(true)
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .installmentDetails(installmentDetails)
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
5. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Merchant-Defined Data Details {#ttp-payment-txn-sale-merch-defined-data-details}
==========================================================================================

Use this information to process a sale with merchant-defined data details. This transaction includes required merchant-defined data details in the payment request.  
Follow these steps to process a sale with merchant-defined data details.

1. Create an `AdditionalDetails` object and set one or more merchant defined data fields.

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

Sale with On-Reader Tipping {#tap-to-phone-payment-txn-sale-on-reader-tip-task}
===============================================================================

Use this information to process a sale with on-reader tipping. At the start of each transaction, the terminal prompts the customer to add a tip by showing suggested tip amounts. The customer chooses or enters a tip amount on the terminal before presenting their payment card.  
Follow these steps to process a sale with on-reader tipping.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Create a `TippingProcessStepParameters` object to configure the tipping function. The options are percentage choice, tip amount, or total amount.

3. Create a `TransactionProcessParameters` object to add the tipping step.

4. Retrieve the `transactionIntent` value from the `mposUI` object, and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)
               .customIdentifier("yourReferenceForTheTransaction")
               .build()

   //  Use to display three tipping percentage choices
   val tipStep = TippingProcessStepParameters.Builder()
               .askForPercentageChoice()
           //  Optional to configure tipping percentages | Default values = 10, 15, 20
           //  .percentages(BigDecimal("10"), BigDecimal("20"), BigDecimal("30"))
           //  Optional to show confirmation screen
           //  .showTotalAmountConfirmationScreen(true)
               .build()

   //  Use to ask for tip amount
   //  val tipStep = TippingProcessStepParameters.Builder()
           //  .askForTipAmount()
           //  Optional to show confirmation screen
           //  .showTotalAmountConfirmationScreen(true)
           //  .build()

   //  Use to ask for total transaction amount including tip
           //  val tipStep = TippingProcessStepParameters.Builder()
           //  .askForTotalAmount()
           //  Optional to show confirmation screen
           //  .showTotalAmountConfirmationScreen(true)
           //  .build()

   val processParameters = TransactionProcessParameters.Builder()
       .addStep(tipStep)
       .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters, processParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
5. After the transaction is completed and the Summary screen is dismissed, `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   Override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
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
                  Toast.makeText(findViewById(android.R.id.content), “Transaction was declined, aborted, or failed”, Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
6. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUI` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Payment Facilitator Details {#ttp-payment-txn-sale-payment-facilitator-task}
======================================================================================

Use this information to process a sale with payment facilitator details. This transaction includes the required payment facilitator details in the payment request.  
Follow these steps to process a sale with payment facilitator details.

1. Create a `MerchantDetails` object and set one ore more of the payment facilitator fields.

   ```
   val merchantDetails = MerchantDetailsBuilder()
           .salesOrganizationId("12345")
           .subMerchantId("SM67890")
           .merchantDescriptor("ExampleMerchant")
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .merchantDetails(merchantDetails)
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
5. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Tax Details {#ttp-payment-txn-sale-tax-details-task}
==============================================================

Use this information to process a sale with tax details. This transaction includes required tax details in the payment request.  
Follow these steps to process a sale with tax details.

1. Create a `TaxDetails` object and set one ore more of the tax fields.

   ```
   val taxDetails = TaxDetailsBuilder()
           .merchantTaxId("TaxID1234")
           .salesSlipNumber(12345678)
           .includedTaxAmount(BigDecimal("5.00"))
           .includedLocalTaxAmount(BigDecimal("1.00"))
           .includedNationalTaxAmount(BigDecimal("2.00"))
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .taxDetails(taxDetails)
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
5. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Email a Customer Receipt {#tap-to-phone-payment-txn-email-receipt-task}
=======================================================================

Follow these steps to email a customer receipt from a previous transaction.

1. Retrieve the `SendEmailReceiptIntent` variable from the `mposUI` object and use the `startActivity` method to initiate the emailing a receipt flow.

   ```
   val SendEmailReceiptIntent = mposUi.createSendEmailReceiptIntent(transactionIdentifier)
   startActivityForResult(SendEmailReceiptIntent, MposUi.REQUEST_CODE_SEND_EMAIL)
   ```
2. After the emailing activity is completed, the `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
       super.onActivityResult(requestCode, resultCode, data)
       "onActivityResult: $resultCode".logDebug(TAG)

       val parentLayout: View = activity!!.findViewById(android.R.id.content)

       if (requestCode == MposUi.REQUEST_CODE_SEND_EMAIL) {

           if (resultCode == MposUi.RESULT_CODE_EMAIL_SUCCESS) {
               Snackbar.make(parentLayout, "Receipt sent via email", Snackbar.LENGTH_SHORT).show()
           }
           else if (resultCode == MposUi.RESULT_CODE_EMAIL_FAILED) {
               Snackbar.make(parentLayout, "Fail while sending receipt via email", Snackbar.LENGTH_SHORT).show()
           }
       }
   }
   ```

