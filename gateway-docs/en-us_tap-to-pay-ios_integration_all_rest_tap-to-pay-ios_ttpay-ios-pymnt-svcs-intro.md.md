Tap to Pay on iPhone Payment Services {#ttpay-ios-pymnt-svcs-intro}
===================================================================

This section describes the payment services featured in the Tap to Pay on iPhone Solution.

Sale {#ttpay-ios-sale}
======================

Use this information to process a sale transaction. This transaction combines an authorization and a capture into a single transaction.  
When an internet connection is not available, you can use the Store and Forward feature to process offline sale and stand-alone credit transactions.

1. Create a `ChargeParameters` object and call `startChargeTransaction(with:)`.

   ```
   // Throws MposUIReaderError.notActivated if device is not activated
   let online = try await reader.mposUIOnline()

   let chargeParameters = ChargeParameters(amount: Decimal(1.00),
                                           currency: .USD,
                                           customIdentifier: "yourReferenceForTheTransaction")

   let charge = await online.startChargeTransaction(with: chargeParameters)

   switch charge {
   case .success(let transaction):
       print("Transaction successful: \(transaction.identifier)")
   case .failure(let error):
       print("Transaction failed: \(error)")
   @unknown default:
       break
   }
   ```

Refund {#ttpay-ios-refund}
==========================

Use this information to process a refund for a full or partial transaction amount by using a reference to the original transaction. This transaction is also called a *linked refund*. This Acceptance Devices solution also supports stand-alone credits.

1. Get the online payment service and call `refundTransaction(withID:partiallyWithAmount:)` with the original transaction identifier.

   ```
   // Throws MposUIReaderError.notActivated if device is not activated
   let online = try await reader.mposUIOnline()

   let linkedRefund = await online.refundTransaction(
       withID: "transactionIdentifier",
       partiallyWithAmount: (Decimal(1.00), .USD)
   )

   switch linkedRefund {
   case .success(let transaction):
       print("Refund successful.")
   case .cancelledByUser:
       print("Refund cancelled.")
   case .error(let developerInfo):
       print("Refund failed. Info: \(developerInfo)")
   }
   ```

Stand-Alone Credit {#ttpay-ios-standalone-credit}
=================================================

Use this information to process a stand-alone credit. This transaction is used to process a credit without reference to the original transaction. The customer is required to present their payment card for this transaction.  
When an internet connection is not available, you can use the Store and Forward feature to process offline sale and stand-alone credit transactions.

> WARNING Use a linked refund transaction whenever possible. When processing a stand-alone credit, there is no limit on the credit amount because there is no reference to the original transaction amount.

1. Create a `RefundParameters` object and call `startStandaloneRefundTransaction(with:)`.

   ```
   // Throws MposUIReaderError.notActivated if device is not activated
   let online = try await reader.mposUIOnline()

   let refundParameters = RefundParameters(amount: Decimal(1.00),
                                           currency: .USD,
                                           customIdentifier: "yourReferenceForTheTransaction")

   let refund = await online.startStandaloneRefundTransaction(with: refundParameters)

   switch refund {
   case .success(let transaction):
       print("Refund successful: \(transaction.identifier)")
   case .failure(let error):
       print("Refund failed: \(error)")
   @unknown default:
       break
   }
   ```

Pre-Authorization {#ttpay-ios-pre-auth}
=======================================

Use this information to process a pre-authorization for an initial amount. This transaction places a temporary hold on the customer's payment card. The transaction amount can be captured at a later time.  
Most authorizations expire in 5 to 7 days. The issuing bank sets this period of time. When an authorization expires with the issuing bank, your bank or processor might require you to re-submit an authorization request and include a request for capture in the same message.

1. Create the online payment service, create a `ChargeParameters` object with `autocapture` set to `false`, and call `startChargeTransaction(with:)`.

   ```
   // Throws MposUIReaderError.notActivated if device is not activated
   let online = try await reader.mposUIOnline()

   let chargeParameters = ChargeParameters(amount: Decimal(1.00),
                                           currency: .USD,
                                           customIdentifier: "yourReferenceForTheTransaction",
                                           autocapture: false)

   let charge = await online.startChargeTransaction(with: chargeParameters)
   ```

Incremental Authorization {#ttpay-ios-increm-auth}
==================================================

Use this information to process an incremental authorization. This transaction can be applied to an existing pre-authorization request to increase the authorized amount before capture.

1. Create the online payment service and call `incrementTransaction(withID:withAmount:)` with the transaction identifier and additional amount.

   ```
   // Throws MposUIReaderError.notActivated if device is not activated
   let online = try await reader.mposUIOnline()

   let increment = await online.incrementTransaction(
       withID: "transactionIdentifier",
       withAmount: (Decimal(1.00), .USD)
   )

   switch increment {
   case .success(let transaction):
       print("Increment successful.")
   case .cancelledByUser:
       print("Increment cancelled.")
   case .error(let developerInfo):
       print("Increment failed. Info: \(developerInfo)")
   }
   ```

Capture {#ttpay-ios-capture}
============================

Use this information to capture a pre-authorized transaction. The capture request references the approved pre-authorization request.

1. Create the online payment service and call `captureTransaction(withID:partiallyWithAmount:)` with the transaction identifier and capture amount.

   ```
   // Throws MposUIReaderError.notActivated if device is not activated
   let online = try await reader.mposUIOnline()

   let capture = await online.captureTransaction(
       withID: "transactionIdentifier",
       partiallyWithAmount: (Decimal(1.00), .USD)
   )

   switch capture {
   case .success(let transaction):
       print("Capture successful.")
   case .cancelledByUser:
       print("Capture cancelled.")
   case .error(let developerInfo):
       print("Capture failed. Info: \(developerInfo)")
   }
   ```

Sale with On-Reader Tipping {#ttpay-ios-sale-on-reader-tip}
===========================================================

Use this information to process a sale with on-reader tipping. At the start of each transaction, the device prompts the customer to add a tip by showing suggested tip amounts and a no-tip option. The customer chooses or enters an amount before presenting their payment card.

1. Create the online payment service.

2. Create a `Tipping` configuration for the on-reader tip options.

3. Add the tipping configuration to the `ChargeParameters` object and call `startChargeTransaction(with:)`.

   ```
   // Throws MposUIReaderError.notActivated if device is not activated
   let online = try await reader.mposUIOnline()

   // Percentage choices
   let tipConfig = Tipping.percentageChoice([5, 10, 15])

   // Custom tip amount input
   // let tipConfig = Tipping.input(.tipAmount())

   // Total amount including tip
   // let tipConfig = Tipping.input(.totalAmount())

   let chargeParameters = ChargeParameters(amount: Decimal(1.00),
                                           currency: .USD,
                                           customIdentifier: "yourReferenceForTheTransaction",
                                           tip: tipConfig)

   let charge = await online.startChargeTransaction(with: chargeParameters)
   ```

Check Transaction Status Using `showSummary` {#ttpay-ios-check-txn-status-summary}
==================================================================================

To submit a check transaction status request, you must have the `transactionIdentifier` value for the transaction that you want to check. Use the check transaction status request to obtain response data for a transaction that was lost or timed out.  
When you send the request using the `showSummary` method, the transaction details are shown on the Summary screen.

1. Create the online payment service and call `showSummary(forID:)` with the transaction identifier.

   ```
   // Throws MposUIReaderError.notActivated if device is not activated
   let online = try await reader.mposUIOnline()

   let summary = await online.showSummary(forID: "transactionIdentifier")

   switch summary {
   case .success(let transaction):
       print("Transaction status: \(transaction.identifier)")
   case .error(let developerInfo):
       print("Failed to retrieve summary. Info: \(developerInfo)")
   }
   ```

Check Transaction Status Using `lookupTransaction` {#ttpay-ios-check-txn-status-lookup}
=======================================================================================

To submit a check transaction status request, you must have the `transactionIdentifier` value for the transaction that you want to check. Use the check transaction status request to obtain response data for a transaction that was lost or timed out.  
When you send the request using the `lookupTransaction` method, the transaction details are shown in the `transaction` object.

1. Create the online payment service and call `lookupTransaction(forID:)` with the transaction identifier.

   ```
   // Throws MposUIReaderError.notActivated if device is not activated
   let online = try await reader.mposUIOnline()

   let result = await online.lookupTransaction(forID: "transactionIdentifier")

   switch result {
   case .success(let transaction):
       print("Transaction found: \(transaction.identifier)")
   case .notFound:
       print("Transaction not found.")
   case .networkError(let developerInfo):
       print("Network error. Info: \(developerInfo)")
   case .unexpected(let developerInfo):
       print("Unexpected error. Info: \(developerInfo)")
   }
   ```

Store and Forward Offline Transactions {#ttpay-ios-storeforward-offline-intro}
==============================================================================

Use this information to use the Store and Forward feature to process offline sale and stand-alone credit transactions when an internet connection is not available.

> WARNING Using offline transaction payment services involves risk. Because these transactions are not authorized in real time, you assume responsibility for potential issues such as failed transactions, increased fraud, and higher chargeback rates. Only use offline transactions when necessary such as during temporary internet outages. Whenever possible, it is recommended to process online sale transactions to ensure secure and immediate authorization.
> IMPORTANT Store and Forward requires iOS 18.4 or later.

Offline Sale {#ttpay-ios-storeforward-offline-sale}
===================================================

Use this information to process a Store and Forward offline sale transaction. This transaction combines an authorization and a capture into a single transaction. When an internet connection is not available, the transaction is stored offline.  
Stored offline transactions must be submitted for authorization when an internet connection is available.

> WARNING  
> Whenever possible, process online sale transactions to ensure secure and immediate authorization. Using offline transaction payment services involves risk. Because these transactions are not authorized in real time, you assume responsibility for potential issues.

1. Create the offline payment service.

2. Create a `ChargeParameters` object for the offline sale.

3. Call `startChargeTransaction(with:)` to store the sale transaction offline.

   ```
   // Throws MposUIReaderError.notActivated if device is not activated
   let offline = try await reader.mposUIOffline()

   let chargeParameters = ChargeParameters(amount: Decimal(1.00),
                                           currency: .USD,
                                           customIdentifier: "yourReferenceForTheTransaction")

   let result = await offline.startChargeTransaction(with: chargeParameters)

   switch result {
   case .offlineSuccess(let offlineTransaction):
       print("Stored offline. ID: \(offlineTransaction.id), amount: \(offlineTransaction.amount)")
   case .failure(let error):
       print("Transaction failed: \(error)")
   @unknown default:
       break
   }
   ```

Offline Stand-Alone Credit {#ttpay-ios-storeforward-offline-standalone-credit}
==============================================================================

Use this information to process a Store \& Forward offline stand-alone credit transaction. When an internet connection is not available, the transaction is stored offline.  
Stored offline transactions must be submitted for authorization when an internet connection is available.

1. Create the offline payment service.

2. Create a `RefundParameters` object for the offline stand-alone credit.

3. Call `startStandaloneRefundTransaction(with:)` to store the stand-alone credit transaction offline.

   ```
   // Throws MposUIReaderError.notActivated if device is not activated
   let offline = try await reader.mposUIOffline()

   let refundParameters = RefundParameters(amount: Decimal(1.00),
                                           currency: .USD,
                                           customIdentifier: "yourReferenceForTheTransaction")

   let result = await offline.startStandaloneRefundTransaction(with: refundParameters)

   switch result {
   case .offlineSuccess(let offlineTransaction):
       print("Refund stored offline. ID: \(offlineTransaction.id)")
   case .failure(let error):
       print("Refund failed: \(error)")
   @unknown default:
       break
   }
   ```

Check Offline Transactions Batch Status {#ttpay-ios-storeforward-offline-trxn-batch-status}
===========================================================================================

Use this information to retrieve a summary of Store and Forward offline transactions that are pending submission. The summary shows how many transactions are pending upload, when the session expires, and the cumulative (total monetary) amount of the stored transactions.  
The offline session is valid for 24 hours from when the last online transaction was completed. If the offline session expires, the device must go online before you can continue to perform Store and Forward transactions. The SDK refreshes the offline session automatically when the Store and Forward component initializes on an activated device (for example, after app launch), when an online transaction is performed, or when the integrator calls the `syncSession()` method.  
When the device is rebooted or the passcode is turned off and on, the offline session becomes invalid. To refresh the offline session, the device must go online and perform an online transaction. After the online transaction is complete, the SDK uses the same automatic refresh behavior described for expired sessions.

1. Use the offline payment service to get the status of the offline transactions batch.

   ```
   // Throws MposUIReaderError.notActivated if device is not activated
   let offline = try await reader.mposUIOffline()
   let session = await offline.getSession()

   print("Pending transactions: \(session.transactionCount)")
   print("Session expires: \(session.expirationDate)")
   print("Cumulative amount: \(session.cumulativeAmount)")
   ```

Retrieve Offline Transactions Pending Submission {#ttpay-ios-storeforward-retrieve-pend-txns}
=============================================================================================

Use this information to retrieve a list of Store and Forward offline transactions that are pending submission for authorization.

1. Use the offline payment service to retrieve the list of offline transactions that are pending submission.

   ```
   // Throws MposUIReaderError.notActivated if device is not activated
   let offline = try await reader.mposUIOffline()
   let transactions = offline.getTransactionList()

   for tx in transactions {
       print("[\(tx.type)] \(tx.amount) \(tx.currency) — \(tx.date)")
   }
   ```

Submit Offline Transactions Batch for Authorization {#ttpay-ios-store-forward-submit-batch}
===========================================================================================

Use this information to submit a batch of Store and Forward offline transactions for authorization.  
After processing offline transactions, submit them for authorization as soon as an internet connection is available. Transactions remain stored locally until they are successfully uploaded.

> IMPORTANT  
> The device must have an internet connection before calling the ` syncSession() ` method, as shown in the code example.

1. Confirm that an internet connection is available.

2. Create the offline payment service.

3. Call the `syncSession()` method to submit the offline transactions batch for authorization.

   ```
   // Throws MposUIReaderError.notActivated if device is not activated
   let offline = try await reader.mposUIOffline()
   let result: SyncSessionResult = await offline.syncSession()

   switch result {
   case .success:
       print("Batch session refreshed.")
   case .failure(.notActivated):
       print("Device not activated.")
   case .failure(.sessionInvalidated):
       print("Session invalidated — re-authenticate.")
   case .failure(.other(let developerInfo)):
       print("Sync failed: \(developerInfo)")
   }
   ```

Email a Customer Receipt {#ttpay-ios-email-cust-receipt}
========================================================

Use this information to email the receipt for an existing transaction to a customer.

1. Create the online payment service and call `sendEmailReceipt(forID:)` with the transaction identifier.

   ```
   // Throws MposUIReaderError.notActivated if device is not activated
   let online = try await reader.mposUIOnline()

   let email = await online.sendEmailReceipt(forID: "transactionIdentifier")

   switch email {
   case .success:
       print("Receipt sent.")
   case .cancelByUser:
       print("Receipt cancelled.")
   case .error(let developerInfo):
       print("Failed to send receipt. Info: \(developerInfo)")
   }
   ```

