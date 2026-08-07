# Setup Checkout — Unified Checkout or Flex Microcheckout

## Question

Can an agent configure a checkout integration (Unified Checkout or Flex Microcheckout) and successfully capture a payment?

## Context

The developer needs to:
1. Read the Payment Gateway checkout documentation
2. Understand the checkout setup process (Unified Checkout or Flex Microcheckout)
3. Configure the checkout with the right parameters
4. Make a test transaction that returns a transaction ID

## Expected Behavior

The agent should:
- Read the Payment Gateway developer docs about Unified Checkout or Flex Microcheckout
- Find the checkout configuration parameters
- Configure the checkout with the test card
- Make a test transaction
- Get a transaction ID back in the response

## Inputs

- Payment Gateway sandbox credentials (from authentication scenario)
- Payment Gateway test card (4111111111111111, expiry 12/2031)
- Payment Gateway sandbox URL
- Checkout configuration options (from Payment Gateway docs)

## Success Criteria

- [ ] **PASS**: Agent configures a checkout (Unified Checkout or Flex Microcheckout)
- [ ] **PASS**: Agent makes a test transaction that returns a transaction ID
- [ ] **PASS**: Transaction ID is a valid Payment Gateway format (not an error)

## Error Categories to Track

- `CHECKOUT_MISSING_CONFIG` — agent didn't find the right config parameters
- `CHECKOUT_INVALID_PARAMS` — agent used wrong checkout parameters
- `CHECKOUT_NO_TRANSACTION_ID` — agent got a response but no transaction ID
- `CHECKOUT_AUTH_ERROR` — agent's auth failed during checkout setup

## Resources

- Payment Gateway developer portal: `developer.example.com`
- Payment Gateway llms.txt: `developer.example.com/llms.txt`
- Checkout docs: `developer.example.com/docs/checkout` (or similar)
- Unified Checkout API reference
- Flex Microcheckout API reference

## Agent Instruction

Read the Payment Gateway checkout documentation. Set up either Unified Checkout or Flex Microcheckout with the test card and make a test transaction that returns a transaction ID.
