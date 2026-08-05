Standalone Mode Payment Services {#ttp-sis-pymnt-svcs-standalone-mode-intro}
============================================================================

Use the information in this section to process payment services in the Acceptance Devices app when operated in Standalone mode.  
These are some benefits of using Standalone mode:

* Start transactions directly from the Android device.

* Fastest way to begin accepting payments.

* No integration required with a point-of-sale (POS) system.

* Serves as a backup option when your POS system is unavailable for Local or Cloud semi-integrated modes.
  {#ttp-sis-pymnt-svcs-standalone-mode-intro_ul_f1b_dhp_vzb}
  IMPORTANT When the Acceptance Devices app is in Standalone mode, the Android device does not communicate with your POS system to exchange transaction details. You are responsible for reconciling transactions with your internal systems and records.  
  For information about other modes available in the Acceptance Devices app, see:

* [Local Mode Payment Services](/docs/cybs/en-us/tap-to-phone-sis/integration/all/rest/tap-to-phone-sis/ttp-sis-pymnt-svcs-intro.md "")

* [Cloud Mode Payment Services](/docs/cybs/en-us/tap-to-phone-sis/integration/all/rest/tap-to-phone-sis/ttp-sis-pymnt-svcs-cloud-mode-intro.md "")
  {#ttp-sis-pymnt-svcs-standalone-mode-intro_ul_l5b_yqm_3fc}

Enable Standalone Mode in the Acceptance Devices App {#ttp-sis-standalone-mode-enable}
======================================================================================

Follow these steps to enable Standalone mode in the Acceptance Devices app:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Standalone Mode.
4. Toggle Enable Standalone Mode to ON.
5. Choose the currency in which you want to process transactions. Tap Save.
6. If you want to enable custom merchant reference codes, toggle Custom Transaction Reference to ON.
7. Tap the back navigation arrow to return to the home screen. You can now process transactions in Standalone mode.

Sale {#ttp-sis-standalone-mode-sale}
====================================

Use the information in this section to process a sale transaction when the app is in Standalone mode. This type of transaction combines an authorization and a capture into a single transaction.  
Follow these steps to process a sale transaction:

1. In the Acceptance Devices app, tap Sale.
2. Enter the transaction amount.
3. Tap Submit to start the transaction.

Refund {#ttp-sis-standalone-mode-refund}
========================================

Use the information in this section to process a refund when the app is in Standalone mode. This type of refund includes a reference to the original transaction for a full or partial transaction amount.  
Stand-alone credits are also supported in this Acceptance Devices solution. For more information, see [Stand-Alone Credit](/docs/cybs/en-us/tap-to-phone-sis/integration/all/rest/tap-to-phone-sis/ttp-sis-pymnt-svcs-standalone-mode-intro/ttp-sis-standalone-mode-standalone-credit.md "").  
Follow these steps to process a refund:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Transaction History.
4. Tap the transaction you want to refund.
5. Tap Refund.
6. Enter the transaction amount.
7. Tap Refund to start the transaction.

Stand-Alone Credit {#ttp-sis-standalone-mode-standalone-credit}
===============================================================

Use the information in this section to process a stand-alone credit when the app is in Standalone mode. This type of transaction is used to process a credit without reference to the original transaction. The customer must present their payment card for this type of transaction.

> WARNING
> When processing a stand-alone credit, there is no limit on the credit amount because there is no reference to the original transaction amount. The recommendation is to use a refund transaction whenever possible. For more information, see [Refund](/docs/cybs/en-us/tap-to-phone-sis/integration/all/rest/tap-to-phone-sis/ttp-sis-pymnt-svcs-standalone-mode-intro/ttp-sis-standalone-mode-refund.md "").  
> Follow these steps to process a stand-alone credit:

1. In the Acceptance Devices app, tap Other Transactions.
2. Tap Refund.
3. Enter your Acceptance Devices app passcode.
4. Enter the transaction amount.
5. Tap Submit to start the transaction.

Sale with On-Reader Tipping {#ttp-sis-standalone-mode-sale-on-reader-tip}
=========================================================================

Use the information in this section to process a sale with on-reader tipping in Standalone mode. At the start of each transaction, the terminal prompts the customer to add a tip by showing suggested tip amounts. The customer selects or enters a tip amount on the terminal before presenting their payment card.  
Follow these steps to process a sale with on-reader tipping:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Standalone Mode.
4. Toggle Ask for Tip to ON.
5. Tap the back navigation arrow to return to the home screen.
6. Tap Sale.
7. Enter the transaction amount.
8. Tap Submit to start the transaction.

Pre-Authorization {#ttp-sis-standalone-mode-pre-auth}
=====================================================

Use the information in this section to process a pre-authorization for an initial amount in Standalone mode. A pre-authorization transaction places a temporary hold on the customer's payment card, which can be captured at a later time.  
Most authorizations expire in 5 to 7 days. The issuing bank sets the length of time before expiration. When an authorization expires with the issuing bank, your bank or processor might require that you re-submit an authorization request and include a request for capture in the same message. For more information, see [Capture](/docs/cybs/en-us/tap-to-phone-sis/integration/all/rest/tap-to-phone-sis/ttp-sis-pymnt-svcs-standalone-mode-intro/ttp-sis-standalone-mode-capture.md "").  
Follow these steps to process a pre-authorization:

1. In the Acceptance Devices app, tap Other Transactions.
2. Tap Pre-Authorization.
3. Enter the transaction amount.
4. Tap Submit to start the transaction.

Capture {#ttp-sis-standalone-mode-capture}
==========================================

Use the information in this section to capture a pre-authorized transaction in Standalone mode. The capture request references the approved pre-authorization request.  
Follow these steps to process a capture:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Transaction History.
4. Tap the transaction that you want to capture.
5. Tap Capture.
6. Enter the transaction amount.
7. Tap Capture to start the transaction.

Sale with Installment Details {#ttp-sis-standalone-mode-sale-install-details}
=============================================================================

Use the information in this section to process a sale transaction with installment details when the app is in Standalone mode. This type of transaction can be used to include the required installment details as part of the sale transaction.  
This transaction is available only in the Latin American and Caribbean (LAC) region.  
Follow these steps to process a sale transaction with installment details:

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

Sale with Payment Facilitator Details {#ttp-sis-standalone-mode-pymt-fac-details}
=================================================================================

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

Sale with Tax Details {#ttp-sis-standalone-mode-sale-tax-details}
=================================================================

Use the information in this section to process a sale transaction with tax details when the app is in Standalone mode. This type of transaction can be used to include the required tax details as part of the sale transaction.  
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

Email a Customer Receipt {#ttp-sis-standalone-mode-email-cust-recpt}
====================================================================

Use the information in this section to email a customer receipt from a previous transaction when the app is in Standalone mode.  
Follow these steps to email a customer receipt:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Transaction History.
4. Tap the transaction for which you want to email the receipt.
5. Tap Send Receipt.

