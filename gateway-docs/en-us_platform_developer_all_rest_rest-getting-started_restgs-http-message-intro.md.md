Deprecating September 2026: HTTP Signature Messaging

Set Up an HTTP Signature Message ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-deprecating-100x20.svg/jcr:content/renditions/original) {#restgs-http-message-intro}
==================================================================================================================================================================================================================

To set up HTTP signature messaging, you must complete the tasks described in this section.

> WARNING  
> By **September 2026** , all merchants using HTTP signature messaging must migrate to JSON Web Token (JWT) messaging in order to support message-level encryption (MLE). You risk transaction failures if you do not implement this update. If you are setting up your system to be REST-compliant for the first time, ` Payment Gateway ` recommends using JWT messaging.  
> To update your system to support JWT messaging, use one of these methods:
>
> * [JWT messaging using a shared secret key pair](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro.md "")

* [JWT messaging using a P12 certificate](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro.md "")

#### Figure:

Set Up HTTP Signature Messaging ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-http-all-750x175.svg/jcr:content/renditions/original)

1. Sign up for a test account. See [Sign Up for a Sandbox Account](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-register.md "").
2. Create a shared secret key. See [Create a Shared Secret Key Pair](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro/restgs-security-key-pair-intro.md "").
3. Construct a message using HTTP signature security. See [Construct Messages Using HTTP Signature Security](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro/restgs-http-message-conf-intro.md "").
4. Test your REST transaction messages. See [Test Your Setup](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro/restgs-test.md "").
5. Go live by transitioning your sandbox account into a production account. [Going Live](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-go-live-intro.md "").

