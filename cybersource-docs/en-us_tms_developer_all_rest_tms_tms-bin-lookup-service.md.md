BIN Lookup Service and `TMS` {#tms-bin-lookup-service}
======================================================

When some types of tokens are provisioned, `TMS` returns the BIN details that are provided by the BIN Lookup Service. This section describes how to retrieve the BIN information provided by the BIN Lookup Service for a PAN or network token.

> IMPORTANT
> You must be enabled for network tokenization to retrieve BIN details using ` TMS `.  
> `TMS` returns BIN data when you send a request to create or retrieve these token types:

* [Payment instrument tokens](/docs/cybs/en-us/tms/developer/all/rest/tms/tms-pi-tkn.md "")
* [Instrument identifier tokens](/docs/cybs/en-us/tms/developer/all/rest/tms/tms-ii-tkn.md "")  
  For more information about using the BIN Lookup Service, see the [*BIN Lookup Service Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/bin-lookup/developer/all/rest/bin-lookup/bin-lookup-about-guide.md "")

Endpoints
---------

Instrument Identifier Tokens
:
**Test:** `GET ``https://apitest.cybersource.com``/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}?retrieveBinDetails=true`{#tms-bin-lookup-service_restcust-test}
:
**Test:** `POST ``https://apitest.cybersource.com``/tms/v1/instrumentidentifiers?retrieveBinDetails=true`{#tms-bin-lookup-service_restcust-test-post}
:
**Production:** `GET ``https://api.cybersource.com``/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}?retrieveBinDetails=true`
:
**Production:** `POST ``https://api.cybersource.com``/tms/v1/instrumentidentifiers?retrieveBinDetails=true`{#tms-bin-lookup-service_restcust-prod-post}
:
**Production in India:** `GET ``https://api.in.cybersource.com``/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}?retrieveBinDetails=true`{#tms-bin-lookup-service_restcust-prod-india}
:
**Production in India:** `POST ``https://api.in.cybersource.com``/tms/v1/instrumentidentifiers?retrieveBinDetails=true`

Payment Instrument Tokens
:
**Test:** `GET ``https://apitest.cybersource.com``/tms/v1/paymentinstruments/{paymentInstrumentTokenId}?retrieveBinDetails=true`{#tms-bin-lookup-service_rest-pi-test}
:
**Test:** `POST ``https://apitest.cybersource.com``/tms/v1/paymentinstruments?retrieveBinDetails=true`{#tms-bin-lookup-service_rest-pi-test-post}
:
**Production:** `GET ``https://api.cybersource.com``/tms/v1/paymentinstruments/{paymentInstrumentTokenId}?retrieveBinDetails=true`{#tms-bin-lookup-service_rest-pi-prod}
:
**Production:** `POST ``https://api.cybersource.com``/tms/v1/paymentinstruments?retrieveBinDetails=true`{#tms-bin-lookup-service_rest-pi-prod-post}
:
**Production in India:** `GET ``https://api.in.cybersource.com``/tms/v1/paymentinstruments/{paymentInstrumentTokenId}?retrieveBinDetails=true`
:
**Production in India:** `POST ``https://api.in.cybersource.com``/tms/v1/paymentinstruments?retrieveBinDetails=true`  
*`{instrumentIdentifierTokenId}`* and *{paymentInstrumentTokenId}* are the token IDs that are returned in the id field when you created the token.
