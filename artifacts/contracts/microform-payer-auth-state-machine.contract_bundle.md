# Workflow Contract Bundle — `microform-payer-auth-state-machine`

schema_version: `content.workflow_contract_bundle.v0`

Local proof only. DocETL-style extraction and Harbor/Tempo-style eval export are inspirations — not live upstream integrations.

## 1. What source confusion became this contract?

**Goal:** Sequence Microform tokenization with Payer Authentication enrollment, challenge/frictionless handling, and authorization using the authentication result.

Confusion points:
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

Source seed ids: `seed-mpa-01, seed-mpa-02, seed-mpa-03, seed-mpa-04, seed-mpa-05, seed-mpa-06, seed-mpa-07`

## 2. What did PM approve or edit?

- pm_decision: `edit`
- title: Microform + Payer Auth State Machine
- stages: `microform_tokenize, payer_auth_setup, enrollment_check, challenge_or_frictionless, validate_authentication, authorize_with_auth_result`

API/SDK facts:
- Microform tokenization is not itself a Payer Auth / 3DS completion
- Enrollment may return FRICTIONLESS, CHALLENGE, or UNAVAILABLE paths
- Authorization must carry authentication transaction references when 3DS was performed

## 3. What agent-visible task pack was created?

- task_pack_path: `artifacts/task_packs/microform-payer-auth-state-machine.agent_task.json`
- agent_visible_path: `artifacts/task_packs/microform-payer-auth-state-machine.agent_task.json`
- The agent pack is the public contract surface (instruction, stages, allowed context). It must not include oracle, bad answer, or private checks.

## 4. What hidden truth exists, without showing it?

- hidden_truth_path: `artifacts/task_packs/microform-payer-auth-state-machine.verifier_private.json`
- oracle_present: `true`
- bad_answer_present: `true`
- private_checks_present: `true`
- agent_pack_omits_oracle: `true`
- agent_pack_omits_bad_answer: `true`
- agent_pack_omits_private_checks: `true`
- oracle_field_count: `5`
- bad_answer_field_count: `6`
- private_check_count: `4`
- hidden_truth_sha256: `6b70bcae5256da6cac7754388fc99244c82dad08c6a1e8aae60f19b8383cdddc`

Hidden truth content is intentionally omitted from this bundle.

## 5. How would this map to a future Harbor/Tempo-style eval task?

- preview_only: `true`
- runner_integration: `not implemented`
- environment.mode: `local-simulated`
- test_ref.workflow_id: `microform-payer-auth-state-machine`
- expected_artifact: A structured plan listing each stage, the API/SDK fact it depends on, and the readiness check before moving to the next stage.
- isolation_note: V0 does not run Harbor, tempo-evals, or Docker isolation. This preview documents how a future eval export could package the agent-visible task against verifier-private fixtures.

## 6. What verifier result or product action exists now?

- verifier_result_path: `artifacts/verifier_results/microform-payer-auth-state-machine.result.json`
- improvement_actions:
  - [docs] Clarify Microform + Payer Auth State Machine stage ordering in public docs
  - [content_cli] Ship a Content CLI workflow verifier for this contract
