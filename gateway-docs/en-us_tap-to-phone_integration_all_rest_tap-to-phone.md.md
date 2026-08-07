Acceptance Devices \| Tap to Pay on Android Solution Integration Guide {#tap-to-phone-about-guide}
==================================================================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
--------------------

This guide is written for application developers who want to integrate the Acceptance Devices \| Tap to Pay on Android software development kit (SDK) into their apps and to process contactless transactions on mobile devices.  
Integrating this SDK requires software development skills and the understanding of contactless payments on near-field communication (NFC)-enabled, commercial, off-the-shelf (COTS) mobile devices. You must write code that uses the SDK to integrate the Acceptance Devices \| Tap to Pay on Android payment service into your existing payment system.

Conventions
-----------

These statements appear in this document:

> IMPORTANT
> An *Important* statement contains information essential to successfully completing a task or learning a concept.
> WARNING
> A *Warning* contains information or instructions, which, if not heeded, can result in a security risk, irreversible loss of data, or significant cost in time or revenue or both.

Customer Support
----------------

For support information about any service, visit the Support Center:  
<http://support.example.com>

Recent Revisions to This Document {#tap-to-phone-doc-revisions}
===============================================================

26.07.01
--------

:
Updated instructions and code examples in [Sale with Lodging Details](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-payment-txn-intro/ttp-payment-txn-sale-lodging-details.md "").
:
Added support for new payment features:

    * [Sale with Airline Details](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-payment-txn-intro/ttp-payment-txn-sale-airline-details.md "")
    * [Sale with Auto Rental Details](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-payment-txn-intro/ttp-payment-txn-sale-auto-rental-details.md "")
    * [Sale with Billing and Shipping Details](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-payment-txn-intro/ttp-payment-txn-sale-bill-ship-details.md "")
    * [Sale with Merchant-Defined Data Details](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-payment-txn-intro/ttp-payment-txn-sale-merch-defined-data-details.md "")
    {#tap-to-phone-doc-revisions_ul_ub5_whb_5jc2}

:
Added new SDK release and updated release version in code examples. See [SDK Version 2.115.0 Release Notes](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/ttp-release-notes-intro/ttp-aio-rel-notes-v2-115-intro.md "").

26.06.01
--------

:
Updated all code examples in [Enabling Device Enrollment](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-get-started-intro/ttp-device-enroll-intro.md "").
:
Added new SDK release and updated release version in code examples. See [SDK Version 2.114.0 Release Notes](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/ttp-release-notes-intro/ttp-aio-rel-notes-v2-114-intro.md "").

26.05.01
--------

Added new SDK release and updated release version in code examples. See [SDK Version 2.113.0 Release Notes](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/ttp-release-notes-intro/ttp-aio-rel-notes-v2-113-intro.md "").

26.04.01
--------

:
Added support for Newland S90 and S90 Pro payment terminals in [Payment Devices Supported by Tap to Pay on Android Solution](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-intro/tap-to-phone-intro-supported-pymnt-devices.md "").
:
Added new SDK release and updated release version in code examples. See [SDK Version 2.112.0 Release Notes](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/ttp-release-notes-intro/ttp-aio-rel-notes-v2-112-intro.md "").

26.03.01
--------

:
Updated and moved code example into the new step 5 instruction in [Create an mposUI Instance](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-get-started-intro/tap-to-phone-mposui-instance-create-intro/tap-to-phone-mposui-instance-create-task.md "").
:
Removed `Configure the accessory as Tap to Phone` parameter from and updated code example in [Create a UiConfiguration Instance](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-get-started-intro/tap-to-phone-mposui-instance-create-intro/tap-to-phone-uiconfig-instance-create-intro/tap-to-phone-uiconfig-instance-configure-task.md "").
:
Added support for a new transaction type: [Sale with Lodging Details](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-payment-txn-intro/ttp-payment-txn-sale-lodging-details.md "").
:
Added new SDK release and updated release version in code examples. See [SDK Version 2.111.0 Release Notes](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/ttp-release-notes-intro/ttp-aio-release-notes-archive-intro/ttp-aio-rel-notes-v2-111-intro.md "").

Introduction to Acceptance Devices \| Tap to Pay on Android Solution {#tap-to-phone-intro}
==========================================================================================

Using existing mobile technology, the Acceptance Devices \| Tap to Pay on Android Solution enables any compatible Android smartphone to operate as a secure payment acceptance device. By integrating the Tap to Pay on Android software development kit (SDK) into your Android point-of-sale (POS) application, you can efficiently manage the payment flow and deliver a seamless transaction experience for both merchants and customers.  
For information about the current version of the SDK, see the [Release Notes for Tap to Pay on Android Solution](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/ttp-release-notes-intro.md "").

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
events](/content/dam/documentation/pgw/en-us/topics/payments-processing/card-processing/tap-to-phone/images/ttp-sdk-sequence-diagram-600x450.svg/jcr:content/renditions/original)

1. The Android point-of-sale (POS) app integrates to the Tap to Pay on Android SDK.
2. The merchant's Android POS app sends a request to the Tap to Pay on Android SDK to process a payment.
3. The Tap to Pay on Android SDK user interface (UI) opens on the Android device screen and guides the customer through the payment flow.
4. The Tap to Pay on Android SDK sends a response with the transaction result and details to the Android POS app.
   {#tap-to-phone-workflow_ol_xhq_lnz_yxb}

Payment Devices Supported by Tap to Pay on Android Solution {#tap-to-phone-intro-supported-pymnt-devices}
=========================================================================================================

The Tap to Pay on Android Solution supports validated payment devices that meet compatibility requirements. For more information, see [Compatibility Requirements for Android Devices](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-intro/tap-to-phone-intro-android-device-reqs.md "").  
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
The PCI-Certified MPoC Solution uses the Tap to Pay Ready app by Relay to meet PCI MPoC software, attestation, and monitoring requirements. The app uses a transparent overlay during payment processing to preserve the seamless UI experience. For app installation instructions, see [Install the Tap to Pay Ready App](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-get-started-intro/ttp-comply-pci-mpoc-install-app-intro/ttp-comply-pci-mpoc-install-app-task.md "").  
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
events](/content/dam/documentation/pgw/en-us/topics/payments-processing/card-processing/tap-to-phone/images/ttp-android-mpoc-600x350.svg/jcr:content/renditions/original)  
The PCI-Certified MPoC Solution workflow typically includes this sequence of events:

1. The point-of-sale (POS) app sends a request to the Tap to Pay Ready app to initiate a secure switch to the other app. This activity is invisible to the customer, which ensures that the UI experience is seamless.
2. The PCI-Certified MPoC Solution uses the Tap to Pay Ready app to provide a transparent overlay to securely capture payment details.
3. The Tap to Pay Ready backend receives payment details from the Tap to Pay Ready app to complete transaction processing.

Getting Started with the Tap to Pay on Android Solution {#tap-to-phone-get-started-intro}
=========================================================================================

Use this information to get started with integrating the Tap to Pay on Android Solution. When the integration is completed, your application will be ready to start processing payments. For more information, see [Tap to Pay on Android Payment Services](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-payment-txn-intro.md "").

Configuring the Tap to Pay on Android SDK {#tap-to-phone-configure-ttp-intro}
=============================================================================

Use this information to configure the Tap to Pay on Android SDK.

Configure the Project *settings.gradle* File {#tap-to-phone-configure-project-settings-gradle}
==============================================================================================

Follow this step to configure your project's *settings.gradle* file.

1. Add the repository to your project's *settings.gradle* file.

   ```
   dependencyResolutionManagement {
       repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
       repositories {
           mavenCentral()
           google()
           exclusiveContent {
               forRepository {
                   maven {
                       setUrl("https://repo.relay.com/mpos-releases/")
                   }
               }
               filter {
                   includeGroup("io.payworks")
               }
           }
       }
   }
   ```

Configure the Project *build.gradle* File {#tap-to-phone-configure-project-build-gradle}
========================================================================================

Follow this step to configure your project's *build.gradle* file.

1. Add the Kotlin Gradle plug-in, which is required to use this solution. Note that Kotlin version 2.1 or later and Android Gradle version 8.2 or later are required.

   ```
   plugins {
       id("com.android.application") version "8.2.0" apply false
       id("org.jetbrains.kotlin.android") version "2.1.0" apply false
   }
   ```

Configure the Module *build.gradle* File {#tap-to-phone-configure-module-build-gradle}
======================================================================================

Follow these steps to configure your module *build.gradle* file.

1. In the Android section, add these exclusion rules to your module's *build.gradle* file.

   ```
   android {
       ...
       packaging {
           resources {
               excludes.add("META-INF/*")
               excludes.add("LICENSE.txt")
               excludes.add("asm-license.txt")
           }
       }
   }
   ```
2. In order for the app to support Java 17 features, you must set the compatibility levels.

   ```
   android {
       ...
       compileOptions {
           sourceCompatibility = JavaVersion.VERSION_17
           targetCompatibility = JavaVersion.VERSION_17
       }
       kotlinOptions {
           jvmTarget = "17"
       }
   }
   ```
3. The Tap to Pay on Android Solution library publishes a release build type only. The debug build type is not available, so set the matchingFallbacks field value to `release`.

   ```
   android {
       ...
       buildTypes {
           ...
           debug {
               matchingFallbacks.apply {
                   clear()
                   add("release")
               }
           }
       }
   }
   ```
4. > IMPORTANT Stay current with the latest SDK. The SDK repository is continuously updated to make available the six latest versions. When a new version is released, the oldest is removed and can no longer be used for new application builds. Establish a regular process for updating to the newest available SDK version to avoid potential build failures and to ensure that your application runs with the latest features, performance enhancements, and security updates.
   > Add the required Default UI and Tap to Pay on Android libraries to the Dependencies section of your module's *build.gradle* file. The SDK version number shown in the dependencies section should match the current SDK release. For example: 2.115.0.

   ```
   dependencies {
       ...
       // This is the Default UI dependency
       implementation("io.payworks:paybutton-android:2.115.0")

       // This is the Tap to Pay dependency
       implementation("io.payworks:mpos.android.taptophone:2.115.0")   
   }
   ```

Update the *AndroidManifest.xml* File {#tap-to-phone-configure-android-manifest-xml}
====================================================================================

To support a large heap size and ensure the necessary permissions for the Default UI, update your `AndroidManifest.xml` file. Enabling a larger heap is essential for scenarios where terminal updates require the handling and transfer of large volumes of data. WARNING

> Do not enable automatic backup in your app's *AndroidManifest* file. The Tap to Pay on Android SDK uses the Android Keystore to install and store cryptographic keys in your app. Using automatic backup restores the default encryption preferences and causes a functionality error in the Tap to Pay on Android SDK.
> Follow these steps to update your *AndroidManifest.xml* file:

1. Set the `android:allowBackup` attribute to `false` and the `android:largeHeap` attribute to `true`.

   ```
   &lt;application
       ...
       android:allowBackup="false"
       android:largeHeap="true"
       &gt;
       ...
   &lt;/application&gt;
   ```
2. Enable the needed permissions for the Default UI.

   ```
   &lt;manifest ... &gt;
       ...
       &lt;!-- Needed for Default UI ! --&gt;
       &lt;uses-permission android:name="android.permission.INTERNET"/&gt;
       &lt;uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/&gt;
       &lt;uses-permission android:name="android.permission.READ_PHONE_STATE"/&gt;                   
       ...
   &lt;/manifest&gt;
   ```

Configure ProGuard Rules to Enable Obfuscation {#tap-to-phone-configure-proguard-rules}
=======================================================================================

Follow these steps to configure ProGuard rules that enable obfuscation.

1. To enable obfuscation for any of your build types, define the setting in the relevant *build.gradle* file for your app.

   ```
   buildTypes {
       release {
           isMinifyEnabled = true
           proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
       }
   }
   ```
2. If you are using ProGuard as an obfuscation tool in your app, add these rules to the *proguard-rules.pro* file.

   ```
   # OkHttp
   -keepattributes Signature
   -keepattributes *Annotation*
   -dontwarn com.squareup.okhttp.**
   -keep class com.squareup.okhttp.* { *; }
   -dontwarn okio.**

   # Acceptance Devices
   -keep class io.mpos.** { *; }
   -dontwarn io.mpos.**
   -keep class com.relay.vac.tc.** {*;}
   -keep class com.nimbusds.jose.** {*;}
   -keep class org.bouncycastle.** {*;}
   -keep class retrofit2.** { *; }
   -keep interface retrofit2.** { *; }
   -keep class com.relay.auth.** { *; }
   -dontwarn com.relay.auth.**
   -keep class androidx.** { *; }

   # Relay Sensory Branding
   -keep class com.relay.SensoryBrandingView

   # Mastercard Sonic Branding 
   -keep class com.mastercard.sonic.BuildConfig {*;}
   ```

Installing the Tap to Pay Ready App {#ttp-comply-pci-mpoc-install-app-intro}
============================================================================

The Tap to Pay Ready app must be installed on your Android device to support PCI-compliant payment processing. This app is a core component of the PCI-Certified MPoC Solution. For more information, see [PCI MPoC Standard Compliance](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-intro/ttp-comply-pci-mpoc-intro.md "") and [Transaction Workflow for the PCI-Certified MPoC Solution](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-intro/ttp-comply-pci-mpoc-txn-workflow.md "").

Install the Tap to Pay Ready App {#ttp-comply-pci-mpoc-install-app-task}
========================================================================

Use one of these options to install the Tap to Pay Ready App on your device:

* Click this [Google Play store link](https://play.google.com/store/apps/details?id=com.relay.kic.app.kernel "") to install the app directly on your Android device. No additional set up is required.
* Download the app when prompted during device enrollment. For more information, see [Enroll a Device](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-get-started-intro/ttp-device-enroll-intro/ttp-device-enroll-device.md "").
  {#ttp-comply-pci-mpoc-install-app-task_ul_efj_qrt_tfc}

Generating a Secret Key for an Existing Merchant ID {#ttp-mid-secret-key-generate-intro}
========================================================================================

You must enter a secret key and MID in the `mposUi` instance that you create.  
Use this information to generate a secret key for an existing merchant ID (MID) through the `Business Center` or by submitting a REST API request.  
For more information about the `mposUi` instance, see [Creating an mposUI Instance](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-get-started-intro/tap-to-phone-mposui-instance-create-intro.md "").

Generate a Secret Key for an Existing Merchant ID in the Business Center {#ttp-mid-secret-key-generate-ebc-task}
================================================================================================================

You can generate an secret key for an existing merchant ID (MID) in the `Business Center`. Enter these values in the `mposUi` instance that you create. For more information, see [Creating an mposUI Instance](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-get-started-intro/tap-to-phone-mposui-instance-create-intro.md "").  
Follow these steps to generate a secret key for an existing MID in the `Business Center`:

1. In the `Business Center`, go to the left navigation panel and choose Payment Configuration **\&gt;** Key Management. The Key Management page appears.

2. From the Merchant drop-down list, choose the merchant ID for which you want to generate a secret key.

3. Click Generate Key.

4. In the Recommended Key Types list, scroll down and choose Acceptance Devices Secret Key.

5. Click Generate Key. The Key Generation page appears.

6. Click Generate Key. Your MID and secret key appear on the page.

7. Click the Copy or Download icon to obtain the MID and secret key.

   #### ADDITIONAL INFORMATION

   > IMPORTANT
   > If you choose to copy the secret key information instead of downloading it, be sure to save it locally. After you leave the ` Business Center ` Key Generation page, you will not be able to retrieve the same secret key again. To obtain a new key, you must restart the key generation process.

Generate a Secret Key for an Existing Merchant ID Using a REST API Request {#ttp-mid-secret-key-generate-rest-api-task}
=======================================================================================================================

You can submit a REST API request to generate a secret key for an existing merchant ID (MID). Enter these values in the `mposUi` instance you create. For more information, see [Creating an mposUI Instance](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-get-started-intro/tap-to-phone-mposui-instance-create-intro.md "").  
You must authenticate each request that you send to a `Payment Gateway` API. In order to authenticate an API request, you can use a REST shared secret key or a REST certificate. For more information about authentication requirements, see [*Getting Started with REST Developer Guide*](https://developer.example.com/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md "").

Endpoints:
----------

**Test:** `POST ``https://apitest.example.com``/kms/v2/keys-sym-pos`  
**Production:** `POST ``https://api.example.com``/kms/v2/keys-sym-pos`

Required Fields for Generating a Secret Key for an Existing Merchant ID Using a REST API Request {#ttp-mid-secret-key-generate-api-reqfields}
=============================================================================================================================================

keyInformation.organizationId
:

REST Example: Generating a Secret Key for an Existing Merchant ID Using a REST API Request {#ttp-mid-secret-key-generate-api-ex-rest}
=====================================================================================================================================

Request

```
{
    "keyInformation":
    [
        {
            "organizationId": "transacting_MID"
        }
    ]
}
```

Response to a Successful Request

```
{
    "submitTimeUtc": "2023-08-07T13:07:17Z",
    "status": "ACCEPTED",
    "keyInformation": [
      {
           "organizationId": "transacting_MID",
           "externalOrganizationId": "MerchantId",
           "key": "SecretKey",
           "keyId": "af922a42-6d2c-41fd-92f7-09d908647de4",
           "status": "ACTIVE",
           "expirationDate": "2033-08-07T13:07:17Z"
      }
   ]
}
```

Creating an mposUI Instance {#tap-to-phone-mposui-instance-create-intro}
========================================================================

Use this information to create and configure an `mposUI` instance.

Create an `mposUI` Instance {#tap-to-phone-mposui-instance-create-task}
=======================================================================

Before starting this procedure, you must obtain secret key and merchant ID (MID) values to enter in to your `mposUI` instance. For more information, see [Generating a Secret Key for an Existing Merchant ID](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-get-started-intro/ttp-mid-secret-key-generate-intro.md ""). Create an `mposUI` instance to access the functionality of the Tap to Pay on Android SDK.  
Follow these steps to create an `mposUI` instance.

1. Create an `mposUI` instance using the `create` function.

2. Set the merchantId field value to the merchant ID that you obtained.

3. Set the merchantSecret field value to the secret key that you obtained.

4. Specify the environment by setting the providerMode field value to `TEST` or to `LIVE`.

   * Use the ProviderMode.TEST setting to test your integration without charging a real payment card. Use the merchant ID and secret key you obtained from the test environment.
   * Use the ProviderMode.LIVE setting to process live transactions. Use the merchant ID and secret key you obtained from the production environment.
5. Configure the accessory as Tap to Phone.

   ```
   val mposUi = MposUi.create( 
               providerMode = ProviderMode.LIVE, // ProviderMode.TEST 
               merchantId = "MerchantId", 
               merchantSecret = "SecretKey",
               terminalParameters = AccessoryParameters.Builder(AccessoryFamily.TAP_TO_PHONE).integrated().build()
           )
   ```

Configure an mposUI Instance {#tap-to-phone-uiconfig-instance-create-intro}
===========================================================================

To use the `mposUI` instance with the Tap to Pay on Android SDK, you must configure the `mposUI` instance by creating a `UiConfiguration` instance.

Create a `UiConfiguration` Instance {#tap-to-phone-uiconfig-instance-configure-task}
====================================================================================

Use a `UiConfiguration` instance to configure the UI functionality of the Tap to Pay on Android SDK.  
You can configure these parameters in the `UiConfiguration` instance that you create:

* Configure these Summary screen features:
  * Refund a transaction (`REFUND_TRANSACTION`).
  * Send a receipt by email (`SEND_RECEIPT_VIA_EMAIL`).
  * Capture a transaction (`CAPTURE_TRANSACTION`).
  * Retry a failed transaction (`RETRY_TRANSACTION`).
  * Increment a transaction (`INCREMENT_TRANSACTION`).
    {#tap-to-phone-uiconfig-instance-configure-task_ul_mkm_dm3_lyb}
* Configure the Summary screen so that it can be skipped (`SKIP_SUMMARY_SCREEN`) or so that it closes after 5 seconds (`CLOSE_AFTER_TIMEOUT`). The default setting is to show the Summary screen.
* Configure the signature capture so that it prints on the paper receipt (`ON_RECEIPT`) or is skipped (`NONE`). The default setting is on-screen signature capture.

{#tap-to-phone-uiconfig-instance-configure-task_ul_kpy_gl3_lyb}  
Follow this step to create the `UiConfiguration` instance in your app:

1. Create and configure the `UiConfiguration` instance.

   ```
   mposUi.configuration = UiConfiguration(
     summaryFeatures = setOf(
               SummaryFeature.REFUND_TRANSACTION,
               SummaryFeature.SEND_RECEIPT_VIA_EMAIL,
               SummaryFeature.CAPTURE_TRANSACTION,
               SummaryFeature.RETRY_TRANSACTION,
               SummaryFeature.INCREMENT_TRANSACTION
         )
   // Use this to skip the summary screen
   // resultDisplayBehavior = UiConfiguration.ResultDisplayBehavior.SKIP_SUMMARY_SCREEN,
   // Use this to set signature capture to be on paper receipt
   // signatureCapture = SignatureCapture.ON_RECEIPT,
   )
   ```

Create a `TapToPhoneConfiguration` Instance {#ttp-taptophone-config-instance}
=============================================================================

Create a `TapToPhoneConfiguration` instance to configure the device enrollment process of the Tap to Pay on Android SDK.  
You can configure these parameters in the `TapToPhoneConfiguration` instance that you create:

* Configure the enrollment process to prompt the merchant to enter the serial number of a previously enrolled device (`MANUAL_INPUT`). The default setting is to show a list of previously enrolled devices and prompt the merchant to select a device from the list (`DEVICE_LIST`).
* Configure the Serial Number Confirmation screen to be skipped (`SKIP`). The default setting is to show the screen (`SHOW_WITH_SERIAL_NUMBER`).

{#ttp-taptophone-config-instance_ul_jcd_rsn_rgc}  
Follow this step to create and configure the `TapToPhoneConfiguration` instance in your app:

1. Create and configure the instance.

   ```
   mposUi.tapToPhone.tapToPhoneConfiguration = TapToPhoneConfiguration(
   	serialNumberInputMethod = SerialNumberInputMethod.DEVICE_LIST,
   	confirmationScreenOption = ConfirmationScreenOption.SHOW_WITH_SERIAL_NUMBER
   	)
   ```

Customizing the Default User Interface {#ttp-customize-default-ui-intro}
========================================================================

Use this information to customize the Default UI so that it matches your brand's visual identity. The included screenshots highlight several style elements with labels for reference. Note that not all available style elements are shown. A detailed description of the style elements follows the screenshots.

#### Figure: {#ttp-customize-default-ui-intro_fig_w4y_1q4_5fc}

Tap to Pay on Android Default UI Style Elements  
![Example 1, Tap to Pay on Android Default UI style elements showing icons, labeled
buttons, colors, and text](/content/dam/documentation/pgw/en-us/topics/payments-processing/card-processing/tap-to-phone/images/ttp-customize-ui1.png/jcr:content/renditions/original)

#### Figure: {#ttp-customize-default-ui-intro_fig_gk1_fq4_5fc}

Tap to Pay on Android Default UI Style Elements  
![Example 2, Tap to Pay on Android Default UI style elements showing icons, labeled
buttons, colors, and text](/content/dam/documentation/pgw/en-us/topics/payments-processing/card-processing/tap-to-phone/images/ttp-customize-ui2.png/jcr:content/renditions/original)

#### Figure: {#ttp-customize-default-ui-intro_fig_iv4_jq4_5fc}

Tap to Pay on Android Default UI Style Elements  
![Example 3, Tap to Pay on Android Default UI style elements showing icons, labeled
buttons, colors, and text](/content/dam/documentation/pgw/en-us/topics/payments-processing/card-processing/tap-to-phone/images/ttp-customize-ui3.png/jcr:content/renditions/original) This list describes the style elements that you can customize in the Default UI:

`animationStrokeColor`
:
Stroke or outline color for animations.

`approvedStateColor`
:
Indicator color that appears for the approved transaction badge and animation.

`cardPresentAnimationStrokeColor`
:
Overrides the `animationStrokeColor` style element in the card reader drawing on present-card animations. By default, this element is the same color as the `animationStrokeColor` style element.

`colorControlActivated`
:
Color applied to switch controls in their active state.

`colorOnPrimary`
:
Primary color that appears for the filled button text and animation details.

`colorOnSurface`
:
Color for text that appears over the content view, transaction status badges text, and outlined button stroke.

`colorPrimary`
:
Primary color that appears for the filled buttons and animations.

`colorSurface`
:
Background color that appears for the content view.

`colorSurfaceOnSurface`
:
Background color for displayed lists such as transaction history.

`contactlessStateActiveColor`
:
Active indicator color that appears when the contactless interface is ready or when a payment card is tapped on the device.

`contactlessStateErrorColor`
:
Error indicator color that appears when a problem occurs when the device attempts to read a card on the contactless interface.

`contactlessStateInactiveColor`
:
Inactive indicator color that appears when the contactless interface is not active.

`declinedErrorStateColor`
:
Indicator color that appears for these elements:

    * Declined transaction badges and animation
    * Error transaction badges and animation
    * Error dialog boxes
    * Input field error messages
    {#ttp-customize-default-ui-intro_ul_pqr_1qj_bqb}

`notificationColor`
:
Alert notification color that appears with *Poor connection* and *Low battery* notifications. The default color is yellow.

`preAuthorizedStateColor`
:
Indicator color that appears for the pre-authorized transaction badge.

`smallComponentCornerSize`
:
Defines the corner radius of the buttons and transaction status badge. Set this element to `0dp` for square corners, `4dp` for slightly square corners (default), or `32dp` for round corners.

`toolBarLogo`
:
Logo that appears during transaction processing. The image must be rectangular, have the minimum dimensions of 144 x 36 pixels, and a 4:1 ratio.

Customize Style Elements Using a Theme {#ttp-customize-default-ui-style-theme}
==============================================================================

Follow these steps to customize the Default UI style elements.

1. Introduce a new theme to your application that includes the `Theme.PayButton2` theme as a parent theme.

   ```
   &lt;!-- Paybutton theme --&gt;
   &lt;style name="Theme.AppTheme.SampleTheme" parent="Theme.PayButton2"&gt;
       &lt;!-- Text color --&gt;
       &lt;item name="colorOnSurface"&gt;@color/black&lt;/item&gt;

       &lt;!-- Background color --&gt;
       &lt;item name="colorSurface"&gt;@color/white&lt;/item&gt;

       &lt;!-- Contactless indicators --&gt;
       &lt;item name="contactlessStateActiveColor"&gt;@color/dui_green&lt;/item&gt;
       &lt;item name="contactlessStateInactiveColor"&gt;@color/dui_light_gray2&lt;/item&gt;
       &lt;item name="contactlessStateErrorColor"&gt;@color/dui_red&lt;/item&gt;

       &lt;!-- Transaction status --&gt;
       &lt;item name="approvedStateColor"&gt;@color/dui_green&lt;/item&gt;
       &lt;item name="declinedErrorStateColor"&gt;@color/dui_red&lt;/item&gt; &lt;!-- Also used for error messages and dialogs --&gt;
       &lt;item name="preAuthorizedStateColor"&gt;@color/dui_dark_gray&lt;/item&gt;

       &lt;!-- Filled buttons and animations primary color --&gt;
       &lt;item name="colorPrimary"&gt;@color/dui_blue&lt;/item&gt;

       &lt;!-- Used over the primary color for text on filled buttons and details on animations --&gt;
       &lt;item name="colorOnPrimary"&gt;@color/dui_white&lt;/item&gt;

       &lt;!-- Corner radius for the buttons and transaction status badges --&gt;
       &lt;item name="smallComponentCornerSize"&gt;4dp&lt;/item&gt;

       &lt;!-- Company logo --&gt;
       &lt;item name="toolBarLogo"&gt;@drawable/logo_140x36&lt;/item&gt;

       &lt;!-- Stroke color for icons and animations --&gt;
       &lt;item name="animationStrokeColor"&gt;@color/dui_black&lt;/item&gt;
   &lt;/style&gt;
   ```
2. Call one of these methods to set the theme:

   ```
   mposUi.themeRes = R.style.Theme_AppTheme_SampleTheme
   ```

Customize Style Elements Using a `UiConfiguration` Instance {#ttp-customize-default-ui-style-uiconfig}
======================================================================================================

Use this customization feature to dynamically change some Default UI style elements while the app is in use. These style elements can be customized using a `UiConfiguration` instance:

* `toolbarLogo`
* `colorScheme` (and its sub-elements)
* `cornerRadius`

{#ttp-customize-default-ui-style-uiconfig_ul_axl_lzd_1gc} Follow this step to customize Default User Interface style elements using a `UiConfiguration` instance:

1. Create the `UiConfiguration` instance.

   ```
   mposUi.configuration = UiConfiguration(
     // other UiConfiguration parameters
     toolbarLogo = "....",
     colorScheme = UiConfiguration.ColorScheme(
       colorPrimary = 0xFF1A1F71,
       colorOnPrimary = 0xFFFFFFFF,
       colorSurface = 0xFFFFFFFF,
       colorOnSurface = 0xFF1C1B1B,
     ),
     cornerRadius = UiConfiguration.CornerRadius.ROUND
   )
   ```

Enable Dark Mode in the Default User Interface {#ttp-customize-default-ui-dark-mode}
====================================================================================

When the payment device is set to dark mode, the Default UI payment screens automatically adjust to display darker, high-contrast colors compared to the default light mode settings. This feature is particularly useful in low-light environments such as restaurants and bars.  
By default, the dark mode background color is dark gray (`#121212`). To customize the background to pure black (`#000000`), define a new `Theme.PayButton2` theme in the `values-night` resource folder.  
For more information about the dark mode setting on Android devices, see the [Android documentation](https://developer.android.com/reference/androidx/appcompat/app/AppCompatDelegate#setDefaultNightMode(int) "").  
Follow this step to change dark mode behavior:

1. Use this Android method to enforce light or dark mode across your entire application and the Default UI, regardless of the system setting on the device. This example enforces night mode.

   ```
   AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES)
   ```

Enabling Device Enrollment {#ttp-device-enroll-intro}
=====================================================

Use this information to enable device enrollment and view the device enrollment result in the Tap to Pay on Android SDK. The enrollment workflow guides you through the device enrollment activity.

Enroll a Device {#ttp-device-enroll-device}
===========================================

Before starting the device enrollment process, make sure the Tap to Pay Ready app is installed on the Android device. Download the app using this [Google Play Store link](https://play.google.com/store/apps/details?id=com.relay.kic.app.kernel ""). If the app is not installed before device enrollment, you will be prompted to install it during the enrollment process. To learn more about the Tap to Pay Ready app, see [PCI MPoC Standard Compliance](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-intro/ttp-comply-pci-mpoc-intro.md "").  
Use the information in this section to enroll a device using the `enrollDevice` activity. This activity presents a merchant-facing UI that enables users to enroll a new device or a previously enrolled device by selecting or entering the device's serial number. Follow this step to enroll a device.

1. Use the `enrollDevice` activity to enroll the device.

   ```
   val mposUi: MposUi = ...
   mposUi.tapToPhone.enrollDevice(activity, requestCode)
   ...
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
       super.onActivityResult(requestCode, resultCode, data)

       val isEnrollmentSuccessful =
           resultCode == EnrollResultIntent.ENROLLMENT_RESULT_CODE &&
           data?.getStringExtra(EnrollResultIntent.ENROLLMENT_RESULT_EXTRA) ==
               EnrollResultIntent.ENROLLMENT_RESULT_EXTRA_ENROLLED

       if (isEnrollmentSuccessful) {
           val serialNumber = data?.getStringExtra(
               EnrollResultIntent.ENROLLMENT_RESULT_EXTRA_SERIAL_NUMBER
           )
           onEnrollmentComplete(serialNumber)
       } else {
           onEnrollmentFailed()
       }
   }
   ```

   #### Step Result

The `enroll` activity returns the result Intent.

Enroll a Previously Enrolled Device {#ttp-device-enroll-prev-device}
====================================================================

Use this information to enroll a previously enrolled device by using the `reEnrollDevice` activity. This activity enables you to perform device re-enrollment through the SDK by supplying a stored serial number. This streamlined workflow eliminates the need for the merchant to manually select or enter the serial number during re-enrollment.

1. Use the `reEnrollDevice` activity to enroll the previously enrolled device.

   ```
   val mposUi: MposUi = ...
   mposUi.tapToPhone.reEnrollDevice(activity, serialNumber, requestCode)
   ...
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
       super.onActivityResult(requestCode, resultCode, data)

       val isEnrollmentSuccessful =
           resultCode == EnrollResultIntent.ENROLLMENT_RESULT_CODE &&
           data?.getStringExtra(EnrollResultIntent.ENROLLMENT_RESULT_EXTRA) ==
               EnrollResultIntent.ENROLLMENT_RESULT_EXTRA_ENROLLED

       if (isEnrollmentSuccessful) {
           val serialNumber = data?.getStringExtra(
               EnrollResultIntent.ENROLLMENT_RESULT_EXTRA_SERIAL_NUMBER
           )
           onEnrollmentComplete(serialNumber)
       } else {
           onEnrollmentFailed()
       }
   }
   ```

   #### Step Result

The `enroll` activity returns the result `Intent`.

View the Device Enrollment Result {#ttp-device-enroll-view-result}
==================================================================

After completing device enrollment, use the `enroll` activity or `isDeviceEnrolled` function to view the device enrollment result.  
The `enroll` activity returns the result `Intent` when the device enrollment process is successful. This example shows the information that is returned in the result `Intent`:

```
RESULT_CODE: EnrollResultIntent.ENROLLMENT_RESULT_CODE (3489523)
EXTRA: EnrollResultIntent.ENROLLMENT_RESULT_EXTRA (enrollmentResult)
EXTRA: EnrollResultIntent.ENROLLMENT_RESULT_EXTRA_ENROLLED (deviceEnrolled)
EXTRA: EnrollResultIntent.ENROLLMENT_RESULT_EXTRA_SERIAL_NUMBER (serialNumber)
```

{#ttp-device-enroll-view-result_codeblock_z2v_5xg_ndc}  
The `isDeviceEnrolled` function returns a `true` value when the device is enrolled or a `false` value when not. This example shows how to use the function:

```
val isEnrolled = mposUi.tapToPhone.isDeviceEnrolled()
```

Tap to Pay on Android Payment Services {#tap-to-phone-payment-txn-intro}
========================================================================

Use this information to process Tap to Pay on Android Solution payment services.

Sale {#tap-to-phone-payment-txn-sale}
=====================================

Use this information to process a sale. This transaction combines an authorization and a capture into a single transaction.  
Follow these steps to process a sale.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` value from the `mposUI` object, and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is completed and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                   val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                   Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                   Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
4. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUI` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Refund {#tap-to-phone-payment-txn-refund}
=========================================

Use this information to process a refund by referencing the original transaction. You can issue refunds for either the full amount or a partial amount of the original transaction.  
Stand-alone credits are also supported and can be processed independently of a previous transaction. For more information, see [Stand-Alone Credit](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-payment-txn-intro/tap-to-phone-payment-txn-standalone-credit.md "").  
Follow these steps to process a refund.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` value from the `mposUI` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder() 
               .refund(“transactionIdentifier”) 
               //Specify amount and currency for partial refunds 
               //.amountAndCurrency(BigDecimal(1.00), Currency.EUR) 
               .build() 

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters) 
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is completed and the Summary screen is dismissed, `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) { 
       super.onActivityResult(requestCode, resultCode, data) 
     
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) { 
           when (resultCode) { 
               // Result code from a successful transaction 
               MposUi.RESULT_CODE_APPROVED -&gt; { 
                   val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRAN
   SACTION_IDENTIFIER) 
                   Toast.makeText(findViewById(android.R.id.content),"Transaction approved!
   \nIdentifier: $transactionIdentifier",  
   Toast.LENGTH_LONG).show() 
               } 
               // Result code from a declined, aborted or failed transaction 
               MposUi.RESULT_CODE_FAILED -&gt; { 
                Toast.makeText(findViewById(android.R.id.content), "Transaction was decline
   d, aborted, or failed",  
   Toast.LENGTH_LONG).show() 
               } 
           } 
       } 
   }
   ```
4. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUI` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Stand-Alone Credit {#tap-to-phone-payment-txn-standalone-credit}
================================================================

Use this information to process a stand-alone credit. This transaction enables you to issue a credit without referencing a previous transaction. The customer must present their payment card.

> WARNING
> When processing a stand-alone credit, there is no limit on the credit amount because the transaction does not reference the original purchase. To help manage risk, it is recommended to use a refund transaction whenever possible. For more information, see [Refund](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-payment-txn-intro/tap-to-phone-payment-txn-refund.md "").  
> Follow these steps to process a stand-alone credit.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` value from the `mposUI` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder() 
               .refund(BigDecimal("1.00"), Currency.EUR)     
               .customIdentifier("yourReferenceForTheTransaction") 
               .build() 

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters) 
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is completed and the Summary screen is dismissed, `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
              // Result code from a successful transaction
              MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", 
   Toast.LENGTH_LONG).show()
              }
              // Result code from a declined, aborted or failed transaction
              MposUi.RESULT_CODE_FAILED -&gt; {
              Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", 
   Toast.LENGTH_LONG).show()
              }
           }
       }
   }
   ```
4. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUI` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Check Transaction Status {#tap-to-phone-payment-txn-check-txn-status}
=====================================================================

Use this information to request a check transaction status. This transaction enables you to retrieve response data for a transaction that was lost or timed out. You must have the `transactionIdentifier` value for the transaction that you want to check. When the check transaction status request is complete, the transaction details show on the Summary screen.  
Follow these steps to request a check transaction status.

1. Obtain the `transactionIdentifier` value in the `onActivityResult` method of the original transaction.

2. Retrieve the transaction `summaryIntent` value from the `mposUI` object.

3. Use the `startActivity` method to initiate the Summary screen.

   ```
   val summaryIntent = mposUi.createTransactionSummaryIntent(transactionIdentifier = "transactionIdentifier")
   startActivityForResult(summaryIntent, MposUi.REQUEST_CODE_SHOW_SUMMARY)
   ```
4. After the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)
       // Result code from closing the summary screen
       if (resultCode == MposUi.RESULT_CODE_SUMMARY_CLOSED) {
           // Accessing status from the transaction that was just queried
           val transactionStatus = mposUi.latestTransaction?.status
           Toast.makeText(activity, "Summary closed. Transaction status: $transactionStatus", Toast.LENGTH_SHORT).show()  
       }
   }
   ```
5. You can get the full transaction object by retrieving the `latestTransaction` property from the mposUi object.  
    

   ```
   val transactionObject = mposUi.latestTransaction
   ```

 

Pre-Authorization {#tap-to-phone-payment-txn-pre-auth-task}
===========================================================

Use this information to process a pre-authorization for an initial amount. A pre-authorization transaction places a temporary hold on the customer's payment card. The transaction amount can be captured at a later time.  
Most authorizations expire within 5 to 7 days, as determined by the issuing bank. When an authorization expires, your bank, the issuing bank, or payment processor might require you to resubmit the authorization request and include a capture request in the same message. For more information, see[Capture](/docs/gateway/en-us/tap-to-phone/integration/all/rest/tap-to-phone/tap-to-phone-payment-txn-intro/tap-to-phone-payment-txn-capture-task.md "").  
To help ensure successful transaction processing, monitor authorization timelines and use combined authorization and capture requests when necessary.  
Follow these steps to process a pre-authorization.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` value from the `mposUI` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .autoCapture(false)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is completed and the Summary screen is dismissed, `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   Override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
4. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUI` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Incremental Authorization {#tap-to-phone-payment-txn-incremental-auth-task}
===========================================================================

Use this information to process an incremental authorization. An incremental authorization is used after an approved pre-authorization to increase the authorized amount before capture.  
Follow these steps to process an incremental authorization.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` value from the `mposUI` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder() 
               .incrementalAuthorization("transactionIdentifier") 
               .amountAndCurrency(BigDecimal("1.00"), Currency.EUR) 
               .build() 

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters) 
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is completed and the Summary screen is dismissed, `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   Override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) { 
       super.onActivityResult(requestCode, resultCode, data) 
     
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) { 
           when (resultCode) { 
               // Result code from a successful transaction 
               MposUi.RESULT_CODE_APPROVED -&gt; { 
                   val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRAN
   SACTION_IDENTIFIER) 
                   Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier",  
   Toast.LENGTH_LONG).show() 
               } 
               // Result code from a declined, aborted or failed transaction 
               MposUi.RESULT_CODE_FAILED -&gt; { 
           Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed",  
   Toast.LENGTH_LONG).show() 
               } 
           } 
       } 
   }
   ```
4. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUI` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Capture {#tap-to-phone-payment-txn-capture-task}
================================================

Use this information to capture a pre-authorized transaction. The capture request references the approved pre-authorization request.  
Follow these steps to process a capture.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Retrieve the `transactionIntent` value from the `mposUI` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
              .capture("transactionIdentifier") 
           // Specify amount and currency for partial captures
           // .amountAndCurrency(BigDecimal("1.00"), Currency.EUR)
              .build() 

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters) 
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
3. After the transaction is completed and the Summary screen is dismissed, `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   Override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) { 
       super.onActivityResult(requestCode, resultCode, data) 
     
       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) { 
           when (resultCode) { 
               // Result code from a successful transaction 
               MposUi.RESULT_CODE_APPROVED -&gt; { 
           val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRAN
   SACTION_IDENTIFIER) 
           Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier",  
   Toast.LENGTH_LONG).show() 
               } 
               // Result code from a declined, aborted or failed transaction 
               MposUi.RESULT_CODE_FAILED -&gt; {     
           Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed",  
   Toast.LENGTH_LONG).show() 
               } 
           } 
       } 
   }
   ```
4. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUI` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Airline Details {#ttp-payment-txn-sale-airline-details}
=================================================================

Use this information to process a sale with airline details. This transaction includes required airline and related service details in the payment request.  
Follow these steps to process a sale with airline details.

1. Create an `AdditionalDetails` object and set one or more airline (`airlineDetails`) fields and related service (`ancillaryDetails`) fields.

   ```
   val airlineDetails = AdditionalDetailsBuilder()
           .airlineDetails(
               AirlineDetailsBuilder()
                   .agentCode("AGT12345")
                   .agentName("Relay Travel")
                   .arrivalDate(SimpleDateFormat("MMddyyyy", Locale.US).parse("01202024"))
                   .carrierName("Relay Airways")
                   .clearingCount(1)
                   .clearingSequence("1")
                   .creditReasonIndicator(CreditReasonIndicator.OTHER)
                   .customerCode("CORP12345")
                   .documentType(DocumentType.AIRLINE)
                   .electronicTicket(true)
                   .exchangeTicketAmount(BigDecimal("0.00"))
                   .exchangeTicketFee(BigDecimal("0.00"))
                   .firstName("John")
                   .lastName("Doe")
                   .numberOfPassengers("1")
                   .passengerName("John Doe")
                   .planNumber("01")
                   .purchaseType(PurchaseType.TICKET)
                   .reservationSystem("00001")
                   .restrictedTicketIndicator(RestrictedTicketIndicator.NONREFUNDABLE)
                   .ticketIssueDate(SimpleDateFormat("yyyyMMdd", Locale.US).parse("20240115"))
                   .ticketIssuerAddress("1 Market St")
                   .ticketIssuerCity("San Francisco")
                   .ticketIssuerCode("UA")
                   .ticketNumber("0141234567890")
                   .ticketRestrictionText("00000")
                   .ticketUpdateIndicator(TicketUpdateIndicator.NEW)
                   .totalClearingAmount("450.00")
                   .totalFee(BigDecimal("25.00"))
                   .addLegDetails(
                       listOf(
                           LegDetailsBuilder()
                               .arrivalTime("1230")
                               .arrivalTimeSegment(TimeSegment.PM)
                               .carrierCode("UA")
                               .legClass("Y")
                               .conjunctionTicket("0141234567891")
                               .couponNumber("1")
                               .departureDate(SimpleDateFormat("yyyyMMdd", Locale.US).parse("20240115"))
                               .departureTime("0930")
                               .departureTimeSegment(TimeSegment.AM)
                               .destination("JFK")
                               .endorsementsRestrictions("NONREF")
                               .exchangeTicket("0141234567892")
                               .fare(BigDecimal("450.00"))
                               .fareBasis("Y26")
                               .fee(BigDecimal("25.00"))
                               .flightNumber("1234")
                               .originatingAirportCode("SFO")
                               .stopoverCode(StopoverCode.NO_STOPOVER)
                               .tax(BigDecimal("38.00"))
                       )
                   )
                   .build()
           )
           .ancillaryDetails(
               AncillaryDetailsBuilder()
                   .connectedTicketNumber("0149876543210")
                   .creditReasonIndicator(CreditReasonIndicator.OTHER)
                   .feeDescription("Checked baggage")
                   .passengerName("Jane Doe")
                   .ticketNumber("0141234567890")
                   .addServiceDetails(
                       listOf(
                           ServiceDetailsBuilder()
                               .categoryCode("BAGO")
                               .subcategoryCode("CHKD")
                               .feeAmount(BigDecimal("35.00"))
                               .feeCode("0DB")
                       )
                   )
                   .build()
           )
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)
               .customIdentifier("yourReferenceForTheTransaction")
               .additionalDetails(airlineDetails)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?)
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. Get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Auto Rental Details {#ttp-payment-txn-sale-auto-rental-details}
=========================================================================

Use this information to process a sale with auto rental details. This transaction includes required auto rental details in the payment request.  
Follow these steps to process a sale with auto rental details.

1. Create an `AdditionalDetails` object and set one or more of the auto rental fields.

   ```
   val autoRentalDetails = AdditionalDetailsBuilder()
           .autoRentalDetails(
               // Set value of the builder to the number of rental days
               AutoRentalDetailsBuilder("5")
                   .pickUpState("CA")
                   .pickUpTime(SimpleDateFormat("HHmmss", Locale.US).parse("093000"))
                   .programCode("01")
                   .ratePerMile(BigDecimal("0.25"))
                   .regularMileageCost(BigDecimal("50.00"))
                   .rentalAddress("1 Market St")
                   .rentalLocationID("LOC001")
                   .renterName("Bob Smith")
                   .returnCity("Los Angeles")
                   .returnCountry("USA")
                   .returnDate(SimpleDateFormat("MMddyyyy", Locale.US).parse("01202024"))
                   .returnLocation("LAX Terminal 1")
                   .returnLocationID("LOC002")
                   .returnState("CA")
                   .specialProgramCode(SpecialProgramCode.NONE)
                   .taxAmount(BigDecimal("18.50"))
                   .taxIndicator(true)
                   .taxRate(BigDecimal("0.08"))
                   .taxStatusIndicator("Y")
                   .taxSummary("18.50")
                   .taxType("VAT")
                   .timePeriod(TimePeriod.DAILY)
                   .towingCharge(BigDecimal("0.00"))
                   .vehicleIdentificationNumber("1FTSW21P34EB12345")
                   .vehicleInsuranceIndicator(true)
                   .vehicleMake("Ford")
                   .vehicleModel("Focus")
                   .weeklyRentalRate(BigDecimal("280.00"))
                   .promotion(
                       PromotionDetailsBuilder()
                           .code("PROMO2024")
                           .additionalCode("WKND10")
                   )
                   .build()
           )
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)
               .customIdentifier("yourReferenceForTheTransaction")
               .additionalDetails(autoRentalDetails)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?)
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. Get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Billing and Shipping Details {#ttp-payment-txn-sale-bill-ship-details}
================================================================================

Use this information to process a sale with billing and shipping details. This transaction includes required billing and shipping details in the payment request.  
Follow these steps to process a sale with billing and shipping details.

1. Create an `AdditionalDetails` object and set one or more of the billing and shipping fields.

   ```
   val billingAndShippingDetails = AdditionalDetailsBuilder()
           .billingDetails(
               BillingDetailsBuilder()
                   .firstName("Alice")
                   .middleName("M")
                   .lastName("Smith")
                   .title("Ms.")
                   .company("Relay Inc.")
                   .companyTaxID("123456789")
                   .street1("123 Main St")
                   .city("San Francisco")
                   .state("CA")
                   .postalCode("94105")
                   .country("US")
                   .email("alice@example.com")
                   .phoneNumber("14155550123")
                   .customerID("CUST12345")
                   .personalID("PID1234567890")
                   .ipAddress("192.0.2.1")
                   .hostname("host.example.com")
                   .comments("VIP customer")
                   .build()
           )
           .shippingDetails(
               ShippingDetailsBuilder()
                   .firstName("Bob")
                   .lastName("Jones")
                   .company("Relay Inc.")
                   .street1("500 Market St")
                   .city("New York")
                   .state("NY")
                   .postalCode("10001")
                   .country("US")
                   .phoneNumber("12125550188")
                   .build()
           )
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)
               .customIdentifier("yourReferenceForTheTransaction")
               .additionalDetails(billingAndShippingDetails)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?)
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. Get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Lodging Details {#ttp-payment-txn-sale-lodging-details}
=================================================================

Use this information to process a sale with lodging details. This transaction includes the required lodging details in the payment request.  
Follow these steps to process a sale with lodging details.

1. Create a `AdditionalDetails` object and set one or more lodging fields.

   ```
   val lodgingDetails = AdditionalDetailsBuilder()
           .lodgingDetails(
               // Set value of the builder to the duration of stay
               LodgingDetailsBuilder(3)
                   .checkInDate("030125")
                   .checkOutDate("030425")
                   .guestSmokingPreference("N")
                   .numberOfGuests(2)
                   .numberOfRoomsBooked(1)
                   .guestName("John Doe")
                   .roomLocation("Ocean View")
                   .roomTaxElements("VAT")
                   .roomBedType("KING")
                   .roomRateType("CORPORATE")
                   .specialProgramCode("1")
                   .dailyRoomRate1(BigDecimal("150.00"))
                   .dailyRoomRate2(BigDecimal("160.00"))
                   .dailyRoomRate3(BigDecimal("170.00"))
                   .roomNights1(1)
                   .roomNights2(1)
                   .roomNights3(1)
                   .corporateClientCode("CORP123456")
                   .promotionalCode("PROMO2025")
                   .additionalCoupon("DISCOUNT10")
                   .travelAgencyCode("TA789")
                   .travelAgencyName("Premium Travel Agency")
                   .customerServicePhoneNumber("1-800-555-0199")
                   .tax(BigDecimal("45.00"))
                   .prepaidCost(BigDecimal("200.00"))
                   .foodAndBeverageCost(BigDecimal("125.00"))
                   .roomTax(BigDecimal("30.00"))
                   .adjustmentAmount(BigDecimal("15.00"))
                   .phoneCost(BigDecimal("8.00"))
                   .restaurantCost(BigDecimal("95.00"))
                   .roomServiceCost(BigDecimal("40.00"))
                   .miniBarCost(BigDecimal("25.00"))
                   .laundryCost(BigDecimal("18.00"))
                   .miscellaneousCost(BigDecimal("12.00"))
                   .giftShopCost(BigDecimal("35.00"))
                   .movieCost(BigDecimal("10.00"))
                   .healthClubCost(BigDecimal("20.00"))
                   .valetParkingCost(BigDecimal("30.00"))
                   .cashDisbursementCost(BigDecimal("5.00"))
                   .nonRoomCost(BigDecimal("40.00"))
                   .businessCenterCost(BigDecimal("15.00"))
                   .loungeBarCost(BigDecimal("55.00"))
                   .transportationCost(BigDecimal("75.00"))
                   .gratuityCost(BigDecimal("45.00"))
                   .conferenceRoomCost(BigDecimal("120.00"))
                   .audioVisualCost(BigDecimal("65.00"))
                   .banquetCost(BigDecimal("180.00"))
                   .internetAccessCost(BigDecimal("12.00"))
                   .earlyCheckOutCost(BigDecimal("20.00"))
                   .nonRoomTax(BigDecimal("25.00"))
                   .build()
           )
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)
               .customIdentifier("yourReferenceForTheTransaction")
               .additionalDetails(lodgingDetails)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?)
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Installment Details {#ttp-payment-txn-sale-installment-details-task}
==============================================================================

Use this information to process a sale with installment details. This transaction includes the required installment payment details in the payment request.
IMPORTANT This transaction is available only in the Latin American and Caribbean (LAC) region.  
Follow these steps to process a sale with installment details.

1. Create an `InstallmentDetails` object and set one ore more of the installment fields.

   ```
   // Set value of the builder to the number of installments
   val installmentDetails = InstallmentDetailsBuilder(5)
           // Set to PlanType.ISSUER_FUNDED for issuer funded plans
           .planType(PlanType.MERCHANT_FUNDED)
           .includesInterest(true)
           .governmentPlan(true)
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .installmentDetails(installmentDetails)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Merchant-Defined Data Details {#ttp-payment-txn-sale-merch-defined-data-details}
==========================================================================================

Use this information to process a sale with merchant-defined data details. This transaction includes required merchant-defined data details in the payment request.  
Follow these steps to process a sale with merchant-defined data details.

1. Create an `AdditionalDetails` object and set one or more merchant defined data fields.

   ```
   val mddDetails = AdditionalDetailsBuilder()
           .mddDetails(
               MddDetailsBuilder()
                   .field1("value1")
                   .field2("value2")
                   .field3("value3")
                   .field4("value4")
                   .field5("value5")
                   .field6("value6")
                   .field7("value7")
                   .field8("value8")
                   .field9("value9")
                   .field10("value10")
                   .field11("value11")
                   .field12("value12")
                   .field13("value13")
                   .field14("value14")
                   .field15("value15")
                   .field16("value16")
                   .field17("value17")
                   .field18("value18")
                   .field19("value19")
                   .field20("value20")
                   .build()
           )
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` variable from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)
               .customIdentifier("yourReferenceForTheTransaction")
               .additionalDetails(mddDetails)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?)
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. Get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with On-Reader Tipping {#tap-to-phone-payment-txn-sale-on-reader-tip-task}
===============================================================================

Use this information to process a sale with on-reader tipping. At the start of each transaction, the terminal prompts the customer to add a tip by showing suggested tip amounts. The customer chooses or enters a tip amount on the terminal before presenting their payment card.  
Follow these steps to process a sale with on-reader tipping.

1. Create a `TransactionParameters` object and provide the required information for the payment.

2. Create a `TippingProcessStepParameters` object to configure the tipping function. The options are percentage choice, tip amount, or total amount.

3. Create a `TransactionProcessParameters` object to add the tipping step.

4. Retrieve the `transactionIntent` value from the `mposUI` object, and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)
               .customIdentifier("yourReferenceForTheTransaction")
               .build()

   //  Use to display three tipping percentage choices
   val tipStep = TippingProcessStepParameters.Builder()
               .askForPercentageChoice()
           //  Optional to configure tipping percentages | Default values = 10, 15, 20
           //  .percentages(BigDecimal("10"), BigDecimal("20"), BigDecimal("30"))
           //  Optional to show confirmation screen
           //  .showTotalAmountConfirmationScreen(true)
               .build()

   //  Use to ask for tip amount
   //  val tipStep = TippingProcessStepParameters.Builder()
           //  .askForTipAmount()
           //  Optional to show confirmation screen
           //  .showTotalAmountConfirmationScreen(true)
           //  .build()

   //  Use to ask for total transaction amount including tip
           //  val tipStep = TippingProcessStepParameters.Builder()
           //  .askForTotalAmount()
           //  Optional to show confirmation screen
           //  .showTotalAmountConfirmationScreen(true)
           //  .build()

   val processParameters = TransactionProcessParameters.Builder()
       .addStep(tipStep)
       .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters, processParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
5. After the transaction is completed and the Summary screen is dismissed, `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   Override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), “Transaction was declined, aborted, or failed”, Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
6. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUI` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Payment Facilitator Details {#ttp-payment-txn-sale-payment-facilitator-task}
======================================================================================

Use this information to process a sale with payment facilitator details. This transaction includes the required payment facilitator details in the payment request.  
Follow these steps to process a sale with payment facilitator details.

1. Create a `MerchantDetails` object and set one ore more of the payment facilitator fields.

   ```
   val merchantDetails = MerchantDetailsBuilder()
           .salesOrganizationId("12345")
           .subMerchantId("SM67890")
           .merchantDescriptor("ExampleMerchant")
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .merchantDetails(merchantDetails)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Sale with Tax Details {#ttp-payment-txn-sale-tax-details-task}
==============================================================

Use this information to process a sale with tax details. This transaction includes required tax details in the payment request.  
Follow these steps to process a sale with tax details.

1. Create a `TaxDetails` object and set one ore more of the tax fields.

   ```
   val taxDetails = TaxDetailsBuilder()
           .merchantTaxId("TaxID1234")
           .salesSlipNumber(12345678)
           .includedTaxAmount(BigDecimal("5.00"))
           .includedLocalTaxAmount(BigDecimal("1.00"))
           .includedNationalTaxAmount(BigDecimal("2.00"))
           .build()
   ```
2. Create a `TransactionParameters` object and provide the required information for the payment.

3. Retrieve the `transactionIntent` from the `mposUi` object and use the `startActivity` method to initiate the transaction flow.

   ```
   val transactionParameters = TransactionParameters.Builder()
               .charge(BigDecimal("1.00"), Currency.EUR)    
               .customIdentifier("yourReferenceForTheTransaction")
               .taxDetails(taxDetails)
               .build()

   val transactionIntent = mposUi.createTransactionIntent(transactionParameters)
   startActivityForResult(transactionIntent, MposUi.REQUEST_CODE_PAYMENT)
   ```
4. After the transaction is complete and the Summary screen is dismissed, the `onActivityResult` method is triggered. This action returns information about the last transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) 
   {
       super.onActivityResult(requestCode, resultCode, data)

       if (requestCode == MposUi.REQUEST_CODE_PAYMENT) {
           when (resultCode) {
               // Result code from a successful transaction
               MposUi.RESULT_CODE_APPROVED -&gt; {
                  val transactionIdentifier = data?.getStringExtra(MposUi.RESULT_EXTRA_TRANSACTION_IDENTIFIER)
                  Toast.makeText(findViewById(android.R.id.content),"Transaction approved!\nIdentifier: $transactionIdentifier", Toast.LENGTH_LONG).show()
               }
               // Result code from a declined, aborted or failed transaction
               MposUi.RESULT_CODE_FAILED -&gt; {
                  Toast.makeText(findViewById(android.R.id.content), "Transaction was declined, aborted, or failed", Toast.LENGTH_LONG).show()
               }
           }
       }
   }
   ```
5. You can get the full transaction object by retrieving the `latestTransaction` property from the `mposUi` object.

   ```
   val transactionObject = mposUi.latestTransaction
   ```

Email a Customer Receipt {#tap-to-phone-payment-txn-email-receipt-task}
=======================================================================

Follow these steps to email a customer receipt from a previous transaction.

1. Retrieve the `SendEmailReceiptIntent` variable from the `mposUI` object and use the `startActivity` method to initiate the emailing a receipt flow.

   ```
   val SendEmailReceiptIntent = mposUi.createSendEmailReceiptIntent(transactionIdentifier)
   startActivityForResult(SendEmailReceiptIntent, MposUi.REQUEST_CODE_SEND_EMAIL)
   ```
2. After the emailing activity is completed, the `onActivityResult` method is triggered. This action returns information about the previous transaction.

   ```
   override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
       super.onActivityResult(requestCode, resultCode, data)
       "onActivityResult: $resultCode".logDebug(TAG)

       val parentLayout: View = activity!!.findViewById(android.R.id.content)

       if (requestCode == MposUi.REQUEST_CODE_SEND_EMAIL) {

           if (resultCode == MposUi.RESULT_CODE_EMAIL_SUCCESS) {
               Snackbar.make(parentLayout, "Receipt sent via email", Snackbar.LENGTH_SHORT).show()
           }
           else if (resultCode == MposUi.RESULT_CODE_EMAIL_FAILED) {
               Snackbar.make(parentLayout, "Fail while sending receipt via email", Snackbar.LENGTH_SHORT).show()
           }
       }
   }
   ```

Release Notes for Tap to Pay on Android Solution {#ttp-release-notes-intro}
===========================================================================

These release notes are organized by release name and version, from newest to oldest.  
Each release note includes these details:

* Name of release
* Type of release: app or SDK
* Version number
* Operating system: Android or iOS
* Release date: MM-DD-YYYY format

{#ttp-release-notes-intro_ul_qcb_lvk_k1c}These are the types of release notes published:


* General information
* Improvements
* New features
* Fixed issues
* Updated requirements
* Security updates
* Hot fixes
  {#ttp-release-notes-intro_ul_l24_23q_h1c}

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

