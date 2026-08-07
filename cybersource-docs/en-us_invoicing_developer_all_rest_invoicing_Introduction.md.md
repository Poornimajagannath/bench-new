Introduction to Invoicing {#Introduction}
=========================================

The Invoicing API enables you to create and send invoices as well as track outstanding invoices. Your customers can pay using their preferred payment method from any device on a secure `Cybersource` hosted website. Automated reminders are available to help you remind customers of upcoming due dates or overdue invoices. For more information, see [Invoicing API Requests](/docs/cybs/en-us/invoicing/developer/all/rest/invoicing/invoicing-services-intro.md "").  
You can also customize your invoice payment page to display your brand logo and color, as well as add custom messages to your invoice emails. Shipping information and phone numbers can also be collected at the time of payment. For more information, see [Invoicing Settings API Requests](/docs/cybs/en-us/invoicing/developer/all/rest/invoicing/invoicing-settings-intro.md "").  
The Invoicing API uses Cybersource's `Unified Checkout` to securely process payments so that you do not have to handle confidential payment data. Fraud and risk management tools are incorporated into `Unified Checkout` to prevent fraud and reduce chargebacks. For additional security, you can add payer authentication to your invoice payment processing. For more information, see [Add Payer Authentication to Invoicing](/docs/cybs/en-us/invoicing/developer/all/rest/invoicing/invoicing-features-intro.md "").  
To receive notifications when an invoice is paid, sent, or cancelled, you can create a subscription to receive invoicing webhook notifications. For more information, see [Webhook Notifications for Invoicing](/docs/cybs/en-us/invoicing/developer/all/rest/invoicing/invoicing-webhooks-intro.md "").

> IMPORTANT
> The merchant is responsible for complying with any legal and tax requirements when issuing invoices to clients. ` Cybersource ` does not certify that the invoicing tool meets any such client requirements.
> IMPORTANT
> Invoicing fields are strictly designated for non-personal data and must not be used to capture personally identifying information. You are prohibited from capturing, obtaining, or transmitting any personally identifying information in or through any invoicing fields, including merchant-defined data fields.  
> Personally identifying information includes, but is not limited to, address, payment card number, social security number, driver's license number, state-issued identification number, passport number, and card verification numbers (CVV, CVC2, CVV2, CID, CVN). In the event it is discovered that a merchant is capturing and/or transmitting personally identifying information, whether or not intentionally, the merchant's account is immediately suspended, which results in a rejection of any and all transaction requests submitted by the merchant after the point of suspension.

Requirements
------------

The Invoicing API requires a transaction MID account and API authentication before you can begin sending API messages to `Cybersource`. For more information, see the [REST Getting Started User Guide](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md "") .

Configure `Unified Checkout`
----------------------------

Invoicing supports `Unified Checkout`, which enables you to accept numerous types of digital payments, such as Apple Pay, `Click to Pay`, and Google Pay.  
For more information about enabling these digital payments using `Unified Checkout`, see the [Enable Digital Payments](https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro.md "") section in the *Digital Accept Secure Integration Developer Guide*.

Tokenization for Merchant-Initiated Transactions {#Introduction_mits}
---------------------------------------------------------------------

You can create Token Management Service (TMS) tokens from invoice transactions using Transaction Management in the `Business Center`.

> IMPORTANT
> If you create and use TMS tokens for merchant-initiated transactions (MITs), you must comply with the **Consent Agreement Provisions** as stated in the [*Improving Authorization Management for Transactions with Stored Credentials*](https://usa.relay.com/dam/VCOM/global/support-legal/documents/stored-credential-transaction-framework-vbs-10-may-17.pdf "") guide.

Sandbox Testing {#Introduction_invoice-settings-toc}
----------------------------------------------------

You can test invoicing API requests using the [Invoicing API Reference](https://developer.cybersource.com/api-reference-assets/index.md#invoicing "") in the `Cybersource` developer center.
