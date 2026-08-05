Viewing the Results of Transaction Processing {#batch-results-txn-response}
===========================================================================

After a transaction batch file is validated successfully, `Cybersource` processes the transactions specified in the batch file and then creates *transaction response files*. These CSV-formatted files show the processing results for the batched transaction requests.  
One response file lists processing results for all transactions, whether accepted, rejected, or in error. The other response file lists results only for transactions that were rejected or that triggered a processing error.

Full list of transaction responses
:
This file lists results only for transactions that were rejected or that triggered a processing error.

    * File name format: `&lt;merchantID&gt;.&lt;batchID&gt;.reply.all`
    * File name example: `CyberVacations.12345.reply.all`

List of exceptions
:
This file lists results only for transactions that were rejected or that triggered a processing error.

    * File name format: `&lt;merchantID&gt;.&lt;batchID&gt;.reply.rejected`
    * File name example: `CyberVacations.12345.reply.rejected`

When all transactions requested in a batch file succeed, an email notification is sent.

```
Batch with batchID=55555 was validated successfully.
```

When processing of batched transaction requests succeeds, an email notification is sent. See [Email Notification for Successful Transaction Processing](/docs/cybs/en-us/batch/user/all/so/batch-upload/batch-results-email-notifs/batch-results-email-notifs-successful-txns.md "").  
The topics in this section cover this information:

* How to download a transaction response file
* The header of a transaction response file
* The data records in a transaction response file
* An example transaction response file

