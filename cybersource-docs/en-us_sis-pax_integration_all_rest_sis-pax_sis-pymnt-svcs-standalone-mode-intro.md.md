Standalone Mode Payment Services {#sis-pymnt-svcs-standalone-mode-intro}
========================================================================

Use this information to process payment services available in the Acceptance Devices app when operated in Standalone mode.  
These are some benefits of using Standalone mode:

* You can start transactions directly from the terminal.

* This mode is the fastest way to begin accepting payments.

* There is no integration required when using this mode with a point-of-sale (POS) system.

* Use this mode as a backup option when your POS system is unavailable for Local or Cloud semi-integrated modes.
  {#sis-pymnt-svcs-standalone-mode-intro_ul_f1b_dhp_vzb}
  IMPORTANT When the Acceptance Devices app is in Standalone mode, the terminal does not communicate with your POS system to exchange transaction details. You are responsible for reconciling transactions with your internal systems and records.  
  For information about other modes available in the Acceptance Devices app, see:

* [Local Mode Payment Services](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro.md "")

* [Cloud Mode Payment Services](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro.md "")
  {#sis-pymnt-svcs-standalone-mode-intro_ul_l5b_yqm_3fc}

Enable Standalone Mode in the Acceptance Devices App {#sis-standalone-mode-enable}
==================================================================================

Follow these steps to enable Standalone mode in the Acceptance Devices app:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Standalone Mode.
4. Toggle Enable Standalone Mode to ON.
5. Choose the currency in which you want to process transactions. Tap Save.
6. If you want to enable custom merchant reference codes, toggle Custom Transaction Reference to ON.
7. Tap the back navigation arrow to return to the home screen. You can now process transactions in Standalone mode.

Sale {#sis-standalone-mode-sale}
================================

Use this information to process a sale transaction when the app is in Standalone mode. This type of transaction combines an authorization and a capture into a single transaction.  
Follow these steps to process a sale transaction:

1. In the Acceptance Devices app, tap Sale.
2. Enter the transaction amount.
3. Tap Submit to start the transaction.

Refund {#sis-standalone-mode-refund}
====================================

Use this information to process a refund when the app is in Standalone mode. This type of refund includes a reference to the original transaction for a full or partial transaction amount.  
Stand-alone credits are also supported in this Acceptance Devices solution. For more information, see [Stand-Alone Credit](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-standalone-mode-intro/sis-standalone-mode-standalone-credit.md "").  
Follow these steps to process a refund:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Transaction History.
4. Tap the transaction you want to refund.
5. Enter the transaction amount.
6. Tap Refund to start the transaction.

Stand-Alone Credit {#sis-standalone-mode-standalone-credit}
===========================================================

Use this information to process a stand-alone credit when the app is in Standalone mode. This type of transaction is used to process a credit without reference to the original transaction. The customer is required to present their card for this type of transaction.

> WARNING
> When processing a stand-alone credit, there is no limit on the credit amount because there is no reference to the original transaction amount. The recommendation is to use a refund transaction whenever possible. For more information, see [Refund](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-standalone-mode-intro/sis-standalone-mode-refund.md "").  
> Follow these steps to process a stand-alone credit:

1. In the Acceptance Devices app, tap Other Transactions.
2. Tap Refund.
3. Enter your Acceptance Devices app passcode.
4. Enter the transaction amount.
5. Tap Submit to start the transaction.

Sale with On-Reader Tipping {#sis-standalone-mode-sale-on-reader-tip}
=====================================================================

Use this information to process a sale with on-reader tipping in Standalone mode. At the start of each transaction, the terminal prompts the customer to add a tip by showing suggested tip amounts. The customer selects or enters a tip amount on the terminal before presenting their payment card.  
Follow these steps to process a sale with on-reader tipping:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Standalone Mode.
4. Toggle Ask for Tip to ON.
5. Tap the back navigation arrow to return to the home screen.
6. Tap Sale.
7. Enter the transaction amount.
8. Tap Submit to start the transaction.

Pre-Authorization {#sis-standalone-mode-pre-auth}
=================================================

Use this information to process a pre-authorization for an initial amount in Standalone mode. A pre-authorization transaction places a temporary hold on the customer's payment card. The transaction amount can be captured at a later time.  
Most authorizations expire in 5 to 7 days. The issuing bank sets the length of time before expiration. When an authorization expires with the issuing bank, your bank or processor might require you to re-submit an authorization request and include a request for capture in the same message. For more information, see [Capture](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-standalone-mode-intro/sis-standalone-mode-capture.md "").  
Follow these steps to process a pre-authorization:

1. In the Acceptance Devices app, tap Other Transactions.
2. Tap Pre-Authorization.
3. Enter the transaction amount.
4. Tap Submit to start the transaction.

Capture {#sis-standalone-mode-capture}
======================================

Use this information to capture a pre-authorized transaction in Standalone mode. The capture request references the approved pre-authorization request.  
Follow these steps to process a capture:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Transaction History.
4. Tap the transaction you want to capture.
5. Tap Capture.
6. Enter the transaction amount.
7. Tap Capture to start the transaction.

Mail Order or Telephone Order Sale {#sis-standalone-mode-moto-sale}
===================================================================

Use this information to process a mail order or telephone order (MOTO) sale in Standalone mode. The payment card is not physically tapped, inserted, or swiped in the terminal for a MOTO transaction.  
Follow these steps to process a MOTO sale:

1. In the Acceptance Devices app, tap Other Transactions.
2. Tap MOTO.
3. Enter the transaction amount.
4. Tap Submit to start the transaction.

Account Verification {#sis-standalone-mode-acct-verif}
======================================================

Use this information to process an account verification when the app is in Standalone mode. The account verification transaction submits a zero-amount authorization request to validate the payment card.  
Follow these steps to process an account verification:

1. In the Acceptance Devices app, tap Other Transactions.
2. Tap Account Verification to start the transaction.

Offline Transactions {#sis-standalone-mode-offline-txn-intro}
=============================================================

Offline mode is a feature that you can enable and customize in the `Business Center`. The default setting is `Disabled`. For more information, see [Customizing the Acceptance Devices App](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-get-started-intro/sis-ad-app-customize-intro.md "").

> WARNING
> By using this feature, you assume the risk of failed transactions and the possibility of increased fraud and chargebacks. Process transactions offline only when required such as during an internet outage. Whenever possible, process transactions online instead. For more information, see [Sale](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-standalone-mode-intro/sis-standalone-mode-sale.md "").  
> When an internet connection is available, submit the offline transactions batch for authorization while in Offline mode.  
> Use this information to enable and disable Offline mode when the app is in Standalone mode. When an internet connection is not available, you can use this mode to process offline sale and refund transactions.

Enable or Disable Offline Mode {#sis-standalone-mode-offline-txn-enable-disable}
================================================================================

IMPORTANT The recommendation is to resume operating in online mode as soon as an internet connection is available. To do so, you must first disable Offline mode.  
Follow these steps to enable or disable Offline mode.

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Offline Mode.
4. Toggle Enable Offline Mode to ON or OFF.
5. Tap the back navigation arrow to return to the home screen.

Offline Sale {#sis-standalone-mode-offline-txn-sale}
====================================================

Follow these steps to process an offline sale with Offline mode enabled:

1. In the Acceptance Devices app, tap Sale.
2. Enter the transaction amount.
3. Tap Submit to start the transaction.

Offline Refund {#sis-standalone-mode-offline-txn-refund}
========================================================

Follow these steps to process an offline refund with Offline mode enabled:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Offline Mode.
4. Tap the transaction you want to refund.
5. Tap Refund.
6. Enter the transaction amount.
7. Tap Refund to start the transaction.

Submit an Offline Transactions Batch for Authorization {#sis-standalone-mode-offline-txn-batch-auth}
====================================================================================================

IMPORTANT The recommendation is to submit the batch as soon as an internet connection is available. Offline mode must be enabled before you can submit a batch for authorization.  
Follow these steps to submit an offline transactions batch for authorization with Offline mode enabled:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Offline Mode.
4. Tap Submit Offline Batch.

Sale with Installment Details {#sis-standalone-mode-sale-install-details}
=========================================================================

Use this information to process a sale transaction with installment details when the app is in Standalone mode. This payment service enables you to include the required installment details as part of the sale transaction.

> IMPORTANT  
> This transaction is available only in the Latin American and Caribbean (LAC) region.  
> Follow these steps to process a sale transaction with installment details:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Standalone Mode.
4. Tap Installment Details.
5. Toggle Enable Installment Details to ON.
6. Configure the installment details.
7. Tap the back navigation arrow to return to the home screen.
8. Tap Sale.
9. Enter the transaction amount.
10. Tap Submit to start the transaction.

Sale with Payment Facilitator Details {#sis-standalone-mode-pymt-fac-details}
=============================================================================

Use the information to process a sale transaction with payment facilitator details when the app is in Standalone mode. This payment service enables you to include required payment facilitator details as part of the sale transaction.  
Follow these steps to process a sale transaction with payment facilitator details:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Standalone Mode.
4. Tap Payment Facilitator Details.
5. Toggle Enable Payment Facilitator Details to ON.
6. Configure the payment facilitator details.
7. Tap the back navigation arrow to return to the home screen.
8. Tap Sale.
9. Enter the transaction amount.
10. Tap Submit to start the transaction.

Sale with Tax Details {#sis-standalone-mode-sale-tax-details}
=============================================================

Use this information to process a sale transaction with tax details when the app is in Standalone mode. This type of transaction can be used to include the required tax details as part of the sale transaction.  
Follow these steps to process a sale transaction with tax details:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Standalone Mode.
4. Tap Tax Details.
5. Toggle Enable Tax Details to ON.
6. Configure the tax details.
7. Tap the back navigation arrow to return to the home screen.
8. Tap Sale
9. Enter the transaction amount.
10. Tap Submit to start the transaction.

Print a Customer or Merchant Receipt {#sis-standalone-mode-print-cust-merchant-recpt}
=====================================================================================

Use this information to print a customer or merchant receipt from a previous transaction when the app is in Standalone mode. This feature can only be used with terminals that have integrated printers.  
Follow these steps to print a customer or merchant receipt:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Transaction History.
4. Tap the transaction for which you want to email the receipt.
5. Tap Print Customer Receipt or Print Merchant Receipt.

Email a Customer Receipt {#sis-standalone-mode-email-cust-recpt}
================================================================

Use this information to email a customer receipt from a previous transaction when the app is in Standalone mode.  
Follow these steps to email a customer receipt:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Transaction History.
4. Tap the transaction for which you want to email the receipt.
5. Tap Send Receipt.

