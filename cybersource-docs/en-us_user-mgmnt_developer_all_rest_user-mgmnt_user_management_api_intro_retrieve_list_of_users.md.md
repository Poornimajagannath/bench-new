REST API

Retrieve a List of Users {#Id18ANJ200OPF_Id18ANJ90F0PN}
=======================================================

You can retrieve a list of Business Center users within your organization and view their account information.  
See [Create an API Request](/docs/cybs/en-us/user-mgmnt/developer/all/rest/user-mgmnt/user_management_api_intro/create_request_with_client_application.md "") for general information on how to call this API.  
Use this resource to retrieve a list of [Business Center](https://ebc2.cybersource.com/ebc2/app/Home "") users:  
**Sandbox:** `POST https://apitest.cybersource.com/ums/v1/users/search`  
**Live:** `POST https://api.cybersource.com/ums/v1/users/search`  
**Live in India:** `POST https://api.in.cybersource.com/ums/v1/users/search`  
For a detailed API reference, see the [Search User Information](/api-reference-assets/index.md#user-management_usermanagementsearch_search-user-information "") section of the interactive API Reference.

Request
-------

To retrieve a list of [Business Center](https://ebc2.cybersource.com/ebc2/app/Home "") users who are in your organization, you must pass one of the following fields or field combinations:

* `organizationId`
* `userName`
* `userName` with `organizationId`
* `roleId` with `organizationId`
* `permissionId` with `organizationId`

{#Id18ANJ200OPF_ul_1}

|      Field       |                                                                                        Description                                                                                         |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `organizationId` | *(Conditional)* The organization ID of the user(s). This can be the merchant ID, account ID, or reseller ID. You can pass this field only or pass it with one of the other request fields. |
| `userName`       | (*Conditional)* The specific user name of the user you want to view. You can pass this field only or pass it with the `organizationId` field.                                              |
| `permissionId`   | *(Conditional)* Pass this field with the `organizationId` field to filter your search results to a specific permission.                                                                    |
| `roleId`         | *(Conditional)* Pass this field with the `organizationId` field to filter your search results to a specific user role.                                                                     |
[Request Fields]

{#Id18ANJ200OPF_retrieve_list_of_users}  
**Request example:**  
The following request searches for all admin users within the Global Art Supplies, Inc. organization.

```
{
  "organizationId": "GlobalArtSupplies",
  "roleId": "Admin"
}       
```

Response
--------

A successful response returns a `users` array with one or more `user` objects.  
Each [user](../../../../../../../api-reference-assets/index.md#user-management_usermanagementsearch_search-user-information_responsefielddescription_200_users_accountInformation "") object consists of the following objects:

* `accountInformation` - Includes the fields: `userName`, `roleId`, `permissions`, `status`, `createdTime`, `lastAccessTime`, `languagePreference`, and `timezone`.
  * The user account `status` field can have one of the following values: `active`, `inactive`, `locked`, `disabled`, `forgotpassword`, and `deleted`.
    {#Id18ANJ200OPF_ul_3}
* `organizationInformation` - Includes the field: `organizationId`.
* `contactInformation` - Includes the fields: `email`, `phoneNumber`, `firstName`, and `lastName`.
* `customFields` created by your organization

{#Id18ANJ200OPF_ul_2}  
**Response example:**  
The following response lists admin users within the Global Art Supplies, Inc. organization.

```
{
  "users": [
    {
      "accountInformation": {
        "userName": "minajon",
        "roleId": "Admin",
        "permissions": [
          "ReportViewPermission",
          "ReportGeneratePermission"
        ],
        "status": "active",
        "createdTime": "2020-06-14T19:45:52.093Z",
        "lastAccessTime": "2021-03-14T19:45:52.093Z",
        "languagePreference": "en-US",
        "timezone": "America/Los_Angeles"
      },
      "organizationInformation": {
        "organizationId": "GlobalArtSupplies"
      },
      "contactInformation": {
        "email": "mina@globalartsupplies.world",
        "phoneNumber": "3105551212",
        "firstName": "Mina",
        "lastName": "Jon"
      },
      "customFields": {
        "employeeId": "007",
        "jobTitle": "Sales Director",
        "department": "Sales"
      }
    }
  ]
}
        
```

