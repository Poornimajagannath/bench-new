# Quarantine list — excluded from ingestion by policy

- When: `2026-08-07T06:45:19+00:00`
- Corpus: `data/products/boarding/guides`
- Excluded kinds: `index_navigation`, `legal`, `release_note`
- Quarantined docs: **6** of 9

This list is the decision record. Ingestion must not pull these paths
unless policy is amended and the census re-run.

| # | Kind | Path | Title | Reasons |
| ---: | --- | --- | --- | --- |
| 1 | `index_navigation` | `en-us_boarding_developer_all_rest_boarding_boarding-intro-overview.md.md` | Introduction to the Boarding Registration Service | filename looks like intro/index and content is navigation-heavy |
| 2 | `index_navigation` | `en-us_boarding_developer_all_rest_boarding_boarding-intro-template.md.md` | Product Templates | filename looks like intro/index and content is navigation-heavy |
| 3 | `index_navigation` | `en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro.md.md` | Manage Organizations | filename looks like intro/index and content is navigation-heavy |
| 4 | `index_navigation` | `en-us_boarding_developer_all_rest_boarding_boarding-reg-intro.md.md` | Create Organizations | filename looks like intro/index and content is navigation-heavy |
| 5 | `index_navigation` | `en-us_boarding_developer_all_rest_boarding_templates-matrix-intro.md.md` | Product Boarding Template Reference | filename looks like intro/index and content is navigation-heavy |
| 6 | `index_navigation` | `en-us_boarding_developer_all_rest_boarding_templates-tasks.md.md` | Using Templates | tiny stub without procedural content |
