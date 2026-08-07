Introduction to Acceptance Devices \| Tap to Pay on Android Solution {#tap-to-phone-intro}
==========================================================================================

Using existing mobile technology, the Acceptance Devices \| Tap to Pay on Android Solution enables any compatible Android smartphone to operate as a secure payment acceptance device. By integrating the Tap to Pay on Android software development kit (SDK) into your Android point-of-sale (POS) application, you can efficiently manage the payment flow and deliver a seamless transaction experience for both merchants and customers.  
For information about the current version of the SDK, see the [Release Notes for Tap to Pay on Android Solution](/docs/cybs/en-us/tap-to-phone/integration/all/rest/tap-to-phone/ttp-release-notes-intro.md "").

Compatibility Requirements for Android Devices {#tap-to-phone-intro-android-device-reqs}
========================================================================================

To accept contactless payments, your Android device must be compatible with the Tap to Pay on Android Solution. These are the key requirements for a compatible Android device:
* Tap to Pay Ready app is installed. You can download the app from the [Google Play Store](https://play.google.com/store/apps/details?id=com.relay.kic.app.kernel "").
* Google Play Integrity API contains `DEVICE_INTEGRITY` verdict. For more information, see the [Android Developer documentation](https://developer.android.com/google/play/integrity/additional-tools#check-device "").
* Supports Google Mobile Services (GMS) and Google Play Store.
* Hardware-backed keystore.
* Near-field communication (NFC) enabled chip.
* Android 12 or later operating system (OS), with a security update version of May 2022 or later. Android OS versions that do not receive security updates are not supported.
* Automatic time and date detection are enabled.
* Developer options are disabled.
* Device is not rooted. This setting prevents you from changing system-level files or settings.
  {#tap-to-phone-intro-android-device-reqs_ul_pvy_4g2_hwb}

Transaction Workflow for Tap to Pay on Android Solution {#tap-to-phone-workflow}
================================================================================

This diagram shows the transaction workflow for the Tap to Pay on Android Solution.

#### Figure: {#tap-to-phone-workflow_fig_p3v_vqv_lfc}

Tap to Pay on Android Solution Transaction Workflow  
![Tap to Pay on Android Solution transaction workflow showing sequence of
events](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/tap-to-phone/images/ttp-sdk-sequence-diagram-600x450.svg/jcr:content/renditions/original)

1. The Android point-of-sale (POS) app integrates to the Tap to Pay on Android SDK.
2. The merchant's Android POS app sends a request to the Tap to Pay on Android SDK to process a payment.
3. The Tap to Pay on Android SDK user interface (UI) opens on the Android device screen and guides the customer through the payment flow.
4. The Tap to Pay on Android SDK sends a response with the transaction result and details to the Android POS app.
   {#tap-to-phone-workflow_ol_xhq_lnz_yxb}

Payment Devices Supported by Tap to Pay on Android Solution {#tap-to-phone-intro-supported-pymnt-devices}
=========================================================================================================

The Tap to Pay on Android Solution supports validated payment devices that meet compatibility requirements. For more information, see [Compatibility Requirements for Android Devices](/docs/cybs/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-intro/tap-to-phone-intro-android-device-reqs.md "").  
The table lists supported payment devices. However, all models of supported devices are not shown. If your device is not listed, contact your implementation manager for help with determining if the device is supported.

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
| Sunmi L3, M3, V3          |                   |                       |
| Zebra EM45                |                   |                       |
[Compatible, Validated Payment Devices]

PCI MPoC Standard Compliance {#ttp-comply-pci-mpoc-intro}
=========================================================

The Tap to Pay on Android Solution complies with the PCI Security Standards Council (PCI SSC) Mobile Payments on COTS (MPoC) standard. This standard is typically referred to as *PCI MPoC*. Compliance with this standard helps ensure secure and reliable payment processing across supported Android devices.  
The PCI-Certified MPoC Solution uses the Tap to Pay Ready app by Relay to meet PCI MPoC software, attestation, and monitoring requirements. The app uses a transparent overlay during payment processing to preserve the seamless UI experience. For app installation instructions, see [Install the Tap to Pay Ready App](/docs/cybs/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-get-started-intro/ttp-comply-pci-mpoc-install-app-intro/ttp-comply-pci-mpoc-install-app-task.md "").  
Using an app-to-app approach, payment processing is handled independently from your point-of-sale (POS) application. Transactions are started in your POS app, securely passed to the Tap to Pay Ready app for processing, and then returned to the original app. This approach meets compliance requirements and helps you achieve these benefits:

* Reduces PCI compliance complexity
* Lowers development and maintenance costs
* Accelerates time-to-market
* Enables seamless MPoC-related updates without affecting your app
  {#ttp-comply-pci-mpoc-intro_ul_odk_nyy_xgc}  
  For information about the PCI compliance status of the Tap to Pay on Android Solution, see the [PCI MPoC Solution Listing](https://listings.pcisecuritystandards.org/popups/mpoc_solution.php?reference=2025-01570.003 "").

Transaction Workflow for the PCI-Certified MPoC Solution {#ttp-comply-pci-mpoc-txn-workflow}
============================================================================================

This diagram shows the transaction workflow for the PCI-Certified MPoC Solution in the Tap to Pay on Android Solution.

#### Figure:

PCI-Certified MPoC Solution Workflow  
![PCI-certified MPoC solution transaction workflow showing the sequence of
events](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/tap-to-phone/images/ttp-android-mpoc-600x350.svg/jcr:content/renditions/original)  
The PCI-Certified MPoC Solution workflow typically includes this sequence of events:

1. The point-of-sale (POS) app sends a request to the Tap to Pay Ready app to initiate a secure switch to the other app. This activity is invisible to the customer, which ensures that the UI experience is seamless.
2. The PCI-Certified MPoC Solution uses the Tap to Pay Ready app to provide a transparent overlay to securely capture payment details.
3. The Tap to Pay Ready backend receives payment details from the Tap to Pay Ready app to complete transaction processing.

