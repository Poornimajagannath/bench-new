Create Organizations {#boarding-reg-intro}
==========================================

You can create organizations using the API. Instructions for creating organizations are included in these sections:

* [Create a Merchant Organization](/docs/gateway/en-us/boarding/developer/all/rest/boarding/boarding-reg-intro/boarding-reg-create-merch-api.md "")
* [Add a Transacting Organization to a New Merchant Organization](/docs/gateway/en-us/boarding/developer/all/rest/boarding/boarding-reg-intro/boarding-reg-create-new-transacting-api.md "")
* [Add a Transacting Organization to an Existing Organization](/docs/gateway/en-us/boarding/developer/all/rest/boarding/boarding-reg-intro/boarding-reg-create-transacting-api.md "")

{#boarding-reg-intro_ul_rw5_3bq_hvb}  
For API field descriptions, see the [Boarding API Reference Guide](https://developer.example.com/api-reference-assets/index.md?stage=pilot#merchant-boarding_merchant-boarding_create-a-boarding-registration ""). You can test API requests using the reference guide's live console.  
Before beginning, review these topics:

* [Understanding Accounts and Organizations](/docs/gateway/en-us/boarding/developer/all/rest/boarding/boarding-intro-overview/boarding-intro-organizations.md "")
* [Understanding Organization IDs](/docs/gateway/en-us/boarding/developer/all/rest/boarding/boarding-intro-overview/boarding-intro-ids.md "")

If you use the API, keep in mind these considerations:

* The organization registration is done once using the `/registrations` endpoint. Modifications to existing organizations are done using the `/organizations` endpoint. Modifications to the product setups of an organization are done using the `/product-setups` endpoint. Examples of these endpoints are shown in the sections for those operations.
* The boardingFlow field has two values: `ENTERPRISE` and `SMB`. Enterprise creates one organization at a time. SMB (Small Business) creates a combination of one merchant organization and one transacting organization. Enterprise requires two requests, but defines an organization ID for the transacting organization instead of an automatically generated one. Enterprise is recommended. When you create a structural organization, you must set the value of boardingFlow to `ENTERPRISE`.
* The mode field is not currently supported.
* The configurable field must be set to `true` for merchant organizations and `false` for transacting and structural organizations.

