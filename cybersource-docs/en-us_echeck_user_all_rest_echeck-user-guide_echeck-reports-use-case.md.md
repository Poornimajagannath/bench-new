eCheck Reconciliation Reporting Case Study {#echeck-reports-use-case}
=====================================================================

This case study shows an example of eight business days' worth of eCheck activity and how that activity appears on reconciliation reports.  
These reports are reconciliation reports:

* Funding Details Report

* Deposit Details Report

* Chargeback Details Report  
  The case study is written assuming that these things are true about the merchant account:

* Risk Reserve Target: $1,000.00

* Risk Reserve Rate: 10%

* Funding Hold Period: 3 days

* Monthly Transaction Volume Limit: $40,000.00

Day 1 {#echeck-reports-use-case-day1}
=====================================

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/funding-scenario-day-01.svg/jcr:content/renditions/original)  
On day 1, the merchant processes four debit transactions totaling $9,900. The merchant does not process any credit transactions. Because of the 3-day funding hold, no money is moved to the reserve account. All money for day 1 is moved to the settlement account. No reconciliation reports are generated because nothing is funded yet.

Day 2 {#echeck-reports-use-case-day2}
=====================================

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/funding-scenario-day-02.svg/jcr:content/renditions/original)  
On day 2, the merchant processes three debit transactions totaling $4,000 and no credit transactions. Because of the 3-day funding hold, no money is moved to the reserve account. All money for day 2 is moved to the settlement account. No reconciliation reports are generated because nothing is funded yet.

Day 3 {#echeck-reports-use-case-day3}
=====================================

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/funding-scenario-day-03.svg/jcr:content/renditions/original)  
On day 3, the merchant processes one debit transaction totaling $2,000 and one credit transaction totaling $3,000. Because of the 3-day funding hold, no money is moved to the reserve account. All money for day 3 is moved to the settlement account. In this case, because there is $1,000 more credit than debit, $1,000 is removed from the settlement account. No reconciliation reports are generated because nothing is funded yet.

Day 4 {#echeck-reports-use-case-day4}
=====================================

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/funding-scenario-day-04.svg/jcr:content/renditions/original)  
On day 4, the merchant processes three debit transactions totaling $7,000. The merchant does not process any credit transactions. Day 1 is now funded due to the lapse of the 3-day holding period. $990 is moved to the risk reserve account because the risk reserve rate is 10%, and the day 1 total was $9,900. The day 4 total is moved to the settlement account. $5,910 is funded. That amount reflects the settlement account balance, minus the debit totals for days 2, 3, and 4, minus the reserve amount ($990). Because funding occurred, reconciliation reports are generated for day 1 transactions and day 3 credit (there are no holds on credits).

Day 5 {#echeck-reports-use-case-day5}
=====================================

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/funding-scenario-day-05.svg/jcr:content/renditions/original)  
On day 5, the merchant processes two debit transactions totaling $500, and one credit transaction totaling $5,000. $10 is moved to the risk reserve account, bringing the risk reserve account up to its full $1,000. The target funding amount is a negative amount (-$1,010), so nothing is funded on day 5. The settlement amount is -$4,500, so $4,500 is removed from the settlement account. No reconciliation reports are generated because nothing was funded.

Day 6 {#echeck-reports-use-case-day6}
=====================================

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/funding-scenario-day-06.svg/jcr:content/renditions/original)  
On day 6, the merchant processes three debit transactions totaling $8,250 and credit transactions totaling $500. The sum of credit and debit transactions ($7,750) is moved to the settlement account. $490 is funded from days 2 and 3, based on the settlement account balance, minus the debit amounts for days 4, 5, and 6. Reconciliation reports are generated for day 2 and 3 transactions and day 5 and 6 credits.  
On day 6, the $40,000 monthly transaction limit is reached. Consequently, all funding and all credit transactions are put on hold until the following month or until the limit is raised.  
To request that the monthly transaction processing limit is raised, visit the Support Center:  
<http://support.visaacceptance.com>

Day 7 {#echeck-reports-use-case-day7}
=====================================

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/funding-scenario-day-07.svg/jcr:content/renditions/original)  
On day 7, the merchant processes three debit transactions totaling $2,000 and no credit transactions. $2,000 is moved to the settlement account. $5,750 is funded from day 4, based on the settlement account balances, minus days 5 and 6, and day 7 debit amounts. Reconciliation reports are generated for day 4 transactions and day 7 credits.  
On day 7, a Chargeback Details Report is generated because two returns were sent back by payment processors. A debit for $1,500 was returned because of an incorrect account number, and a credit for $250 was returned because the account was closed. The reason codes listed in the chargeback details report are ACH return codes.

Day 8 {#echeck-reports-use-case-day8}
=====================================

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/funding-scenario-day-08.svg/jcr:content/renditions/original)  
On day 8, the merchant processes three debit transactions totaling $5,000 and no credit transactions. $5,000 is moved to the settlement account. $500 is funded from day 5 and $5,750 is re-deposited (because there was no account to which to move it), for a total deposit amount of $6,250.
