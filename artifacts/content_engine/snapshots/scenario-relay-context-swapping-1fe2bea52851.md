# Relay — Context-Swapping Benchmark

**Date:** 2026-07-21
**Purpose:** Test whether AI agents can swap Payment Gateway context between merchants without breaking auth/payment flows.

## Question

Can an agent successfully adapt a Payment Gateway integration when the merchant credentials, business requirements, and API usage patterns change?

## Context

In production, Relay merchants frequently:
- Switch between sandbox and production environments
- Use different payment methods (card, ACH, digital wallet, bank transfer)
- Handle different currencies and tax jurisdictions
- Manage recurring billing, tokenized payments, and 3D Secure flows
- Require PCI compliance, data masking, and audit logging
- Need to handle failed transactions, refunds, and chargebacks

The agent must demonstrate:
1. Understanding of payment method differences
2. Ability to handle currency/tax configuration
3. Knowledge of security requirements
4. Proper error handling for different failure modes

## Expected Behavior

The agent should:
- Read the Payment Gateway REST API spec
- Understand different payment method configurations
- Generate code that handles multiple payment types
- Include proper error handling and retry logic
- Follow security best practices (no hardcoded credentials)

## Scenarios

### Scenario A: Multi-Payment Method Integration
**Task:** Generate code that accepts card, ACH, and digital wallet payments

**Success Criteria:**
- [ ] Agent understands the difference between payment types
- [ ] Agent generates correct model structures for each payment type
- [ ] Agent includes proper error handling for each payment method
- [ ] Agent handles currency conversion correctly

### Scenario B: Currency & Tax Configuration
**Task:** Generate code that handles multi-currency payments with tax calculation

**Success Criteria:**
- [ ] Agent understands currency code requirements
- [ ] Agent includes tax jurisdiction configuration
- [ ] Agent handles decimal precision correctly
- [ ] Agent includes proper validation

### Scenario C: Recurring Billing & Tokenization
**Task:** Generate code for subscription payments with token management

**Success Criteria:**
- [ ] Agent understands token creation flow
- [ ] Agent generates correct subscription model structure
- [ ] Agent handles recurring billing schedule
- [ ] Agent includes proper error handling for failed recurring payments

## Resources

- Payment Gateway REST API spec (via MCP `get_model_class_details`)
- Payment Gateway SDK templates (via MCP `get_code_template`)
- Acceptance Agent Toolkit docs (via MCP)

## Agent Instruction

Read the Payment Gateway documentation via MCP tools. Generate code for a multi-payment method integration that handles card, ACH, and digital wallet payments with proper error handling.
