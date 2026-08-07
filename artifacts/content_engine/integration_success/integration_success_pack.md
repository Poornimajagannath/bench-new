# Integration Success Pack (V0)

**Product:** Integration Success OS

A developer can integrate our API in a single session, with clear steps, working references, and a go-live checklist.

Local proof only. No live sandbox calls.

## Guided quickstart steps

1. Tokenize with Microform
2. Run Payer Auth setup
3. Check enrollment
4. Handle challenge or frictionless
5. Validate authentication
6. Authorize with authentication references

## API reference operations

- `createCredit`
- `createPayment`
- `getPayment`
- `capturePayment`
- `createMppCredentialSetup`
- `checkMppEnrollment`
- `createCustomer`
- `getCustomer`

## Go-live checklist

- [ ] **Load sandbox auth from environment variables** — Use PGW_MERCHANT_ID / PGW_KEY_ID / PGW_SHARED_SECRET; never hardcode.
- [ ] **Complete first successful sandbox API call** — Primary ops available: createCredit, createPayment, getPayment, capturePayment
- [ ] **Do not treat Microform tokenize as completed 3DS** — Run enrollment and challenge/frictionless handling before authorization.
- [ ] **Handle auth and validation errors without leaking secrets** — Use generated error eval seeds; keep evidence support-safe.
- [ ] **Switch to production only after sandbox checklist passes** — V0 does not call production. Keep PGW_ENVIRONMENT=sandbox until ready.

## Lineage

- quickstart units: `artifacts/content_engine/objects/microform-payer-auth-quickstart.quickstart_units.json`
- api reference units: `artifacts/content_engine/generated/payments-core-openapi.api_reference_units.json`
- eval seeds: `artifacts/content_engine/generated/payments-core-openapi.eval_seeds.json`
- workflow contract: `artifacts/contracts/microform-payer-auth-state-machine.contract_bundle.json`

## Honesty

- docetl: `style-only-upstream`
- tempo/harbor: `eval-seeds-only`
- network: `denied`
