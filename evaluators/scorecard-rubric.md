# Scorecard Rubric

## Six Score Categories (0-3 each)

### 1. integration_success
**What it measures:** Did the agent complete the integration successfully?

| Score | Meaning |
|-------|---------|
| 3 | Full success — API calls succeed, expected response received |
| 2 | Partial success — core integration works but some edge cases fail |
| 1 | Minimal — agent got a response but integration is incomplete |
| 0 | Failed — no successful integration achieved |

### 2. auth_clarity
**What it measures:** Were authentication instructions clear and correct?

| Score | Meaning |
|-------|---------|
| 3 | Auth worked on first try, docs were clear and correct |
| 2 | Auth required 1-2 retries, minor doc gaps |
| 1 | Auth took many retries, significant doc gaps |
| 0 | Auth was completely unclear or incorrect |

### 3. sdk_usability
**What it measures:** How easy was it to use the SDK?

| Score | Meaning |
|-------|---------|
| 3 | SDK was intuitive, well-documented, no surprises |
| 2 | SDK had minor quirks but was usable |
| 1 | SDK had significant quirks or undocumented behavior |
| 0 | SDK was unusable or completely undocumented |

### 4. docs_sufficiency
**What it measures:** Did the documentation provide all necessary information?

| Score | Meaning |
|-------|---------|
| 3 | Docs covered everything needed to complete the task |
| 2 | Docs had minor gaps but agent could infer missing info |
| 1 | Docs had significant gaps requiring trial/error |
| 0 | Docs were missing critical information |

### 5. agent_guessing
**What it measures:** How much did the agent have to guess vs follow docs?

| Score | Meaning |
|-------|---------|
| 3 | Agent followed docs precisely, no guessing needed |
| 2 | Agent made minor inferences beyond docs |
| 1 | Agent guessed frequently, docs were ambiguous |
| 0 | Agent had to guess almost everything |

### 6. human_intervention
**What it measures:** How much human intervention was required?

| Score | Meaning |
|-------|---------|
| 3 | No human intervention needed |
| 2 | Minimal human intervention (1-2 minor fixes) |
| 1 | Significant human intervention (3+ fixes or major guidance) |
| 0 | Human had to intervene heavily or the agent failed entirely |

### 7. context_switching
**What it measures:** How well did the agent adapt when merchant requirements changed?

| Score | Meaning |
|-------|---------|
| 3 | Agent seamlessly adapted to new payment methods/currencies |
| 2 | Agent adapted with minor corrections |
| 1 | Agent struggled to adapt, required significant rework |
| 0 | Agent failed to adapt to changed requirements |

### 8. dx_awareness
**What it measures:** How well did the agent identify and document DX issues?

| Score | Meaning |
|-------|---------|
| 3 | Agent identified all major issues with severity ratings |
| 2 | Agent identified most issues, some missed |
| 1 | Agent missed several issues, no severity ratings |
| 0 | Agent didn't identify or report any issues |

## Overall Assessment

- **Status:** "success" if integration_success ≥ 2 and human_intervention ≤ 1 and context_switching ≥ 2
- **Status:** "partial" if integration_success = 1 or human_intervention = 2 or context_switching = 1
- **Status:** "failed" if integration_success = 0 or human_intervention = 3 or context_switching = 0
