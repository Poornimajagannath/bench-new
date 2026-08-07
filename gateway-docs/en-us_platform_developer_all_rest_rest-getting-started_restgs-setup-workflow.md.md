How to Set Up REST {#restgs-setup-workflow}
===========================================

This overview lists the tasks you must complete in order to set up your Payment Gateway account for sending and receiving REST API messages using JSON Web Token (JWT) messaging.  
You can choose from these set up methods:

* JWT messaging using a *P12 certificate*.
* JWT messaging using a *shared secret key pair*.
* JWT messaging using the *REST Client SDK*.
  {#restgs-setup-workflow_ul_gwz_r3x_s3c}

#### Figure:

Set Up Your Payment Gateway Account ![If you are using a custom integration, follow these steps. Step 1: Create a
test account. Step 2: Choose and create your security type using a P12
certificate or shared secret key pair. Step 3: Construct a message with JSON
Web Tokens. Step 4: Enable Message-Level Encryption (MLE). Step 5: Test your
setup. Step 6: Go live. If you are using an SDK integration, follow these
steps. Step 1: Create a test account. Step 2: Choose and create your
security type using a P12 certificate or shared secret key pair. Step 3:
Import an SDK that constructs messages using JSON Web Tokens and
Message-Level Encryption. Step 5: Test your setup. Step 6: Go live.](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-overview-750x635.svg/jcr:content/renditions/original)  
To set up JSON web token messaging using *P12 certificates* , see [Set Up a JSON Web Token Message Using P12 Certificates](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro.md "").  
To set up JSON web token messaging using *shared secret key pairs* , see [Set Up a JSON Web Token Message Using Shared Secret Key Pairs](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro.md "").  
To set up JSON web token messaging using the *REST Client SDK* , see [Set Up a JSON Web Token Message Using the REST SDK](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-sdk-intro.md "").

HTTP Signature Security ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-deprecating-100x20.svg/jcr:content/renditions/original) {#restgs-setup-workflow_section_wkh_3kx_s3c}
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You also have the option to set up your Payment Gateway account for sending and receiving messages using HTTP signature security.  
![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-http-deprecating-550x120.svg/jcr:content/renditions/original)

> WARNING  
> By **September 2026** , all merchants using HTTP signature messaging must migrate to JSON Web Token (JWT) messaging in order to support message-level encryption (MLE). You risk transaction failures if you do not implement this update. If you are setting up your system to be REST-compliant for the first time, ` Payment Gateway ` recommends using JWT messaging.  
> To set up HTTP signature messaging, see [Set Up an HTTP Signature Message](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro.md "").

