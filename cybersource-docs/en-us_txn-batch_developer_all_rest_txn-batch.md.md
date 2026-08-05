Transaction Batch API {#Id18ANJ0S405Z_Id18ANK0F0GX4}
====================================================

Using the Transaction Batch API, you can retrieve transaction batch statuses based on various criteria.

Creating a Request With a Client Application {#Id18ANJ0UK0HS_Id18ANK0FG0ZJ}
===========================================================================

The client uses a GET method to retrieve the batch statuses. To send the request, the header must contain an authorization token and the format for the file you want to download. For information and instructions on creating an authorization token, refer to [Getting Started with the REST API.](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md "")

Client Application Requirements {#Id18ANJ0UK0HS_Id18ANJ0WN0UI}
--------------------------------------------------------------

To connect to the server, your client application must support HTTPS connections. An HTTPS connection is similar to an HTTP connection, but it is encrypted by using Transport Layer Security (TLS). Your client application must support HTTP/1.1 and TLS 1.2 connections.  
HTTPS libraries are available for many programming languages, including Java, C/C++, Perl, and Visual Basic. You can implement a client in any language that allows you to use HTTPS to communicate with the report server.

> IMPORTANT
> Although you may be able to use a third-party client application to download ` Cybersource ` reports, ` Cybersource ` does not recommend or support third-party client applications or client libraries that may interfere with ` Cybersource ` applications.

Request Format {#Id18ANJ0UK0HS_Id18ANJ0YG0YK}
---------------------------------------------

To create a request, your client application must send an HTTP GET message to the server. The URL that you specify in your message indicates which function you are calling and the parameters of the call:
https://\&lt; `url_prefix`\&gt;/ `pts`/ `v1`/ `transaction-batches`/

Request Header {#Id18ANJ0UK0HS_id199UHD050HT}
---------------------------------------------

The default format for responses is JSON, but the Batch Detail Report can also return CSV or XML. You can set the response to return CSV or XML in the request header by setting the `Accept` value to either `application/xml` or `text/csv`.

Retrieve a List of Batch Files {#Id18ANJ200OPF_Id18ANJ90F0PN}
=============================================================

For a list of batch files, the request format is:

```keyword varname
GET https://&lt;url_prefix&gt;/pts/v1/transaction-batches&startTime={startTime}&endTime={endTime}
```

| Value                   | Description                                                                                                                                                                                                    | Required/Optional |
|:------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| \&lt; `url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com * **Test:** `apitest.cybersource.com` | Required          |
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

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#reporting "") .

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

Retrieve Batch Submission Detail Report {#id199UH0D10YK_id199UH07L0HS}
======================================================================

The Batch Submission Detail Report provides real-time detailed status information about the transactions that you previously uploaded in the `Business Center` or processed with the Offline Transaction File Submission service. The default format for responses is JSON, but the Batch Submission Detail Report can also return CSV or XML. You can set the response to return CSV or XML in the request header by setting the `Accept` value to either `application/xml` or `text/csv`.  
To request the report, your client application must send an HTTP GET message to the report server. Format the URL as follows:

```keyword varname
https://&lt;url_prefix&gt;/pts/v1/transaction-batch-details/{id}
```

| Value                   | Description                                                                                                                                                                                                    | Required/Optional |
|:------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| \&lt; `url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com * **Test:** `apitest.cybersource.com` | Required          |
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

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#reporting "") .
