# Setup Checkout — Unified Checkout or Flex Microcheckout

## Question

Can an agent configure a checkout integration (Unified Checkout or Flex Microcheckout) and successfully capture a payment?

## Context

The developer needs to:
1. Read the CyberSource checkout documentation
2. Understand the checkout setup process (Unified Checkout or Flex Microcheckout)
3. Configure the checkout with the right parameters
4. Make a test transaction that returns a transaction ID

## Expected Behavior

The agent should:
- Read the CyberSource developer docs about Unified Checkout or Flex Microcheckout
- Find the checkout configuration parameters
- Configure the checkout with the test card
- Make a test transaction
- Get a transaction ID back in the response

## Inputs

- CyberSource sandbox credentials (from authentication scenario)
- CyberSource test card (4111111111111111, expiry 12/2031)
- CyberSource sandbox URL
- Checkout configuration options (from CyberSource docs)

## Success Criteria

- [ ] **PASS**: Agent configures a checkout (Unified Checkout or Flex Microcheckout)
- [ ] **PASS**: Agent makes a test transaction that returns a transaction ID
- [ ] **PASS**: Transaction ID is a valid CyberSource format (not an error)

## Error Categories to Track

- `CHECKOUT_MISSING_CONFIG` — agent didn't find the right config parameters
- `CHECKOUT_INVALID_PARAMS` — agent used wrong checkout parameters
- `CHECKOUT_NO_TRANSACTION_ID` — agent got a response but no transaction ID
- `CHECKOUT_AUTH_ERROR` — agent's auth failed during checkout setup

## Resources

- CyberSource developer portal: `developer.cybersource.com`
- CyberSource llms.txt: `developer.cybersource.com/llms.txt`
- Checkout docs: `developer.cybersource.com/docs/checkout` (or similar)
- Unified Checkout API reference
- Flex Microcheckout API reference

## Agent Instruction

Read the CyberSource checkout documentation. Set up either Unified Checkout or Flex Microcheckout with the test card and make a test transaction that returns a transaction ID.
