# Demo proof — Microform + Payer Auth state machine

Local proof only. No network. No live credentials.

## 1. What developers were confused about

- Microform capture vs Payer Auth state machine
- enrollment → challenge → validation ordering
- which authentication ids must flow into payment authorization
- Treating Microform tokenize as if 3DS were already complete

## 2. What Relay discovered

Goal: Sequence Microform tokenization with Payer Authentication enrollment, challenge/frictionless handling, and authorization using the authentication result.

Stages:

1. `microform_tokenize`
2. `payer_auth_setup`
3. `enrollment_check`
4. `challenge_or_frictionless`
5. `validate_authentication`
6. `authorize_with_auth_result`

## 3. What the bad answer got wrong

- Authorized immediately after Microform token
- Skipped enrollment / challenge / validation
- Did not pass auth refs into payment

## 4. How the verifier caught it

Failed checks (full expected set required):

- `enrollment_present`
- `dual_path_handling`
- `auth_refs_on_payment`
- `state_machine_complete`

## 5. What product surface improves next

- Clarify Microform + Payer Auth stage ordering in public docs
- Ship a Relay CLI workflow verifier for this contract:

```bash
relay workflow verify --id microform-payer-auth-state-machine --fixture local
```

## Artifacts

- Agent-visible: `artifacts/task_packs/microform-payer-auth-state-machine.agent_task.json`
- Verifier-only: `artifacts/task_packs/microform-payer-auth-state-machine.verifier_private.json`
- Generated run report: `artifacts/reports/microform-payer-auth-state-machine.report.md`
