# Change an Organization's Status

<!-- section:prose -->
Move an organization between statuses after boarding.
<!-- /section:prose -->

_Generated from `normalized/2026-08-08-boarding.claims.json`; do not hand-edit. Fix the source and regenerate._

<!-- section:facts -->

## Preconditions

- **Gap:** no prerequisite is specified in the source docs.

## Steps

### REST API path

1. **API:** `GET /oms/v1/organizations/{organizationId}` — Change an Organization's Status
   - Actor: Partner system (REST API)
   - test host: `https://apitest.cybersource.com`
   - Required fields: **Gap:** not listed for this endpoint in the source.
   - Example request:
     ```json
     {}
     ```
   - Expected outcome: HTTP 200 OK (see example response).
   - outcome_missing: false
   - Example response:
     ```json
     200 OK
     ```
   - <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:get:6ff93759`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-change-org-status)</sub>

### Business Center UI path

2. **Action:** Find the merchant in the search results and click the eyeball icon in the More column.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-status-change:step:1:6739b4df`</sub>

3. **Action:** Click the **Status** drop-down menu in the upper-right side of the page and select a status.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-status-change:step:2:780c8902`</sub>

4. **Action:** Click **Confirm**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-status-change:step:3:86078fe2`</sub>

<!-- sequence_stats: steps=4 outcome_gaps=3 outcome_missing=3 api_ops=1 ui_steps=3 -->

## Constraints

- **Gap:** no constraint-kind claims found for this workflow.

## Failure modes

- **Gap:** no error cases documented for this workflow in the source docs.

<!-- /section:facts -->
