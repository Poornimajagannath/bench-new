# Agent Readiness Testing — Benchmark Scenario

**Date:** 2026-07-21
**Purpose:** Test whether AI agents can systematically identify and report DX issues when integrating with payment APIs.

## Question

Can an agent systematically test a payment integration and produce a structured report of DX issues, blockers, and recommendations?

## Context

Agents integrating CyberSource face several categories of DX issues:
- SDK installation problems (version mismatches, missing dependencies)
- Authentication failures (field name mismatches, crypto issues)
- Model structure errors (missing required fields, wrong nested objects)
- Error handling gaps (unclear error responses, missing recovery docs)
- Currency/internationalization issues (wrong ISO codes, locale handling)

The agent must demonstrate:
1. Systematic testing methodology
2. Ability to categorize and prioritize issues
3. Clear documentation of findings
4. Actionable recommendations

## Expected Behavior

The agent should:
- Read the CyberSource documentation
- Test multiple integration scenarios (auth, card payment, currency config)
- Document each finding with severity and bucket
- Produce a structured findings report
- Recommend fixes for each issue

## Scenarios

### Scenario A: Auth Integration Test
**Task:** Test authentication with CyberSource and report all DX issues encountered

**Success Criteria:**
- [ ] Agent correctly identifies SDK installation requirements
- [ ] Agent discovers field name mismatches between docs and SDK
- [ ] Agent documents auth failures with root cause analysis
- [ ] Agent provides severity ratings for each issue

### Scenario B: Multi-Payment Method Test
**Task:** Test card, ACH, and digital wallet integrations and report findings

**Success Criteria:**
- [ ] Agent understands differences between payment methods
- [ ] Agent documents model structure requirements for each type
- [ ] Agent identifies currency handling gaps
- [ ] Agent reports error handling deficiencies

### Scenario C: Currency & Internationalization Test
**Task:** Test multi-currency payment flows and report DX issues

**Success Criteria:**
- [ ] Agent tests at least 3 different currencies
- [ ] Agent identifies locale handling issues
- [ ] Agent documents tax/jurisdiction configuration gaps
- [ ] Agent provides recommendations for internationalization

## Resources

- CyberSource REST API spec (via MCP `get_model_class_details`)
- CyberSource SDK templates (via MCP `get_code_template`)
- Currency/tax configuration docs
- Error handling documentation

## Agent Instruction

Read the CyberSource documentation via MCP tools. Systematically test integration scenarios (auth, payment methods, currency config) and produce a structured DX issue report with severity ratings and recommendations.
