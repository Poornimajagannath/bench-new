Samsung Pay Developer Guide {#applepay-about-guide}
===================================================

Audience and Purpose
--------------------

This document is written for merchants who want to enable customers to use Samsung Pay to pay for in-app purchases. This document provides an overview for integrating the Samsung Pay SDK and describes how to request the `Cybersource` API to process an authorization. Merchants must use the Samsung Pay SDK to receive the customer's encrypted payment data before requesting the `Cybersource` API to process the transaction.

Conventions
-----------

The following special statements are used in this document:

> An *Important* statement contains information essential to successfully completing a task or learning a concept.
> A *Warning* contains information or instructions, which, if not heeded, can result in a security risk, irreversible loss of data, or significant cost in time or revenue or both.

Related Documentation
---------------------

Refer to the Support Center for complete technical documentation:  
<http://www.cybersource.com/support_center/support_documentation>

Customer Support
----------------

For support information about any service, visit the Support Center:  
<http://support.example.com>

Recent Revisions to This Document {#samsungpay-doc-revisions}
=============================================================

24.02
-----

This revision contains only editorial changes and no technical updates.

24.01
-----

This revision contains only editorial changes and no technical updates.

23.01 {#samsungpay-doc-revisions_section_sj4_l11_4xb}
-----------------------------------------------------

Removed American Express and Discover as supported card types.

22.03
-----

Removed paymentNetworkToken_requestorID field from list of required fields and code examples for authorizations.

22.02
-----

Deprecated PNT assurance fields replaced with new fields
:
For `Platform Connect` only, the deprecated API request and response fields paymentNetworkToken_assuranceLevel are replaced with the new fields named paymentNetworkToken_assuranceMethod.

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE CARD PLATFORM CONNECT ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT CARD PLATFORM CONNECT ACQUIRER.

Requirements for Using Samsung Pay {#samsungpay-requirements}
=============================================================

In order to use the `Cybersource` platform to process Samsung Pay transactions, you must have:

* A `Cybersource` account. If you do not already have a `Cybersource` account, contact your local `Cybersource` sales representative.
* A merchant account with a supported processor.
* A profile on the Samsung Pay Partner Portal and an associated partner ID.
  {#samsungpay-requirements_ul_scm_kwb_s4b}

> Samsung Pay relies on authorizations with payment network tokens. You can sign up for Samsung Pay only when both of the following statements are true:
>
> * Your processor supports payment network tokens.
> * ` Cybersource ` supports payment network tokens with your processor.
>
> {#samsungpay-requirements_ul_ugr_qxb_s4b}  
> If one or both of the preceding statements are not true, you must take one of the following actions before you can sign up for Samsung Pay:
>
> * Obtain a new merchant account with a processor that supports payment network tokens.
> * Wait until your processor supports payment network tokens.
>   {#samsungpay-requirements_ul_tf5_txb_s4b}

Supported Card Types and Optional Features {#samsungpay-processors}
===================================================================

|                         Processor                         |                            Card Types                             |           Optional Features            |
|-----------------------------------------------------------|-------------------------------------------------------------------|----------------------------------------|
| `Platform Connect` Vantiv is the supported acquirer. | * JCB * Mastercard * Relay {#samsungpay-processors_ul_jh1_dwq_l4b} | * Recurring payments * Split shipments |

Related Information
-------------------

[Payments Developer Guide](https://developer.cybersource.com/docs.md#PaymentServices "")

Transaction Endpoints {#samsungpay-txn-endpoints}
=================================================

Test transactions:

* Akamai endpoint: <http://ics2testa.ic3.com/>

* Non-Akamai endpoint: <http://ics2test.ic3.com/>
  {#samsungpay-txn-endpoints_ul_hyw_gzw_dpb}  
  Production transactions:

* Akamai endpoint: <http://ics2a.ic3.com/>

* Non-Akamai endpoint: <http://ics2.ic3.com/>
  {#samsungpay-txn-endpoints_ul_eln_lzw_dpb}

Getting Started {#samsungpay-getting-started-intro}
===================================================

Follow these steps to set up Samsung Pay with `Cybersource`:

1. Registering with Samsung and `Cybersource`:
   1. [Registering with Samsung Pay](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-getting-started-intro/samsungpay-registering.md "")
   2. [Registering with Cybersource](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-getting-started-intro/samsungpay-registering-cybs.md "")
      {#samsungpay-getting-started-intro_ol_ed4_pcn_fpb}
2. Integrating the Samsung SDK, which includes the following tasks:
   1. [Creating a Project](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-getting-started-intro/samsungpay-creating-project.md "")
   2. [Integrating the Samsung Pay SDK](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-getting-started-intro/samsungpay-integrating-sdk.md "")
   3. [Using the API Key](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-getting-started-intro/samsungpay-using-api-key.md "")
3. Using the Samsung SDK to:
   1. [Verify That Your Application is Eligible for Samsung Pay](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-getting-started-intro/samsungpay-initalize-for-app.md "")
   2. [Initiating a Payment](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-getting-started-intro/samsungpay-initiating-payment.md "")
   3. [Requesting a Payment](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-getting-started-intro/samsungpay-requesting-payment.md "")
      {#samsungpay-getting-started-intro_ol_pvr_pwm_fpb}

Registering with Samsung Pay {#samsungpay_registering}
======================================================

1. Create a profile by completing the merchant application on the Samsung Pay Partner Portal.

   #### ADDITIONAL INFORMATION

   After your merchant application is approved, you receive a unique partner ID. Include this ID in your application. You need the partner ID in order to generate a Certificate Signing Request (CSR) in the ` Business Center `. Samsung requires the CSR file in order to encrypt sensitive payment data; it contains an identifier and public key.

2. Using the Samsung Pay Partner Portal, upload the CSR file.

3. Enter an application name and a package name. When you associate the CSR file with the application, Samsung generates a product ID.

4. Create login details for application developers on the Samsung Pay Partner Portal.

5. Download and integrate the Samsung Pay SDK into your application.

   #### ADDITIONAL INFORMATION

   The SDK contains:

   * A Javadoc
   * The Samsung Pay SDK files *samsungpay.jar* and *sdk-v1.0.0.jar*
   * A sample app
   * The branding guide
   * Image files
6. Register a Samsung account ID and request a *debug-api-key* file using the Samsung Pay Partner Portal. The Samsung account ID, the *debug-api-key*, and the product ID are used to validate your application so that you can use the Samsung Pay SDK for testing.

7. Submit your application for approval using the Samsung Pay Partner Portal. Upload the final version of the Android Application Package (APK) file using the Samsung Pay Partner Portal, and include screenshots of your checkout page displaying the Samsung Pay logo.

Registering with `Cybersource` {#samsungpay_registering_cybs}
=============================================================

1. Log in to the `Business Center`:

   #### ADDITIONAL INFORMATION

   * Create a CSR file for test transactions: [`https://businesscentertest.cybersource.com`](https://businesscentertest.cybersource.com "")
   * Create a CSR file for production transactions: [`https://businesscentertest.cybersource.com`](https://businesscenter.cybersource.com "")
     {#samsungpay_registering_cybs_ol_iph_jdx_dpb}
2. On the left navigation pane, click the Payment Configuration icon.

3. Click Digital Payment Solutions. The Digital Payments page opens.

4. Click Configure. The Samsung Pay Registration panel opens.

5. Enter your Samsung partner ID.

6. Click Generate New CSR.

7. To download your CSR, click the Download icon next to the key.

8. Follow your browser's instructions to save and open the file.

   #### ADDITIONAL INFORMATION

   > Only one CSR is permitted for each unique Samsung partner ID. If you modify your Samsung partner ID, you must generate a new CSR.

9. Complete the enrollment process by submitting your CSR to Samsung.

Creating a Project {#samsungpay-creating-project}
=================================================

You use Android Studio to create a new Android Studio project, which is required to integrate the Samsung SDK.

1. Download Android Studio from the following website: [https://developer.android.com/studio/index.html](https://developer.android.com/studio/index.md "").
2. Open Android Studio and click Start a new Android Studio project.
3. In the New Project settings menu, enter the name of your application and the company domain.
4. To change the package name, click Edit. By default, Android Studio sets the last element of the project's package name to the name of your application.
5. Click Next.
6. In the Target Android Devices settings menu, choose the required API levels.
7. Click Next.
8. Choose the required activity and click Finish.

Integrating the Samsung Pay SDK {#samsungpay-integrating-sdk}
=============================================================

1. Add the *samsungpay.jar* and *sdk-v1.0.0.jar* files to the *libs* folder of your Android project.

2. Choose Gradle Scripts \&gt; build.gradle and enter the dependencies shown below.

   #### ADDITIONAL INFORMATION

   ```
   dependencies {
       compile files('libs/samsungpay.jar')
       compile files(libs/sdk-v1.0.0.jar')
   }          
   ```
3. Import the package.

   #### ADDITIONAL INFORMATION

   ```
   import com.samsung.android.sdk.samsungpay;              
   ```

Using the API Key {#samsungpay-using-api-key}
=============================================

The API key is used to verify that your app (in debug mode or release mode) can use the Samsung Pay SDK APIs with the Samsung Pay application. To get the API key, you must create a *debug-api-key* file and include it in the *manifest* file.

1. To use the API key, include it in the *manifest* file with a custom tag. This enables the merchant app android *manifest* file to provide the `DebugMode`, `spay_debug_api_key` values as metadata.

Example: Debug Mode {#samsungpay-apikey-ex-debug}
=================================================

```
&lt;meta-data
    android:name="debug_mode"
    android:value="Y" /&gt;
&lt;meta-data
    android:name="spay_debug_api_key"
    android:value="asdfggkndkeie17283094858" /&gt;                                 
```

Example: Release Mode {#samsungpay_apikey_ex_release}
=====================================================

```
&lt;meta-data
    android:name="debug_mode"
    android:value="N" /&gt;                         
```

Verify That Your Application is Eligible for Samsung Pay {#samsungpay-initalize-for-app}
========================================================================================

You must initialize the *SSamsungPay* class to verify that your application is eligible for Samsung Pay and to display the Samsung Pay button to the customer (refer to branding guidelines).  
The *SSamsungPay* class provides the following API methods:

* `initialize()`---initializes the Samsung Pay SDK and verifies eligibility for Samsung Pay, including the device, software, and business area.

  > Request the ` initialize() ` API method of the *SSamsungPay* class before using the Samsung Pay SDK.

* `getVersionCode()`---retrieves the version number of the Samsung Pay SDK as an integer.

* `getVersionName()`---retrieves the version name of the Samsung Pay SDK as a string.
  {#samsungpay-initalize-for-app_ul_s5x_cdr_2pb}  
  After the `initialize()` API method request is successful, display the Samsung Pay button to the customer.  
  If the `initialize()` API method request fails, the method displays one of the following errors:

* `SsdkUnsupportedException`---the device is not a Samsung device or does not support the Samsung Pay package.

* `NullPointerException`---the context passed is null.
  {#samsungpay-initalize-for-app_ul_lnf_pdr_2pb}

Example: Samsung Pay Class {#samsungpay_ex_pay_class}
=====================================================

```
SSamsungPay spay = new SSamsungPay();
try {
    spay.initialize(mContext);
} catch (SsdkUnsupportedException e1) {
    e1.printStackTrace();
    pay_button.setVisibility(View.INVISIBLE);
}                
```

Initiating a Payment {#samsungpay_initiating_payment}
=====================================================

You are required to use a specific transaction request structure and required fields to initiate a payment.

Required Fields for Initiating a Payment {#samsungpay-initiate-mandatory}
=========================================================================

The following fields are required for initiating a payment; include these fields in the `PaymentInfo` class:

> If the required fields are not included, you receive a ` NullPointerException ` error.

Merchant Name
:
The merchant name as it appears on the payment sheet of Samsung Pay and customer's bank statement.

Amount
:

Payment Protocol
:
3-D Secure.

Permitted Card Brands
:
Specify the card brands that are supported such as American Express, JCB, Mastercard, or Relay.

Merchant ID
:

Order Number
:

Shipping Address
:
This field is required if SEND_SHIPPING or NEED_BILLING_AND_SEND_SHIPPING is set for `AddressVisibilityOption`.

Address Visibility Option
:

Card Holder Name
:

Recurring Option
:

Example: Transaction Request Structure {#samsungpay-ex-txn-req-structure}
=========================================================================

```
private PaymentInfo makeTransactionDetails() {
// Supported card brands
ArrayList&lt;CardInfo.Brand&gt; brandList = new ArrayList&lt;CardInfo.Brand&gt;();
if (cardBrand.isChecked())
brandList.add(CardInfo.Brand.CARD);
if (mcBrand.isChecked())
brandList.add(CardInfo.Brand.Mastercard);
if (amexBrand.isChecked())
brandList.add(CardInfo.Brand.AMERICANEXPRESS);

// Basic payment information
PaymentInfo paymentReq = new PaymentInfo.Builder()
.setMerchantId(“merchantID”)
.setMerchantName("Test").setAmount(getAmount())
.setShippingAddress(getShippingAddressInfo())
.setOrderNumber(orderNoView.getText().toString())
.setPaymentProtocol(PaymentProtocol.PROTOCOL_3DS)
.setAddressInPaymentSheet(AddressInPaymentSheet.DO_NOT_SHOW)
.setAllowedCardBrands(brandList) .setRecurringEnabled(isRecurring)
.setCardHolderNameEnabled(isCardHolderNameRequired)
.build();
return paymentReq;
}

// Add shipping address details
private Address getShippingAddressInfo() {
Address address = new Address.Builder()
.setAddressee(name.getText().toString())
.setAddressLine1(addLine1.getText().toString())
.setAddressLine2(addline2.getText().toString())
.setCity(city.getText().toString())
.setState(state.getText().toString())
.setCountryCode(country.getSelectedItem().toString())
.setPostalCode(zip.getText().toString()).build(); return address;
}

// Add amount details private Amount getAmount() {
Amount amount = new Amount.Builder()
.setCurrencyCode(currencyType.getSelectedItem().toString())
.setItemTotalPrice(productPrice.getText().toString())
.setShippingPrice(shippingPrice.getText().toString())
.setTax(taxPrice.getText().toString())
.setTotalPrice(totalAmount.getText().toString()).build();
return amount;
}            
```

Requesting a Payment {#samsungpay-requesting-payment}
=====================================================

1. Use the `startSamsungPay()` API method in the `PaymentManager` class. The `PaymentManager` class includes the following API methods:

   #### ADDITIONAL INFORMATION

   * `startSamsungPay()`---requests to initiate payment with Samsung Pay.
   * `updateAmount()`---updates the transaction amount if shipping address or card information is updated by Samsung Pay.
   * `updateAmountFailed()`---returns an error code when the new amount cannot be updated because of a wrong address.
2. Request the `startSamsungPay()` API method and include the following data:

   #### ADDITIONAL INFORMATION

   * `PaymentInfo`---contains payment information.
   * `PID`---the product ID created in the Samsung Pay Partner Portal.
   * `StatusListener`---the result of the payment request is delivered to `StatusListener`. This listener should be registered before you call the `startSamsungPay()` API method.

   When you request the `startSamsungPay()` API method, the Samsung Pay online payment sheet is displayed on your application. The customer selects a registered card for payment and can also update the billing and shipping address.  
   The payment reply is delivered as one of the following events to `StatusListener`:

   * `onSuccess()`---this event is requested when Samsung Pay confirms the payment. It includes `encryptedPaymentCredential` in JSON format:
     * **method:** Payment protocol: 3-D Secure.
     * **merchant_ref:** Merchant reference code.
     * **billing_address.street**: Number, street name.
     * **billing_address.state_province:** Two-letter state code.
     * **billing_address.zip_postal_code:** Five-character zip code.
     * **billing_address.city:** City name.
     * **billing_address.county:**Two-letter country code.
     * **3ds.type:** `S` for Samsung Pay. Encrypted.
     * **3ds.version:** Current version `100`. Encrypted.
     * **3ds.data:** Base64-encoded payment data. Encrypted.
       {#samsungpay-requesting-payment_ul_wd1_dhr_2pb} Refer to the Samsung Pay developer website for information on how to decrypt the encrypted payment credential.

* `onFailure()`---this event is requested when the transaction fails. It returns an error code and error message.

Example: Request startSamsungPay() API Method {#samsungpay-ex-req-startsp-method}
=================================================================================

```
public void onPayButtonClicked(View v) {
    // Call startSamsungPay() method of PaymentManager class.
    // To create a transaction request for makeTransactionDetails() in
    the following code, see Example: Transaction Request Structure.
    try {
        mPaymentManager.startSamsungPay(makeTransactionDetails(), "enter
        product ID",
mStatusListener);
    } catch (NullPointerException e) {
    e.printStackTrace();
    }
}

private PaymentManager.StatusListener mStatusListener = new
PaymentManager.StatusListener() {
    @Override
    public void onFailure(int errCode, String msg) {
        Log.d(TAG, " onFailed );
    }
    @Override
    public void onSuccess(PaymentInfo arg0, String result) {
        Log.d(TAG, "onSuccess ");
    };                        
```

Services {#samsungpay_services}
===============================

The following services are available:

* [Authorization Service](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro.md "")
* [Authorization Reversal Service](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-reversal-intro.md "")
* [Capture Service](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-capture-intro.md "")
* [Sale Service](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-sale-intro.md "")
  {#samsungpay_services_ul_ewn_45f_fpb}

Authorization Service {#samsungpay-auth-intro}
==============================================

You can authorize a payment for Samsung Pay using two different types of decryption methods: `Cybersource` or Merchant. Each decryption method requires a different set of required API fields. In addition, depending on which card type is used, different fields are required for requesting the authorization service.

|    Payment Processor    |                             Authorization and Capture Information                             |
|-------------------------|-----------------------------------------------------------------------------------------------|
| `Platform Connect` | `Platform Connect` limits authorization and capture amounts to 999999999999 (twelve 9s). |
[Processor-Specific Information About Authorizations and Captures]

Authorizing a Payment with JCB Using `Cybersource` Decryption Method {#samsungpay-auth-cybs-jcb-intro}
======================================================================================================

This section provides the following information:

* [Required Fields for Authorizing a Payment Using JCB and the Cybersource Decryption Method](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-cybs-jcb-intro/samsungpay-auth-cybsdecypt-jcb-mandatory.md "")
* [Authorizing a Payment](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-cybs-jcb-intro/samsungpay-auth-procedure.md "")
* [Example: Cybersource Decryption with JCB Using the Simple Order API](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-cybs-jcb-intro/samsungpay-auth-cybsdecrypt-ex-jcb-so.md "")
  {#samsungpay-auth-cybs-jcb-intro_ul_xb4_psp_npb}

Required Fields for Authorizing a Payment Using JCB and the `Cybersource` Decryption Method {#samsungpay-auth-cybsdecypt-jcb-mandatory}
=======================================================================================================================================

The following fields are required when submitting an authorization request using the `Cybersource` decryption method:

* encryptedPayment_data-set this field to the Base64-encoded value obtained from the paymentData property of the PKPaymentToken object.
* encryptedPayment_descriptor-set this field to` RklEPUNPTU1PTi5TQU1TVU5HLklOQVBQLlBBWU1FTlQ=`.
* paymentSolution-set this field to `008`.

Related Information {#samsungpay-auth-cybsdecypt-jcb-mandatory_section_abb_khn_b1c}
-----------------------------------------------------------------------------------

[Simple Order API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/so/api-fields/api-fields-so-intro.md "")

Authorizing a Payment {#samsung-auth-procedure}
===============================================

1. Request the service. Set the ccAuthService_run field to `true`, and send the request to one of these endpoints:
   * [transactionProcessor](https://ics2ws.ic3.com/commerce/1.x/transactionProcessor "")
   * [transactionProcessor](https://ics2wsa.ic3.com/commerce/1.x/transactionProcessor "")
     {#samsung-auth-procedure_auth-s1-request-so}
2. Include the required fields in the request. {#samsung-auth-procedure_auth-s2-reqfields}
3. Include optional fields in the request as needed.{#samsung-auth-procedure_auth-s3-optfields}
4. Check the response message to make sure that the request was successful. A value of `ACCEPT` for the decision field indicates success. For information about reason codes, see [Reason Codes for the Simple Order API](https://developer.cybersource.com/docs/cybs/en-us/reason-codes-so/reference/all/so/reason-codes-so/reason-codes-so.md "").

Example: `Cybersource` Decryption with JCB Using the Simple Order API {#samsungpay-auth-cybsdecrypt-ex-jcb-so}
==============================================================================================================

Authorization Request

```
&lt;requestMessage xmlns="urn:schemas-cybersource-com:transaction-data-1.121"&gt;
    &lt;merchantID&gt;demomerchant&lt;/merchantID&gt;
    &lt;merchantReferenceCode&gt;demorefnum&lt;/merchantReferenceCode&gt;
    &lt;billTo&gt;
        &lt;firstName&gt;Jane&lt;/firstName&gt;
        &lt;lastName&gt;Smith&lt;/lastName&gt;
        &lt;street1&gt;123 Main Street&lt;/street1&gt;
        &lt;city&gt;Small Town&lt;/city&gt;
        &lt;state&gt;CA&lt;/state&gt;
        &lt;postalCode&gt;98765&lt;/postalCode&gt;
        &lt;country&gt;US&lt;/country&gt;
        &lt;email&gt;jsmith@example.com&lt;/email&gt;
    &lt;/billTo&gt;
    &lt;purchaseTotals&gt;
        &lt;currency&gt;USD&lt;/currency&gt;
        &lt;grandTotalAmount&gt;5.00&lt;/grandTotalAmount&gt;
    &lt;/purchaseTotals&gt;
    &lt;encryptedPayment&gt;
        &lt;descriptor&gt;RklEPUNPTU1PTi5TQU1TVU5HLklOQVBQLlBBWU1FTlQ=&lt;/descriptor&gt;
        &lt;data&gt;ABCDEFabcdefABCDEFabcdef0987654321234567&lt;/data&gt;
        &lt;encoding&gt;Base64&lt;/encoding&gt;
    &lt;/encryptedPayment&gt;
    &lt;card&gt;
        &lt;cardType&gt;007&lt;/cardType&gt;
    &lt;/card&gt;
    &lt;ccAuthService run="true"/&gt;
        &lt;paymentSolution&gt;008&lt;/paymentSolution&gt;
&lt;/requestMessage&gt;    
```

Authorization Response

```
&lt;c:replyMessage&gt;
    &lt;c:merchantReferenceCode&gt;demorefnum&lt;/c:merchantReferenceCode&gt;
    &lt;c:requestID&gt;4465840340765000001541&lt;/c:requestID&gt;
    &lt;c:decision&gt;ACCEPT&lt;/c:decision&gt;
    &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
    &lt;c:token&gt;
        &lt;c:expirationMonth&gt;07&lt;/c:expirationMonth&gt;
        &lt;c:expirationYear&gt;2025&lt;/c:expirationYear&gt;
        &lt;c:prefix&gt;239845&lt;/c:prefix&gt;
        &lt;c:suffix&gt;2947&lt;/c:suffix&gt;
    &lt;/c:token&gt;
    &lt;c:purchaseTotals&gt;
        &lt;c:currency&gt;USD&lt;/c:currency&gt;
    &lt;/c:purchaseTotals&gt;
    &lt;c:ccAuthReply&gt;
        &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
        &lt;c:amount&gt;5.00&lt;/c:amount&gt;
        &lt;c:authorizationCode&gt;888888&lt;/c:authorizationCode&gt;
        &lt;c:avsCode&gt;X&lt;/c:avsCode&gt;
        &lt;c:avsCodeRaw&gt;I1&lt;/c:avsCodeRaw&gt;
        &lt;c:processorResponse&gt;100&lt;/c:processorResponse&gt;
        &lt;c:reconciliationID&gt;11267051CGJSMQDC&lt;/c:reconciliationID&gt;
    &lt;/c:ccAuthReply&gt;
&lt;/c:replyMessage&gt;
```

Authorizing a Payment with Mastercard Using `Cybersource` Decryption Method {#samsungpay-auth-cybs-mc-intro}
============================================================================================================

This section provides the following information:

* [Required Fields for Authorizing a Payment Using Mastercard and the Cybersource Decryption Method](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-cybs-mc-intro/samsungpay-auth-cybsdecypt-mc-mandatory.md "")
* [Authorizing a Payment](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-cybs-jcb-intro/samsungpay-auth-procedure.md "")
* [Example: Cybersource Decryption with Mastercard Using the Simple Order API](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-cybs-mc-intro/samsungpay-auth-cybsdecrypt-ex-mc-so.md "")
  {#samsungpay-auth-cybs-mc-intro_ul_oj3_jtp_npb}

Required Fields for Authorizing a Payment Using Mastercard and the `Cybersource` Decryption Method {#samsungpay-auth-cybsdecypt-mc-mandatory}
=============================================================================================================================================

The following fields are required when submitting an authorization request using the `Cybersource` decryption method:

* ccAuthService_commerceIndicator-set this field to `spa`.
* encryptedPayment_data
  * Set the field to the value that was returned from Samsung Pay in the *3ds.data* block as follows:
    * Retrieve the payment data from Samsung Pay in JSON Web Encryption (JWE) format.
    * Encode it in Base64.
    * Add the value to the encryptedPayment_data field.
* encryptedPayment_descriptor-set this field to` RklEPUNPTU1PTi5TQU1TVU5HLklOQVBQLlBBWU1FTlQ=`.
* paymentNetworkToken_transactionType-set this field to `1`.
* paymentSolution-set this field to `008`.

Related Information {#samsungpay-auth-cybsdecypt-mc-mandatory_section_abb_khn_b1c}
----------------------------------------------------------------------------------

[Simple Order API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/so/api-fields/api-fields-so-intro.md "")

Example: `Cybersource` Decryption with Mastercard Using the Simple Order API {#samsungpay-auth-cybsdecrypt-ex-mc-so}
====================================================================================================================

Authorization Request

```
&lt;requestMessage xmlns="urn:schemas-cybersource-com:transaction-data-1.121"&gt;
    &lt;merchantID&gt;demomerchant&lt;/merchantID&gt;
    &lt;merchantReferenceCode&gt;demorefnum&lt;/merchantReferenceCode&gt;
    &lt;billTo&gt;
        &lt;firstName&gt;James&lt;/firstName&gt;
        &lt;lastName&gt;Smith&lt;/lastName&gt;
        &lt;street1&gt;1295 Charleston Road&lt;/street1&gt;
        &lt;city&gt;Test City&lt;/city&gt;
        &lt;state&gt;CA&lt;/state&gt;
        &lt;postalCode&gt;99999&lt;/postalCode&gt;
        &lt;country&gt;US&lt;/country&gt;
        &lt;email&gt;demo@example.com&lt;/email&gt;
    &lt;/billTo&gt;
    &lt;purchaseTotals&gt;
        &lt;currency&gt;USD&lt;/currency&gt;
        &lt;grandTotalAmount&gt;5.00&lt;/grandTotalAmount&gt;
    &lt;/purchaseTotals&gt;
    &lt;ccAuthService run="true"&gt;
        &lt;commerceIndicator&gt;spa&lt;/commerceIndicator&gt;
    &lt;/ccAuthService&gt;
    &lt;encryptedPayment&gt;
        &lt;data&gt;ABCDEFabcdefABCDEFabcdef0987654321234567&lt;/data&gt;
        &lt;descriptor&gt;RklEPUNPTU1PTi5TQU1TVU5HLklOQVBQLlBBWU1FTlQ=&lt;/descriptor&gt;
    &lt;/encryptedPayment&gt;
    &lt;paymentSolution&gt;008&lt;/paymentSolution&gt;
    &lt;paymentNetworkToken&gt;
        &lt;transactionType&gt;1&lt;/transactionType&gt;
    &lt;/paymentNetworkToken&gt;
&lt;/requestMessage&gt;    
```

Authorization Response

```
&lt;c:replyMessage&gt;
    &lt;c:merchantReferenceCode&gt;demorefnum&lt;/c:merchantReferenceCode&gt;
    &lt;c:requestID&gt;4465840340765000001541&lt;/c:requestID&gt;
    &lt;c:decision&gt;ACCEPT&lt;/c:decision&gt;
    &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
    &lt;c:purchaseTotals&gt;
        &lt;c:currency&gt;USD&lt;/c:currency&gt;
    &lt;/c:purchaseTotals&gt;
    &lt;c:ccAuthReply&gt;
        &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
        &lt;c:amount&gt;5.00&lt;/c:amount&gt;
        &lt;c:authorizationCode&gt;888888&lt;/c:authorizationCode&gt;
        &lt;c:avsCode&gt;X&lt;/c:avsCode&gt;
        &lt;c:avsCodeRaw&gt;I1&lt;/c:avsCodeRaw&gt;
        &lt;c:authorizedDateTime&gt;2015-11-03T20:53:54Z&lt;/c:authorizedDateTime&gt;
        &lt;c:processorResponse&gt;100&lt;/c:processorResponse&gt;
        &lt;c:reconciliationID&gt;11267051CGJSMQDC&lt;/c:reconciliationID&gt;
    &lt;/c:ccAuthReply&gt;
    &lt;c:token&gt;
        &lt;c:prefix&gt;128945&lt;/c:prefix&gt;
        &lt;c:suffix&gt;2398&lt;/c:suffix&gt;
        &lt;c:expirationMonth&gt;08&lt;/c:expirationMonth&gt;
        &lt;c:expirationYear&gt;2021&lt;/c:expirationYear&gt;
    &lt;/c:token&gt;
&lt;/c:replyMessage&gt;
```

Authorizing a Payment with Relay Using `Cybersource` Decryption Method {#samsungpay-auth-cybs-relay-intro}
========================================================================================================

This section provides the following information:

* [Required Fields for Authorizing a Payment Using Relay and the Cybersource Decryption Method](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-cybs-relay-intro/samsungpay-auth-cybsdecypt-relay-mandatory.md "")
* [Authorizing a Payment](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-cybs-jcb-intro/samsungpay-auth-procedure.md "")
* [Example: Cybersource Decryption with Relay Using the Simple Order API](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-cybs-relay-intro/samsungpay-auth-cybsdecrypt-ex-relay-so.md "")
  {#samsungpay-auth-cybs-relay-intro_ul_oj3_jtp_npb}

Required Fields for Authorizing a Payment Using Relay and the `Cybersource` Decryption Method {#samsungpay-auth-cybsdecypt-relay-mandatory}
=========================================================================================================================================

The following fields are required when submitting an authorization request using the `Cybersource` decryption method:

* ccAuthService_commerceIndicator-set this field to `internet`.
* encryptedPayment_data
  * Set the field to the value that was returned from Samsung Pay in the *3ds.data* block as follows:
    * Retrieve the payment data from Samsung Pay in JSON Web Encryption (JWE) format.
    * Encode it in Base64.
    * Add the value to the encryptedPayment_data field.
* encryptedPayment_descriptor-set this field to` RklEPUNPTU1PTi5TQU1TVU5HLklOQVBQLlBBWU1FTlQ=`.
* paymentNetworkToken_transactionType-set this field to `1`.
* paymentSolution-set this field to `008`.

Related Information {#samsungpay-auth-cybsdecypt-relay-mandatory_section_abb_khn_b1c}
------------------------------------------------------------------------------------

[Simple Order API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/so/api-fields/api-fields-so-intro.md "")

Example: `Cybersource` Decryption with Relay Using the Simple Order API {#samsungpay-auth-cybsdecrypt-ex-relay-so}
================================================================================================================

Authorization Request

```
&lt;requestMessage xmlns="urn:schemas-cybersource-com:transaction-data-1.121"&gt;
    &lt;merchantID&gt;demomerchant&lt;/merchantID&gt;
    &lt;merchantReferenceCode&gt;demorefnum&lt;/merchantReferenceCode&gt;
    &lt;billTo&gt;
        &lt;firstName&gt;James&lt;/firstName&gt;
        &lt;lastName&gt;Smith&lt;/lastName&gt;
        &lt;street1&gt;1295 Charleston Road&lt;/street1&gt;
        &lt;city&gt;Test City&lt;/city&gt;
        &lt;state&gt;CA&lt;/state&gt;
        &lt;postalCode&gt;99999&lt;/postalCode&gt;
        &lt;country&gt;US&lt;/country&gt;
        &lt;email&gt;demo@example.com&lt;/email&gt;
    &lt;/billTo&gt;
    &lt;purchaseTotals&gt;
        &lt;currency&gt;USD&lt;/currency&gt;
        &lt;grandTotalAmount&gt;5.00&lt;/grandTotalAmount&gt;
    &lt;/purchaseTotals&gt;
    &lt;ccAuthService run="true"&gt;
        &lt;commerceIndicator&gt;internet&lt;/commerceIndicator&gt;
    &lt;/ccAuthService&gt;
    &lt;encryptedPayment&gt;
        &lt;data&gt;ABCDEFabcdefABCDEFabcdef0987654321234567&lt;/data&gt;
        &lt;descriptor&gt;RklEPUNPTU1PTi5TQU1TVU5HLklOQVBQLlBBWU1FTlQ=&lt;/descriptor&gt;
    &lt;/encryptedPayment&gt;
    &lt;paymentSolution&gt;008&lt;/paymentSolution&gt;
    &lt;paymentNetworkToken&gt;
        &lt;transactionType&gt;1&lt;/transactionType&gt;
    &lt;/paymentNetworkToken&gt;
&lt;/requestMessage&gt;    
```

Authorization Response

```
&lt;c:replyMessage&gt;
    &lt;c:merchantReferenceCode&gt;demorefnum&lt;/c:merchantReferenceCode&gt;
    &lt;c:requestID&gt;4465840340765000001541&lt;/c:requestID&gt;
    &lt;c:decision&gt;ACCEPT&lt;/c:decision&gt;
    &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
    &lt;c:purchaseTotals&gt;
        &lt;c:currency&gt;USD&lt;/c:currency&gt;
    &lt;/c:purchaseTotals&gt;
    &lt;c:ccAuthReply&gt;
        &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
        &lt;c:amount&gt;5.00&lt;/c:amount&gt;
        &lt;c:authorizationCode&gt;888888&lt;/c:authorizationCode&gt;
        &lt;c:avsCode&gt;X&lt;/c:avsCode&gt;
        &lt;c:avsCodeRaw&gt;I1&lt;/c:avsCodeRaw&gt;
        &lt;c:authorizedDateTime&gt;2015-11-03T20:53:54Z&lt;/c:authorizedDateTime&gt;
        &lt;c:processorResponse&gt;100&lt;/c:processorResponse&gt;
        &lt;c:reconciliationID&gt;11267051CGJSMQDC&lt;/c:reconciliationID&gt;
    &lt;/c:ccAuthReply&gt;
    &lt;c:token&gt;
        &lt;c:prefix&gt;294672&lt;/c:prefix&gt;
        &lt;c:suffix&gt;4397&lt;/c:suffix&gt;
        &lt;c:expirationMonth&gt;08&lt;/c:expirationMonth&gt;
        &lt;c:expirationYear&gt;2021&lt;/c:expirationYear&gt;
    &lt;/c:token&gt;
&lt;/c:replyMessage&gt;
```

Authorizing a Payment with JCB Using Merchant Decryption Method {#samsungpay-auth-merchant-jcb-intro}
=====================================================================================================

This section provides the following information:

* [Required Fields for Authorizing a Payment Using JCB and the Merchant Decryption Method](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-merchant-jcb-intro/samsungpay-auth-merdecypt-jcb-mandatory.md "")
* [Authorizing a Payment](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-cybs-jcb-intro/samsungpay-auth-procedure.md "")
* [Example: Merchant Decryption with JCB Using the Simple Order API](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-merchant-jcb-intro/samsungpay-auth-merdecrypt-ex-jcb-so.md "")
  {#samsungpay-auth-merchant-jcb-intro_ul_pcj_krp_npb}

Required Fields for Authorizing a Payment Using JCB and the Merchant Decryption Method {#samsungpay-auth-merdecypt-jcb-mandatory}
=================================================================================================================================

The following fields are required when submitting an authorization request using the Merchant decryption method:

* ccAuthService_cavv-set this field to the 3-D Secure cryptogram of the payment network token.
* card_accountNumber-set this field to the payment network token value.
* card_expirationMonth-set this field to the payment network token expiration month value.
* card_expirationYear-set this field to the payment network token expiration year value.
* ccAuthService_eciRaw-set this field to the ECI value contained in the Samsung Pay reply message.
* ccAuthService_networkTokenCryptogram-set this field to the network token cryptogram.
* paymentNetworkToken_transactionType-set this field to `1`.
* paymentSolution-set this field to `008`.

Related Information {#samsungpay-auth-merdecypt-jcb-mandatory_section_abb_khn_b1c}
----------------------------------------------------------------------------------

[Simple Order API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/so/api-fields/api-fields-so-intro.md "")

Example: Merchant Decryption with JCB Using the Simple Order API {#samsungpay-auth-merdecrypt-ex-jcb-so}
========================================================================================================

Authorization Request

```
&lt;requestMessage xmlns="urn:schemas-cybersource-com:transaction-data-1.121"&gt;
    &lt;merchantID&gt;demomerchant&lt;/merchantID&gt;
    &lt;merchantReferenceCode&gt;demorefnum&lt;/merchantReferenceCode&gt;
    &lt;billTo&gt;
        &lt;firstName&gt;Jane&lt;/firstName&gt;
        &lt;lastName&gt;Smith&lt;/lastName&gt;
        &lt;street1&gt;123 Main Street&lt;/street1&gt;
        &lt;city&gt;Small Town&lt;/city&gt;
        &lt;state&gt;CA&lt;/state&gt;
        &lt;postalCode&gt;98765&lt;/postalCode&gt;
        &lt;country&gt;US&lt;/country&gt;
        &lt;email&gt;jsmith@example.com&lt;/email&gt;
    &lt;/billTo&gt;
    &lt;purchaseTotals&gt;
        &lt;currency&gt;USD&lt;/currency&gt;
        &lt;grandTotalAmount&gt;5.00&lt;/grandTotalAmount&gt;
    &lt;/purchaseTotals&gt;
    &lt;card&gt;
        &lt;accountNumber&gt;xxxx11111111xxxx&lt;/accountNumber&gt;
        &lt;expirationMonth&gt;12&lt;/expirationMonth&gt;
        &lt;expirationYear&gt;2020&lt;/expirationYear&gt;
        &lt;cvNumber&gt;123&lt;/cvNumber&gt;
        &lt;cardType&gt;007&lt;/cardType&gt;
    &lt;/card&gt;
    &lt;ccAuthService run="true"&gt;
        &lt;cavv&gt;ABCDEFabcdefABCDEFabcdef0987654321234567&lt;/cavv&gt;
        &lt;eciRaw&gt;5&lt;/eciRaw&gt;
    &lt;/ccAuthService&gt;
    &lt;paymentNetworkToken&gt;
        &lt;transactionType&gt;1&lt;/transactionType&gt;
    &lt;/paymentNetworkToken&gt;
    &lt;paymentSolution&gt;008&lt;/paymentSolution&gt;
&lt;/requestMessage&gt;
```

Authorization Response

```
&lt;c:replyMessage&gt;
    &lt;c:merchantReferenceCode&gt;demorefnum&lt;/c:merchantReferenceCode&gt;
    &lt;c:requestID&gt;4465840340765000001541&lt;/c:requestID&gt;
    &lt;c:decision&gt;ACCEPT&lt;/c:decision&gt;
    &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
    &lt;c:purchaseTotals&gt;
        &lt;c:currency&gt;USD&lt;/c:currency&gt;
    &lt;/c:purchaseTotals&gt;
    &lt;c:ccAuthReply&gt;
        &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
        &lt;c:amount&gt;5.00&lt;/c:amount&gt;
        &lt;c:authorizationCode&gt;888888&lt;/c:authorizationCode&gt;
        &lt;c:avsCode&gt;X&lt;/c:avsCode&gt;
        &lt;c:avsCodeRaw&gt;I1&lt;/c:avsCodeRaw&gt;
        &lt;c:authorizedDateTime&gt;2015-11-03T20:53:54Z&lt;/c:authorizedDateTime&gt;
        &lt;c:processorResponse&gt;100&lt;/c:processorResponse&gt;
        &lt;c:reconciliationID&gt;11267051CGJSMQDC&lt;/c:reconciliationID&gt;
    &lt;/c:ccAuthReply&gt;
&lt;/c:replyMessage&gt;
```

NVP Request

```
merchantID=demomerchant
merchantReferenceCode=demorefnum
billTo_firstName=Jane
billTo_lastName=Smith
billTo_street1=123 Main Street
billTo_city=Small Town
billTo_state=CA
billTo_postalCode=98765
billTo_country=US
billTo_email=jsmith@example.com
purchaseTotals_currency=USD
purchastTotals_grandTotalAmount=5.00
card_accountNumber=xxxx00202036xxxx
card_expirationYear=2020
card_cvnNumber=123
cardType=007
ccAuthService_cavv=ABCDEFabcdefABCDEFabcdef0987654321234567
ccAuthService_eciRaw=5
paymentNetworkToken_requestorID=987654321plokijuhygtfrdeswa 
paymentNetworkToken_transactionType=1
paymentSolution=008
```

NVP Response

```
merchantReferenceCode=demorefnum
requestID=4465840340765000001541
decision=accept
reasonCode=100
requestToken=Ahj/7wSR5C/4Icd2fdAKakGLadfg5535r/ghx3Z90AoBj3u
purchaseTotals_currency=USD
ccAuthReply_reasonCode=100
ccAuthReply_amount=5.00
ccAuthReply_authorizationCode=888888
ccAuthReply_avsCode=X
ccAuthReply_avsCodeRaw=I1
ccAuthReply_authorizedDateTime=2015-11-03T20:53:54Z
ccAuthReply_processorResponse=100
ccAuthReply_reconciliationID=11267051CGJSMQDC
```

Authorizing a Payment with Mastercard Using Merchant Decryption Method {#samsungpay-auth-merchant-mc-intro}
===========================================================================================================

This section provides the following information:

* [Required Fields for Authorizing a Payment Using Mastercard and the Merchant Decryption Method](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-merchant-mc-intro/samsungpay-auth-merdecypt-mc-mandatory.md "")
* [Authorizing a Payment](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-cybs-jcb-intro/samsungpay-auth-procedure.md "")
* [Example: Merchant Decryption with Mastercard Using the Simple Order API](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-merchant-mc-intro/samsungpay-auth-merdecrypt-ex-mc-so.md "")
  {#samsungpay-auth-merchant-mc-intro_ul_pcj_krp_npb}

Required Fields for Authorizing a Payment Using Mastercard and the Merchant Decryption Method {#samsungpay-auth-merdecypt-mc-mandatory}
=======================================================================================================================================

The following fields are required when submitting an authorization request using the Merchant decryption method:

* card_accountNumber-set this field to the payment network token value.
* card_expirationMonth-set this field to the payment network token expiration month value.
* card_expirationYear-set this field to the payment network token expiration year value.
* ccAuthService_commerceIndicator- set this field to `spa`.
* ccAuthService_networkTokenCryptogram-set this field to the network token cryptogram.
* paymentNetworkToken_transactionType-set this field to `1`.
* paymentSolution-set this field to `008`.
* ucaf_authenticationData--set this field to the 3-D Secure cryptogram of the payment network token.
* ucaf_collectionIndicator-set this field to `2`.

Related Information {#samsungpay-auth-merdecypt-mc-mandatory_section_abb_khn_b1c}
---------------------------------------------------------------------------------

[Simple Order API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/so/api-fields/api-fields-so-intro.md "")

Example: Merchant Decryption with Mastercard Using the Simple Order API {#samsungpay-auth-merdecrypt-ex-mc-so}
==============================================================================================================

Authorization Request

```
&lt;requestMessage xmlns="urn:schemas-cybersource-com:transaction-data-1.121"&gt;
    &lt;merchantID&gt;demomerchant&lt;/merchantID&gt;
    &lt;merchantReferenceCode&gt;demorefnum&lt;/merchantReferenceCode&gt;
    &lt;billTo&gt;
        &lt;firstName&gt;James&lt;/firstName&gt;
        &lt;lastName&gt;Smith&lt;/lastName&gt;
        &lt;street1&gt;1295 Charleston Road&lt;/street1&gt;
        &lt;city&gt;Test City&lt;/city&gt;
        &lt;state&gt;CA&lt;/state&gt;
        &lt;postalCode&gt;99999&lt;/postalCode&gt;
        &lt;country&gt;US&lt;/country&gt;
        &lt;email&gt;demo@example.com&lt;/email&gt;
    &lt;/billTo&gt;
    &lt;purchaseTotals&gt;
        &lt;currency&gt;USD&lt;/currency&gt;
        &lt;grandTotalAmount&gt;5.00&lt;/grandTotalAmount&gt;
    &lt;/purchaseTotals&gt;
    &lt;card&gt;
        &lt;accountNumber&gt;xxxx55555555xxxx&lt;/accountNumber&gt;
        &lt;expirationMonth&gt;12&lt;/expirationMonth&gt;
        &lt;expirationYear&gt;2020&lt;/expirationYear&gt;
    &lt;/card&gt;
    &lt;ucaf&gt;
        &lt;authenticationData&gt;ABCDEFabcdefABCDscdef0987654321234567&lt;/authenticationData&gt;
        &lt;collectionIndicator&gt;2&lt;/collectionIndicator&gt;
    &lt;/ucaf&gt;
    &lt;ccAuthService run="true"&gt;
        &lt;commerceIndicator&gt;spa&lt;/commerceIndicator&gt;
    &lt;/ccAuthService&gt;
    &lt;paymentNetworkToken&gt;
        &lt;transactionType&gt;1&lt;/transactionType&gt;
    &lt;/paymentNetworkToken&gt;
    &lt;paymentSolution&gt;008&lt;/paymentSolution&gt;
&lt;/requestMessage&gt;    
```

Authorization Response

```
&lt;c:replyMessage&gt;
    &lt;c:merchantReferenceCode&gt;demorefnum&lt;/c:merchantReferenceCode&gt;
    &lt;c:requestID&gt;4465840340765000001541&lt;/c:requestID&gt;
    &lt;c:decision&gt;ACCEPT&lt;/c:decision&gt;
    &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
    &lt;c:purchaseTotals&gt;
        &lt;c:currency&gt;USD&lt;/c:currency&gt;
    &lt;/c:purchaseTotals&gt;
    &lt;c:ccAuthReply&gt;
        &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
        &lt;c:amount&gt;5.00&lt;/c:amount&gt;
        &lt;c:authorizationCode&gt;888888&lt;/c:authorizationCode&gt;
        &lt;c:avsCode&gt;X&lt;/c:avsCode&gt;
        &lt;c:avsCodeRaw&gt;I1&lt;/c:avsCodeRaw&gt;
        &lt;c:authorizedDateTime&gt;2015-11-03T20:53:54Z&lt;/c:authorizedDateTime&gt;
        &lt;c:processorResponse&gt;100&lt;/c:processorResponse&gt;
        &lt;c:reconciliationID&gt;11267051CGJSMQDC&lt;/c:reconciliationID&gt;
    &lt;/c:ccAuthReply&gt;
&lt;/c:replyMessage&gt;
```

Authorizing a Payment with Relay Using Merchant Decryption Method {#samsungpay-auth-merchant-relay-intro}
=======================================================================================================

This section provides the following information:

* [Required Fields for Authorizing a Payment Using Relay and the Merchant Decryption Method](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-merchant-relay-intro/samsungpay-auth-merdecypt-relay-mandatory.md "")
* [Authorizing a Payment](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-cybs-jcb-intro/samsungpay-auth-procedure.md "")
* [Example: Merchant Decryption with Relay Using the Simple Order API](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-merchant-relay-intro/samsungpay-auth-merdecrypt-ex-relay-so.md "")
  {#samsungpay-auth-merchant-relay-intro_ul_pcj_krp_npb}

Required Fields for Authorizing a Payment Using Relay and the Merchant Decryption Method {#samsungpay-auth-merdecypt-relay-mandatory}
===================================================================================================================================

The following fields are required when submitting an authorization request using the Merchant decryption method:

* ccAuthService_cavv-set this field to the 3-D Secure cryptogram of the payment network token.
* card_accountNumber-set this field to the payment network token value.
* card_expirationMonth-set this field to the payment network token expiration month value.
* card_expirationYear-set this field to the payment network token expiration year value.
* ccAuthService_eciRaw-for JCB transactions, set this field to the ECI value contained in the Samsung Pay reply message.
* ccAuthService_commerceIndicator-set this field to `internet`.
* ccAuthService_networkTokenCryptogram-set this field to the network token cryptogram.
* paymentNetworkToken_transactionType-set this field to `1`.
* paymentSolution-set this field to `008`.

Related Information {#samsungpay-auth-merdecypt-relay-mandatory_section_abb_khn_b1c}
-----------------------------------------------------------------------------------

[Simple Order API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/so/api-fields/api-fields-so-intro.md "")

Example: Merchant Decryption with Relay Using the Simple Order API {#samsungpay-auth-merdecrypt-ex-relay-so}
==========================================================================================================

Authorization Request

```
&lt;requestMessage xmlns="urn:schemas-cybersource-com:transaction-data-1.121"&gt;
    &lt;merchantID&gt;demomerchant&lt;/merchantID&gt;
    &lt;merchantReferenceCode&gt;demorefnum&lt;/merchantReferenceCode&gt;
    &lt;billTo&gt;
        &lt;firstName&gt;James&lt;/firstName&gt;
        &lt;lastName&gt;Smith&lt;/lastName&gt;
        &lt;street1&gt;1295 Charleston Road&lt;/street1&gt;
        &lt;city&gt;Test City&lt;/city&gt;
        &lt;state&gt;CA&lt;/state&gt;
        &lt;postalCode&gt;99999&lt;/postalCode&gt;
        &lt;country&gt;US&lt;/country&gt;
        &lt;email&gt;demo@example.com&lt;/email&gt;
    &lt;/billTo&gt;
    &lt;purchaseTotals&gt;
        &lt;currency&gt;USD&lt;/currency&gt;
        &lt;grandTotalAmount&gt;5.00&lt;/grandTotalAmount&gt;
    &lt;/purchaseTotals&gt;
    &lt;card&gt;
        &lt;accountNumber&gt;xxxx10000000xxxx&lt;/accountNumber&gt;
        &lt;expirationMonth&gt;12&lt;/expirationMonth&gt;
        &lt;expirationYear&gt;2020&lt;/expirationYear&gt;
    &lt;/card&gt;
    &lt;ccAuthService run="true"&gt;
        &lt;cavv&gt;ABCDEFabcdefABCDEFabcdef0987654321234567&lt;/cavv&gt;
        &lt;commerceIndicator&gt;internet&lt;/commerceIndicator&gt;
    &lt;/ccAuthService&gt;
    &lt;paymentNetworkToken&gt;
        &lt;transactionType&gt;1&lt;/transactionType&gt;
    &lt;/paymentNetworkToken&gt;
    &lt;paymentSolution&gt;008&lt;/paymentSolution&gt;
&lt;/requestMessage&gt;    
```

Authorization Response

```
&lt;c:replyMessage&gt;
    &lt;c:merchantReferenceCode&gt;demorefnum&lt;/c:merchantReferenceCode&gt;
    &lt;c:requestID&gt;4465840340765000001541&lt;/c:requestID&gt;
    &lt;c:decision&gt;ACCEPT&lt;/c:decision&gt;
    &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
    &lt;c:purchaseTotals&gt;
        &lt;c:currency&gt;USD&lt;/c:currency&gt;
    &lt;/c:purchaseTotals&gt;
    &lt;c:ccAuthReply&gt;
        &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
        &lt;c:amount&gt;5.00&lt;/c:amount&gt;
        &lt;c:authorizationCode&gt;888888&lt;/c:authorizationCode&gt;
        &lt;c:avsCode&gt;X&lt;/c:avsCode&gt;
        &lt;c:avsCodeRaw&gt;I1&lt;/c:avsCodeRaw&gt;
        &lt;c:authorizedDateTime&gt;2015-11-03T20:53:54Z&lt;/c:authorizedDateTime&gt;
        &lt;c:processorResponse&gt;100&lt;/c:processorResponse&gt;
        &lt;c:reconciliationID&gt;11267051CGJSMQDC&lt;/c:reconciliationID&gt;
    &lt;/c:ccAuthReply&gt;
&lt;/c:replyMessage&gt;
```

Authorization Reversal Service {#samsungpay-reversal-intro}
===========================================================

The authorization reversal service is a follow-on service that uses the request ID returned from the previous authorization. An authorization reversal releases the hold that the authorization placed on the customer's credit card funds. Use this service to reverse an unnecessary or undesired authorization.

|    Payment Processor    |                                                      Authorization Reversal Information                                                      |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `Platform Connect` | Card types supported for full authorization reversals: American Express, China UnionPay, Diners Club, Discover, JCB, mada, Mastercard, Relay. |
[Processor-Specific Information About Authorization Reversals]

Required Fields for Reversing an Authorization {#samsungpay-reversal-mandatory}
===============================================================================

The following fields are required when creating an authorization reversal request:

ccAuthReversalService_authRequestID
:
Set to the request ID that was included in the authorization reply message.

ccAuthReversalService_run
:
Set to `true`.

merchantID
:

merchantReferenceCode
:

paymentSolution
:
Set to `008`.

purchaseTotals_currency
:

purchaseTotals_grandTotalAmount
:
Either purchaseTotals_grandTotalAmount or item_#_unitPrice must be included in the request.

Related Information {#samsungpay-reversal-mandatory_section_abb_khn_b1c}
------------------------------------------------------------------------

[Simple Order API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/so/api-fields/api-fields-so-intro.md "")

Reversing an Authorization {#samsungpay-reversal-procedure}
===========================================================

1. Request the service. Set the ccAuthReversalService_run field to `true`, and send the request to one of these endpoints:
   * `https://ics2ws.ic3.com/commerce/1.x/transactionProcessor`
   * `https://ics2wsa.ic3.com/commerce/1.x/transactionProcessor`
     {#samsungpay-reversal-procedure_choices_wc1_pkn_b1c}
2. Check the response message to make sure that the request was successful. A value of `ACCEPT` for the decision field indicates success. For information about reason codes, see [Reason Codes for the Simple Order API](https://developer.cybersource.com/docs/cybs/en-us/reason-codes-so/reference/all/so/reason-codes-so/reason-codes-so.md "").

XML Example: Basic Credit Card Authorization Reversal Using the Simple Order API {#samsungpay-reversal-ex-xml-so}
=================================================================================================================

Authorization Reversal Request

```
&lt;requestMessage xmlns="urn:schemas-cybersource-com:transaction-data-1.121"&gt;
    &lt;merchantID&gt;retail_910&lt;/merchantID&gt;
    &lt;merchantReferenceCode&gt;MS299131501003&lt;/merchantReferenceCode&gt;
    &lt;purchaseTotals&gt;
        &lt;currency&gt;USD&lt;/currency&gt;
        &lt;grandTotalAmount&gt;99.49&lt;/grandTotalAmount&gt;
    &lt;/purchaseTotals&gt;
    &lt;ccAuthReversalService run="true"&gt;
        &lt;authRequestID&gt;6152173358406291304007&lt;/authRequestID&gt;
    &lt;/ccAuthReversalService&gt;
    &lt;paymentSolution&gt;008&lt;/paymentSolution&gt;
&lt;/requestMessage&gt;
```

Authorization Reversal Response

```
&lt;c:replyMessage xmlns="urn:schemas-cybersource-com:transaction-data-1.121"&gt;
    &lt;c:merchantReferenceCode&gt;MS299131501003&lt;/c:merchantReferenceCode&gt;
    &lt;c:requestID&gt;1019827520348290570293&lt;/c:requestID&gt;
    &lt;c:purchaseTotals&gt;
        &lt;c:currency&gt;USD&lt;/c:currency&gt;
    &lt;/c:purchaseTotals&gt;
    &lt;c:ccAuthReversalReply&gt;
        &lt;c:amount&gt;99.49&lt;/c:amount&gt;
        &lt;c:authorizationCode&gt;1&lt;/c:authorizationCode&gt;
    &lt;/c:ccAuthReversalReply&gt;
&lt;/c:replyMessage&gt;
```

Capture Service {#samsungpay-capture-intro}
===========================================

The capture service is a follow-on service that uses the request ID returned from the previous authorization. The request ID links the capture to the authorization. This service transfers funds from the customer's account to your bank and usually takes two to four days to complete.

|    Payment Processor    |                             Authorization and Capture Information                             |
|-------------------------|-----------------------------------------------------------------------------------------------|
| `Platform Connect` | `Platform Connect` limits authorization and capture amounts to 999999999999 (twelve 9s). |
[Processor-Specific Information About Authorizations and Captures]

Required Fields for Capturing a Payment {#samsungpay-capture-mandatory}
=======================================================================

The following fields are required when creating a capture request:

ccCaptureService_authRequestID
:
Set to the request ID that was included in the authorization reply message. Optional when ccAuthService and ccCaptureService are in the same request.

ccCaptureService_run
:
Set to `true`.

merchantID
:

merchantReferenceCode
:

paymentSolution
:
Set to `008`.

purchaseTotals_currency
:

purchaseTotals_grandTotalAmount
:
Either purchaseTotals_grandTotalAmount or item_#_unitPrice must be included in the request.

Related Information {#samsungpay-capture-mandatory_section_abb_khn_b1c}
-----------------------------------------------------------------------

[Simple Order API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/so/api-fields/api-fields-so-intro.md "")

Capturing a Payment {#samsungpay-capture-procedure}
===================================================

1. Request the service. Set the ics_applications field to `ics_bill`, and send the request to one of these endpoints:
   * `https://ics2ws.ic3.com/commerce/1.x/transactionProcessor `
   * `https://ics2wsa.ic3.com/commerce/1.x/transactionProcessor`
     {#samsungpay-capture-procedure_choices_b3c_4ln_b1c}
2. Check the response message to make sure that the request was successful. A value of `ACCEPT` for the decision field indicates success. For information about reason codes, see [Reason Codes for the Simple Order API](https://developer.cybersource.com/docs/cybs/en-us/reason-codes-so/reference/all/so/reason-codes-so/reason-codes-so.md "").

XML Example: Basic Credit Card Capture Using the Simple Order API {#samsungpay-capture-ex-xml-so}
=================================================================================================

Capture Request

```
&lt;requestMessage xmlns="urn:schemas-cybersource-com:transaction-data-1.37"&gt;
    &lt;merchantID&gt;Napa Valley Vacations&lt;/merchantID&gt;
    &lt;merchantReferenceCode&gt;482046C3A7E94F5BD1FE3C66C&lt;/merchantReferenceCode&gt;
    &lt;item id="0"&gt;
        &lt;unitPrice&gt;49.95&lt;/unitPrice&gt;
        &lt;quantity&gt;1&lt;/quantity&gt;
    &lt;/item&gt;
    &lt;purchaseTotals&gt;
        &lt;currency&gt;USD&lt;/currency&gt;
    &lt;/purchaseTotals&gt;
    &lt;ccCaptureService run="true"&gt;
        &lt;authRequestID&gt;0305782650000167905080&lt;/authRequestID&gt;
    &lt;/ccCaptureService&gt;
    &lt;paymentSolution&gt;008&lt;/paymentSolution&gt;
&lt;/requestMessage&gt;
```

Capture Response

```
&lt;c:replyMessage xmlns:c="urn:schemas-cybersource-com:transaction-data-1.37"&gt;
    &lt;c:merchantReferenceCode&gt;482046C3A7E94F5BD1FE3C66C&lt;/c:merchantReferenceCode&gt;
    &lt;c:requestID&gt;1019827520348290570293&lt;/c:requestID&gt;
    &lt;c:decision&gt;ACCEPT&lt;/c:decision&gt;
    &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
    &lt;c:purchaseTotals&gt;
        &lt;c:currency&gt;USD&lt;/c:currency&gt;
    &lt;/c:purchaseTotals&gt;
    &lt;c:ccCaptureReply&gt;
        &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
        &lt;c:amount&gt;49.95&lt;/c:amount&gt;
        &lt;c:reconciliationID&gt;1094820975023470&lt;/c:reconciliationID&gt;
    &lt;/c:ccCaptureReply&gt;
&lt;/c:replyMessage&gt;
```

Sale Service {#samsungpay-sale-intro}
=====================================

A sale is a bundled authorization and capture. Request the authorization and capture services at the same time. `Cybersource` processes the capture immediately.

Required Fields for Performing a Sale {#samsungpay-sale-cybsdecypt-amex-mandatory}
==================================================================================

The following fields are required when submitting a sale request:

ccCaptureService_run
:
Set this field to `true`.

Fields required for requesting the authorization service
:
Use the same values that are set for requesting the [Authorization Service](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro.md "").

Related Information {#samsungpay-sale-cybsdecypt-amex-mandatory_section_abb_khn_b1c}
------------------------------------------------------------------------------------

[Simple Order API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/so/api-fields/api-fields-so-intro.md "")

Authorizing and Capturing a Payment {#samsungpay-sale-procedure}
================================================================

You can authorize and capture a payment at the same time, which is known as performing a sale.

1. Request the service. Set the ics_applications field to `ics_auth,ics_bill`, and send the request to one of these internet endpoints:
   * `https://ics2ws.ic3.com/commerce/1.x/transactionProcessor`
   * `https://ics2wsa.ic3.com/commerce/1.x/transactionProcessor`
     {#samsungpay-sale-procedure_choices_m3g_1mn_b1c}
2. Check the response message to make sure that the request was successful. A value of `ACCEPT` for the decision field indicates success. For information about reason codes, see [Reason Codes for the Simple Order API](https://developer.cybersource.com/docs/cybs/en-us/reason-codes-so/reference/all/so/reason-codes-so/reason-codes-so.md "").

XML Example: Basic Credit Card Sale Using the Simple Order API {#samsungpay-sale-ex-xml-so}
===========================================================================================

Authorization and Capture (Sale) Request

```
&lt;requestMessage xmlns="urn:schemas-cybersource-com:transaction-data-1.121"&gt;
    &lt;merchantID&gt;demomerchant&lt;/merchantID&gt;
    &lt;merchantReferenceCode&gt;demorefnum&lt;/merchantReferenceCode&gt;
    &lt;billTo&gt;
        &lt;firstName&gt;James&lt;/firstName&gt;
        &lt;lastName&gt;Smith&lt;/lastName&gt;
        &lt;street1&gt;1295 Charleston Road&lt;/street1&gt;
        &lt;city&gt;Test City&lt;/city&gt;
        &lt;state&gt;CA&lt;/state&gt;
        &lt;postalCode&gt;99999&lt;/postalCode&gt;
        &lt;country&gt;US&lt;/country&gt;
        &lt;email&gt;demo@example.com&lt;/email&gt;
    &lt;/billTo&gt;
    &lt;purchaseTotals&gt;
        &lt;currency&gt;USD&lt;/currency&gt;
        &lt;grandTotalAmount&gt;5.00&lt;/grandTotalAmount&gt;
    &lt;/purchaseTotals&gt;
    &lt;ccCaptureService run="true"&gt;
        &lt;commerceIndicator&gt;aesk&lt;/commerceIndicator&gt;
    &lt;/ccCaptureService&gt;
    &lt;encryptedPayment&gt;
        &lt;data&gt;ABCDEFabcdefABCDEFabcdef0987654321234567&lt;/data&gt;
        &lt;descriptor&gt;RklEPUNPTU1PTi5TQU1TVU5HLklOQVBQLlBBWU1FTlQ=&lt;/descriptor&gt;
    &lt;/encryptedPayment&gt;
    &lt;paymentSolution&gt;008&lt;/paymentSolution&gt;
    &lt;paymentNetworkToken&gt;
        &lt;transactionType&gt;1&lt;/transactionType&gt;
    &lt;/paymentNetworkToken&gt;
&lt;/requestMessage&gt;    
```

Authorization and Capture (Sale) Response

```
&lt;c:replyMessage&gt;
    &lt;c:merchantReferenceCode&gt;demorefnum&lt;/c:merchantReferenceCode&gt;
    &lt;c:requestID&gt;4465840340765000001541&lt;/c:requestID&gt;
    &lt;c:decision&gt;ACCEPT&lt;/c:decision&gt;
    &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
    &lt;c:purchaseTotals&gt;
        &lt;c:currency&gt;USD&lt;/c:currency&gt;
    &lt;/c:purchaseTotals&gt;
    &lt;c:ccAuthReply&gt;
        &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
        &lt;c:amount&gt;5.00&lt;/c:amount&gt;
        &lt;c:authorizationCode&gt;888888&lt;/c:authorizationCode&gt;
        &lt;c:avsCode&gt;V&lt;/c:avsCode&gt;
        &lt;c:avsCodeRaw&gt;I1&lt;/c:avsCodeRaw&gt;
        &lt;c:authorizedDateTime&gt;2015-11-03T20:53:54Z&lt;/c:authorizedDateTime&gt;
        &lt;c:processorResponse&gt;100&lt;/c:processorResponse&gt;
        &lt;c:reconciliationID&gt;11267051CGJSMQDC&lt;/c:reconciliationID&gt;
    &lt;/c:ccAuthReply&gt;
    &lt;c:ccCaptureReply&gt;
        &lt;c:reconciliationID&gt;02850840187309570&lt;/c:reconciliationID&gt;
        &lt;c:amount&gt;100.00&lt;/c:amount&gt;
    &lt;/c:ccCaptureReply&gt;
    &lt;c:token&gt;
        &lt;c:prefix&gt;593056&lt;/c:prefix&gt;
        &lt;c:suffix&gt;0842&lt;/c:suffix&gt;
        &lt;c:expirationMonth&gt;08&lt;/c:expirationMonth&gt;
        &lt;c:expirationYear&gt;2021&lt;/c:expirationYear&gt;
    &lt;/c:token&gt;
&lt;/c:replyMessage&gt;
```

Authorizing a Payment with American Express Using `Cybersource` Decryption Method {#samsungpay-auth-cybs-amex-intro}
====================================================================================================================

This section provides the following information:

* [Required Fields for Authorizing a Payment Using American Express and the Cybersource Decryption Method](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-auth-cybsdecypt-amex-mandatory.md "")
* [Authorizing a Payment](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-cybs-jcb-intro/samsungpay-auth-procedure.md "")
* [Example: Cybersource Decryption with American Express Using the Simple Order API](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-auth-cybsdecrypt-ex-amex-so.md "")
  {#samsungpay-auth-cybs-amex-intro_ul_pcj_krp_npb}

Example: `Cybersource` Decryption with American Express Using the Simple Order API {#samsungpay-auth-cybsdecrypt-ex-amex-so}
============================================================================================================================

Authorization Request

```
&lt;requestMessage xmlns="urn:schemas-cybersource-com:transaction-data-1.121"&gt;
    &lt;merchantID&gt;demomerchant&lt;/merchantID&gt;
    &lt;merchantReferenceCode&gt;demorefnum&lt;/merchantReferenceCode&gt;
    &lt;billTo&gt;
        &lt;firstName&gt;James&lt;/firstName&gt;
        &lt;lastName&gt;Smith&lt;/lastName&gt;
        &lt;street1&gt;1295 Charleston Road&lt;/street1&gt;
        &lt;city&gt;Test City&lt;/city&gt;
        &lt;state&gt;CA&lt;/state&gt;
        &lt;postalCode&gt;99999&lt;/postalCode&gt;
        &lt;country&gt;US&lt;/country&gt;
        &lt;email&gt;demo@example.com&lt;/email&gt;
    &lt;/billTo&gt;
    &lt;purchaseTotals&gt;
        &lt;currency&gt;USD&lt;/currency&gt;
        &lt;grandTotalAmount&gt;5.00&lt;/grandTotalAmount&gt;
    &lt;/purchaseTotals&gt;
    &lt;ccAuthService run="true"&gt;
        &lt;commerceIndicator&gt;aesk&lt;/commerceIndicator&gt;
    &lt;/ccAuthService&gt;
    &lt;encryptedPayment&gt;
        &lt;data&gt;ABCDEFabcdefABCDEFabcdef0987654321234567&lt;/data&gt;
        &lt;descriptor&gt;RklEPUNPTU1PTi5TQU1TVU5HLklOQVBQLlBBWU1FTlQ=&lt;/descriptor&gt;
    &lt;/encryptedPayment&gt;
    &lt;paymentSolution&gt;008&lt;/paymentSolution&gt;
    &lt;paymentNetworkToken&gt;
        &lt;transactionType&gt;1&lt;/transactionType&gt;
    &lt;/paymentNetworkToken&gt;
&lt;/requestMessage&gt;    
```

Authorization Response

```
&lt;c:replyMessage&gt;
    &lt;c:merchantReferenceCode&gt;demorefnum&lt;/c:merchantReferenceCode&gt;
    &lt;c:requestID&gt;4465840340765000001541&lt;/c:requestID&gt;
    &lt;c:decision&gt;ACCEPT&lt;/c:decision&gt;
    &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
    &lt;c:purchaseTotals&gt;
        &lt;c:currency&gt;USD&lt;/c:currency&gt;
    &lt;/c:purchaseTotals&gt;
    &lt;c:ccAuthReply&gt;
        &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
        &lt;c:amount&gt;5.00&lt;/c:amount&gt;
        &lt;c:authorizationCode&gt;888888&lt;/c:authorizationCode&gt;
        &lt;c:avsCode&gt;V&lt;/c:avsCode&gt;
        &lt;c:avsCodeRaw&gt;I1&lt;/c:avsCodeRaw&gt;
        &lt;c:authorizedDateTime&gt;2015-11-03T20:53:54Z&lt;/c:authorizedDateTime&gt;
        &lt;c:processorResponse&gt;100&lt;/c:processorResponse&gt;
        &lt;c:reconciliationID&gt;11267051CGJSMQDC&lt;/c:reconciliationID&gt;
    &lt;/c:ccAuthReply&gt;
    &lt;c:token&gt;
        &lt;c:prefix&gt;593056&lt;/c:prefix&gt;
        &lt;c:suffix&gt;0842&lt;/c:suffix&gt;
        &lt;c:expirationMonth&gt;08&lt;/c:expirationMonth&gt;
        &lt;c:expirationYear&gt;2021&lt;/c:expirationYear&gt;
    &lt;/c:token&gt;
&lt;/c:replyMessage&gt;
```

Required Fields for Authorizing a Payment Using American Express and the Merchant Decryption Method {#samsungpay-auth-merdecypt-amex-mandatory}
===============================================================================================================================================

The following fields are required when submitting an authorization request using the Merchant decryption method:

* ccAuthService_cavv-set this field to the 3-D Secure cryptogram of the payment network token. Include the whole 20-byte cryptogram in the cavv field. For a 40-byte cryptogram, split the cryptogram into two 20-byte binary values (block A and block B). Set the cavv field to the block A value and set the xid field to the block B value.
* card_accountNumber-set this field to the payment network token value.
* card_expirationMonth-set this field to the payment network token expiration month value.
* card_expirationYear-set this field to the payment network token expiration year value.
* ccAuthService_commerceIndicator-set this field to `aesk`.
* ccAuthService_networkTokenCryptogram-set this field to the network token cryptogram.
* paymentNetworkToken_transactionType-set this field to `1`.
* paymentSolution-set this field to `008`.

Related Information {#samsungpay-auth-merdecypt-amex-mandatory_section_abb_khn_b1c}
-----------------------------------------------------------------------------------

[Simple Order API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/so/api-fields/api-fields-so-intro.md "")

Authorizing a Payment with American Express Using Merchant Decryption Method {#samsungpay-auth-merchant-amex-intro}
===================================================================================================================

This section provides the following information:

* [Required Fields for Authorizing a Payment Using American Express and the Merchant Decryption Method](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-auth-merdecypt-amex-mandatory.md "")
* [Authorizing a Payment](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-services/samsungpay-auth-intro/samsungpay-auth-cybs-jcb-intro/samsungpay-auth-procedure.md "")
* [Example: Merchant Decryption with American Express Using the Simple Order API](/docs/cybs/en-us/samsung-pay/developer/ctv/so/samsungpay/samsungpay-auth-merdecrypt-ex-amex-so.md "")
  {#samsungpay-auth-merchant-amex-intro_ul_pcj_krp_npb}

Required Fields for Authorizing a Payment Using American Express and the `Cybersource` Decryption Method {#samsungpay-auth-cybsdecypt-amex-mandatory}
=====================================================================================================================================================

The following fields are required when submitting an authorization request using the `Cybersource` decryption method:

* ccAuthService_commerceIndicator-set this field to `aesk`.
* encryptedPayment_data
  * Set the field to the value that was returned from Samsung Pay in the *3ds.data* block as follows:
    * Retrieve the payment data from Samsung Pay in JSON Web Encryption (JWE) format.
    * Encode it in Base64.
    * Add the value to the encryptedPayment_data field.
* encryptedPayment_descriptor-set this field to` RklEPUNPTU1PTi5TQU1TVU5HLklOQVBQLlBBWU1FTlQ=`.
* paymentNetworkToken_transactionType-set this field to `1`.
* paymentSolution-set this field to `008`.

Related Information
-------------------

[Simple Order API Field Reference Guide](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/so/api-fields/api-fields-so-intro.md "")

Example: Merchant Decryption with American Express Using the Simple Order API {#samsungpay-auth-merdecrypt-ex-amex-so}
======================================================================================================================

Authorization Request

```
&lt;requestMessage xmlns="urn:schemas-cybersource-com:transaction-data-1.121"&gt;
    &lt;merchantID&gt;demomerchant&lt;/merchantID&gt;
    &lt;merchantReferenceCode&gt;demorefnum&lt;/merchantReferenceCode&gt;
    &lt;billTo&gt;
        &lt;firstName&gt;James&lt;/firstName&gt;
        &lt;lastName&gt;Smith&lt;/lastName&gt;
        &lt;street1&gt;1295 Charleston Road&lt;/street1&gt;
        &lt;city&gt;Test City&lt;/city&gt;
        &lt;state&gt;CA&lt;/state&gt;
        &lt;postalCode&gt;99999&lt;/postalCode&gt;
        &lt;country&gt;US&lt;/country&gt;
        &lt;email&gt;demo@example.com&lt;/email&gt;
    &lt;/billTo&gt;
    &lt;purchaseTotals&gt;
        &lt;currency&gt;USD&lt;/currency&gt;
        &lt;grandTotalAmount&gt;5.00&lt;/grandTotalAmount&gt;
    &lt;/purchaseTotals&gt;
    &lt;card&gt;
        &lt;accountNumber&gt;xxxx8224631xxxx&lt;/accountNumber&gt;
        &lt;expirationMonth&gt;12&lt;/expirationMonth&gt;
        &lt;expirationYear&gt;2020&lt;/expirationYear&gt;
    &lt;/card&gt;
    &lt;ccAuthService run="true"&gt;
        &lt;cavv&gt;ABCDEFabcdefABCDEFabcdef0987654321234567&lt;/cavv&gt;
        &lt;commerceIndicator&gt;aesk&lt;/commerceIndicator&gt;
        &lt;xid&gt;1234567890987654321ABCDEFabcdefABCDEF123&lt;/xid&gt;
    &lt;/ccAuthService&gt;
    &lt;paymentNetworkToken&gt;
        &lt;transactionType&gt;1&lt;/transactionType&gt;
    &lt;/paymentNetworkToken&gt;
    &lt;paymentSolution&gt;008&lt;/paymentSolution&gt;
&lt;/requestMessage&gt;    
```

Authorization Response

```
&lt;c:replyMessage&gt;
    &lt;c:merchantReferenceCode&gt;demorefnum&lt;/c:merchantReferenceCode&gt;
    &lt;c:requestID&gt;4465840340765000001541&lt;/c:requestID&gt;
    &lt;c:decision&gt;ACCEPT&lt;/c:decision&gt;
    &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
    &lt;c:purchaseTotals&gt;
        &lt;c:currency&gt;USD&lt;/c:currency&gt;
    &lt;/c:purchaseTotals&gt;
    &lt;c:ccAuthReply&gt;
        &lt;c:reasonCode&gt;100&lt;/c:reasonCode&gt;
        &lt;c:amount&gt;5.00&lt;/c:amount&gt;
        &lt;c:authorizationCode&gt;888888&lt;/c:authorizationCode&gt;
        &lt;c:avsCode&gt;V&lt;/c:avsCode&gt;
        &lt;c:avsCodeRaw&gt;I1&lt;/c:avsCodeRaw&gt;
        &lt;c:authorizedDateTime&gt;2015-11-03T20:53:54Z&lt;/c:authorizedDateTime&gt;
        &lt;c:processorResponse&gt;100&lt;/c:processorResponse&gt;
        &lt;c:reconciliationID&gt;11267051CGJSMQDC&lt;/c:reconciliationID&gt;
    &lt;/c:ccAuthReply&gt;
&lt;/c:replyMessage&gt;
```

