Release Notes for PAX All-in-One Android Solution {#pax-aio-release-notes-intro}
================================================================================

These release notes are organized by release name and version, from newest to oldest.  
Each release note includes these details:

* Name of release
* Type of release: app or SDK
* Version number
* Operating system: Android or iOS
* Release date: MM-DD-YYYY format

{#pax-aio-release-notes-intro_ul_qcb_lvk_k1c}These are the types of release notes published:


* General information
* Improvements
* New features
* Fixed issues
* Updated requirements
* Security updates
* Hot fixes
  {#pax-aio-release-notes-intro_ul_l24_23q_h1c}

SDK Version 2.115.0 Release Notes {#ttp-aio-rel-notes-v2-115-intro}
===================================================================

These release notes are for the PAX All-in-One and Tap to Pay on Android SDKs, version 2.115.0 for Android. The release date is 07-20-2026.

Fixed Issues {#ttp-aio-rel-notes-v2-115-fixed}
==============================================

Fixed an intermittent issue that could cause the device to crash during contactless transactions.

SDK Version 2.114.0 Release Notes {#ttp-aio-rel-notes-v2-114-intro}
===================================================================

These release notes are for the PAX All-in-One and Tap to Pay on Android SDKs, version 2.114.0 for Android. The release date is 06-09-2026.

New Features {#ttp-aio-rel-notes-v2-114-features}
=================================================

The solution supports adding these types of details during transactions:

* Airline
* Auto rental
* Billing and shipping
  {#ttp-aio-rel-notes-v2-114-features_ul_tgs_wkb_r3c}

Improvements {#ttp-aio-rel-notes-v2-114-improve}
================================================

Improved the user experience when performing an EBT balance inquiry.

SDK Version 2.113.0 Release Notes {#ttp-aio-rel-notes-v2-113-intro}
===================================================================

These release notes are for the PAX All-in-One and Tap to Pay on Android SDKs, version 2.113.0 for Android. The release date is 05-26-2026.

Fixed Issues {#ttp-aio-rel-notes-v2-113-fixed}
==============================================

* Fixed an issue where the secure PIN keyboard was incorrectly positioned on the PAX A3700 device screen, obscuring the PIN entry field.
* Fixed an issue where the `colorScheme` property of `uiConfiguration` was ignored for Tap to Pay integrations.
  {#ttp-aio-rel-notes-v2-113-fixed_ul_nfy_pg5_jjc}

SDK Version 2.112.0 Release Notes {#ttp-aio-rel-notes-v2-112-intro}
===================================================================

These release notes are for the PAX All-in-One and Tap to Pay on Android SDKs, version 2.112.0 for Android. The release date is 04-20-2026.

Improvements {#ttp-aio-rel-notes-v2-112-improve}
================================================

Applied general fixes to the UI.

Fixed Issues {#ttp-aio-rel-notes-v2-112-fixed}
==============================================

Fixed an intermittent issue that caused email receipts to display incorrect locale-specific formatting.

Archive of Release Notes {#ttp-aio-release-notes-archive-intro}
===============================================================

This archive of release notes for the PAX All-in-One Android Solution and Tap to Pay on Android Solution is organized by release name and version, from newest to oldest. For information about current releases, see [Release Notes for PAX All-in-One Android Solution](https://developer.example.com/docs/gateway/en-us/pax-all-in-one/integration/all/na/pax-all-in-one/pax-aio-release-notes-intro.md "") and . Also see, [Release Notes for Tap to Phone Android Solution](https://developer.example.com/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/ttp-release-notes-intro.md "").  
Each release note includes these details:

* Name of release
* Type of release: app or SDK
* Version number
* Operating system: Android or iOS
* Release date: MM-DD-YYYY format

{#ttp-aio-release-notes-archive-intro_ul_qcb_lvk_k1c1}  
These are the types of release notes published:

* General information
* Improvements
* New features
* Fixed issues
* Updated requirements
* Security updates
* Hot fixes
  {#ttp-aio-release-notes-archive-intro_ul_l24_23q_h1c1}

SDK Version 2.111.0 Release Notes {#ttp-aio-rel-notes-v2-111-intro}
===================================================================

These release notes are for the PAX All-in-One and Tap to Pay on Android SDKs, version 2.111.0 for Android. The release date is 03-15-2026.

New Features {#ttp-aio-rel-notes-v2-111-features}
=================================================

Added support for these new devices and features:

* PAX A6650, A6630, A99, and A50 payment terminals.
* Printing custom content when using PAX terminals with integrated printers.
* Providing lodging details during a transaction.
* Enabling Kiosk mode on PAX terminals.
* Meeza card type, Egypt's national payment scheme.
  {#ttp-aio-rel-notes-v2-111-features_ul_tgs_wkb_r3c}

SDK Version 2.110.0 Release Notes {#ttp-aio-rel-notes-v2-110-intro}
===================================================================

These release notes are for the PAX All-in-One and Tap to Pay on Android SDKs, version 2.110.0 for Android. The release date is 02-16-2026.

New Features {#ttp-aio-rel-notes-v2-110-features}
=================================================

Tap to Pay: Added support for processing transactions in multiple currencies with a single device enrollment.

Improvements {#ttp-aio-rel-notes-v2-110-improve}
================================================

* Improved the user experience when performing a magstripe transaction.
* Improved error messages shown during transactions.
* Tap to Pay: Re-enrolling a device no longer requires clearing Tap to Pay Ready App data.
  {#ttp-aio-rel-notes-v2-110-improve_ul_hqr_4yg_33c}

Fixed Issues {#ttp-aio-rel-notes-v2-110-fixed}
==============================================

* Tap to Pay: Fixed the issue where the enrollment screen appeared in dark mode even when the app was not set to dark mode.
* Fixed the issue that could prevent the credit and debit selection from appearing during a magstripe transaction.
* Fixed the issue where an oversized toolbar logo was not resized correctly.
* Applied general UI fixes.
  {#ttp-aio-rel-notes-v2-110-fixed_ul_qjk_5yg_33c}

General Information {#ttp-aio-rel-notes-v2-110-general}
=======================================================

Deprecated AccessoryParameters from the `UiConfiguration` instance. Starting from this SDK version, use `AccessoryParameters` in the `mposUI` instance instead.

SDK Version 2.109.0 Release Notes {#ttp-aio-rel-notes-v2-109-intro}
===================================================================

These release notes are for the PAX All-in-One and Tap to Pay on Android SDKs, version 2.109.0 for Android. The release date is 01-22-2026.

New Features {#ttp-aio-rel-notes-v2-109-features}
=================================================

Added the ability to configure the maximum amount allowed for an offline transaction and the maximum total amount allowed for an offline transaction batch submitted for authorization.

Fixed Issues {#ttp-aio-rel-notes-v2-109-fixed}
==============================================

Applied general fixes to UI.

SDK Version 2.108.0 Release Notes {#ttp-aio-rel-notes-v2-108-0-intro}
=====================================================================

These release notes are for the PAX All-in-One and Tap to Pay on Android SDKs, version 2.108.0 for Android. The release date is 12-03-2025.

New Features {#ttp-aio-rel-notes-v2-108-0-features}
===================================================

Added the ability to perform an incremental authorization on the Summary screen.

Improvements {#ttp-aio-rel-notes-v2-108-0-improve}
==================================================

Improved the tipping calculation to exclude tax amounts.

Fixed Issues {#ttp-aio-rel-notes-v2-108-0-fixed}
================================================

Fixed the issue that rarely caused a crash when performing a magstripe transaction.

General Information {#ttp-aio-rel-notes-v2-108-0-general}
=========================================================

Removed the `SHOW_TOTAL_PREAUTHORIZED` configuration option from the Summary screen features.

SDK Version 2.107.0 Release Notes {#ttp-aio-rel-notes-v2-107-0-intro}
=====================================================================

These release notes are for the PAX All-in-One and Tap to Pay on Android SDKs, version 2.107.0 for Android. The release date is 11-19-2025.

New Features {#ttp-aio-rel-notes-v2-107-0-newfeatures}
======================================================

Tap to Pay: Added support for Discover and Diners payment cards.

Improvements {#ttp-aio-rel-notes-v2-107-0-improve}
==================================================

Improved the logic for displaying the Summary screen features.

Fixed Issues {#ttp-aio-rel-notes-v2-107-0-fixed}
================================================

* Fixed the issue that occasionally caused stand-alone credit transactions to stall.
* Fixed the issue that caused the SDK to crash when providing tax, installments, or payment facilitator details.
* PAX: Fixed the issue that caused the Retry button to not work after a failed receipt print for a completed transaction.
* Tap to Pay: Fixed the issue that caused the Tap icon to not appear on the Present Card screen.
* Tap to Pay: Fixed the issue that occasionally caused the touch area to not align correctly with the Cancel button.

General Information {#ttp-aio-rel-notes-v2-107-0-general}
=========================================================

* Deprecated PayButton 1.0 from the SDK. It will be removed from the next release.
* Removed the `defaultSummaryFeature` configuration option from the Summary screen parameters.

SDK Version 2.106.0 Release Notes {#ttp-aio-rel-notes-v2-106-0-intro}
=====================================================================

These release notes are for the PAX All-in-One and Tap to Pay on Android SDKs, version 2.106.0 for Android. The release date is 10-09-2025.

New Features {#ttp-aio-rel-notes-v2-106-0-newfeatures}
======================================================

* PAX: Added the ability to process Electronic Benefit Transfer (EBT) payment card transactions.
* PAX: Added the ability to read non-PCI custom magstripe cards such as gift cards and loyalty program cards.

SDK Version 2.105.0 Release Notes {#ttp-aio-rel-notes-v2-105-0-intro}
=====================================================================

These release notes are for the PAX All-in-One and Tap to Pay on Android SDKs, version 2.105.0 for Android. The release date is 09-15-2025.

Improvements {#ttp-aio-rel-notes-v2-105-0-improve}
==================================================

Tap to Pay: Added the ability to configure the enrollment process to show or hide the serial number confirmation screen after a successful enrollment.

Fixed Issues {#ttp-aio-rel-notes-v2-105-0-fixed}
================================================

* Fixed the issue that caused the SDK to occasionally crash while using the tipping feature in some languages.
* Fixed the issue that caused automatic printing to occasionally fail when performing a refund.

SDK Version 2.104.0 Release Notes {#ttp-aio-rel-notes-v2-104-0-intro}
=====================================================================

These release notes are for the PAX All-in-One and Tap to Pay on Android SDKs, version 2.104.0 for Android. The release date is 08-18-2025.

Improvements {#ttp-aio-rel-notes-v2-104-0-improve}
==================================================

* Improved the user experience on some screens by removing the requirement for user interaction.
* Improved the error messages that can appear during transactions.
* Tap to Pay Phone: Added the ability to configure the enrollment process to show a list of previously enrolled devices or to enable the merchant to enter the device serial number manually.
  {#ttp-aio-rel-notes-v2-104-0-improve_ul_oqp_hrh_3gc}

SDK Version 2.103.1 Release Notes {#ttp-aio-release-notes-v2-103-1-intro}
=========================================================================

These release notes are for the PAX All-in-One and Tap to Pay on Android SDKs, version 2.103.1 for Android. The release date is 07-24-2025.

Fixed Issues {#ttp-aio-release-notes-v2-103-1-fixed-issues}
===========================================================

Fixed the issue that caused a blank screen to occasionally appear on the device after a transaction processes.

SDK Version 2.103.0 Release Notes {#ttp-aio-release-notes-v2-103-0-intro}
=========================================================================

These release notes are for the PAX All-in-One and Tap to Pay on Android SDKs, version 2.103.0 for Android. The release date is 07-16-2025.

New Features {#ttp-aio-release-notes-v2-103-0-newfeatures}
==========================================================

* Tap to Pay: Added a Device Selection screen that enables merchants to enroll a previously enrolled device without manually entering the serial number. This is now the default process when performing a device enrollment.
* Added the ability to customize the DefaultUI style elements using a `UiConfiguration` instance.
  {#ttp-aio-release-notes-v2-103-0-newfeatures_ul_i5q_gtd_1gc}

Improvements {#ttp-aio-release-notes-v2-103-0-improve}
======================================================

Tap to Pay: Re-enrolling a device can now be done without clearing the app data.

Fixed Issues {#ttp-aio-release-notes-v2-103-0-fixed-issues}
===========================================================

Applied general fixes to UI.

SDK Version 2.102.0 Release Notes {#ttp-aio-release-notes-v2-102-0-intro}
=========================================================================

These release notes are for the PAX All-in-One and Tap to Pay on Android SDKs, version 2.102.0 for Android. The release date is 06-27-2025.

New Features {#ttp-aio-release-notes-v2-102-0-newfeatures}
==========================================================

* Tap to Pay: The solution is now PCI-MPoC compliant, which requires the Tap to Pay Ready app to be installed on the Android devices. After upgrading to this SDK version, re-enroll devices.
* Tap to Pay: Added support for American Express.

Improvements {#ttp-aio-release-notes-v2-102-0-improve}
======================================================

* The `toolBarlogo` style element now appears on the Present Card screen.
* The customer is no longer prompted for the tip amount a second time when a failed transaction is retried. Whatever tip amount the customer chose during the original transaction is included in the transaction.
* Tap to Pay: Improved the error messages that can appear during device enrollment and transaction processing.

SDK Version 2.101.1 Release Notes {#ttp-aio-release-notes-v2-101-1-intro}
=========================================================================

These release notes are for the PAX All-in-One and Tap to Pay on Android SDKs, version 2.101.1 for Android. The release date is 05-23-2025.

New Features {#ttp-aio-release-notes-v2-101-1-newfeatures}
==========================================================

* Added support for landscape mode on large-screen devices.
* Added support for the PAX A3700.

Improvements {#ttp-aio-release-notes-v2-101-1-improve}
======================================================

* Improved the error message that can appear when a magnetic-stripe card is not read correctly by the device.
* Tap To Phone: Improved the error messages that can appear during enrollment of previously enrolled device.

Fixed Issues {#ttp-aio-release-notes-sdk-v2-101-1-fixed-issues}
===============================================================

* Fixed the issue that caused the `toolBarlogo` element not to work when using an XML file. This element controls the logo that appears on the device during transactions.
* Fixed the issue on the Signature screen that caused the transaction to fail when the Continue button was tapped multiple times.

SDK Version 2.100.0 Release Notes {#ttp-aio-release-notes-v2-100-0-intro}
=========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.100.0 for Android. The release date is 04-21-2025.

Improvements {#ttp-aio-release-notes-v2-100-0-improve}
======================================================

Updated the UI to use Google Material Design 3.

Fixed Issues {#ttp-aio-release-notes-sdk-v2-100-0-fixed-issues}
===============================================================

Tap To Phone: Fixed the issue that caused the device serial number to not be shown after a failed device enrollment.

SDK Version 2.99.0 Release Notes {#ttp-aio-release-notes-v2-99-0-intro}
=======================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.99.0 for Android. The release date is 03-25-2025.

New Features {#ttp-aio-release-notes-v2-99-0-new-features}
==========================================================

Tap To Phone: Added the ability to re-enroll a previously enrolled device by providing the serial number to the SDK.

Improvements {#ttp-aio-release-notes-v2-99-0-improve}
=====================================================

* Improved the error message that appears when trying to start an unsupported transaction type.
* Tap To Phone: Improved the error messages that can appear during enrollment and transactions.
* Tap To Phone: The device serial number is now returned in the `EnrollResultIntent` after performing a device enrollment.

SDK Version 2.98.0 Release Notes {#ttp-aio-release-notes-sdk-v2-98-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.98.0 for Android. The release date is 02-19-2025.

Updated Requirements {#ttp-aio-release-notes-sdk-v2-98-0-updated-rqmnts}
========================================================================

Tap to Phone: Added new ProGuard rule for Relay sensory branding. Include this rule in your *proguard-rules.pro* file going forward.

New Features {#ttp-aio-release-notes-sdk-v2-98-0-new-features}
==============================================================

Added Arabic as a supported language.

Improvements {#ttp-aio-release-notes-sdk-v2-98-0-improve}
=========================================================

* Tap to Phone: Improved the device enrollment experience by removing the requirement to provide an International Mobile Equipment Identity (IMEI) number. After upgrading to this SDK version, devices need to be re-enrolled.
* Tap to Phone: Improved experience when attempting to perform a transaction with an unsupported card.
* Tap to Phone: Improved the error messages that can appear during enrollment and transactions.
* Tap to Phone: Added a check to confirm that NFC is enabled when a transaction is started.

Fixed Issues {#ttp-aio-release-notes-sdk-v2-98-0-fixed-issues}
==============================================================

* Fixed the issue that caused the print receipt buttons to not appear after requesting a check transaction status.
* Fixed the issue that required some dependencies to be imported manually.

SDK Version 2.97.0 Release Notes {#ttp-aio-release-notes-sdk-v2-97-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.97.0 for Android. The release date is 01-29-2025.

Improvements {#ttp-aio-release-notes-sdk-v2-97-0-improve}
=========================================================

* Tap to Phone: Improved the error messages that can appear during enrollment.
* Tap to Phone: Improved experience when attempting to perform a transaction with an unsupported currency.
* MOTO transactions will no longer prompt for tip if tipping is configured.

SDK Version 2.96.0 Release Notes {#ttp-aio-release-notes-sdk-v2-96-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.96.0 for Android. The release date is 11-26-2024.

Fixed Issues {#ttp-aio-release-notes-sdk-v2-96-0-fixed-issues}
==============================================================

Fixed various issues that occasionally caused the SDK to crash.

SDK Version 2.95.0 Release Notes {#ttp-aio-release-notes-sdk-v2-95-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.95.0 for Android. The release date is 10-22-2024.

Improvements {#ttp-aio-release-notes-sdk-v2-95-0-improve}
=========================================================

Tap to Phone: Improved the error messages that can appear during enrollment and transactions.

Fixed Issues {#ttp-aio-release-notes-sdk-v2-95-0-fixed-issues}
==============================================================

* Fixed the issue that occasionally caused the "Low Battery" notification to be shown incorrectly.
* Fixed the issue that caused the value provided for `merchantDescriptor` to not be captured correctly.
  {#ttp-aio-release-notes-sdk-v2-95-0-fixed-issues_ul_uz4_z4c_fdc}

SDK Version 2.94.0 Release Notes {#ttp-aio-release-notes-sdk-v2-94-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.94.0 for Android. The release date is 09-11-2024.

Fixed Issues {#ttp-aio-release-notes-sdk-v2-94-0-fixed-issues}
==============================================================

* Fixed the issue that rarely caused a crash when performing a magstripe transaction.
* Fixed the issue that rarely caused a crash during the card selection process.

New Features {#ttp-aio-release-notes-sdk-v2-94-0-new-features}
==============================================================

* Added the ability to provide payment facilitator details when performing a transaction.
* Added the ability to provide tax details when performing a transaction.
* Added the ability to provide installment details for the Latin America \& Caribbean (LAC) region when performing a transaction.

SDK Version 2.93.0 Release Notes {#ttp-aio-release-notes-sdk-v2-93-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.93.0 for Android. The release date is 08-19-2024.

Improvements {#ttp-aio-release-notes-sdk-v2-93-0-improve}
=========================================================

Improved the error messages that can appear for connection-related issues.

Updated Requirements {#ttp-aio-release-notes-sdk-v2-93-0-updated-rqmnts}
========================================================================

Updated the Mastercard sonic branding library to version 1.5.0. Use this version of the branding library with the SDK going forward.

Fixed Issues {#ttp-aio-release-notes-sdk-v2-93-0-fixed-issues}
==============================================================

* Fixed the issue that caused a crash if `MposUi.create` was called twice.
* Fixed the issue that caused receipt data to be missing when using `transaction.getCustomerReceipt` or `transaction.getMerchantReceipt` functions for Tap to Phone transactions.
* Fixed the issue that caused some devices to not have the expected behavior when the signature capture configuration was set to `NONE`.
* Fixed the issue that caused `mposUi.latestTransaction` object to not be updated after requesting a check transaction status.

SDK Version 2.92.0 Release Notes {#ttp-aio-release-notes-sdk-v2-92-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.92.0 for Android. The release date is 07-05-2024.

Improvements {#ttp-aio-release-notes-sdk-v2-92-0-improve}
=========================================================

* Error message screens now have a timeout of 15 seconds.
* Improved the error message that appears when an offline transaction is attempted before the first online transaction is processed on the device.

SDK Version 2.91.0 Release Notes {#ttp-aio-release-notes-sdk-v2-91-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.91.0 for Android. The release date is 06-12-2024.

New Features {#ttp-aio-release-notes-sdk-v2-91-0-new-features}
==============================================================

In order to skip signature capture, the signature capture configuration can be now be set to `NONE`.

Improvements {#ttp-aio-release-notes-sdk-v2-91-0-improve}
=========================================================

Tap to Phone: Improved the error messages that can appear during device enrollment.

Fixed Issues {#ttp-aio-release-notes-sdk-v2-91-0-fixed-issues}
==============================================================

* Fixed the issue that caused the A920 MAX terminal not to be recognized correctly.
* Fixed the issue that caused the Retry button to appear on the Summary screen of approved transactions when the `RETRY_TRANSACTION` feature was configured as the default summary feature.

SDK Version 2.90.0 Release Notes {#ttp-aio-release-notes-sdk-v2-90-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.90.0 for Android. The release date is 05-16-2024.

New Features {#ttp-aio-release-notes-sdk-v2-90-0-new-features}
==============================================================

* Added the ability to process partial refunds and captures from the transaction summary screen.
* Added support for PAX IM30 and PAX A920 MAX devices.

Improvements {#ttp-aio-release-notes-sdk-v2-90-0-improve}
=========================================================

Updated the Present Card animation that appears when processing an offline transaction.

Updated Requirements {#ttp-aio-release-notes-sdk-v2-90-0-updated-rqmnts}
========================================================================

* Tap to Phone: Updated the minimum supported operating system to Android 12.
* Updated the minimum supported Kotlin version to 1.8.

Fixed Issues {#ttp-aio-release-notes-sdk-v2-90-0-fixed-issues}
==============================================================

Fixed the issue that rarely caused the terminal to become unresponsive after attempting to use an unsupported card.

General Information {#ttp-aio-release-notes-sdk-v2-90-0-gen-info}
=================================================================

* Removed deprecated `statementDescription` and `applicationFee` parameters.
* Removed deprecated NightMode configuration.

SDK Version 2.89.0 Release Notes {#ttp-aio-release-notes-sdk-v2-89-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.89.0 for Android. The release date is 04-18-2024.

Fixed Issues {#ttp-aio-release-notes-sdk-v2-89-0-fixed-issues}
==============================================================

Fixed the issue that caused the merchant receipt for MOTO transactions not to include the transaction status.

Improvements {#ttp-aio-release-notes-sdk-v2-89-0-improve}
=========================================================

Tap to Phone: Added translations for error messages in all supported languages.

SDK Version 2.88.0 Release Notes {#ttp-aio-release-notes-sdk-v2-88-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.88.0 for Android. The release date is 03-18-2024.

New Features {#ttp-aio-release-notes-sdk-v2-88-0-new-features}
==============================================================

* PAX All-in-One SDK now supports:
  * Offline transactions, also known as *deferred authorization* or *store and forward*
  * On-receipt tipping
    {#ttp-aio-release-notes-sdk-v2-88-0-new-features_ul_vr4_xfb_z1c}
* Added support for 67 additional currencies.
  {#ttp-aio-release-notes-sdk-v2-88-0-new-features_ul_wsj_grk_v1c}

Improvements {#ttp-aio-release-notes-sdk-v2-88-0-improve}
=========================================================

Added the necessary ProGuard rules to the Tap to Phone SDK. This improvement eliminates the need to maintain the rules in the app project.

SDK Version 2.87.0 Release Notes {#ttp-aio-release-notes-sdk-v2-87-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.87.0 for Android. The release date is 02-20-2024.

General Information {#ttp-aio-release-notes-sdk-v2-87-0-gen-info}
=================================================================

* NightMode was deprecated from `UiConfiguration` and will be removed in the next release.
* Changed the "Bugfixes" release note title to "Fixed Issues."

Updated Requirements {#ttp-aio-release-notes-sdk-v2-87-0-update-requirements}
=============================================================================

Updated the Relay sensory branding library to version 2.2. Use this version of the branding library with the SDK going forward.

Fixed Issues {#ttp-aio-release-notes-sdk-v2-87-0-fixed-issues}
==============================================================

* Fixed the issue that caused Default UI to crash if the app was running in the background during the card selection process.
* Fixed the issue that caused the incorrect formatting of the signature line on a printed receipt.

SDK Version 2.86.0 Release Notes {#ttp-aio-release-notes-sdk-v2-86-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.86.0. The release date is 01-16-2024.

Improvements {#ttp-aio-release-notes-sdk-v2-86-0-improve}
=========================================================

Improved error messages that appear during Tap to Phone device enrollment.

SDK Version 2.85.0 Release Notes {#ttp-aio-release-notes-sdk-v2-85-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.85.0. The release date is 12-19-2023.

Improvements {#ttp-aio-release-notes-sdk-v2-85-0-improve}
=========================================================

* Improved the UI experience when cancelling a Tap to Phone transaction from the PIN entry screen.
* Enabled the PAX device screen to power on automatically when a transaction is started when the screen is off.

Fixed Issues {#ttp-aio-release-notes-sdk-v2-85-0-fixed-issues}
==============================================================

* Fixed the issue related to integrators using WorkManager to schedule background work.
* Fixed the issue that occasionally caused the last screen of a canceled Tap to Phone transaction not to be dismissed automatically.
* Fixed the issue that caused MOTO transactions to crash if the language was set to German.

SDK Version 2.84.0 Release Notes {#ttp-aio-release-notes-sdk-v2-84-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.84.0. The release date is 11-23-2023.

Improvements {#ttp-aio-release-notes-sdk-v2-84-0-improve}
=========================================================

* Improved error handling at the start of a Tap to Phone transaction.
* Improved UI during initialization of a Tap to Phone transaction.
* Improved UX during cancellation of a Tap to Phone transaction.

SDK Version 2.83.0 Release Notes {#ttp-aio-release-notes-sdk-v2-83-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.83.0. The release date is 10-19-2023.

New Features {#ttp-aio-release-notes-sdk-v2-83-0-new-features}
==============================================================

Tap to Phone now supports these transaction types: pre-authorization, incremental authorization, and capture.

Improvements {#ttp-aio-release-notes-sdk-v2-83-0-improve}
=========================================================

* Improved the display of error messages that are more than 40 characters long.
* Added an indicator on the Summary screen that the customer signature should be captured on the printed receipt for Tap to Phone transactions.

Fixed Issues {#ttp-aio-release-notes-sdk-v2-83-0-fixed-issues}
==============================================================

* Fixed the issue that resulted in an inconsistent state when a new transaction was started while the Summary screen was displayed.
* Fixed the issue that occurred during a successful refund transaction in which the Information screen showed the original transaction amount instead of the refunded amount.
* Fixed the issue that caused transactions that used currencies with two-digit numeric codes to fail.

SDK Version 2.82.0 Release Notes {#ttp-aio-release-notes-sdk-v2-82-0-intro}
===========================================================================

These release notes are for the PAX All-in-One and Tap to Phone Android SDKs, version 2.82.0. The release date is 09-19-2023.

New Features {#ttp-aio-release-notes-sdk-v2-82-0-new-features}
==============================================================

Tap to Phone now supports the on-device tipping feature.

Fixed Issues {#ttp-aio-release-notes-sdk-v2-82-0-fixed-issues}
==============================================================

* Fixed the issue that caused Tap to Phone transactions to freeze when using the signature on-receipt feature.
* Fixed the issue that caused the SDK to crash when attempting to recover a transaction after the Inconclusive screen is shown.
* Fixed the issue that caused the SDK to crash when starting a transaction with a zero amount and custom tipping.
* Fixed the issue that caused the wrong value to be returned when calling the `isReadyForTransaction` method before the first transaction.

