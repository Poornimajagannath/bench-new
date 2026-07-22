# Findings Template

## Run Metadata

| Field | Value |
|-------|-------|
| Run ID | `{run_id}` |
| Scenario | `{scenario}` |
| Agent | `{agent}` |
| SDK Version | `{sdk_version}` |
| Date | `{date}` |
| Environment | `{environment}` |

## Issue Summary

| Category | Count |
|----------|-------|
| High severity | {high_count} |
| Medium severity | {medium_count} |
| Low severity | {low_count} |
| **Total** | {total_count} |

## Detailed Findings

### Finding {N}: {title}

| Property | Value |
|----------|-------|
| Bucket | {bucket} |
| Severity | {severity} |
| Description | {description} |
| Evidence | {evidence} |
| Fix | {fix} |
| Status | {open/closed} |

## Summary by Category

### Authentication
- {summary_of_auth_issues}

### SDK Usage
- {summary_of_sdk_issues}

### Documentation Gaps
- {summary_of_doc_issues}

### Currency/Internationalization
- {summary_of_currency_issues}

### Error Handling
- {summary_of_error_issues}

## Recommendations

1. {recommendation_1}
2. {recommendation_2}
3. {recommendation_3}

## Agent Performance

| Metric | Value |
|--------|-------|
| Docs consulted | {count} |
| Errors encountered | {count} |
| Time to first response | {seconds}s |
| Time to first success | {seconds}s |
| Human interventions | {count} |
| Agent guessing frequency | {low/medium/high} |

## Overall Scorecard

```json
{
  "scenario": "{scenario}",
  "agent": "{agent}",
  "status": "{status}",
  "scores": {
    "integration_success": {score},
    "auth_clarity": {score},
    "sdk_usability": {score},
    "docs_sufficiency": {score},
    "agent_guessing": {score},
    "human_intervention": {score},
    "context_switching": {score},
    "dx_awareness": {score}
  }
}
```
