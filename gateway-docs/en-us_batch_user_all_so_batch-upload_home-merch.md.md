Introduction to Offline Transaction File Submission {#home-merch}
=================================================================

`Payment Gateway` supports the offline submission of multiple payment requests specified in a single file. Instead of submitting individual requests, you can upload a file that contains a set, or *batch* , of transaction requests. You specify the same information for a batched request as you would specify for an individually submitted request. One *batch file* can include transactions that use different services, currencies, countries, merchant IDs, and card types, thus eliminating the burden of handling these values separately.  
This guide describes how to upload a batch file using the `Payment Gateway` `Business Center`.  
`Payment Gateway` attempts to validate the contents of the uploaded batch file and, if any errors are detected in the file, none of the batched requests are processed. File validation results and transaction processing results are available through email notifications, results files, and downloadable reports.
` Payment Gateway ` recommends against using the batch upload feature for TID-based processors or APACS-based processors. With these processors, transactions submitted through batch files can result in timeouts and errors. For more information, contact customer support.
