Retrieve Organization Details {#boarding-retrieve-an-organization}
==================================================================

You can send a GET request to retrieve the details of an organization. You can use the GET request without parameters to retrieve the full details or use the `fields` query parameter to limit the results. See [Using Query Parameters to Filter Results](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-manage-org-intro/boarding-retrieve-organizations/boarding-retrieve-organizations-query-parameters.md "") for more information about using the `fields` parameter.

Endpoint {#boarding-retrieve-an-organization_d7e743}
----------------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/oms/v1/organizations/{organizationId}`{#boarding-retrieve-an-organization_d7e750}  
**Test:** `GET ``https://apitest.cybersource.com``/oms/v1/organizations/{organizationId}`{#boarding-retrieve-an-organization_d7e760}  
Where *`{organizationId}`*is the ID that returned in the organization's boarding API response. Include only the fields you want to update.
