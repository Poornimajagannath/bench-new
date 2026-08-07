Release Notes for Tap to Pay on iPhone Solution {#ttp-ios-rel-notes-intro}
==========================================================================

These release notes are organized by release name and version, from newest to oldest.  
Each release note includes these details:

* Name of release
* Type of release: app or SDK
* Version number
* Operating system: Android or iOS
* Release date: MM-DD-YYYY format

{#ttp-ios-rel-notes-intro_ul_qcb_lvk_k1c}These are the types of release notes published:


* General information
* Improvements
* New features
* Fixed issues
* Updated requirements
* Security updates
* Hot fixes
  {#ttp-ios-rel-notes-intro_ul_l24_23q_h1c}

SDK Version 3.2.0 Release Notes {#ttp-ios-rel-notes-v320-intro}
===============================================================

These release notes are for the Tap to Pay on iPhone SDK, version 3.2.0 for iOS. The release date is 10-06-2025.

New Features {#ttp-ios-rel-notes-v320-features}
===============================================

Added tip amount and total amount as tipping options.

SDK Version 3.7.0 Release Notes {#ttp-ios-rel-notes-v370-intro}
===============================================================

These release notes are for the Tap to Pay on iPhone SDK, version 3.7.0 for iOS. The release date is 05-28-2026.

General Information {#ttp-ios-rel-notes-v370-gen-info}
======================================================

* For submitting offline transactions, the `startBatchUpload()` method was replaced with the `syncSession()` method.
* Updated device activation methods.

New Features {#ttp-ios-rel-notes-v370-features}
===============================================

Added support for Spanish (Spain) and Spanish (Mexico) language variants.

Improvements {#ttp-ios-rel-notes-v370-improved}
===============================================

* Activating a device with an activation code can now be done without manually entering the activation code.
* Reactivating a device no longer requires uninstalling the app first.
* Improved error messages is shown during transactions.
* Applied general improvements to the UI.

SDK Version 3.6.0 Release Notes {#ttp-ios-rel-notes-v360-intro}
===============================================================

These release notes are for the Tap to Pay on iPhone SDK, version 3.6.0 for iOS. The release date is 04-10-2026.

General Information {#ttp-ios-rel-notes-v360-gen-info}
======================================================

The SDK 3.6.0 release introduces architectural changes that replace several core protocols and methods. Before you build with SDK 3.6.0, update integrations built with earlier SDK versions. Before upgrading from SDK 3.5.0, review these updated or new topics in the integration guide:

* Creating an SDK instance: The `mposUI` instance was replaced with a `MposUIReader` instance.
* Credentials: The `environment` field and `Credentials.Environment` type were removed. Use the standalone `MposEnvironment` enum.
* Device activation: The device enrollment methods were replaced with new activation methods.
* Payment services: The payment service transaction methods are now accessed by using the `MposUIOnline` service.
* Stand-alone credit: The return type for a stand-alone credit transaction was changed from `Result&lt;Transaction, MposUIError&gt;` to `RefundTransactionResult`.

{#ttp-ios-rel-notes-v360-gen-info_ul_pqb_1gy_l3c}  
For more information about these topics, see [Recent Revisions to This Document](/docs/gateway/en-us/tap-to-pay-ios/integration/all/rest/tap-to-pay-ios/ttpay-ios-about-guide/ttpay-ios-doc-revisions.md "").

New Features {#ttp-ios-rel-notes-v360-features}
===============================================

* Added support for Store \& Forward transactions.
* Added support for activating a device using an activation code instead of credentials.

{#ttp-ios-rel-notes-v360-features_ul_pqb_1gy_l3c}  
For more information about these topics, see[Recent Revisions to This Document](/docs/gateway/en-us/tap-to-pay-ios/integration/all/rest/tap-to-pay-ios/ttpay-ios-about-guide/ttpay-ios-doc-revisions.md "").

Improvements {#ttp-ios-rel-notes-v360-improved}
===============================================

Applied general improvements to the UI.

SDK Version 3.5.0 Release Notes {#ttp-ios-rel-notes-v350-intro}
===============================================================

These release notes are for the Tap to Pay on iPhone SDK, version 3.5.0 for iOS. The release date is 02-26-2026.

New Features {#ttp-ios-rel-notes-v350-features}
===============================================

* Added a Device Selection screen that enables merchants to enroll a previously enrolled device without manually entering the serial number.
* Added support for re-enrolling a previously enrolled device by providing the stored serial number to the SDK.
  {#ttp-ios-rel-notes-v350-features_ul_pqb_1gy_l3c}

Improvements {#ttp-ios-rel-notes-v350-improved}
===============================================

* Added the ability to configure the enrollment process to show a list of previously enrolled devices or to enable the merchant to enter the device serial number manually.
* Added the ability to configure the enrollment process to show or hide the serial number confirmation screen after successful enrollment.
* Improved the ability to debug your application during development.
* Improved error messages that can appear during transaction processing.
* Applied general improvements to the UI.

SDK Version 3.3.0 Release Notes {#ttp-ios-rel-notes-v330-intro}
===============================================================

These release notes are for the Tap to Pay on iPhone SDK, version 3.3.0 for iOS. The release date is 10-31-2025.

Improvements {#ttp-ios-rel-notes-v330-improved}
===============================================

* Improved the error messages that can appear during transaction processing.
* Applied general improvements to UI.
  {#ttp-ios-rel-notes-v330-improved_ul_dvj_rpt_dhc}

Fixed Issues {#ttp-ios-rel-notes-v330-fixed}
============================================

* Fixed the issue that occasionally caused the Signature screen to be shown twice.
* Fixed the issue that caused the Increment button to be shown on the Summary screen after the transaction is fully refunded.
  {#ttp-ios-rel-notes-v330-fixed_ul_dvj_rpt_dhc}

