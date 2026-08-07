Understanding Organization IDs {#boarding-intro-ids}
====================================================

Organizations relate to each other using IDs. Every organization is assigned an organization ID. When an organization has a subordinate, it is assigned a child ID that identifies the subordinate. The subordinate is assigned a parent ID that identifies the parent organization. Organization IDs must be unique, not just within the portfolio or account, but across the system.  
In the illustration below, merchant's ID is `Merchant Account 1`. The merchant's child IDs are `Transacting MID1` and `Transacting MID2`. The merchant's parent ID is `Portfolio`.

#### Figure: {#boarding-intro-ids_fig_ut4_p5f_q5b}

Understanding Organization IDs ![](/content/dam/new-documentation/documentation/en-us/topics/platform/bam/boarding/images/create-merchant-account-new-transacting.svg/jcr:content/renditions/original)  
IMPORTANT Do not include sensitive information in the Org ID field. A security validation check is in place to ensure that the unique Org ID field (e.g., Cybersource MID) does not contain PAN or other sensitive information to provide an additional layer of protection for your data during the onboarding process.
