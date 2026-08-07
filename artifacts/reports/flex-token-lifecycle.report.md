# Content Bench V0 Report — `flex-token-lifecycle`

Local proof only. No network. No live credentials.

## 1. What developers were confused about

- TMS createInstrument rejects my Flex JWT when I send it as pan
- entity:Flex
- entity:Microform
- entity:TMS
- entity:createInstrument
- Support said not to treat the JWT like a reusable PAN, but checkout still fails when creating a permanent instrument
- entity:transientTokenJwt
- alt_goal:Resolve developer confusion involving Flex, Microform, TMS, transientTokenJwt
- Is persisting the Flex JWT wrong, and what is the correct permanent instrument path
- alt_goal:how transientTokenJwt but our backend stores it in Redis for later TMS createInstrument. Is persisting the Flex JWT wrong, and what is the correct permanent instrument path?
- Can TMS createInstrument accept a Flex Microform token without sending pan? We keep getting INVALID_DATA when we map transientTokenJwt into card number fields.
- alt_goal:Can TMS createInstrument accept a Flex Microform token without sending pan?
- We thought authorize with the transient token was enough and skipped TMS entirely
- alt_goal:which API creates a reusable instrument identifier?
- Our team mixes Flex Microform JWT handling with TMS instrument CRUD and auth keeps failing
- alt_goal:Resolve developer confusion involving Flex, Microform, TMS
- We authorize immediately with transientTokenJwt and later cannot reuse it
- entity:authorization
- alt_goal:What is the correct lifecycle from Flex Microform capture to permanent TMS instrument before authorization?

## 2. What Content Bench discovered

- can I pass it straight into TMS to store a permanent instrument, or do I need another step?
- stages:capture_transient_token,validate_token_type,create_permanent_instrument,authorize_with_instrument
- fact:Flex Microform returns a short-lived transientTokenJwt
- fact:TMS createInstrument accepts a Flex token via a dedicated transient-token path, not as raw pan
- fact:Transient tokens must not be persisted as long-lived customer credentials

## 3. What the bad answer got wrong

- Treats transientTokenJwt as a reusable PAN and skips TMS persistence
- persists_transient_jwt: expected=False actual=True
- uses_transient_token_path: expected=True actual=False
- calls_tms_create_instrument: expected=True actual=False
- stages_completed contains 'validate_token_type': False

## 4. How the verifier caught it

- failed check `no_persist_transient`
- failed check `uses_flex_to_tms_path`
- failed check `creates_permanent_instrument`
- failed check `stage_order_includes_validate`

## 5. What product surface improves next

- Clarify Flex Token Lifecycle stage ordering in public docs
- Ship a Content CLI workflow verifier for this contract

## Classification

- category: `token-lifecycle-confusion`
- summary: Bad answer for flex-token-lifecycle failed 4 verifier check(s).

## Artifacts

- task pack: `artifacts/task_packs/flex-token-lifecycle.agent_task.json`
- verifier results: `artifacts/verifier_results/flex-token-lifecycle.result.json`

## Content CLI workflow verifier (recommended)

- goal: can I pass it straight into TMS to store a permanent instrument, or do I need another step?
- command: `content workflow verify --id flex-token-lifecycle --fixture local`
- readiness checks:
  - Frozen seeds present under data/seeds/
  - No live credentials exported
  - Local fixture id resolved for workflow
  - Stage ready: capture_transient_token
  - Stage ready: validate_token_type
  - Stage ready: create_permanent_instrument
  - Stage ready: authorize_with_instrument
- recovery path:
  - Re-run discovery to refresh typed candidate
  - Compare agent plan stages against workflow contract stages
  - Apply verifier-private checks to the candidate answer only
  - Emit support-safe evidence without secrets or PAN
