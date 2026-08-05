PIN Debit Optional Features {#pd-feature-intro}
===============================================

This section describes the optional features that are available for PIN Debit processing.

Cash Back {#pd-feature-cash-back-intro}
=======================================

This feature enables a customer in a card-present situation to add a cash-back amount to the total transaction amount when using a debit card. The customer receives that amount in cash along with the purchase. For example, a customer purchasing products totaling 18.99 might ask for 20.00 cash back. They would pay a total of 38.99 (18.99 + 20.00) with their debit card and receive 20.00 in cash along with their products.
IMPORTANT Cash back is not supported on partial authorizations.  
To use this feature, include the orderInformation.amountDetails.cashbackAmount field in a PIN debit purchase request.  
When the cash-back amount is 0.00, do not include the orderInformation.amountDetails.cashbackAmount field.  
For more information, see [PIN Debit Purchase with Contactless EMV and Cash Back](/docs/cybs/en-us/pin-debit/developer/ctv/rest/pin-debit/pd-processing/pd-cash-back-cntctlss-task.md "").

Merchant Descriptors {#pd-feature-merchdescr-intro}
===================================================

This feature enables you to submit merchant descriptor values that are displayed on a cardholder's statement.
IMPORTANT Before using merchant descriptors in your requests, check with your bank to learn whether you must pre-register your merchant descriptor information with them.  
`Cybersource` always provides merchant descriptor information to the acquirer for all of your PIN debit purchase and PIN debit credit transactions. When you do not include a particular merchant descriptor in your PIN debit purchase or PIN debit credit request, `Cybersource` uses the corresponding value from your merchant account.  
For more information, see [PIN Debit Purchase with Swiped Track Data and Merchant Descriptors](/docs/cybs/en-us/pin-debit/developer/ctv/rest/pin-debit/pd-processing/pd-purch-swipe-merchdescr-task.md "").

Merchant Descriptor Fields
--------------------------

You can include these merchant descriptor fields in a PIN debit purchase or PIN debit credit:

merchantInformation.merchantDescriptor.administrativeArea
:
If you include this field in a request, you must also include merchantInformation.merchantDescriptor.country.

merchantInformation.merchantDescriptor.alternateName
:

merchantInformation.merchantDescriptor.country
:
If you include this field in a request, you must also include merchantInformation.merchantDescriptor.administrativeArea.

merchantInformation.merchantDescriptor.locality
:

merchantInformation.merchantDescriptor.name
:

merchantInformation.merchantDescriptor.postalCode
:

Merchant-Inititated Reversals {#pd-feature-mit-reversal-intro}
==============================================================

When you do not receive a response message after sending a PIN debit purchase or credit request, your request might have timed out. This feature enables you to reverse a timed-out transaction within 2 hours of the original request.  
When using the merchant-initiated reversals feature, include the clientReferenceInformation.transactionId field in your original request for a PIN debit purchase. The value of the transaction ID must be unique for 60 days. It links your reversal request to your original request.

Partial Authorizations {#pd-feature-partial-auth-intro}
=======================================================

For PIN debit cards, the issuing bank can approve a partial amount if the balance on the card is less than the requested authorization amount.  
Support for your processor and card type does not guarantee a partial authorization. The issuing bank decides whether or not to approve a partial amount. When the balance on a debit card or prepaid card is less than the requested authorization amount, the issuing bank can approve a partial amount. When this happens, you can accept multiple forms of payment for the order starting with some or all of the approved amount, followed by one or more different payment methods.  
You must opt in to be able to receive and capture partial authorizations. Choose one of these options:

* Call `Cybersource` customer support to have your merchant account enabled for partial authorizations. When you do this, all of your authorization requests are enabled for partial authorizations.


* Set the processingInformation.authorizationOptions.partialAuthIndicator field to `true` in a PIN debit purchase request. When you do this, only that specific transaction is enabled for partial authorization.

When your account is enabled for partial authorizations, you can disable partial authorization for a specific transaction by setting the processingInformation.authorizationOptions.partialAuthIndicator field to `false` in the PIN debit purchase request.  
For more information, see [PIN Debit Partial Authorization with Swiped Track Data](/docs/cybs/en-us/pin-debit/developer/ctv/rest/pin-debit/pd-processing/pd-purch-swipe-partial-task.md "").

Payment Network Tokens {#pd-feature-pnt-intro}
==============================================

Payment network tokens are supported as card-present contactless transactions.

Surcharge Fees {#pd-feature-surcharge-intro}
============================================

This feature enables you to charge the customer a surcharge fee for a PIN debit purchase or credit transaction.
IMPORTANT Surcharge fees are not allowed on debit or prepaid cards in the U.S.  
Include the surcharge amount in the total transaction amount, and set the orderInformation.amountDetails.surcharge.amount field to the surcharge amount. This information is passed to the issuer and acquirer for tracking. The issuer can provide information about the surcharge amount to the customer.  
When there is no surcharge fee, do not include the orderInformation.amountDetails.surcharge.amount field in the request.  
For more information, see [PIN Debit Purchase with Contactless EMV and a Surcharge Fee](/docs/cybs/en-us/pin-debit/developer/ctv/rest/pin-debit/pd-processing/pd-cntctlss-purch-srchrg-task.md "").
