Recent Revisions to This Document {#reporting-changes}
======================================================

24.04
-----

This revision contains only editorial changes and no technical updates.

24.03
-----

:
Removed references to deprecated guide.
:
Added new report fields for `Token Management Service`. See [Token Fields](/docs/cybs/en-us/reporting/developer/all/rest/reporting/reporting_fields/token.md "").

24.02
-----

:
This revision contains only editorial changes and no technical updates.

24.01
-----

Network Token Life-Cycle Management
:
Added Network Token Life-Cycle Management fields. See [Network Token Life-Cycle Management Fields](/docs/cybs/en-us/reporting/developer/all/rest/reporting/reporting_fields/lcm-net-tkn-api-fields.md "").

Time Zones
:
Added Supported Time Zones. See [Supported Time Zones](/docs/cybs/en-us/reporting/developer/all/rest/reporting/time-zones.md "").

23.01
-----

:
Updated the URL format in [Downloading On-Demand Conversion Detail Report](/docs/cybs/en-us/reporting/developer/all/rest/reporting/reporting_api/reporting-ondemand-detail-download.md "").

VISA Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Visa Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Visa/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER VISA NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE VISA PLATFORM CONNECT ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER VISA NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT VISA PLATFORM CONNECT ACQUIRER.

Reporting API {#reporting_api}
==============================

Using the Reporting API, you can:

* View report attributes before creating a subscription
* View report subscriptions
* Create, edit, and delete report subscriptions
* Download reports
* Create one-time reports

For detailed information about reports or how to migrate to REST from our servlets, see these guides:

* [Reporting User Guide](https://apps.cybersource.com/library/documentation/dev_guides/reporting_and_reconciliation/Reporting_User/html "")

Creating Requests With a Client Application {#reporting-client-apps-create-request}
===================================================================================

The client uses GET, POST, and PUT methods to send requests to the server. To send the request, you must include an authorization token in the header and specify the format for the report that you want to download.

Request Format
--------------

To create a request, you must send an HTTP message to the report server with your client application. The URL and method that you specify in your message indicates which function you are requesting and the parameters of the request. Partners can specify the organization ID, which enables them to create requests that return data for a specific merchant. For example, to download a report, you would format the URL as follows:

```
https://&lt;url_prefix&gt;/reporting/v3/report-downloads?organizationId={organizationId}&download=true&reportDate={date}&reportName={reportName}
```

If the organizationId field value is `SampleMerchant`, you would use the following URL to download the report from February 20, 2018, titled SampleDailyReport from the production system:

```
https://&lt;url_prefix&gt;/reporting/v3/report-downloads?organizationId=SampleMerchant&reportDate=20180220&reportName=SampleDailyReport
```

> IMPORTANT
> Pass the organizationId field in the request only if you are a partner creating a request to retrieve data for a specific merchant. Otherwise, the organizationId field is passed in your authentication method and not required in the request.

Client Application Requirements
-------------------------------

To connect to the report server, your client application must support HTTPS encrypted by using Transport Layer Security (TLS). Your client application must support HTTP/1.1 and TLS 1.2 connections.  
HTTPS libraries are available for many programming languages, including Java, C/C++, Perl, and Visual Basic. You can implement a client in any language that allows you to use HTTPS to communicate with the report server.

> IMPORTANT Although you may be able to use a third-party client application to download the reports, we do not recommend or support third-party client applications or client libraries that may interfere with our applications.

Request Header
--------------

The default format for responses is JSON, but some reports can also return CSV or XML. You can set the response to return CSV or XML in the request header by setting the `Accept` value to either `application/xml` or `text/csv`. The report format can be set for the following reports:

* Conversion Detail
* Purchase and Refund Detail

Viewing Report Definitions {#reporting-definitions-view}
========================================================

You can view a list of supported reports and their attributes before subscribing to them. You can also view the attributes of an individual report type.  
For a summary of all reports, the request format is:

```
GET https://&lt;url_prefix&gt;/reporting/v3/report-definitions?organizationId={organizationId}
```

| Value                   | Description                                                                                                                                                                                                | Required/ Optional |
|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| \&lt; `url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Production**: api.cybersource.com * **Production in India**: api.in.cybersource.com * **Test**: apitest.cybersource.com | Required           |
| `{organizationId}`      | The organization ID under which the report is subscribed. This can be the merchant ID, account ID, or reseller ID.                                                                                         | Optional           |
[Summary Report Definition URL Values]

For a summary of a single report type, the request format is:

```keyword varname
GET https://&lt;url_prefix&gt;/reporting/v3/report-definitions/{reportDefinitionName}?organizationId={organizationId}&download=true
```

| Value                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Required/ Optional |
|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| `&lt; url_prefix&gt;`    | Name of the server from which to download the report. Use one of these values: * **Test:** `apitest.cybersource.com` * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com {#reporting-definitions-view_ul_u1j_gxk_byb}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Required           |
| `{reportDefinitionName}` | Name of the report type you want to review. The options are: * `TransactionRequestClass`: Transaction Request Report * `PaymentBatchDetailClass`: Payment Batch Detail Report * `ExceptionDetailClass`: Transaction Exception Detail Report * `ProcessorSettlementDetailClass`: Processor Settlement Detail Report * `ProcessorEventsDetailClass`: Processor Events Detail Report * `FundingDetailClass`: Funding Detail Report * `AgingDetailClass`: Aging Detail Report * `ChargebackAndRetrievalDetailClass`: Chargeback And Retrieval Detail Report * `DepositDetailClass`: Deposit Detail Report * `FeeDetailClass`: Fee Detail Report * `InvoiceSummaryClass`: Invoice Summary Report * `PayerAuthDetailClass`: Payer Authentication Detail Report * `ConversionDetailClass`: Conversion Detail Report * `SubscriptionDetailClass`: Subscription Detail Report * `JPTransactionDetailClass`: JP Transaction Detail Report * `ServiceFeeDetailClass`: Service Fee Detail Report * `GatewayTransactionRequestClass`: Gateway Transaction Request Report * `DecisionManagerEventDetailClass`: `Decision Manager` Event Detail Report * `RecurringBillingDetailClass`: Recurring Billing Details Report | Required           |
| `{organizationId}`       | The organization ID under which the report is subscribed. This can be the merchant ID, account ID, or reseller ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Optional           |
[Single Report Definition URL Values]

{#reporting-definitions-view_table1}

Responses
---------

This call can return one of the following HTTP status codes:

* 200: Ok.
* 400: Invalid request.
* 404: Report not found.

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#reporting "") .

Managing Report Subscriptions {#reporting-subscriptions-manage}
===============================================================

The API enables you to view the details of a single report subscription and a list of all report subscriptions. You can also create, edit, and delete report subscriptions.

Viewing Report Subscriptions {#reporting-subscriptions-view}
============================================================

For a summary of all report subscriptions, the request format is:

```keyword varname
GET https://&lt;url_prefix&gt;/reporting/v3/report-subscriptions
```

| Value                  | Description                                                                                                                                                                                                    |
|:-----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \&lt;`url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Test:** `apitest.cybersource.com` * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com |
[Summary Report Subscriptions URL Values]

For a summary of a single report subscription, the request format is:

```keyword varname
GET https://&lt;url_prefix&gt;/reporting/v3/report-subscriptions/{reportName}
```

| Value                  | Description                                                                                                                                                                                                    | Required/ Optional |
|:-----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| \&lt;`url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Test:** `apitest.cybersource.com` * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com | Required           |
| `{reportName}`         | Unique name of the report subscription you want to review.                                                                                                                                                     | Required           |
[Single Report Subscription URL Values]

Responses
---------

This call can return one of the following HTTP status codes:

* 200: Ok.
* 400: Invalid request.
* 404: Report not found.

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#reporting "") .

Creating and Updating Report Subscriptions {#reporting-subscriptions-create-update}
===================================================================================

To create or update a report subscription, your client application must send an HTTP PUT request to the report server. The request body contains the details for creating the subscription, such as the report type, the start time, and the frequency. The format of the URL is as follows:

```keyword varname
PUT https://&lt;url_prefix&gt;/reporting/v3/report-subscriptions
```

For example, if you wanted to create a report titled Daily Transactions, the request would be:

```
PUT https://&lt;url_prefix&gt;/reporting/v3/report-subscriptions
```

The request body would be:

```
{
                "organizationId": "myorg",
                "reportName": "DailyTransactions",
                "reportDefinitionName": "TransactionDetailClass",
                "reportFields": [
                    "Request.RequestID",
                    "Request.TransactionDate",
                    "Request.MerchantID",
                    "BillTo.FirstName",
                    "BillTo.LastName",
                    "BillTo.City",],
                "startTime": "1100",
                "reportMimeType": "application/xml,
                "reportFrequency": "DAILY",
                "timezone": "GMT",
                "startTime": "0900",
                "startDay": "1"
                }
            
```

| Value                | Description                                                                                                                                                                                                    |
|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `&lt;url_prefix&gt;` | Name of the server from which to download the report. Use one of these values: * **Test:** `apitest.cybersource.com` * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com |
[Create/Update Report Subscription URL Values]

{#reporting-subscriptions-create-update_table3}  
Not all configuration options below are available for all reports.

| Value                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Required/ Optional |
|:--------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| **`organizationId`**                        | The organization ID under which the report is subscribed. This can be the merchant ID, account ID, or reseller ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Optional           |
| **`reportDefinitionName`**                  | Name of the report type you want to review. The options are: * `TransactionRequestClass`: Transaction Request Report * `PaymentBatchDetailClass`: Payment Batch Detail Report * `ExceptionDetailClass`: Transaction Exception Detail Report * `ProcessorSettlementDetailClass`: Processor Settlement Detail Report * `ProcessorEventsDetailClass`: Processor Events Detail Report * `FundingDetailClass`: Funding Detail Report * `AgingDetailClass`: Aging Detail Report * `ChargebackAndRetrievalDetailClass`: Chargeback And Retrieval Detail Report * `DepositDetailClass`: Deposit Detail Report * `FeeDetailClass`: Fee Detail Report * `InvoiceSummaryClass`: Invoice Summary Report * `PayerAuthDetailClass`: Payer Authentication Detail Report * `ConversionDetailClass`: Conversion Detail Report * `SubscriptionDetailClass`: Subscription Detail Report * `JPTransactionDetailClass`: JP Transaction Detail Report * `ServiceFeeDetailClass`: Service Fee Detail Report * `GatewayTransactionRequestClass`: Gateway Transaction Request Report * `DecisionManagerEventDetailClass`: `Decision Manager` Event Detail Report * `RecurringBillingDetailClass`: Recurring Billing Details Report | Required           |
| **`reportFields`**                          | Array of field names which should be included in the report. For a list of available fields, see [Reporting Fields and Descriptions](/docs/cybs/en-us/reporting/developer/all/rest/reporting/reporting_fields.md "")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Required           |
| **`reportMimeType`**                        | Format of the report. Valid values are: * application/xml * text/csv                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Optional           |
| **`reportFrequency`**                       | Frequency of the report subscription. The options are: * Daily * Weekly * Monthly                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Optional           |
| **`reportName`**                            | Unique name of the report subscription you want to create or edit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Required           |
| **`timeZone`**                              | Merchant's time zone. For a list of supported time zones, see [Supported Time Zones](/docs/cybs/en-us/reporting/developer/all/rest/reporting/time-zones.md ""). For example: America/Chicago                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Required           |
| **`startTime`**                             | Time of day the report will run. Format: HHMM                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Optional           |
| **`startDay`**                              | Day of month (1-31) the report will run for monthly reports.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Optional           |
| **`reportFilters`**                         | Array that contains additional filters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Optional           |
| **`reportPreferences.signedAmounts`**       | Indicator that determines whether or not a negative sign is used for the amount of all refunded transactions. Valid values: * true * false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Optional           |
| **`reportPreferences.fieldNameConvention`** | Specify the field naming convention to be followed in reports (applicable only to csv report formats). Valid values: * Simple Order API * SCMP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Optional           |
| **`selectedMerchantGroupName`**             | Name of the merchant group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Optional           |
[Create/Update Report Subscription Request Body Values]

Responses
---------

This call can return one of the following HTTP status codes:

* 200: Ok.
* 304: Not modified.
* 404: Report not found.

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#reporting "") .

Deleting Report Subscriptions {#reporting-subscriptions-delete}
===============================================================

To delete a report subscription, your client application must send an HTTP DELETE request to the report server. The format of the URL is as follows:

```keyword varname
DELETE https://&lt;url_prefix&gt;/reporting/v3/report-subscriptions/{reportName}
```

For example, if you wanted to delete a report titled Daily Transactions, the request would be:

```keyword varname
DELETE https://&lt;url_prefix&gt;/reporting/v3/report-subscriptions/DailyTransactions
```

| Value                  | Description                                                                                                                                                                                                    | Required/Optional |
|:-----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| \&lt;`url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Test:** `apitest.cybersource.com` * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com | Required          |
| `{reportName}`         | Unique name of the report subscription you want to create or edit.                                                                                                                                             | Required          |
[Delete Report Subscription URL Values]

Responses
---------

This call can return one of the following HTTP status codes:

* 200: Ok.
* 400: Invalid request.
* 404: Report not found.

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#reporting "") .

Retrieving Available Reports {#reporting-retrieving}
====================================================

Using the API, you can retrieve a list of reports that are generated and available for download. The request format is:

```
https://&lt;url_prefix&gt;/reporting/v3/reports?startTime={startTime}&endTime={endTime}?timeQueryType={timeQueryType}
```

| Value                  | Description                                                                                                                                                                                                    | Required/Optional |
|:-----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| \&lt;`url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Test:** `apitest.cybersource.com` * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com | Required          |
| `{organizationId}`     | The organization ID under which the report is subscribed. This can be the merchant ID, account ID, or reseller ID.                                                                                             | Optional          |
| `{startTime}`          | Report start date to search on in ISO 8601 format. **Example**: 2016-11-22T12:00:00.000Z                                                                                                                       | Required          |
| `{endTime}`            | Report end date to search on in ISO 8601 format. **Example**: 2016-11-22T12:00:00.000Z                                                                                                                         | Required          |
| `{timeQueryType}`      | Time you would like to search. Valid values: * reportTimeFrame * executedTime                                                                                                                                  | Required          |
| `{reportMimeType}`     | Format of the report. Valid values are: * application/xml * text/csv                                                                                                                                           | Optional          |
| `{reportFrequency}`    | Frequency of the report subscription. The options are: * Daily * Weekly * Monthly * Adhoc                                                                                                                      | Optional          |
| `{reportName}`         | Unique name of the report.                                                                                                                                                                                     | Optional          |
| `{reportDefinitionId}` | Report definition ID.                                                                                                                                                                                          | Optional          |
| `{reportStatus}`       | Status of the report. The options are: * COMPLETED * PENDING * QUEUED * RUNNING * ERROR * NO_DATA                                                                                                              | Optional          |
[Create/Update Report Subscription Request URL Values]

Responses
---------

This call can return one of the following HTTP status codes:

* 200: Ok.
* 400: Invalid request.
* 404: Report not found or there are no available transactions.

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#reporting "") .

Downloading Reports {#reporting-download}
=========================================

You can use the Reporting API to download completed reports. For information about creating reports, see the *`Business Center` Reporting User Guide*. You cannot receive a report in more than one format.

Request Format
--------------

To request a report, your client application must send an HTTP GET message to the report server. The URL that you specify in your message indicates which report you want to download. Format the URL as follows:

```keyword varname
https://&lt;url_prefix&gt;/reporting/v3/report-downloads&organizationId={organizationId}&reportDate={date}&reportName={reportName}
```

For example, if your organization ID were `SampleMerchant`, you would use the following URL to download the XML version of the February 20, 2017, which is named Sample Daily Report:

```keyword varname
https://&lt;url_prefix&gt;/reporting/v3/report-downloads&organizationId=SampleMerchant&reportDate=20170220&reportName=SampleDailyReport
```

| Value                  | Description                                                                                                                                                                                                    | Required/ Optional |
|:-----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| \&lt;`url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Test:** `apitest.cybersource.com` * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com | Required           |
| `{organizationId}`     | The organization ID under which the report is subscribed. This can be the merchant ID, account ID, or reseller ID.                                                                                             | Optional           |
| `{reportName}`         | Unique name of the report subscription you want to create or edit.                                                                                                                                             | Required           |
| `{reportDate}`         | The date of the report. For reports that span multiple days, this value would be the end date of the report. **Format:** YYYY-MM-DD                                                                            | Required           |
[Report Download URL Values]

{#reporting-download_table1}  
You can also download reports based on the report ID. To find out the report ID for a report, perform a report search as described in [Retrieving Available Reports](/docs/cybs/en-us/reporting/developer/all/rest/reporting/reporting_api/reporting-retrieving.md "") and find the report ID value you want to search for in the response. Format the URL as follows:

```keyword varname
https://&lt;url_prefix&gt;/reporting/v3/reports/{reportId}&organizationId={organizationId}
```

| Value                  | Description                                                                                                                                                                                                    |
|:-----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \&lt;`url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Test:** `apitest.cybersource.com` * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com |
| `{reportId}`           | Report ID.                                                                                                                                                                                                     |
| `{organizationId}`     | The organization ID under which the report is subscribed. This can be the merchant ID, account ID, or reseller ID.                                                                                             |
[Report Download by Report ID URL Values]

Responses
---------

This call can return one of the following HTTP status codes:

* 200: Ok.
* 400: Invalid request.
* 404: Report not found or there are no available transactions.

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#reporting "") .

Creating a One-Time Report {#reporting-onetime-create}
======================================================

To create a one-time report, your client application must send an HTTP POST request to the report server. The request body contains the details for creating the report, such as the report type, the start time, and the frequency. The format of the URL is as follows:

```keyword varname
PUT https://&lt;url_prefix&gt;/reporting/v3/reports
```

The request body would be:

```
{
                "organizationId": "myorg",
                "reportName": "DailyTransactions",
                "reportDefinitionName": "TransactionDetailClass",
                "reportFields": [
                    "Request.RequestID",
                    "Request.TransactionDate",
                    "Request.MerchantID",
                    "BillTo.FirstName",
                    "BillTo.LastName",
                    "BillTo.City",],
                "startTime": "1100",
                "reportMimeType": "application/xml,
                "reportFrequency": "DAILY",
                "timezone": "GMT",
                "startTime": "0900",
                "startDay": "1"
                }
            
```

| Value                  | Description                                                                                                                                                                                                    |
|:-----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \&lt;`url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Test:** `apitest.cybersource.com` * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com |
[Create One-Time Report URL Values]

| Value                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Required/ Optional |
|:---------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| **`organizationId`**                         | The organization ID under which the report is subscribed. This can be the merchant ID, account ID, or reseller ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Optional           |
| **`reportDefinitionName`**                   | Name of the report type you want to review. The options are: * `TransactionRequestClass`: Transaction Request Report * `PaymentBatchDetailClass`: Payment Batch Detail Report * `ExceptionDetailClass`: Transaction Exception Detail Report * `ProcessorSettlementDetailClass`: Processor Settlement Detail Report * `ProcessorEventsDetailClass`: Processor Events Detail Report * `FundingDetailClass`: Funding Detail Report * `AgingDetailClass`: Aging Detail Report * `ChargebackAndRetrievalDetailClass`: Chargeback And Retrieval Detail Report * `DepositDetailClass`: Deposit Detail Report * `FeeDetailClass`: Fee Detail Report * `InvoiceSummaryClass`: Invoice Summary Report * `PayerAuthDetailClass`: Payer Authentication Detail Report * `ConversionDetailClass`: Conversion Detail Report * `SubscriptionDetailClass`: Subscription Detail Report * `JPTransactionDetailClass`: JP Transaction Detail Report * `ServiceFeeDetailClass`: Service Fee Detail Report * `GatewayTransactionRequestClass`: Gateway Transaction Request Report * `DecisionManagerEventDetailClass`: `Decision Manager` Event Detail Report * `RecurringBillingDetailClass`: Recurring Billing Details Report | Required           |
| **`reportFields`**                           | Array of field names which should be included in the report. For a list of available fields, see [Reporting Fields and Descriptions](/docs/cybs/en-us/reporting/developer/all/rest/reporting/reporting_fields.md "")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Required           |
| **`reportMimeType`**                         | Format of the report. Valid values are: * application/xml * text/csv                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Optional           |
| **`reportName`**                             | Unique name of the report subscription you want to create or edit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Required           |
| **`timeZone`**                               | Merchant's time zone. For a list of supported time zones, see [Supported Time Zones](/docs/cybs/en-us/reporting/developer/all/rest/reporting/time-zones.md ""). **Example:** America/Chicago                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Optional           |
| **`startTime`**                              | Time of day the report will run. **Format:** HHMM                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Optional           |
| **`startDay`**                               | Day of month (1-31) the report will run for monthly reports.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Optional           |
| **`reportFilters`**                          | Array that contains additional filters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Optional           |
| **`reportPreferences.signed Amounts`**       | Indicator that determines whether or not a negative sign is used for the amount of all refunded transactions. Valid values: * true * false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Optional           |
| **`reportPreferences.fieldName Convention`** | Specify the field naming convention to be followed in reports (applicable only to csv report formats). Valid values: * SOAPI * SCMP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Optional           |
| **`selectedMerchantGroupName`**              | Name of the merchant group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Optional           |
[Create/Update Report Subscription Request Body Values]

Responses
---------

This call can return one of the following HTTP status codes:

* 200: Ok.
* 304: Not modified.
* 404: Report not found or no transactions are available.

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#reporting "") .

Downloading On-Demand Conversion Detail Report {#reporting-ondemand-detail-download}
====================================================================================

The Conversion Detail Report contains details of transactions for a merchant. To request the report, your client application must send an HTTP GET message to the report server. The default format for responses is JSON, but some reports can also return CSV or XML. You can set the response to return CSV or XML in the request header by setting the `Accept` value to either `application/xml` or `text/csv`.  
Format the URL as follows:

```keyword varname
https://&lt;url_prefix&gt;/reporting/v3/conversion-details?startTime={startTime}&endTime={endTime}&organizationId={organizationId}
```

| Value                   | Description                                                                                                                                                                                                    | Required/ Optional |
|:------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| \&lt; `url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Test:** `apitest.cybersource.com` * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com | Required           |
| `{startTime}`           | Report start date to search on in ISO 8601 format. **Example:** 2016-11-22T12:00:00.000Z                                                                                                                       | Required           |
| `{endTime}`             | Report end date to search on in ISO 8601 format. **Example:** 2016-11-22T12:00:00.000Z                                                                                                                         | Required           |
| `{organizationId}`      | The organization ID under which the report is subscribed. This can be the merchant ID, account ID, or reseller ID.                                                                                             | Optional           |
[On-Demand Conversion Detail Report URL Values]

Responses
---------

This call can return one of the following HTTP status codes:

* 200: Ok.
* 400: Invalid request.
* 404: Report not found or no transactions are available.

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#reporting "") .

Downloading On-Demand Notification of Change Report {#reporting-ondemand-noc-download}
======================================================================================

The Notification of Change Report contains a list of `eCheck`-related values updated as a result of a response to an `eCheck` settlement transaction. To request the report, your client application must send an HTTP GET message to the report server. Format the URL as follows:

```keyword varname
https://&lt;url_prefix&gt;/reporting/v3/notification-of-changes?startTime={startTime}&endTime={endTime}
```

| Value                   | Description                                                                                                                                                                                                    | Required/Optional |
|:------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| \&lt; `url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Test:** `apitest.cybersource.com` * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com | Required          |
| `{startTime}`           | Report start date to search on in ISO 8601 format. **Example:** 2016-11-22T12:00:00.000Z                                                                                                                       | Required          |
| `{endTime}`             | Report end date to search on in ISO 8601 format. **Example:** 2016-11-22T12:00:00.000Z                                                                                                                         | Required          |
[On-Demand Notification of Change Report URL Values]

Responses
---------

This call can return one of the following HTTP status codes:

* 200: Ok.
* 400: Invalid request.
* 401: Unauthorized. The provided token is no longer valid.
* 404: Report not found or no transactions are available.
* 500: Internal server error.

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#reporting "") .

Downloading On-Demand Purchase and Refund Detail Report {#reporting-ondemand-purchase-refund-download}
======================================================================================================

The Purchase and Refund Detail Report contains purchase and refund details that have been submitted to your payment processor. Merchants using certain payment processors will also see fee and funding data. To request the report, your client application must send an HTTP GET message to the report server. The default format for responses is JSON, but some reports can also return CSV or XML. You can set the response to return CSV or XML in the request header by setting the `Accept` value to either `application/xml` or `text/csv`.  
Format the URL as follows:

```keyword varname
https://&lt;url_prefix&gt;/reporting/v3/purchase-refund-details&startTime={startTime}&endTime={endTime}
```

| Value                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Required/ Optional |
|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| \&lt; `url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Test:** `apitest.cybersource.com` * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com                                                                                                                                                                                                                                                                                                                     | Required           |
| `{startTime}`           | Report start date to search on in ISO 8601 format. **Example:** 2016-11-22T12:00:00.000Z                                                                                                                                                                                                                                                                                                                                                                                                                                           | Required           |
| `{endTime}`             | Report end date to search on in ISO 8601 format. **Example:** 2016-11-22T12:00:00.000Z                                                                                                                                                                                                                                                                                                                                                                                                                                             | Required           |
| `{organizationId}`      | The organization ID under which the report is subscribed. This can be the merchant ID, account ID, or reseller ID.                                                                                                                                                                                                                                                                                                                                                                                                                 | Optional           |
| `{paymentSubtype}`      | Payment subtypes. The default value is `ALL`. Valid values: * ALL: All Payment Subtypes * VI: Visa * MC: Mastercard * AX: American Express * DI: Discover * DP: PINless Debit                                                                                                                                                                                                                                                                                                                                                      | Optional           |
| `{viewBy}`              | View results by request date or submission date. The default value is `requestDate`. Valid values: * requestDate: Request Date * submissionDate: Submission Date                                                                                                                                                                                                                                                                                                                                                                   | Optional           |
| `{groupName}`           | Group name, which is defined in the Group Management Module in the `Business Center`.                                                                                                                                                                                                                                                                                                                                                                                                                                              | Optional           |
| `{offset}`              | Controls the starting point within the collection of results, which defaults to 0. The first item in the collection is retrieved by setting a zero offset. For example, if you have a collection of 15 items to be retrieved from a resource and you specify limit=5, you can retrieve the entire set of results in 3 successive requests by varying the offset value: `offset=0`, `offset=5`, and `offset=10`. If an offset larger than the number of results is provided, this will result in no embedded object being returned. | Optional           |
| `{limit}`               | Controls the maximum number of items that may be returned for a single request. The default is 2000.                                                                                                                                                                                                                                                                                                                                                                                                                               | Optional           |
[On-Demand Purchase and Refund Detail Report URL Values]

Responses
---------

This call can return one of the following HTTP status codes:

* 200: Ok.
* 400: Invalid request.
* 401: Unauthorized. The provided token is no longer valid.
* 404: Report not found or no transactions are available.
* 500: Internal server error.

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#reporting "") .

Downloading On-Demand Net Funding Report {#reporting-ondemand-net-funding-download}
===================================================================================

The Net Funding report contains the daily interchange, discount, and standard assessments. Some month-end fees, such as authorizations, are detected at the end of the month and appear in the Net Funding report on that particular day. Total Net Funding is obtained after subtracting chargebacks, fees, and any other negative amounts. To request the report, your client application must send an HTTP GET message to the report server. Format the URL as follows:

```keyword varname
https://&lt;url_prefix&gt;/reporting/v3/net-fundings&startTime={startTime}&endTime={endTime}
```

| Value                   | Description                                                                                                                                                                                                    | Required/ Optional |
|:------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| \&lt; `url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Test:** `apitest.cybersource.com` * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com | Required           |
| `{startTime}`           | Report start date to search on in ISO 8601 format. **Example:** 2016-11-22T12:00:00.000Z                                                                                                                       | Required           |
| `{endTime}`             | Report end date to search on in ISO 8601 format. **Example:** 2016-11-22T12:00:00.000Z                                                                                                                         | Required           |
| `{organizationId}`      | The organization ID under which the report is subscribed. This can be the merchant ID, account ID, or reseller ID.                                                                                             | Optional           |
| `{groupName}`           | Group name, which is defined in the Group Management Module in the `Business Center`.                                                                                                                          | Optional           |
[On-Demand Net Funding Report URL Values]

Responses
---------

This call can return one of the following HTTP status codes:

* 200: Ok.
* 400: Invalid request.
* 401: Unauthorized. The provided token is no longer valid.
* 404: Report not found or no transactions are available.
* 500: Internal server error.

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#reporting "") .

Downloading Payment Batch Summary Report {#reporting-payment-batch-summary-download}
====================================================================================

The Payment Batch Summary report shows total sales and refunds by currency and payment method. To request the report, your client application must send an HTTP GET message to the report server. Format the URL as follows:

```keyword varname
https://&lt;url_prefix&gt;/reporting/v3/payment-batch-summaries&startTime={startTime}&endTime={endTime}
```

| Value                   | Description                                                                                                                                                                                                                                                                                                                                                | Required/ Optional                                                   |
|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------|
| \&lt; `url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Test:** `apitest.cybersource.com` * **Production:** `api.cybersource.com` * **Production in India:** api.in.cybersource.com                                                                                                                                             | Required                                                             |
| `{startTime}`           | Report start date to search on in ISO 8601 format (yyyy-MM-dd'T'HH:mm:ss.SSSZ). **Example:** 2019-05-01T12:00:00-05:00                                                                                                                                                                                                                                     | Required                                                             |
| `{endTime}`             | Report end date to search on in ISO 8601 format (yyyy-MM-dd'T'HH:mm:ss.SSSZ). **Example:** 2019-08-30T12:00:00-05:00                                                                                                                                                                                                                                       | Required                                                             |
| `{organizationId}`      | The organization ID under which the report is subscribed. This can be the merchant ID, account ID, or reseller ID.                                                                                                                                                                                                                                         | Optional                                                             |
| `{rollUp}`              | Specifies whether to present data in spans of a single day, week, or month. The options are: * `day` * `week` * `month`                                                                                                                                                                                                                                    | Conditional. Required when requesting breakdown data for a merchant. |
| `{breakdown}`           | Used to request data at the parent-level account, such as Reseller. The options are: * `account_rollup`: Returns batch summaries data aggregated at the account level. * `all_merchant`: Returns batch summaries data for all MIDs that belong to the requesting parent ID. * `selected_merchant`: Returns batch summaries data for the selected merchant. | Conditional. Required when requesting breakdown data for a merchant. |
| `{startDayOfWeek}`      | Start day of week to breakdown data. The options are: * `1` * `2` * `3` * `4` * `5` * `6` * `7`                                                                                                                                                                                                                                                            | Optional                                                             |
[On-Demand Net Funding Report URL Values]

Responses
---------

This call can return one of the following HTTP status codes:

* 200: Ok.
* 400: Invalid request.
* 404: Report not found or no transactions are available.

For detailed information on the responses, including which fields are returned, see the [Reporting REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#reporting "") .

Reporting Fields and Descriptions {#reporting-fields}
=====================================================

This section contains a list of available reporting fields by field type (for example, billing, settlement, tokens). Where available, additional details, including description, field format, and mapped values, are included.

Application Fields {#application}
=================================

| Field Name |                             Description                              |
|------------|----------------------------------------------------------------------|
| Name       | Name of application used.                                            |
| Rcode      | One-digit code indicating whether the entire request was successful. |
| ReasonCode | Numeric value that corresponds to the result of the overall request. |
| Rflag      | One-word description of the result of the entire request.            |
| Rmsg       | Message that explains the `&lt;ics_flag&gt;` value.                  |
[Application Field Names and Descriptions]

Authorization Results Fields {#auth-results}
============================================

| Field Name |                    Description                     |
|------------|----------------------------------------------------|
| AVSResult  | Optional results of address verification test.     |
| CVVResult  | Optional results of card verification number test. |
[Authorization Results Field Names and Descriptions]

Bank Information Fields {#bank-info}
====================================

Field names in this group are prepended with the text BankInfo:

| Field Name |                                           Description                                            |
|------------|--------------------------------------------------------------------------------------------------|
| Address    | Bank's address.                                                                                  |
| BranchCode | Code that identifies the branch of the customer's bank when you are not using the IBAN.          |
| City       | City in which the bank is located.                                                               |
| Country    | Country in which the bank is located.                                                            |
| Name       | Bank's name.                                                                                     |
| SwiftCode  | Bank's SWIFT code. Unique address of the bank. Also known as the Bank Identification Code (BIC). |
[Bank Information Field Names and Descriptions]

Batch Fields {#batch}
=====================

| Field Name  |                       Description                       |
|-------------|---------------------------------------------------------|
| BatchDate   | Date when the batch was sent to the processor.          |
| BatchID     | Batch in which the transaction was sent.                |
| Status      | Status of batch file.                                   |
| SuccessFlag | Indicates whether batch file processing was successful. |
[Batch Field Names and Descriptions]

Bill To Fields {#bill-to}
=========================

Field names in this group are prepended with the text BillTo:

| Field Name   | Description                                                                                                                                                                                                                      |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Address1     | First line of the billing street address as it appears on the credit card issuer's records.                                                                                                                                      |
| Address2     | Additional address information.                                                                                                                                                                                                  |
| City         | City of the billing address.                                                                                                                                                                                                     |
| CompanyName  | Name of the customer's company.                                                                                                                                                                                                  |
| CompanyTaxID | Tax identification number of customer's company.                                                                                                                                                                                 |
| Country      | Country of the billing address.                                                                                                                                                                                                  |
| CustomerID   | Your identifier for the customer.                                                                                                                                                                                                |
| Email        | Customer's email address, including the full domain name.                                                                                                                                                                        |
| FirstName    | First name of the billed customer.                                                                                                                                                                                               |
| HostName     | DNS resolved hostname from billTo_ipAddress.                                                                                                                                                                                     |
| IPAddress    | Customer's IP address.                                                                                                                                                                                                           |
| LastName     | Last name of the billed customer.                                                                                                                                                                                                |
| MiddleName   | Middle name of the billed customer.                                                                                                                                                                                              |
| NameSuffix   | Suffix of billed customer.                                                                                                                                                                                                       |
| PersonalID   | Personal identifier. This field is supported only for Redecard in Brazil for `Cybersource Latin American Processing`. Set this field to the Cadastro de Pessoas Fisicas (CPF), which is required for AVS for Redecard in Brazil. |
| Phone        | Customer's phone number.                                                                                                                                                                                                         |
| State        | State or province of the billing address.                                                                                                                                                                                        |
| Title        | Title of the billed customer.                                                                                                                                                                                                    |
| UserName     | Customer's user name.                                                                                                                                                                                                            |
| Zip          | ZIP/Postal code for the billing address. The postal code must consist of five to nine digits.                                                                                                                                    |
[Bill To Field Names and Descriptions]

Chargeback and Retrieval Fields {#chargeback}
=============================================

|           Field Name            |                                                         Description                                                          |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| AdjustmentAmount                | Amount of the chargeback adjustment.                                                                                         |
| AdjustmentCurrency              | Currency of the chargeback adjustment.                                                                                       |
| AdjustmentARN                   | Association reference number.                                                                                                |
| CaseIdentifier                  | Numerical identifier created by `Cybersource` to represent a unique chargeback, representment, or other exception.           |
| CaseNumber                      | Processor-assigned case number.                                                                                              |
| CaseTime                        | The date that the case was opened.                                                                                           |
| CaseType                        | Description of the case type.                                                                                                |
| ChargebackAmount                | Amount of the chargeback.                                                                                                    |
| ChargebackCurrency              | Chargeback currency code.                                                                                                    |
| ChargebackMessage               | Text message from the issuer explaining the reason for the chargeback or other exception.                                    |
| ChargebackReasonCode            | Association chargeback reason code.                                                                                          |
| ChargebackReasonCodeDescription | Text description of the reason code.                                                                                         |
| ChargebackTime                  | The date that the chargeback was originated by the issuing bank.                                                             |
| DocumentIndicator               | Indicates whether or not there are associated documents. Possible values: * `Y` * `N`                                        |
| FeeAmount                       | Amount of the chargeback exception fee.                                                                                      |
| FeeCurrency                     | Currency code for the chargeback exception fee.                                                                              |
| FinancialImpact                 | Indicates whether or not there is a financial impact. Possible values: * `Y` * `N`                                           |
| FinancialImpactType             | Debit, credit, or none.                                                                                                      |
| MerchantCategoryCode            | Four-digit number that the payment card industry uses to classify merchants into market segments.                            |
| PartialIndicator                | Flag indicating whether the transaction is enabled for partial chargeback.                                                   |
| ResolutionTime                  | Resolution time in UTC.                                                                                                      |
| ResolvedToIndicato              | Indicates resolved to status of transaction. Possible values: * `B`: Bank * `M`: Merchant * `S`: Split * `G`: General ledger |
| RespondByDate                   | Date by which item must be submitted to the chargeback processor to allow sufficient time for representment.                 |
| TransactionType                 | Capture type of the original transaction.                                                                                    |
[Chargeback and Retrieval Field Names and Descriptions]

Check Fields {#check}
=====================

Field names in this group are prepended with the text Check:

|    Field Name     |                                 Description                                  |
|-------------------|------------------------------------------------------------------------------|
| BankTransitNumber | ---                                                                          |
| AccountEncoderID  | Identifier for the bank that provided the customer's encoded account number. |
| SecCode           | Authorization method used for the transaction.                               |
[Check Field Names and Descriptions]

Conversion Fields {#conversion}
===============================

|    Field Name    |                       Description                        |
|------------------|----------------------------------------------------------|
| ConversionDate   | Date order converted.                                    |
| NewDecision      | Reviewer evaluation result.                              |
| OriginalDecision | Order profile evaluation result.                         |
| Profile          | Order profile used to evaluate the order.                |
| Reviewer         | Person who evaluated order originally marked for review. |
| ReviewerComments | Additional information added by reviewer.                |
| Queue            | Review queue originally assigned to order.               |
[Conversion Field Names and Descriptions]

Deposit Fields {#deposit}
=========================

| Field Name              | Description                                                                                                                     |
|:------------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| Amount                  | Amount of the deposit.                                                                                                          |
| Category                | Category of the deposit.                                                                                                        |
| Currency                | Currency code of the deposit.                                                                                                   |
| ExchangeRate            | Exchange rate. Includes a decimal point and up to 4 decimal places.                                                             |
| ExchangeRateDescription | Exchange rate description from the funding bank.                                                                                |
| Identifier              | Unique reference number for this deposit.                                                                                       |
| MerchantBankAcctLast4   | Bank account number to which the funds transfer will be deposited. For security purposes, all but the last 4 digits are masked. |
| MerchantBankAcctName    | Name used on the bank account.                                                                                                  |
| MerchantBankCode        | Routing number for the account to which the funds transfer will be deposited.                                                   |
| MerchantBankCountry     | Country in which the bank is located. Use the two-character ISO Standard Country Codes.                                         |
| MerchantBankName        | Bank's name.                                                                                                                    |
| MerchantID              | `Cybersource` merchant ID.                                                                                                      |
| Method                  | Funds transfer method.                                                                                                          |
| Status                  | Status of the deposit. Possible values: * `S`: Success * `P`: Pending * `F`: Failed                                             |
| Time                    | Deposit time for the transaction in UTC.                                                                                        |
| TransferMessage         | Deposit transfer message provided by the processor.                                                                             |
| Type                    | Description of events included in this funds transfer.                                                                          |
[Deposit Field Names and Descriptions]

Device Fields {#device}
=======================

| Field Name |                      Description                      |
|------------|-------------------------------------------------------|
| DeviceID   | Identification number of device used for transaction. |
[Device Field Names and Descriptions]

Event Fields {#event}
=====================

|    Field Name    |                                                Description                                                 |
|------------------|------------------------------------------------------------------------------------------------------------|
| Amount           | Amount for the event.                                                                                      |
| CurrencyCode     | Currency code for the event.                                                                               |
| Event            | Type of event that occurred for the transaction.                                                           |
| EventDate        | Date in GMT format that the event occurred. This field can be null for some event types, such as Declined. |
| ProcessorMessage | Additional information from the processor about the event, such as an error message or explanation.        |
[Event Field Names and Descriptions]

Exception Fields {#exception}
=============================

|             Field Name             |                                                            Description                                                             |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Action                             | Brief description of the action.                                                                                                   |
| ClientID                           | ID of the client.                                                                                                                  |
| CYBSExceptionID                    | Exception ID number assigned by `Cybersource`.                                                                                     |
| DccLookupStatus                    | DCC lookup status of the transaction.                                                                                              |
| DccExchangeRate                    | DCC exchange rate of the transaction.                                                                                              |
| DccMarginRate                      | DCC margin rate of the transaction.                                                                                                |
| ExceptionAmount                    | Amount specified in the exception.                                                                                                 |
| ExceptionAmount Currency           | Exception currency represented in ISO 4217:2008 alpha-3.                                                                           |
| ExceptionCategory                  | Type of exception.                                                                                                                 |
| ExceptionDate                      | Date of exception.                                                                                                                 |
| ExceptionDescription               | Description of exception.                                                                                                          |
| ExceptionDeviceHardwareRevision    | Hardware revision number of the device.                                                                                            |
| ExceptionDeviceID                  | ID of the device.                                                                                                                  |
| ExceptionDeviceOS                  | Operating system of the device.                                                                                                    |
| ExceptionDeviceOS Version          | Operating system verion of the device.                                                                                             |
| ExceptionDevice TerminalID         | Device Terminal ID number.                                                                                                         |
| ExceptionMessage                   | Description of the exception.                                                                                                      |
| ExceptionReasonCode                | Reason code for the error that occurred. This reason code is the same one that you receive in the response or transaction receipt. |
| ExceptionReason Description        | Description of exception reason.                                                                                                   |
| ExceptionStatus                    | Current status of the transaction.                                                                                                 |
| ExceptionStatusCode                | Status code of the exception.                                                                                                      |
| ExceptionType                      | Type of exception.                                                                                                                 |
| FinancialStatus                    | Financial status of the transaction.                                                                                               |
| LastActionDate                     | Date of last action on the transaction.                                                                                            |
| LocalCurrencyCode                  | Local currency code.                                                                                                               |
| NextActionDate                     | Date of next action on the transaction.                                                                                            |
| OriginalTransaction SubmissionDate | Date on which the transaction was submitted.                                                                                       |
| PartnerMerchantID                  | Merchant ID of partner.                                                                                                            |
| PartnerMerchantName                | Merchant name of partner.                                                                                                          |
| PaymentNumber                      | Payment number.                                                                                                                    |
| ProcessorCaseID                    | Processor-assigned case number                                                                                                     |
| ProcessorResponseCode              | Code returned directly from the processor for the exception that occurred.                                                         |
| ReasonCode                         | Reason code for the exception that occurred.                                                                                       |
| RetryCount                         | Total number of payments that are pending in retry mode.                                                                           |
| SchemeOperator                     | Scheme operator.                                                                                                                   |
| SDKVersion                         | SDK version being used.                                                                                                            |
| SettlementProcessor                | Name of settlement processor.                                                                                                      |
| StorageMechanism                   | Storage mechanism being used.                                                                                                      |
[Exception Field Names and Descriptions]

Fee Fields {#fee}
=================

| Field Name               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AssessmentAmount         | Amount of the assessment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| AssessmentCurrency       | Currency of the assessment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| BillingCycle             | Billing cycle of the merchant. Possible values: * `daily` * `weekly` * `monthly`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| BillingType              | Billing type of the merchant. Possible values: * `discount` * `interchangePlus` * `serviceFee` * `other`                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ClearedInterchangeLevel  | Code for the clearing level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DiscountAmount           | DiscountRate \*TransactionAmount. This value includes four decimal points.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DiscountCurrency         | Currency of the discount.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DiscountRate             | Discount rate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DowngradeReasonCode      | Reason for downgrade. Possible values: * `1`: Transaction exceeded timeliness. * `2`: Authorization code is missing. * `8`: POS entry mode does not qualify. * `9`: POS condition code does not qualify. * `A`: POS terminal capability does not qualify. * `D`: Mail/phone/e-commerce indicator does not qualify. * `K`: Transaction cleared as intraregional. * `L`: Transaction cleared as interregional. * `R`: Reclassification. * `U`: UK domestic. * `V`: German domestic. * `W`: Transaction cleared as world signia. * `X`: Did not qualify at merchant price level |
| InterchangeAmount        | Final amount of transaction after the interchange rates are applied.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| InterchangeCurrency      | ISO currency code for the currency of the clearing rate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| InterchangeRate          | Interchange rate for the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PerItemFeeAmount         | Fee for a single item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PerItemFeeCurrency       | Currency for a single item fee.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PricedInterchangeLevel   | Interchange flat rate that was assigned when you set up your account. This value includes four decimal points.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ServiceFeeAmount         | Amount of service fee for transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ServiceFeeAmountCcy      | Currency of the service fee.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ServiceFeeFixedAmount    | Amount of the fixed service fee for the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ServiceFeeFixedAmountCcy | Currency of the fixed service fee.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ServiceFeeRate           | Percentage rate of the service fee.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| SettlementAmount         | Amount of the settlement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| SettlementCurrency       | Currency of the settlement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SettlementTime           | Time the settlement was processed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| SettlementTimeZone       | Time zone of the settlement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| SourceDescriptor         | Source descriptor for transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| TotalFeeAmount           | Total amount of all fee transactions for the specified date range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| TotalFeeCurrency         | Currency for all fee transactions for the specified date range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
[Fee Field Names and Descriptions]

Fee Summary Fields {#fee-summary}
=================================

| Field Name        | Description                         |
|:------------------|:------------------------------------|
| CardType          | Card type.                          |
| Count             | Count.                              |
| FeeDescription    | Fee description.                    |
| FeeType           | Fee type.                           |
| FundingCurrency   | Currency in which fees are applied. |
| PaymentMethod     | Payment method used.                |
| PercentageFee     | Percentage fee charged.             |
| PerItemFee        | Fee charged per item.               |
| TotalFeeAmount    | Total fee amount.                   |
| TransactionAmount | Transaction amount.                 |
| TransactionType   | Transaction type.                   |
[Fee Summary Field Names and Descriptions]

Funding Fields {#Id18APB0DF0QU}
===============================

Field names in this group are prepended with the text Funding:

| Field Name                   | Description                                                                  |
|:-----------------------------|:-----------------------------------------------------------------------------|
| CurrencyExchange Description | Exchange rate description from the processor.                                |
| CurrencyExchangeRate         | Exchange rate for converting from transaction currency to funding currency.  |
| FeeAmount                    | Fee for the transaction.                                                     |
| FeeCurrency                  | Fee currency represented in ISO 4217:2008 alpha-3.                           |
| FeeDescription               | Fee description from the processor.                                          |
| FundingAccountSuffix         | Last 4 digits of funding account.                                            |
| FundingAmount                | Funding amount of the transaction.                                           |
| FundingBankCode              | Bank code of the funding bank.                                               |
| FundingBankCountry           | Bank country of the funding bank represented in ISO 3166-1 alpha-3.          |
| FundingBankName              | Name of bank funding the transaction.                                        |
| FundingCurrency              | Funding currency represented in ISO 4217:2008 alpha-3.                       |
| FundingDate                  | Funding date of the transaction.                                             |
| FundingIdentification Number | Funding identification for the funding of the transaction.                   |
| FundingProcessorMessage      | Funding response message from the processor.                                 |
| FundingTransferMessage       | Funding transfer message provided by the processor.                          |
| ProcessorResponseCode        | Funding response code from the processor.                                    |
| Status                       | Funding status. Possible values: * `S`: Success * `P`: Pending * `F`: Failed |
[Funding Field Names and Descriptions]

Fund Transfer Fields {#fund-transfer}
=====================================

Field names in this group are prepended with the text FundTransfer:

| Field Name     | Description                                          |
|:---------------|:-----------------------------------------------------|
| BankCheckDigit | Code used to validate the customer's account number. |
| IbanIndicator  | International Bank Account Number (IBAN).            |
[Fund Transfer Field Names and Descriptions]

Gift Card Fields {#gift_cards}
==============================

| Field Name       | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Data Type (Length) | SOAPI Value               | SCMP Value                  |
|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:--------------------------|:----------------------------|
| Current Balance  | Current gift card balance in your local currency.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | String (12)        | giftCard_ currentBalance  | gift_card_ current_balance  |
| Previous Balance | Previous gift card balance in your local currency. This value was the gift card balance before the concurrent transaction was applied to the gift card. This field is supported only on ValueLink. For example, when a customer purchases a gift card and uses the gift card to purchase a product at the same time, the response message includes: * Previous gift card balance, which was the balance before the purchase of the product * Current gift card balance, which is the balance after the purchase of the product | String (12)        | giftCard_ previousBalance | gift_card_ previous_balance |
| Redemption Type  | Type of redemption. Possible values: * `CASHOUT` * `REDEMPTION` * `REDEMPTION_PARTIAL_ALLOWED` (default) This field is supported only on ValueLink.                                                                                                                                                                                                                                                                                                                                                                            | String (26)        | giftCard_ previousBalance | gift_card_ redemption_type  |
[Gift Card Fields]

Healthcare Fields {#health-care}
================================

| Field Name   | Description                                                                                                 | Data Type (Length) |
|:-------------|:------------------------------------------------------------------------------------------------------------|:-------------------|
| Amount       | Amount of the healthcare payment.                                                                           | VARCHAR2 (13)      |
| AmountType   | Type of healthcare payment. For example: * `healthcare` * `dental` * `clinic` {#health-care_ul_mxz_vmh_krb} | VARCHAR2 (35)      |
| Currency     | Currency used in transaction.                                                                               | VARCHAR2 (3)       |
| IndustryType | Type of industry for the transaction.                                                                       | VARCHAR2 (20)      |
[Healthcare Fields]

Invoice Fields {#invoice}
=========================

Field names in this group are prepended with the text Invoice:

|       Field Name        |             Description             |
|-------------------------|-------------------------------------|
| BillingGroupDescription | Description of the billing group.   |
| NotProcessed            | Number of unprocessed transactions. |
| OrganizationID          | Merchant ID.                        |
| PerformedServices       | `Cybersource` service name.         |
| Processed               | Number of processed transactions.   |
| Total                   | Invoice count.                      |
[Invoice Field Names and Descriptions]

JP Fields {#jp}
===============

| Field Name                  | Description                                                                                           | Data Type (Field Length) |
|:----------------------------|:------------------------------------------------------------------------------------------------------|:-------------------------|
| Amount                      | Transaction grand total.                                                                              | ---                      |
| AuthForward                 | Name of Japanese acquirer that processed transaction. Available only for CCS (CAFIS) and JCN Gateway. | ---                      |
| Authorization Code          | Transaction authorization code.                                                                       | ---                      |
| CardSuffix                  | Last four digits of card.                                                                             | ---                      |
| Currency                    | Currency used in transaction.                                                                         | ---                      |
| CustomerFirst Name          | Customer first name.                                                                                  | ---                      |
| CustomerLast Name           | Customer last name.                                                                                   | ---                      |
| Date                        | Date of transaction.                                                                                  | ---                      |
| Gateway                     | Name of gateway used to process transaction.                                                          | ---                      |
| JPOInstallment Method       | Number of payment installments (Japanese payment method only).                                        | ---                      |
| JPOPayment Method           | Type of Japanese payment method used.                                                                 | ---                      |
| MerchantID                  | `Cybersource` (gateway) merchant identifier.                                                          | ---                      |
| Merchant ReferenceNumber    | Merchant order reference or tracking number.                                                          | ---                      |
| NetworkToken TransType      | Network token transaction type.                                                                       | ---                      |
| PaymentMethod               | Method of payment.                                                                                    | ---                      |
| RequestID                   | Client request identifier.                                                                            | ---                      |
| SubscriptionID              | Customer profile identifier for requested service.                                                    | ---                      |
| Time                        | Time of transaction.                                                                                  | ---                      |
| Transaction ReferenceNumber | Reference number used to reconcile `Cybersource` (gateway) reports with processor reports.            | ---                      |
| TransactionType             | Type of transaction.                                                                                  | ---                      |
[JP Field Names and Descriptions]

Line Item Fields {#line-item}
=============================

Field names in this group are prepended with the text LineItems:

|     Field Name     |                                        Description                                        |
|--------------------|-------------------------------------------------------------------------------------------|
| FulfillmentType    | Information about the product code used for the line item.                                |
| InvoiceNumber      | Invoice number for order.                                                                 |
| MerchantProductSku | Identification code for the product.                                                      |
| Number             | Number of the line item in an order.                                                      |
| ProductCode        | Used to determine product category: electronic, handling, physical, service, or shipping. |
| ProductName        | Name of product.                                                                          |
| Quantity           | Quantity of product.                                                                      |
| TaxAmount          | Total tax to apply to the product.                                                        |
| UnitPrice          | Per-item price of the product.                                                            |
[Line Item Field Names and Descriptions]

Merchant Defined Data Fields {#merchant-defined-data}
=====================================================

Field names in this group are prepended with the text Merchant-DefinedDataFields:

|         Field Name          |                            Definition                            |
|-----------------------------|------------------------------------------------------------------|
| MerchantDefinedData_ field1 | Fields that you can use to store information (Field1 - Field20). |
[Merchant Defined Data Field Names and Descriptions]

Network Token Life-Cycle Management Fields {#net-tkn-lcm-fields}
================================================================

Field names in this group are prepended with the text LifeCycleManagementEvent, NetworkToken, or TMSToken:

|          Group           | Field Name                | Definition                                                                                   |
|--------------------------|:--------------------------|:---------------------------------------------------------------------------------------------|
| LifeCycleManagementEvent | LCMEventDateProcessed     | Date on which the life-cycle management event was fully processed.                           |
| LifeCycleManagementEvent | LCMEventStatus            | Processing status of the life-cycle management event.                                        |
| LifeCycleManagementEvent | LCMEventStatusText        | Free-formatted text field detailing the process of the life-cycle management event.          |
| LifeCycleManagementEvent | LCMEventType              | Type of life-cycle management event that is applied.                                         |
| LifeCycleManagementEvent | LCMEventUniqueID          | Unique identifier for the life-cycle management event that is applied.                       |
| NetworkToken             | CardExpiryDate            | Expiration date of the card.                                                                 |
| NetworkToken             | CardSuffix                | Last four digits of the card.                                                                |
| NetworkToken             | PAR                       | A unique reference that identifies the underlying payment account.                           |
| NetworkToken             | TokenExpiryDate           | Expiration date of the network token.                                                        |
| NetworkToken             | TokenModifiedDate         | Date on which the network token was modified.                                                |
| NetworkToken             | TokenRequestorID          | Identifier of the wallet that the network token belongs to.                                  |
| NetworkToken             | TokenService              | Token service that provisioned the network token.                                            |
| NetworkToken             | TokenState                | State of the network token.                                                                  |
| NetworkToken             | TokenSuffix               | Last four digits of the network token.                                                       |
| NetworkToken             | TokenUniqueID             | Unique identifier for the network token.                                                     |
| TMSToken                 | Creator                   | Organization ID or merchant ID of the organization or merchant that created the `TMS` token. |
| TMSToken                 | InstrumentIdentifierID    | Unique identifier for the instrument identifier.                                             |
| TMSToken                 | InstrumentIdentifierState | Current state of the instrument identifier token.                                            |
| TMSToken                 | VaultID                   | Unique identifier for the vault to which the token belongs.                                  |
[Network Token Life-Cycle Management Fields]

Payment Data Fields {#payment-data}
===================================

Field names in this group are prepended with the text PaymentData:

| Field Name                  | Description                                                                                                                                             |
|:----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| AAV_CAVV                    | Optional authentication data that you can receive after the customer is authenticated.                                                                  |
| ACHVerificationResult       | Raw result of the ACH verification service.                                                                                                             |
| ACHVerificationResultMapped | Mapped result of the ACH verification service.                                                                                                          |
| AcquirerMerchantID          | Merchant ID of acquirer.                                                                                                                                |
| AcquirerMerchantNumber      | Merchant number of acquirer.                                                                                                                            |
| Amount                      | Grand total for the order.                                                                                                                              |
| AuthIndicator               | Authorization indicator for the transaction.                                                                                                            |
| AuthorizationCode           | Authorization code for the payment.                                                                                                                     |
| AuthorizationType           | Authorization type of the payment.                                                                                                                      |
| AuthReversalAmount          | Authorization reversal amount.                                                                                                                          |
| AuthReversalResult          | Result of the authorization reversal.                                                                                                                   |
| AVSResult                   | Raw code for Address Verification Service result for the payment.                                                                                       |
| AVSResultMapped             | Address Verification Service result for the payment.                                                                                                    |
| BalanceAmount               | Remaining balance on the account.                                                                                                                       |
| BalanceCurrencyCode         | Currency of the remaining balance on the account.                                                                                                       |
| BankAccountName             | Name of bank account.                                                                                                                                   |
| BankCode                    | Code of bank branch.                                                                                                                                    |
| BinNumber                   | Bank identification number. In the `Business Center`, this field is called AccountPrefix.                                                               |
| CardCategory                | Type of card used in the transaction.                                                                                                                   |
| CardCategoryCode            | Category code of card used in the transaction.                                                                                                          |
| CardPresent                 | Card-present transaction indicator.                                                                                                                     |
| CardVerificationMethod      | Card verification method used.                                                                                                                          |
| CurrencyCode                | Currency code for the payment.                                                                                                                          |
| CVResult                    | CVN result code.                                                                                                                                        |
| DCCIndicator                | Flag that indicates whether Dynamic Currency Conversion is being used for the transaction.                                                              |
| DomesticRouting             | Flag indicates whether the transaction was routed domestically.                                                                                         |
| ECI                         | Optional information that you can receive if you use the Payer Authentication service.                                                                  |
| eCommerceIndicator          | Type of e-commerce transaction.                                                                                                                         |
| EMVRequestFallback          | EMV request fallback indicator.                                                                                                                         |
| EVEmail                     | Mapped Electronic Verification response code for the customer's email address.                                                                          |
| EVEmailRaw                  | Raw Electronic Verification response code from the processor for the customer's email address.                                                          |
| EventType                   | Type of event that occurred for the transaction.                                                                                                        |
| EVName                      | Mapped Electronic Verification response code for the customer's name.                                                                                   |
| EVNameRaw                   | Raw Electronic Verification response code from the processor for the customer's last name.                                                              |
| EVPhoneNumber               | Mapped Electronic Verification response code for the customer's phone number.                                                                           |
| EVPhoneNumberRaw            | Raw Electronic Verification response code from the processor for the customer's phone number.                                                           |
| EVPostalCode                | Mapped Electronic Verification response code for the customer's postal code.                                                                            |
| EVPostalCodeRaw             | Raw Electronic Verification response code from the processor for the customer's postal code.                                                            |
| EVStreet                    | Mapped Electronic Verification response code for the customer's street address.                                                                         |
| EVStreetRaw                 | Raw Electronic Verification response code from the processor for the customer's street address.                                                         |
| ExchangeRate                | Exchange rate.                                                                                                                                          |
| ExchangeRateDate            | Time stamp for the exchange rate.                                                                                                                       |
| GrandTotal                  | Grand total amount for the order, including tax, for requests that do not contain payment information.                                                  |
| IssuerResponseCode          | Response code of issuer.                                                                                                                                |
| MandateReferenceNumber      | Mandate reference number.                                                                                                                               |
| NetworkCode                 | Network code.                                                                                                                                           |
| NumberOfInstallments        | Total number of installments when making payments in installments.                                                                                      |
| PaymentProcessor            | Name of payment processor.                                                                                                                              |
| PaymentProductCode          | Type of payment product used by the consumer to pay on a payment provider's website, such as installments or bank transfer.                             |
| PaymentRequestID            | Original request ID for the purchase.                                                                                                                   |
| PinType                     | Type of PIN entry.                                                                                                                                      |
| POSCatLevel                 | Category of point of sale (POS).                                                                                                                        |
| POSEntryMode                | POS entry mode.                                                                                                                                         |
| POSEnvironment              | POS environment.                                                                                                                                        |
| ProcessorMID                | Processor merchant ID.                                                                                                                                  |
| ProcessorResponseCode       | The error message sent directly from the bank.                                                                                                          |
| ProcessorResponseID         | Response ID sent from the processor.                                                                                                                    |
| ProcessorTID                | Transaction ID (TID) that is used to identify and track a transaction throughout its life cycle.                                                        |
| ProcessorTransactionID      | Processor transaction ID.                                                                                                                               |
| RequestedAmount             | Amount requested to be authorized.                                                                                                                      |
| RequestedAmountCurrencyCode | Currency for the amount requested to be authorized.                                                                                                     |
| RoutingNetworkType          | Type of routing network.                                                                                                                                |
| StoreAndForwardIndicator    | Indicates whether store-and-forward is used for transaction.                                                                                            |
| SubMerchantCity             | Sub-merchant's city.                                                                                                                                    |
| SubMerchantCountry          | Sub-merchant's country.                                                                                                                                 |
| SubMerchantEmail            | Sub-merchant's email address.                                                                                                                           |
| SubMerchantID               | Sub-merchant's ID.                                                                                                                                      |
| SubMerchantName             | Sub-merchantv name.                                                                                                                                     |
| SubMerchantPhone            | Sub-merchant's phone number.                                                                                                                            |
| SubMerchantPostalCode       | Sub-merchant's postal code.                                                                                                                             |
| SubMerchantState            | Sub-merchant's state.                                                                                                                                   |
| SubMerchantStreet           | Sub-merchant's street address.                                                                                                                          |
| SurchargeFee                | Surcharge fee amount.                                                                                                                                   |
| SurchargeFeeSign            | Sign (+ or -) of the surcharge amount.                                                                                                                  |
| TargetAmount                | Converted amount.                                                                                                                                       |
| TargetCurrency              | Billing currency.                                                                                                                                       |
| TerminalIDAlternate         | Alternate terminal ID.                                                                                                                                  |
| TotalTaxAmount              | Total tax amount for all of the line items in the transaction.                                                                                          |
| TransactionRefNumber        | Reference number for the transaction.                                                                                                                   |
| XID                         | Optional transaction identifier generated by Payer Authentication that you can receive when the customer is enrolled and when validation is successful. |
[Payment Data Field Names and Descriptions]

Payment Method Fields {#payment-method}
=======================================

Field names in this group are prepended with the text PaymentMethod:

| Field Name          | Description                                                                                                                                                          |
|:--------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AccountSuffix       | Last four digits of the customer's payment account number.                                                                                                           |
| BankAccountName     | Bank's account name.                                                                                                                                                 |
| BankCode            | Bank's code. Used for some countries when you are not using the IBAN. Contact `Cybersource` customer support for required country-specific bank account information. |
| BoletoBarCodeNumber | Numeric representation of the boleto barcode.                                                                                                                        |
| BoletoNumber        | Boleto Bancário payment number.                                                                                                                                      |
| CardCategory        | Type of card used.                                                                                                                                                   |
| CardCategoryCode    | Code for card type used.                                                                                                                                             |
| CardType            | Type of card to authorize.                                                                                                                                           |
| CheckNumber         | Check number.                                                                                                                                                        |
| ExpirationMonth     | Two-digit month in which the credit card expires.                                                                                                                    |
| ExpirationYear      | Four-digit year in which the credit card expires.                                                                                                                    |
| IssueNumber         | Number of times a Maestro (UK domestic) card has been issued to the account holder.                                                                                  |
| MandateId           | Identification reference for the direct debit mandate.                                                                                                               |
| MandateType         | Type of mandate.                                                                                                                                                     |
| SignatureDate       | Date of signature.                                                                                                                                                   |
| StartMonth          | Month of the start of the Maestro (UK domestic) card validity period.                                                                                                |
| StartYear           | Year of the start of the Maestro (UK domestic) card validity period.                                                                                                 |
| WalletType          | Type of wallet.                                                                                                                                                      |
[Payment Method Field Names and Descriptions]

POS Terminal Exceptions Fields {#pos-terminal-exceptions}
=========================================================

Field names in this group are prepended with the text POSTerminalExceptions:

| Field Name                       | Description                                                                                                           |
|:---------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| POSTerminalException.BillToEmail | Email address of the user.                                                                                            |
| CardVerificationMethod           | Type of customer verification.                                                                                        |
| ClientID                         | Client identifier for an installation. Generated by the operating system.                                             |
| DCCExchangeRate                  | Dynamic Currency Conversion (DCC) exchange rate.                                                                      |
| DCCLookupStatus                  | Lookup Status of DCC.                                                                                                 |
| DCCMarginRate                    | Margin rate of DCC.                                                                                                   |
| DeviceHardwareRevision           | Hardware revision printed on the back of the credit card reader.                                                      |
| DeviceID                         | Serial number printed on the back of the credit card reader. Dashes are removed from the serial number.               |
| DeviceOS                         | Operating system of the device.                                                                                       |
| DeviceOSVersion                  | Operating system version of the device.                                                                               |
| DeviceTerminalID                 | Terminal ID assigned to the credit card reader. It is used by the clearing institute to identify credit card readers. |
| ExceptionCategory                | Status of the transaction.                                                                                            |
| ExceptionDescription             | Detailed description of the status of the transaction.                                                                |
| ExceptionStatusCode              | Code that represents the status of the transaction.                                                                   |
| LocalCurrencyCode                | Three-digit security code for the local currency.                                                                     |
| MerchantID                       | Merchant ID.                                                                                                          |
| PartnerMerchantID                | Three-digit ID for the partner merchant.                                                                              |
| PartnerMerchantName              | Name of the merchant that performed the transaction.                                                                  |
| PartnerOriginalTransactionID     | Unique ID for the transaction.                                                                                        |
| ProcessorMID                     | Merchant ID of the merchant that performed the transaction. Assigned by the clearing institute.                       |
| POSTerminalException.RequestID   | Unique ID of the transaction processor; for debugging purposes.                                                       |
| SchemeOperator                   | Scheme of the credit card.                                                                                            |
| SDKVersion                       | Version of the software development kit (SDK).                                                                        |
| StorageMechanism                 | Source from which payment details are collected.                                                                      |
| TerminalID                       | Terminal ID of the merchant that performed the transaction.                                                           |
| TransactionDate                  | Date of the transaction.                                                                                              |
[POS Terminal Exceptions Field Names and Descriptions]

Profile Fields {#profile}
=========================

Field names in this group are prepended with the text Profile:

| Field Name      | Description                       |
|:----------------|:----------------------------------|
| Name            | Name of the profile.              |
| ProfileDecision | Decision returned by the profile. |
| ProfileMode     | Activity mode of the profile.     |
| RuleDecision    | Decision returned by the rule.    |
| RuleName        | Name of the rule.                 |
[Profile Field Names and Descriptions]

Proof XML Fields {#proof-xml}
=============================

Field names in this group are prepended with the text ProofXML:

| Field Name         | Description                                     |
|:-------------------|:------------------------------------------------|
| AcquirerBin        | Acquiring bank identification number.           |
| Date               | Transaction date.                               |
| DirectoryServerURL | Directory server URL.                           |
| Enrolled           | Enrollment indicator.                           |
| MerchantID         | `Cybersource` merchant ID used for transaction. |
| Pan                | Customer masked account number.                 |
| Password           | Password.                                       |
[Proof XML Field Names and Descriptions]

Recipient Fields {#recipient}
=============================

Field names in this group are prepended with the text Recipient:

| Field Name               | Description                    |
|:-------------------------|:-------------------------------|
| Address                  | Recipient street address.      |
| City                     | Recipient city.                |
| Country                  | Recipient country.             |
| DOB                      | Recipient date of birth.       |
| FirstName                | Recipient first name.          |
| LastName                 | Recipient last name.           |
| MiddleInitial            | Recipient name middle initial. |
| PhoneNumber              | Recipient phone number.        |
| PostalCode               | Recipient postal code.         |
| RecipientBillingAmount   | Transaction billed amount.     |
| RecipientBillingCurrency | Recipient billing currency.    |
| ReferenceNumber          | Recipient reference number.    |
| State                    | Recipient state.               |
[Recipient Field Names and Descriptions]

Request Fields {#request}
=========================

Field names in this group are prepended with the text Request:

| Field Name                    | Description                                                                     |
|:------------------------------|:--------------------------------------------------------------------------------|
| Comments                      | Optional comments that you can make about the subscription or customer profile. |
| eCommerceIndicator            | E-commerce indicator for the transaction.                                       |
| MerchantID                    | `Cybersource` merchant ID used for the transactions.                            |
| MerchantReference Number      | Merchant-generated order reference or tracking number.                          |
| PartnerOriginal TransactionID | Transaction ID from the partner.                                                |
| PartnerSDKVersion             | SDK version used to process the transaction.                                    |
| RequestID                     | ID for the transaction request.                                                 |
| Source                        | Source of request.                                                              |
| SubscriptionID                | ID for the customer profile.                                                    |
| TerminalSerialNumber          | Serial number of the terminal.                                                  |
| TransactionDate               | Date on which the transaction occurred.                                         |
| TransactionID                 | ID of the transaction.                                                          |
| TransactionRefNumber          | Transaction reference number.                                                   |
| TransactionType               | Type of transaction.                                                            |
| User                          | Information about a user.                                                       |
[Request Field Names and Descriptions]

Risk Fields {#risk}
===================

Field names in this group are prepended with the text Risk:

| Field Name               | Description                                                                                                                                                                                                                                                                             |
|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AppliedAVS               | Indicates whether or not Address Verification Service rules were applied to the transaction.                                                                                                                                                                                            |
| AppliedCategoryGift      | Importance of billing and shipping addresses in assessing the order. If you do not specify a value in your request, the server uses the default value for your merchant ID.                                                                                                             |
| AppliedCategoryTime      | Importance of time of day in assessing the order. If you do not specify a value in your request, the server uses the default value for your merchant ID.                                                                                                                                |
| AppliedCV                | Indicates whether or not card verification was applied to the transaction.                                                                                                                                                                                                              |
| AppliedHostHedge         | Importance of email and IP addresses of the customer in assessing the order. If you do not specify a value in your request, the server uses the default value for your merchant ID.                                                                                                     |
| AppliedThreshold         | Score threshold applied to the order.                                                                                                                                                                                                                                                   |
| AppliedTimeHedge         | Importance of time of day in assessing the order. If you do not specify a value in your request, the server uses the default value for your merchant ID.                                                                                                                                |
| AppliedVelocityHedge     | Importance of the number of orders from the customer in a specific time period in assessing the order. If you do not specify a value in your request, the server uses the default value for your merchant ID.                                                                           |
| BinAccountType           | Type of customer.                                                                                                                                                                                                                                                                       |
| BinCountry               | Country (two-digit country code) associated with the BIN of the customer's card used for the payment.                                                                                                                                                                                   |
| BinIssuer                | Name of the bank or entity that issued the card account.                                                                                                                                                                                                                                |
| BinScheme                | Subtype of card account.                                                                                                                                                                                                                                                                |
| CodeType                 | Category of information code returned for an order.                                                                                                                                                                                                                                     |
| CodeValue                | Description of the information code returned in the `&lt;CodeType&gt;` element.                                                                                                                                                                                                         |
| ConsumerLoyalty          | Indicates whether a loyalty program is used or the number of the loyalty reward account that is used.                                                                                                                                                                                   |
| ConsumerPasswordProvided | Reserved for future use.                                                                                                                                                                                                                                                                |
| ConsumerPromotions       | Reserved for future use.                                                                                                                                                                                                                                                                |
| CookiesAccepted          | Indicates whether the customer's web browser accepts cookies. This field can contain one of the following values: * `true`: The customer's browser accepts cookies. * `false`: The customer's browser does not accept cookies.                                                          |
| CookiesEnabled           | Indicates whether cookies are enabled in the customer's browser.                                                                                                                                                                                                                        |
| DeviceFingerPrint        | Indicates whether Device Fingerprint is used.                                                                                                                                                                                                                                           |
| Factors                  | Information that affected the score of the order.                                                                                                                                                                                                                                       |
| FlashEnabled             | Indicates whether Flash is enabled in the customer's browser.                                                                                                                                                                                                                           |
| GiftWrap                 | Reserved for future use.                                                                                                                                                                                                                                                                |
| HostSeverity             | Risk associated with the customer's email domain.                                                                                                                                                                                                                                       |
| ImagesEnabled            | Indicates whether images are enabled in the customer's browser.                                                                                                                                                                                                                         |
| IPCity                   | Name of the city decoded from the IP address used directly or indirectly by the customer to send the order.                                                                                                                                                                             |
| IPCountry                | Name of the country decoded from the IP address used directly or indirectly by the customer to send the order.                                                                                                                                                                          |
| IPRoutingMethod          | Routing method decoded from the IP address used directly or indirectly by the customer to send the order.                                                                                                                                                                               |
| IPState                  | Name of the state decoded from the IP address used directly or indirectly by the customer to send the order.                                                                                                                                                                            |
| JavascriptEnabled        | Indicates whether JavaScript is enabled in the customer's browser.                                                                                                                                                                                                                      |
| LostPassword             | Reserved for future use.                                                                                                                                                                                                                                                                |
| ProductRisk              | Indicates the level of risk for the product. This field can contain one of these values: * `low`: The product is associated with few chargebacks. * `normal`: The product is associated with a normal number of chargebacks. * `high`: The product is associated with many chargebacks. |
| ProxyIPAddress           | IP address of the proxy if it is available.                                                                                                                                                                                                                                             |
| ProxyIPAddressActivities | Actions associated with the proxy IP address.                                                                                                                                                                                                                                           |
| ProxyIPAddressAttributes | Characteristics associated with the proxy IP address.                                                                                                                                                                                                                                   |
| ProxyServerType          | Type of proxy server based on the HTTP header.                                                                                                                                                                                                                                          |
| RepeatCustomer           | Reserved for future use.                                                                                                                                                                                                                                                                |
| ReturnsAccepted          | Indicates whether returns are accepted for this order. This field can contain one of these values: * `true`: Returns are accepted for this order. * `false`: Returns are not accepted for this order.                                                                                   |
| Score                    | Total score calculated for the order.                                                                                                                                                                                                                                                   |
| TimeLocal                | Local time of order.                                                                                                                                                                                                                                                                    |
| TrueIPAddress            | Customer's true IP address detected by the application.                                                                                                                                                                                                                                 |
| TrueIPaddressActivities  | Actions associated with the true IP address.                                                                                                                                                                                                                                            |
| TrueIPAddressAttributes  | Characteristics associated with the true IP address.                                                                                                                                                                                                                                    |
| TrueIPAddressCity        | City associated with the true IP address.                                                                                                                                                                                                                                               |
| TrueIPAddressCountry     | Country associated with the true IP address.                                                                                                                                                                                                                                            |
[Risk Field Names and Descriptions]

SCA Exemption Fields {#sca_exemption}
=====================================

| Field Name         | Description                                                                                                                                                                                                                                                                                                                                             |
|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCAExemption       | Reason that the transaction is exempt from strong customer authentication (SCA) requirements. Possible values: * `delegated_authentication_exemption_indicator` * `low_value_exemption_indicator` * `risk_analysis_exemption_indicator` * `secure_corporate_payment_indicator` * `trusted_merchant_exemption_indicator` {#sca_exemption_ul_fwg_3dn_hsb} |
| SCAExemptionValues | Number indicating whether the associated SCA exemption was included in the transaction. Possible values: * `0`: Not exempt * `1`: Exempt {#sca_exemption_ul_qcm_ldn_hsb}                                                                                                                                                                                |
[SCA Exemption Field Names and Descriptions]

Sender Fields {#sender}
=======================

| Field Name            | Description                                                            |
|:----------------------|:-----------------------------------------------------------------------|
| Address               | Sender address.                                                        |
| City                  | Sender city.                                                           |
| Country               | Sender country.                                                        |
| DOB                   | Sender date of birth.                                                  |
| FirstName             | Sender first name.                                                     |
| LastName              | Sender last name.                                                      |
| MiddleInitial         | Sender name middle initial.                                            |
| PhoneNumber           | Sender phone number.                                                   |
| PostalCode            | Sender postal code.                                                    |
| SenderReferenceNumber | Reference number generated by you that uniquely identifies the sender. |
| SourceOfFunds         | Source of funds.                                                       |
| State                 | Sender state.                                                          |
[Sender Field Names and Descriptions]

Settlement Fields {#settlement}
===============================

Field names in this group are prepended with the text Settlement:

| Field Name             | Description                                                                     |
|:-----------------------|:--------------------------------------------------------------------------------|
| SettlementAge          | Settlement aging.                                                               |
| SettlementAmount       | Amount that is settled for transaction.                                         |
| SettlementCurrencyCode | Currency code that is applied to settlement.                                    |
| SettlementDate         | Date on which settlement is applied.                                            |
| SourceResponseCode     | Response code that is sent from source.                                         |
| SourceResponseMessage  | Response message that is sent from source.                                      |
| Status                 | Settlement status. Possible values: * `S`: Success * `P`: Pending * `F`: Failed |
[Settlement Field Names and Descriptions]

Shipping Fields {#shipping}
===========================

Field names in this group are prepended with the text Shipping:

| Field Name | Description                           |
|:-----------|:--------------------------------------|
| Carrier    | Carrier that is used to ship product. |
| Method     | Shipping method for the product.      |
[Shipping Field Names and Descriptions]

Ship To Fields {#ship-to}
=========================

Field names in this group are prepended with the text ShipTo:

| Field Name  | Description                         |
|:------------|:------------------------------------|
| Address1    | Shipping address first line.        |
| Address2    | Shipping address second line.       |
| City        | Shipping city.                      |
| CompanyName | Name of company.                    |
| Country     | Shipping address country.           |
| FirstName   | Recipient first name.               |
| LastName    | Recipient last name.                |
| Phone       | Recipient phone number.             |
| State       | Shipping address state or province. |
| Zip         | Shipping address ZIP/postal code.   |
[Ship To Field Names and Descriptions]

Token Fields {#token}
=====================

Field names in this group are prepended with the text NetworkToken, TMSToken, or Token:

|    Group     |       Field Name       |                  Description                   |
|:------------:|:----------------------:|:----------------------------------------------:|
| NetworkToken |    NetworkTokenPAR     | Network token payment account reference (PAR). |
|   TMSToken   |       CustomerID       |            `TMS` customer token ID.            |
|   TMSToken   |  PaymentInstrumentID   |       `TMS` payment instrument token ID.       |
|   TMSToken   | InstrumentIdentifierID |     `TMS` instrument identifier token ID.      |
|   TMSToken   |   ShippingAddressID    |        `TMS` shipping address token ID.        |
|    Token     | NetworkTokenTransType  |        Network token transaction type.         |
|    Token     |       TokenCode        |            Transaction token code.             |
[Token Field Names and Descriptions]

Travel Fields {#travel}
=======================

Field names in this group are prepended with the text Travel:

| Field Name         | Description                                                       |
|:-------------------|:------------------------------------------------------------------|
| CompleteRoute      | Concatenation of individual travel legs.                          |
| DepartureDateTime  | First leg departure date and time.                                |
| JourneyType        | Type of travel.                                                   |
| Number             | Passenger number.                                                 |
| PassengerFirstName | Passenger's first name.                                           |
| PassengerEmail     | Passenger's email address, including the complete domain name.    |
| PassengerId        | Ticketed passenger ID.                                            |
| PassengerLastName  | Passenger's last name.                                            |
| PassengerPhone     | Passenger's phone number.                                         |
| PassengerStatus    | Company's passenger classification, such as frequent flyer.       |
| PassengerType      | Passenger classification associated with the price of the ticket. |
[Travel Field Names and Descriptions]

Verify Enrollment Request Fields {#verify-enrollment-request}
=============================================================

Field names in this group are prepended with the text VEReq:

| Field Name  | Description                     |
|:------------|:--------------------------------|
| AcquirerBin | Acquiring bank ID number.       |
| MerchantID  | Merchant ID.                    |
| Pan         | Customer masked account number. |
[Verify Enrollment Field Names and Descriptions]

Verify Enrollment Response Fields {#verify-enrollment-response}
===============================================================

Field names in this group are prepended with the text VERes:

| Field Name | Description                            |
|:-----------|:---------------------------------------|
| AccountID  | Account ID.                            |
| AcsUrl     | ACS URL.                               |
| Enrolled   | Indicates that enrollment is verified. |
[Verify Enrollment Response Field Names and Descriptions]

Supported Time Zones {#time-zones}
==================================

This table lists the supported values for specifying a time zone. When using the `Business Center`, select the applicable time zone from the values listed in the `Business Center` column. When sending an API request, set the field to a value listed in the API column.

| `Business Center`                                                    | API                     |
|:---------------------------------------------------------------------|:------------------------|
| Africa/Cairo - (GMT+02:00) Eastern European Time                     | `Africa/Cairo`          |
| Africa/Johannesburg - (GMT+02:00) South Africa Standard Time         | `Africa/Johannesburg`   |
| Africa/Tripoli - (GMT+02:00) Eastern European Time                   | `Africa/Tripoli`        |
| Africa/Tunis - (GMT+01:00) Central European Time                     | `Africa/Tunis`          |
| America/Anchorage - (GMT-09:00) Alaska Standard Time                 | `America/Anchorage`     |
| America/Bogota - (GMT-05:00) Colombia Time                           | `America/Bogota`        |
| America/Buenos_Aires - (GMT-03:00) Argentine Time                    | `America/Buenos_Aires`  |
| America/Chicago - (GMT-06:00) Central Standard Time                  | `America/Chicago`       |
| America/Denver - (GMT-07:00) Mountain Standard Time                  | `America/Denver`        |
| America/Edmonton - (GMT-07:00) Mountain Standard Time                | `America/Edmonton`      |
| America/Godthab - (GMT-03:00) Western Greenland Time                 | `America/Godthab`       |
| America/Halifax - (GMT-04:00) Atlantic Standard Time                 | `America/Halifax`       |
| America/Indianapolis - (GMT-05:00) Eastern Standard Time             | `America/Indianapolis`  |
| America/La_Paz - (GMT-04:00) Bolivia Time                            | `America/La_Paz`        |
| America/Los_Angeles - (GMT-08:00) Pacific Standard Time              | `America/Los_Angeles`   |
| America/Mexico_City - (GMT-06:00) Central Standard Time              | `America/Mexico_City`   |
| America/New_York - (GMT-05:00) Eastern Standard Time                 | `America/New_York`      |
| America/Noronha - (GMT-02:00) Fernando de Noronha Time               | `America/Noronha`       |
| America/Phoenix - (GMT-07:00) Mountain Standard Time                 | `America/Phoenix`       |
| America/Sao_Paulo - (GMT-03:00) Brasilia Time                        | `America/Sao_Paulo`     |
| America/St_Johns - (GMT-03:30) Newfoundland Standard Time            | `America/St_Johns`      |
| America/Vancouver - (GMT-08:00) Pacific Standard Time                | `America/Vancouver`     |
| America/Winnipeg - (GMT-06:00) Central Standard Time                 | `America/Winnipeg`      |
| Asia/Baku - (GMT+04:00) Azerbaijan Time                              | `Asia/Baku`             |
| Asia/Bangkok - (GMT+07:00) Indochina Time                            | `Asia/Bangkok`          |
| Asia/Calcutta - (GMT+05:30) India Standard Time                      | `Asia/Calcutta`         |
| Asia/Dacca - (GMT+06:00) Bangladesh Time                             | `Asia/Dacca`            |
| Asia/Dubai - (GMT+04:00) Gulf Standard Time                          | `Asia/Dubai`            |
| Asia/Hong_Kong - (GMT+08:00) Hong Kong Time                          | `Asia/Hong_Kong`        |
| Asia/Jakarta - (GMT+07:00) West Indonesia Time                       | `Asia/Jakarta`          |
| Asia/Jerusalem - (GMT+02:00) Israel Standard Time                    | `Asia/Jerusalem`        |
| Asia/Katmandu - (GMT+05:45) Nepal Time                               | `Asia/Katmandu`         |
| Asia/Kuala_Lumpur - (GMT+08:00) Malaysia Time                        | `Asia/Kuala_Lumpur`     |
| Asia/Macao - (GMT+08:00) China Standard Time                         | `Asia/Macao`            |
| Asia/Magadan - (GMT+11:00) Magadan Time                              | `Asia/Magadan`          |
| Asia/Manila - (GMT+08:00) Philippines Time                           | `Asia/Manila`           |
| Asia/Rangoon - (GMT +06:30) Myanmar Standard Time                    | `Asia/Rangoon`          |
| Asia/Riyadh - (GMT+03:00) Arabia Standard Time                       | `Asia/Riyadh`           |
| Asia/Saigon - (GMT+07:00) Indochina Time                             | `Asia/Saigon`           |
| Asia/Seoul - (GMT+09:00) Korea Standard Time                         | `Asia/Seoul`            |
| Asia/Shanghai - (GMT+08:00) China Standard Time                      | `Asia/Shanghai`         |
| Asia/Singapore - (GMT+08:00) Singapore Time                          | `Asia/Singapore`        |
| Asia/Taipei - (GMT+08:00) China Standard Time                        | `Asia/Taipei`           |
| Asia/Tbilisi - (GMT+04:00) Georgia Time                              | `Asia/Tbilisi`          |
| Asia/Tokyo - (GMT+09:00) Japan Standard Time                         | `Asia/Tokyo`            |
| Asia/Yakutsk - (GMT+09:00) Yakutsk Time                              | `Asia/Yakutsk`          |
| Atlantic/Cape_Verde - (GMT-01:00) Cape Verde Time                    | `Atlantic/Cape_Verde`   |
| Australia/Adelaide - (GMT+09:30) Australian Central Standard Time    | `Australia/Adelaide`    |
| Australia/Brisbane - (GMT+10:00) Australian Eastern Standard Time    | `Australia/Brisbane`    |
| Australia/Broken_Hill - (GMT+09:30) Australian Central Standard Time | `Australia/Broken_Hill` |
| Australia/Darwin - (GMT+09:30) Australian Central Standard Time      | `Australia/Darwin`      |
| Australia/Eucla - (GMT+08:45) Australian Western Standard Time       | `Australia/Eucla`       |
| Australia/Hobart - (GMT+10:00) Australian Eastern Standard Time      | `Australia/Hobart`      |
| Australia/Lindeman - (GMT+10:00) Australian Eastern Standard Time    | `Australia/Lindeman`    |
| Australia/Lord_Howe - (GMT+10:30) Lord Howe Standard Time            | `Australia/Lord_Howe`   |
| Australia/Melbourne - (GMT+10:00) Australian Eastern Standard Time   | `Australia/Melbourne`   |
| Australia/Perth - (GMT+08:00) Australian Western Standard Time       | `Australia/Perth`       |
| Australia/Sydney - (GMT+10:00) Australian Eastern Standard Time      | `Australia/Sydney`      |
| Europe/Amsterdam - (GMT+01:00) Central European Time                 | `Europe/Amsterdam`      |
| Europe/Athens - (GMT+02:00) Eastern European Time                    | `Europe/Athens`         |
| Europe/Belgrade - (GMT+01:00) Central European Time                  | `Europe/Belgrade`       |
| Europe/Berlin - (GMT+01:00) Central European Time                    | `Europe/Berlin`         |
| Europe/Brussels - (GMT+01:00) Central European Time                  | `Europe/Brussels`       |
| Europe/Bucharest - (GMT+02:00) Eastern European Time                 | `Europe/Bucharest`      |
| Europe/Budapest - (GMT+01:00) Central European Time                  | `Europe/Budapest`       |
| Europe/Copenhagen - (GMT+01:00) Central European Time                | `Europe/Copenhagen`     |
| Europe/Dublin - (GMT+00:00) Greenwich Mean Time                      | `Europe/Dublin`         |
| Europe/Helsinki - (GMT+02:00) Eastern European Time                  | `Europe/Helsinki`       |
| Europe/Istanbul - (GMT+02:00) Eastern European Time                  | `Europe/Istanbul`       |
| Europe/Lisbon - (GMT+00:00) Western European Time                    | `Europe/Lisbon`         |
| Europe/London - (GMT+00:00) Greenwich Mean Time                      | `Europe/London`         |
| Europe/Madrid - (GMT+01:00) Central European Time                    | `Europe/Madrid`         |
| Europe/Malta - (GMT+01:00) Central European Time                     | `Europe/Malta`          |
| Europe/Minsk - (GMT+03:00) Moscow Standard Time                      | `Europe/Minsk`          |
| Europe/Monaco - (GMT+01:00) Central European Time                    | `Europe/Monaco`         |
| Europe/Moscow - (GMT+03:00) Moscow Standard Time                     | `Europe/Moscow`         |
| Europe/Oslo - (GMT+01:00) Central European Time                      | `Europe/Oslo`           |
| Europe/Paris - (GMT+01:00) Central European Time                     | `Europe/Paris`          |
| Europe/Prague - (GMT+01:00) Central European Time                    | `Europe/Prague`         |
| Europe/Riga - (GMT+02:00) Eastern European Time                      | `Europe/Riga`           |
| Europe/Rome - (GMT+01:00) Central European Time                      | `Europe/Rome`           |
| Europe/Stockholm - (GMT+01:00) Central European Time                 | `Europe/Stockholm`      |
| Europe/Vienna - (GMT+01:00) Central European Time                    | `Europe/Vienna`         |
| Europe/Warsaw - (GMT+01:00) Central European Time                    | `Europe/Warsaw`         |
| Europe/Zurich - (GMT+01:00) Central European Time                    | `Europe/Zurich`         |
| GMT - (GMT+00:00) Greenwich Mean Time                                | `GMT`                   |
| Pacific/Auckland - (GMT+12:00) New Zealand Standard Time             | `Pacific/Auckland`      |
| Pacific/Honolulu - (GMT-10:00) Hawaii Standard Time                  | `Pacific/Honolulu`      |
| Pacific/Norfolk - (GMT+11:00) Norfolk Time                           | `Pacific/Norfolk`       |
| Pacific/Pago_Pago - (GMT-11:00) Samoa Standard Time                  | `Pacific/Pago_Pag`      |
[Time Zones]

