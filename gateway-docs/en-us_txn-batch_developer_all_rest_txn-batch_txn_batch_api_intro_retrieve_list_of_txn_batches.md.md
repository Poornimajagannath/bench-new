Retrieve a List of Batch Files {#Id18ANJ200OPF_Id18ANJ90F0PN}
=============================================================

For a list of batch files, the request format is:

```keyword varname
GET https://&lt;url_prefix&gt;/pts/v1/transaction-batches&startTime={startTime}&endTime={endTime}
```

| Value                   | Description                                                                                                                                                                                                    | Required/Optional |
|:------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| \&lt; `url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Production:** `api.example.com` * **Production in India:** api.in.example.com * **Test:** `apitest.example.com` | Required          |
| \&lt; `startTime`\&gt;  | Report start date to search on in ISO 8601 format (yyyy-MM-dd'T'HH:mm:ss.SSSZ). **Example:** 2019-05-01T12:00:00-05:00                                                                                         | Required          |
| \&lt; `endTime`\&gt;    | Report end date to search on in ISO 8601 format (yyyy-MM-dd'T'HH:mm:ss.SSSZ). **Example:** 2019-08-30T12:00:00-05:00                                                                                           | Required          |
[Batch File Summary URL Values]

{#Id18ANJ200OPF_retrieve_list_of_users}

Responses {#Id18ANJ200OPF_id199UGG0C05Z}
----------------------------------------

This call can return one of the following HTTP status codes:

* 200: Ok.
* 400: Invalid request.
* 401: Not authorized.
* 403: Not authenticated.
* 404: Report not found or no transactions are available.
* 500: Bad Gateway.

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.example.com/api-reference-assets/index.md#reporting "") .
