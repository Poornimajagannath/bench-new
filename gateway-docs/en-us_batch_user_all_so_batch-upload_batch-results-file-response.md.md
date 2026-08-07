Viewing the Results of Batch File Validation {#batch-results-file-response}
===========================================================================

After a transaction batch file is uploaded, `Payment Gateway` checks the validity of the file contents and then creates a batch validation response file. This XML-formatted file shows whether the batch file validation succeeded or failed.  
The name of a batch validation response file associates the file with a specific batch file. The result files are identified by the merchant ID and the batch ID:

* The filename has this format: `&lt;merchantID&gt;.&lt;batchID&gt;.validate.xml`

* This is an example filename: `CyberVacations.39768.validate.xml`
  In addition to creating batch validation response files, ` Payment Gateway ` sends an email notification when a batch validation fails or succeeds. See [Viewing Email Notifications](/docs/gateway/en-us/batch/user/all/so/batch-upload/batch-results-email-notifs.md "").  
  The topics in this section cover this information:

* How to download a batch validation response file

* The structure of a batch validation response file

* The XML elements of a batch validation response file

* Error codes in a batch validation response

* Example batch validation response files

