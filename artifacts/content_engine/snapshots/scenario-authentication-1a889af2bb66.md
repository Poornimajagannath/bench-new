# Authentication — First API Call

## Question

Can an agent figure out how to authenticate with the CyberSource API and make its first successful call?

## Context

The developer needs to:
1. Understand where to get API credentials from the CyberSource developer portal
2. Use the correct credential format (not what docs claim — the SDK field names are different from what the docs say)
3. Make a successful API call with the test card

## Expected Behavior

The agent should:
- Read the CyberSource developer docs
- Find the authentication/credentials section
- Use the correct field names (`merchantKeyId`, `merchantsecretKey` — NOT `keyId`, `secretKey`)
- Make an API call with the sandbox test card
- Get a valid auth response (not an error)

## Inputs

- CyberSource sandbox credentials (set via env vars: `CYBS_MERCHANT_ID`, `CYBS_KEY_ID`, `CYBS_SHARED_SECRET`)
- CyberSource test card number (standard test card, e.g., 4111111111111111)
- CyberSource sandbox URL

## Success Criteria

- [ ] Agent successfully authenticates (no auth errors)
- [ ] Agent makes a valid API call that returns a response (not an error)
- [ ] Agent uses the correct credential field names (not what the docs claim)

## Error Categories to Track

- `AUTH_MISSING_CREDENTIALS` — agent didn't find or use credentials
- `AUTH_WRONG_FIELD_NAMES` — agent used `keyId`/`secretKey` instead of `merchantKeyId`/`merchantsecretKey`
- `AUTH_INVALID_MERCHANT_ID` — agent found wrong merchant ID
- `AUTH_NETWORK_ERROR` — agent pointed to wrong API endpoint

## Resources

- CyberSource developer portal: `developer.cybersource.com`
- CyberSource llms.txt: `developer.cybersource.com/llms.txt`
- CyberSource API reference (for auth endpoints)

## Agent Instruction

Read the CyberSource developer documentation and find the authentication section. Get the right credentials and make a successful API call with the sandbox test card.
