# Relay Bench V0 Report — `microform-payer-auth-state-machine`

Local proof only. No network. No live credentials.

## 1. What developers were confused about

- We authorize immediately after the Microform token
- entity:Microform
- entity:Payer Authentication
- entity:3DS
- entity:enrollment
- entity:challenge
- entity:authorization
- alt_goal:where does Payer Authentication (3DS) enrollment and challenge fit — and what states must I handle before authorization?
- Payer Authentication enrollment sometimes returns challenge and sometimes frictionless
- Our Microform flow collapses both into one success branch and auth refs are missing on payment
- entity:frictionless
- alt_goal:Resolve developer confusion involving Microform, Payer Authentication, enrollment, challenge
- Do we still need enrollment_check after Microform tokenize if the card network often returns frictionless
- We skip validation_authentication and payments fail intermittently
- alt_goal:Resolve developer confusion involving Microform, frictionless
- Which authentication transaction id must flow from Payer Auth validation into the authorization request after Microform? We only pass the Flex token today.
- entity:Flex
- alt_goal:Which authentication transaction id must flow from Payer Auth validation into the authorization request after Microform?
- Is Microform tokenization itself a completed 3DS / Payer Authentication step? Our checkout treats tokenize as done and never runs challenge_or_frictionless handling.
- alt_goal:Resolve developer confusion involving Microform, Payer Authentication, 3DS
- What is the correct state machine order for Microform then Payer Auth setup, enrollment, challenge, validate, authorize
- alt_goal:What is the correct state machine order for Microform then Payer Auth setup, enrollment, challenge, validate, authorize?
- Without it, enrollment fails and authorization has no authentication references
- alt_goal:Resolve developer confusion involving Microform, enrollment, authorization

## 2. What Relay discovered

- Sequence Microform tokenization with Payer Authentication enrollment, challenge/frictionless handling, and authorization using the authentication result.
- stages:microform_tokenize,payer_auth_setup,enrollment_check,challenge_or_frictionless,validate_authentication,authorize_with_auth_result
- fact:Microform tokenization is not itself a Payer Auth / 3DS completion
- fact:Enrollment may return FRICTIONLESS, CHALLENGE, or UNAVAILABLE paths
- fact:Authorization must carry authentication transaction references when 3DS was performed

## 3. What the bad answer got wrong

- Authorizes immediately after Microform token; skips enrollment/challenge/validation
- runs_enrollment_check: expected=True actual=False
- handles_challenge_and_frictionless: expected=True actual=False
- passes_auth_refs_to_payment: expected=True actual=False
- stages_completed contains_all ['enrollment_check', 'challenge_or_frictionless', 'validate_authentication']: False

## 4. How the verifier caught it

- failed check `enrollment_present`
- failed check `dual_path_handling`
- failed check `auth_refs_on_payment`
- failed check `state_machine_complete`

## 5. What product surface improves next

- Clarify Microform + Payer Auth State Machine stage ordering in public docs
- Ship a Relay CLI workflow verifier for this contract

## Classification

- category: `state-machine-gap`
- summary: Bad answer for microform-payer-auth-state-machine failed 4 verifier check(s).

## Artifacts

- task pack: `artifacts/task_packs/microform-payer-auth-state-machine.agent_task.json`
- verifier results: `artifacts/verifier_results/microform-payer-auth-state-machine.result.json`

## Relay CLI workflow verifier (recommended)

- goal: Sequence Microform tokenization with Payer Authentication enrollment, challenge/frictionless handling, and authorization using the authentication result.
- command: `relay workflow verify --id microform-payer-auth-state-machine --fixture local`
- readiness checks:
  - Frozen seeds present under data/seeds/
  - No live credentials exported
  - Local fixture id resolved for workflow
  - Stage ready: microform_tokenize
  - Stage ready: payer_auth_setup
  - Stage ready: enrollment_check
  - Stage ready: challenge_or_frictionless
  - Stage ready: validate_authentication
  - Stage ready: authorize_with_auth_result
- recovery path:
  - Re-run discovery to refresh typed candidate
  - Compare agent plan stages against workflow contract stages
  - Apply verifier-private checks to the candidate answer only
  - Emit support-safe evidence without secrets or PAN
