Getting Started with the Tap to Pay on iPhone Solution {#ttpay-ios-get-started-intro}
=====================================================================================

Use this information to get started with integrating the Tap to Pay on iPhone Solution. After completing the integration, you can start accepting payments. For more information, see [Tap to Pay on iPhone Payment Services](/docs/gateway/en-us/tap-to-pay-ios/integration/all/rest/tap-to-pay-ios/ttpay-ios-pymnt-svcs-intro.md "").

Configuring the Tap to Pay on iPhone SDK {#ttpay-ios-configure-intro}
=====================================================================

Use this information to configure the Tap to Pay on iPhone SDK.

Add the Tap to Pay on iPhone SDK to Your Xcode Project {#ttpay-ios-add-ttpay-on-iphone-sdk}
===========================================================================================

Follow these steps to add the Tap to Pay on iPhone SDK to your Xcode project.

> IMPORTANT Stay current with the latest SDK. The SDK repository is continuously updated to make available the six latest versions. When a new version is released, the oldest is removed and can no longer be used for new application builds. Establish a regular process for updating to the newest available SDK version to avoid potential build failures and to ensure that your application runs with the latest features, performance enhancements, and security updates.

1. In the Xcode app, click File.
2. Click Add Package Dependencies.
3. In the search bar, enter this GitHub link: [acceptance-devices-ios-sdk](https://github.com/relay/acceptance-devices-ios-sdk "").
4. Set the Dependency Rule to Up to Next Major Version.
5. Open the Add to Target drop-down menu, then choose your app.
6. Click Add Package.

Request the Tap to Pay on iPhone Entitlement {#ttpay-ios-request-ttp-on-iphone-entitlement}
===========================================================================================

You must have an Apple Developer account to complete this task. Use this [link](https://developer.apple.com/contact/request/tap-to-pay-on-iphone/ "") to create an account or to sign in to your existing account. To use the Tap to Pay on iPhone solution, you must request the Tap to Pay on iPhone entitlement from Apple and configure your application to use it.

1. [Sign in to your Apple Developer account.](https://developer.apple.com/contact/request/tap-to-pay-on-iphone/ "")
2. [Request the Tap to Pay on iPhone entitlement.](https://developer.apple.com/contact/request/tap-to-pay-on-iphone/ "")
3. Configure your application to use the Tap to Pay on iPhone entitlement. For more information, see [Setting up Tap to Pay on iPhone](https://developer.apple.com/documentation/proximityreader/setting-up-the-entitlement-for-tap-to-pay-on-iphone "") in the Apple Developer documentation.

Create a Sandbox Apple Account to Test Your Integration {#ttpay-ios-create-sandbox-apple-acct}
==============================================================================================

Before you can test your Tap to Pay on iPhone integration in a sandbox environment, you must create a Sandbox Apple account.  
Follow these steps to create a Sandbox Apple Account.

1. See the Apple Developer documentation: [Create a Sandbox Apple Account](https://developer.apple.com/help/app-store-connect/test-in-app-purchases/create-a-sandbox-apple-account/ "").
2. Sign in to your Sandbox Apple account from the device on which you will test transactions.

Generating a Secret Key for an Existing Merchant ID {#ttpay-ios-mid-secret-key-generate-intro}
==============================================================================================

Use this information to generate a secret key for an existing merchant ID (MID) in the `Business Center` or by using a REST API request. The secret key and MID are required values that you must enter in the `mposUIReader` instance that you create.

Generate a Secret Key for an Existing Merchant ID in the Business Center {#ttpay-ios-mid-secret-key-generate-ebc-task}
======================================================================================================================

You can generate a secret key for an existing merchant ID (MID) in the `Business Center`. You use these values when creating the `mposUIReader` instance.  
Follow these steps to generate a secret key for an existing MID in the `Business Center`.

1. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Key Management. The Key Management page appears.

2. From the Merchant drop-down list, choose a merchant ID.

3. Click Generate Key.

4. In the Recommended Key Types list, scroll down and choose Acceptance Devices Secret Key.

5. Click Generate Key. The Key Generation page appears.

6. Click Generate Key. Your MID and secret key appear on the page.

7. Click the Copy or Download icon to obtain the MID and secret key.

   #### ADDITIONAL INFORMATION

   > IMPORTANT
   > If you choose to copy the secret key instead of downloading it, save the information locally because you cannot return to the ` Business Center ` Key Generation page to obtain the same secret key. You must restart the process to obtain a new secret key.

Generate a Secret Key for an Existing Merchant ID Using a REST API Request {#ttpay-ios-mid-secret-key-generate-rest-api-task}
=============================================================================================================================

You can use a REST API request to generate a secret key for an existing merchant ID (MID). You must enter this value in the `mposUIReader` instance that you create.  
You must authenticate each request that you send to a `Payment Gateway` API. To authenticate an API request, you can use a REST shared secret key or a REST certificate. For more information about authentication requirements, see the [*Getting Started with REST Developer Guide*](https://developer.example.com/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md "").

Endpoints:
----------

**Test:** `POST ``https://apitest.example.com``/kms/v2/keys-sym-pos`  
**Production:** `POST ``https://api.example.com``/kms/v2/keys-sym-pos`

Required Fields to Generate a Secret Key for an Existing Merchant ID Using a REST API Request {#ttpay-ios-mid-secret-key-generate-api-reqfields}
================================================================================================================================================

This field is required to generate a secret key for an existing merchant ID when using a REST API request:

:
keyInformation.organizationId

REST Example: Generate a Secret Key for an Existing Merchant ID Using a REST API Request {#ttpay-ios-mid-secret-key-generate-api-ex-rest}
=========================================================================================================================================

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

Creating an `mposUIReader` Instance {#ttpay-ios-mposui-reader-intro}
====================================================================

Use this information to create and configure an `mposUIReader` instance. Before creating this instance, you must first create `Credentials` and `Configuration` objects.

Create an `mposUIReader` `Credentials` Object {#ttpay-ios-mposui-reader-credentials}
====================================================================================

Before starting this task, obtain a merchant ID and secret key. You use these values when creating the `Credentials` object.

> IMPORTANT  
> Things to know about migrating from SDK 3.5.0 to SDK 3.6.0:
>
> * The environment parameter was removed from the ` Credentials ` object.
> * Use the standalone ` MposEnvironment ` enum, with the value ` .live ` or ` .test `, when calling ` activate() `.

* The merchant parameter was renamed to merchantId .  
  The `Credentials` object is required to access the functionality of the Tap to Pay on iPhone SDK. Before you can create an `mposUIReader` instance, you must create the `Credentials` object.

1. Import `MposUI`.

2. Create a `Credentials` object.

3. Set the merchantId field value to the merchant ID that you obtained.

4. Set the secret field value to the secret key that you obtained.

   ```
   import MposUI

   let credentials = try Credentials(merchantId: "MerchantId",
                                     secret: "SecretKey")
   ```

Create an `mposUIReader` `Configuration` Object {#ttpay-ios-mposui-reader-configuraiton}
========================================================================================

Before you can create the `mposUIReader` instance in the Tap to Pay on iPhone SDK, you must create the `Configuration` object.  
Use the `Configuration` object to configure these parameters for the `mposUIReader` instance:

* Configure these Summary screen features:
  * Refund a transaction (`.refundTransaction`).
  * Send a receipt by email (`.sendReceiptViaEmail`).
  * Capture a transaction (`.captureTransaction`).
  * Increment a transaction (`.incrementTransaction`).
  * Retry a failed transaction (`.retryTransaction`).
    {#ttpay-ios-mposui-reader-configuraiton_ul_mkm_dm3_lyb}
* Configure the Summary screen so that it can be skipped (`.skipSummaryScreen`). The default setting is to show the Summary screen (`.displayIndefinitely`).
* Configure the signature capture so that it prints on the paper receipt (`.onReceipt`) or is skipped (`.none`). The default setting is on-screen signature capture.
* Configure the device activation process to prompt the merchant to enter the serial number of a previously activated device (`.manualInput`). The default setting is to show a list of previously activated devices and prompt the merchant to choose a device from the list (`.deviceList`).
* Configure the Serial Number Confirmation screen to be skipped (`.skip`). The default setting is to show the screen (`.showWithSerialNumber`).
  {#ttpay-ios-mposui-reader-configuraiton_ul_kpy_gl3_lyb}

1. Create the `Configuration` object.

   ```
   let configuration = Configuration(summaryFeatures: [.sendReceiptViaEmail, .refundTransaction, .captureTransaction, .incrementTransaction, .retryTransaction],
                                     resultConfiguration: .displayIndefinitely,
                                     signatureCapture: .onScreen,
                                     enrollmentConfiguration: .init(serialNumberInputMethod: deviceList, confirmationScreenOption: showWithSerialNumber)
                                     )
   ```

Create an `mposUIReader` Instance {#ttpay-ios-mposui-reader-instance}
=====================================================================

Before you can create the `mposUIReader` instance, you must create and configure the `Configuration` object.

> IMPORTANT
> Things to know about migrating from SDK 3.5.0 to SDK 3.6.0: If your app has activated devices in production, use the migration builder to preserve existing activations. This step migrates the device state from the old storage location to the new Apple Keychain-backed storage location and merchants do not need to reactivate their devices.
>
> ```
>   let reader: MposUIReader = await mposUiBuilder(
>     credentials: credentials,
>     environment: .live,
>     configuration: configuration
> )
>   
> ```
>
> Both builders return the same ` MposUIReader ` type. When all of your in-production merchants have upgraded to and used SDK 3.6.0 at least one time, switch to ` mposUIReaderBuilder ` in a future release.

1. Call `mposUIReaderBuilder` with the `Configuration` object to create an `mposUIReader` instance.

   ```
   let reader: MposUIReader = await mposUIReaderBuilder(
       configuration: configuration
   )
   ```

Managing Device Activation {#ttpay-ios-device-activate-intro}
=============================================================

Before you can use a device to process transactions, it must be activated. Activation registers the device with the payment platform. Use this information to manage device activation in the Tap to Pay on iPhone SDK.

> IMPORTANT  
> Things to know about migrating from SDK 3.5.0 to SDK 3.6.0:
>
> * The term ` Enrollment ` was replaced with ` Activation ` throughout the SDK.
> * The ` mposUI.enroll() ` method was replaced with ` reader.activation() `, followed by ` activation.activate(credentials:environment:) `.
> * The ` mposUI.enroll(with: serialNumber) ` method was replaced with ` activation.activate(credentials:environment:deviceId:) `.
> * The ` mposUI.enrollmentStatus() ` method was replaced with ` reader.activationStatus `, which is now an asynchronous property, not a method.
> * The ` .enrolling ` intermediate status no longer exists.

* Update your application code to handle these new result cases: ` .alreadyActivated ` and ` .activatedToAnotherMerchant `.

Activate a New Device Using Credentials {#ttpay-ios-device-activate-new-credentials}
====================================================================================

Use this information to activate a new device using credentials. When you activate the device, specify whether the device is used in the production environment or the sandbox environment.  
In the code example, the `environment` parameter is set to `.live` so that the device can be used to process real transactions. To activate a device for use in sandbox testing, set the `environment` parameter to `.test`.

1. Call `reader.activation()` to get an `MposUIActivation` object, and then call `activate(credentials:environment:)` with credentials and your chosen environment.

   ```
   let activation = try await reader.activation()
   let result: ActivationResult = await activation.activate(
       credentials: credentials,
       environment: .live
   )

   switch result {
   case .success(let device, let isNewDevice):
       print("Merchant: \(device.merchantId)")
       print("Device ID: \(device.deviceId)")
       print("Env: \(device.environment)")
       print("Currencies: \(device.supportedCurrencies)")
   case .cancelledByUser:
       print("Activation cancelled.")
   case .error(let developerInfo):
       print("Activation failed. Info: \(developerInfo)")
   @unknown default:
       break
   }
   ```

Activate a New Device Using an Activation Code {#ttpay-ios-device-activate-new-code}
====================================================================================

Use this information to activate a new device using an activation code. The activation code can be generated in the `Business Center` and is valid for 24 hours.  
There are two options for using an activation code to activate a new device. The merchant can enter the activation code on the device screen or the activation code can be passed programmatically.

> NOTE  
> The activation code must be sourced from a trusted backend channel and must never be logged or persisted on the device.  
> In the code example, the `environment` parameter in the `activateWithOtp(environment:)` call is set to `.live` so the device can be used to process real transactions. To activate a device for use in sandbox testing, set the `environment` parameter to `.test`.

1. Call `reader.activation()` to get an `MposUIActivation` object, and then call `activateWithOtp(environment:)` with your chosen environment.

   ```
   let activation = try await reader.activation()
   let result: ActivationResult = await activation.activateWithOtp(
       environment: .live,
       otp: nil
   )

   switch result {
   case .success(let device, let isNewDevice):
       print("Activated. Merchant: \(device.merchantId)")
   case .cancelledByUser:
       print("Activation cancelled.")
   case .invalidOTP(let developerInfo):
       print("Invalid OTP. Info: \(developerInfo)")
   case .error(let developerInfo):
       print("Activation failed. Info: \(developerInfo)")
   @unknown default:
       break
   }
   ```

Reactivate a Previously Activated Device Using Credentials {#ttpay-ios-device-activate-reactivate-credentials}
==============================================================================================================

Use this information to reactivate a previously activated device by using credentials and a stored serial number (`deviceId`, as shown in the code example). Supplying the stored device ID streamlines the activation workflow because the merchant does not need to manually select or enter the device ID during activation.  
In the code example, the `environment` parameter in the `activate(credentials:environment:deviceId:)` call is set to `.live` so the device can be used to process real transactions. To activate a device for use in sandbox testing, set the `environment` parameter to `.test`.

1. Call `reader.activation()` to get an `MposUIActivation` object, and then call `activate(credentials:environment:deviceId:)` with credentials, your chosen environment, and the stored device ID.

   ```
   let activation = try await reader.activation()
   let result: ActivationResult = await activation.activate(
       credentials: credentials,
       environment: .live,
       deviceId: "deviceId"
   )

   switch result {
   case .success(let device, let isNewDevice):
       print("Reactivated. Merchant: \(device.merchantId)")
       print("Device ID: \(device.deviceId)")
   case .cancelledByUser:
       print("Activation cancelled.")
   case .error(let developerInfo):
       print("Activation failed. Info: \(developerInfo)")
   @unknown default:
       break
   }
   ```

Reactivate a Previously Activated Device Using an Activation Code {#ttpay-ios-device-activate-reactivate-code}
==============================================================================================================

Use this information to reactivate a previously activated device by using an activation code and a stored serial number (`deviceId`, as shown in the code example). The activation code can be generated in the `Business Center` and is valid for 24 hours.
Supplying the stored device ID streamlines the activation workflow because the merchant does not need to manually select or enter the device ID during activation.  
There are two options for using an activation code during the device reactivation process. The merchant can enter the activation code on the device screen or the activation code can be passed programmatically.

> NOTE  
> The activation code must be sourced from a trusted backend channel and must never be logged or persisted on the device.  
> In the code example, the `environment` parameter in the `activateWithOtp(environment:deviceId:)` call is set to `.live` so the device can be used to process real transactions. To activate a device for use in sandbox testing, set the `environment` parameter to `.test`.

1. Call `reader.activation()` to get an `MposUIActivation` object, and then call `activateWithOtp(environment:deviceId:)` with your chosen environment and the stored device ID.

   ```
   let activation = try await reader.activation()
   let result: ActivationResult = await activation.activateWithOtp(
       environment: .live,
       deviceId: "deviceId"
   )

   switch result {
   case .success(let deviceId, let isNewDevice, let supportedCurrencies):
       print("Activation successful. Device ID: \(deviceId)")
   case .cancelledByUser:
       print("Activation cancelled.")
   case .alreadyActivated:
       print("Device is already activated for this merchant.")
   case .activatedToAnotherMerchant:
       print("Device is activated to a different merchant.")
   case .error(let developerInfo):
       print("Activation failed. Info: \(developerInfo)")
   }
   ```

Check Activation Status {#ttpay-ios-device-activate-check-status}
=================================================================

You can check the activation status only for a previously activated device. Use the `activationStatus` property to check whether the device is activated.

```
let status: ActivationStatus = await reader.activationStatus

switch status {
case .activated(let info):
    print("Merchant: \(info.merchantId)")
    print("Device:   \(info.deviceId)")
    print("Env:      \(info.environment)")
    print("Currencies: \(info.supportedCurrencies)")
case .notActivated:
    print("Device not activated. Please activate the device.")
}
```

Show Merchant Education Screens {#ttpay-ios-device-enroll-merch-edu-screens}
============================================================================

When a device activation is completed successfully, the Merchant Education screens must show on the device. The Merchant Education screens also must be accessible in your app's Settings or Help section.  
Use Apple's `ProximityReaderDiscovery` object to show the Merchant Education screens. This object provides the UI with information about how to use Tap to Pay on iPhone.

Enforcing Light Mode on the Device {#ttpay-ios-enforce-light-mode}
==================================================================

Use this information to configure the app to always display in Light Mode. When Dark Mode is enabled on the device, enforcing Light Mode for the app overrides the device setting and ensures high-contrast visibility for payment-related screens.

1. Add this key-value pair to the app's Info.plist file.

   ```
   &lt;key&gt;UIUserInterfaceStyle&lt;/key&gt;
   &lt;string&gt;Light&lt;/string&gt;
   ```

