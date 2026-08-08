# Ingestion report

Milestone 0.5: corpus cleaned at the door. `raw/` is immutable evidence; serve layers read only `normalized/` and `content/`.

- Stamp date: `2026-08-08-boarding`
- Docs fetched into raw: 190
- Claims extracted: 2360
- Raw dir: `raw/2026-08-08-boarding`
- Normalized file: `normalized/2026-08-08-boarding.claims.json`
- Read contract: normalized/, content/
- Forbidden: raw/

## Claims by schema

| Schema | Count |
| --- | ---: |
| quickstart_step | 969 |
| endpoint_fact | 0 |
| error_case | 65 |
| prose_claim | 214 |
| field_table | 1112 |

## Drop log

| Path | Reason | Bytes | First heading | Detail |
| --- | --- | ---: | --- | --- |
| en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-about-guide.md.md | quarantine_policy | 922 | About This Guide | census kind=index_navigation — excluded by policy |
| en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-doc-rev.md.md | quarantine_policy | 1484 | Recent Revisions to This Document | census kind=index_navigation — excluded by policy |
| en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro.md.md | quarantine_policy | 282 | Product Boarding Template Reference | census kind=index_navigation — excluded by policy |
| en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-card.md.md | quarantine_policy | 314 | Card Processing Templates | census kind=index_navigation — excluded by policy |
| en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-tasks.md.md | quarantine_policy | 130 | Using Templates | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-about-guide.md.md | quarantine_policy | 899 | Merchant Boarding | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-about-guide_boarding-revisions.md.md | quarantine_policy | 3036 | Recent Revisions to This Document | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-intro-overview.md.md | quarantine_policy | 784 | Introduction to the Boarding Registration Service | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-intro-templat-0.md.md | quarantine_policy | 1906 | Product Templates | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-intro-template.md.md | quarantine_policy | 1906 | Product Templates | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-intro-template_templates-components.md.md | quarantine_policy | 1179 | Template Components | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-intro-template_templates-products.md.md | quarantine_policy | 332 | Products | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro.md.md | quarantine_policy | 776 | Manage Organizations | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro_boarding-change-org-status_boarding-change-org-status-example.md.md | quarantine_policy | 244 | REST Example: Changing an Organization's Status | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro_boarding-retrieve-an-organization_boarding-retrieve-an-organization-example.md.md | quarantine_policy | 282 | REST Example: Retrieving an Organization | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro_boarding-retrieve-organizations_boarding-retrieve-organizations-example.md.md | quarantine_policy | 346 | REST Example: Retrieving a List of Organizations | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro_boarding-update-information-api_boarding-update-information-api-example.md.md | quarantine_policy | 375 | REST Example: Updating an Organization's Information | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-products-intro.md.md | quarantine_policy | 1799 | Product Enablement and Configuration Using the BRS API | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth_boarding-payer-auth-enable-intro.md.md | quarantine_policy | 546 | Enable `Payer Authentication` | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_boarding-tms-enable-intro.md.md | quarantine_policy | 529 | Enable `Token Management Service` Using a Template | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_boarding-tms-enable-net-tkn-existing-intro.md.md | quarantine_policy | 748 | Enable `TMS` and Enroll in Network Tokenization for an Existing Merchant | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_boarding-tms-enable-net-tkn-intro.md.md | quarantine_policy | 663 | Enable `TMS` and Enroll in Network Tokenization for a New Merchant | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-tms_boarding-pecs-tms-enable-intro.md.md | quarantine_policy | 571 | Enable `TMS` with a Template Using the PECS API | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-tms_boarding-pecs-tms-enable-net-tkn-intro.md.md | quarantine_policy | 628 | Enable `TMS` and Enroll in Network Tokenization Using the PECS API | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_boarding-reg-intro.md.md | quarantine_policy | 2443 | Create Organizations | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_templates-matrix-intro.md.md | quarantine_policy | 282 | Product Boarding Template Reference | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_templates-matrix-intro_templates-matrix-card.md.md | quarantine_policy | 314 | Card Processing Templates | census kind=index_navigation — excluded by policy |
| en-us_boarding_developer_all_rest_boarding_templates-tasks.md.md | quarantine_policy | 130 | Using Templates | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_boarding-about-guide.md.md | quarantine_policy | 888 | Merchant Boarding User Guide | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_boarding-about-guide_boarding-revisions.md.md | quarantine_policy | 932 | Recent Revisions to This Document | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_boarding-intro-overview.md.md | quarantine_policy | 909 | Introduction to the Boarding Registration Service | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_boarding-intro-template.md.md | quarantine_policy | 1905 | Product Templates | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_boarding-intro-template_templates-components.md.md | quarantine_policy | 1179 | Template Components | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_boarding-intro-template_templates-products.md.md | quarantine_policy | 332 | Products | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay.md.md | quarantine_policy | 195 | Alternative Payments | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-enablement-products-intro.md.md | quarantine_policy | 127 | Enablement-Only Products | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro.md.md | quarantine_policy | 1019 | Create Organizations | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_merchants-v2-edit-intr-0.md.md | quarantine_policy | 695 | Managing Organization Information (Version 2) | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_merchants-v2-edit-intro.md.md | quarantine_policy | 682 | Manage Organization Information | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_merchants-v2-edit-products-intro.md.md | quarantine_policy | 718 | Update an Organization's Products | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_merchants-v2-search-results.md.md | quarantine_policy | 1100 | Search Results (Version 2) | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_merchants-v2-search_merchants-v2-search-results.md.md | quarantine_policy | 1071 | Search Results | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_merchants-v2-status-chang-0.md.md | quarantine_policy | 391 | Changing an Organization's Status (Version 2) | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_templates-matrix-intro.md.md | quarantine_policy | 282 | Product Boarding Template Reference | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_templates-matrix-intro_templates-matrix-card.md.md | quarantine_policy | 314 | Card Processing Templates | census kind=index_navigation — excluded by policy |
| en-us_boarding_user_all_ebc_boarding-user_templates-tasks.md.md | quarantine_policy | 130 | Using Templates | census kind=index_navigation — excluded by policy |
| 2026-08-08-boarding/en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-about.md.md | no_schema_match | 898 | Boarding Templates | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-about_templates-components.md.md | no_schema_match | 1104 | Template Components | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-pa.md.md | no_schema_match | 2003 | Payer Authentication Templates | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-extend-hierarchy_boarding-extend-hierarchy-diagram.md.md | no_schema_match | 934 | Hierarchy Example | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-extend-hierarchy_boarding-reg-create-structural-api.md.md | no_schema_match | 620 | Add a Structural Organization to a Merchant Organization | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-extend-hierarchy_boarding-reg-create-structural-api_boarding-reg-create-structural-api-example.md.md | no_schema_match | 2121 | REST Example: Creating a Structural Organization | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-extend-hierarchy_boarding-reg-create-structural-api_boarding-reg-create-structural-api-req-fields.md.md | no_schema_match | 629 | Required Fields for Boarding a Structural Organization | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro_boarding-retrieve-organizations.md.md | no_schema_match | 753 | Retrieve a List of Organizations | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro_boarding-update-information-api.md.md | no_schema_match | 916 | Update an Organization's Information | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth_boarding-payer-auth-enable-intro_boarding-payer-auth-enable-ex-rest.md.md | no_schema_match | 4406 | REST Example: Enabling `Payer Authentication` | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_boarding-tms-enable-intro_boarding-tms-enable-ex-rest.md.md | no_schema_match | 1616 | REST Example: Enabling `TMS` Using a Template | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_boarding-tms-enable-intro_boarding-tms-enable-reqfields.md.md | no_schema_match | 4269 | Required Fields for Enabling `TMS` Using a Template | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_boarding-tms-enable-net-tkn-existing-intro_boarding-tms-enable-net-tkn-existing-ex-rest.md.md | no_schema_match | 4265 | REST Example: Enabling `TMS` and Enrolling in Network Tokenization for an Existing Merchant | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_boarding-tms-enable-net-tkn-existing-intro_boarding-tms-enable-net-tkn-existing-reqfields.md.md | no_schema_match | 11083 | Required Fields for Enabling `TMS` and Enrolling in Network Tokenization for an Existing Merchant | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_boarding-tms-enable-net-tkn-intro_boarding-tms-enable-net-tkn-ex-rest.md.md | no_schema_match | 3837 | REST Example: Enabling `TMS` and Enrolling in Network Tokenization for a New Merchant | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_boarding-tms-enable-net-tkn-intro_boarding-tms-enable-net-tkn-reqfields.md.md | no_schema_match | 11044 | Required Fields for Enabling `TMS` and Enrolling in Network Tokenization for a New Merchant | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy.md.md | no_schema_match | 809 | Token Vault Management | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth_pecs-config-payerauth.md.md | no_schema_match | 529 | Configure `Payer Authentication` Using the PECS API | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-tms_boarding-pecs-tms-enable-intro_boarding-pecs-tms-enable-ex-rest.md.md | no_schema_match | 983 | REST Example: Enabling `TMS` with a Template Using the PECS API | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-tms_boarding-pecs-tms-enable-intro_boarding-pecs-tms-enable-reqfields.md.md | no_schema_match | 651 | Required Fields for Enabling `TMS` with a Template Using the PECS API | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-tms_boarding-pecs-tms-enable-net-tkn-intro_boarding-pecs-tms-enable-net-tkn-ex-rest.md.md | no_schema_match | 2676 | REST Example: Enabling `TMS` and Enrolling in Network Tokenization Using the PECS API | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-tms_boarding-pecs-tms-enable-net-tkn-intro_boarding-pecs-tms-enable-net-tkn-reqfields.md.md | no_schema_match | 3450 | Required Fields for Enabling `TMS` and Enrolling in Network Tokenization Using the PECS API | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-update-product-api_boarding-update-product-api-example.md.md | no_schema_match | 1017 | Example: Adding a New Product to an Existing Organization Using the PECS API | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-update-product-api_boarding-update-product-api-req-fields.md.md | no_schema_match | 412 | Required Fields for Adding a New Products | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-add-delete-processor.md.md | no_schema_match | 673 | Add and Delete a Processor Using the PECS API | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-add-delete-processor_pecs-add-delete-processor-ex.md.md | no_schema_match | 1883 | Example: Adding and Deleting a Processor Using the PECS API | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-add-processor.md.md | no_schema_match | 460 | Add a Processor Using the PECS API | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-add-processor_pecs-add-processor-ex.md.md | no_schema_match | 2150 | Example: Adding a Processor Using the PECS API | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-add-processor_pecs-add-processor-req-fields.md.md | no_schema_match | 2076 | Required Fields for Adding a Processor Using the PECS API | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-delete-processor.md.md | no_schema_match | 609 | Delete a Processor Using the PECS API | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-delete-processor_pecs-delete-processor-ex.md.md | no_schema_match | 1845 | Example: Deleting a Processor Using the PECS API | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-update-batch.md.md | no_schema_match | 465 | Update Batch Group Using the PECS API | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-update-batch_pecs-update-batch-ex.md.md | no_schema_match | 1354 | Example: Updating a Batch Group Using the API | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-update-batch_pecs-update-batch-req-fields.md.md | no_schema_match | 810 | Required Fields for Updating a Batch Group Using the PECS API | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-reg-create-transacting-integ-api-example.md.md | no_schema_match | 4765 | REST Example: Creating a Transacting Organization with Integration Information | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-reg-intro_boarding-reg-create-merch-api.md.md | no_schema_match | 536 | Create a Merchant Organization | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-reg-intro_boarding-reg-create-merch-api_boarding-reg-create-merch-api-example.md.md | no_schema_match | 2102 | REST Example: Creating a Merchant Organization | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-reg-intro_boarding-reg-create-merch-api_boarding-reg-create-merch-api-req-fields.md.md | no_schema_match | 2665 | Required Fields for Boarding a Merchant Organization | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-reg-intro_boarding-reg-create-new-transacting-api.md.md | no_schema_match | 705 | Add a Transacting Organization to a New Merchant Organization | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-reg-intro_boarding-reg-create-new-transacting-api_boarding-reg-create-new-transacting-api-example.md.md | no_schema_match | 3578 | REST Example: Creating a Transacting Organization | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-reg-intro_boarding-reg-create-new-transacting-api_boarding-reg-create-new-transacting-api-req-fields.md.md | no_schema_match | 2706 | Required Fields for Adding a Transacting Organization to an Existing Organization | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-reg-intro_boarding-reg-create-transacting-api_boarding-reg-create-transacting-api-example.md.md | no_schema_match | 7349 | REST Example: Creating a Transacting Organization | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-reg-intro_boarding-reg-create-transacting-api_boarding-reg-create-transacting-api-req-fields.md.md | no_schema_match | 2696 | Required Fields for Adding a Transacting Organization to an Existing Organization | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_templates-matrix-intro_templates-matrix-pa.md.md | no_schema_match | 2003 | Payer Authentication Templates | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-extend-hierarchy_boarding-extend-hierarchy-diagram.md.md | no_schema_match | 934 | Hierarchy Example | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy.md.md | no_schema_match | 809 | Token Vault Management | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_merchants-v2-edit-products-intr-0.md.md | no_schema_match | 670 | Updating an Organization's Products (Version 2) | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_templates-matrix-intro_templates-matrix-pa.md.md | no_schema_match | 2003 | Payer Authentication Templates | no quickstart/endpoint/error/prose claim extracted |

## Sampled human check (10 drops)

Do not triage by filename alone. For each row confirm shell vs missed claim.

| # | Path | Reason | Bytes | First heading |
| ---: | --- | --- | ---: | --- |
| 1 | `2026-08-08-boarding/en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-about.md.md` | no_schema_match | 898 | Boarding Templates |
| 2 | `2026-08-08-boarding/en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-about_templates-components.md.md` | no_schema_match | 1104 | Template Components |
| 3 | `2026-08-08-boarding/en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-pa.md.md` | no_schema_match | 2003 | Payer Authentication Templates |
| 4 | `2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-extend-hierarchy_boarding-extend-hierarchy-diagram.md.md` | no_schema_match | 934 | Hierarchy Example |
| 5 | `2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-extend-hierarchy_boarding-reg-create-structural-api.md.md` | no_schema_match | 620 | Add a Structural Organization to a Merchant Organization |
| 6 | `2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-extend-hierarchy_boarding-reg-create-structural-api_boarding-reg-create-structural-api-example.md.md` | no_schema_match | 2121 | REST Example: Creating a Structural Organization |
| 7 | `2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-extend-hierarchy_boarding-reg-create-structural-api_boarding-reg-create-structural-api-req-fields.md.md` | no_schema_match | 629 | Required Fields for Boarding a Structural Organization |
| 8 | `2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro_boarding-retrieve-organizations.md.md` | no_schema_match | 753 | Retrieve a List of Organizations |
| 9 | `2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro_boarding-update-information-api.md.md` | no_schema_match | 916 | Update an Organization's Information |
| 10 | `2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth_boarding-payer-auth-enable-intro_boarding-payer-auth-enable-ex-rest.md.md` | no_schema_match | 4406 | REST Example: Enabling `Payer Authentication` |
