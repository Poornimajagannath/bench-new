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
