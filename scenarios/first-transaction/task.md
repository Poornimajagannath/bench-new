# First Transaction — Payment Auth

## Question

Can an agent make its first successful payment authentication with CyberSource?

## Context

The developer needs to:
1. Use the credentials from the authentication scenario
2. Read the CyberSource payment API documentation
3. Make a test payment auth with the test card
4. Get a transaction ID back in the response

## Expected Behavior

The agent should:
- Read the CyberSource developer docs about payments/APIs
- Use the correct auth fields and API endpoint
- Make a payment auth with the test card
- Get a transaction ID back in the response

## Inputs

- CyberSource sandbox credentials (from authentication scenario)
- CyberSource test card (4111111111111111, expiry 12/2031)
- CyberSource sandbox URL
- Payment API documentation

## Success Criteria

- [ ] **PASS**: Agent makes a payment auth that returns a 200-level HTTP response
- [ ] **PASS**: Agent does not throw payment errors (400/422)
- [ ] **PASS**: Agent gets a transaction ID in the response

## Error Categories to Track

- `PAYMENT_MISSING_FIELD` — agent didn't include required fields (e.g., billTo)
- `PAYMENT_INVALID_CARD` — agent used an invalid card number
- `PAYMENT_AUTH_ERROR` — agent's auth failed
- `PAYMENT_WRONG_ENDPOINT` — agent pointed to wrong API endpoint

## Resources

- CyberSource developer portal: `developer.cybersource.com`
- CyberSource llms.txt: `developer.cybersource.com/llms.txt`
- Payment API reference

## Agent Instruction

Read the CyberSource payment documentation. Make a payment authentication with the test card that returns a transaction ID.
