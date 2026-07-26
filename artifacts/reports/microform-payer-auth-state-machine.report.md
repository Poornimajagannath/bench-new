# Relay Bench V0 Report — `microform-payer-auth-state-machine`

Local proof only. No network. No live credentials.

## 1. What developers were confused about

- Right now we authorize immediately after the Microform token and sometimes miss the authentication transaction id
- entity:Microform
- entity:Payer Authentication
- entity:3DS
- entity:enrollment
- entity:challenge
- entity:authorization

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
- Ship a VAP CLI workflow verifier for this contract

## Classification

- category: `state-machine-gap`
- summary: Bad answer for microform-payer-auth-state-machine failed 4 verifier check(s).

## Artifacts

- task pack: `artifacts/task_packs/microform-payer-auth-state-machine.task_pack.json`
- verifier results: `artifacts/verifier_results/microform-payer-auth-state-machine.result.json`

## VAP CLI workflow verifier (recommended)

- goal: Sequence Microform tokenization with Payer Authentication enrollment, challenge/frictionless handling, and authorization using the authentication result.
- command: `vap workflow verify --id microform-payer-auth-state-machine --fixture local`
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

