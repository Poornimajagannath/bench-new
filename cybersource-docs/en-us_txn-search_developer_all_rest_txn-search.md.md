Recent Revisions to This Document {#txn-revisions}
==================================================

24.03
-----

This revision contains only editorial changes and no technical updates.

24.02
-----

This revision contains only editorial changes and no technical updates.

24.01
-----

Added Supported Time Zones. See [Supported Time Zones](/docs/cybs/en-us/txn-search/developer/all/rest/txn-search/time-zones.md "").

23.04
-----

These card payment application filters are now grouped in a new filter category called Card Payments in the Transaction Search toolbar:

* ics_auth
* ics_auth_reversal
* ics_credit
* ics_bill

The descriptions of these filters have been updated in [Services Returned by the API](/docs/cybs/en-us/txn-search/developer/all/rest/txn-search/txn-applications.md "") to show the new filter category name.

23.03
-----

Updated the following:

* Added new transaction filters to [Filtering by Query Parameter](/docs/cybs/en-us/txn-search/developer/all/rest/txn-search/txn-search-intro/txn-filtering.md "").
* Removed all mentions of the QueryServlet throughout.

23.02
-----

This revision contains only editorial changes and no technical updates.

23.01
-----

Added Important notes to [Transaction Details API](/docs/cybs/en-us/txn-search/developer/all/rest/txn-search/txn-details-intro.md "") and [Retrieving a Transaction](/docs/cybs/en-us/txn-search/developer/all/rest/txn-search/txn-details-intro/txn-details-request.md "").

22.02
-----

This revision contains only editorial changes and no technical updates.

22.01
-----

Added the following:

* New transaction filters to [Filtering by Query Parameter](/docs/cybs/en-us/txn-search/developer/all/rest/txn-search/txn-search-intro/txn-filtering.md "").
* [Filtering Using the paymentInformation.paymentType Field](/docs/cybs/en-us/txn-search/developer/all/rest/txn-search/txn-search-intro/txn-filtering/txn-search-filter-paymentType-type.md "")

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE CARD PLATFORM CONNECT ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT CARD PLATFORM CONNECT ACQUIRER.

Introduction {#txn-intro}
=========================

By using the Transaction Search and Details API, you can search for and view the details of any transaction. The response payload for REST is JSON.  
For information about which services can be returned by the Transaction Search and Details APIs, see [Services Returned by the API](/docs/cybs/en-us/txn-search/developer/all/rest/txn-search/txn-applications.md "").

Transaction Search API {#txn-search-intro}
==========================================

Using the Transaction Search API, you can search for your transactions that meet specific criteria.  
To create a transaction search, your client application must send a POST request. The request body contains the details for creating the search, such as the search name, the time zone, and the parameters for the search.

Creating a Transaction Search Request {#txn-search-request}
===========================================================

Follow these steps to create a transaction search request:

1. Send a POST request to `https://&lt;url_prefix&gt;/tss/v2/searches` and include these required fields:

   #### ADDITIONAL INFORMATION

   * query
   * sort

   Use the name of the server as the `&lt;url_prefix&gt;`:

   * **Production:** `api.cybersource.com`
   * **Production in India:** api.in.cybersource.com
   * **Test:** `apitest.cybersource.com`
2. Include these optional fields:

   #### ADDITIONAL INFORMATION

   * save
   * name
   * timezone
   * offset
   * sort

For a list of supported time zones, see [Supported Time Zones](/docs/cybs/en-us/txn-search/developer/all/rest/txn-search/time-zones.md "").

Filtering by Query Parameter {#txn-filtering}
=============================================

You can use the supported API fields in the table below as query parameters in the `query` field of the search request.  
Supported operators are `AND` and `OR`.  
Use the format `field:value AND field2:value`.  
Field hierarchy uses the dotted format `object.field` or `object.field.subfield`.  
This list identifies the supported fields and how each filter can be used.  
**Query Parameters:**

applicationInformation.applications.reconciliationId OR reconciliationId
:
Transaction reference number, returned by the original transaction response.
:
Examples:

    ```
    applicationInformation.applications.reconciliationId:H74U3AD377ER921
    ```

    {#txn-filtering_codeblock_d33_wcl_byb}

    ```
    reconciliationId:H74U3AD377ER921
    ```

    {#txn-filtering_codeblock_qct_xcl_byb}

buyerInformation.merchantCustomerId
:
Your identifier for the customer.
:
Example:

    ```
    buyerInformation.merchantCustomerId:0535439670
    ```

    {#txn-filtering_codeblock_vcl_1dl_byb}

clientReferenceInformation.code
:
Client-generated order reference or tracking number. We recommend that you send a unique value for each transaction so that you can perform meaningful searches for the transaction.
:
Example:

    ```
    clientReferenceInformation.code:12345
    ```

    {#txn-filtering_codeblock_hjj_ddl_byb}

clientReferenceInformation.partner.solutionId
:
Identifier for the partner that is integrated to our platform.
:
Example:

    ```
    clientReferenceInformation.partner.solutionId:89012345
    ```

    {#txn-filtering_codeblock_bc2_gdl_byb}

deviceInformation.ipAddress
:
IP address of the customer's device.
:
Example:

    ```
    deviceInformation.ipAddress:23.45.35.29
    ```

    {#txn-filtering_codeblock_ex4_jdl_byb}

id
:
A unique identification number generated by `Cybersource` to identify the submitted request.
:
Example:

    ```
    id:6590834057836283403955
    ```

    {#txn-filtering_codeblock_qdk_ldl_byb}

installmentInformation.identifier
:
Identifier for an installment payment transaction.
:
Example:

    ```
    installmentInformation.identifier:1000000000
    ```

    {#txn-filtering_codeblock_sr2_4dl_byb}

merchantId
:
`Cybersource` merchant ID.
:
Example:

    ```
    merchantId:merchant10
    ```

    {#txn-filtering_codeblock_gfy_qdl_byb}

merchantInformation.resellerId
:
Only for reseller. Query transactions for all merchants under the reseller portfolio.
:
Example:

    ```
    merchantInformation.resellerId:1234
    ```

    {#txn-filtering_codeblock_nny_tdl_byb}

merchantInformation.accountId
:
Query transactions for one of your merchant accounts.
:
Example:

    ```
    merchantInformation.accountId:cybs_acct
    ```

    {#txn-filtering_codeblock_x5v_wdl_byb}

orderInformation.amountDetails.currency
:
ISO Standard Currency Codes. See [ISO Standard Country Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf "") for more information.
:
Example:

    ```
    orderInformation.amountDetails.currency:[USD]
    ```

    {#txn-filtering_codeblock_bk1_zdl_byb}

orderInformation.amountDetails.totalAmount
:
Grand total for the order.
:
Example:

    ```
    orderInformation.amountDetails.totalAmount:100.00
    ```

    {#txn-filtering_codeblock_oyc_b2l_byb}

orderInformation.billTo.email
:
Customer's email address.
:
Example:

    ```
    orderInformation.billTo.email:null@example.com
    ```

    {#txn-filtering_codeblock_qfj_d2l_byb}

orderInformation.billTo.firstName
:
Customer's first name. This name must be the same as the name on the card.
:
Example:

    ```
    orderInformation.billTo.firstName:John
    ```

    {#txn-filtering_codeblock_fwl_f2l_byb}

orderInformation.billTo.lastName
:
Customer's last name. This name must be the same as the name on the card.
:
Example:

    ```
    orderInformation.billTo.lastName:Doe
    ```

    {#txn-filtering_codeblock_rzs_h2l_byb}

orderInformation.billTo.phoneNumber
:
Phone number associated with the customer's billing address.
:
Example:

    ```
    orderInformation.billTo.phoneNumber:8394552567
    ```

    {#txn-filtering_codeblock_rfj_j2l_byb}

orderInformation.shipTo.phoneNumber
:
Phone number associated with the customer's shipping address.
:
Example:

    ```
    orderInformation.shipTo.phoneNumber:8394552567
    ```

    {#txn-filtering_codeblock_bvd_l2l_byb}

paymentInformation.bank.account.number
:
Full bank account number.
:
Example:

    ```
    paymentInformation.bank.account.number:1234567890
    ```

    {#txn-filtering_codeblock_jxg_n2l_byb}

paymentInformation.bank.account.prefix
:
The initial six numbers of a bank account number.
:
Example:

    ```
    paymentInformation.bank.account.prefix:1234
    ```

    {#txn-filtering_codeblock_rtw_42l_byb}

paymentInformation.bank.account.suffix
:
Last four digits of the customer's bank account number.
:
Example:

    ```
    paymentInformation.bank.account.suffix:4321
    ```

    {#txn-filtering_codeblock_lfz_q2l_byb}

paymentInformation.card.number
:
Full payment account number.
:
Example:

    ```
    paymentInformation.card.number:4111111111111111
    ```

    {#txn-filtering_codeblock_ymt_s2l_byb}

paymentInformation.card.prefix
:
Initial six numbers on a payment account number.
:
Example:

    ```
    paymentInformation.card.prefix:4111
    ```

    {#txn-filtering_codeblock_q4l_52l_byb}

paymentInformation.card.suffix
:
Last four digits of the customer's card number.
:
Example:

    ```
    paymentInformation.card.suffix:1111
    ```

    {#txn-filtering_codeblock_rwb_w2l_byb}

paymentInformation.customer.customerId
:
Unique identifier for the customer's card and billing information.
:
Example:

    ```
    paymentInformation.customer.customerId:548323
    ```

    {#txn-filtering_codeblock_wrl_y2l_byb}

paymentInformation.paymentType.method
:
Indicates the payment method used in this payment transaction. See [Filtering by Payment Type](/docs/cybs/en-us/txn-search/developer/all/rest/txn-search/txn-search-intro/txn-filtering/txn-search-filter-paymentType-type.md "") for more information.
:
Example:

    ```
    paymentInformation.paymentType.method:MC
    ```

    {#txn-filtering_codeblock_y23_1fl_byb}

paymentInformation.paymentType.type
:
Indicates the payment type used in this payment transaction. For example: credit card or check. See [Filtering by Payment Type](/docs/cybs/en-us/txn-search/developer/all/rest/txn-search/txn-search-intro/txn-filtering/txn-search-filter-paymentType-type.md "") for more information.
:
Example:

    ```
    paymentInformation.paymentType.type:credit card
    ```

    {#txn-filtering_codeblock_p23_cfl_byb}

processingInformation.commerceIndicator
:
Type of transaction. Some payment card companies use this information when determining discount rates.
:
Example:

    ```
    processingInformation.commerceIndicator:123abc
    ```

    {#txn-filtering_codeblock_mjx_dfl_byb}

processorInformation.approvalCode
:
Authorization code returned by the processor.
:
Example:

    ```
    processorInformation.approvalCode:1234
    ```

    {#txn-filtering_codeblock_cn2_gfl_byb}

processorInformation.retrievalReferenceNumber
:
Unique number that our platform generates to identify the transaction.
:
Example:

    ```
    processorInformation.retrievalReferenceNumber:122908889379
    ```

    {#txn-filtering_codeblock_prb_3fl_byb}

submitTimeUtc
:
The date and time a transaction was submitted, or a range of times. See [Filtering Using submitTimeUtc](/docs/cybs/en-us/txn-search/developer/all/rest/txn-search/txn-search-intro/txn-filtering/txn-search-filter-submitTimeUtc.md "") for more information.
:
Example:

    ```
    submitTimeUtc:[2022-05-11T03:21:03Z]
    ```

    {#txn-filtering_codeblock_rsv_jfl_byb}

{#txn-filtering_dl_icb_scl_byb}  
The following examples show several ways of using these keywords in the query parameter.

| Type of Search                                      | Example                                                                                                              |
|:----------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| Two filters, using AND.                             | "query": "clientReferenceInformation.code:1111 AND submitTimeUtc:\[NOW/DAY-1DAYS TO NOW/DAY+1DAY}"                   |
| Three values for one filter, using OR.              | "query": "clientReferenceInformation.code:(1111 OR 2222 OR 3333)"                                                    |
| Multiple filters and values, using both AND and OR. | "query": "clientReferenceInformation.code:(1111 OR 2222 OR 3333) AND submitTimeUtc:\[NOW/DAY-1DAYS TO NOW/DAY+1DAY}" |
[Keyword Query Examples]

Filtering Using the paymentInformation.paymentType Field {#txn-search-filter-paymentType-type}
==============================================================================================

The `paymentInformation.paymentType.type` field enables you to filter transactions by the payment type.  
Possible values and descriptions for paymentInformation.paymentType.type and corresponding paymentInformation.paymentType.method values:

* `bank transfer`: Bank transfer
  * `mch`: Bancontact
  * `rbt`: Bank Transfer
  * `br`: Brazil Bank Transfer
  * `blf`: Belfius
  * `co`: China Cash on Order
  * `ct`: China Bank Transfer
  * `cw`: China eWallet
  * `eps`: EPS
  * `vks`: Finland Bank Transfer
  * `gpy`: Giropay
  * `ion`: Interac Online
  * `idl`: iDeal
  * `wpb`: PayByBank
  * `kbc`: KBC
  * `pzw`: Przelewy24
  * `sof`: Sofort
  * `dbb`: Sweden Bank Transfer
    {#txn-search-filter-paymentType-type_ul_az1_fcq_r5b}
* `cash payments`: Cash payment
  * `oxo`: Oxxo
  * `mlb`: Multibanco
    {#txn-search-filter-paymentType-type_ul_gps_dcq_r5b}
* `check`: Check
  * `c`: Checking
  * `x`: Corporate Checking
  * `u`: Checking without Account Number
  * `s`: Savings
    {#txn-search-filter-paymentType-type_ul_i3k_ccq_r5b}
* `credit card`: Credit card
  * `ax`: American Express
  * `ar`: Aura Card
  * `bb`: Bebe
  * `bl`: Bill Me Later
  * `cn`: Carnet
  * `cs`: Carta Si
  * `cb`: Carte Blanche
  * `cl`: Cartes Bancaires
  * `cc`: Casual Corner
  * `cp`: China UnionPay (CUP)
  * `dk`: Dankort
  * `do`: Delta Online
  * `dc`: Diners Club
  * `di`: Discover
  * `ds`: Dick's Sportswear
  * `dn`: Disney
  * `ed`: eDiscreet
  * `el`: ELO Card
  * `en`: Encoded Account
  * `er`: EnRoute
  * `fb`: Falabella
  * `gm`: GE Capital Money UK
  * `ep`: Eftpos
  * `tc`: GE TwinPay Credit
  * `td`: GE TwinPay Debit
  * `hc`: Hipercard
  * `hd`: Home Depot Consumer
  * `hr`: Household
  * `ja`: JAL
  * `jc`: JCB
  * `jw`: Jcrew
  * `kr`: Korean Cards
  * `la`: Laser
  * `lw`: Lowe's Consumer
  * `mb`: MBNA
  * `mc`: Mastercard
  * `mg`: MagnaCash
  * `mo`: Maestro
  * `mr`: Meijer
  * `md`: Mada
  * `nc`: Nicos
  * `or`: Orico Card
  * `rc`: Redecard
  * `dp`: Pinless Debit
  * `rp`: RuPay
  * `rh`: Restoration Hardware
  * `sb`: Sam's Club Business
  * `sc`: Sam's Club Consumer
  * `sr`: Sears
  * `st`: Style Cards
  * `ua`: UATP
  * `unk`: Unknown Card
  * `ve`: Relay Electron
  * `vi`: Relay
  * `wm`: Walmart
    {#txn-search-filter-paymentType-type_ul_cqf_1cq_r5b}
* `direct debit`: Direct debit
  * `dd`: Direct Debit
  * `sdd`: Adyen SEPA Direct Debit
    {#txn-search-filter-paymentType-type_ul_lnq_ybq_r5b}
* `ewallet`: eWallet
  * `abr`: Alipay Barcode
  * `adm`: Alipay Domestic (mobile)
  * `apd`: Alipay Domestic
  * `apy`: Alipay International
  * `aym`: Alipay International (mobile)
  * `aqr`: Alipay QR Code
  * `acc`: Alipay Credit Card
  * `ctp`: Common Transaction Processing
  * `rbt`: Bank transfer
  * `mbp`: Mobile Billing
  * `vme`: V.me
    {#txn-search-filter-paymentType-type_ul_ihr_xbq_r5b}
* `gift card`: Gift card
  * `vl`: ValueLink
    {#txn-search-filter-paymentType-type_ul_okg_wbq_r5b}
* `invoice payments`: Invoice payments
  * `kli`: Klarna
  * `afm`: Affirm
    {#txn-search-filter-paymentType-type_ul_cdj_vbq_r5b}
* `paypal`: PayPal
  * `paypal`: PayPal
    {#txn-search-filter-paymentType-type_ul_wrh_rbq_r5b}
* `switch card`: Switch card
  * `so`: Solo
  * `sw`: Switch
    {#txn-search-filter-paymentType-type_ul_kv2_5bq_r5b}

Filtering Using the submitTimeUtc Field {#txn-search-filter-submitTimeUtc}
==========================================================================

The submitTimeUtc field uses date math expressions and enables you to use dates and times relative to a fixed moment, including the current time, which is represented by `NOW`.  
You can also use UNIX Epoch Time for the start and end time. For example, `submitTimeUtc:[1556712000000 TO 1556757600000]`.  
**Date Math Syntax:** Date math expressions consist of adding some quantity of time in a specified unit, or rounding the current time by a specified unit. Expressions can be joined and are evaluated left to right.  
A slash (`/`) is used to indicate rounding. `NOW/HOUR` represents the beginning of the current hour. If the current time is 4:12 p.m. (`NOW`), then `NOW/HOUR` would be the start of that hour, 4:00 p.m. Valid values in date math are:

* `DAY` or `DAYS`
* `MONTH` or `MONTHS`
* `MINUTE` or `MINUTES`

{#txn-search-filter-submitTimeUtc_ul_xhq_dbl_byb}  
**Date Math Range:** Date math supports date range searches. The syntax is `[startDate TO endDate}`.  
A square bracket (`[`) indicates that the date is included in the range; a curly bracket (`}`) indicates that the date is excluded.  
For example, to search transactions from the previous day, and the current date is May 3, 2019, `[NOW/DAY-1DAY TO NOW/DAY}` would search for transactions with a date between May 2, 2019, 12:00 AM to May 2, 2019, 11:59 PM.  
**More Examples:**

* Last hour: `[NOW/HOUR-1HOUR TO NOW/HOUR}`
* Today: `[NOW/DAY TO NOW/DAY+1DAY}`
* Yesterday: `[NOW/DAY-1DAY TO NOW/DAY}`
* Past 7 days: `[NOW/DAY-7DAYS TO NOW/DAY+1DAY}`
* Month-to-Date: `[NOW/MONTH TO NOW/DAY+1DAY}`
* Past month: `[NOW/MONTH-1MONTH TO NOW/MONTH}`
* Past 6 months: `[NOW/DAY-6MONTHS TO NOW/DAY+1DAY}`
* Past 12 months: `[NOW/DAY-12MONTHS TO NOW/DAY+1DAY]`
* Past 13 months: `[NOW/DAY-13MONTHS TO NOW/DAY+1DAY]`
  {#txn-search-filter-submitTimeUtc_ul_owb_dbl_byb}

Example: Creating a Search Request {#txn-search-example}
========================================================

Search Request

```
POST https://&lt;url_prefix&gt;/tss/v2/searches

{
  "save": "save",
  "name": "Search by Code",
  "timezone": "America/Denver",
  "query": "clientReferenceInformation.code:123456",
  "offset": "0",
  "limit": "100",
  "sort": "submitTimeUtc:desc"
}
```

Retrieving a Saved Transaction Search Request {#txn-search-retrieve}
====================================================================

To retrieve a saved transaction search, your client application must send an HTTPS GET request to the server. The format of the URL is as follows:

```
GET https://&lt;url_prefix&gt;/tss/v2/searches/{searchID}
```

| Value                  | Description                                                                                                                                                                                                    |
|:-----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \&lt;`url_prefix`\&gt; | Name of the server from which to download the report. Use one of these values: * **Production:** `api.cybersource.com` * **Production in India**: api.in.cybersource.com * **Test:** `apitest.cybersource.com` |
| `searchID`             | The ID returned in the search request response.                                                                                                                                                                |
[Transaction Search Request URL Values]

{#txn-search-retrieve_rx_txn_search_request_url_values}

Responses {#txn-search-retrieve_Id18AO80Q0RYK}
----------------------------------------------

This call can return one of the following HTTP status codes:

* `200`: Successful response.
* `404`: The specified resource is not found in the system.
* `500`: Unexpected server error.

For detailed information on the responses, including which fields are returned, see the [Transaction Search REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#transaction-search "").

Transaction Details API {#txn-details-intro}
============================================

Using the Transaction Details API, you can view the details of any transaction by its request ID. If you do not know the request ID for the transaction, you can use the Transaction Search API to retrieve it. See [Retrieving a Saved Transaction Search Request](/docs/cybs/en-us/txn-search/developer/all/rest/txn-search/txn-search-intro/txn-search-request.md "") for details.
IMPORTANT The Transaction Details API is designed to provide reports of processed transactions for a specific time period. It is not intended for use in real-time transaction processing. During exceptional periods, response times for this API may exceed 2 minutes.

Retrieving a Transaction {#txn-details-request}
===============================================

Send a GET request to the following URL, where `{id}` is the request ID of the transaction:

```
https://&lt;url_prefix&gt;/tss/v2/transactions/{id}
```

Responses {#txn-details-request_Id18AO80Q0RYK}
----------------------------------------------

This call returns one of the following HTTP status codes:

* `200`: Successful response.
* `404`: The specified resource is not found in the system.
* `500`: Unexpected server error.

For detailed information on the responses, including which fields are returned, see the [Transaction Search REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#transaction-search "").
IMPORTANT If the response is an HTTP 404 status code, retry the API call 5 minutes later, for a maximum of five tries.

Services Returned by the API {#txn-applications}
================================================

The Transaction Details API response contains an applications array that lists the services that processed the request. The table below lists all the services that can be returned by the Transaction Search and Details APIs.

| Application                     | Description                                      |
|:--------------------------------|:-------------------------------------------------|
| ics_score                       | Advanced Fraud Screen                            |
| ics_ap_auth                     | Alt Pay Authorization                            |
| ics_ap_auth_reversal            | Alt Pay Authorization Reversal                   |
| ics_ap_billing_agreement        | Alt Pay Billing Agreement                        |
| ics_ap_cancel                   | Alt Pay Cancel                                   |
| ics_ap_capture                  | Alt Pay Capture                                  |
| ics_ap_initiate                 | Alt Pay Initiate                                 |
| ics_ap_options                  | Alt Pay Options                                  |
| ics_ap_order                    | Alt Pay Order                                    |
| ics_ap_refund                   | Alt Pay Refund                                   |
| ics_ap_sale                     | Alt Pay Sale                                     |
| ics_ap_sessions                 | Alt Pay Session                                  |
| ics_ap_check_status             | Alt Pay Service Status                           |
| ics_auto_auth_reversal          | Automatic Authorization Reversal                 |
| ics_bank_transfer               | Bank Transfer                                    |
| ics_bank_transfer_real_time     | Bank Transfer Real Time                          |
| ics_bank_transfer_refund        | Bank Transfer Refund                             |
| ics_bin_lookup                  | BIN Lookup Service                               |
| ics_boleto_payment              | Boleto Payment                                   |
| ics_auth                        | Card Authorization                               |
| ics_auth_reversal               | Card Full Authorization Reversal                 |
| ics_bill                        | Card Settlement                                  |
| ics_credit                      | Card Credit                                      |
| ics_cm_action                   | Case Management Action                           |
| ics_china_payment               | China Payment                                    |
| ics_china_refund                | China Refund                                     |
| ics_auto_full_auth_reversal     | Credit Card Auto Full Authorization Reversal     |
| ics_auth_refresh                | Credit Card System Authorization                 |
| ics_credit_auth                 | Credit Card Credit Authorization                 |
| ics_risk_update                 | Customer List Modification                       |
| ics_dcc                         | DCC Lookup                                       |
| ics_dcc_update                  | DCC Update                                       |
| ics_decision                    | Decision Manager                                 |
| ics_dm_event                    | Decision Manager Events                          |
| ics_direct_debit                | Direct Debit                                     |
| ics_direct_debit_mandate        | Direct Debit Mandate                             |
| ics_direct_debit_refund         | Direct Debit Refund                              |
| ics_direct_debit_validate       | Direct Debit Validation                          |
| ics_ecp_authenticate            | Electronic Check Authenticate                    |
| ics_ecp_credit                  | Electronic Check Credit                          |
| ics_ecp_debit                   | Electronic Check Debit                           |
| ics_ecp_avs                     | Electronic Check Account Validation              |
| ics_get_masterpass_data         | Get MasterPass Data                              |
| ics_get_card_checkout_data      | Get `Relay Click to Pay`                          |
| ics_create_isv                  | Gift Certificate Creation                        |
| ics_get_isv_history             | Gift Certificate History                         |
| ics_add_value_to_isv            | Gift Certificate Increase                        |
| ics_get_isv_info                | Gift Certificate Information                     |
| ics_modify_isv                  | Gift Certificate Modification                    |
| ics_get_isv_profiles            | Gift Certificate Profiles                        |
| ics_redeem_isv                  | Gift Certificate Redemption                      |
| ics_gift_card_activation        | Gift Card Activation Service                     |
| ics_gift_card_balance_inquiry   | Gift Card Balance Inquiry Service                |
| ics_gift_card_redemption        | Gift Card Redemption Service                     |
| ics_gift_card_refund            | Gift Card Refund Service                         |
| ics_gift_card_reload            | Gift Card Reload Service                         |
| ics_gift_card_reversal          | Gift Card Reversal Service                       |
| ics_gift_card_void              | Gift Card Void Service                           |
| ics_gift_card_timeout_reversal  | Gift Card Timeout Reversal Service               |
| ics_ifs_setup                   | IFS Setup                                        |
| ics_ifs_update                  | IFS Update                                       |
| ics_incremental_auth            | Incremental Authorization                        |
| ics_ipgeo                       | IP Geolocation                                   |
| ics_oct                         | Original Credit Transaction                      |
| ics_pa_setup                    | Payer Authentication Setup                       |
| ics_pa_enroll                   | Payer Authentication Enrollment                  |
| ics_pa_validate                 | Payer Authentication Validation                  |
| ics_authentication_exemptions   | Relay Exemption Service                           |
| paypal_mip_agreement_ipn        | PayPal Billing Agreement                         |
| ics_paypal_button_create        | PayPal Button Create                             |
| ics_paypal_credit               | PayPal Credit                                    |
| ics_paypal_authorization        | PayPal Express Checkout Authorization            |
| ics_paypal_create_agreement     | PayPal Express Checkout Billing Agreement Create |
| ics_paypal_update_agreement     | PayPal Express Checkout Billing Agreement Update |
| ics_paypal_ec_order_setup       | PayPal Express Checkout Order Setup              |
| ics_paypal_auth_reversal        | PayPal Express Checkout Auth Reversal            |
| ics_paypal_ec_do_payment        | PayPal Express Checkout Do Payment               |
| ics_paypal_do_ref_transaction   | PayPal Express Checkout Do Reference             |
| ics_paypal_refund               | PayPal Express Checkout Refund                   |
| ics_paypal_do_capture           | PayPal Express Checkout Settlement               |
| paypal_ipn                      | PayPal Payment                                   |
| ics_paypal_preapproved_payment  | PayPal Preapproved Payment                       |
| ics_pin_debit_credit            | PIN Debit Credit                                 |
| ics_pin_debit_purchase          | PIN Debit Purchase                               |
| ics_pin_debit_reversal          | PIN Debit Reversal                               |
| ics_timeout_pin_debit_reversal  | PIN Debit Timeout Reversal                       |
| ics_pinless_debit               | PINless Debit                                    |
| ics_pinless_debit_validate      | PINless Debit Validation                         |
| ics_pinless_debit_reversal      | PINless Debit Reversal                           |
| ics_export                      | Product Export Verification                      |
| ics_service_fee_auth            | Service Fee Authorization                        |
| ics_service_fee_auth_reversal   | Service Fee Authorization Reversal               |
| ics_service_fee_bill            | Service Fee Settlement                           |
| ics_service_fee_credit          | Service Fee Credit Card Credit                   |
| ics_service_fee_ecp_credit      | Service Fee eCheck Credit                        |
| ics_service_fee_ecp_debit       | Service Fee eCheck Debit                         |
| ics_pay_subscription_create     | Subscription Creation                            |
| ics_pay_subscription_create_dup | Subscription Creation Duplicates                 |
| ics_pay_subscription_delete     | Subscription Delete                              |
| ics_pay_subscription_update     | Subscription Modification                        |
| ics_dav                         | Shipping Address Verification                    |
| ics_download                    | Software Download URL                            |
| ics_tax                         | Tax Calculation                                  |
| ics_timeout_auth_reversal       | Timeout Auth Reversal                            |
| ics_timeout_oct_reversal        | Timeout OCT Reversal                             |
| ics_void                        | Voided Transactions                              |
| ics_auto_void_auth_reversal     | Authorization Reversal after Void                |
| ics_pay_subscription_retrieve   | Subscription Retrieval                           |
| ics_ap_create_mandate           | Alt Pay Direct Debit - Create Mandate            |
| ics_ap_update_mandate           | Alt Pay Direct Debit - Update Mandate            |
| ics_ap_import_mandate           | Alt Pay Direct Debit - Import Mandate            |
| ics_ap_revoke_mandate           | Alt Pay Direct Debit - Revoke Mandate            |
| ics_ap_mandate_status           | Alt Pay Direct Debit - Mandate status            |
[Applications Returned by the API]

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

