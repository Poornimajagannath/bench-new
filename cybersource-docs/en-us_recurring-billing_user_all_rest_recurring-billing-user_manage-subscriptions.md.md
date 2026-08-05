Managing Subscriptions {#manage-subscriptions}
==============================================

You can manage subscriptions in `Manage Subscriptions` and `Token Management` areas of the `Business Center`.

#### Figure:

Subscription Flow ![](/content/dam/documentation/cybs/en-us/olh/RecurringBilling/images/subscription-status-flow-600x450.svg/jcr:content/renditions/original)  
A subscription always has one of these statuses:

Pending
:
The first payment is scheduled, or the subscription is in transition to another state.

Active
:
The subscription is currently in use. It is set with a payment instrument, and a payment is scheduled at a pre-determined frequency that you agreed upon with your customer.

Delinquent
:
When a scheduled recurring payment fails, the account is placed in a Delinquent status while the system retries the payment a number of times. If the retries all fail, the account is placed into a Suspended status.

Suspended
:
The automated retry logic failed to obtain successful payment, or you have explicitly suspended the subscription. In order to resume a suspended subscription for the next billing cycle, choose one of these options:

    * Collect a different payment method from your customer and then reactivate the subscription.
    * Cancel the subscription and create a new subscription for your customer.

Cancelled
:
You have explicitly cancelled the subscription, and it cannot be reactivated. You might cancel an active or pending subscription when you and the customer agree to end the subscription. You might choose to cancel a delinquent subscription rather than wait for the automatic retry logic to proceed. You might cancel a suspended subscription if the customer does not have an acceptable alternate payment method.
> IMPORTANT You cannot cancel a subscription within 10 minutes before or after a payment begins processing.

Completed
:
All scheduled payments were made. This is the state of a subscription that ends with all scheduled payments successfully completed. This state applies to subscriptions set up with a scheduled end date.
> IMPORTANT You cannot reactivate a completed subscription.

{#manage-subscriptions_dl_v53_cdm_y2c}

> IMPORTANT
> For information about managing subscriptions from the ` Token Management ` area in the ` Business Center `, see [Managing Subscriptions in Token Management](/docs/cybs/en-us/recurring-billing/user/all/rest/recurring-billing-user/manage-subscriptions-tms.md "").

