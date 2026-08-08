# Send a Registration Email

<!-- section:prose -->
Send the merchant a registration email to create Business Center credentials.
<!-- /section:prose -->

_Generated from `normalized/2026-08-08-boarding.claims.json`; do not hand-edit. Fix the source and regenerate._

<!-- section:facts -->

## Preconditions

- **Gap:** no prerequisite is specified in the source docs.

## Steps

### Business Center UI path

1. **Action:** Click the eyeball icon for the merchant to view organizational details.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-email:step:2:25c1f5e9`</sub>

2. **Action:** Click the **Send email** drop-down menu. Select either **Test Email** to send a registration email for the organization in the testing environment, or **Production Email** to send a registration for the organization in the production environment.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-email:step:3:f24467e9`</sub>

<!-- sequence_stats: steps=2 outcome_gaps=2 outcome_missing=2 api_ops=0 ui_steps=2 -->

## Constraints

- [ttl_or_validity] The email is valid for 24 hours.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_merchants-v2-email:prose:7ca8aa96ad28`</sub> · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_merchants-v2-email.md.md

## Failure modes

- **Gap:** no error cases documented for this workflow in the source docs.

<!-- /section:facts -->
