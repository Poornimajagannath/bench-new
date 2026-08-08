# Change an Organization's Status

<!-- section:prose -->
Move an organization between statuses after boarding.
<!-- /section:prose -->

_Generated from `normalized/2026-08-08-boarding.claims.json`; do not hand-edit. Fix the source and regenerate._

<!-- section:facts -->

## Preconditions

- **Gap:** no prerequisite is specified in the source docs.

## API endpoints

### Change an Organization's Status

- **Method:** `GET`
- **Path:** `/oms/v1/organizations/{organizationId}`
- **production host:** `https://api.cybersource.com`

#### Example request

```json
{}
```

#### Example response

```json
200 OK
```

- <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:get:662fc29c`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-change-org-status)</sub>

### Change an Organization's Status

- **Method:** `GET`
- **Path:** `/oms/v1/organizations/{organizationId}`
- **test host:** `https://apitest.cybersource.com`

#### Example request

```json
{}
```

#### Example response

```json
200 OK
```

- <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:get:6ff93759`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-change-org-status)</sub>


## Steps

### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_merchants-v2-status-change.md.md`

1. **Action:** Find the merchant in the search results and click the eyeball icon in the More column.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-status-change:step:1:6739b4df`</sub>
2. **Action:** Click the **Status** drop-down menu in the upper-right side of the page and select a status.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-status-change:step:2:780c8902`</sub>
3. **Action:** Click **Confirm**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-status-change:step:3:86078fe2`</sub>

## Constraints

- **Gap:** no constraint-kind claims found for this workflow.

## Failure modes

- **Gap:** no error cases documented for this workflow in the source docs.

<!-- /section:facts -->
