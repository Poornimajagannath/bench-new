SCMP Mandate Compliance for HTTPS Upgrade Migration Guide {#so-conversion-about-guide}
======================================================================================

Audience and Purpose
--------------------

This guide is written for merchants who need to upgrade their SCMP API payment system to send Simple Order API messages to and receive them from `Cybersource`.

Convention
----------

This statement appears in this document:

> An *Important* statement contains information essential to successfully completing a task or learning a concept.

Customer Support
----------------

For support information about any service, visit the Support Center:  
<http://support.example.com>

Recent Revisions to This Document {#so-conversion-recent-revisions}
===================================================================

25.04.01
--------

Retitled guide from *SCMP-to-Simple Order Conversion Migration Guide* to *SCMP Mandate Compliance for HTTPS Upgrade Migration Guide*.  
Added additional details about the security updates and requirements in the introduction. See [Introduction to SCMP Mandate Compliance for HTTPS Upgrade](/docs/cybs/en-us/so-p12/migration/all/so/so-conversion/so-conversion-intro.md "").  
Added new section explaining how to upgrade the `Cybersource` Java SCMP Client SDK. See [Java SCMP Client SDK Upgrade](/docs/cybs/en-us/so-p12/migration/all/so/so-conversion/so-conversion-java-sdk.md "").

25.03.01
--------

Initial release.

Introduction to SCMP Mandate Compliance for HTTPS Upgrade {#so-conversion-intro}
================================================================================

The HTTP SCMP endpoints will be decommissioned on April 30th, 2025, as a part of a Cybersource security update, and only these SCMP HTTPS endpoints will be valid:

* **Test:** `ics2test.ic3.com`
* **Production:** `ics2.ic3.com`

This migration guide explains how to upgrade your SCMP payment system in order to remain compliant with the security update and avoid service disruptions.

Upgrade Methods
---------------

Depending on the library you integrated your payment system with, you can complete this upgrade using one of these methods:

* **Java SCMP Client SDK:** This method only requires you to update the endpoint configuration in your Java SCMP Client SDK to HTTPS. Only the Java SDK version 5.4.0 is valid for this upgrade.
* **Conversion kit for Simple Order API:** This method uses a conversion kit to upgrade your SCMP payment system to a Simple Order payment system. It is available for C++ and Java programming environments and any application developed using the .NET framework. If your payment system utilizes a language that we do not have a sample reference for, Cybersource recommends upgrading using the SOAP toolkit or the REST API. For more information about upgrading using the SOAP toolkit, see the [*SOAP Toolkits for Web Services Developer Guide*](https://developer.cybersource.com/library/documentation/dev_guides/SOAP_Toolkits/SOAP_toolkits.pdf "") and the [Cybersource SOAP Toolkit](https://github.com/CyberSource/cybersource-soap-toolkit "") in GitHub.
* **REST API:** If you prefer, you can upgrade your payment system to the REST API instead. For more information about how to upgrade to REST, see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md ""). Cybersource recommends that you upgrade using this method if possible.

Additional Support
------------------

If you have additional questions, please contact your `Cybersource` account representative for more information, or submit a support ticket here:  
<https://support.example.com/>

C++ Payment System Upgrade {#so-conversion-cplusplus}
=====================================================

This section describes how to transition your SCMP payment system to send and receive HTTPS Simple Order API transmissions using the C++ programming language. Upgrading your payment system to Simple Order requires you to download an API key from the `Business Center`.

**Enable SCMP-to-Simple Order Conversion** {#so-conversion-cplusplus_converting-intro}
--------------------------------------------------------------------------------------

The conversion kit method enables users with an SCMP payment system to maintain their SCMP system while using the Simple Order endpoint. When you send an SCMP request to `Cybersource`, the request is converted into a Simple Order request and then sent to the corresponding Simple Order endpoint. When `Cybersource` returns a Simple Order response, the response is converted into SCMP for your system to process it. This image demonstrates the conversion process:

#### Figure:

SCMP-to-Simple Order Conversion  
![](/content/dam/new-documentation/documentation/en-us/topics/platform/soap/conversion/images/scmp-to-so.svg/jcr:content/renditions/original)

Setting Up SCMP-to-Simple Order Conversion
------------------------------------------

Follow these steps to set up SCMP-to-Simple Order conversion.

1. Add the SCMP conversion kit to your payment system. Retrieve the conversion kit files from the *SCMPToNVPTest* folder in GitHub:  
   <https://github.com/CyberSource/cybersource-sdk-cplusplus/tree/master/SCMPToNVPTest>

2. Add the *cybs.ini* file to your application. Retrieve the *cybs.ini* file from the *resources* folder in GitHub:  
   <https://github.com/CyberSource/cybersource-sdk-cplusplus/blob/master/resources/cybs.ini>

3. Update these parameter values in your *cybs.ini* file:

   * merchantID: Set to your production merchant ID used for commerce.
   * keysDirectory: Set to the file path that leads to your P12 certificate.
   * serverURL: Set to the `Cybersource` Simple Order endpoint.
   * keyFilename: Set to the file name of your .p12 file.
   * password: Set to your P12 certificate password.
   * sslCertFile: Set to the file path and name of your .p12 file.

   ```
   merchantID=your-merchant-id
   keysDirectory=c:/keys
   serverURL=https://ics2wstest.ic3.com/commerce/1.x/transactionProcessor/
   keyFilename=your-merchant-id.p12
   password=test-password
   sslCertFile=c:/keys/ics2wstest.ic3.crt
   ```

   You can set other files at your discretion. See the comments in the *README.md* file to determine which values to change: <https://github.com/CyberSource/cybersource-sdk-cplusplus/blob/master/SCMPToNVPTest/README.md>

4. After your SCMP payment software creates a request, replace your existing request to SCMP with a request to the `processRequest` method from the class in the *ics_util.cpp* file. Then, pass your SCMP request as a parameter in the `processRequest` method.

   ```
   ics_msg* scmpResponse = processRequest(scmpRequest);  // &lt;-- User inputs their SCMP request here
   ```

   If you do not have the *ics_util.cpp* file, you can retrieve it from the *SCMPToNVPTest* folder in GitHub:  
   <https://github.com/CyberSource/cybersource-sdk-cplusplus/blob/master/SCMPToNVPTest/ics_util.cpp>

Result {#so-conversion-cplusplus_result}
----------------------------------------

When you send an API request to `Cybersource`, the `processRequest` method converts your SCMP request into a Simple Order request. It then sends the converted request to the correct Simple Order endpoint. When you receive a Simple Order response from `Cybersource`, the response is converted into SCMP for your payment system to process.

Java Payment System Upgrade {#so-conversion-java}
=================================================

Follow these instructions to transition your SCMP payment system to send and receive HTTPS Simple Order API transmissions using the Java programming language. Upgrading your payment system to Simple Order requires you to download an API key from the `Business Center`.  
If your system uses the `Cybersource` Java SDK to send API messages, there is an alternative upgrade method that only requires you to have to update the SCMP endpoint configuration in the SDK. For more information, see [Java SCMP Client SDK Upgrade](/docs/cybs/en-us/so-p12/migration/all/so/so-conversion/so-conversion-java-sdk.md "").

> You must use Java 8 or later to implement this change.

**Enable SCMP-to-Simple Order Conversion**
------------------------------------------

The conversion kit method enables users with an SCMP payment system to maintain their SCMP system while using the Simple Order endpoint. When you send an SCMP request to `Cybersource`, the request is converted into a Simple Order request and then sent to the corresponding Simple Order endpoint. When `Cybersource` returns a Simple Order response, the response is converted into SCMP for your system to process it. This image demonstrates the conversion process:

#### Figure:

SCMP-to-Simple Order Conversion  
![](/content/dam/new-documentation/documentation/en-us/topics/platform/soap/conversion/images/scmp-to-so.svg/jcr:content/renditions/original)

Setting Up SCMP-to-Simple Order Conversion
------------------------------------------

Follow these steps to set up SCMP-to-Simple Order conversion.

1. Add the SCMP conversion kit to your payment system. Retrieve the conversion kit files from the *SCMPSampleClient* folder in GitHub:  
   <https://github.com/CyberSource/cybersource-sdk-java/tree/master/samples/scmp/SCMPSampleClient>

2. Add the *cybs.properties* file to your application. Retrieve the *cybs.properties* file from the *samples/scmp/SCMPSampleClient* folder in GitHub:  
   <https://github.com/CyberSource/cybersource-sdk-java/blob/master/samples/scmp/SCMPSampleClient/cybs.properties>

3. Update these parameter values in your *cybs.properties* file:

   * merchantID: Set to your production merchant ID used for commerce.
   * keysDirectory: Set to the file path that leads to your P12 certificate.
   * keyAlias: Set to your merchant ID (MID) name.
   * keyPassword: Set to your P12 certificate password.
   * sendToProduction: Set to one of these possible values to determine which environment your API request message is sent to:
     * `true`: production environment.
     * `false`: CAS environment.

   ```
   merchantID=test_mid
   keysDirectory=/user/oliver/keys/
   keyAlias=test_mid
   keyPassword=test_password
   sendToProduction=true
   ```

   You can set other files at your discretion. See the comments in the *README.md* file to determine which values to change: <https://github.com/CyberSource/cybersource-sdk-java/blob/master/README.md>

4. After your SCMP payment software creates a request, replace your existing request to SCMP with a request to the `processRequest` method from the class in the *Util.java* file. Then pass your SCMP request as a parameter in the `processRequest` method.

   ```
   ICSReply scmpReply = Util.processRequest (scmpRequest, cyberProperties);
   ```

   If you do not have the *Util.java* file, it is available in the *samples/scmp/SCMPSampleClient/**src*** folder in GitHub:  
   <https://github.com/CyberSource/cybersource-sdk-java/blob/master/samples/scmp/SCMPSampleClient/src/Util.java>

Result
------

When you send an API request to `Cybersource`, the `processRequest` method converts your SCMP request into a Simple Order request. It then sends the converted request to the correct Simple Order endpoint. When you receive a Simple Order response from `Cybersource`, the response is converted into SCMP for your payment system to process.

Java SCMP Client SDK Upgrade {#so-conversion-java-sdk}
======================================================

Follow these steps to upgrade the endpoint configuration in your Java SCMP Client SDK.

> Only the Java SCMP Client SDK version 5.4.0 is valid for this upgrade.

1. Open your *ICSClient.props* file using a text editor application. This file is located in the *properties* folder in your Java SDK.

2. Change the `serverURL` property value to one of these valid HTTPS endpoints that corresponds to your environment:

   Test Endpoint
   :

       ```
       serverURL=https://ics2test.ic3.com:443/
       ```

   Production Endpoint
   :

       ```
       serverURL=https://ics2.ic3.com:443/
       ```

3. Add the useJdkUrlConnection property and set its value to `true`.

   ```
   useJdkUrlConnection=true
   ```
4. (Optional) Run the authorization sample in the *ICSAuthTest.java* file to test and confirm that your HTTPS connection is successful. The file is in the *samples* folder.  
   In the sample authorization, set the field value in the customer_cc_expyr field to a future four digit year.

Troubleshooting Using Certificates
----------------------------------

If you receive an error message when sending an API request to the HTTPS endpoints, you may need to add certificates to your payment system. Follow these steps to add the Certificate Authority (CA) root certificate and intermediate certificate to your system.

1. Download the certificates from the attachments section in this support article:  
   <https://support.example.com/knowledgebase/knowledgearticle/?code=KA-05544>

2. Import the certificates to your Java truststore.

3. If you need to enable your system to trust the certificates, add these two properties and values to your *ICSClient.props* file to override the default Java truststore.

   ```
   ssl.trustStore={path_to_your_truststore}/keys/truststore.jks
   ssl.trustStorePassword={your_password}
   ```

.NET Payment System Upgrade {#so-conversion-other}
==================================================

This section describes how to transition your SCMP payment system to send and receive HTTPS Simple Order API transmissions. Upgrading your payment system to Simple Order requires you to download an API key from the `Business Center`.

**Enable SCMP-to-Simple Order Conversion**
------------------------------------------

The conversion kit method enables users with an SCMP payment system to maintain their SCMP system while using the Simple Order endpoint. When you send an SCMP request to `Cybersource`, the request is converted into a Simple Order request and then sent to the corresponding Simple Order endpoint. When `Cybersource` returns a Simple Order response, the response is converted into SCMP for your system to process it. This image demonstrates the conversion process:

#### Figure:

SCMP-to-Simple Order Conversion  
![](/content/dam/new-documentation/documentation/en-us/topics/platform/soap/conversion/images/scmp-to-so.svg/jcr:content/renditions/original)

Setting Up SCMP-to-Simple Order Conversion
------------------------------------------

Follow these steps to set up SCMP-to-Simple Order conversion.
1. Add the SCMP conversion kit to your payment system. Retrieve the conversion kit files from the *scmp* folder in GitHub:  
   <https://github.com/CyberSource/cybersource-sdk-dotnet/tree/master/CyberSourceSamples/src/scmp>

2. Update these values in your *app.config* file. Retrieve the *app.config* file from the *scmp* folder in GitHub:  
   <https://github.com/CyberSource/cybersource-sdk-dotnet/blob/master/CyberSourceSamples/src/scmp/app.config>

   * merchantID: Set to your production merchant ID used for commerce.
   * keysDirectory: Set to the file path that leads to your P12 certificate.
   * keyAlias: Set to your merchant ID (MID) name.
   * password: Set to your P12 certificate password.

   ```
   &lt;add key="cybs.merchantID" value="" /&gt;
   &lt;add key="cybs.keysDirectory" value="" /&gt;
   &lt;add key="cybs.keysAlias" value="" /&gt;
   &lt;add key="cybs.Password" value="" /&gt;
   ```

   You can set other files at your discretion. See the comments in the *README.md* file to determine which values to change:  
   <https://github.com/CyberSource/cybersource-sdk-dotnet/blob/master/README.md>

3. After your SCMP payment software creates a request message, run the *processRequest* method found in the *Util.cs* file against that request.

Result
------

When you send an API request to `Cybersource`, the `processRequest` method converts your SCMP request into a Simple Order request. It then sends the converted request to the correct Simple Order endpoint. When you receive a Simple Order response from `Cybersource`, the response is converted into SCMP for your payment system to process.
