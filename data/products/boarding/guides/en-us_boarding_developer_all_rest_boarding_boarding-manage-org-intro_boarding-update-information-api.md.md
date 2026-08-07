Update an Organization's Information {#boarding-update-information-api}
=======================================================================

Use these instructions to update an organization's information using the API.  
Although organizationId is the only required field, any other field that contains organization information can be added to the API request to update the information in that field.

Endpoint {#boarding-update-information-api_d7e743}
--------------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/oms/v1/organizations/{organizationId}`{#boarding-update-information-api_d7e750}  
**Test:** `GET ``https://apitest.cybersource.com``/oms/v1/organizations/{organizationId}`{#boarding-update-information-api_d7e760}  
Where *`{organizationId}`*is the ID that returned in the organization's boarding API response. Include only the fields you want to update.
