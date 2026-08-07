# Corpus census

- When: `2026-08-07T06:45:19+00:00`
- Corpus: `data/products/boarding/guides`
- Documents classified: **9**
- Eligible for ingestion: **3**
- Quarantined (policy): **6**

## Counts by kind

| Kind | Count | Share | Quarantined by policy? |
| --- | ---: | ---: | --- |
| API reference (`api_reference`) | 1 | 11.1% | no |
| How-to guide (`how_to_guide`) | 2 | 22.2% | no |
| Release note (`release_note`) | 0 | 0.0% | yes |
| Index / navigation (`index_navigation`) | 6 | 66.7% | yes |
| Legal (`legal`) | 0 | 0.0% | yes |
| Marketing (`marketing`) | 0 | 0.0% | no |
| Other / unclassified (`other`) | 0 | 0.0% | no |

## Policy (exclusions on paper)

Kinds excluded from ingestion by policy:

- `index_navigation` — Index / navigation
- `legal` — Legal
- `release_note` — Release note

_Rationale:_ Pre-ingestion policy: release notes, legal, and index/navigation pages are quarantined so they cannot silently enter the claim pipeline. How-to guides, API reference, and marketing remain eligible until a later policy amendment. Amend this file and re-run pipelines/run_corpus_census.py to change the decision record.

## Sample classifications (first 25)

| Path | Kind | Confidence | Reasons |
| --- | --- | --- | --- |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt.md.md` | api_reference | medium | heading/body indicates field reference |
| `en-us_boarding_developer_all_rest_boarding.md.md` | how_to_guide | medium | long-form product guide shell with audience/purpose framing |
| `en-us_boarding_developer_all_rest_boarding_boarding-intro-overview.md.md` | index_navigation | high | filename looks like intro/index and content is navigation-heavy |
| `en-us_boarding_developer_all_rest_boarding_boarding-intro-template.md.md` | index_navigation | medium | filename looks like intro/index and content is navigation-heavy |
| `en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro.md.md` | index_navigation | high | filename looks like intro/index and content is navigation-heavy |
| `en-us_boarding_developer_all_rest_boarding_boarding-reg-intro.md.md` | index_navigation | medium | filename looks like intro/index and content is navigation-heavy |
| `en-us_boarding_developer_all_rest_boarding_templates-matrix-intro.md.md` | index_navigation | high | filename looks like intro/index and content is navigation-heavy |
| `en-us_boarding_developer_all_rest_boarding_templates-tasks.md.md` | index_navigation | medium | tiny stub without procedural content |
| `en-us_boarding_user_all_ebc_boarding-user.md.md` | how_to_guide | medium | procedural how-to signals in content |
