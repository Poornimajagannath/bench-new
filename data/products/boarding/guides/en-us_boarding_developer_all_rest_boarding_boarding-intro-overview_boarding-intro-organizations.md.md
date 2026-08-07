Understanding Accounts and Organizations {#boarding-intro-organizations}
========================================================================

You are assigned a **portfolio** account when you sign up. All merchant accounts are subordinate to the portfolio account. A merchant account consists of a **merchant** organization and its subordinate organizations, which always includes at least one **transacting** organization. You can use **structural** organizations to extend the hierarchy of merchant accounts.

* The **portfolio** account is always the top node in the hierarchy.

* A **merchant** organization represents a business entity. For example, a brand or company. There can only be one merchant in any branch of the hierarchy.

* A **transacting** organization represents an entity that processes payment transactions. For example, a physical store or a payment form on a web page or app. No other organization can be directly subordinate to a transacting organization.

* A **structural** organization represents a conceptual entity that enables you to build an expansive hierarchy between merchant and transacting nodes. For more information on using structural organizations to extend the hierarchy, see [Extending the Hierarchy](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-extend-hierarchy.md "").  
  The image below shows a simple merchant account. The merchant organization is directly beneath the portfolio organization, and contains one transacting organization.

  #### Figure: {#boarding-intro-organizations_fig_cnv_xgj_cfc}

  Sample Merchant Account ![](/content/dam/new-documentation/documentation/en-us/topics/platform/bam/boarding-user/images/create-merchant-account.svg/jcr:content/renditions/original)
  {#boarding-intro-organizations_ul_e22_mgl_g5b}

