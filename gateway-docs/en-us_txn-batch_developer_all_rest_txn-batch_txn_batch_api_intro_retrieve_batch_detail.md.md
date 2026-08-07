Retrieve Batch Submission Detail Report {#id199UH0D10YK_id199UH07L0HS}
======================================================================

The Batch Submission Detail Report provides real-time detailed status information about the transactions that you previously uploaded in the `Business Center` or processed with the Offline Transaction File Submission service. The default format for responses is JSON, but the Batch Submission Detail Report can also return CSV or XML. You can set the response to return CSV or XML in the request header by setting the `Accept` value to either `application/xml` or `text/csv`.  
To request the report, your client application must send an HTTP GET message to the report server. Format the URL as follows:

```keyword varname
https://&lt;url_prefix&gt;/pts/v1/transaction-batch-details/{id}
```

| Value                   | Description                                                                                                                                                                                                    | Required/Optional |
|:------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| \&lt; `url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Production:** `api.example.com` * **Production in India:** api.in.example.com * **Test:** `apitest.example.com` | Required          |
| \&lt; `id`\&gt;         | Unique ID assigned to a batch upload file.                                                                                                                                                                     | Required          |
[Transaction Batch File Definition URL Values]

{#id199UH0D10YK_download_secure_file}

Responses {#id199UH0D10YK_id199UH0809UI}
----------------------------------------

This call can return one of the following HTTP status codes:

* 200: Ok.
* 400: Invalid request.
* 401: Not authorized.
* 403: Not authenticated.
* 404: Report not found or no transactions are available.
* 500: Bad Gateway.

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.example.com/api-reference-assets/index.md#reporting "") .
