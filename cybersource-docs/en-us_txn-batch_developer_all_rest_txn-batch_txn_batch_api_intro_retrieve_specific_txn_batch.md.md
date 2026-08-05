Retrieve a Specific Transaction Batch File {#Id18ANK0H037U_Id18ANK0J80BF}
=========================================================================

To retrieve a specific transaction batch, the request format is:

```keyword varname
GET https://&lt;url_prefix&gt;/pts/v1/transaction-batches/{id}
```

| Value                   | Description                                                                                                                                                                                                    | Required/Optional |
|:------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| \&lt; `url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com * **Test:** `apitest.cybersource.com` | Required          |
| \&lt; `id`\&gt;         | Unique ID assigned to a batch upload file.                                                                                                                                                                     | Required          |
[Transaction Batch File Definition URL Values]

{#Id18ANK0H037U_download_secure_file}

Responses {#Id18ANK0H037U_id199UGK008Y4}
----------------------------------------

This call can return one of the following HTTP status codes:

* 200: Ok.
* 400: Invalid request.
* 401: Not authorized.
* 403: Not authenticated.
* 404: Report not found or no transactions are available.
* 500: Bad Gateway.

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#reporting "") .
