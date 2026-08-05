Introduction to Recurring Billing {#recur-bill-dev-intro}
=========================================================

This guide explains how to integrate the Recurring Billing REST API into your payment system.  
The Recurring Billing service enables you to create and manage payment plans and subscriptions for recurring payment schedules. It automates the storage and handling of your customer's payment information and personal data within secure Visa data centers in compliance with credentials-on-file (COF) best practices. Storage risks and the PCI DSS scope are reduced through the use of the `Token Management Service` (`TMS`).  
`Cybersource` Recurring Billing consists of these three elements:

* **Plan:** Stores the billing schedule.
* **Subscription:** Combines the token and plan and defines the subscription start date, name, and description.
* **Token:** Stores customer billing, shipping, and payment details.  
  For information about Recurring Billing in the `Business Center`, see the [Recurring Billing User Guide](https://developer.cybersource.com/docs/cybs/en-us/recurring-billing/user/all/rest/recurring-billing-user/recur-bill-services-intro.md "").  
  Recurring payments can also be handled with the payments API. Merchant-initiated transactions (MITs) are part of the payments API. For more information on recurring payments using MITs, see the Recurring Payments section in the [Payments Developer Guide](https://developer.cybersource.com/docs.md#PaymentServices "").
  IMPORTANT Do not use this document if you are using the payments API to process recurring payments. When using payments API for MITs, you must capture and store the customer's payment credentials manually. Also, you send the payments API MIT requests to different endpoints than you send the recurring billing requests.  
  The Recurring Billing service is available for the `REST` API only. The service is not available in the `SCMP` API or the `Simple Order` API.

> IMPORTANT
> These Latin American processors are not yet supported for Recurring Billing services:
>
> * ` Comercio Latino `
> * ` Prosa `

Prerequisites
-------------

Your account must be enabled for Recurring Billing and configured for the `Token Management Service` (`TMS`). The customer token is the only token type that can be used with Recurring Billing.  
For more information about `TMS`, see the [`Token Management Service` REST API Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/tms/developer/ctv/rest/tms/tms-overview.md "").

Getting Started with the REST API
---------------------------------

If you have not already, you must register and obtain authentication credentials for the REST API.  
Go to the `Cybersource` [Hello world sandbox](https://developer.cybersource.com/hello-world.md "") in the Developer Center.  
When your system is REST compliant, you can test your Recurring Billing integration by sending requests to the `Cybersource` test server. See *[Getting Started with REST Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-about-guide.md "")*
