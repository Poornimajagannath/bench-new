Additional Features {#recur-bill-addl-feat}
===========================================

Recurring Billing includes these additional features.

System Retry Logic {#recur-bill-sys-retry}
==========================================

`Payment Gateway` automatically retries failed recurring payments based on the type of decline received from the service. The service retries the internal and external payment declines.  
If the Recurring Billing service encounters an internal processing error without sending the request out to the banking network, the service retries the payment until the error is resolved.  
If the recurring billing service encounters an external processing error when the request is sent out to the banking network, `Payment Gateway` retries the payment before changing the subscription status to suspended.  
If the issuer provides a reason code like Do Not Retry, `Payment Gateway` stops all retry attempts. `Payment Gateway` immediately updates the subscription status to suspended.  
The maximum number of retries is five times and is based on the billing frequency. During the retry period, `Payment Gateway` changes the subscription status to delinquent.  
This example shows the system retry logic based on the billing frequency:

* **Daily**: retry 1 hour later, 1 time
* **Monthly**: retry every 2 days, 5 times
* **Weekly**: retry every 1 day, 3 times
* **Yearly**: retry every 15 days, 3 times  
  For a recurring payment that has a custom billing frequency, the Recurring Billing service retries a failed payment based on the billing frequency. As an example, suppose a payment fails for a recurring billing on a 14-day cycle. The Recurring Billing Service uses the Daily retry logic and every 2 weeks uses the Weekly retry logic, even if the duration is the same.

Merchant-Initiated Transactions {#recur-bill-mit}
=================================================

For information about merchant-initiated transactions, see [Support for Merchant-Initiated Transactions and Credential-on-File for Relay, Mastercard, and Discover](https://support.example.com/s/article/Support-for-Merchant-Initiated-Transactions-and-Credential-on-File-for-Relay-Mastercard-and-Discover "").

Customer Notifications {#recur-bill-cust-not}
=============================================

The Recurring Billing service sends email notifications to customers using the email address stored on the customer token. The system sends notifications for three defined payment events:

* Prepayment notification: notification of an upcoming recurring payment.
* Successful payment notification: notification of a successful recurring payment.
* Failed payment notification: notification of recurring payment failure.  
  `Payment Gateway` sends email notifications from a `Payment Gateway` email address.
  IMPORTANT Some mandates require that customers are notified. If notifications are disabled, the merchant is responsible for sending notifications to satisfy any mandates requirements.  
  You can disable notifications in the Recurring Billing settings in the `Business Center`. For more information, see the [*Recurring Billing User Guide*](https://developer.example.com/docs/gateway/en-us/recurring-billing/user/all/rest/recurring-billing-user/recurring-billing-user-about-guide.md "").

Example: Notification of Upcoming Subscription Payment
------------------------------------------------------

Hello,  
Your recurring subscription will be charged to your payment card on file on `${paymentDate}`.  
**Subscription ID** : `${subscriptionId}`  
**Subscription Name** : `${subscriptionName}`  
**Billing Amount** : `${billingAmount} ${currency}`  
**Set-up Fee** : `${setupFee} ${currency}`  
Thank you,  
`${merchantName}`

Example: Notification of Successful Subscription Payment
--------------------------------------------------------

Hello,  
Your recurring subscription has been successfully charged to your payment card on file.  
**Subscription ID** : `${subscriptionId}`  
**Subscription Name** : `${subscriptionName}`  
**Billing Amount** : `${billingAmount} ${currency}`  
**Set-up Fee** : `${setupFee} ${currency}`  
**Transaction ID** : `${transactionId}`  
**Transaction Date** : `${paymentDate}`  
Thank you,  
`${merchantName}`

Example: Notification of Failed Subscription Payment
----------------------------------------------------

Hello,  
Your recurring subscription has failed to charge to your payment card on file.  
**Subscription ID** : `${subscriptionId}`  
**Subscription Name** : `${subscriptionName}`  
**Billing Amount** : `${billingAmount} ${currency}`  
**Setup Fee** : `${setupFee} ${currency}`  
**Transaction ID** : `${transactionId}`  
**Transaction Date** : `${paymentDate}`  
Thank you,  
`${merchantName}`

`Decision Manager` Integration {#recur-bill-dm-int}
===================================================

Recurring transactions are considered low risk compared to unscheduled payments. Therefore, when the `Decision Manager` fraud detection system is enabled on your account, `Payment Gateway` does not submit recurring billing transactions to `Decision Manager` for fraud screening.  
For more information about the `Decision Manager`, you can access the documentation by logging in to the `Business Center`.

Account Updater Integration {#recur-bill-au}
============================================

Account Updater is integrated with the Recurring Billing functionality so that your customer subscriptions can be kept current with credit card data changes. These changes can include a new expiration date, a new credit card number, or a brand change such as a change from Relay to Mastercard.  
For more information relating to Account Updater, contact your `Payment Gateway` representative.

Related Information
-------------------

* [Account Updater Developer Guide](https://developer.example.com/library/documentation/dev_guides/Account_Updater_UG/Account_Updater.pdf "")

