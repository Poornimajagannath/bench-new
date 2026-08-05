Introduction to Acceptance Devices \| Tap to Pay on iPhone Solution {#home-merch}
=================================================================================

The Acceptance Devices \| Tap to Pay on iPhone Solution enables you to use any compatible iPhone as a payment acceptance device. You can integrate the Tap to Pay on iPhone software development kit (SDK) into your iOS POS app to easily manage the payment flow.  
For information about the current version of the Tap to Pay on iPhone SDK, see the [Release Notes for Tap to Pay on iPhone Solution](/docs/cybs/en-us/tap-to-pay-ios/integration/all/rest/tap-to-pay-ios/ttp-ios-rel-notes-intro.md "").

Compatibility Requirements for iPhones {#ttpay-ios-device-reqs}
===============================================================

To accept contactless payments, your iPhone must be compatible with the Tap to Pay on iPhone Solution. These are the requirements for a compatible iPhone:

* iPhone model XS or later
* iOS version that is less than 1 year old (recommendation is to use the latest iOS version available)
  {#ttpay-ios-device-reqs_ul_pvy_4g2_hwb}

Transaction Workflow for the Tap to Pay on iPhone Solution {#ttpay-ios-workflow}
================================================================================

This diagram shows the transaction workflow for the Tap to Pay on iPhone Solution.

#### Figure: {#ttpay-ios-workflow_fig_rmy_hs5_jyb}

Tap to Pay on iPhone Solution Transaction Workflow  
![Tap to Pay on iPhone Solution transaction workflow diagram showing the sequence
of events used to process a transaction](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/tap-to-pay-ios/images/ttp-ios-sdk-sequence-diagram-600x450.svg/jcr:content/renditions/original)

1. The iOS point-of-sale (POS) app integrates to the Tap to Pay on iPhone SDK.
2. The merchant's iOS POS app sends a request to the Tap to Pay on iPhone SDK to process a payment.
3. The Tap to Pay on iPhone SDK user interface (UI) opens on the iPhone screen and guides the customer through the payment flow.
4. The Tap to Pay on iPhone SDK sends a response with the transaction result and details to the iOS POS app.

