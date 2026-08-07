Change an Organization's Status {#boarding-change-org-status}
=============================================================

You can change the status of organization by sending a GET request and including only the fields that you want to update in your request.

Endpoint {#boarding-change-org-status_d7e743}
---------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/oms/v1/organizations/{organizationId}`{#boarding-change-org-status_d7e750}  
**Test:** `GET ``https://apitest.cybersource.com``/oms/v1/organizations/{organizationId}`{#boarding-change-org-status_d7e760}  
Where *`{organizationId}`*is the ID that returned in the organization's boarding API response. Include only the fields you want to update.
