# Ingestion report

Milestone 0.5: corpus cleaned at the door. `raw/` is immutable evidence; serve layers read only `normalized/` and `content/`.

- Stamp date: `2026-08-07-boarding`
- Docs fetched into raw: 3
- Claims extracted: 645
- Raw dir: `raw/2026-08-07-boarding`
- Normalized file: `normalized/2026-08-07-boarding.claims.json`
- Read contract: normalized/, content/
- Forbidden: raw/

## Claims by schema

| Schema | Count |
| --- | ---: |
| quickstart_step | 550 |
| endpoint_fact | 0 |
| error_case | 34 |
| prose_claim | 61 |

## Drop log

| Path | Reason | Detail |
| --- | --- | --- |
| en-us_boarding_developer_all_rest_boarding_boarding-intro-overview.md.md | quarantine_policy | excluded by corpus census quarantine list |
| en-us_boarding_developer_all_rest_boarding_boarding-intro-template.md.md | quarantine_policy | excluded by corpus census quarantine list |
| en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro.md.md | quarantine_policy | excluded by corpus census quarantine list |
| en-us_boarding_developer_all_rest_boarding_boarding-reg-intro.md.md | quarantine_policy | excluded by corpus census quarantine list |
| en-us_boarding_developer_all_rest_boarding_templates-matrix-intro.md.md | quarantine_policy | excluded by corpus census quarantine list |
| en-us_boarding_developer_all_rest_boarding_templates-tasks.md.md | quarantine_policy | excluded by corpus census quarantine list |
