Introduction to `Pay by Link` {#paybylink-intro}
================================================

`Pay by Link` is an easy and fast way to securely sell products or receive donations online. You can send and display a secure payment link across physical and digital marketing. This solution is ideal for distributing the same payment link to multiple customers.  
Integrate `Pay by Link` APIs into your own system to automate the creation and management of payment links. Links for making purchases are referred to as *fixed-price links* , and links for making donations are referred to as *customer-set price links*.

**Benefits**
:
`Pay by Link` enables you to:

    * Get started with a fast and easy setup.
    * Grow your business and revenue through multiple sales channels.
    * Offer customers the convenience of popular payment options.
    * Get paid from any connected device: mobile, tablet, and desktop.
    * Reduce chargebacks and fraud through easy integration with Decision Manager or Fraud Management Essentials.
    * Maintain PCI security and compliance, and minimize future PCI scoping.

**Requirements**
:
Before you can begin using `Pay by Link`, your merchant account must be enabled for Unified Checkout. If you are a merchant, contact your sales representative for more information.

    If you are a portfolio user, you can use the `Business Center` to board and enable your merchants for Unified Checkout and `Pay by Link`. For more information, see the [`Pay by Link`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/templates-matrix-intro/templates-matrix-pay-by-link.md "") section in the *Boarding User Guide*.

    To access `Pay by Link` in the `Business Center`, see [Using the Business Center](/docs/cybs/en-us/paybylink/developer/all/rest/paybylink/paybylink-ebc-intro.md "").

    > IMPORTANT  
    > ` Pay by Link ` fields are strictly designated for non-personal data and must not be used to capture personally identifying information. You are prohibited from capturing, obtaining, or transmitting any personally identifying information in or through any ` Pay by Link ` fields, including merchant-defined data fields.  
    > Personally identifying information includes, but is not limited to, address, payment card number, social security number, driver's license number, state-issued identification number, passport number, and card verification numbers (CVV, CVC2, CVV2, CID, CVN). In the event it is discovered that a merchant is capturing and/or transmitting personally identifying information, whether or not intentionally, the merchant's account is immediately suspended, which results in a rejection of any and all transaction requests submitted by the merchant after the point of suspension.

Tokenization for Merchant-Initiated Transactions
------------------------------------------------

You can create Token Management Service (TMS) tokens from `Pay by Link` transactions using Transaction Management in the `Business Center`.

> IMPORTANT
> If you create and use TMS tokens for merchant-initiated transactions (MITs), you must comply with the **Consent Agreement Provisions** as stated in the [*Improving Authorization Management for Transactions with Stored Credentials*](https://usa.visa.com/dam/VCOM/global/support-legal/documents/stored-credential-transaction-framework-vbs-10-may-17.pdf "") guide.

