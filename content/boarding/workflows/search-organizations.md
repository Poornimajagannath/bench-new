# Search for Organizations

<!-- section:prose -->
Find organizations and view hierarchy from the Business Center.
<!-- /section:prose -->

_Generated from `normalized/2026-08-08-boarding.claims.json`; do not hand-edit. Fix the source and regenerate._

<!-- section:facts -->

## Preconditions

- **Gap:** no prerequisite is specified in the source docs.

## API endpoints

### Retrieve a List of Organizations

- **Method:** `GET`
- **Path:** `/oms/v1/organizations`
- **production host:** `https://api.cybersource.com`

#### Example request

```json
GET https://api.cybersource.com/oms/v1/organizations?hierarchyQery=org1.descendents.1
```

#### Example response

```json
200 OK
```

- <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:get:ecdba5a5`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-retrieve-organizations)</sub>

### Retrieve a List of Organizations

- **Method:** `GET`
- **Path:** `/oms/v1/organizations`
- **test host:** `https://apitest.cybersource.com`

#### Example request

```json
GET https://api.cybersource.com/oms/v1/organizations?hierarchyQery=org1.descendents.1
```

#### Example response

```json
200 OK
```

- <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:get:c4f0fff5`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-retrieve-organizations)</sub>

### Retrieve a List of Organizations

- **Method:** `GET`
- **Path:** `/oms/v1/organizations?hierarchyQery`
- **production host:** `https://api.cybersource.com`

#### Example request

```json
GET https://api.cybersource.com/oms/v1/organizations?hierarchyQery=org1.descendents.1
```

#### Example response

```json
200 OK
```

- <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:get:88be0d9d`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-retrieve-organizations)</sub>

### Retrieve Organization Details

- **Method:** `GET`
- **Path:** `/oms/v1/organizations/{organizationId}`
- **production host:** `https://api.cybersource.com`

#### Example request

```json
GET https://api.cybersource.com/oms/v1/organizations/org1
```

#### Example response

```json
200 OK
```

- <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:get:69b7b081`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-retrieve-an-organization)</sub>

### Retrieve Organization Details

- **Method:** `GET`
- **Path:** `/oms/v1/organizations/{organizationId}`
- **test host:** `https://apitest.cybersource.com`

#### Example request

```json
GET https://api.cybersource.com/oms/v1/organizations/org1
```

#### Example response

```json
200 OK
```

- <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:get:9f1787e8`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-retrieve-an-organization)</sub>

### Retrieve Organization Details

- **Method:** `GET`
- **Path:** `/oms/v1/organizations/org1`
- **production host:** `https://api.cybersource.com`

#### Example request

```json
GET https://api.cybersource.com/oms/v1/organizations/org1
```

#### Example response

```json
200 OK
```

- <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:get:83fa335c`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-retrieve-an-organization)</sub>


## Steps

### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_merchants-v2-search-results-view-org-hierarchy.md.md`

1. **Action:** Find the merchant in search results and click the three dots (...) in the More column.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-search-results-view-org-hierarchy:step:1:0102ee5b`</sub>
2. **Action:** Select View Organization Hierarchy. The organizations immediately above and below the organization are displayed. You can view the hierarchy of these organizations by repeating the steps above.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-search-results-view-org-hierarchy:step:2:a759b28a`</sub>
### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_merchants-v2-search.md.md`

1. **Action:** In the left navigation panel, click the **Portfolio Management** icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-search:step:1:120914e3`</sub>
2. **Action:** Under Merchants, click **Manage Merchants**. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-search:step:2:818e5383`</sub>
3. **Action:** Click **Search** to search for all merchants or use the search filters. There are three default search filters:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-search:step:3:c256c329`</sub>
4. **Action:** To add a filter, click **+ Add Filter**. Select a filter using the drop-down menu, or search for a filter by entering text into the New Filter field.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-search:step:4:d74b4c90`</sub>
5. **Action:** Click **Search** when you finish adding filters.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-search:step:5:d81558aa`</sub>
6. **Action:** To reset the search filters and start over, click **Reset Search** . To understand how to use the search results, see [Search Results](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/merchants-v2-search/merchants-v2-search-results.md).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-search:step:6:19c5eb67`</sub>
### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_merchants-v2-search_merchants-v2-search-results-view-org-hierarchy.md.md`

1. **Action:** Find the merchant in search results and click the three dots (...) in the More column.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-search_merchants-v2-search-results-view-org-hierarchy:step:1:de226944`</sub>
2. **Action:** Select **View Organization Hierarchy**. The organizations immediately above and below the organization are displayed. You can view the hierarchy of these organizations by repeating the steps above.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-search_merchants-v2-search-results-view-org-hierarchy:step:2:ec54ca69`</sub>

## Constraints

- [hierarchy_limit] * `distance` indicates levels of hierarchy.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro_boarding-retrieve-organizations_boarding-retrieve-organizations-query-parameters:prose:d1a55cdefae7`</sub> · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro_boarding-retrieve-organizations_boarding-retrieve-organizations-query-parameters.md.md
- [hierarchy_limit] You can provide a whole number to specify the number levels of hierarchy to return.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro_boarding-retrieve-organizations_boarding-retrieve-organizations-query-parameters:prose:48cc94fecad6`</sub> · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro_boarding-retrieve-organizations_boarding-retrieve-organizations-query-parameters.md.md

## Failure modes

- **Gap:** no error cases documented for this workflow in the source docs.

<!-- /section:facts -->
