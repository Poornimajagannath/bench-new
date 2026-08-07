Reporting User Guide {#concept_zlc_fkr_c2c}
===========================================

This section describes how to use this user guide and where to find further information.

Audience and Purpose
--------------------

This guide describes how to configure and manage your reports using your `Business Center` account.

Conventions
-----------

The following special statement is used in this document:

> IMPORTANT
> An *Important* statement contains information essential to successfully completing a task or learning a concept.

Customer Support
----------------

For support information about any service, visit the Support Center:  
<http://support.example.com>

Recent Revisions to This Document {#reporting-ug-recent-revisions}
==================================================================

25.10.01
--------

New Reports
:
Added Standard Monthly Fee report. For information about the report, see [Standard Monthly Fee Report](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Reports_Available_in_the_Business_Center/c_monthly-fee-details.md ""). For information about the report's fields, see [Standard Monthly Fee Fields](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Report_Fields_and_Descriptions/Fields_Descriptions_Downloadable_Reports/monthly-fee-details.md "").
:
Added Standard Billing Data Package report. For information about the report, see [Standard Billing Data Package Report](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Reports_Available_in_the_Business_Center/c_standard_billing_data_package.md ""). For information about the report's fields, see [Standard Billing Data Package Fields](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Report_Fields_and_Descriptions/Fields_Descriptions_Downloadable_Reports/standard-billing-data-package.md "").

25.09.01
--------

New Report
:
Added a Billable Transactions Detail report. For information about the report, see [Billable Transactions Detail](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Reports_Available_in_the_Business_Center/c_billing_transctions_detail.md ""). For information about the report's fields, see [Billable Transactions Detail Fields](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Report_Fields_and_Descriptions/Fields_Descriptions_Downloadable_Reports/billable-transaction-details.md "").

25.01
-----

This revision contains only editorial changes and no technical updates.

24.04
-----

Strong customer exemption (SCA) fields
:
Added requirements for strong customer exemption (SCA) for `HSBC`. See [SCA Exemption Fields](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Report_Fields_and_Descriptions/Fields_Descriptions_Downloadable_Reports/c_SCA_Exemption_Fields.md "").

24.03
-----

Reporting Fields
:
Added new report fields for `Token Management Service`. See [Token Fields](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Report_Fields_and_Descriptions/Fields_Descriptions_Downloadable_Reports/c_Token_Fields.md "").

24.02
-----

Creating and Accessing Downloadable Reports
:
Removed cross-references to Reporting Migration Guide and Servlet to REST Migration Guide which no longer exists.
:
See [Creating and Accessing Downloadable Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports.md "") and [Related Information](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Get_Started_with_Business_Center_Reporting/c_Related_Information.md "").

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.

Getting Started with `Business Center` `Reports` {#ID-0000004a}
===============================================================

Several reports are automatically enabled for you during the onboarding process, so it is easy to get started with `Business Center` reporting. You can use the Standard reports as is or you can customize them to fit your needs.  
Merchant accounts created in the `Business Center` before May 2019 are not auto-enabled for Standard reports. For information on enabling these reports, see [Subscribing to Standard Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Subscribing_to_Standard_Reports.md "").  
The `Business Center` offers several reporting options for you to access and download your transaction data:

* Standard reports---Track and reconcile your payment activity.
* Custom reports---Use building blocks to create reports for your specific needs.
* Specialized reports---Track and review how you use additional services such as `Decision Manager`, Account Updater, and Tax Calculation.

These reports are available on the `Available Reports` page. Each report contains specific fields to help you understand your transaction data:

* [Transaction Request](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Reports_Available_in_the_Business_Center/c_Transaction_Request.md "")---Daily transaction level report that shows details related to individual transactions. Logs all of your `Business Center` payment gateway activity.
* [Payment Batch Detail](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Reports_Available_in_the_Business_Center/c_Payment_Batch_Detail.md "")---Daily transaction level report that shows all of your sales and refunds that were submitted to your payment processor through the `Business Center`. Tracks which of your transactions have been settled.
* [Payment Events](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Reports_Available_in_the_Business_Center/c_Payment_Events.md "")---Daily transaction level report that shows payment notifications received from your payment processor (for selected processors). Tracks information related to your transactions such as payment notifications and exceptions.
* [Payment Batch Summary](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Reports_Available_in_the_Business_Center/c_Payment_Batch_Summary1.md "")---Summary level report that shows the quality and amount of your sales and refunds by currency and payment method.

To learn more about generating and downloading reports, see:

* [Reports Available in the `Business Center`](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Reports_Available_in_the_Business_Center.md "")---Provides a complete list of all reports available in the `Business Center`, including what each report contains, how to find it, and who can use it.
* [Creating and Accessing Downloadable Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports.md "")---Provides information about downloadable reports, including instructions for creating standard and custom reports.
* [Viewing On-Demand Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Viewing_On-Demand_Reports.md "")---Provides information about reports you can generate on demand.

Related Information {#ID-0000006e}
==================================

To get started using the Reporting API to download your data for use in other business systems, see the [Developer Center](https://developer.cybersource.com/ "").

Creating and Accessing Downloadable Reports {#ID-0000007e}
==========================================================

The `Business Center` generates and stores reports to which you subscribed on the Available Reports page. These reports include standard, preconfigured reports that you enabled and any custom reports you created. For a list of fields and descriptions you can include in downloadable reports, see [Report Fields and Descriptions](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Report_Fields_and_Descriptions.md "").  
Partners and account-level users can also create reports that consolidate data for one or all merchants, or a selected group of merchants, in their portfolios.  
Some merchants, including those processing alternate payment methods, may have access to financial data. For more information about these types of reports, see [Financial and Reconciliation Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Financial_and_Reconciliation_Reports.md "").

How and When Reports Are Generated {#ID-0000008a}
=================================================

You can choose one or both of the following options to create downloadable reports:

* Choose to have your reports built on a regular frequency, such as every day or every week. For example, create a subscription for a daily report covering transactions between 5 p.m. and 5 p.m. The `Business Center` automatically generates the report daily.
* Create as-needed reports to review your transaction history. For example, configure a one-time (as-needed) report that includes all refund transactions in the month of March 2019. The `Business Center` immediately begins building the report.

Downloadable reports are created asynchronously, so they are not available immediately after you create them. As soon as the report is generated, the `Business Center` adds it to the list of `Available Reports` that you can download. For more information, see [Downloading `Available Reports`](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Downloading_Available_Reports.md "").

Report Frequency and Start Time {#ID-00000092}
==============================================

Report frequency and start time determine the contents of a report. When the report runs, it uses the start time and frequency to determine the ending time for transactions included in the report. The frequency controls how often your report is generated. For example:

* A daily report scheduled to start at 5:00 p.m. Pacific Time runs every day and contains transactions that occurred between 5:00 p.m. the previous day and 4:59 p.m. Pacific Time of the current day, every day. A daily report that runs at 5:00 p.m. on February 2 includes transactions for February 1, 5:00 p.m., through February 2, 4:59 p.m.
* A weekly report scheduled to start at 11:00 a.m. Eastern Time on a Monday contains transactions from the previous 7 days that occurred between 11:00 a.m. on the first day of the time period and 10:59 a.m. on the last day. A weekly report that runs at 11:00 a.m. on February 13 includes transactions for February 6, 11:00 a.m., through February 13, 10:59 a.m.
* A monthly report scheduled to start at 6:00 a.m. Pacific Time on the 1st will contain transactions from the previous 28-31 days that occurred between 6:00 a.m. on the first day of the time period and 5:59 a.m. on the last day. A monthly report that runs at 6:00 a.m. on February 1 includes transactions for January 1, 6:00 a.m., through February 1, 5:59 a.m.

Report Generation Date and Time {#ID-0000009a}
==============================================

The generation date and time of a report varies depending on the amount of time it takes to generate the report. Recurring daily reports for merchants are generated and available for download within six hours of the start time. For example:

* A daily report that spans 5:00 p.m. to 4:59 p.m. might have a generate time of 7:00 p.m.
* A daily report that spans 11:00 p.m. to 10:59 p.m. might have a generate time of 1:00 a.m. the following day.

The exact amount of time that is needed to generate a recurring daily report varies based on the size of the report and the load on the system. Weekly, monthly, as-needed reports, or reports for partners, might take longer than six hours to generate.  
A report's *generate date* reflects the actual date the report is created. The report's *date range* reflects the period of time the report data covers. For example, you can generate a report on:

* May 4, which includes transactions processed between January 1 and January 31.
* February 1, which includes transactions processed between January 1 and January 31.
* May 4, which includes transactions processed only on May 1.

The batch time set in the Production environment is based on your merchant configuration. The batch time set in the Test environment is 12:00 am Pacific Time and cannot be changed.

Service Level Targets for Generating Reports {#ID-000000ab}
===========================================================

Recurring daily reports for merchants are expected to generate within six hours of the start time. For example, if a report starts at 1:00 a.m., it should be available for download by 7:00 a.m.  
Reports for account-level users and partners, weekly and monthly reports, and as-needed reports may take longer to generate, based on the amount of data in the report.

File Retention and Lookback Range Information {#ID-000000ae}
============================================================

File retention period and lookback range vary by report type. Contact your `Cybersource` representative for more information.

Downloading `Available Reports` {#ID-000000fa}
==============================================

You can download any report after the `Business Center` completes the request and makes your file available. Daily, recurring reports are available for download within six hours of the report start time. Weekly, monthly, and one-time reports might take longer than six hours to generate.

Downloading Available Reports {#ID-000000fc}
============================================

1. On the left navigation pane, click the Reporting icon.
2. Under Downloadable Reports, click `Available Reports`. The `Available Reports` page appears.
3. Click the tab containing the report you want to download.
4. In the Download column, click the file format link. Only reports that have successfully completed generating and contain data include links.
5. Follow your browser's instructions to open and save the file.

Using Keyword Filters to Locate Reports {#ID-0000010c}
======================================================

Use the Keyword filter in the search toolbar to filter the contents on the `Available Reports` page. When you enter a string into the keyword filter, the `Business Center` searches across all columns on the screen.  
**Example**: Enter "18" in the Keyword filter to locate any report with "18" in the Report Name, Generate Date, or Date Range fields.  
**Example**: Enter "batch" in the Keyword filter to locate any report with "batch" in the Report Name or Report Type fields.

One-Time Reports {#ID-00000112}
===============================

The `Business Center` enables you to create your one-time reports, which are useful when:

* You need information about transactions that occurred before you set up your recurring subscription.
* You want to test a report before setting up a recurring subscription.
* You need a particular type of information only one time, making a recurring subscription unnecessary.
* When you need information from before the previous 31 days, you can create multiple one-time reports. In order to protect system performance, each user is able to generate up to three one-time reports concurrently. Additional one-time reports can be scheduled after the first three reports are generated.

{#ID-00000112_intro-2}  
After your one-time report is generated, it is available to download on the `Available Reports` page. Depending on the size of the report, it can take longer than six hours to generate.  
The process for creating a report subscription is the same as for creating a one-time report. You can create a one-time report using the following steps. To create a custom subscription, see [Creating New Custom Report Subscriptions](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports/c_Creating_New_Custom_Report_Subscriptions.md "").

Generating a One-Time Report {#ID-0000011f}
===========================================

1. On the left navigation pane, click the Reporting icon.{#ID-0000011f_step-1}
   {#ID-0000011f_step-1}

2. Under Downloadable Reports, click `Available Reports`.  
   The `Available Reports` page appears. {#ID-0000011f_step-2}
   {#ID-0000011f_step-2}

3. On the Custom Reports tab, click Create Report.  
   The Create Report Subscription page appears. {#ID-0000011f_step-3}
   {#ID-0000011f_step-3}

4. ***Account level (partner) users only:***Under Account Setup, choose if the report data is retrieved from a merchant or a group of merchants. Then choose an available value in the Merchants or Groups list or use the default value to include all merchants or groups.  
   For more information about groups, see "Manage Groups" in the online help. {#ID-0000011f_step-4.1}
   {#ID-0000011f_step-4}

5. Under Basic Report Setup, enter this field information:

   | In this field | Do this                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   |:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | Report Name   | Enter the name for your report that best reflects the data you want to capture. Each report must have a unique name containing up to 250 characters.                                                                                                                                                                                                                                                                                                                                                                            |
   | Report Type   | Select the type of report that most closely represents the data or process you want to include. For more information about report types, see ["Reports Available in the Business Center."](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Reports_Available_in_the_Business_Center.md "") The `Business Center` automatically includes the most commonly used fields in your report based on this selection. See the next step for more information on how to customize these values. |
   | File Format   | Choose whether the `Business Center` creates the report in XLS or XML format.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | Frequency     | Choose **One-time** . To create a recurring report subscription, see [Subscribing to Standard Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Subscribing_to_Standard_Reports.md "").                                                                                                                                                                                                                                                 |

   {#ID-0000011f_step-5}
   {#ID-0000011f_step-5}

6. To change any of the default fields included in your report, click the Arrow icon to expand the Advanced Report Features section. Then perform one or more of these actions. The available actions depend on the report type and format you choose:

   | In this field or tab | Do this                                                                                                                                                                                                                                                                                                                                                                                                              |
   |:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | Credit Amounts       | Check the box if you want credits to appear as negative amounts. For example: -1390.00.                                                                                                                                                                                                                                                                                                                              |
   | Naming Convention    | Select how you want the field names to appear in the report: * **Simple Order API** displays most of the field names in your report in camel case. For example: FirstName * **SCMP** displays most of the field names in your report with underscores. For example: first_name                                                                                                                                       |
   | Application          | Select one or more types of transactions you want to include in the report. Leave blank to include all types.                                                                                                                                                                                                                                                                                                        |
   | Connection Method    | Select one or more connection methods used to perform the transaction that you want to include in the report. Leave blank to include all types. Available only for reports that include the Source field.                                                                                                                                                                                                            |
   | Payment Channel      | Select one or more payment channels used to perform the transaction that you want to include in the report. Leave blank to include all types.                                                                                                                                                                                                                                                                        |
   | Field Selection      | One or more of the following: * Enter text matching a field name you want to find in the Search field. * Check the box for one or more fields or field types to include or remove from the report; check the Select All box to add or remove all fields.  Click the Arrow icon in a section to expand or collapse it. In the Selected column, click the Delete icon to remove a field or field type from the report. |
   | Field Ordering       | Click and hold the Handle icon to rearrange fields in the Selected column on the Field Selection tab into the order in which you want them to appear in the report. This option is only available for CSV output. XML field ordering cannot be guaranteed.                                                                                                                                                           |

   {#ID-0000011f_step-6}
   {#ID-0000011f_step-6}

7. When you are done, click Create.  
   The `Available Reports` page displays and the new report appears in the Custom Reports List. {#ID-0000011f_step-7}
   {#ID-0000011f_step-7}

Subscribing to Standard Reports {#ID-0000019c}
==============================================

You can enable or disable a subscription for any standard report. You can also change the frequency and output format of any standard report. The `Business Center` automatically generates reports for enabled subscriptions and makes them available on the Available Reports page.  
To save a standard report as a template, click Save As to create a new custom report. You can change the report details of the new report, including subscription cycle and included data. For more information, see [Creating New Custom Report Subscriptions](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports/c_Creating_New_Custom_Report_Subscriptions.md "").

Modifying a Standard Report Subscription {#ID-000001a2}
=======================================================

1. On the left navigation pane, click the Reporting icon.
2. Under Downloadable Reports, click Report Subscription Management. The Report Subscription Management page appears.
3. Click the Standard Report Subscriptions tab. The Standard Report Subscriptions List appears.
4. Select one or more of the following:
   * In the Enable column, select the box to activate the subscription; deselect the box to inactivate it.
   * In the Frequency column, click the Down Arrow icon to modify how often the report is generated.
   * In the Format column, click the Down Arrow icon to modify the file format of the report.

* Click Save As to create a new version of the report. For more information, see [Saving Existing Reports as New Subscriptions](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports/Saving_Existing_Reports_as_New_Subs.md "").

Generating Reports for Multi-Currency Transactions {#ID-000001c0}
=================================================================

Multi-currency transactions involve a conversion of funds from the currency in which the transaction is processed to the currency actually deposited in the merchant's account. Multi-currency reporting includes exchange rate conversion data so you can reconcile the multi-currency transaction with the corresponding deposit.  
You can create reports in the `Business Center` that include the original and local amounts for each transaction, and the exchange rate applied, by modifying the standard Funding Detail report. When you modify the Funding Detail report, it becomes a new custom report subscription.  
Only some acquirers provide multi-currency data. Contact Customer Support to determine if your payment processor supports this feature.

Creating a Multi-currency Report Subscription {#ID-000001c4}
============================================================

1. Follow the steps in [Subscribing to Standard Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Subscribing_to_Standard_Reports.md "") to locate the Funding Detail Report standard report subscription.

2. Click the Save As icon. The Save As New Subscription page appears.

3. Click the Standard Report Subscriptions tab. The Standard Report Subscriptions List appears, and the Report Type list displays `Funding Detail Report`.

4. Enter a unique report name, and select the frequency and output for your report.  **Global Payment (GPN) merchants** : Because multi-currency data are not delivered to the `Business Center` before the 5:00 p.m. report generation time, be sure to select the 11:00 p.m. option in the Subscription Start Time list.

5. In the Advanced Report Features section, click the down arrow. The panel expands.

6. On the Field Selection tab, scroll down to the Funding fields section, then click the down arrow to expand the section.

7. Add the following Funding fields to the report:

   #### ADDITIONAL INFORMATION

   * Exchange Rate
   * Exchange Rate Date
   * Local Amount
   * Local Currency
   * Original Amount
   * Original Currency
8. Click Save As. The Report Subscription Management page appears.

9. To view the new report, click the Custom Report Subscription tab.

Creating Custom Reports {#ID-000001f0}
======================================

The `Business Center` enables you to create your own reports based on the type of data you want to track such as authorizations, sales, or refunds. When you create a report subscription, the `Business Center` provides a default set of fields for you to choose from. You can also add and remove additional fields based on your needs, choose the order in which they appear, and how they display in the report. For a list of fields and descriptions, see [Report Fields and Descriptions](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Report_Fields_and_Descriptions.md "").  
You can also set how often you want to generate the custom report (one-time or recurring). Successfully generated reports appear on the `Available Reports` page. To create a custom report subscription, you can create a brand new subscription or save an existing standard or custom report as a new report.

New Custom Report Subscriptions {#ID-000001f4}
==============================================

A recurring report subscription is a template that describes the attributes of a report, including how often it runs and the period of time it spans. After your recurring report is generated, it is available for download on the `Available Reports` page. You can maintain up to 20 report subscriptions at any time.  
In addition to choosing from available fields, you can customize the following attributes of a recurring subscription:

* **Name**: a unique name for the report. The name cannot be changed after a report is created.
* **Report type**: a set of reports that can be customized. The report type cannot be changed after a report is created.
* **Format**: the format of a generated report (XML or CSV).
* **Frequency**: the frequency at which a report runs (daily, weekly, or monthly).
* **Start time**: the time of day at which a report runs.

The process for creating a report subscription is the same as for creating a one-time report. You can create recurring subscriptions using the following steps. To generate a one-time report, see [Generating One-Time Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Generating_One-Time_Reports.md "").

Creating a Custom Report Subscription {#ID-00000208}
====================================================

1. On the left navigation panel, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-reports.svg/jcr:content/renditions/original) Reports \&gt; Downloadable Reports \&gt; Report Subscription Management.  
   The Report Subscription Management page appears. {#ID-00000208_custom-1}
   {#ID-00000208_custom-1}

2. Click the Custom Report Subscriptions tab. The Custom Reports Subscriptions List appears.{#ID-00000208_custom-3}
   {#ID-00000208_custom-3}

3. Click Create Subscription. The Create Report Subscription page appears.{#ID-00000208_custom-4}
   {#ID-00000208_custom-4}

4. **Account level (partner) users only:** Under Account Setup, select whether to base the report on data from a specific merchant or a group of merchants; then choose an available value in the Merchants or Groups list or use the default value to include all merchants or groups.{#ID-00000208_custom-5}
   {#ID-00000208_custom-5}

5. Under Basic Report Setup, enter this field information:

   #### ADDITIONAL INFORMATION {#ID-00000208_custom-6-intro}

   {#ID-00000208_6-table-entry2}

   | In this field | Do this                                                                                                                                                                                                                                                                                                                        |
   |:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | Report Name   | Enter the name for your report that best reflects the data you want to capture. Each report must have a unique name containing up to 250 characters.                                                                                                                                                                           |
   | Report Type   | Select the type of report that most closely represents the data or process you want to include. The `Business Center` automatically includes the most commonly used fields in your report based on this selection. See the next step for more information on how to customize these values.                                    |
   | File Format   | Choose whether the `Business Center` creates the report in XLS or XML format.                                                                                                                                                                                                                                                  |
   | Frequency     | Choose Recurring subscription to automatically generate daily, weekly, or monthly reports. To create a one-time report, see [Generating One-Time Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Generating_One-Time_Reports.md ""). |

{#ID-00000208_custom-6}
6. To change any of the default fields included in your report, click the Arrow icon to expand the Advanced Report Features section, and then perform one or more of the these actions. The available actions are dependent on the report type and format you select:

#### ADDITIONAL INFORMATION {#ID-00000208_custom-7}

| In this field or tab | Do this                                                                                                                                                                                                                                                                                                                                                                                                             |
|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Credit Amounts       | Check the box if you want credits to appear as negative amounts (for example: -1390.00).                                                                                                                                                                                                                                                                                                                            |
| Naming Convention    | Select how you want the field names to appear in the report: * **Simple Order API** displays most field names in camel case (for example: FirstName) * **SCMP API** displays most field names with underscores (for example: first_name)                                                                                                                                                                            |
| Application          | Select one or more types of transactions you want to include in the report. Leave blank to include all types.                                                                                                                                                                                                                                                                                                       |
| Connection Method    | Select one or more connection methods used to perform the transaction that you want to include in the report. Leave blank to include all types. Available only for reports that include the Source field.                                                                                                                                                                                                           |
| Payment Channel      | Select one or more payment channels used to perform the transaction that you want to include in the report. Leave blank to include all types.                                                                                                                                                                                                                                                                       |
| Field Selection      | One or more of the following: * Enter text matching a field name you want to find in the Search field. * Check the box for one or more fields or field types to include or remove from the report; check the Select All box to add or remove all fields. Click the Arrow icon in a section to expand or collapse it. In the Selected column, click the Delete icon to remove a field or field type from the report. |
| Field Ordering       | Click and hold the Handle icon to rearrange fields (in the Selected column on the Field Selection tab) into the order in which you want them to appear in the report. This option is only available for CSV output. XML field ordering cannot be guaranteed.                                                                                                                                                        |

{#ID-00000208_custom-7}
7. When you are done, click Create. The Manage Report Subscription page appears and the new subscription appears in the Custom Reports Subscriptions List.{#ID-00000208_custom-8}
{#ID-00000208_custom-8}

Saving Existing Reports as New Subscriptions {#ID-00000285}
===========================================================

You can choose to save any existing custom report as a new report. This option enables you to copy all the existing values into the new report and to change them to create a new report with a new name.

Creating a New Report or Subscription Based on an Existing Report {#ID-00000287}
================================================================================

1. On the left navigation pane, click the Reporting icon.

2. Under Downloadable Reports, click Report Subscription Management. The Report Subscription Management page appears.

3. Click the Custom Report Subscriptions tab. The Custom Reports Subscriptions List appears.

4. Next to the report you want to copy, click the Save As icon. The Save New Subscription page appears.

   #### ADDITIONAL INFORMATION

   Under Account Setup, select whether to base the report on data from a specific merchant or a group of merchants, then choose an available value in the Merchants or Groups list. To create a report that includes all merchants or groups, use the default value.

5. Under Basic Report Setup, enter a unique name for the report.

6. You must change at least one attribute or field to save the new report. Use the steps in [Creating New Custom Report Subscriptions](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports/c_Creating_New_Custom_Report_Subscriptions.md "") as a guideline for modifying report values.

7. When you are done, click Save As. The Manage Report Subscription page appears and the new report appears in the Custom Reports Subscriptions List.

Modifying Custom Report Subscriptions {#ID-000002a0}
====================================================

You can edit the values in a custom report (except the report name and frequency), or delete subscriptions you no longer need. You can also create a new report based on an existing subscription. For more information, see [Saving Existing Reports as New Subscriptions](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports/Saving_Existing_Reports_as_New_Subs.md "").

Edit Report Subscriptions {#ID-000002a4}
========================================

1. On the left navigation pane, click the Reporting icon.
2. Under Downloadable Reports, click Report Subscription Management. The Report Subscription Management page appears.
3. Click the Custom Report Subscriptions tab. The Custom Reports Subscriptions List appears.
4. In the row containing the report you want to edit, click the Edit icon. The Edit Report Subscription page appears.
5. You must change at least one attribute or field to save the report. Use the steps in [Creating New Custom Report Subscriptions](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports/c_Creating_New_Custom_Report_Subscriptions.md "") as a guideline for modifying report values.
6. When you are done, click Edit.
7. Click Confirm. The Custom Report Subscriptions list refreshes with the edits you made applied.

Deleting Report Subscriptions {#ID-000002bb}
============================================

1. On the left navigation pane, click the Reporting icon.
2. Under Downloadable Reports, click Report Subscription Management. The Report Subscription Management page appears.
3. Click the Custom Report Subscriptions tab. The Custom Reports Subscriptions List appears.
4. In the row containing the report you want to delete, click the Delete icon.
5. Click Confirm. The Custom Report Subscriptions list refreshes and removes the subscription.

Configuring Payment Batch Detail Report Batch Times {#ID-000002cd}
==================================================================

You can use the Payment Batch Detail report to monitor the batch submission process and help predict your cash flow/funding timing. The batch date and time represents the date and time that the `Business Center` batched the transactions to the processors.  
To ensure that the report contains the most recently batched transactions, schedule the report to begin an hour or two after your daily batch end time. You can also choose to schedule multiple Payment Batch Detail reports to suit your needs.  
There are nuances to consider when scheduling your Payment Batch Detail report because the report contains transactions with a batch date and time that occur within the given interval.  
For some merchants, the batch cut-off time may occur after the end of the logical business day. For example:

* Your logical business day begins at 9:00 a.m. Pacific Time.
* Your logical business day ends at 6:00 p.m. Pacific Time.
* Your batch end time is 7:00 p.m. Pacific Time.

In this situation, it would be useful to schedule the report to begin at 8:00 p.m. Pacific Time so that it contains the transactions batched from the logical business day.  
For other merchants, the batch cut-off time may occur within the logical business day. For example:

* Your logical business day begins at 9:00 a.m. Eastern Time.
* Your logical business day ends at 11:59 p.m. Eastern Time.
* Your batch cut-off time is 9:00 p.m. Eastern Time.

In this situation, transactions from your logical business day will span two batches. Some transactions will be in the batch at 9:00 p.m. and others will be in the next day's batch. You might want to schedule your report to begin at 10:00 p.m. Eastern Time because transactions with a batch date after 10:00 p.m. Eastern Time appear on the following day's batch and report, You can also choose to schedule multiple Payment Batch Detail reports to suit your needs.  
For some merchants, the batch date will occur one calendar day after the transactions occur.  
Sometimes a transaction request date is different from the batch date. For example:

* May 1, 9:00 a.m. Eastern Time---a sale is authorized.
* May 3, 9:00 p.m. Eastern Time---the sale is captured (settled).
* May 4, 1:00 a.m. Eastern Time---The `Business Center` receives acknowledgment from the processor that the sale batched successfully.

In this situation, transactions that are captured on May 3 have a batch date of May 4.

Available Report XSDs {#ID-000002ea}
====================================

The following reports have XSDs to validate downloaded reports. Each report contains both a set of common fields (located here: [`https://api.cybersource.com`/reporting/v3/xsds/Common](https://api.cybersource.com/reporting/v3/xsds/Common "")) as well as fields specific to the report:

* `Decision Manager` Detail: [`https://api.cybersource.com`/reporting/v3/xsds/DecisionManagerDetailReport](https://api.cybersource.com/reporting/v3/xsds/DecisionManagerDetailReport "")
* Payment Batch Detail: [`https://api.cybersource.com`/reporting/v3/xsds/BatchDetailReport](https://api.cybersource.com/reporting/v3/xsds/BatchDetailReport "")
* Transaction Request: [`https://api.cybersource.com`/reporting/v3/xsds/TransactionRequestReport](https://api.cybersource.com/reporting/v3/xsds/TransactionRequestReport "")
* Processor Events Detail:  [`https://api.cybersource.com`/reporting/v3/xsds/EventDetailReport](https://api.cybersource.com/reporting/v3/xsds/ExceptionDetailReport "")
* Transaction Exception Detail:  [`https://api.cybersource.com`/reporting/v3/xsds/ExceptionDetailReport](https://api.cybersource.com/reporting/v3/xsds/ExceptionDetailReport "")

All other reports continue to use DTD format.

Viewing On-Demand Reports {#ID-00000305}
========================================

The `Business Center` includes several on-demand reports that you can view in your browser, depending on which services you use. You select the date range (lookback range) and associated data to view, and the `Business Center` generates the report for you. You can export the results of any on-demand report. You can also generate downloadable reports, including setting up your own subscriptions and custom reports. For more information, see [Creating and Accessing Downloadable Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports.md "").  
For information about all reports available in the `Business Center`, see [Reports Available in the `Business Center`](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Reports_Available_in_the_Business_Center.md "").

Lookback Range Periods for On-Demand Reports {#ID-0000030a}
===========================================================

Lookback range varies by report type. Contact your `Cybersource` representative for more information.

Payment Batch Summary {#ID-00000346}
====================================

The Payment Batch Summary report shows total sales and refunds by currency and payment method. For record-level reporting, see [Payment Batch Detail](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Reports_Available_in_the_Business_Center/c_Payment_Batch_Detail.md ""). By default the report includes data for one day but you can choose to view data by the week or month. The data can be exported to either a CSV or PDF file.

Viewing the Payment Batch Summary Report {#ID-0000034a}
=======================================================

1. On the left navigation panel, choose Reporting \&gt; Payment Batch Summary.  
   The Payment Batch Summary Report page appears. {#ID-0000034a_step-1}
   {#ID-0000034a_step-1}

2. In the search toolbar, choose the Frequency filter that you want to include in the report.{#ID-0000034a_step-3}
   {#ID-0000034a_step-3}

3. **Portfolio** users: select the Merchant for whom you want to view data. **Account level** users: select a Merchant to filter by an individual merchant instead of by account values.{#ID-0000034a_step-4}
   {#ID-0000034a_step-4}

4. Depending on the frequency you chose, select the specific day, week, or month you want to review.

   #### ADDITIONAL INFORMATION {#ID-0000034a_step-5}

   Only months that have already occurred in the current year display in the month list. To view all months of a previous year, choose the year first, then choose the desired month. To view results from the period prior to or following the chosen period, click Previous or Next below the search toolbar.
   {#ID-0000034a_step-5}

5. Choose the currency code of the transactions you want to include.{#ID-0000034a_step-6}
   {#ID-0000034a_step-6}

6. Click Export and choose your desired aggregation options and file format. Export options are determined by the frequency you chose.{#ID-0000034a_step-7}
   {#ID-0000034a_step-7}

7. Follow your web browser's instructions to open and save the file.{#ID-0000034a_step-8}
   {#ID-0000034a_step-8}

Payer Authorization Summary {#ID-00000367}
==========================================

You can generate the Payer Authorization Summary report to track enrollment and validation services performance. The report includes the number of transactions and total amount for groups of transactions based on each currency and card type you support. Use the information to estimate how your transactions are screened by payer authentication: successful, attempted, or incomplete. By default, the report includes one data for one day, but you can also choose to view by the week or month.

Viewing the Payer Authorization Summary Report {#ID-00000369}
=============================================================

1. In the left navigation panel, click the Reporting icon.
2. Under `Transaction Reports`, click Payer Auth Summary. The Payer Auth Summary Report page appears.
3. In the search toolbar, select the Date Range you want to include in the report. Account level users must select a merchant as well.
4. Based on the Date Range selected, choose the specific day, week, or month you want to review.   Only months that have already occurred in the current year display in the Month list. To view all months of a previous year, select the year first, then choose the desired month.   To view results from the period prior to or following the selected period, click Previous or Next below the search toolbar.

Notification of Change {#ID-00000379}
=====================================

You can view a list of `eCheck`-related values updated as a result of a response to an `eCheck` settlement transaction in the Notification of Change report. Merchants who have an active PGP key can also export this information to a CSV or XML file. By default, the report shows data from the prior day, but you can choose to view by the previous week or month, or by using a custom date range (up to 6 months).

Viewing the Notification of Change Report {#ID-0000037b}
========================================================

1. In the left navigation panel, click the Reporting icon.
2. Under `Transaction Reports`, click Notification of Change. The Notification of Change page appears.
3. In the search toolbar, select the Date Range of transactions to be included in the report. Results are automatically sorted to display **Latest Results First**.
4. To change the view, select Oldest Results First in the Sort Order filter.
5. Click Export and choose your desired file format.   Export is available only if you have a PGP security key.
6. Follow your browser's instructions to open and save the file.

Purchase and Refund Details {#ID-00000390}
==========================================

The Purchase and Refund report includes all purchases and refund transactions, as well as all activities related to transactions resulting in an adjustment to the net proceeds. By default the report shows data from the prior day, but you can choose to view by the previous week or month, or by using a custom period of time (up to 31 days within the previous 18 months).  
Additionally, you can view data by either:

* **Request date**: date the transaction was captured.
* **Submission date**: date on which the transaction was sent to the processor (can be later than request date).

This report is only available for selected merchants. For more information about the Purchase and Refund Details report, refer to [Financial and Reconciliation Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Financial_and_Reconciliation_Reports.md "").

Viewing the Purchase and Refund Details Report {#ID-0000039c}
=============================================================

1. In the left navigation panel, click the Reporting icon.

2. Under Financial Reports, click Purchase \& Refund Details. The Purchase \& Refund Details page appears.

3. In the search toolbar, select:

   #### ADDITIONAL INFORMATION

   * **Merchant** data you want to view.
   * **Date Range** you want to include in the report.
   * **View By** and choose which date on which to base the report.
4. Click one of the following tabs to view data details:

   #### ADDITIONAL INFORMATION

   * Request
   * Settlement
   * Authorization
   * Fees \& Funding
   * Others
5. For any transaction, click the Request ID link to view the Transaction Details page.

6. Click Export to download a file containing transactions in the list, then choose desired format.

7. Follow your browser's instructions to open and save the file.

Fields in the Chargeback Report {#ID-00000421}
==============================================

For descriptions and mapping details about Chargeback report fields, see [Fields and Descriptions for Downloadable Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Report_Fields_and_Descriptions/Fields_Descriptions_Downloadable_Reports.md "").

| Field Name                 |
|:---------------------------|
| RequestId                  |
| TrackingNumber             |
| MerchantName               |
| CyberSourceId              |
| ProcessorMerchantId        |
| TransactionReferenceNumber |
| MerchantReferenceNumber    |
| NatureOfDispute            |
| CBAlertType                |
| CBAmount                   |
| CurrencyCode               |
| CBSign                     |
| CBAction                   |
| CBActionDescription        |
| CardType                   |
| OriginalSettlementDate     |
| CBDate                     |
| CBReasonCode               |
| ResponseDueDate            |
| CustomerId                 |
| Application                |
[Fields in the Chargeback Report]

|--------------------------|----------------------------------|------------------------------|
| **Application Fields**                                                                   |||
| Name                     | Rcode                            | Rflag                        |
| Rmsg                     |                                  |                              |
| **BankInfo Fields**                                                                      |||
| Address                  | BranchCode                       | City                         |
| Country                  | Name                             | SwiftCode                    |
| **BillTo Fields**                                                                        |||
| Address1                 | Address2                         | City                         |
| CompanyName              | CompanyTaxID                     | Country                      |
| CustomerID               | Email                            | FirstName                    |
| HostName                 | IPAddress                        | LastName                     |
| MiddleName               | NameSuffix                       | PersonalID                   |
| Phone                    | State                            | Title                        |
| UserName                 | Zip                              |                              |
| **ChargebackAndRetrieval Fields**                                                        |||
| ARN                      | AdjustmentAmount                 | AdjustmentCurrency           |
| CaseIdentifier           | CaseNumber (\*)                  | CaseTime (\*)                |
| CaseType (\*)            | ChargebackAmount (\*)            | ChargebackCurrency (\*)      |
| ChargebackMessage        | ChargebackOriginalAmount         | ChargebackOriginalCurrency   |
| ChargebackReasonCode     | ChargebackReasonCode Description | ChargebackTime (\*)          |
| DocumentIndicator        | FeeAmount                        | FeeCurrency                  |
| FinancialImpact (\*)     | FinancialImpactType              | MerchantCategoryCode         |
| PartialIndicator         | ResolutionTime                   | ResolvedToIndicator          |
| RespondByDate            | TransactionType (\*)             |                              |
| **Check Fields**                                                                         |||
| AccountEncoderID         | SecCode                          |                              |
| **Device Fields**                                                                        |||
| DeviceID                 |                                  |                              |
| **FundTransfer Fields**                                                                  |||
| BankCheckDigit           | IbanIndicator                    |                              |
| **LineItems Fields**                                                                     |||
| FulfillmentType          | InvoiceNumber                    | MerchantProductSku           |
| Number                   | ProductCode                      | ProductName                  |
| Quantity                 | TaxAmount                        | UnitPrice                    |
| **MerchantDefinedData Fields**                                                           |||
| Field1 - Field20         |                                  |                              |
| **PaymentData Fields**                                                                   |||
| AAV_CAVV                 | ACHVerificationResult            | ACHVerificationResult Mapped |
| AVSResult                | AVSResultMapped                  | Amount                       |
| AuthIndicator            | AuthReversalAmount               | AuthReversalResult           |
| AuthorizationCode        | AuthorizationType                | BalanceAmount                |
| BalanceCurrencyCode      | BinNumber                        | CVResult                     |
| CardCategory             | CardCategoryCode                 | CurrencyCode                 |
| DCCIndicator             | ECI                              | EVEmail                      |
| EVEmailRaw               | EVName                           | EVNameRaw                    |
| EVPhoneNumber            | EVPhoneNumberRaw                 | EVPostalCode                 |
| EVPostalCodeRaw          | EVStreet                         | EVStreetRaw                  |
| EventType                | ExchangeRate                     | ExchangeRateDate             |
| GrandTotal               | NetworkTransactionID             | NumberOfInstallments         |
| PaymentProcessor         | PaymentProductCode               | PaymentRequestID             |
| ProcessorResponseCode    | ProcessorResponseID              | ProcessorTID                 |
| RequestedAmount          | RequestedAmountCurrency Code     | TargetAmount                 |
| TargetCurrency           | TotalTaxAmount                   | TransactionRefNumber         |
| XID                      |                                  |                              |
| **PaymentMethod Fields**                                                                 |||
| AccountSuffix            | BankAccountName                  | BankCode                     |
| BoletoBarCodeNumber      | BoletoNumber                     | CardType                     |
| CheckNumber              | ExpirationMonth                  | ExpirationYear               |
| IssueNumber              | MandateId                        | MandateType                  |
| SignatureDate            | StartMonth                       | StartYear                    |
| WalletType               |                                  |                              |
| **Profile Fields**                                                                       |||
| Name                     | ProfileDecision                  | ProfileMode                  |
| RuleDecision             | RuleName                         |                              |
| **Recipient Fields**                                                                     |||
| RecipientBillingAmount   | RecipientBillingCurrency         |                              |
| **Request Fields**                                                                       |||
| Comments                 | MerchantID (\*)                  | MerchantReferenceNumber      |
| RequestID (\*)           | Source                           | SubscriptionID               |
| TransactionDate (\*)     | User                             |                              |
| **Risk Fields**                                                                          |||
| AppliedAVS               | AppliedCV                        | AppliedCategoryGift          |
| AppliedCategoryTime      | AppliedHostHedge                 | AppliedThreshold             |
| AppliedTimeHedge         | AppliedVelocityHedge             | BinAccountType               |
| BinCountry               | BinIssuer                        | BinScheme                    |
| CodeType                 | CodeValue                        | ConsumerLoyalty              |
| ConsumerPasswordProvided | ConsumerPromotions               | CookiesAccepted              |
| CookiesEnabled           | DeviceFingerPrint                | Factors                      |
| FlashEnabled             | GiftWrap                         | HostSeverity                 |
| IPCity                   | IPCountry                        | IPRoutingMethod              |
| IPState                  | ImagesEnabled                    | JavascriptEnabled            |
| LostPassword             | ProductRisk                      | ProxyIPAddress               |
| ProxyIPAddressActivities | ProxyIPAddressAttributes         | ProxyServerType              |
| RepeatCustomer           | ReturnsAccepted                  | Score                        |
| TimeLocal                | TrueIPAddress                    | TrueIPAddressAttributes      |
| TrueIPAddressCity        | TrueIPAddressCountry             | TrueIPaddressActivities      |
| Sender Fields                                                                            |||
| SenderReferenceNumber    |                                  |                              |
| **ShipTo Fields**                                                                        |||
| Address1                 | Address2                         | City                         |
| Country                  | FirstName                        | LastName                     |
| Phone                    | State                            | Zip                          |
| **Shipping Fields**                                                                      |||
| Carrier                  | Method                           |                              |
| **Token Fields**                                                                         |||
| TokenCode                |                                  |                              |
| **Travel Fields**                                                                        |||
| CompleteRoute            | DepartureDateTime                | JourneyType                  |
| Number                   | PassengerEmail                   | PassengerFirstName           |
| PassengerId              | PassengerLastName                | PassengerPhone               |
| PassengerStatus          | PassengerType                    |                              |
[Chargeback Report Fields]

Reports Available in the `Business Center` {#ID-000006f3}
=========================================================

This section includes an alphabetical listing of all reports available in the `Business Center`. Each report description includes a description, availability, locations, and instructions for learning more. The availability of some reports is based on the services or products you use.  
Some users may also have access to financial data. For more information about reports containing this type of data, see [Financial and Reconciliation Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Financial_and_Reconciliation_Reports.md "").

Account Updater Reply File {#ID-000006f7}
=========================================

|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Results of account updater batch file. The updates include expiration dates, credit card numbers, and brands.                                                                                                                             |
| Who can use it?                       | Merchants using Account Updater product. For more information about using Account Updater, see the [Account Updater User Guide](https://apps.cybersource.com/library/documentation/dev_guides/Account_Updater_UG/Account_Updater.pdf ""). |
| What do I use it for?                 | ---                                                                                                                                                                                                                                       |
| What kind of report is it?            | Downloadable Third-Party report                                                                                                                                                                                                           |
| Where do I find it?                   | On the left navigation pane, under `Reports`, click **Downloadable Reports** , then **`Available Reports`** . Click **Third Party Reports**, then click the file you want to open.                                                        |
| Which APIs can I use to get the data? | Secure File Share API                                                                                                                                                                                                                     |
| How do I create one?                  | File is created automatically for Account Updater users.                                                                                                                                                                                  |
[Account Updater Reply File]

Batch Upload Reply File {#ID-0000072c}
======================================

|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Contains transactions processed via offline transaction file submission. File name is either: * Reply.All * Reply.Rejected                                                                                                                                                   |
| Who can use it?                       | Merchants using Offline Transaction File Submission product. For more information, see [Offline Transaction File Submission Implementation Guide](https://developer.cybersource.com/library/documentation/dev_guides/Offline_Trans_File_Submission/Batch_Upload_ENT.pdf ""). |
| What do I use it for?                 | ---                                                                                                                                                                                                                                                                          |
| What kind of report is it?            | Downloadable Third-Party report                                                                                                                                                                                                                                              |
| Where do I find it?                   | On the left navigation pane, under `Reports`, click Downloadable Reports, then `Available Reports`. Click **Third Party Reports**, then click the file you want to open.                                                                                                     |
| Which APIs can I use to get the data? | Secure File Share API                                                                                                                                                                                                                                                        |
| How do I create one?                  | File is created automatically for Offline Transaction File Submission users.                                                                                                                                                                                                 |
[Batch Upload Reply File]

Billable Transactions Detail {#c_billing_transactions_details}
==============================================================

|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?      | Provides transaction details at the Request Identifier level including Billing Code per MID. Enables resellers and merchants to reconcile their usage of Acceptance Solutions services with their monthly billed transactions in their invoice. |
| Who can use it?                          | Resellers and merchants.                                                                                                                                                                                                                        |
| What do I use it for?                    | To reconcile usage of Acceptance Solutions services with monthly billed transactions in the invoice.                                                                                                                                            |
| What kind of report is it?               | This report is a standard report and also a downloadable custom report.                                                                                                                                                                         |
| Where do I find it?                      | On the left navigation panel, go to `Reports` \&gt; Downloadable Reports \&gt; `Available Reports`. Click Create custom report. You can also customize the report on the Report Subscription Management page.                                   |
| Which APIs can I use to obtain the data? | Use the reporting API: * /reporting/v3/report-downloads * /reporting/v3/report-subscriptions * /reporting/v3/reports {#c_billing_transactions_details_ul_agz_fpk_tfc}                                                                           |
| How do I create one?                     | For more information, see [Creating Custom Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports.md "").                            |
[Billable Transactions Detail Report]

Conversion Detail (Downloadable) {#ID-00000764}
===============================================

|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Results of converted orders for each reviewer.                                                                                                                                                                                                                                                     |
| Who can use it?                       | For more information about using `Decision Manager`, see the `Decision Manager` Documentation tab in the `Business Center`.                                                                                                                                                                        |
| What do I use it for?                 | Provides information for all orders that were not immediately accepted but instead flagged for review. Contains all transactions that were decisioned in selected time period.                                                                                                                     |
| What kind of report is it?            | Downloadable Custom report For information about the on-demand version of this report, see [Conversion Detail (On-Demand)](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Reports_Available_in_the_Business_Center/c_Conversion_Detail_On-Demand.md ""). |
| Where do I find it?                   | On the left navigation pane, under `Reports`, click Downloadable Reports, then `Available Reports`. Click **Create Report** to create a new report. You can also customize the report on the Report Subscription Management page.                                                                  |
| Which APIs can I use to get the data? | Reporting API (`/reporting/v3/report-downloads`)                                                                                                                                                                                                                                                   |
| How do I create one?                  | For more information, see [Creating Custom Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports.md "").                                                                               |
[Conversion Detail Report - Downloadable]

Report fields can be modified. Report field names in bold are required.

| Field Type |         Field Name          |
|------------|-----------------------------|
| Conversion | **ConversionDate**          |
| Request    | **MerchantReferenceNumber** |
| Request    | **RequestID**               |
[Fields Included in Standard Conversion Detail Report]

Conversion Detail (On-Demand) {#ID-000007bd}
============================================

|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | This report contains the results of the converted orders for each reviewer. This information gives you an overview of all orders that were not immediately accepted.             |
| Who can use it?                       | Merchants using `Decision Manager`. For more information, see the `Decision Manager` tab in the `Business Center`.                                                               |
| What do I use it for?                 | Provides information for all orders that were not immediately accepted but instead flagged for review. Contains all transactions that were decisioned in selected time period.   |
| What kind of report is it?            | On-Demand Report (`Decision Manager` only)                                                                                                                                       |
| Where do I find it?                   | On the loft navigation pane, click **`Reports`** , then click **Conversion Detail**.                                                                                             |
| Which APIs can I use to get the data? | Reporting API                                                                                                                                                                    |
| How do I create one?                  | For more information, see [Viewing On-Demand Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Viewing_On-Demand_Reports.md ""). |
[Conversion Detail Report - On-Demand]

Report fields cannot be modified.

| Field Name               |
|:-------------------------|
| \&lt;url_prefix\&gt;     |
| \&lt;startTime\&gt;      |
| \&lt;endTime\&gt;        |
| \&lt;organizationID\&gt; |
[Fields Included in On-Demand Conversion Detail Report]

`Decision Manager` Detail {#ID-00000809}
========================================

|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Data from selected fields for `Decision Manager` orders within a specific period of time. The report consists of the data from the fields you select. Three default fields are preselected (Merchant ID, Request ID, and Transaction Date) and cannot be deselected. |
| Who can use it?                       | Merchants using `Decision Manager`. For more information, see the `Decision Manager` Documentation tab in the `Business Center`.                                                                                                                                     |
| What do I use it for?                 | View details of `Decision Manager` orders.                                                                                                                                                                                                                           |
| What kind of report is it?            | Downloadable Custom report                                                                                                                                                                                                                                           |
| Where do I find it?                   | On the left navigation pane, under `Reports`, click Downloadable Reports, then `Available Reports`. Click **Create Report** to create a new report. You can also customize the report on the Report Subscription Management page.                                    |
| Which APIs can I use to get the data? | ---                                                                                                                                                                                                                                                                  |
| How do I create one?                  | For more information, see [Creating Custom Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports.md "").                                                 |
[`Decision Manager` Detail Report]

`Decision Manager` Events Detail {#ID-00000842}
===============================================

|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Selected fields for `Decision Manager` account login, creation, and update events. Report fields can be modified.                                                                                                                 |
| Who can use it?                       | Merchants using `Decision Manager`. For more information, see the `Decision Manager` Documentation tab in the `Business Center`.                                                                                                  |
| What do I use it for?                 | Download and analyze account creation and login and account update event details.                                                                                                                                                 |
| What kind of report is it?            | Downloadable Custom report                                                                                                                                                                                                        |
| Where do I find it?                   | On the left navigation pane, under `Available Reports`, click Downloadable Reports, then `Reports`. Click **Create Report** to create a new report. You can also customize the report on the Report Subscription Management page. |
| Which APIs can I use to get the data? | ---                                                                                                                                                                                                                               |
| How do I create one?                  | For more information, see [Creating Custom Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports.md "").              |
[`Decision Manager` Events Detail Report]

Fee Detail {#ID-0000087c}
=========================

|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Transaction-level fees as reported by the payment processor.                                                                                                                                                                                                                                                                                                                                 |
| Who can use it?                       | Merchants using a payment processor that shares data with the `Business Center`. Can also be consolidated at the account or partner level. For more information, see [Fee Details Report](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Financial_and_Reconciliation_Reports/c_Fields_Available_in_Financial_Reports/c_Fee_Details_Report.md ""). |
| What do I use it for?                 | Understand transaction-level fees in order to perform financial reconciliation.                                                                                                                                                                                                                                                                                                              |
| What kind of report is it?            | Downloadable Custom Report                                                                                                                                                                                                                                                                                                                                                                   |
| Where do I find it?                   | On the left navigation pane, under `Reports`, click Downloadable Reports, then `Available Reports`. Click **Create Report** to create a new report. You can also create a report subscription on the Report Subscription Management page.                                                                                                                                                    |
| Which APIs can I use to get the data? | Reporting API (`/reporting/v3/report-downloads`)                                                                                                                                                                                                                                                                                                                                             |
| How do I create one?                  | For more information, see [Creating Custom Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports.md "").                                                                                                                                                                         |
[Fee Detail Report]

Report fields can be modified. Report field names in bold are required.

| Field Type | Field Name              |
|:-----------|:------------------------|
| Fee        | **AssessmentAmount**    |
| Fee        | **AssessmentCurrency**  |
| Fee        | **BillingType**         |
| Fee        | **DiscountAmount**      |
| Fee        | **DiscountCurrency**    |
| Fee        | **InterchangeAmount**   |
| Fee        | **InterchangeCurrency** |
| Fee        | **SettlementAmount**    |
| Fee        | **SettlementCurrency**  |
| Fee        | **SettlementTime**      |
| Fee        | **SettlementTimeZone**  |
| Fee        | **TotalFeeAmount**      |
| Fee        | **TotalFeeCurrency**    |
| Request    | **MerchantID**          |
| Request    | **RequestID**           |
| Request    | **TransactionDate**     |
[Fields included by default in Fee Detail Report]

Invoice Summary {#ID-0000090a}
==============================

|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Total count of billable transactions by application type.                                                                                                                                                                                 |
| Who can use it?                       | Any merchant. Can also be consolidated at the account or partner level.                                                                                                                                                                   |
| What do I use it for?                 | View the count of billable transactions.                                                                                                                                                                                                  |
| What kind of report is it?            | Downloadable Standard report                                                                                                                                                                                                              |
| Where do I find it?                   | On the left navigation pane, under `Reports`, click Downloadable Reports, then `Available Reports`. Click **Create Report** to create a new report. You can also create a report subscription on the Report Subscription Management page. |
| Which APIs can I use to get the data? | Reporting API (`/reporting/v3/report-downloads`)                                                                                                                                                                                          |
| How do I create one                   | For more information, see [Subscribing to Standard Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Subscribing_to_Standard_Reports.md "").      |
[Invoice Summary Report]

Report fields cannot be modified.

| Field Type | Field Name              |
|:-----------|:------------------------|
| Invoice    | OrganizationID          |
| Invoice    | PerformedServices       |
| Invoice    | BillingGroupDescription |
| Invoice    | Processed               |
| Invoice    | NotProcessed            |
| Invoice    | Total                   |
[Fields Included in Standard Invoice Summary Report]

JP Transaction {#ID-00000963}
=============================

|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Report that contains details specific to transactions processed using the JCN gateway.                                                                                                                                                 |
| Who can use it?                       | Merchants using JCN gateway and who are enabled for JP reports.                                                                                                                                                                        |
| What do I use it for?                 | View transactions submitted to the payment processor.                                                                                                                                                                                  |
| What kind of report is it?            | Downloadable Custom report                                                                                                                                                                                                             |
| Where do I find it?                   | On the left navigation pane, under **`Reports`** , click Downloadable Reports, then `Available Reports`. Click **Create Report** to create a new report. You can also customize the report on the Report Subscription Management page. |
| Which APIs can I use to get the data? | Reporting API (/reporting/v3/report-downloads)                                                                                                                                                                                         |
| How do I create one?                  | For more information, see [Creating Custom Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports.md "").                   |
[JP Transaction Report]

Network Token Life-Cycle Management {#net-tkn-lcm}
==================================================

|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | The report contains network-token related fields. The report is updated when life-cycle management events are reported to the `Token Management Service` (`TMS`).                                                            |
| Who can use it?                       | Merchants enabled with network tokenization.                                                                                                                                                                                 |
| What do I use it for?                 | View and generate reports on network token life-cycle management event data for auditing and performance monitoring purposes. Merchants can view the life-cycle management events for provisioned network tokens.            |
| What kind of report is it?            | Downloadable with standard and custom options.                                                                                                                                                                               |
| Where do I find it?                   | On the left navigation pane, under `Reports`, choose Downloadable Report \&gt; `Available Reports`. Click **Create Report** to create a new report. You can customize the report on the Report Subscription Management page. |
| Which APIs can I use to get the data? | Use the reporting API: * `/reporting/v3/report-downloads` * `/reporting/v3/report-subscriptions` * `/reporting/v3/reports`                                                                                                   |
| How do I create one?                  | See [Creating Custom Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports.md "").                               |
[Network Token Life-Cycle Management Report]

Notification of Change {#ID-00000998}
=====================================

|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Report that includes echeck-related fields updated as a result of a response to an echeck settlement transaction.                                                                                      |
| Who can use it?                       | Enabled for merchants processing echecks on certain gateways.                                                                                                                                          |
| What do I use it for?                 | MA merchants: report contains transactions that GPN has reported as funded. Non-MA merchants: report contains batched transactions.                                                                    |
| What kind of report is it?            | On-Demand report                                                                                                                                                                                       |
| Where do I find it?                   | On the loft navigation pane, click **`Reports`** . Under `Transaction Reports`, click **Notification of Change**.                                                                                      |
| Which APIs can I use to get the data? | Reporting API (`/reporting/v3/report-downloads`)                                                                                                                                                       |
| How do I create one?                  | For more information, see [Notification of Change](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Viewing_On-Demand_Reports/c_Notification_of_Change.md ""). |
[Notification of Change Report]

| Field Name                   |
|:-----------------------------|
| Merchant Reference Number    |
| Transaction Reference Number |
| NOC Date                     |
| NOC Code                     |
| Updated Account Type         |
| Updated Routing Number       |
| Updated Account Number       |
| Updated Consumer Name        |
[Fields in the Notification of Change Report]

Payer Authentication Detail {#ID-000009ef}
==========================================

|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Detail-level report that includes the number of transactions and total amount for groups of transactions based on each currency and card type you support.                                                                        |
| Who can use it?                       | ---                                                                                                                                                                                                                               |
| What do I use it for?                 | ---                                                                                                                                                                                                                               |
| What kind of report is it?            | Downloadable Custom report                                                                                                                                                                                                        |
| Where do I find it?                   | On the left navigation pane, under `Reports`, click Downloadable Reports, then `Available Reports`. Click **Create Report** to create a new report. You can also customize the report on the Report Subscription Management page. |
| Which APIs can I use to get the data? | ---                                                                                                                                                                                                                               |
| How do I create one?                  | For more information, see [Creating Custom Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports.md "").              |
[Payer Authentication Detail Report]

Report fields can be modified. Report field names in bold are required.

| Field Type             | Field Name          |
|:-----------------------|:--------------------|
| PayerAuthDetailRequest | **DSTransactionID** |
| PayerAuthDetailRequest | **MerchantID**      |
| PayerAuthDetailRequest | **RequestID**       |
| PayerAuthDetailRequest | **TransactionDate** |
[Fields Included in Standard Payer Authentication Detail Report]

Payer Authentication Summary {#ID-00000a44}
===========================================

|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Summary-level report of data contained in Payer Authentication Detail report.                                                                                                                                                     |
| Who can use it?                       | Merchants and account-level users enabled for Payer Auth service.                                                                                                                                                                 |
| What do I use it for?                 | View recent activity in graphical format.                                                                                                                                                                                         |
| What kind of report is it?            | On-Demand report                                                                                                                                                                                                                  |
| Where do I find it?                   | On the left navigation pane, under `Reports`, click Downloadable Reports, then `Available Reports`. Click **Create Report** to create a new report. You can also customize the report on the Report Subscription Management page. |
| Which APIs can I use to get the data? | ---                                                                                                                                                                                                                               |
| How do I create one?                  | On the left navigation pane, click **`Reports`** . Under `Transaction Reports`, click **Payer Auth Summary**.                                                                                                                     |
[Payer Authentication Summary Report]

Payment Batch Detail {#ID-00000a79}
===================================

|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Daily transaction level report that surfaces all of sales and refunds that have been submitted to your payment processor.                                                                                                                                                                                                                                                                                                     |
| Who can use it?                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                           |
| What do I use it for?                 | Understand which of your transactions have been settled.                                                                                                                                                                                                                                                                                                                                                                      |
| What kind of report is it?            | Downloadable report with Standard and Custom options.                                                                                                                                                                                                                                                                                                                                                                         |
| Where do I find it?                   | On the left navigation pane, under `Reports`, click Downloadable Reports, then `Available Reports`. Click **Create Report** to create a new report. You can also customize the report on the Report Subscription Management page.                                                                                                                                                                                             |
| Which APIs can I use to get the data? | ---                                                                                                                                                                                                                                                                                                                                                                                                                           |
| How do I create one?                  | For more information, see [Downloading Available Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Downloading_Available_Reports.md "") or [Creating Custom Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports.md ""). |
[Payment Batch Detail Report]

For more information, see [Configuring Payment Batch Detail Report Batch Times](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Modifying_Custom_Report_Subscriptions/Config_Pay_Batch_Detail_Report_Batch_Times.md ""). Report fields can be modified. Report field names in bold are required.

| Field Type | Field Name           |
|:-----------|:---------------------|
| Batch      | **BatchDate**        |
| Batch      | **BatchID**          |
| Batch      | **Status**           |
| Request    | LocalizedRequestDate |
| Request    | **MerchantID**       |
| Request    | **RequestID**        |
| Request    | **TransactionDate**  |
[Fields Included in Standard Payment Batch Detail Report]

Payment Batch Summary {#ID-00000adf}
====================================

|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | On-demand summary level report that includes a count and amount of your sales and refunds by currency and payment method.                                                                                                                                                                                      |
| Who can use it?                       | **Account level** users: * Total account value (sum of all merchants) or individual merchants in your account * Can view aggregated account-level data or merchant-by-merchant **Portfolio** users: * Account value for individual merchants in your account **Merchant** users: * Total value of your account |
| What do I use it for?                 | Get a quick overview of your payment activity.                                                                                                                                                                                                                                                                 |
| What kind of report is it?            | On-Demand report                                                                                                                                                                                                                                                                                               |
| Where do I find it?                   | On the left navigation pane, click **`Reports`**, then Payment Batch Summary Report.                                                                                                                                                                                                                           |
| Which APIs can I use to get the data? | ---                                                                                                                                                                                                                                                                                                            |
| How do I create one?                  | For more information, see [Payment Batch Summary](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Viewing_On-Demand_Reports/c_Payment_Batch_Summary.md "").                                                                                                           |
[Payment Batch Summary Report]

Payment Events {#ID-00000b1d}
=============================

|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Daily transaction level report that surfaces payment notifications received from your processor (for selected processors).                                                                                                        |
| Who can use it?                       | Merchants whose processors share data with the `Business Center`. Can also be consolidated at the account or partner level.                                                                                                       |
| What do I use it for?                 | Track information related to your transactions such as payment notifications, or exceptions.                                                                                                                                      |
| What kind of report is it?            | Downloadable Custom report                                                                                                                                                                                                        |
| Where do I find it?                   | On the left navigation pane, under `Reports`, click Downloadable Reports, then `Available Reports`. Click **Create Report** to create a new report. You can also customize the report on the Report Subscription Management page. |
| Which APIs can I use to get the data? | Reporting API (`/reporting/v3/report-downloads`)                                                                                                                                                                                  |
| How do I create one?                  | For more information, see [Downloading Available Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Downloading_Available_Reports.md "").  |
[Payment Events Report]

Point of Sale (POS) Terminal Exception {#ID-00000b51}
=====================================================

|---------------------------------------|--------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | POS transactions that could not be processed (transaction failed before reaching gateway). |
| Who can use it?                       | Merchants processing transactions using Payworks.                                          |
| What do I use it for?                 | View transactions that failed at the point of sale.                                        |
| What kind of report is it?            | On-Demand report                                                                           |
| Where do I find it?                   | On the left navigation pane, click **`Reports`** , then click **POS Terminal Exception**.  |
| Which APIs can I use to get the data? | ---                                                                                        |
| How do I create one?                  | ---                                                                                        |
[Point of Sale Exception Report]

Report fields cannot be modified.

| Field Type            | Field Name                   |
|:----------------------|:-----------------------------|
| POSTerminalExceptions | SchemeOperator               |
| POSTerminalExceptions | ProcessorMID                 |
| POSTerminalExceptions | TerminalID                   |
| POSTerminalExceptions | TransactionDate              |
| POSTerminalExceptions | DCCLookupStatus              |
| POSTerminalExceptions | LocalCurencyCode             |
| POSTerminalExceptions | DCCExchangeRate              |
| POSTerminalExceptions | DCCMarginRate                |
| POSTerminalExceptions | PartnerOriginalTransactionID |
| POSTerminalExceptions | PartnerMerchantID            |
| POSTerminalExceptions | PartnerMerchantName          |
| POSTerminalExceptions | CardVerificationMethod       |
| POSTerminalExceptions | StorageMechanism             |
| POSTerminalExceptions | DeviceHardwareRevision       |
| POSTerminalExceptions | DeviceID                     |
| POSTerminalExceptions | DeviceTerminalID             |
| POSTerminalExceptions | ClientID                     |
| POSTerminalExceptions | DeviceOS                     |
| POSTerminalExceptions | DeviceOSVersion              |
| POSTerminalExceptions | SDKVersion                   |
| POSTerminalExceptions | ExceptionCategory            |
| POSTerminalExceptions | ExceptionStatusCode          |
| POSTerminalExceptions | ExceptionDescription         |
| POSTerminalExceptions | MerchantID                   |
| POSTerminalExceptions | Amount                       |
| POSTerminalExceptions | FirstName                    |
| POSTerminalExceptions | LastName                     |
| POSTerminalExceptions | ExpirationMO                 |
| POSTerminalExceptions | ExpirationYR                 |
| POSTerminalExceptions | AccountSuffix                |
| POSTerminalExceptions | CurrencyCode                 |
[Fields Included in POS Terminal Exception Report]

Processor Events Detail {#ID-00000bf0}
======================================

|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Payment notifications received from the processor for a variety of payment events.                                                                                                                                                                                                                                                                                                                                            |
| Who can use it?                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                           |
| What do I use it for?                 | ---                                                                                                                                                                                                                                                                                                                                                                                                                           |
| What kind of report is it?            | Downloadable with Standard and Custom options.                                                                                                                                                                                                                                                                                                                                                                                |
| Where do I find it?                   | On the left navigation pane, under `Reports`, click Downloadable Reports, then `Available Reports`. Click **Create Report** to create a new report. You can also customize the report on the Report Subscription Management page.                                                                                                                                                                                             |
| Which APIs can I use to get the data? | ---                                                                                                                                                                                                                                                                                                                                                                                                                           |
| How do I create one?                  | For more information, see [Downloading Available Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Downloading_Available_Reports.md "") or [Creating Custom Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports.md ""). |
[Processor Events Detail Report]

Report fields can be modified. Report field names in bold are required.

| Field Type | Field Name           |
|:-----------|:---------------------|
| Event      | **Event**            |
| Event      | **EventDate**        |
| Event      | **ProcessorMessage** |
| Request    | LocalizedRequestDate |
| Request    | **MerchantID**       |
| Request    | **RequestID**        |
| Request    | **TransactionDate**  |
[Fields Included in Standard Processor Events Detail Report]

Processor Settlement Detail {#ID-00000c54}
==========================================

|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | All settlement responses sent by your acquirer, listed by transaction and status. Settlement requests are sent in batches. This report shows the response details.       |
| Who can use it?                       | Customers using an Alternate Payment integration with the Financial Service Provider (FSP) model.                                                                        |
| What do I use it for?                 | Financial reconciliation                                                                                                                                                 |
| What kind of report is it?            | ---                                                                                                                                                                      |
| Where do I find it?                   | Generated reports appear in the Custom tab of the `Available Reports` page.                                                                                              |
| Which APIs can I use to get the data? | ---                                                                                                                                                                      |
| How do I create one?                  | Customers with a supported processor can select the type from the "Report Type" drop-down when creating a report with the Create Report/Create Report Subscription page. |
[Processor Settlement Detail Report]

Recurring Billing Detail Report {#c-recurring-billing-detail-report}
====================================================================

|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Detailed information about recurring billing transactions.                                                                                                                                                                                |
| Who can use it?                       | Users with applicable permissions.                                                                                                                                                                                                        |
| What do I use it for?                 | Analyzing recurring billing transactions.                                                                                                                                                                                                 |
| What kind of report is it?            | Downloadable Standard report                                                                                                                                                                                                              |
| Where do I find it?                   | On the left navigation pane, under `Reports`, click Downloadable Reports, then `Available Reports`. Click **Create Report** to create a new report. You can also create a report subscription on the Report Subscription Management page. |
| Which APIs can I use to get the data? | The REST API Endpoint: `/reporting/v3/reports`                                                                                                                                                                                            |
| How do I create one?                  | For more information, see [Subscribing to Standard Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Subscribing_to_Standard_Reports.md "").      |
[Subscription Detail Report]

Standard Billing Data Package Report {#c_standard_billing_data_package}
=======================================================================

|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?      | Provides comprehensive billing information about services that each merchant used.                                                                                                                                   |
| Who can use it?                          | Partners and resellers.                                                                                                                                                                                              |
| What do I use it for?                    | Resellers can use this data to invoice the merchant for the services the merchant used.                                                                                                                              |
| What kind of report is it?               | Downloadable custom report.                                                                                                                                                                                          |
| Where do I find it?                      | On the left navigation panel, go to `Reports` \&gt; Downloadable Reports \&gt; `Available Reports`. Click **Create custom report** . You can also customize the report on the Report Subscription Management page.   |
| Which APIs can I use to obtain the data? | Use the reporting API: * /reporting/v3/report-downloads * /reporting/v3/report-subscriptions * /reporting/v3/reports {#c_standard_billing_data_package_ul_agz_fpk_tfc}                                               |
| How do I create one?                     | For more information, see [Creating Custom Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports.md ""). |
[Standard Billing Data Package Report]

Standard Monthly Fee Report {#c_Monthly_Fee_Details}
====================================================

|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?      | Provides details about the various monthly fees that Relay charges the reseller merchants.                                                                                                                            |
| Who can use it?                          | Partners and resellers.                                                                                                                                                                                              |
| What do I use it for?                    | Consolidates the fees that are charged to a reseller so that the reseller can pass these fees through to the merchant.                                                                                               |
| What kind of report is it?               | Downloadable custom report.                                                                                                                                                                                          |
| Where do I find it?                      | On the left navigation panel, go to `Reports` \&gt; Downloadable Reports \&gt; `Available Reports`. Click **Create custom report** . You can also customize the report on the Report Subscription Management page.   |
| Which APIs can I use to obtain the data? | Use the reporting API: * /reporting/v3/report-downloads * /reporting/v3/report-subscriptions * /reporting/v3/reports {#c_Monthly_Fee_Details_ul_agz_fpk_tfc}                                                         |
| How do I create one?                     | For more information, see [Creating Custom Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports.md ""). |
[Standard Monthly Fee Report]

Subscription Detail {#ID-00000cb9}
==================================

|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Detailed information about on-demand customer profiles and transactions.                                                                                                                                                                  |
| Who can use it?                       | ---                                                                                                                                                                                                                                       |
| What do I use it for?                 | ---                                                                                                                                                                                                                                       |
| What kind of report is it?            | Downloadable Standard report                                                                                                                                                                                                              |
| Where do I find it?                   | On the left navigation pane, under `Reports`, click Downloadable Reports, then `Available Reports`. Click **Create Report** to create a new report. You can also create a report subscription on the Report Subscription Management page. |
| Which APIs can I use to get the data? | ---                                                                                                                                                                                                                                       |
| How do I create one?                  | For more information, see [Subscribing to Standard Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Subscribing_to_Standard_Reports.md "").      |
[Subscription Detail Report]

| Field Type                | Field Name                      |
|:--------------------------|:--------------------------------|
| Subscriptions             | CustomerAccountID               |
| Subscriptions             | RecurringPaymentEventAmount     |
| Subscriptions             | RecurringPaymentAmount          |
| Subscriptions             | SubscriptionTitle               |
| Subscriptions             | SubscriptionStatus              |
| Subscriptions             | SubscriptionPaymentMethod       |
| Subscriptions             | RecurringStartDate              |
| Subscriptions             | RecurringNumberOfPayments       |
| Subscriptions             | RecurringFrequency              |
| Subscriptions             | RecurringApprovalRequired       |
| Subscriptions             | RecurringPaymentEventApprovedBy |
| Subscriptions             | RecurringAutomaticRenew         |
| Subscriptions             | SetupFee                        |
| Subscriptions             | SetupFeeCurrency                |
| Subscriptions             | SubscriptionType                |
| Subscriptions             | LastSubscriptionStatus          |
| Subscriptions             | NextScheduledDate               |
| Subscriptions             | EventRetryCount                 |
| Subscriptions             | PaymentsSuccess                 |
| Subscriptions             | PaymentSuccessAmount            |
| Subscriptions             | InstallmentSequence             |
| Subscriptions             | InstallmentTotalCount           |
| Subscriptions             | RequestID                       |
| Subscriptions             | SubscriptionID                  |
| Subscriptions             | TransactionDate                 |
| Subscriptions             | MerchantRefNo                   |
| Subscriptions             | TransRefNo                      |
| Subscriptions             | EcommerceIndicator              |
| Subscriptions             | BillToFirstName                 |
| Subscriptions             | BillToLastName                  |
| Subscriptions             | BillToAddress1                  |
| Subscriptions             | BillToAddress2                  |
| Subscriptions             | BillToCity                      |
| Subscriptions             | BillToState                     |
| Subscriptions (continued) | BillToZip                       |
| Subscriptions (continued) | BillToCountry                   |
| Subscriptions (continued) | BillToCompanyName               |
| Subscriptions (continued) | BillToEmail                     |
| Subscriptions (continued) | ConsumerPhone                   |
| Subscriptions (continued) | IPAddress                       |
| Subscriptions (continued) | ShipToFirstName                 |
| Subscriptions (continued) | ShipToLastName                  |
| Subscriptions (continued) | ShipToAddress1                  |
| Subscriptions (continued) | ShipToAddress2                  |
| Subscriptions (continued) | ShipToCity                      |
| Subscriptions (continued) | ShipToState                     |
| Subscriptions (continued) | ShipToZip                       |
| Subscriptions (continued) | ShipToCountry                   |
| Subscriptions (continued) | ShipToCompanyName               |
| Subscriptions (continued) | CardType                        |
| Subscriptions (continued) | CustomerCCExpiryMonth           |
| Subscriptions (continued) | CustomerCCExpiryYear            |
| Subscriptions (continued) | CustomerCCStartMonth            |
| Subscriptions (continued) | CustomerCCStartYear             |
| Subscriptions (continued) | CustomerCCIssueNo               |
| Subscriptions (continued) | CustomerCCAccountSuffix         |
| Subscriptions (continued) | CustomerCCSubTypeDescription    |
| Subscriptions (continued) | CustomerCCRoutingNumber         |
| Subscriptions (continued) | Applications                    |
| Subscriptions (continued) | PaymentProcessor                |
| Subscriptions (continued) | CurrencyCode                    |
| Subscriptions (continued) | ReasonCode                      |
| Subscriptions (continued) | AuthRCode                       |
| Subscriptions (continued) | AuthCode                        |
| Subscriptions (continued) | AuthType                        |
| Subscriptions (continued) | AuthAVSResults                  |
| Subscriptions (continued) | AuthResponseCode                |
| Subscriptions (continued) | AuthCardVerificationResult      |
| Subscriptions (continued) | RCode                           |
| Subscriptions (continued) | RFlag                           |
| Subscriptions (continued) | RMsg                            |
| Subscriptions (continued) | RequestToken                    |
| Subscriptions (continued) | MerchantDefinedData1            |
| Subscriptions (continued) | MerchantDefinedData2            |
| Subscriptions (continued) | MerchantDefinedData3            |
| Subscriptions (continued) | MerchantDefinedData4            |
| Subscriptions (continued) | TaxAmount                       |
| Subscriptions (continued) | Comments                        |
| Subscriptions (continued) | MerchantSecureData1             |
| Subscriptions (continued) | MerchantSecureData2             |
| Subscriptions (continued) | MerchantSecureData3             |
| Subscriptions (continued) | MerchantSecureData4             |
| Subscriptions (continued) | MerchantID                      |
[Fields Included in Subscription Detail Report]

Tax Detail {#ID-00000dfb}
=========================

|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Jurisdiction-level tax data derived from your tax calculation service (ics_tax) requests and associated tax determination responses, as returned by the tax engine.                                                                       |
| Who can use it?                       | ---                                                                                                                                                                                                                                       |
| What do I use it for?                 | ---                                                                                                                                                                                                                                       |
| What kind of report is it?            | Downloadable Standard report                                                                                                                                                                                                              |
| Where do I find it?                   | On the left navigation pane, under `Reports`, click Downloadable Reports, then `Available Reports`. Click **Create Report** to create a new report. You can also create a report subscription on the Report Subscription Management page. |
| Which APIs can I use to get the data? | ---                                                                                                                                                                                                                                       |
| How do I create one?                  | For more information, see [Subscribing to Standard Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Subscribing_to_Standard_Reports.md "").      |
[Tax Detail Report]

Report fields cannot be modified.

| Field Type     | Field Name                |
|:---------------|:--------------------------|
| Tax            | RequestID                 |
| Tax            | MerchantID                |
| Tax            | MerchantReferenceNumber   |
| Tax            | InvoiceDate               |
| Tax            | OrderAcceptanceCity       |
| Tax            | OrderAcceptanceCountry    |
| Tax            | OrderAcceptancePostalCode |
| Tax            | OrderAcceptanceState      |
| Tax            | ProductCode               |
| Tax            | ProductName               |
| Tax            | MerchantProductSKU        |
| Tax            | Quantity                  |
| Tax            | ReportingDate             |
| Tax            | ShipFromCity              |
| Tax            | ShipFromCountry           |
| Tax, continued | ShipFromPostalCode        |
| Tax, continued | ShipFromState             |
| Tax, continued | ShipToCity                |
| Tax, continued | ShipToCountry             |
| Tax, continued | ShipToPostalCode          |
| Tax, continued | ShipToState               |
| Tax, continued | ShipToAddress1            |
| Tax, continued | TransactionType           |
| Tax, continued | UnitPrice                 |
| Tax, continued | Country                   |
| Tax, continued | TaxAmount                 |
| Tax, continued | TaxName                   |
| Tax, continued | CurrencyCode              |
| Tax, continued | JurisdictionName          |
| Tax, continued | JurisdictionType          |
| Tax, continued | JurisdictionCode          |
| Tax, continued | LineItemAmount            |
| Tax, continued | LineItemExemptAmount      |
| Tax, continued | TaxableAmount             |
| Tax, continued | JurisdictionRate          |
| Tax, continued | State                     |
| Tax, continued | SequenceNumber            |
| Tax, continued | Status                    |
[Fields Included in Tax Detail Report]

Transaction Exception Detail {#ID-00000eb5}
===========================================

|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Details failures that happen after a follow-on transaction is submitted to the payment gateway.                                                                                                                                                                                                                                                                                                                               |
| Who can use it?                       | Available to all merchants.                                                                                                                                                                                                                                                                                                                                                                                                   |
| What kind of report is it?            | Downloadable with Standard and Custom options.                                                                                                                                                                                                                                                                                                                                                                                |
| Where do I find it?                   | On the left navigation pane, under `Reports`, click Downloadable Reports, then `Available Reports`. Click **Create Report** to create a new report. You can also customize the report on the Report Subscription Management page.                                                                                                                                                                                             |
| Which APIs can I use to get the data? | ---                                                                                                                                                                                                                                                                                                                                                                                                                           |
| How do I create one?                  | For more information, see [Downloading Available Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Downloading_Available_Reports.md "") or [Creating Custom Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports.md ""). |
[Transaction Exception Detail Report]

Report fields can be modified. Report field names in bold are required.

| Field Type | Field Name                |
|:-----------|:--------------------------|
| Exception  | **Action**                |
| Exception  | **ExceptionCategory**     |
| Exception  | **ExceptionMessage**      |
| Exception  | **ExceptionType**         |
| Exception  | **ProcessorResponseCode** |
| Exception  | **ReasonCode**            |
| Request    | LocalizedDate             |
| Request    | **MerchantID**            |
| Request    | **RequestID**             |
| Request    | **TransactionDate**       |
[Fields Included in Standard Transaction Exception Detail Report]

Transaction Request {#ID-00000f20}
==================================

|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What is the purpose of this report?   | Daily transaction level report that surfaces details related to each individual transaction. Report fields can be modified.                                                                                                       |
| Who can use it?                       | Available to all organizations.                                                                                                                                                                                                   |
| What kind of report is it?            | Downloadable Custom report                                                                                                                                                                                                        |
| Where do I find it?                   | On the left navigation pane, under `Reports`, click Downloadable Reports, then `Available Reports`. Click **Create Report** to create a new report. You can also customize the report on the Report Subscription Management page. |
| Which APIs can I use to get the data? | ---                                                                                                                                                                                                                               |
| How do I create one?                  | For more information, see [Creating Custom Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports/c_Creating_Custom_Reports.md "").              |
[Transaction Request Report]

Report fields can be modified. Report field names in bold are required.

| Field Type | Field Name          |
|:-----------|:--------------------|
| Request    | LocalizedDate       |
| Request    | **MerchantID**      |
| Request    | **RequestID**       |
| Request    | **TransactionDate** |
[Fields Included in Standard Transaction Request Report]

Report Fields and Descriptions {#ID-00000f71}
=============================================

This section includes report field names and descriptions for downloadable reports and card-present transactions, and field names with compound values.

Fields and Descriptions for Downloadable Reports {#ID-00000f73}
===============================================================

Available reporting fields that can be used in downloadable reports are shown in this section and organized by field type. For example, billing, settlement, and tokens. If available, additional details, including description, field format, and mapped values, are included.  
Fields available for reporting in `Decision Manager` are indicated by "(`Decision Manager`)" in the section's table title.  
For more information, see [Creating and Accessing Downloadable Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports.md "").

Advanced Fraud Screen (AFS) Fields {#ID-00000f7a}
=================================================

| Field Name      | Description                                       |
|:----------------|:--------------------------------------------------|
| Factors         | Information that affected score of the order.     |
| HostSeverity    | Risk associated with customer's email domain.     |
| InfoCodeString  | List of information codes triggered by the order. |
| IPAddress       | Customer's IP address.                            |
| IPCountry       | Name of the country decoded from IP address.      |
| IPRoutingMethod | Routing method decoded from IP address.           |
| IPState         | Name of the state decoded from IP address.        |
| Model           | Name of score model used for the transaction.     |
| Score           | Total score calculated for the order.             |
[Advanced Fraud Screen Fields (`Decision Manager`)]

Application Fields {#ID-00000fb8}
=================================

| Field Name | Description                                                          | Data Type (Length) | Simple Order API Value |
|:-----------|:---------------------------------------------------------------------|:-------------------|:-----------------------|
| Name       | Name of application used.                                            | VARCHAR2           | Name                   |
| Rcode      | One-digit code indicating whether the entire request was successful. | Number (12)        | Rcode                  |
| ReasonCode | ---                                                                  | ---                | ReasonCode             |
| Rflag      | One-word description of the result of the entire request.            | VARCHAR2 (50)      | Rflag                  |
| Rmsg       | Message that explains the \&lt;ics_rflag\&gt; value.                 | VARCHAR2 (255)     | Rmsg                   |
[Application Fields]

Authorization Results Fields {#ID-00001008}
===========================================

| Field Name | Description                                        |
|:-----------|:---------------------------------------------------|
| AVSResult  | Optional results of address verification test.     |
| CVVResult  | Optional results of card verification number test. |
[Authorization Results Fields]

Bank Information Fields {#ID-00001028}
======================================

| Field Name | Description                                                                                      | Data Type  (Length) |
|:-----------|:-------------------------------------------------------------------------------------------------|:--------------------|
| Address    | Bank's address.                                                                                  | VARCHAR2 (50)       |
| BranchCode | Code that identifies the branch of the customer's bank when you are not using the IBAN.          | VARCHAR2 (50)       |
| City       | City in which the bank is located.                                                               | VARCHAR2 (50)       |
| Country    | Country in which the bank is located.                                                            | VARCHAR2 (50)       |
| Name       | Bank's name.                                                                                     | VARCHAR2 (50)       |
| SwiftCode  | Bank's SWIFT code. Unique address of the bank. Also known as the Bank Identification Code (BIC). | VARCHAR2 (50)       |
[Bank Information Fields]

Batch Fields {#ID-00001074}
===========================

| Field Name  | Description                                                 | Data Type (Length) |
|:------------|:------------------------------------------------------------|:-------------------|
| BatchDate   | Date when the batch was sent to the processor.              | Date               |
| BatchID     | Identifier for the batch in which the transaction was sent. | VARCHAR2 (8)       |
| Status      | Status of batch file.                                       | VARCHAR2 (10)      |
| SuccessFlag | Indicates whether batch file processing was successful.     | VARCHAR            |
[Batch Fields]

Billable Transactions Detail Fields {#billable-transaction-details}
===================================================================

|        Field Name         |                                                        Description                                                         |                   Data Type (Length)                    | Mandatory/Optional |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|--------------------|
| Currency                  | The ISO currency code used in the transaction.                                                                             | String                                                  | M                  |
| Merchant Reference Number | The order reference or tracking number generated by the merchant.                                                          | String                                                  | M                  |
| Organization ID           | The transacting MID value assigned by `Cybersource` or Acceptance Platform.                                           | String including the special character, underscore (_). | M                  |
| Payment Processor         | The name of the payment processor.                                                                                         | String                                                  | O                  |
| Product Code              | The `Cybersource` product code for the transaction.                                                                        | String                                                  | M                  |
| Product Description       | The `Cybersource` product description for the transaction.                                                                 | String including special characters.                    | M                  |
| Quantity                  | The quantity of the service requested.                                                                                     | Number                                                  | M                  |
| Requested Amount          | The amount used in the transaction.                                                                                        | Number                                                  | M                  |
| Request ID                | The unique identification number generated by `Cybersource` or Acceptance Platform to identify the submitted request. | Number                                                  | M                  |
| Service Name              | The name of the service being requested as identified in `Cybersource` or Acceptance Platform.                        | String                                                  | M                  |
| Transaction Date          | The date of the transaction. Format: `YYYY-MM-DDHH:MM:SS `                                                                 | Number                                                  | M                  |
[Billable Transactions Detail Field Names and Descriptions]

Bill To Fields {#ID-000010ad}
=============================

| Field Name   | Description                                                                                                                                                                               | Data Type (Length) | Simple Order API Value  |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:------------------------|
| Address1     | First line of the billing street address as it appears on the credit card issuer's records.                                                                                               | VARCHAR2 (400)     | billTo_street1          |
| Address2     | Additional address information.                                                                                                                                                           | VARCHAR2 (400)     | billTo_street2          |
| City         | City of the billing address.                                                                                                                                                              | VARCHAR2 (50)      | billTo_city             |
| CompanyName  | Name of the customer's company.                                                                                                                                                           | VARCHAR2 (60)      | billTo_company          |
| CompanyTaxID | Tax identification number of customer's company.                                                                                                                                          | VARCHAR2 (9)       | billTo_companyTaxID     |
| Country      | Country of the billing address.                                                                                                                                                           | VARCHAR2 (2)       | billTo_country          |
| CustomerID   | Your identifier for the customer.                                                                                                                                                         | VARCHAR2 (30)      | billTo_customerID       |
| Email        | Customer's email address, including the full domain name.                                                                                                                                 | VARCHAR2 (1500)    | billTo_email            |
| FirstName    | First name of the billed customer.                                                                                                                                                        | VARCHAR2 60)       | billTo_firstName        |
| HostName     | DNS resolved hostname from  billTo_ipAddress.                                                                                                                                             | VARCHAR2 (255)     | billTo_hostname         |
| IPAddress    | Customer's IP address.                                                                                                                                                                    | VARCHAR2 (15)      | billTo_ipAddress        |
| LastName     | Last name of the billed customer.                                                                                                                                                         | VARCHAR2 (60)      | billTo_lastName         |
| MiddleName   | Middle name of the billed customer.                                                                                                                                                       | VARCHAR2 (60)      | billTo_middleName       |
| NameSuffix   | Suffix of billed customer.                                                                                                                                                                | VARCHAR2 (60)      | billTo_suffix           |
| PersonalID   | Personal identifier. This field is supported only for Redecard in Brazil for . Set this field to the Cadastro de Pessoas Fisicas (CPF), which is required for AVS for Redecard in Brazil. | VARCHAR2 (40)      | billTo_personalID       |
| Phone        | Customer's phone number.                                                                                                                                                                  | VARCHAR2 (100)     | billTo_phoneNumber      |
| State        | State or province of the billing address.                                                                                                                                                 | VARCHAR2 (64)      | billTo_state            |
| Title        | Title of the billed customer.                                                                                                                                                             | VARCHAR2 (30)      | billTo_title            |
| UserName     | Customer's user name.                                                                                                                                                                     | VARCHAR2 (30)      | billTo_customerUserName |
| Zip          | Zip/Postal code for the billing address. The postal code must consist of 5 to 9 digits.                                                                                                   | VARCHAR2 (10)      | billTo_postalCode       |
[Bill To Fields]

Case Management Fields {#ID-000011a2}
=====================================

| Field Name             | Description                                              |
|:-----------------------|:---------------------------------------------------------|
| ActiveNumberOfRules    | Indicates the number of rules in use in the profile.     |
| ActiveProfileDecision  | Decision of active profile.                              |
| ActiveProfileName      | Name of the active profile.                              |
| ActiveProfileScore     | Score of the active profile.                             |
| ActiveRuleDecision     | Summarizes the active rule decision.                     |
| ActiveRuleName         | Name of active rule as it appears in Profile Editor.     |
| ActiveRuleScore        | Score of the active rules.                               |
| OwnerOrganization      | Organization name of the reviewer assigned to the order. |
| OwnerUsername          | Specific reviewer assigned to the order.                 |
| PassiveNumberOfRules   | Indicates the number of rules in use in the profile.     |
| PassiveProfileDecision | Decision of passive profile.                             |
| PassiveProfileName     | Name of the passive profile.                             |
| PassiveProfileScore    | Score of the passive profile.                            |
| PassiveRuleDecision    | Summarizes the passive rule decision.                    |
| PassiveRuleName        | Name of passive rule as it appears in Profile Editor.    |
| PassiveRuleScore       | Score of the passive rules.                              |
| Priority               | Degree of importance assigned to the order.              |
| Queue                  | Order queue selected.                                    |
| ReviewDate             | Date and time of final decision.                         |
| ReviewDecision         | Summarizes final outcome for the order.                  |
| ReviewNotes            | Comments made by reviewer about the order.               |
[Case Management Fields (`Decision Manager`)]

Chargeback and Retrieval Fields {#ID-0000121b}
==============================================

| Field Name                       | Description                                                                                                                | Data Type (Length) |
|:---------------------------------|:---------------------------------------------------------------------------------------------------------------------------|:-------------------|
| AdjustmentAmount                 | Amount of the chargeback adjustment.                                                                                       | Number             |
| AdjustmentCurrency               | Currency of the chargeback adjustment.                                                                                     | VARCHAR2 (3)       |
| AdjustmentARN                    | Association reference number.                                                                                              | VARCHAR2 (64)      |
| CaseIdentifier                   | Numerical identifier created to represent a unique chargeback, representment, or other exception.                          | Number             |
| CaseNumber                       | Processor-assigned case number.                                                                                            | VARCHAR2 (64)      |
| CaseTime                         | The date that the case was opened.                                                                                         | Date               |
| CaseType                         | Description of the case type.                                                                                              | VARCHAR            |
| ChargebackAmount                 | Amount of the chargeback.                                                                                                  | Number             |
| ChargebackCurrency               | Chargeback currency code.                                                                                                  | VARCHAR2 (3)       |
| ChargebackMessage                | Text message from the issuer explaining the reason for the chargeback or other exception.                                  | VARCHAR2 (64)      |
| ChargebackReasonCode             | Association chargeback reason code.                                                                                        | VARCHAR2 (10)      |
| ChargebackReasonCode Description | Text description of the reason code.                                                                                       | VARCHAR2 (64)      |
| ChargebackTime                   | The date that the chargeback was originated by the issuing bank.                                                           | Date               |
| DocumentIndicator                | Indicates whether or not there are associated documents. Possible values: * `Y` * `N`                                      | VARCHAR2 (1)       |
| FeeAmount                        | Amount of the chargeback exception fee.                                                                                    | Number             |
| FeeCurrency                      | Currency code for the chargeback exception fee.                                                                            | VARCHAR2 (3)       |
| FinancialImpact                  | Indicates whether or not there is a financial impact. Possible values: * `Y` * `N`                                         | VARCHAR2 (1)       |
| FinancialImpactType              | Debit, credit, or none.                                                                                                    | VARCHAR2 (2)       |
| MerchantCategoryCode             | Four-digit number that the payment card industry uses to classify merchants into market segments.                          | VARCHAR2 (4)       |
| PartialIndicator                 | Flag indicating whether the transaction is enabled for partial chargeback.                                                 | VARCHAR2 (1)       |
| ResolutionTime                   | Resolution time in UTC.                                                                                                    | Date               |
| ResolvedToIndicato               | Indicates resolved to status of transaction. Possible values: * `B`: Bank * `M`: Merchant * `S`: Split `G`: General ledger | VARCHAR2 (20)      |
| RespondByDate                    | Date by which item must be submitted to the chargeback processor to allow sufficient time for representment.               | Date               |
| TransactionType                  | Capture type of the original transaction.                                                                                  | VARCHAR2 (6)       |
[Chargeback and Retrieval Fields]

Check Fields {#ID-000012ef}
===========================

| Field Name        | Description                                                                  | Data Type (Length)       |
|:------------------|:-----------------------------------------------------------------------------|:-------------------------|
| BankTransitNumber | Bank routing number.                                                         | Non-negative integer (9) |
| AccountEncoderID  | Identifier for the bank that provided the customer's encoded account number. | VARCHAR2 (3)             |
| SecCode           | Authorization method used for the transaction.                               | VARCHAR2 (3)             |
[Check Fields]

Conversion Fields {#ID-00001316}
================================

| Field Name       | Description                                              |
|:-----------------|:---------------------------------------------------------|
| ConversionDate   | Date order converted.                                    |
| NewDecision      | Reviewer evaluation result.                              |
| OriginalDecision | Order profile evaluation result.                         |
| Profile          | Order profile used to evaluate the order.                |
| Reviewer         | Person who evaluated order originally marked for review. |
| ReviewerComments | Additional information added by reviewer.                |
| Queue            | Review queue originally assigned to order.               |
[Conversion Fields]

Customer Fields {#ID-00001359}
==============================

| Field Name          | Description                                                                         |
|:--------------------|:------------------------------------------------------------------------------------|
| BillingAddress1     | First line of billing street address as it appears on credit card issuer's records. |
| BillingAddress2     | Additional address information.                                                     |
| BillingCity         | Billing address city.                                                               |
| BillingCompanyName  | Customer's company name.                                                            |
| BillingCountry      | Billing address country.                                                            |
| BillingEmail        | Customer's email address.                                                           |
| BillingFirstName    | First name of the billed customer.                                                  |
| BillingLastName     | Last name of the billed customer.                                                   |
| BillingPhone        | Customer's phone number.                                                            |
| BillingPostalCode   | Billing address postal code.                                                        |
| BillingState        | Billing address state or province.                                                  |
| CustomerID          | Your identifier for the customer.                                                   |
| ShippingAddress1    | First line of the shipping address.                                                 |
| ShippingAddress2    | Second line of the shipping address.                                                |
| ShippingCity        | Shipping address city.                                                              |
| ShippingCompanyName | Recipient's company name.                                                           |
| ShippingCountry     | Shipping address country.                                                           |
| ShippingFirstName   | First name of the recipient.                                                        |
| ShippingLastName    | Last name of the recipient.                                                         |
| ShippingPhone       | Recipient's phone number.                                                           |
| ShippingPostalCode  | Shipping address postal code.                                                       |
| ShippingState       | Shipping address state or province.                                                 |
[Customer Fields (`Decision Manager`)]

Deposit Fields {#ID-000013d8}
=============================

| Field Name              | Description                                                                                                                     | Data Type (Length) |
|:------------------------|:--------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| Amount                  | Amount of the deposit.                                                                                                          | Number             |
| Category                | Category of the deposit.                                                                                                        | VARCHAR2 (25)      |
| Currency                | Currency code of the deposit.                                                                                                   | VARCHAR2 (3)       |
| ExchangeRate            | Exchange rate. Includes a decimal point and up to 4 decimal places.                                                             | Number             |
| ExchangeRateDescription | Exchange rate description from the funding bank.                                                                                | VARCHAR2 (64)      |
| Identifier              | Unique reference number for this deposit.                                                                                       | VARCHAR2 (64)      |
| MerchantBankAcctLast4   | Bank account number to which the funds transfer will be deposited. For security purposes, all but the last 4 digits are masked. | VARCHAR2 (4)       |
| MerchantBankAcctName    | Name used on the bank account.                                                                                                  | VARCHAR2 (35)      |
| MerchantBankCode        | Routing number for the account to which the funds transfer will be deposited.                                                   | VARCHAR2 (35)      |
| MerchantBankCountry     | Country in which the bank is located. Use the two-character ISO Standard Country Codes.                                         | VARCHAR2 (2)       |
| MerchantBankName        | Bank's name.                                                                                                                    | VARCHAR2 (35)      |
| MerchantID              | Merchant ID.                                                                                                                    | VARCHAR2 (30)      |
| Method                  | Funds transfer method.                                                                                                          | VARCHAR2 (25)      |
| Status                  | Status of the deposit. Possible values: * `S`: Success * `P`: Pending * `F`: Failed                                             | VARCHAR2 (7)       |
| Time                    | Deposit time for the transaction in UTC.                                                                                        | Date               |
| TransferMessage         | Deposit transfer message provided by the processor.                                                                             | VARCHAR2 (64)      |
| Type                    | Description of events included in this funds transfer.                                                                          | VARCHAR2 (3)       |
[Deposit Fields]

Device Fields {#ID-0000146b}
============================

| Field Name | Description                                           | Data Type (Length) |
|:-----------|:------------------------------------------------------|:-------------------|
| DeviceID   | Identification number of device used for transaction. | VARCHAR2 (3)       |
[Device Fields]

Device Fingerprint Fields {#ID-00001484}
========================================

| Field Name                        | Description                                                                                                                       |
|:----------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| BrowserLanguage                   | Comma-separated list of languages preferred or supported by the browser.                                                          |
| CookiesEnabled                    | Indicates if cookies are enabled in customer's browser.                                                                           |
| DeviceFirstSeen                   | Date when the device was first encountered.                                                                                       |
| DeviceLatitude                    | Latitude of the GPS location of the device.                                                                                       |
| DeviceLongitude                   | Longitude of the GPS location of the device.                                                                                      |
| DeviceMatched                     | Longitude of the GPS location of the mobile device.                                                                               |
| Fingerprint/DeviceFingerprint     | Unique ID of a computer or other device.                                                                                          |
| FlashEnabled                      | Indicates if Flash is enabled in customer's browser.                                                                              |
| FlashOperatingSystem              | Device operating system as reported by Flash.                                                                                     |
| FlashVersion                      | Version of Flash installed on the device.                                                                                         |
| GPSAccuracy                       | Indicates the accuracy of the GPS location of the mobile device.                                                                  |
| ImagesEnabled                     | Indicates if images are enabled in customer's browser.                                                                            |
| Jailbreak/RootPrivileges          | Indicates if a mobile device has root privileges.                                                                                 |
| Jailbreak/RootReason              | Additional information describing elements on mobile device that triggered escalation to root privileges.                         |
| JavaScriptEnabled                 | Indicates if JavaScript is enabled in customer's browser.                                                                         |
| ProfiledURL                       | URL of profiled page.                                                                                                             |
| ProfilingDate/Time                | Time of device profiling.                                                                                                         |
| ProfilingDuration/RequestDuration | Total time in milliseconds to process the profiling request.                                                                      |
| ProxyIPAddress                    | IP address of proxy if available.                                                                                                 |
| ProxyIPAddressActivities          | Actions associated with the proxy IP address.                                                                                     |
| ProxyIPAddressAttributes          | Characteristics associated with the proxy IP address.                                                                             |
| ProxyServerType                   | Type of proxy server based on the HTTP header.                                                                                    |
| ScreenResolution                  | Screen resolution of the device.                                                                                                  |
| SmartID                           | Device identifier generated from attributes collected during profiling.                                                           |
| SmartIDConfidenceLevel            | Probability that the Smart ID is correctly identifying a returning device.                                                        |
| TimeOnPage                        | Time period in milliseconds that device profiling page displays on browser before it closes or user navigates away from the page. |
| TrueIPAddress                     | Customer's true IP address detected by the application.                                                                           |
| TrueIPAddressActivities           | Actions associated with the true IP address.                                                                                      |
| TrueIPAddressAttributes           | Characteristics associated with the true IP address.                                                                              |
| TrueIPAddressCity                 | City associated with the true IP address.                                                                                         |
| TrueIPAddressCountry              | Country associated with the true IP address.                                                                                      |
| TypeofBrowserAgent                | Indicates if a mobile device or a computer was used to initiate the session.                                                      |
[Device Fingerprint Fields (`Decision Manager`)]

Emailage Fields {#ID-00001535}
==============================

| Field Name                 | Description                                                                                                                          |
|:---------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| CompanyName                | Name of company to which the email belongs.                                                                                          |
| DomainCategory             | The category type for company's email domain.                                                                                        |
| DomainCompany              | Domain of company to which the email belongs.                                                                                        |
| DomainCorporate            | Indicates if domain is registered to a business.                                                                                     |
| DomainCountryCode          | Domain of country code to which the email belongs.                                                                                   |
| DomainCreationDate         | Creation date of the domain.                                                                                                         |
| DomainCreationDate-DaysOld | Number of days since email domain was created.                                                                                       |
| DomainExists               | Verifies if the email domain exists.                                                                                                 |
| DomainName                 | The email address domain name.                                                                                                       |
| DomainRisk                 | Provides risk level for the domain.                                                                                                  |
| EmailCreationDate          | Creation date of the email.                                                                                                          |
| EmailCreationDate-DaysOld  | Number of days since email account was created.                                                                                      |
| EmailExists                | Verifies if email address exists.                                                                                                    |
| EmailFirstSeenDate         | The oldest time stamp found for records associated with email address.                                                               |
| EmailFirstSeenDate-DaysOld | Number of days since email was first seen.                                                                                           |
| EmailLocation              | Location of the person who owns email address.                                                                                       |
| EmailNameMatch             | Indicates status of the name of the customer matching the email owner.                                                               |
| EmailOwnerName             | Name of the person who owns the email address.                                                                                       |
| EmailageReason             | Provides information relevant to understanding the Emailage Risk Score.                                                              |
| EmailageReasonDescription  | Provides information relevant to understanding the Emailage Risk Score.                                                              |
| EmailageRecommendation     | Recommendation based on results of other Emailage fields.                                                                            |
| EmailageRiskBand           | Indicates the number associated with certain Emailage Score ranges.                                                                  |
| EmailageScore              | Proprietary algorithm that calculates the fraud risk associated with an email address.                                               |
| FraudType                  | If multiple companies within the Emailage system marked the queried value as fraud, this field provides the most recent fraud type.  |
| Gender                     | Gender of the person who owns the email address.                                                                                     |
| IP Postal                  | Postal code associated with the IP address.                                                                                          |
| IPAnonymousProxy           | Indicates if the user's IP address is an anonymous proxy.                                                                            |
| IPCity                     | For U.S., city where the IP is located.                                                                                              |
| IPCountry                  | Name of the country associated with the IP.                                                                                          |
| IPRegion                   | For U.S., state where the IP is located.                                                                                             |
| IPReputation               | Reputation of the proxy, indicates the likelihood that the user's IP address is an open proxy.                                       |
| IPRiskLevel                | Provides the fraud risk for the IP Address.                                                                                          |
| LastConfirmationDate       | The last date the email address was queried in the Emailage system.                                                                  |
| PhoneSyntaxValidation      | Indicates if the phone syntax is valid.                                                                                              |
| SMLinks                    | Count of social media sites that match the queried email.                                                                            |
| SocialMediaFriends         | Total friends for the email owner located on social media sites.                                                                     |
| SourceIndustry             | If FraudType contains a value, this field provides the industry of the most recent company to mark the email as fraud or legitimate. |
| Title                      | Title of the email owner.                                                                                                            |
| Totalhits                  | Number of times the email address was queried in the Emailage system in a 7 day period.                                              |
| Uniquehits                 | Number of unique companies that queried the email address in the Emailage system in a 7 day period.                                  |
[Emailage Fields (`Decision Manager`)]

Event Fields {#ID-0000160e}
===========================

| Field Name       | Description                                                                                                | Data Type (Length) |
|:-----------------|:-----------------------------------------------------------------------------------------------------------|:-------------------|
| Amount           | Amount for the event.                                                                                      | Number (19)        |
| CurrencyCode     | Currency code for the event.                                                                               | VARCHAR2 (5)       |
| Event            | Type of event that occurred for the transaction.                                                           | VARCHAR2 (20)      |
| EventDate        | Date in GMT format that the event occurred. This field can be null for some event types, such as Declined. | Date               |
| ProcessorMessage | Additional information from the processor about the event, such as an error message or explanation.        | VARCHAR2 (255)     |
[Event Fields]

Exception Fields {#ID-00001643}
===============================

| Field Name                         | Description                                                                                                                     | Data Type (Length) |
|:-----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| Action                             | Brief description of the action.                                                                                                | VARCHAR2 (20)      |
| ClientID                           | ---                                                                                                                             | ---                |
| CYBSExceptionID                    | Assigned exception ID number.                                                                                                   | Number (18)        |
| DccLookupStatus                    | ---                                                                                                                             | ---                |
| DccExchangeRate                    | ---                                                                                                                             | ---                |
| DccMarginRate                      | ---                                                                                                                             | ---                |
| ExceptionAmount                    | Amount specified in the exception.                                                                                              | Number (19)        |
| ExceptionAmountCurrency            | Exception currency represented in ISO 4217:2008 alpha-3.                                                                        | VARCHAR2 (255)     |
| ExceptionCategory                  | Type of exception.                                                                                                              | VARCHAR2 (20)      |
| ExceptionDate                      | Date of exception.                                                                                                              | Number (18)        |
| ExceptionDescription               | ---                                                                                                                             | ---                |
| ExceptionDeviceHardwareRevision    | ---                                                                                                                             | ---                |
| ExceptionDeviceID                  | ---                                                                                                                             | ---                |
| ExceptionDeviceOS                  | ---                                                                                                                             | ---                |
| ExceptionDeviceOSVersion           | ---                                                                                                                             | ---                |
| ExceptionDeviceTerminalID          | ---                                                                                                                             | ---                |
| ExceptionMessage                   | Description of the exception.                                                                                                   | VARCHAR2 (255)     |
| ExceptionReasonCode                | Reason code for the error that occurred. This reason code is the same one that you receive in the reply or transaction receipt. | VARCHAR2 (60)      |
| ExceptionReasonDescription         | Description of exception reason.                                                                                                | VARCHAR2 (255)     |
| ExceptionStatus                    | Current status of the transaction.                                                                                              | VARCHAR2 (30)      |
| ExceptionStatusCode                | ---                                                                                                                             | ---                |
| ExceptionType                      | Type of exception.                                                                                                              | Number (26)        |
| FinancialStatus                    | Financial status of the transaction.                                                                                            | Number (5)         |
| LastActionDate                     | Date of last action on the transaction.                                                                                         | Date               |
| LocalCurrencyCode                  | Local currency code.                                                                                                            | ---                |
| NextActionDate                     | Date of next action on the transaction.                                                                                         | Date               |
| OriginalTransaction SubmissionDate | Date on which the transaction was submitted.                                                                                    | Date               |
| PartnerMerchantID                  | ---                                                                                                                             | ---                |
| PartnerMerchantName                | ---                                                                                                                             | ---                |
| PaymentNumber                      | Payment number.                                                                                                                 | VARCHAR2           |
| ProcessorCaseID                    | Processor-assigned case number.                                                                                                 | VARCHAR2 (30)      |
| ProcessorResponseCode              | Code returned directly from the processor for the exception that occurred.                                                      | VARCHAR2 (12)      |
| ReasonCode                         | Reason code for the exception that occurred.                                                                                    | VARCHAR2 (12)      |
| RetryCount                         | Total number of payments that are pending in retry mode.                                                                        | Number             |
| SchemeOperator                     | ---                                                                                                                             | ---                |
| SDKVersion                         | ---                                                                                                                             | ---                |
| SettlementProcessor                | Name of settlement processor.                                                                                                   | VARCHAR2 (40)      |
| StorageMechanism                   | ---                                                                                                                             | ---                |
[Exception Fields]

Fee Fields {#ID-00001760}
=========================

| Field Name                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Data Type (Length) |
|:--------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| AcquirerInterchangeAmount                   | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ---                |
| AssessmentAmount                            | Amount of the assessment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Number             |
| AssessmentCurrency                          | Currency of the assessment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | VARCHAR2 (3)       |
| BillingCycle                                | Billing cycle of the merchant. Possible values: * `daily` * `weekly` * `monthly`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | VARCHAR2 (25)      |
| BillingType                                 | Billing type of the merchant. Possible values: * `discount` * `interchangePlus` * `serviceFee` * `other`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | VARCHAR2 (25)      |
| ClearedInterchangeLevel                     | Code for the clearing level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | VARCHAR2 (3)       |
| ConversionFee                               | Fee amount added for currency conversion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | ---                |
| ConversionFeeCurrency                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ---                |
| DiscountAmount                              | DiscountRate \*TransactionAmount. This value includes 4 decimal points.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Number             |
| DiscountCurrency                            | Currency of the discount.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | VARCHAR2 (3)       |
| DiscountRate                                | Discount rate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Number             |
| DowngradeReasonCode                         | Reason for downgrade. Possible values: * `1`: Transaction exceeded timeliness. * `2`: Authorization code is missing. * `8`: POS entry mode does not qualify. * `9`: POS condition code does not qualify. * `A`: POS terminal capability does not qualify. * `D`: Mail/phone/e-commerce indicator does not qualify. * `K`: Transaction cleared as intraregional. * `L`: Transaction cleared as interregional. * `R`: Reclassification. * `U`: UK domestic. * `V`: German domestic. * `W`: Transaction cleared as world signia. * `X`: Did not qualify at merchant price level. | VARCHAR2 (6)       |
| ExchangeRate                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ---                |
| GrossInterchangeAmount                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ---                |
| InterchangeAmount                           | Final amount of transaction after the interchange rates are applied.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Number             |
| InterchangeCurrency                         | ISO currency code for the currency of the clearing rate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | VARCHAR2 (3)       |
| InterchangeRate                             | Interchange rate for the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Number             |
| IssuerInterchangeAmount                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ---                |
| MerchantID                                  | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ---                |
| OtherInterchangeAmount                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ---                |
| PerItemFeeAmount                            | Fee for a single item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Number             |
| PerItemFeeCurrency                          | Currency for a single item fee.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | VARCHAR2 (3)       |
| PricedInterchangeLevel                      | Interchange flat rate that was assigned when you set up your account. This value includes 4 decimal points.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | VARCHAR2 (3)       |
| ReimbursementFee                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ---                |
| ReimbursementFeeDebit CreditIndicator       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ---                |
| ServiceFeeAmount                            | Amount of service fee for transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Number             |
| ServiceFeeAmountCcy                         | Currency of the service fee.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | VARCHAR2 (3)       |
| ServiceFeeFixedAmount                       | Amount of the fixed service fee for the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Number             |
| ServiceFeeFixedAmountCcy                    | Currency of the fixed service fee.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | VARCHAR2 (3)       |
| ServiceFeeRate                              | Percentage rate of the service fee.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Number             |
| SettlementAmount                            | Amount of the settlement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Number             |
| SettlementCurrency                          | Currency of the settlement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | VARCHAR2 (3)       |
| SettlementTime                              | Time the settlement was processed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Date               |
| SettlementTimeZone                          | Time zone of the settlement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | VARCHAR2 (6)       |
| SourceDescriptor                            | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | VARCHAR2 (6)       |
| TotalFeeAmount                              | Total amount of all fee transactions for the specified date range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Number             |
| TotalFeeCurrency                            | Currency for all fee transactions for the specified date range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | VARCHAR2 (3)       |
| TransactionIntegrityFee                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ---                |
| TransactionIntegrityFeeDebitCreditIndicator | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ---                |
[Fee Fields]

Fee Summary Fields {#ID-000018c3}
=================================

| Field Name        | Description                     |
|:------------------|:--------------------------------|
| CardType          | Card type.                      |
| Count             | Count.                          |
| FeeDescription    | Fee description.                |
| FeeType           | Fee type.                       |
| FundingCurrency   | Currency in which fees applied. |
| PaymentMethod     | Payment method used.            |
| PercentageFee     | Percentage fee.                 |
| PerItemFee        | Fee charged per item.           |
| TotalFeeAmount    | Total fee amount.               |
| TransactionAmount | Transaction amount.             |
| TransactionType   | Transaction type.               |
[Fee Summary Fields]

Funding Fields {#ID-00001923}
=============================

| Field Name                   | Description                                                                     | Data Type (Length) |
|:-----------------------------|:--------------------------------------------------------------------------------|:-------------------|
| CurrencyExchange Description | Exchange rate description from the processor.                                   | VARCHAR2 (64)      |
| CurrencyExchangeRate         | Exchange rate for converting from transaction currency to funding currency.     | Number             |
| FeeAmount                    | Fee for the transaction.                                                        | Number             |
| FeeCurrency                  | Fee currency represented in ISO 4217:2008 alpha-3.                              | VARCHAR2 (3)       |
| FeeDescription               | Fee description from the processor.                                             | VARCHAR2 (64)      |
| FundingAccountSuffix         | Last 4 digits of funding account.                                               | VARCHAR2 (40)      |
| FundingAmount                | Funding amount of the transaction.                                              | Number             |
| FundingBankCode              | Bank code of the funding bank.                                                  | ---                |
| FundingBankCountry           | Bank country of the funding bank represented in ISO 3166-1 alpha-3.             | ---                |
| FundingBankName              | Name of bank funding the transaction.                                           | ---                |
| FundingCurrency              | Funding currency represented in ISO 4217:2008 alpha-3.                          | VARCHAR2 (3)       |
| FundingDate                  | Funding date of the transaction.                                                | Date               |
| FundingIdentification Number | Funding identification for the funding of the transaction.                      | VARCHAR2 (64)      |
| FundingProcessor Message     | Funding response message from the processor.                                    | VARCHAR2 (64)      |
| FundingTransferMessage       | Funding transfer message provided by the processor.                             | VARCHAR2 (64)      |
| ProcessorResponseCode        | Funding response code from the processor.                                       | VARCHAR2 (10)      |
| Status                       | Funding status. Possible values: * `S` (success) * `P` (pending) * `F` (failed) | VARCHAR2 (10)      |
[Funding Fields]

Fund Transfer Fields {#ID-000019b7}
===================================

| Field Name     | Description                                          | Data Type (Length) |
|:---------------|:-----------------------------------------------------|:-------------------|
| BankCheckDigit | Code used to validate the customer's account number. | CHAR (2)           |
| IbanIndicator  | International Bank Account Number (IBAN).            | CHAR (1)           |
[Fund Transfer Fields]

Gift Card Fields {#c_Gift_Card_Fields}
======================================

| Field Name      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Data Type (Length) | Simple Order API Value   |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:-------------------------|
| CurrentBalance  | Current gift card balance in your local currency.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | String (12)        | giftCard_currentBalance  |
| PreviousBalance | Previous gift card balance in your local currency. This value was the gift card balance before the concurrent transaction was applied to the gift card. This field is supported only on ValueLink. For example, when a customer purchases a gift card and uses the gift card to purchase a product at the same time, the response message includes: * Previous gift card balance, which was the balance before the purchase of the product * Current gift card balance, which is the balance after the purchase of the product | String (12)        | giftCard_previousBalance |
| RedemptionType  | Type of redemption. Possible values: * `CASHOUT` * `REDEMPTION` * `REDEMPTION_ PARTIAL_ ALLOWED` (default) This field is supported only on ValueLink.                                                                                                                                                                                                                                                                                                                                                                          | String (26)        | giftCard_previousBalance |
[Gift Card Fields]

Health Care Fields {#c_Healthcare_Fields}
=========================================

| Field Name   | Description                                                                                                         | Data Type (Length) |
|:-------------|:--------------------------------------------------------------------------------------------------------------------|:-------------------|
| Amount       | Amount of the healthcare payment.                                                                                   | VARCHAR2 (13)      |
| AmountType   | Type of healthcare payment. For example: * `healthcare` * `dental` * `clinic` {#c_Healthcare_Fields_ul_mxz_vmh_krb} | VARCHAR2 (35)      |
| Currency     | Currency used in transaction.                                                                                       | VARCHAR2 (3)       |
| IndustryType | Type of industry for the transaction.                                                                               | VARCHAR2 (20)      |
[Healthcare Fields]

Invoice Fields {#ID-00001a06}
=============================

| Field Name              | Definition                          | Data Type (Length) |
|:------------------------|:------------------------------------|:-------------------|
| BillingGroupDescription | Description of the billing group.   | VARCHAR2 (50)      |
| NotProcessed            | Number of unprocessed transactions. | Number             |
| OrganizationID          | Merchant ID.                        | VARCHAR2 (30)      |
| PerformedServices       | ICS service name.                   | VARCHAR2 (30)      |
| Processed               | Number of processed transactions.   | Number             |
| Total                   | Invoice count.                      | Number             |
[Invoice Fields]

Japanese Payment (JP) Fields {#ID-00001a44}
===========================================

| Field Name                 | Description                                                                                           |
|:---------------------------|:------------------------------------------------------------------------------------------------------|
| Amount                     | Transaction grand total.                                                                              |
| AuthForward                | Name of Japanese acquirer that processed transaction. Available only for CCS (CAFIS) and JCN Gateway. |
| AuthorizationCode          | Transaction authorization code.                                                                       |
| CardSuffix                 | Last four digits of card.                                                                             |
| Currency                   | Currency used in transaction.                                                                         |
| CustomerFirstName          | Customer first name.                                                                                  |
| CustomerLastName           | Customer last name.                                                                                   |
| Date                       | Date of transaction.                                                                                  |
| Gateway                    | Name of gateway used to process transaction.                                                          |
| JPOInstallmentMethod       | Number of payment installments (Japanese payment method only).                                        |
| JPOPaymentMethod           | Type of Japanese payment method used.                                                                 |
| MerchantID                 | Gateway merchant identifier.                                                                          |
| MerchantReferenceNumber    | Merchant order reference or tracking number.                                                          |
| NetworkTokenTransType      | Network token transaction type.                                                                       |
| PaymentMethod              | Method of payment.                                                                                    |
| RequestID                  | Client request identifier.                                                                            |
| SubscriptionID             | Customer profile identifier for requested service.                                                    |
| Time                       | Time of transaction.                                                                                  |
| TransactionReferenceNumber | Reference number used to reconcile gateway reports with processor reports.                            |
| TransactionType            | Type of transaction.                                                                                  |
[Japanese Payment Fields]

Line Item Fields {#ID-00001ab9}
===============================

| Field Name         | Description                                                                               | Data Type (Length) | Simple Order API Value |
|:-------------------|:------------------------------------------------------------------------------------------|:-------------------|:-----------------------|
| FulfillmentType    | Information about the product code used for the line item.                                | VARCHAR2 (2)       | ---                    |
| InvoiceNumber      | Invoice number for order.                                                                 | VARCHAR2 (30)      | item_#_invoiceNumber   |
| MerchantProductSku | Identification code for the product.                                                      | VARCHAR2 (255)     | item_#_productSKU      |
| Number             | Number of the line item in an order.                                                      | Number             | ---                    |
| ProductCode        | Used to determine product category: electronic, handling, physical, service, or shipping. | VARCHAR2 (255)     | item_#_productCode     |
| ProductName        | Name of product.                                                                          | VARCHAR2 (255)     | item_#_productName     |
| Quantity           | Quantity of product.                                                                      | Number (12)        | item_#_quantity        |
| TaxAmount          | Total tax to apply to the product.                                                        | Number (19)        | item_#_taxAmount       |
| UnitPrice          | Per-item price of the product.                                                            | Number             | item_#_unitPrice       |
[Line Item Fields]

Mark As Suspect Fields {#ID-00001b34}
=====================================

| Field Name      | Description                             |
|:----------------|:----------------------------------------|
| MarkingDate     | Date the order was marked.              |
| MarkingNotes    | Notes about the customer or the order.  |
| MarkingReason   | Selected reason for marking the order.  |
| MarkingUserName | Identity of the user marking the order. |
[Mark As Suspect Fields (`Decision Manager`)]

Merchant-Defined Data Fields {#ID-00001b58}
===========================================

| Field Name           | Description                                  | Data Type (Length) |
|:---------------------|:---------------------------------------------|:-------------------|
| MerchantDefinedData1 | Field that you can use to store information. | VARCHAR2 (1175)    |
| MerchantDefinedData2 | Field that you can use to store information. | VARCHAR2 (1175)    |
| MerchantDefinedData3 | Field that you can use to store information. | VARCHAR2 (1175)    |
| MerchantDefinedData4 | Field that you can use to store information. | VARCHAR2 (1175)    |
[Merchant-Defined Data Fields (`Decision Manager`)]

Merchant Defined Data Fields {#ID-00001b88}
===========================================

| Field Name                  | Description                                                      | Data Type (Length) | Simple Order API Value     |
|:----------------------------|:-----------------------------------------------------------------|:-------------------|:---------------------------|
| Merchant DefinedData_field1 | Fields that you can use to store information (Field1 - Field20). | VARCHAR2 (1175)    | merchantDefinedData_field1 |
[Merchant Defined Data Fields]

Network Token Life-Cycle Management Fields {#lcm-net-tkn-fields}
================================================================

Fields in this group prepend the field name with "LifeCycleManagementEvent", "NetworkToken", or "TMSToken":

|          Group           | Field Name                | Description                                                                         |
|--------------------------|:--------------------------|:------------------------------------------------------------------------------------|
| LifeCycleManagementEvent | LCMEventDateProcessed     | Date that the Life-Cycle Management event was fully processed.                      |
| LifeCycleManagementEvent | LCMEventStatus            | Processing status of the Life-Cycle Management event.                               |
| LifeCycleManagementEvent | LCMEventStatusText        | Free-formatted text field detailing the process of the Life-Cycle Management event. |
| LifeCycleManagementEvent | LCMEventType              | Type of Life-Cycle Management event that has been applied.                          |
| LifeCycleManagementEvent | LCMEventUniqueID          | Unique identifier for the Life-Cycle Management event applied.                      |
| NetworkToken             | CardExpiryDate            | Expiration date of the card.                                                        |
| NetworkToken             | CardSuffix                | Last 4 digits of the card.                                                          |
| NetworkToken             | PAR                       | A unique reference that identifies the underlying payment account.                  |
| NetworkToken             | TokenExpiryDate           | Expiration date of the network token.                                               |
| NetworkToken             | TokenModifiedDate         | Date that the network token was modified.                                           |
| NetworkToken             | TokenRequestorID          | Identifier of the wallet that the network token belongs to.                         |
| NetworkToken             | TokenService              | Token service that provisioned the network token.                                   |
| NetworkToken             | TokenState                | State of the network token.                                                         |
| NetworkToken             | TokenSuffix               | Last 4 digits of the network token.                                                 |
| NetworkToken             | TokenUniqueID             | Unique Identifier for the network token.                                            |
| TMSToken                 | Creator                   | Organization ID or merchant ID that created the `TMS` token.                        |
| TMSToken                 | InstrumentIdentifierID    | Unique identifier for the instrument identifier.                                    |
| TMSToken                 | InstrumentIdentifierState | Current state of the instrument identifier token.                                   |
| TMSToken                 | VaultID                   | Unique identifier for the vault that the token belongs to.                          |
[Network Token Life-Cycle Management Fields]

Order Fields {#ID-00001bab}
===========================

| Field Name              | Description                                                          |
|:------------------------|:---------------------------------------------------------------------|
| ConnectionMethod        | Method by which order was sent to `Decision Manager`.                |
| GiftWrap                | Indicates if the customer requested gift wrapping for this purchase. |
| MerchantID              | Merchant ID.                                                         |
| MerchantReferenceNumber | Order or tracking number.                                            |
| Price                   | Price of each item.                                                  |
| ProductCode             | Type of product in the offer.                                        |
| ProductName             | Name of the product.                                                 |
| ProductSKU              | Merchant's product.                                                  |
| Quantity                | Quantity of product being purchased.                                 |
| ReasonCode              | One-digit code that indicates if the entire request was successful.  |
| ReplyCode               | One-digit code that indicates if the entire request was successful.  |
| ReplyFlag               | One-word description of the result of the entire request.            |
| ReplyMessage            | Message that explains the reply flag.                                |
| RequestID               | Identifier for the request generated by the client.                  |
| ReturnAccepted          | Indicates if returns are accepted for this order.                    |
| ShippingMethod          | Shipping method for the product.                                     |
| TaxTax                  | Total tax to apply to the product.                                   |
| TransactionDate         | Date of transaction.                                                 |
[Order Fields (`Decision Manager`)]

Payer Authentication Detail Request Fields {#ID-00001c16}
=========================================================

| Field Name      | Description                               |
|:----------------|:------------------------------------------|
| MerchantID      | Merchant ID used for the transactions.    |
| RequestID       | Identifier for the transaction request.   |
| TransactionDate | Date on which the transaction took place. |
| TransactionID   | Identifier of transaction.                |
| TransactionType | Transaction type.                         |
[Payer Authentication Detail Request Fields]

Payer Authentication Request Fields {#ID-00001c3f}
==================================================

| Field Name     | Description                           |
|:---------------|:--------------------------------------|
| AccountID      | Account identifier.                   |
| AcquirerBin    | Acquiring bank identification number. |
| CardExpiry     | Card expiration.                      |
| Country        | Country.                              |
| MerchantID     | Merchant identifier.                  |
| MerchantName   | Merchant name.                        |
| MerchantURL    | Merchant URL.                         |
| PurchaseAmount | Purchase amount.                      |
| PurchaseDate   | Purchase date.                        |
| PurchaseXID    | Purchase XID.                         |
[Payer Authentication Request Fields]

Payer Authentication Response Fields {#ID-00001c81}
===================================================

| Field Name        | Description                           |
|:------------------|:--------------------------------------|
| AcquirerBin       | Acquiring bank identification number. |
| AuthTime          | Authorization time.                   |
| CAVV              | CAVV.                                 |
| ECI               | Ecommerce indicator.                  |
| MerchantID        | Merchant identifier.                  |
| PurchaseAmount    | Purchase amount.                      |
| PurchaseDate      | Purchase date.                        |
| PurchaseXID       | Purchase XID.                         |
| TransactionStatus | Transaction status.                   |
[Payer Authentication Response Fields]

Payment Data Fields {#ID-00001cbe}
==================================

| Field Name                     | Description                                                                                                                                                                                    | Data Type (Length)       |
|:-------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| AAV_CAVV                       | Optional authentication data that you can receive after the customer is authenticated.                                                                                                         | VARCHAR2 (3)             |
| ACHVerificationResult          | Raw result of the ACH Verification service.                                                                                                                                                    | ---                      |
| ACHVerificationResult Mapped   | Mapped result of the ACH Verification service.                                                                                                                                                 | ---                      |
| AcquirerMerchantID             | ---                                                                                                                                                                                            | ---                      |
| AcquirerMerchantNumber         | Identifier that was assigned to you by your acquirer. This value must be printed on the receipt.                                                                                               | String (15)              |
| Amount                         | Grand total for the order.                                                                                                                                                                     | Number (19)              |
| AuthIndicator                  | ---                                                                                                                                                                                            | ---                      |
| AuthorizationCode              | Authorization code for the payment.                                                                                                                                                            | VARCHAR2 (15)            |
| AuthorizationType              | Authorization type of the payment.                                                                                                                                                             | VARCHAR2 (1)             |
| AuthReversalAmount             | ---                                                                                                                                                                                            | ---                      |
| AuthReversalResult             | ---                                                                                                                                                                                            | ---                      |
| AVSResult                      | Raw code for Address Verification Service result for the payment.                                                                                                                              | VARCHAR2 (10)            |
| AVSResultMapped                | Address Verification Service result for the payment.                                                                                                                                           | VARCHAR2 (5)             |
| BalanceAmount                  | Remaining balance on the account.                                                                                                                                                              | Number (19)              |
| BalanceCurrencyCode            | Currency of the remaining balance on the account.                                                                                                                                              | VARCHAR2 (3)             |
| BankAccountName                | Name of account holder.                                                                                                                                                                        | VARCHAR2 (90)            |
| BankCode                       | Bank code or sort code for the account if a bank account was used for the transaction.                                                                                                         | VARCHAR2 (15)            |
| BatchFilesID                   | ---                                                                                                                                                                                            | ---                      |
| BinNumber                      | Bank identification number.                                                                                                                                                                    | VARCHAR2 (8)             |
| CardCategory                   | Type of card used in the transaction.                                                                                                                                                          | VARCHAR2 (10)            |
| CardCategoryCode               | Category code of card used in the transaction.                                                                                                                                                 | ---                      |
| CardPresent                    | Indicates whether the card is present at the time of the transaction.                                                                                                                          | String (1)               |
| CardVerificationMethod         | ---                                                                                                                                                                                            | ---                      |
| CurrencyCode                   | Currency code for the payment.                                                                                                                                                                 | VARCHAR2 (3)             |
| CustomerAccountID              | ---                                                                                                                                                                                            | ---                      |
| CVResult                       | CVN result code.                                                                                                                                                                               | ---                      |
| DCCIndicator                   | Flag that indicates whether DCC is being used for the transaction.                                                                                                                             | VARCHAR2 (1)             |
| ECI                            | Optional information that you can receive if you use the Payer Authentication service.                                                                                                         | Number (5)               |
| eCommerceIndicator             | Type of eCommerce transaction.                                                                                                                                                                 | CHAR (1)                 |
| EMVRequestFallback             | Indicates that a fallback method was used to enter credit card information into the POS terminal.                                                                                              | String (5)               |
| EVEmail                        | Mapped Electronic Verification response code for the customer's email address.                                                                                                                 | VARCHAR2 (5)             |
| EVEmailRaw                     | Raw Electronic Verification response code from the processor for the customer's email address.                                                                                                 | VARCHAR2 (10)            |
| EventType                      | Type of event that occurred for the transaction.                                                                                                                                               | ---                      |
| EVName                         | Mapped Electronic Verification response code for the customer's name.                                                                                                                          | VARCHAR2 (5)             |
| EVNameRaw                      | Raw Electronic Verification response code from the processor for the customer's last name.                                                                                                     | VARCHAR2 (10)            |
| EVPhoneNumber                  | Mapped Electronic Verification response code for the customer's phone number.                                                                                                                  | VARCHAR2 (5)             |
| EVPhoneNumberRaw               | Raw Electronic Verification response code from the processor for the customer's phone number.                                                                                                  | VARCHAR2 (10)            |
| EVPostalCode                   | Mapped Electronic Verification response code for the customer's postal code.                                                                                                                   | VARCHAR2 (5)             |
| EVPostalCodeRaw                | Raw Electronic Verification response code from the processor for the customer's postal code.                                                                                                   | VARCHAR2 (10)            |
| EVStreet                       | Mapped Electronic Verification response code for the customer's street address.                                                                                                                | VARCHAR2 (5)             |
| EVStreetRaw                    | Raw Electronic Verification response code from the processor for the customer's street address.                                                                                                | VARCHAR2 (10)            |
| ExchangeRate                   | Exchange rate.                                                                                                                                                                                 | Number (27)              |
| ExchangeRateDate               | Time stamp for the exchange rate.                                                                                                                                                              | Date                     |
| GrandTotal                     | Grand total amount for the order, including tax, for requests that do not contain payment information.                                                                                         | Number (19)              |
| IssuerResponseCode             | Additional authorization code that must be printed on the receipt when returned by the processor.                                                                                              | VARCHAR2 (15)            |
| JpoJccaTerminalID              | Unique terminal identifier provided by Japan Credit Card Association (JCCA).                                                                                                                   | ---                      |
| JpoPaymentMethod               | Indicates Japanese payment option being used.                                                                                                                                                  | ---                      |
| MandateReferenceNumber         | ---                                                                                                                                                                                            | ---                      |
| MerchantCategoryCode           | Four-digit number that payment card industry uses to classify merchants into market segments.                                                                                                  | ---                      |
| NetworkCode                    | ---                                                                                                                                                                                            | ---                      |
| NumberOfInstallments           | Total number of installments when making payments in installments.                                                                                                                             | VARCHAR2 (3)             |
| OriginalAmount                 | ---                                                                                                                                                                                            | ---                      |
| OriginalCurrency               | ---                                                                                                                                                                                            | ---                      |
| PaymentProcessor               | Name of payment processor.                                                                                                                                                                     | VARCHAR2 (40)            |
| PaymentProductCode             | Type of payment product used by the consumer to pay on a payment provider's site, such as installments or bank transfer.                                                                       | ---                      |
| PaymentRequestID               | Original request ID for the purchase.                                                                                                                                                          | Number (26)              |
| PinType                        | Method that was used to verify the cardholder's identity.                                                                                                                                      | Integer (1)              |
| POSCatLevel                    | Type of cardholder-activated terminal.                                                                                                                                                         | Non-negative Integer (1) |
| POSEntryMode                   | Method of entering credit card information into the POS terminal.                                                                                                                              | String (11)              |
| POSEnvironment                 | Operating environment.                                                                                                                                                                         | String (1)               |
| POSTerminalCapability          | POS terminal's capability.                                                                                                                                                                     | ---                      |
| ProcessorMID                   | ---                                                                                                                                                                                            | ---                      |
| ProcessorResponseCode          | The error message sent directly from the bank.                                                                                                                                                 | VARCHAR2 (60)            |
| ProcessorResponseID            | Response ID sent from the processor.                                                                                                                                                           | VARCHAR2 (50)            |
| ProcessorTID                   | Transaction identification (TID) that is used to identify and track a transaction throughout its life cycle.                                                                                   | VARCHAR2 (60)            |
| ProcessorTransactionID         | ---                                                                                                                                                                                            | ---                      |
| RequestedAmount                | Amount requested to be authorized.                                                                                                                                                             | Number (19)              |
| RequestedAmountCurrencyCode    | Currency for the amount requested to be authorized.                                                                                                                                            | VARCHAR2 (5)             |
| RoutingNetworkType             | Processor scheme used for routing the transaction.                                                                                                                                             | String (1)               |
| SalesSlipNumber                | Transaction identifier that you generate.                                                                                                                                                      | ---                      |
| ShopName                       | Name of the shop.                                                                                                                                                                              | ---                      |
| ShopNameKatakana               | Shop name displayed in katakana characters.                                                                                                                                                    | ---                      |
| ShopNameLocal                  | Shop name displayed in local dialect.                                                                                                                                                          | ---                      |
| SolutionType                   | Type of digital payment used. Valid values: 001 006 007                                                                                                                                        | ---                      |
| StoreAndForwardIndicator       | When connectivity is unavailable, the client software that is installed on the POS terminal can store a transaction in its memory and send it for authorization when connectivity is restored. | String (5)               |
| SubMerchantCity                | Sub-merchant's city.                                                                                                                                                                           | ---                      |
| SubMerchantCountry             | Sub-merchant's country.                                                                                                                                                                        | ---                      |
| SubMerchantEmail               | Sub-merchant's email address.                                                                                                                                                                  | ---                      |
| SubMerchantID                  | Identifier assigned to sub-merchant.                                                                                                                                                           | ---                      |
| SubMerchantName                | Sub-merchant's name.                                                                                                                                                                           | ---                      |
| SubMerchantPhone               | Sub-merchant's phone number.                                                                                                                                                                   | ---                      |
| SubMerchantPostalCode          | Sub-merchant's ZIP/Postal code.                                                                                                                                                                | ---                      |
| SubMerchantState               | Sub-merchant's state.                                                                                                                                                                          | ---                      |
| SubMerchantStreet              | First line of sub-merchant's street address.                                                                                                                                                   | ---                      |
| SubsequentAuth                 | Indicates whether the transaction is a merchant-initiated transaction or subsequent authorization.                                                                                             | String (1)               |
| SubsequentAuthFirst            | Indicates whether the customer initiated the transaction and whether the credentials are stored for future authorizations.                                                                     | String (1)               |
| SubsequentAuthReason           | Reason for the merchant-initiated transaction or incremental authorization.                                                                                                                    | String (1)               |
| SubsequentAuthStoredCredential | Indicates whether you obtained the payment information from credentials on file (COF) instead of from the customer.                                                                            | String (1)               |
| SubsequentAuthTransactionID    | Network transaction identifier that was returned for a previous authorization in the series.                                                                                                   | String (15)              |
| TargetAmount                   | Converted amount.                                                                                                                                                                              | Number (19)              |
| TargetCurrency                 | Billing currency.                                                                                                                                                                              | VARCHAR2 (3)             |
| TerminalIDAlternate            | Identifier for an alternate terminal at your retail location.                                                                                                                                  | String (8)               |
| TotalTaxAmount                 | Total tax amount for all of the line items in the transaction.                                                                                                                                 | Number (19)              |
| TransactionRefNumber           | Reference number for the transaction.                                                                                                                                                          | VARCHAR2 (60)            |
| XID                            | Optional transaction identifier generated by Payer Authentication that you can receive when the customer is enrolled and when validation is successful.                                        | VARCHAR2 (40)            |
[Payment Data Fields]

Payment Method Fields {#ID-00002031}
====================================

| Field Name             | Description                                                                                                                                            | Data Type (Length) | Simple Order API Value |
|:-----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:-----------------------|
| AccountEncoderID       | ---                                                                                                                                                    | ---                | AccountEncoder ID      |
| AccountSuffix          | Last four digits of the customer's payment account number.                                                                                             | VARCHAR2 (4)       | card_suffix            |
| AccountType            | ---                                                                                                                                                    | ---                | AccountType            |
| BankAccountName        | Bank's account name.                                                                                                                                   | VARCHAR2 (90)      | BankAccount Name       |
| BankCheckDigit         | ---                                                                                                                                                    | ---                | BankCheckDigit         |
| BankCity               | ---                                                                                                                                                    | ---                | BankCity               |
| BankCode               | Bank's code. Used for some countries when you are not using the IBAN. Contact Customer Support for required country-specific bank account information. | VARCHAR2 (15)      | BankInfo_bankCode      |
| BankCountry            | ---                                                                                                                                                    | ---                | BankCountry            |
| BankNumber             | ---                                                                                                                                                    | ---                | BankNumber             |
| BankTransit Number     | ---                                                                                                                                                    | ---                | BankTransit Number     |
| BoletoBarCode Number   | Numeric representation of the boleto barcode.                                                                                                          | VARCHAR2 (50)      | ---                    |
| BoletoNumber           | Boleto Bancário payment number.                                                                                                                        | VARCHAR2 (50)      | boletoNumber           |
| BranchCode             | ---                                                                                                                                                    |                    | BranchCode             |
| CardCategory           | Type of card used.                                                                                                                                     | VARCHAR2 (10)      | cardCategory           |
| CardCategoryCode       | Code for card type used.                                                                                                                               | VARCHAR2 (10)      | ---                    |
| CardType               | Type of card to authorize.                                                                                                                             | VARCHAR2 (5)       | card_cardType          |
| CheckNumber            | Check number.                                                                                                                                          | VARCHAR2 (10)      | check_checkNumber      |
| EffectiveDate          | ---                                                                                                                                                    | ---                | effectiveDate          |
| ExpirationMonth        | Two-digit month in which the credit card expires.                                                                                                      | VARCHAR2 (4)       | card_expirationMonth   |
| ExpirationYear         | Four-digit year in which the credit card expires.                                                                                                      | VARCHAR2 (4)       | card_expirationYear    |
| IbanIndicator          | ---                                                                                                                                                    | ---                | IbanIndicator          |
| IssueNumber            | Number of times a Maestro (UK Domestic) card has been issued to the account holder.                                                                    | VARCHAR2 (5)       | card_issueNumber       |
| MandateId              | Identification reference for the direct debit mandate.                                                                                                 | VARCHAR2 (35)      | ---                    |
| MandateType            | Type of mandate.                                                                                                                                       | VARCHAR2 (20)      | ---                    |
| NetworkToken TransType | ---                                                                                                                                                    | ---                | NetworkToken TransType |
| OverridePayment Method | ---                                                                                                                                                    | ---                | ---                    |
| SignatureDate          | Date of signature.                                                                                                                                     | Date               | ---                    |
| StartMonth             | Month of the start of the Maestro (UK Domestic) card validity period.                                                                                  | VARCHAR2 (4)       | card_startMonth        |
| StartYear              | Year of the start of the Maestro (UK Domestic) card validity period.                                                                                   | VARCHAR2 (4)       | card_startYear         |
| SwiftCode              | ---                                                                                                                                                    | ---                | SwiftCode              |
| TypeDescription        | ---                                                                                                                                                    | ---                | ---                    |
| WalletType             | Type of wallet.                                                                                                                                        | VARCHAR2 (20)      | partnerSolutionID      |
[Payment Method Fields]

Payment Fields {#ID-000021aa}
=============================

| Field Name             | Description                                                                     |
|:-----------------------|:--------------------------------------------------------------------------------|
| AccountSuffix          | Last four digits of the customer's payment account number.                      |
| AuthEVAddress1         | Mapped Electronic Verification response code for the customer's street address. |
| AuthEVEmail            | Mapped Electronic Verification response code for the customer's email address.  |
| AuthEVLastName         | Mapped Electronic Verification response code for the customer's last name.      |
| AuthEVPhone            | Mapped Electronic Verification response code for the customer's phone number.   |
| AuthEVPostalCode       | Mapped Electronic Verification response code for the customer's postal code.    |
| AVSResultMapped        | Address Verification Service result for the payment.                            |
| CardBIN                | Eight-digit card issuer bank identification number.                             |
| CardBINCountry         | Country associated with the origin of the card.                                 |
| CardIssuer             | Name of the bank.                                                               |
| CardScheme             | Subtype of card account.                                                        |
| CardType               | Type of payment card account.                                                   |
| CardVerificationResult | Raw result of the ACH Verification service.                                     |
| ECommerceIndicator     | Type of eCommerce transaction.                                                  |
| LocalCurrencyCode      | Your local pricing currency code.                                               |
| LocalOrderAmount       | Amount in your original local pricing currency.                                 |
| OrderAmount            | Grand total amount or the individual line-item amounts.                         |
| OrderCurrency          | Currency used for the order.                                                    |
[Payment Fields (`Decision Manager`)]

POS Terminal Exceptions Fields {#ID-00002215}
=============================================

| Field Name                      | Description                                                                                                             | Data Type (Length) |
|:--------------------------------|:------------------------------------------------------------------------------------------------------------------------|:-------------------|
| AccountSuffix                   | ---                                                                                                                     | ---                |
| Amount                          | ---                                                                                                                     | ---                |
| BillToEmail                     | Email address of the user.                                                                                              | String (255)       |
| CardVerificationMethod          | Type of customer verification.                                                                                          | String (60)        |
| ClientID                        | Client identifier for an installation; generated by the operating system.                                               | String (60)        |
| CurrencyCode                    | ---                                                                                                                     | ---                |
| DCCExchangeRate                 | Dynamic Currency Conversion exchange rate.                                                                              | Decimal (22.4)     |
| DCCLookupStatus                 | Lookup Status of Dynamic Currency Conversion.                                                                           | String (255)       |
| DCCMarginRate                   | Margin rate of Dynamic Currency Conversion.                                                                             | Decimal (22.4)     |
| DeviceHardwareRevision          | Hardware revision printed on the back of the credit card reader.                                                        | String (60)        |
| DeviceID                        | Serial number printed on the back of the credit card reader. Dashes are stripped from the serial number.                | String (1024)      |
| DeviceOS                        | Operating system of the device.                                                                                         | String (60)        |
| DeviceOSVersion                 | Operating system version of the device.                                                                                 | String (30)        |
| DeviceTerminalID                | Terminal identifier assigned to the credit card reader; used by the clearing institute to identify credit card readers. | String (255)       |
| ExceptionCategory               | Status of the transaction.                                                                                              | String (255)       |
| ExceptionDescription            | Detailed description of the status of the transaction.                                                                  | String (255)       |
| ExceptionStatusCode             | Code that represents the status of the transaction.                                                                     | String (255)       |
| ExpirationMO                    | ---                                                                                                                     | ---                |
| ExpirationYR                    | ---                                                                                                                     | ---                |
| FirstName                       | ---                                                                                                                     | ---                |
| LastName                        | ---                                                                                                                     | ---                |
| LocalCurrencyCode               | Three-digit security code for the local currency.                                                                       | String (3)         |
| MerchantID                      | ---                                                                                                                     | ---                |
| PartnerMerchantID               | Three-digit identifier for the partner merchant.                                                                        | String (3)         |
| PartnerMerchantName             | Name of the merchant that performed the transaction.                                                                    | String (100)       |
| PartnerOriginalTransaction ID   | Unique identifier of the transaction.                                                                                   | String (60)        |
| ProcessorMID                    | Merchant identifier of the merchant that performed the transaction; as assigned by the clearing institute.              | String (120)       |
| POSTerminalException. RequestID | Unique identifier of the transaction processor; for debugging purposes.                                                 | Integer (26)       |
| SchemeOperator                  | Scheme of the credit card.                                                                                              | String (60)        |
| SDKVersion                      | Version of the software development kit (SDK).                                                                          | String (30)        |
| StorageMechanism                | Source from which payment details have been collected.                                                                  | String (60)        |
| TerminalID                      | Terminal identifier of the merchant that performed the transaction.                                                     | String (60)        |
| TransactionDate                 | ---                                                                                                                     | ---                |
[POS Terminal Exceptions Fields]

Profile Fields {#ID-0000230f}
=============================

| Field Name      | Description                       | Data Type (Length) |
|:----------------|:----------------------------------|:-------------------|
| Name            | Name of the profile.              | VARCHAR2 (30)      |
| ProfileDecision | Decision returned by the profile. | VARCHAR2 (255)     |
| ProfileMode     | Activity mode of the profile.     | VARCHAR2 (1)       |
| RuleDecision    | Decision returned by the rule.    | VARCHAR2 (255)     |
| RuleName        | Name of the rule.                 | VARCHAR2 (30)      |
[Profile Fields]

Proof XML Fields {#ID-00002344}
===============================

| Field Name         | Description                           |
|:-------------------|:--------------------------------------|
| AcquirerBin        | Acquiring bank identification number. |
| Date               | Transaction date.                     |
| DirectoryServerURL | Directory server URL.                 |
| Enrolled           | Enrollment indicator.                 |
| MerchantID         | Merchant ID used for transaction.     |
| Pan                | Customer masked account number.       |
| Password           | Password.                             |
[Proof XML Fields]

Recipient Fields {#ID-00002387}
===============================

| Field Name               | Description                    | Data Type (Length) |
|:-------------------------|:-------------------------------|:-------------------|
| Address                  | Recipient street address.      | ---                |
| City                     | Recipient city.                | ---                |
| Country                  | Recipient country.             | ---                |
| DOB                      | Recipient date of birth.       | ---                |
| FirstName                | Recipient first name.          | ---                |
| LastName                 | Recipient last name.           | ---                |
| MiddleInitial            | Recipient name middle initial. | ---                |
| PhoneNumber              | Recipient phone number.        | ---                |
| PostalCode               | Recipient postal code.         | ---                |
| RecipientBillingAmount   | Transaction billed amount.     | Number (19)        |
| RecipientBillingCurrency | Recipient billing currency.    | CHAR (3)           |
| ReferenceNumber          | Recipient reference number.    | ---                |
| State                    | Recipient state.               | ---                |
[Recipient Fields]

Recurring Billing Fields {#ID-000023f5}
=======================================

| Field Name                     | Description                                                                   | Data Type (Length)          |
|:-------------------------------|:------------------------------------------------------------------------------|:----------------------------|
| BillingPeriodLength            | Length of the billing period.                                                 | VARCHAR2(50 CHAR) NOT NULL  |
| BillingPeriodUnit              | Billing period unit. For example: `day`, `week`, `month`.                     | VARCHAR2(1 CHAR) NOT NULL   |
| PlanPeriodLength               | Length of the plan.                                                           | VARCHAR2(50 CHAR)           |
| PlanPeriodUnit                 | Plan period unit. For example: `day`, `week`, `month`.                        | VARCHAR2(1 CHAR)            |
| PlanDescription                | Description of the plan.                                                      | VARCHAR2(300 CHAR)          |
| PlanCurrency                   | Currency of the plan.                                                         | VARCHAR2(10 CHAR) NOT NULL  |
| PlanID                         | Unique identifier of the plan.                                                | VARCHAR2(100 CHAR)          |
| PlanCode                       | Unique code of the plan.                                                      | VARCHAR2(20 CHAR)           |
| SetupFee                       | Fee for setting up the subscription.                                          | NUMBER                      |
| SubscriptionStatus             | Current status of the subscription. For example, `active` or `inactive`.      | VARCHAR2(20 CHAR) NOT NULL  |
| SubscriptionID                 | Unique identifier of the plan.                                                | NUMBER NOT NULL             |
| SubscriptionCode               | Unique code of the subscription.                                              | VARCHAR2(20 CHAR) NOT       |
| SubscriptionName               | Unique name of the subscription.                                              | VARCHAR2(100 CHAR) NOT NULL |
| SubscriptionNextPaymentDate    | Date of the next payment for this subscription.                               | DATE                        |
| SubscriptionSuccessfulPayments | Number of successful payments for this subscription.                          | NUMBER NOT NULL             |
| SubscriptionRetryCount         | Number of times a failed payment has been retried.                            | NUMBER                      |
| SubscriptionStartDate          | Date the subscription starts.                                                 | DATE NOT NULL               |
| SubscriptionPaymentAmount      | Amount paid for this subscription.                                            | NUMBER NOT NULL             |
| TMSCustomerID                  | Unique customer ID of a `TMS` customer in the `Cybersource` system.           | VARCHAR2(100 CHAR) NOT NULL |
| TMSPaymentInstrumentID         | Unique payment instrument ID of a `TMS` customer in the `Cybersource` system. | VARCHAR2(100 CHAR) NOT NULL |
| TMSShippingID                  | Unique shipping ID of a `TMS` customer in the `Cybersource` system.           | VARCHAR2(100 CHAR)          |
[Recurring Billing Fields]

Request Fields {#ID-0000249b}
=============================

| Field Name                    | Description                                                                     | Data Type (Length) | Simple Order API Value      |
|:------------------------------|:--------------------------------------------------------------------------------|:-------------------|:----------------------------|
| Comments                      | Optional comments that you can make about the subscription or customer profile. | VARCHAR2 255)      | Comments                    |
| eCommerceIndicator            | Transaction type.                                                               | ---                | ---                         |
| LocalizedrequestDate          | ---                                                                             | ---                | \[DERIVED\]                 |
| MerchantID                    | Merchant ID used for the transactions.                                          | VARCHAR2 (30)      | ---                         |
| MerchantReference Number      | Merchant's order reference or tracking number.                                  | Number (38)        | Merchant ReferenceNumber    |
| PartnerOriginal TransactionID | Partner original transaction identifier.                                        | ---                | ---                         |
| PartnerSDKVersion             | Partner SDK version.                                                            | ---                | PartnerSDKVersion           |
| RequestID                     | Identifier for the transaction request.                                         | Number (26)        | RequestID                   |
| Source                        | Source of request.                                                              | ---                | Source                      |
| SubscriptionID                | Identifier for the customer profile.                                            | VARCHAR2 (26)      | SubscriptionID              |
| TerminalSerialNumber          | ---                                                                             | ---                | TerminalSerial Number       |
| TransactionDate               | Date on which the transaction took place.                                       | Date               | RequestDate                 |
| TransactionID                 | ---                                                                             | ---                | TransactionId               |
| TransactionRefNumber          | Transaction identifier.                                                         | ---                | Transaction ReferenceNumber |
| TransactionType               | Transaction type.                                                               | ---                | ---                         |
| User                          | Information about a user.                                                       | VARCHAR2 (30)      | ---                         |
| LocalizedRequestDate          | Localized request date.                                                         | ---                | ---                         |
[Request Fields]

SCA Exemption Fields {#c_SCA_Exemption_Fields}
==============================================

> NOTE
> If you are using the ` HSBC ` processor, you must obtain approval from ` HSBC ` before you use strong customer authentication (SCA) exemptions on authorization transactions for these exemption types:
>
> * Authentication outage
> * Follow-on recurring payment
> * Low-risk transaction
>
> This requirement does not apply to the ` low_value_exemption_indicator ` field

|     Field Name     |                                                                                                                                                                         Description                                                                                                                                                                         |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCAExemption       | Reason the transaction is exempt from strong customer authentication (SCA) requirements. Possible values: * `delegated_authentication_exemption_indicator` * `low_value_exemption_indicator` * `risk_analysis_exemption_indicator` * `secure_corporate_payment_indicator` * `trusted_merchant_exemption_indicator` {#c_SCA_Exemption_Fields_ul_fwg_3dn_hsb} |
| SCAExemptionValues | Number indicating whether the associated SCA Exemption was included in the transaction. Possible values: * `0`: Not exempt. * `1`: Exempt. {#c_SCA_Exemption_Fields_ul_qcm_ldn_hsb}                                                                                                                                                                         |

Sender Fields {#ID-0000278d}
============================

| Field Name             | Description                                                            | Data Type (Length) | Simple Order API Value |
|:-----------------------|:-----------------------------------------------------------------------|:-------------------|:-----------------------|
| Address                | Sender address.                                                        | ---                | SenderAddress          |
| City                   | Sender city.                                                           | ---                | SenderCity             |
| Country                | Sender country.                                                        | ---                | SenderCountry          |
| DOB                    | Sender date of birth.                                                  | ---                | SenderDOB              |
| FirstName              | Sender first name.                                                     | ---                | SenderFirstName        |
| LastName               | Sender last name.                                                      | ---                | SenderLastName         |
| MiddleInitial          | Sender name middle initial.                                            | ---                | SenderMiddleInitial    |
| PhoneNumber            | Sender phone number.                                                   | ---                | SenderPhone Number     |
| PostalCode             | Sender postal code.                                                    | ---                | SenderPostalCode       |
| SenderReference Number | Reference number generated by you that uniquely identifies the sender. | VARCHAR2 (16)      | SenderReference Number |
| SourceOfFunds          | Source of funds.                                                       | ---                | SenderSourceOf Funds   |
| State                  | Sender state.                                                          | ---                | SenderState            |
[Sender Fields]

Settlement Fields {#ID-00002829}
================================

| Field Name             | Description                                                                     | Data Type (Length) |
|:-----------------------|:--------------------------------------------------------------------------------|:-------------------|
| SettlementAge          | Settlement aging.                                                               | Number             |
| SettlementAmount       | Amount settled for transaction.                                                 | Number             |
| SettlementCurrencyCode | Currency code applied to settlement.                                            | VARCHAR2 (3)       |
| SettlementDate         | Date settlement applied.                                                        | Date               |
| SourceResponseCode     | Response code sent from source.                                                 | VARCHAR2 (10)      |
| SourceResponseMessage  | Response message sent from source.                                              | VARCHAR2 (64)      |
| Status                 | Settlement status. Possible values: * `S`: Success * `P`: Pending * `F`: Failed | VARCHAR2 (10)      |
[Settlement Fields]

Shipping Fields {#ID-00002877}
==============================

| Field Name | Description                      | Data Type (Length) |
|:-----------|:---------------------------------|:-------------------|
| Carrier    | Carrier used to ship product.    | VARCHAR2 (12)      |
| Method     | Shipping method for the product. | VARCHAR2 (10)      |
[Shipping Fields]

Ship To Fields {#ID-0000289e}
=============================

| Field Name  | Description                         | Data Type (Length)  | Simple Order API Values |
|:------------|:------------------------------------|:--------------------|:------------------------|
| Address1    | Shipping address first line.        | VARCHAR2 (400 CHAR) | shipTo_Address1         |
| Address2    | Shipping address second line.       | VARCHAR2 (400 CHAR) | shipTo_Address2         |
| City        | Shipping city.                      | VARCHAR2 (50 CHAR)  | shipTo_city             |
| CompanyName | ---                                 | ---                 | shipTo_companyName      |
| Country     | Shipping address country.           | VARCHAR2 (60 CHAR)  | shipTo_country          |
| FirstName   | Recipient first name.               | VARCHAR2 (60 CHAR)  | shipTo_firstName        |
| LastName    | Recipient last name.                | VARCHAR2 (60 CHAR)  | shipTo_lastName         |
| Phone       | Recipient phone number.             | VARCHAR2 (100 CHAR) | shipTo_phoneNumber      |
| State       | Shipping address state or province. | VARCHAR2 (25 CHAR)  | shipTo_state            |
| Zip         | Shipping address Zip/postal code.   | VARCHAR2 (10 CHAR)  | shipTo_postalCode       |
[Ship To Fields]

Standard Billing Data Package Fields {#standard-billing-data-package}
=====================================================================

|            Field Name            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Data Type (Length) | Mandatory/Optional | Default Value |    Padding Value     |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------|---------------|----------------------|
| **Header Record**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ||||||
| File Date                        | The date when the system generated the report. Format: `YYYYMMDD`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Number (8)         | M                  | ---           | ---                  |
| File Time                        | The time of the day when the system generated the report. Format: `HHMMSS`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Number (6)         | M                  | ---           | ---                  |
| Institution ID                   | Unique ID of the partner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Number (8)         | M                  | `0`           | 0 (To the left)      |
| Record Type                      | Record identifier. Fixed value is `HR`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | String (2)         | M                  | `HR`          | ---                  |
| **Detail Records**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ||||||
| Acquirer Merchant ID             | Merchant ID assigned by the acquirer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | String (15)        | O                  | Space         | Space (To the right) |
| Amount Sign                      | Possible values: * `001` Positive * `002` Negative {#standard-billing-data-package_ul_tsd_kn2_4fc}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String (3)         | M                  | Space         | ---                  |
| Card Acceptor ID                 | ID assigned to a merchant by acquirer and used in transactions. Used only for Payment Gateway Services (Card Present and Card Not Present)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | String (15)        | O                  | Space         | Space (To the right) |
| Card Scheme                      | Payment network linked to the payment card. Possible values: * `001` Relay * `002` Mastercard * `003` American Express * `004` Discover * `005` Diners Club * `006` Carte Blanche * `007` JCB * `008` Optima * `011` Twinpay (credit) * `012` Twinpay (debit) * `013` Walmart * `014` Enroute * `015` Lowes Consumer * `016` Home Depot Consumer * `017` MBNA * `018` Dick's Sportwear * `019` Casual Corner * `020` Sears * `021` JAL * `023` Disney * `024` Switch/Solo * `025` Sams Club Consumer * `026` Sams Club Business * `027` Nicos * `029` Bebe * `030` Restoration Hardware * `031` Delta * `032` Solo * `033` Relay Electron * `034` Dankort * `035` Laser * `036` Cartes Bancaires * `037` Carta * `042` Maestro * `043` GE MONEY * `044` Korean cards * `045` Style * `046` J.Crew * `050` Hipercard * `051` Aura * `052` Redecard * `053` Orico card * `054` Elo * `055` Capital One Private Label * `058` Carnet * `059` ValueLink * `061` RuPay * `062` China UnionPay * `063` Falabella Private Label * `064` Prompt card * `065` Korean Domestic * `066` Banricompras | String (3)         | O                  | Space         | ---                  |
| Card Type                        | Type of payment card. Possible values: * `C` Credit card * `D` Debit card * `P` Prepaid card                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | String (2)         | O                  | Space         | Space (To the right) |
| Client Reference                 | Unique identifier assigned to a client in `Cybersource`. The special character underscore (_) is allowed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String (30)        | M                  | `0`           | Space (To the right) |
| Count                            | Sum count of transactions for a given product code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Number (10)        | M                  | Space         | 0 (To the left)      |
| Currency Code                    | ISO numeric currency code used in the transaction                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | String (3)         | M                  | Space         | ---                  |
| Domestic/International Indicator | Indicates whether the transaction was domestic or international. Possible values: * `01` Domestic * `02` International {#standard-billing-data-package_ul_drd_r42_4fc}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | String (2)         | O                  | Space         | ---                  |
| Product Code                     | The product code for the transaction or the partner opted product code associated to the `Cybersource` product code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | String (10)        | M                  | Space         | 0 (To the left)      |
| Record Type                      | Record identifier. Fixed value is `DR`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | String (2)         | M                  | `DR`          | ---                  |
| Statistic Type                   | Not in use.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | String (4)         | O                  | `0`           | 0 (To the left)      |
| Total Amount                     | Sum payment value for a given product code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Number (18)        | M                  | `0`           | 0 (To the left)      |
| Transaction Date                 | Date of the transaction. Format:: `YYYYMMDD`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Number (8)         | M                  | ---           | ---                  |
| **Trailer Record**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ||||||
| Number of Records                | The total number of records in the report including the Header Record, Detail Records, and Trailer Record.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Number (6)         | M                  | Space         | 0 (To the left)      |
| Record Type                      | Record identifier. Fixed Value is `TR`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | String (2)         | M                  | `TR`          | ---                  |
[Standard Billing Data Package Field Names and Descriptions]

Standard Monthly Fee Fields {#monthly-fee-details}
==================================================

|      Field Name      |                                                          Description                                                          | Data Type (Length) | Mandatory/Optional | Default Value |    Padding Value     |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------|---------------|----------------------|
| **Header Record**                                                                                                                                                                                                                ||||||
| File Date            | The date when the system generated the report. Format: `YYYYMMDD`                                                             | Number (8)         | M                  | ---           | ---                  |
| File Time            | The time of the day when the system generated the report. Format: `HHMMSS`                                                    | Number (6)         | M                  | ---           | ---                  |
| Institution ID       | Unique ID of the partner.                                                                                                     | Number (8)         | M                  | `0`           | 0 (To the left)      |
| Record Type          | Record identifier. Fixed value is `HR`.                                                                                       | String (2)         | M                  | `HR`          | ---                  |
| **Detail Records**                                                                                                                                                                                                               ||||||
| Acquirer Merchant ID | Merchant ID assigned by the acquirer.                                                                                         | String (15)        | O                  | Space         | Space (To the right) |
| Actual Fee           | Actual fee value for a given product code. The value is corrected to two decimal places. This value is a multiple of 100.     | Number (18)        | O                  | `0`           | 0 (To the left)      |
| Client Reference     | Unique identifier assigned to a client. The special character underscore (_) is allowed.                                      | String (30)        | M                  | `0`           | Space (To the right) |
| Currency Code        | ISO currency code.                                                                                                            | String (3)         | M                  | Space         | ---                  |
| Fee Type             | Type of fee. Possible values: * `MONTHLY` * `ONETIME` * `MIN`                                                                 | String (30)        | M                  | Space         | Space (To the right) |
| Organization Type    | Type of organization. Possible values: * `RESELLER` * `RESOLD` * `MID` * `RESELLER_MID` {#monthly-fee-details_ol_yg3_d35_rfc} | String (15)        | O                  | Space         | Space (To the right) |
| Product Code         | `Cybersource` product code for the fee.                                                                                       | String (30)        | M                  | Space         | 0 (To the left)      |
| Quantity             | Quantity for the given product code.                                                                                          | Number (18)        | M                  | `0`           | 0 (To the left)      |
| Record Type          | Record identifier. Fixed value is `DR`.                                                                                       | String (2)         | M                  | `DR`          | ---                  |
| Tax                  | Tax value for a given product code. The value is corrected to two decimal places. This value is a multiple of 100.            | Number (18)        | O                  | `0`           | 0 (To the left)      |
| Total Fee            | Total fee value for a given product code. The value is corrected to two decimal places. This value is a multiple of 100.      | Number (18)        | M                  | `0`           | 0 (To the left)      |
| **Trailer Record**                                                                                                                                                                                                               ||||||
| Number of Records    | The total number of records in the report including the Header Record, Detail Records, and Trailer Record.                    | Number (6)         | M                  | Space         | 0 (To the left)      |
| Record Type          | Record identifier. Fixed Value is `TR`.                                                                                       | String (2)         | M                  | `TR`          | ---                  |
[Standard Monthly Fee Field Names and Descriptions]

Tax Fields {#ID-00002925}
=========================

| Field Name                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Data Type (Length) | Simple Order API Values                |
|:--------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:---------------------------------------|
| Country                               | Credit card billing country. Use the two-character ISO Standard Country Codes. When shipTo_country is not provided, billTo_ country is used in its place. When billTo_country is set to US or CA,billTo_postalCode and billTo_state are also required. It is your responsibility to determine whether a field is required for the transaction you are requesting.                                                                                                                                                                       | String (15)        | billTo_country                         |
| CurrencyCode                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | String (5)         | purchaseTotals_currency                |
| LineExemptAmount                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | ---                | ---                                    |
| InvoiceDate                           | Date of the tax calculation. Use format YYYYMMDD. You can provide a date in the past if you are calculating tax for a refund and want to know what the tax was on the date the order was placed. You can provide a date in the future if you are calculating the tax for a future date, such as an upcoming tax holiday. > NOTE The default is the date, in Pacific time, that the request is received. Keep this in mind if you are in a different time zone and want the tax calculated with the rates that apply on a specific date. | String (8)         | invoiceHeader_invoiceDate              |
| JurisdictionCode                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | ---                | ---                                    |
| JurisdictionName                      | Free-text description of the jurisdiction for the item. For example, San Mateo County.Returned only if the show_tax_per_offer field is set to yes.                                                                                                                                                                                                                                                                                                                                                                                      | String (15)        | tax_ offer#_jurisdiction#_name         |
| JurisdictionType                      | Free-text description of the jurisdiction for the item. For example, San Mateo County.Returned only if the show_tax_per_offer field is set to yes.                                                                                                                                                                                                                                                                                                                                                                                      | String (15)        | taxReply_item_#_jurisdiction0..n       |
| LineItemAmount                        | Line Amount total.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String (15)        | ---                                    |
| LineNo                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | String (15)        | ---                                    |
| MerchantIdentifer                     | Merchant ID. Use the same merchant ID for evaluation, testing, and production.                                                                                                                                                                                                                                                                                                                                                                                                                                                          | String (30)        | merchantID                             |
| Merchant ReferenceCode                | Merchant-generated order reference or tracking number. See *Getting Started with `Cybersource` SCMP API* for more information.                                                                                                                                                                                                                                                                                                                                                                                                          | String (50)        | merchantReference Code                 |
| PointOfOrder AcceptanceCity           | This item-level field overrides the corresponding request-level field. This field is not used unless the item_#_ orderAcceptance State and item_#_ orderAcceptance Country fields are present.                                                                                                                                                                                                                                                                                                                                          | String (50)        | item_#_orderAcceptanceCity             |
| PointOfOrder Acceptance Country       | This item-level field overrides the corresponding request-level field. This field is not used unless the item_#_ orderAcceptanceState and item_#_ orderAcceptanceCity fields are present. Use the two-character ISO Standard CountryCodes.                                                                                                                                                                                                                                                                                              | String (2)         | item_#_orderAcceptance Country         |
| PointOfOrder AcceptancePostalCode     | Order acceptance ZIP/Postal Code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | String (10)        | item_#_orderAcceptancePostalCode       |
| PointOfOrder AcceptanceState Province | This item-level field overrides the corresponding request-level field. This field is not used unless the item_#_orderAcceptanceCity and item_#_orderAcceptance Country fields are present. Use the State, Province, and Territory Codes for the United States and Canada.                                                                                                                                                                                                                                                               | String (2)         | item_#_orderAcceptanceState            |
| PointOfOrderOriginCity                | Order origin city. This field is not used unless the taxService_orderOriginState and taxService_orderOriginCountry fields are present.                                                                                                                                                                                                                                                                                                                                                                                                  | String (50)        | taxService_orderOriginCity             |
| PointOfOrderOriginCountry             | This item-level field overrides the corresponding request-level field. This field is not used unless the item_#_ orderAcceptanceState and item_#_orderAcceptanceCity fields are present. Use the two-character ISO Standard Country Codes.                                                                                                                                                                                                                                                                                              | String (2)         | item_#_orderAcceptance Country         |
| PointOfOrderOriginPostalCode          | Order origin postal code. This field is not used unless the taxService_orderOriginCity, taxService_orderOriginState, and taxService_orderOriginCountry fields are present.                                                                                                                                                                                                                                                                                                                                                              | String (10)        | taxService_orderOriginPostalCode       |
| PointOfOrderOriginStateProvince       | Order origin state. This field is not used unless the taxService_orderOriginCity and taxService_orderOriginCountry fields are present. Use the State, Province, and Territory Codes for the United States and Canada.                                                                                                                                                                                                                                                                                                                   | String (2)         | taxService_orderOriginState            |
| ProductCode                           | Type of product. This value is used to determine the product category: electronic, handling, physical, service, or shipping. The default value is default. To use the tax calculation service, use values listed in the Tax Product Code Guide. For information about this document, contact Customer Support.                                                                                                                                                                                                                          | String (20)        | item_#_productCode                     |
| ProductName                           | Name of the product. Some services use this value for communication with the customer, so the name should clearly represent the product. For ccAuthService and ccCaptureService, required if item_#_productCode is not default or one of the values related to shipping and handling.                                                                                                                                                                                                                                                   | String (30)        | item_#_productName                     |
| ProductSku                            | Product's identifier code. For ccAuthService and ccCaptureService, required if item_#_productCode is not default or one of the values related to shipping and handling.                                                                                                                                                                                                                                                                                                                                                                 | String (30)        | item_#_productSKU                      |
| Quantity                              | Quantity of the product being purchased.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | String (20)        | item_#_quantity                        |
| Rate                                  | Jurisdiction tax rate for the item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | String (15)        | taxReply_item_#_jurisdiction_#_rate    |
| ReportingDate                         | Reporting date of any committed transaction. Defaults to current date if not provided. Also the default Tax Calculation Date unless a different date is specified in invoiceHeader_invoiceDate.                                                                                                                                                                                                                                                                                                                                         | String (8)         | taxService_reportingDate               |
| RequestIdentifier                     | Identifier for the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | String (26)        | requestId                              |
| ShipFromCity                          | City from which the order is shipped, which is used to determine tax rules and/or rates applied to the transaction based on sourcing. This field is used only when shipFrom_state and shipFrom_country are present.                                                                                                                                                                                                                                                                                                                     | String (50)        | shipFrom_city                          |
| ShipFromCountry                       | Country from which the product is shipped, which is used to determine tax rules and/or rates applied to the transaction based on sourcing. This item-level field overrides the corresponding request-level field. Use the two character ISO Standard Country Codes.                                                                                                                                                                                                                                                                     | String (2)         | item_#_shipFromCountry                 |
| ShipFromPostal Code                   | Postal code from which the product is shipped, which is used to determine tax rules and/or rates applied to the transaction based on sourcing. This item-level field overrides the corresponding request-level field.                                                                                                                                                                                                                                                                                                                   | String (10)        | item_#_shipFromPostalCode              |
| ShipFromState Province                | State from which the order is shipped, which is used to determine tax rules and/or rates applied to the transaction based on sourcing. This field is used only when shipFrom_city and shipFrom_country are present. Use the State, Province, and Territory Codes for the United States and Canada.                                                                                                                                                                                                                                      | String (2)         | shipFrom_state                         |
| ShipToCity                            | City of the shipping address. This field is used only when the shipTo_state and shipTo_country fields are present.                                                                                                                                                                                                                                                                                                                                                                                                                      | String (50)        | shipTo_city                            |
| ShipToCountry                         | Country of the shipping address. Use the two-character ISO Standard Country Codes. This field is used only when the ship_to_city and ship_to_state fields are present.                                                                                                                                                                                                                                                                                                                                                                  | String (2)         | ship_to_country                        |
| ShipToPostalCode                      | Postal code for the shipping address. The postal code must consist of 5 to 9 digits. When the shipping country is the U.S., the 9-digit postal code must follow this format: \[5 digits\]\[dash\]\[4 digits\] Example: `12345-6789` When the shipping country is Canada, the 6-digit postal code must follow this format: \[alpha\]\[numeric\]\[alpha\] \[space\] \[numeric\]\[alpha\] \[numeric\] Example: `A1B 2C3`                                                                                                                   | String (10)        | shipTo_postalCode                      |
| ShipToState Province                  | State or province of the shipping address. Use the State, Province, and Territory Codes for the United States and Canada. The default value for shipTo_state is billTo_ state. This field is used only when the shipTo_city and shipTo_country fields are present.                                                                                                                                                                                                                                                                      | String (2)         | shipTo_state                           |
| ShipToStreet                          | Street of the shipping address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | ---                | ---                                    |
| StateProvince                         | This item-level field overrides the corresponding request-level field. This field is not used unless the item_#_orderOriginCity and item_#_orderOriginCountry fields are present.                                                                                                                                                                                                                                                                                                                                                       | String (15)        | item_#_orderOriginState                |
| TaxableAmount                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | ---                | ---                                    |
| TaxAmount                             | Total tax for all items.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | String (15)        | taxReply_totalTaxAmount                |
| TaxName                               | Name of the jurisdiction tax for the item. For example, CA State Tax.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | String (15)        | taxReply_item_#_jurisdiction_#_taxName |
| TransactionType                       | Sale/Refund. Based on refund indicator (refund or not).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | ---                | ---                                    |
| UnitPrice                             | Per-item price of the product. This value cannot be negative.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | String (15)        | item_#_unitPrice                       |
[Tax Fields]

Token Fields {#ID-00002b0c}
===========================

Fields in this group prepend the field name with "NetworkToken", "TMSToken", or "Token":

|    Group     |       Field Name       |                  Description                   | Data Type (Length) |
|:------------:|:----------------------:|:----------------------------------------------:|:------------------:|
| NetworkToken |    NetworkTokenPAR     | Network token payment account reference (PAR). |   VARCHAR (100)    |
|   TMSToken   |       CustomerID       |            `TMS` customer token ID.            |    VARCHAR (60)    |
|   TMSToken   |  PaymentInstrumentID   |       `TMS` payment instrument token ID.       |    VARCHAR (60)    |
|   TMSToken   | InstrumentIdentifierID |     `TMS` instrument identifier token ID.      |    VARCHAR (60)    |
|   TMSToken   |   ShippingAddressID    |        `TMS` shipping address token ID.        |    VARCHAR (60)    |
|    Token     | NetworkTokenTransType  |        Network token transaction type.         |        ---         |
|    Token     |       TokenCode        |            Transaction token code.             |   VARCHAR (255)    |
[Token Fields]

Travel Fields {#ID-00002b2c}
============================

| Field Name         | Description                                                         | Data Type (Length) |
|:-------------------|:--------------------------------------------------------------------|:-------------------|
| CompleteRoute      | Concatenation of individual travel legs.                            | VARCHAR2 (255)     |
| DepartureDateTime  | First leg departure date and time.                                  | Date               |
| JourneyType        | Type of travel.                                                     | VARCHAR2 (32)      |
| Number             | Passenger number.                                                   |                    |
| PassengerFirstName | Passenger's first name.                                             | VARCHAR2 (60)      |
| PassengerEmail     | Passenger's email address, including the complete domain name.      | VARCHAR2 (1500)    |
| PassengerId        | Ticketed passenger identifier.                                      | VARCHAR2 (32)      |
| PassengerLastName  | Passenger's last name.                                              | VARCHAR2 (60)      |
| PassengerPhone     | Passenger's phone number.                                           | VARCHAR2 (100)     |
| PassengerStatus    | Company's passenger classification, such as frequent flyer program. | VARCHAR2 (32)      |
| PassengerType      | Passenger classification associated with the price of the ticket.   | VARCHAR2 (32)      |
[Travel Fields (`Decision Manager`)]

Velocity Morphing Fields {#ID-00002b8c}
=======================================

| Field Name | Description                          |
|:-----------|:-------------------------------------|
| Count      | Velocity morphing count information. |
[Velocity Morphing Fields (`Decision Manager`)]

Verify Enrollment Request Fields {#ID-00002ba1}
===============================================

| Field Name  | Description                           |
|:------------|:--------------------------------------|
| AcquirerBin | Acquiring bank identification number. |
| MerchantID  | Merchant identifier.                  |
| Pan         | Customer masked account number.       |
[Verify Enrollment Request Fields]

Verify Enrollment Response Fields {#ID-00002bc8}
================================================

| Field Name | Description                    |
|:-----------|:-------------------------------|
| AccountID  | Account identifier.            |
| AcsUrl     | ACS URL.                       |
| Enrolled   | Indicates enrollment verified. |
[Verify Enrollment Response Fields]

Card-Present Fields {#ID-00002bef}
==================================

The fields in the following table are available in the [Transaction Request](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Reports_Available_in_the_Business_Center/c_Transaction_Request.md "") only for card-present transactions.

| Field Name                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Data Type and Field Length            |
|:--------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------|
| Device.DeviceID                       | Value created by the client software that uniquely identifies the POS device. This value is provided by the client software that is installed on the POS terminal. This value is not sent to the processor but is used for reporting purposes. This field is supported only on American Express Direct and SIX.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | String (32)                           |
| PaymentData.Acquirer MerchantNumber   | Identifier that was assigned to you by your acquirer. This value must be printed on the receipt. This field is supported only on American Express Direct and SIX.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String (15)                           |
| PaymentData.CardPresent               | Indicates whether the card is present at the time of the transaction. Possible values: * `N`: Card is not present. * `Y`: Card is present.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | String (1)                            |
| PaymentData.Card VerificationMethod   | Method that was used to verify the cardholder's identity. Possible values: * `0`: No verification * `1`: Signature * `2`: PIN This field is supported only on American Express Direct, OmniPay Direct, and SIX.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Integer (1)                           |
| PaymentData.EMVRequestFallback        | Indicates that a fallback method was used to enter credit card information into the POS terminal. When a technical problem prevents a successful exchange of information between a chip card and a chip-capable terminal: Swipe the card or key the credit card information into the POS terminal. Use the **pos_entryMode** field to indicate whether the information was swiped or keyed. Possible values: * `true`: Fallback method was used. * `false` (default): Fallback method was not used. This field is supported only on American Express Direct, Chase Paymentech Solutions, GPN, OmniPay Direct, and SIX.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | String (5)                            |
| PaymentData.Issuer ResponseCode       | Additional authorization code that must be printed on the receipt when returned by the processor. This value is generated by the processor and is returned only for a successful transaction. This field is supported only on SIX.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Varchar2 (15)                         |
| PaymentData.PinType                   | Method that was used to verify the cardholder's identity. Possible values: * `0`: No verification * `1`: Signature * `2`: PIN This field is supported only on American Express Direct, OmniPay Direct, and SIX.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Integer (1)                           |
| PaymentData.POSCat Level              | Type of cardholder-activated terminal. Possible values: * `1`: Automated dispensing machine * `2`: Self-service terminal * `3`: Limited amount terminal * `4`: In-flight commerce (IFC) terminal * `5`: Radio frequency device * `6`: Mobile acceptance terminal * `7`: Electronic cash register * `8`: E-commerce device at your location * `9`: Terminal or cash register that uses a dial-up connection to the transaction processing network ***Chase Paymentech Solutions*** Only values `1`, `2`, and `3` are supported. ***FDC Nashville Global*** Only values `7`, `8`, and `9` are supported. ***GPN*** Only values `6`, `7`, `8`, and `9` are supported. ***TSYS Acquiring Solutions*** Only value `6` is supported.                                                                                                                                                                                                                                                                                                                                                         | Nonnegative integer (1)               |
| PaymentData.POSEntry Mode             | Method of entering credit card information into the POS terminal. Possible values: * `contact`: Read from direct contact with chip card. * `contactless`: Read from a contactless interface using chip data. * `keyed`: Manually keyed into POS terminal. This value is not supported on OmniPay Direct or SIX. * `msd`: Read from a contactless interface using magnetic stripe data (MSD). This value is not supported on OmniPay Direct. * `swiped`: Read from credit card magnetic stripe. The `contact`, `contactless`, and `msd` values are supported only for Europay, Mastercard, and Relay (EMV) transactions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | String (11)                           |
| PaymentData.POS Environment           | Operating environment. Possible values: * `0`: No terminal used, or unknown environment. * `1`: On merchant premises, attended. * 2: On merchant premises, unattended, or cardholder terminal. Examples: oil, kiosks, self-checkout, home computer, mobile telephone, personal digital assistant (PDA). Cardholder terminal is supported only for Mastercard transactions. * `3`: Off merchant premises, attended. Examples: portable POS devices at trade shows, at service calls, or in taxis. * `4`: Off merchant premises, unattended, or cardholder terminal. Examples: vending machines, home computer, mobile telephone, PDA. Cardholder terminal is supported only for Mastercard transactions. * `5`: On premises of cardholder, unattended. * `9`: Unknown delivery mode. * `S`: Electronic delivery of product. Examples: music, software, or eTickets that are downloaded over the Internet. * `T`: Physical delivery of product. Examples: music or software that is delivered by mail or by courier. For Mastercard transactions, the only valid values are `2` and `4`. | String (1)                            |
| PaymentData.Routing NetworkType       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | ---                                   |
| PaymentData.StoreAnd ForwardIndicator | When connectivity is unavailable, the client software that is installed on the POS terminal can store a transaction in its memory and send it for authorization when connectivity is restored. This value is provided by the client software that is installed on the POS terminal. This value is not sent to the processor but is used for reporting purposes. Possible values: * `Y` (SCMP) / `true` (SO API) * `N` (SCMP) / `false` (SO API) This field is supported only on American Express Direct and SIX.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | String (1) (SCMP) String (5) (SO API) |
| PaymentData.TerminalID Alternate      | Identifier for an alternate terminal at your retail location. You define the value for this field. This field is supported only for Mastercard transactions on FDC Nashville Global. Use the **pos_terminalID** field to identify the main terminal at your retail location. If your retail location has multiple terminals, use this **pos_terminalIDAlternate** field to identify the terminal used for the transaction. This value is neither verified nor modified before it is passed to the processor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | String (8)                            |
| Request.PartnerOriginal TransactionID | Value that links the previous transaction to the current follow-on request. This value is assigned by the client software that is installed on the POS terminal, which makes it available to the terminal's software and to `Cybersource`. Therefore, you can use this value to reconcile transactions between `Cybersource` and the terminal's software. This value is not sent to the processor but is used for reporting purposes. This field is supported only on American Express Direct and SIX.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | String (32)                           |
| Requst.PartnerSDKVersion              | Version of the software installed on the POS terminal. This value is provided by the client software that is installed on the POS terminal. This value is not sent to the processor but is used for reporting purposes. This field is supported only on American Express Direct and SIX.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String (32)                           |
| Request.TerminalSerial Number         | Terminal serial number assigned by the hardware manufacturer. This value is provided by the client software that is installed on the POS terminal. This value is not sent to the processor but is used for reporting purposes. This field is supported only on American Express Direct and SIX.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | String (32)                           |
[Card-Present Field Descriptions for the Transaction Request Report]

Fields with Compound Values {#ID-00002d17}
==========================================

Some of the new reports contain different field names and headers. In some cases, multiple fields have been combined into a single field with values separated by commas. For example, the `rcode`, `rflag`, and `rmsg` responses for each application have been combined into `ics_rcode`, `ics_rflag`, and `ics_rmsg`. If a transaction called the `ics_auth` and `ics_bill` applications, the `ics_rcode` field could contain 1,1.

|-----------------------------|------------------------------|------------------------|
| **Application Fields**                                                            |||
| Rcode                       | ReasonCode                   | Rflag                  |
| Name                        | Rmsg                         |                        |
| **Health Care Fields**                                                            |||
| amount                      | amountType                   | currency               |
| industryType                |                              |                        |
| **Line Item Fields**                                                              |||
| FulfillmentType             | Quantity                     | UnitPrice              |
| TaxAmount                   | MerchantProductSku           | NameOfProduct          |
| TypeOfProduct               | InvoiceNumber                | Number                 |
| **Payment Method Fields**                                                         |||
| CardType                    | ExpirationMonth              | ExpirationYear         |
| StartMonth                  | StartYear                    | IssueNumber            |
| AccountSuffix               | BoletoNumber                 | BoletoBarCodeNumber    |
| CardCategory                | CardCategoryCode             | WalletType             |
| CheckNumber                 | MandateId                    | MandateType            |
| SignatureDate               | EffectiveDate                | AccountType            |
| TypeDescription             | OverridePaymentMethod        | Type                   |
| **Payment Data Fields**                                                           |||
| AuthorizationType           | AuthorizationCode            | AVSResult              |
| CurrencyCode                | AVSResultMapped              | CVResult               |
| ProcessorResponseCode       | NumberOfInstallments         | ACHVerificationResult  |
| ACHVerificationResultMapped | BalanceAmount                | BalanceCurrencyCode    |
| RequestedAmount             | RequestedAmountCurrency Code | EVEmail                |
| EVEmailRaw                  | EVName                       | EVNameRaw              |
| EVPhoneNumber               | EVPhoneNumberRaw             | EVStreet               |
| EVStreetRaw                 | EVPostalCode                 | EVPostalCodeRaw        |
| BinNumber                   | Amount                       | PaymentRequestID       |
| PaymentProcessor            | TotalTaxAmount               | EventType              |
| GrandTotal                  | ECI                          | AAV_CAVV               |
| XID                         | TargetAmount                 | TargetCurrency         |
| ExchangeRate                | ExchangeRateDate             | DCCIndicator           |
| BankCode                    | BankAccountName              | AuthIndicator          |
| AuthReversalResult          | AuthReversalAmount           | CardPresent            |
| POSEntryMode                | EMVRequestFallback           | TerminalIDAlternate    |
| POSCatLevel                 | CardVerificationMethod       | POSEnvironment         |
| RoutingNetworkType          | StoreAndForwardIndicator     | PinType                |
| IssuerResponseCode          | AcquirerMerchantNumber       | NetworkCode            |
| MandateReferenceNumber      | ProcessorTID                 | ProcessorTransactionID |
| ProcessorMID                | PaymentProductCode           | AcquirerMerchantID     |
| SubMerchantCity             | SubMerchantCountry           | SubMerchantEmail       |
| SubMerchantID               | SubMerchantName              | SubMerchantPhone       |
| SubMerchantPostalCode       | SubMerchantState             | SubMerchantStreet      |
| TransactionRefNumber        | eCommerceIndicator           | CustomerAccountID      |
| BatchFilesID                | SolutionType                 | AuthFactorCode         |
| EMVServiceCode              | AFTIndicator                 | SalesSlipNumber        |
| JpoJccaTerminalID           | JpoPaymentMethod             | ShopName               |
| ShopNameLocal               | ShopNameKatakana             | POSTerminalCapability  |
| MerchantCategoryCode        |                              |                        |
[Fields with Compound Values]

Frequently Asked Questions {#ID-00002e64}
=========================================

This section includes responses to common questions and scenarios you might encounter while using reports in the `Business Center`.  
***Can I order my fields in an XML downloadable report?***  
The XML industry standards do not require field order to be specified. All industry standard XML parsers are compatible with unordered elements. For more information, see <https://www.w3schools.com/xml/el_all.asp>.  
***How soon will my generated report be ready?***  
Daily, recurring reports are available for download within 6 hours of the report start time. Weekly, monthly, and one-time reports might take longer than 6 hours. Reports for partners also may require longer than 6 hours to generate.  
***Is there a limit to the size of a generated report?***  
The report can be any size, but it might take more time to download depending on the file size and the user's network speed.  
***Where can I find report field descriptions***?  
See [Report Fields and Descriptions](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Report_Fields_and_Descriptions.md "").  
***Which report fields can I add to a report?***  
For a list of available fields in each report, see [Fields and Descriptions for Downloadable Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Report_Fields_and_Descriptions/Fields_Descriptions_Downloadable_Reports.md "").  
***How can I identify declined authorizations in my reports?***  
In the Transaction Request Report, authorizations are recorded in the **ApplicationName** field as `ics_auth`. If the authorization was declined, the value in the **RCode** field will be `0`. You can find additional information related to the decline in the **RFlag** and the **RMsg** fields.  
***How do I interpret an authorization reply flag (rFlag)?***  
For more information, see [Reply Flags \& Messages on the Customer Support site.](https://www.cybersource.com/developers/other_resources/quick_references/reply_flags/ "")  
***What is the reporting cycle of the Invoice Summary Report?***  
The Invoice Summary report contains transactions that happen between 12:00 a.m. on the first day of the month and 11:59:59 p.m. Pacific Time on the last day of the month.  
***Why can't I change the time and time zone of the Invoice Summary Report?***  
The Invoice Summary report is designed to run on the same cycle as your monthly billing. This report is expected to contain the transactions that are billed for the month.  
***How can I get a one-time Invoice Summary report to cover the same period of time as my monthly invoice?***  
To create a one-time Invoice Summary report that reflects your monthly invoice, select the start date as the first day of the month; the end date as the last day of the month; and time zone as GMT.  
***Can I reconcile the Payment Batch Detail Report with the same report in the old `Business Center`?***  
If you would like to configure your new Payment Batch Detail report to contain the same transactions that appear in the same report in the old `Business Center`, schedule the report to begin at 12:00 AM PST. In this case, the two reports will contain the same transactions.  
***Is the Acquirer Reference Number (ARN) is reflected in any acquiring reports?***  
It is exposed as Transaction Reference Number in the `Business Center` reports. The GPN returns the ARN, which is a combination of the `Cybersource` `trans_ref_no` field with some specific information from Global Payments.

Financial and Reconciliation Reports {#ID-00002e9f}
===================================================

The `Business Center` enables merchants processing credit card or alternate payments to generate reports containing financial / reconciliation data. For alternate payment merchants, reporting supports both direct merchants and those using financial service providers. For more information about payment processing for alternate payments, see the [Alternate Payment Services support documentation](https://www.cybersource.com/developers/documentation/alternative_payment_services/ "").
NOTE Based on the acquirer and processor you use, one or more of the reports in this section may be available. Contact your representative for more information about which reports are applicable to your organization.  
For instructions on creating report subscriptions and generating downloadable reports, see [Creating and Accessing Downloadable Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports.md "").

| Report Name                      | Description                                                                                                                                                                                                                                      |
|:---------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aging Details                    | Displays transactions which have been settled but not funded, by age.                                                                                                                                                                            |
| Chargeback and Retrieval Details | Reflects all chargeback activity. Each chargeback is displayed, and the report indicates if there was any financial impact.                                                                                                                      |
| Deposit Details                  | Displays what deposits and debits were made to the financial institution account. Each ACH item is displayed with an ACH description (Settlement, Chargeback, Fees, etc.), and whether the money was deposited or debited from the bank account. |
| Fee Details                      | Displays the interchange, Discount, and Assessment fees for each transaction. Alternate payment merchants see Service Fees.                                                                                                                      |
| Funding Details                  | Lists all settled transactions from the daily batch.                                                                                                                                                                                             |
| Processor Settlement Details     | All settlement responses sent by your acquirer, by transaction and status.                                                                                                                                                                       |
| Net Funding                      |                                                                                                                                                                                                                                                  |
[Financial / Reconciliation Reports]

Fields Available in Financial Reports {#ID-00002ee3}
====================================================

The following sections contain details for the fields that are available in each report. For more information about specific fields (including description, field type, and field length); see [Report Fields and Descriptions](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Report_Fields_and_Descriptions.md "").

Aging Details Report {#ID-00002ee6}
===================================

|--------------------------|------------------------------|------------------------------|
| **Application Fields**                                                               |||
| Name                     | Rcode                        | Rflag                        |
| Rmsg                     |                              |                              |
| **BankInfo Fields**                                                                  |||
| Address                  | BranchCode                   | City                         |
| Country                  | Name                         | SwiftCode                    |
| **BillTo Fields**                                                                    |||
| Address1                 | Address2                     | City                         |
| CompanyName              | CompanyTaxID                 | Country                      |
| CustomerID               | Email                        | FirstName                    |
| HostName                 | IPAddress                    | LastName                     |
| MiddleName               | NameSuffix                   | PersonalID                   |
| Phone                    | State                        | Title                        |
| UserName                 | Zip                          |                              |
| **Check Fields**                                                                     |||
| AccountEncoderID         | SecCode                      |                              |
| **Device Fields**                                                                    |||
| DeviceID                 |                              |                              |
| **FundTransfer Fields**                                                              |||
| BankCheckDigit           | IbanIndicator                |                              |
| **LineItems Fields**                                                                 |||
| FulfillmentType          | InvoiceNumber                | MerchantProductSku           |
| Number                   | ProductCode                  | ProductName                  |
| Quantity                 | TaxAmount                    | UnitPrice                    |
| **MerchantDefinedData Fields**                                                       |||
| Field1 - Field20         |                              |                              |
| **PaymentData Fields**                                                               |||
| AAV_CAVV                 | ACHVerificationResult        | ACHVerificationResult Mapped |
| AVSResult                | AVSResultMapped              | Amount                       |
| AuthIndicator            | AuthReversalAmount           | AuthReversalResult           |
| AuthorizationCode        | AuthorizationType            | BalanceAmount                |
| BalanceCurrencyCode      | BinNumber                    | CVResult                     |
| CardCategory             | CardCategoryCode             | CurrencyCode                 |
| DCCIndicator             | ECI                          | EVEmail                      |
| EVEmailRaw               | EVName                       | EVNameRaw                    |
| EVPhoneNumber            | EVPhoneNumberRaw             | EVPostalCode                 |
| EVPostalCodeRaw          | EVStreet                     | EVStreetRaw                  |
| EventType                | ExchangeRate                 | ExchangeRateDate             |
| GrandTotal               | NetworkTransactionID         | NumberOfInstallments         |
| PaymentProcessor         | PaymentProductCode           | PaymentRequestID             |
| ProcessorResponseCode    | ProcessorResponseID          | ProcessorTID                 |
| RequestedAmount          | RequestedAmountCurrency Code | TargetAmount                 |
| TargetCurrency           | TotalTaxAmount               | TransactionRefNumber         |
| XID                      |                              |                              |
| **PaymentMethod Fields**                                                             |||
| AccountSuffix            | BankAccountName              | BankCode                     |
| BoletoBarCodeNumber      | BoletoNumber                 | CardType                     |
| CheckNumber              | ExpirationMonth              | ExpirationYear               |
| IssueNumber              | MandateId                    | MandateType                  |
| SignatureDate            | StartMonth                   | StartYear                    |
| WalletType               |                              |                              |
| **Profile Fields**                                                                   |||
| Name                     | ProfileDecision              | ProfileMode                  |
| RuleDecision             | RuleName                     |                              |
| **Recipient Fields**                                                                 |||
| RecipientBillingAmount   | RecipientBillingCurrency     |                              |
| **Request Fields**                                                                   |||
| Comments                 | MerchantID (\*)              | MerchantReferenceNumber      |
| RequestID (\*)           | Source                       | SubscriptionID               |
| TransactionDate (\*)     | User                         |                              |
| **Risk Fields**                                                                      |||
| AppliedAVS               | AppliedCV                    | AppliedCategoryGift          |
| AppliedCategoryTime      | AppliedHostHedge             | AppliedThreshold             |
| AppliedTimeHedge         | AppliedVelocityHedge         | BinAccountType               |
| BinCountry               | BinIssuer                    | BinScheme                    |
| CodeType                 | CodeValue                    | ConsumerLoyalty              |
| ConsumerPasswordProvided | ConsumerPromotions           | CookiesAccepted              |
| CookiesEnabled           | DeviceFingerPrint            | Factors                      |
| FlashEnabled             | GiftWrap                     | HostSeverity                 |
| IPCity                   | IPCountry                    | IPRoutingMethod              |
| IPState                  | ImagesEnabled                | JavascriptEnabled            |
| LostPassword             | ProductRisk                  | ProxyIPAddress               |
| ProxyIPAddressActivities | ProxyIPAddressAttributes     | ProxyServerType              |
| RepeatCustomer           | ReturnsAccepted              | Score                        |
| TimeLocal                | TrueIPAddress                | TrueIPAddressAttributes      |
| TrueIPAddressCity        | TrueIPAddressCountry         | TrueIPaddressActivities      |
| **Settlement Fields**                                                                |||
| SettlementAge (\*)       | SettlementAmount (\*)        | SettlementCurrencyCode (\*)  |
| SettlementDate (\*)      | SourceResponseCode           | SourceResponseMessage        |
| Status                   |                              |                              |
| Sender Fields                                                                        |||
| SenderReferenceNumber    |                              |                              |
| **ShipTo Fields**                                                                    |||
| Address1                 | Address2                     | City                         |
| Country                  | FirstName                    | LastName                     |
| Phone                    | State                        | Zip                          |
| **Shipping Fields**                                                                  |||
| Carrier                  | Method                       |                              |
| **Token Fields**                                                                     |||
| TokenCode                |                              |                              |
| **Travel Fields**                                                                    |||
| CompleteRoute            | DepartureDateTime            | JourneyType                  |
| Number                   | PassengerEmail               | PassengerFirstName           |
| PassengerId              | PassengerLastName            | PassengerPhone               |
| PassengerStatus          | PassengerType                |                              |
[Fields Available in the Aging Details Report]

Chargeback and Retrieval Details Report {#ID-0000314e}
======================================================

|--------------------------|------------------------------|---------------------------------|
| **Application Fields**                                                                  |||
| Name                     | Rcode                        | Rflag                           |
| Rmsg                     |                              |                                 |
| **BankInfo Fields**                                                                     |||
| Address                  | BranchCode                   | City                            |
| Country                  | Name                         | SwiftCode                       |
| **BillTo Fields**                                                                       |||
| Address1                 | Address2                     | City                            |
| CompanyName              | CompanyTaxID                 | Country                         |
| CustomerID               | Email                        | FirstName                       |
| HostName                 | IPAddress                    | LastName                        |
| MiddleName               | NameSuffix                   | PersonalID                      |
| Phone                    | State                        | Title                           |
| UserName                 | Zip                          |                                 |
| **ChargebackAndRetrieval Fields**                                                       |||
| ARN                      | AdjustmentAmount             | AdjustmentCurrency              |
| CaseIdentifier           | CaseNumber (\*)              | CaseTime (\*)                   |
| CaseType (\*)            | ChargebackAmount (\*)        | ChargebackCurrency (\*)         |
| ChargebackMessage        | ChargebackReasonCode         | ChargebackReasonCodeDescription |
| ChargebackTime (\*)      | DocumentIndicator            | FeeAmount                       |
| FeeCurrency              | FinancialImpact (\*)         | FinancialImpactType             |
| MerchantCategoryCode     | PartialIndicator             | ResolutionTime                  |
| ResolvedToIndicator      | RespondByDate                | TransactionType (\*)            |
| **Check Fields**                                                                        |||
| AccountEncoderID         | SecCode                      |                                 |
| **Device Fields**                                                                       |||
| DeviceID                 |                              |                                 |
| **FundTransfer Fields**                                                                 |||
| BankCheckDigit           | IbanIndicator                |                                 |
| **LineItems Fields**                                                                    |||
| FulfillmentType          | InvoiceNumber                | MerchantProductSku              |
| Number                   | ProductCode                  | ProductName                     |
| Quantity                 | TaxAmount                    | UnitPrice                       |
| **MerchantDefinedData Fields**                                                          |||
| Field1 - Field20         |                              |                                 |
| **PaymentData Fields**                                                                  |||
| AAV_CAVV                 | ACHVerificationResult        | ACHVerificationResult Mapped    |
| AVSResult                | AVSResultMapped              | Amount                          |
| AuthIndicator            | AuthReversalAmount           | AuthReversalResult              |
| AuthorizationCode        | AuthorizationType            | BalanceAmount                   |
| BalanceCurrencyCode      | BinNumber                    | CVResult                        |
| CardCategory             | CardCategoryCode             | CurrencyCode                    |
| DCCIndicator             | ECI                          | EVEmail                         |
| EVEmailRaw               | EVName                       | EVNameRaw                       |
| EVPhoneNumber            | EVPhoneNumberRaw             | EVPostalCode                    |
| EVPostalCodeRaw          | EVStreet                     | EVStreetRaw                     |
| EventType                | ExchangeRate                 | ExchangeRateDate                |
| GrandTotal               | NetworkTransactionID         | NumberOfInstallments            |
| PaymentProcessor         | PaymentProductCode           | PaymentRequestID                |
| ProcessorResponseCode    | ProcessorResponseID          | ProcessorTID                    |
| RequestedAmount          | RequestedAmountCurrency Code | TargetAmount                    |
| TargetCurrency           | TotalTaxAmount               | TransactionRefNumber            |
| XID                      |                              |                                 |
| **PaymentMethod Fields**                                                                |||
| AccountSuffix            | BankAccountName              | BankCode                        |
| BoletoBarCodeNumber      | BoletoNumber                 | CardType                        |
| CheckNumber              | ExpirationMonth              | ExpirationYear                  |
| IssueNumber              | MandateId                    | MandateType                     |
| SignatureDate            | StartMonth                   | StartYear                       |
| WalletType               |                              |                                 |
| **Profile Fields**                                                                      |||
| Name                     | ProfileDecision              | ProfileMode                     |
| RuleDecision             | RuleName                     |                                 |
| **Recipient Fields**                                                                    |||
| RecipientBillingAmount   | RecipientBillingCurrency     |                                 |
| **Request Fields**                                                                      |||
| Comments                 | MerchantID (\*)              | MerchantReferenceNumber         |
| RequestID (\*)           | Source                       | SubscriptionID                  |
| TransactionDate (\*)     | User                         |                                 |
| **Risk Fields**                                                                         |||
| AppliedAVS               | AppliedCV                    | AppliedCategoryGift             |
| AppliedCategoryTime      | AppliedHostHedge             | AppliedThreshold                |
| AppliedTimeHedge         | AppliedVelocityHedge         | BinAccountType                  |
| BinCountry               | BinIssuer                    | BinScheme                       |
| CodeType                 | CodeValue                    | ConsumerLoyalty                 |
| ConsumerPasswordProvided | ConsumerPromotions           | CookiesAccepted                 |
| CookiesEnabled           | DeviceFingerPrint            | Factors                         |
| FlashEnabled             | GiftWrap                     | HostSeverity                    |
| IPCity                   | IPCountry                    | IPRoutingMethod                 |
| IPState                  | ImagesEnabled                | JavascriptEnabled               |
| LostPassword             | ProductRisk                  | ProxyIPAddress                  |
| ProxyIPAddressActivities | ProxyIPAddressAttributes     | ProxyServerType                 |
| RepeatCustomer           | ReturnsAccepted              | Score                           |
| TimeLocal                | TrueIPAddress                | TrueIPAddressAttributes         |
| TrueIPAddressCity        | TrueIPAddressCountry         | TrueIPaddressActivities         |
| Sender Fields                                                                           |||
| SenderReferenceNumber    |                              |                                 |
| **ShipTo Fields**                                                                       |||
| Address1                 | Address2                     | City                            |
| Country                  | FirstName                    | LastName                        |
| Phone                    | State                        | Zip                             |
| **Shipping Fields**                                                                     |||
| Carrier                  | Method                       |                                 |
| **Token Fields**                                                                        |||
| TokenCode                |                              |                                 |
| **Travel Fields**                                                                       |||
| CompleteRoute            | DepartureDateTime            | JourneyType                     |
| Number                   | PassengerEmail               | PassengerFirstName              |
| PassengerId              | PassengerLastName            | PassengerPhone                  |
| PassengerStatus          | PassengerType                |                                 |
[Fields Available in the Chargeback and Retrieval Details Report]

Deposit Details Report {#ID-000033d9}
=====================================

|-----------------------|-------------------------|------------------|
| **Deposit Fields**                                               |||
| Amount (\*)           | Category (\*)           | Currency (\*)    |
| ExchangeRate          | ExchangeRateDescription | Identifier (\*)  |
| MerchantBankAcctLast4 | MerchantBankAcctName    | MerchantBankCode |
| MerchantBankCountry   | MerchantBankName        | MerchantID (\*)  |
| Method (\*)           | Status (\*)             | Time (\*)        |
| TransferMessage       | Type (\*)               |                  |
[Fields Available in the Deposit Details Report]

Fee Details Report {#ID-00003412}
=================================

|--------------------------|------------------------------|------------------------------|
| **Application Fields**                                                               |||
| Name                     | Rcode                        | Rflag                        |
| Rmsg                     |                              |                              |
| **BankInfo Fields**                                                                  |||
| Address                  | BranchCode                   | City                         |
| Country                  | Name                         | SwiftCode                    |
| **BillTo Fields**                                                                    |||
| Address1                 | Address2                     | City                         |
| CompanyName              | CompanyTaxID                 | Country                      |
| CustomerID               | Email                        | FirstName                    |
| HostName                 | IPAddress                    | LastName                     |
| MiddleName               | NameSuffix                   | PersonalID                   |
| Phone                    | State                        | Title                        |
| UserName                 | Zip                          |                              |
| **Check Fields**                                                                     |||
| AccountEncoderID         | SecCode                      |                              |
| **Device Fields**                                                                    |||
| DeviceID                 |                              |                              |
| **Fee Fields**                                                                       |||
| AssessmentAmount (\*)    | AssessmentCurrency (\*)      | BillingCycle                 |
| BillingType (\*)         | ClearedInterchangeLevel      | DiscountAmount (\*)          |
| DiscountCurrency (\*)    | DiscountRate                 | DowngradeReasonCode          |
| InterchangeAmount (\*)   | InterchangeCurrency (\*)     | InterchangeRate              |
| PerItemFeeAmount         | PerItemFeeCurrency           | PricedInterchangeLevel       |
| ServiceFeeAmount         | ServiceFeeAmountCcy          | ServiceFeeFixedAmount        |
| ServiceFeeFixedAmountCcy | ServiceFeeRate               | SettlementAmount (\*)        |
| SettlementCurrency (\*)  | SettlementTime (\*)          | SettlementTimeZone (\*)      |
| SourceDescriptor         | TotalFeeAmount (\*)          | TotalFeeCurrency (\*)        |
| **FundTransfer Fields**                                                              |||
| BankCheckDigit           | IbanIndicator                |                              |
| **LineItems Fields**                                                                 |||
| FulfillmentType          | InvoiceNumber                | MerchantProductSku           |
| Number                   | ProductCode                  | ProductName                  |
| Quantity                 | TaxAmount                    | UnitPrice                    |
| **MerchantDefinedData Fields**                                                       |||
| Field1 - Field20         |                              |                              |
| **PaymentData Fields**                                                               |||
| AAV_CAVV                 | ACHVerificationResult        | ACHVerificationResult Mapped |
| AVSResult                | AVSResultMapped              | Amount                       |
| AuthIndicator            | AuthReversalAmount           | AuthReversalResult           |
| AuthorizationCode        | AuthorizationType            | BalanceAmount                |
| BalanceCurrencyCode      | BinNumber                    | CVResult                     |
| CardCategory             | CardCategoryCode             | CurrencyCode                 |
| DCCIndicator             | ECI                          | EVEmail                      |
| EVEmailRaw               | EVName                       | EVNameRaw                    |
| EVPhoneNumber            | EVPhoneNumberRaw             | EVPostalCode                 |
| EVPostalCodeRaw          | EVStreet                     | EVStreetRaw                  |
| EventType                | ExchangeRate                 | ExchangeRateDate             |
| GrandTotal               | NetworkTransactionID         | NumberOfInstallments         |
| PaymentProcessor         | PaymentProductCode           | PaymentRequestID             |
| ProcessorResponseCode    | ProcessorResponseID          | ProcessorTID                 |
| RequestedAmount          | RequestedAmountCurrency Code | TargetAmount                 |
| TargetCurrency           | TotalTaxAmount               | TransactionRefNumber         |
| XID                      |                              |                              |
| **PaymentMethod Fields**                                                             |||
| AccountSuffix            | BankAccountName              | BankCode                     |
| BoletoBarCodeNumber      | BoletoNumber                 | CardType                     |
| CheckNumber              | ExpirationMonth              | ExpirationYear               |
| IssueNumber              | MandateId                    | MandateType                  |
| SignatureDate            | StartMonth                   | StartYear                    |
| WalletType               |                              |                              |
| **Profile Fields**                                                                   |||
| Name                     | ProfileDecision              | ProfileMode                  |
| RuleDecision             | RuleName                     |                              |
| **Recipient Fields**                                                                 |||
| RecipientBillingAmount   | RecipientBillingCurrency     |                              |
| **Request Fields**                                                                   |||
| Comments                 | MerchantID (\*)              | MerchantReferenceNumber      |
| RequestID (\*)           | Source                       | SubscriptionID               |
| TransactionDate (\*)     | User                         |                              |
| **Risk Fields**                                                                      |||
| AppliedAVS               | AppliedCV                    | AppliedCategoryGift          |
| AppliedCategoryTime      | AppliedHostHedge             | AppliedThreshold             |
| AppliedTimeHedge         | AppliedVelocityHedge         | BinAccountType               |
| BinCountry               | BinIssuer                    | BinScheme                    |
| CodeType                 | CodeValue                    | ConsumerLoyalty              |
| ConsumerPasswordProvided | ConsumerPromotions           | CookiesAccepted              |
| CookiesEnabled           | DeviceFingerPrint            | Factors                      |
| FlashEnabled             | GiftWrap                     | HostSeverity                 |
| IPCity                   | IPCountry                    | IPRoutingMethod              |
| IPState                  | ImagesEnabled                | JavascriptEnabled            |
| LostPassword             | ProductRisk                  | ProxyIPAddress               |
| ProxyIPAddressActivities | ProxyIPAddressAttributes     | ProxyServerType              |
| RepeatCustomer           | ReturnsAccepted              | Score                        |
| TimeLocal                | TrueIPAddress                | TrueIPAddressAttributes      |
| TrueIPAddressCity        | TrueIPAddressCountry         | TrueIPaddressActivities      |
| Sender Fields                                                                        |||
| SenderReferenceNumber    |                              |                              |
| **ShipTo Fields**                                                                    |||
| Address1                 | Address2                     | City                         |
| Country                  | FirstName                    | LastName                     |
| Phone                    | State                        | Zip                          |
| **Shipping Fields**                                                                  |||
| Carrier                  | Method                       |                              |
| **Token Fields**                                                                     |||
| TokenCode                |                              |                              |
| **Travel Fields**                                                                    |||
| CompleteRoute            | DepartureDateTime            | JourneyType                  |
| Number                   | PassengerEmail               | PassengerFirstName           |
| PassengerId              | PassengerLastName            | PassengerPhone               |
| PassengerStatus          | PassengerType                |                              |
[Fields Available in the Fee Details Report]

Funding Details Report {#ID-000036a3}
=====================================

|------------------------------|------------------------------|------------------------------|
| **Application Fields**                                                                   |||
| Name                         | Rcode                        | Rflag                        |
| Rmsg                         |                              |                              |
| **BankInfo Fields**                                                                      |||
| Address                      | BranchCode                   | City                         |
| Country                      | Name                         | SwiftCode                    |
| **BillTo Fields**                                                                        |||
| Address1                     | Address2                     | City                         |
| CompanyName                  | CompanyTaxID                 | Country                      |
| CustomerID                   | Email                        | FirstName                    |
| HostName                     | IPAddress                    | LastName                     |
| MiddleName                   | NameSuffix                   | PersonalID                   |
| Phone                        | State                        | Title                        |
| UserName                     | Zip                          |                              |
| **Check Fields**                                                                         |||
| AccountEncoderID             | SecCode                      |                              |
| **Device Fields**                                                                        |||
| DeviceID                     |                              |                              |
| **Funding Fields**                                                                       |||
| CurrencyExchange Description | CurrencyExchangeRate         | FeeAmount                    |
| FeeCurrency                  | FeeDescription               | FundingAmount (\*)           |
| FundingCurrency (\*)         | FundingDate (\*)             | FundingProcessorMessage      |
| ProcessorResponseCode        | Status                       |                              |
| **FundTransfer Fields**                                                                  |||
| BankCheckDigit               | IbanIndicator                |                              |
| **LineItems Fields**                                                                     |||
| FulfillmentType              | InvoiceNumber                | MerchantProductSku           |
| Number                       | ProductCode                  | ProductName                  |
| Quantity                     | TaxAmount                    | UnitPrice                    |
| **MerchantDefinedData Fields**                                                           |||
| Field1 - Field20             |                              |                              |
| **PaymentData Fields**                                                                   |||
| AAV_CAVV                     | ACHVerificationResult        | ACHVerificationResult Mapped |
| AVSResult                    | AVSResultMapped              | Amount                       |
| AuthIndicator                | AuthReversalAmount           | AuthReversalResult           |
| AuthorizationCode            | AuthorizationType            | BalanceAmount                |
| BalanceCurrencyCode          | BinNumber                    | CVResult                     |
| CardCategory                 | CardCategoryCode             | CurrencyCode                 |
| DCCIndicator                 | ECI                          | EVEmail                      |
| EVEmailRaw                   | EVName                       | EVNameRaw                    |
| EVPhoneNumber                | EVPhoneNumberRaw             | EVPostalCode                 |
| EVPostalCodeRaw              | EVStreet                     | EVStreetRaw                  |
| EventType                    | ExchangeRate                 | ExchangeRateDate             |
| GrandTotal                   | NetworkTransactionID         | NumberOfInstallments         |
| PaymentProcessor             | PaymentProductCode           | PaymentRequestID             |
| ProcessorResponseCode        | ProcessorResponseID          | ProcessorTID                 |
| RequestedAmount              | RequestedAmountCurrency Code | TargetAmount                 |
| TargetCurrency               | TotalTaxAmount               | TransactionRefNumber         |
| XID                          |                              |                              |
| **PaymentMethod Fields**                                                                 |||
| AccountSuffix                | BankAccountName              | BankCode                     |
| BoletoBarCodeNumber          | BoletoNumber                 | CardType                     |
| CheckNumber                  | ExpirationMonth              | ExpirationYear               |
| IssueNumber                  | MandateId                    | MandateType                  |
| SignatureDate                | StartMonth                   | StartYear                    |
| WalletType                   |                              |                              |
| **Profile Fields**                                                                       |||
| Name                         | ProfileDecision              | ProfileMode                  |
| RuleDecision                 | RuleName                     |                              |
| **Recipient Fields**                                                                     |||
| RecipientBillingAmount       | RecipientBillingCurrency     |                              |
| **Request Fields**                                                                       |||
| Comments                     | MerchantID (\*)              | MerchantReferenceNumber      |
| RequestID (\*)               | Source                       | SubscriptionID               |
| TransactionDate (\*)         | User                         |                              |
| **Risk Fields**                                                                          |||
| AppliedAVS                   | AppliedCV                    | AppliedCategoryGift          |
| AppliedCategoryTime          | AppliedHostHedge             | AppliedThreshold             |
| AppliedTimeHedge             | AppliedVelocityHedge         | BinAccountType               |
| BinCountry                   | BinIssuer                    | BinScheme                    |
| CodeType                     | CodeValue                    | ConsumerLoyalty              |
| ConsumerPasswordProvided     | ConsumerPromotions           | CookiesAccepted              |
| CookiesEnabled               | DeviceFingerPrint            | Factors                      |
| FlashEnabled                 | GiftWrap                     | HostSeverity                 |
| IPCity                       | IPCountry                    | IPRoutingMethod              |
| IPState                      | ImagesEnabled                | JavascriptEnabled            |
| LostPassword                 | ProductRisk                  | ProxyIPAddress               |
| ProxyIPAddressActivities     | ProxyIPAddressAttributes     | ProxyServerType              |
| RepeatCustomer               | ReturnsAccepted              | Score                        |
| TimeLocal                    | TrueIPAddress                | TrueIPAddressAttributes      |
| TrueIPAddressCity            | TrueIPAddressCountry         | TrueIPaddressActivities      |
| Sender Fields                                                                            |||
| SenderReferenceNumber        |                              |                              |
| **ShipTo Fields**                                                                        |||
| Address1                     | Address2                     | City                         |
| Country                      | FirstName                    | LastName                     |
| Phone                        | State                        | Zip                          |
| **Shipping Fields**                                                                      |||
| Carrier                      | Method                       |                              |
| **Token Fields**                                                                         |||
| TokenCode                    |                              |                              |
| **Travel Fields**                                                                        |||
| CompleteRoute                | DepartureDateTime            | JourneyType                  |
| Number                       | PassengerEmail               | PassengerFirstName           |
| PassengerId                  | PassengerLastName            | PassengerPhone               |
| PassengerStatus              | PassengerType                |                              |
[Fields Available in the Funding Details Report]

Settlement Details Report {#ID-00003911}
========================================

|--------------------------|------------------------------|------------------------------|
| **Application Fields**                                                               |||
| Name                     | Rcode                        | Rflag                        |
| Rmsg                     |                              |                              |
| **BankInfo Fields**                                                                  |||
| Address                  | BranchCode                   | City                         |
| Country                  | Name                         | SwiftCode                    |
| **BillTo Fields**                                                                    |||
| Address1                 | Address2                     | City                         |
| CompanyName              | CompanyTaxID                 | Country                      |
| CustomerID               | Email                        | FirstName                    |
| HostName                 | IPAddress                    | LastName                     |
| MiddleName               | NameSuffix                   | PersonalID                   |
| Phone                    | State                        | Title                        |
| UserName                 | Zip                          |                              |
| **Check Fields**                                                                     |||
| AccountEncoderID         | SecCode                      |                              |
| **Device Fields**                                                                    |||
| DeviceID                 |                              |                              |
| **FundTransfer Fields**                                                              |||
| BankCheckDigit           | IbanIndicator                |                              |
| **LineItems Fields**                                                                 |||
| FulfillmentType          | InvoiceNumber                | MerchantProductSku           |
| Number                   | ProductCode                  | ProductName                  |
| Quantity                 | TaxAmount                    | UnitPrice                    |
| **MerchantDefinedData Fields**                                                       |||
| Field1 - Field20         |                              |                              |
| **PaymentData Fields**                                                               |||
| AAV_CAVV                 | ACHVerificationResult        | ACHVerificationResult Mapped |
| AVSResult                | AVSResultMapped              | Amount                       |
| AuthIndicator            | AuthReversalAmount           | AuthReversalResult           |
| AuthorizationCode        | AuthorizationType            | BalanceAmount                |
| BalanceCurrencyCode      | BinNumber                    | CVResult                     |
| CardCategory             | CardCategoryCode             | CurrencyCode                 |
| DCCIndicator             | ECI                          | EVEmail                      |
| EVEmailRaw               | EVName                       | EVNameRaw                    |
| EVPhoneNumber            | EVPhoneNumberRaw             | EVPostalCode                 |
| EVPostalCodeRaw          | EVStreet                     | EVStreetRaw                  |
| EventType                | ExchangeRate                 | ExchangeRateDate             |
| GrandTotal               | NetworkTransactionID         | NumberOfInstallments         |
| PaymentProcessor         | PaymentProductCode           | PaymentRequestID             |
| ProcessorResponseCode    | ProcessorResponseID          | ProcessorTID                 |
| RequestedAmount          | RequestedAmountCurrency Code | TargetAmount                 |
| TargetCurrency           | TotalTaxAmount               | TransactionRefNumber         |
| XID                      |                              |                              |
| **PaymentMethod Fields**                                                             |||
| AccountSuffix            | BankAccountName              | BankCode                     |
| BoletoBarCodeNumber      | BoletoNumber                 | CardType                     |
| CheckNumber              | ExpirationMonth              | ExpirationYear               |
| IssueNumber              | MandateId                    | MandateType                  |
| SignatureDate            | StartMonth                   | StartYear                    |
| WalletType               |                              |                              |
| **Profile Fields**                                                                   |||
| Name                     | ProfileDecision              | ProfileMode                  |
| RuleDecision             | RuleName                     |                              |
| **Recipient Fields**                                                                 |||
| RecipientBillingAmount   | RecipientBillingCurrency     |                              |
| **Request Fields**                                                                   |||
| Comments                 | MerchantID (\*)              | MerchantReferenceNumber      |
| RequestID (\*)           | Source                       | SubscriptionID               |
| TransactionDate (\*)     | User                         |                              |
| **Risk Fields**                                                                      |||
| AppliedAVS               | AppliedCV                    | AppliedCategoryGift          |
| AppliedCategoryTime      | AppliedHostHedge             | AppliedThreshold             |
| AppliedTimeHedge         | AppliedVelocityHedge         | BinAccountType               |
| BinCountry               | BinIssuer                    | BinScheme                    |
| CodeType                 | CodeValue                    | ConsumerLoyalty              |
| ConsumerPasswordProvided | ConsumerPromotions           | CookiesAccepted              |
| CookiesEnabled           | DeviceFingerPrint            | Factors                      |
| FlashEnabled             | GiftWrap                     | HostSeverity                 |
| IPCity                   | IPCountry                    | IPRoutingMethod              |
| IPState                  | ImagesEnabled                | JavascriptEnabled            |
| LostPassword             | ProductRisk                  | ProxyIPAddress               |
| ProxyIPAddressActivities | ProxyIPAddressAttributes     | ProxyServerType              |
| RepeatCustomer           | ReturnsAccepted              | Score                        |
| TimeLocal                | TrueIPAddress                | TrueIPAddressAttributes      |
| TrueIPAddressCity        | TrueIPAddressCountry         | TrueIPaddressActivities      |
| Sender Fields                                                                        |||
| SenderReferenceNumber    |                              |                              |
| **Settlement Fields**                                                                |||
| SettlementAmount (\*)    | SettlementCurrencyCode (\*)  | SettlementDate (\*)          |
| SourceResponseCode       | SourceResponseMessage        | Status                       |
| **ShipTo Fields**                                                                    |||
| Address1                 | Address2                     | City                         |
| Country                  | FirstName                    | LastName                     |
| Phone                    | State                        | Zip                          |
| **Shipping Fields**                                                                  |||
| Carrier                  | Method                       |                              |
| **Token Fields**                                                                     |||
| TokenCode                |                              |                              |
| **Travel Fields**                                                                    |||
| CompleteRoute            | DepartureDateTime            | JourneyType                  |
| Number                   | PassengerEmail               | PassengerFirstName           |
| PassengerId              | PassengerLastName            | PassengerPhone               |
| PassengerStatus          | PassengerType                |                              |
[Fields Available in the Settlement Details Report]

Net Funding {#ID-00003b71}
==========================

You can view the daily interchange, discount, and standard assessments in the Net Funding report. Some month-end fees, such as authorizations, are detected at the end of the month and appear in the Net Funding report on that particular day. Total Net Funding is obtained after subtracting chargebacks, fees, and any other negative amounts.  
By default, the report shows data from the prior day, but you can also choose to view by the previous week, previous month, previous three months, or previous six months. You can also choose to export the data to a CSV, XML, or JSON file.  
The Net Funding report is available only to select merchants. For more information, contact your representative.

Viewing the Net Funding Report {#ID-00003b75}
=============================================

1. In the left navigation panel, click the Reporting icon.
2. Under Financial Reports, click Net Funding. The Net Funding page appears.
3. In the search toolbar, select the Date Range of transactions to be included in the report. Account-level users can also select a merchant or group.
4. Select the Currency in which you want transactions to appear.
5. Click Export and choose your desired file format.
6. Follow your browser's instructions to open and save the file.

Original Credit `Transaction Reports` for Acquirers {#ID-00003b8c}
==================================================================

An Original Credit Transaction (OCT) is a financial transaction that delivers funds directly to a recipient's eligible account. Unlike a purchase transaction, which debits a cardholder's account, an OCT credits the cardholder's account.  
The funds flow in a different direction than in typical card transaction. A full financial BIN is required and the liability to pay lies with the acquirer. Once the issuer accepts the transaction the transaction is completed and funds are pulled from the acquirer in the next settlement window. There are no reversals or chargebacks that can be originated by the acquirer.  
Original Credit Transactions can be used for a variety of services:

* Money Transfers
* Funds Disbursements
* Prepaid Loads
* Merchant Settlements
* Credit Card Bill Payments
* Loyalty and Offers
* Wallet Transfers

For instructions on creating report subscriptions and generating these reports, see [Creating and Accessing Downloadable Reports](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Creating_Accessing_Downloadable_Reports.md "").

| Report Name                            | Description                                                                                                   |
|:---------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| Acquirer Detail Report                 | Provides a detailed listing of all OCT transactions.                                                          |
| Acquirer Exception Detail Report       | Provides exception transactions for one processing day.                                                       |
| Acquirer Chargeback Detail Report      | Provides chargebacks and chargeback reversal transactions received by the acquirer during the processing day. |
| Acquirer Reconciliation Summary Report | Provides a summary of total OCT transactions and total amount processed.                                      |
[Acquirer Original Credit `Transaction Reports`]

Fields Available in Original Credit `Transaction Reports` {#ID-00003bc3}
========================================================================

The following sections contain details for which fields are available in each report. For more information about specific fields, including descriptions, field type and length, see [Report Fields and Descriptions](/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/c_Report_Fields_and_Descriptions.md "").

Acquirer Detail Report {#ID-00003bc6}
=====================================

|--------------------------------|---------------------------------------------|-------------------------------|
| **Additional Information Fields**                                                                          |||
| CardAcceptorID                 | CardAcceptorName                            | CardAcceptorTerminalID        |
| ForwardingInstutionID          | IssuerAffiliateBIN                          | MerchantType                  |
| RecurringPaymentIndicator Flag |                                             |                               |
| **Fee Fields**                                                                                             |||
| ReimbursementFee               | ReimbursementFeeDebit CreditIndicator       | SettlementServiceIndicator    |
| TransactionIntegrityFee        | TransactionIntegrityFeeDebitCreditIndicator |                               |
| **Settlement Fields**                                                                                      |||
| CardholderBillingAmount        | CardholderBillingCurrency Code              | OctSettlementAmount           |
| OctSettlementCurrencyCode      | RateTableDate                               |                               |
| **Transaction Details Fields**                                                                             |||
| AcquirerBusinessID             | AcquiringInstitutionID                      | AffiliateBIN                  |
| AuthorizationIDRespCode        | BatchNumber                                 | BusinessApplicationIdentifier |
| CardNumber                     | CurrencyCodeFor TransactionAmount           | DCCIndicator                  |
| DataRecipient                  | DestinationStationID                        | DowngradeReasonCode           |
| FundsTransferSRE               | IssuerAcquirerIndicator                     | MVVCode                       |
| MerchantID                     | MessageReasonCode                           | NetworkID                     |
| OnlineSettlementDate           | PaymentMethodDescription                    | PaymentMethodType             |
| ProcessingCode                 | ProcessorID                                 | ProductID                     |
| ProductSubtype                 | RequestID                                   | RequestMessageType            |
| ResponseCode                   | RetrievalReferenceNumber                    | SettlementRptEntity           |
| STIPReasonCode                 | SettlementDate                              | SourceMerchantID              |
| SourceOfFunds                  | SourceStationID                             | TraceNumber                   |
| TransactionAmount              | TransactionIdentifier                       | VssProcessingDate             |
[Fields Available in the Acquirer Detail Report]

Acquirer Chargeback Detail Report {#ID-00003c6d}
================================================

|----------------------------|--------------------------|----------------------------------|
| **Chargeback Fields**                                                                  |||
| ChargebackReference Number | ClientCaseNumber         | DisputeCondition                 |
| DisputeStatus              | DocumentationIndicator   | MessageText                      |
| MessageType                | TransmissionDate         | UsageCode                        |
| VROLBundledCaseNumber      | VROLCaseNumber           | VROLFinancialID                  |
| **Transaction Details Fields**                                                         |||
| AcquirerBusinessID         | AcquiringInstitutionID   | CurrencyCodeForTransactionAmount |
| MerchantID                 | PaymentMethodDescription | PaymentMethodType                |
| RequestID                  | SettlementDate           | SourceMerchantID                 |
| TraceNumber                | TransactionAmount        |                                  |
[Fields Available in the Acquirer Chargeback Detail Report]

Acquirer Exception Detail Report {#ID-00003cb8}
===============================================

|--------------------------------|---------------------------------------------|-------------------------------|
| **Additional Information Fields**                                                                          |||
| CardAcceptorID                 | CardAcceptorName                            | CardAcceptorTerminalID        |
| ForwardingInstutionID          | IssuerAffiliateBIN                          | MerchantType                  |
| RecurringPaymentIndicator Flag |                                             |                               |
| **Fee Fields**                                                                                             |||
| ReimbursementFee               | ReimbursementFeeDebit CreditIndicator       | SettlementServiceIndicator    |
| TransactionIntegrityFee        | TransactionIntegrityFeeDebitCreditIndicator |                               |
| **Settlement Fields**                                                                                      |||
| AcquirerBusinessID             | AcquiringInstitutionID                      | AffiliateBIN                  |
| AuthorizationIDRespCode        | BatchNumber                                 | BusinessApplicationIdentifier |
| CardNumber                     | CurrencyCodeFor TransactionAmount           | DCCIndicator                  |
| DataRecipient                  | DestinationStationID                        | DowngradeReasonCode           |
| FundsTransferSRE               | IssuerAcquirerIndicator                     | MVVCode                       |
| MerchantID                     | MessageReasonCode                           | NetworkID                     |
| OnlineSettlementDate           | PaymentMethodDescription                    | PaymentMethodType             |
| ProcessingCode                 | ProcessorID                                 | ProductID                     |
| ProductSubtype                 | RequestID                                   | RequestMessageType            |
| ResponseCode                   | RetrievalReferenceNumber                    | SettlementRptEntity           |
| STIPReasonCode                 | SettlementDate                              | SourceMerchantID              |
| SourceOfFunds                  | SourceStationID                             | TraceNumber                   |
| TransactionAmount              | TransactionIdentifier                       | VssProcessingDate             |
[Fields Available in the Acquirer Exception Detail Report]

Acquirer Reconciliation Summary Report {#ID-00003d4d}
=====================================================

|----------------------------|--------------------------|---------------------------|
| **OCT Summary Fields**                                                          |||
| AccountID                  | CardAcceptorID           | MerchantID                |
| ResellerID                 | SettlementAmountCurrency | SettlementDate            |
| TotalAmountProcessed       | TotalAmountSettled       | TotalFee                  |
| TotalTransactionsProcessed | TotalTransactionsSettled | TransactionAmountCurrency |
[Fields Available in the Acquirer Reconciliation Summary Report]

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

