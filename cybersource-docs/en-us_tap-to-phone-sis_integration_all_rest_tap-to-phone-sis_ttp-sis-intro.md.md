Introduction to Acceptance Devices \| Tap to Pay on Android Acceptance Devices App {#ttp-sis-intro}
===================================================================================================

The Tap to Pay on Android Acceptance Devices App enables partners to easily integrate their point-of-sale (POS) systems with supported Android devices in a semi-integrated manner using Local and Cloud modes. Leveraging the Acceptance Devices Android app and using API requests, your POS system can accept payments by communicating with the Android device over a local Wi-Fi network or the cloud.  
The solution can also be operated in Standalone mode. This mode does not require integration with a POS system and enables you to start transactions directly from the Android device.  
For more information about the modes available in the Acceptance Devices app, see:

* [Local Mode Payment Services](/docs/cybs/en-us/tap-to-phone-sis/integration/all/rest/tap-to-phone-sis/ttp-sis-pymnt-svcs-intro.md "")
* [Cloud Mode Payment Services](/docs/cybs/en-us/tap-to-phone-sis/integration/all/rest/tap-to-phone-sis/ttp-sis-pymnt-svcs-cloud-mode-intro.md "")
* [Standalone Mode Payment Services](/docs/cybs/en-us/tap-to-phone-sis/integration/all/rest/tap-to-phone-sis/ttp-sis-pymnt-svcs-standalone-mode-intro.md "")  
  For information about the current version of the Acceptance Devices Android app, see the [Release Notes for Tap to Pay on Android Acceptance Devices App](/docs/cybs/en-us/tap-to-phone-sis/integration/all/rest/tap-to-phone-sis/ttp-sis-release-notes-intro.md "").

Compatibility Requirements for Android Devices {#ttp-sis-intro-android-device-reqs}
===================================================================================

Your Android device must be compatible with the Tap to Pay on Android Acceptance Devices App to accept contactless payments.  
These are the requirements for a compatible Android device:

* Tap to Pay Ready app is installed. You can download the app from the [Google Play Store](https://play.google.com/store/apps/details?id=com.relay.kic.app.kernel "").
* Google Play Integrity API contains `DEVICE_INTEGRITY` verdict. For more information, see the [Android Developer documentation](https://developer.android.com/google/play/integrity/additional-tools#check-device "").
* Supports Google Mobile Services (GMS) and Google Play Store.
* Android 12 or later operating system (OS), with a security update version of May 2022 or later. Android OS versions that do not receive security updates are not supported.
* Has hardware-backed keystore.
* Contains near-field communication (NFC) enabled chip.
* Automatic time and date detection are enabled.
* Developer options are disabled.
* Device is not rooted. This setting prevents you from changing system-level files or settings.
  {#ttp-sis-intro-android-device-reqs_ul_pvy_4g2_hwb}

Supported Payment Devices {#ttp-sis-intro-supported-pymnt-devices}
==================================================================

The Tap to Pay on Android Acceptance Devices App supports validated payment devices that meet compatibility requirements. For more information, see [Compatibility Requirements for Android Devices](/docs/cybs/en-us/tap-to-phone-sis/integration/all/rest/tap-to-phone-sis/ttp-sis-intro/ttp-sis-intro-android-device-reqs.md "").  
The table lists supported payment devices. However, all models of supported devices are not shown. If your device is not listed, contact your implementation manager for help with determining whether the device is supported.

| Portable Devices          | Kiosk Devices     | Tablet Devices        |
|:--------------------------|:------------------|:----------------------|
| Android compatible phones | Elo Touch 22-inch | iMin Falcon 2         |
| Elo Touch M51             | oona 22           | MobiWire WM26 MobiTab |
| iMin Swift 2              | Sunmi FLEX 3      | oona 10               |
| MobiWire MobiGo2+ Pro     |                   | Orderman HT10         |
| MobiWire MP5 MobiPrint 5  |                   | Sunmi CPad            |
| MobiWire WM19 MobiTap     |                   | Sunmi D3 MINI         |
| Newland S90, S90 Pro      |                   | Sunmi V3 MIX          |
| Orderman 10               |                   |                       |
| Sunmi L3                  |                   |                       |
| Sunmi M3                  |                   |                       |
| Sunmi V3                  |                   |                       |
| Zebra EM45                |                   |                       |
[Compatible, Validated Payment Devices]

Transaction Workflow for the Tap to Pay on Android Acceptance Devices App {#ttp-sis-txn-workflow}
=================================================================================================

This diagram shows the transaction workflow for the Tap to Pay on Android Acceptance Devices App.

#### Figure: {#ttp-sis-txn-workflow_fig_dvm_x1r_jdc}

Tap to Pay on Android Acceptance Devices App Transaction Workflow  
![Tap to Pay on Android Acceptance Devices App transaction workflow showing the
sequence of events](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/tap-to-phone-sis/images/ttp-sis-workflow-diagram-600x400.svg/jcr:content/renditions/original)  
The Tap to Pay on Android Acceptance Devices App workflow typically includes this sequence of events:

1. The point-of-sale (POS) system, running on Windows, Android, or iOS, integrates to the Tap to Pay on Android Acceptance Devices App APIs.
2. The merchant's POS system sends an API request, using the local Wi-Fi network or the cloud, to the Acceptance Devices app that is running on the Android device.
3. The Acceptance Devices app user interface opens on the Android device and displays prompts that guide the customer through the payment flow.
4. The Acceptance Devices app sends an API response to the POS system with the transaction result and details, which completes the transaction.

