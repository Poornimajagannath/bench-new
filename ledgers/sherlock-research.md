---
slug: ledgers/sherlock-research
title: Sherlock Research Ledger
type: ledger
---

# Sherlock Research Ledger

## Format
```
## [YYYY-MM-DD]
- **Question:** [What was researched]
- **Sources:** [Where data came from]
- **Findings:** [Key results]
- **Confidence:** [High / Medium / Low]
- **Tags:** [#relevant-tags]
```

## 2026-07-25
- **Question:** What are the right architecture patterns for multi-persona AI agents?
- **Sources:** gumclaw.github.io/how-i-work/, Hermes docs, GBrain research
- **Findings:** Single runtime with persona skills beats multi-agent fleet. GBrain as shared ledger. Three-tier permissions. Mistakes become rules via policy files.
- **Confidence:** High
- **Tags:** #architecture, #personas, #gumclaw, #lessons-learned

- **Question:** How does Gumclaw's skill system work?
- **Sources:** gumclaw.github.io/how-i-work/skills.html, gumclaw.github.io/how-i-work/guardrails.html
- **Findings:** ~40 skill packs, ~100 scripts. Skills = playbooks, not plugins. Lessons logged to files, not memory. Script library grows from repeated tasks.
- **Confidence:** High
- **Tags:** #gumclaw, #skills, #scripts, #patterns
