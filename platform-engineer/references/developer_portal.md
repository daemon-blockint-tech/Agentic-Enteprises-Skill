# Developer portal

## Table of contents

1. [Catalog entity](#catalog-entity)
2. [Templates](#templates)
3. [Scorecards](#scorecards)

## Catalog entity

Minimum fields per service:

| Field | Purpose |
|---|---|
| name | Unique ID |
| owner | Team/group |
| tier | Criticality (0–3) |
| lifecycle | experimental / production / deprecated |
| repo | Source link |
| on-call | Pager rotation |
| dependencies | Upstream/downstream systems |

## Templates

- Software Templates create repos + register in catalog
- Parameters validated (naming, region, tier)
- Post-create checklist in PR (first deploy, SLO setup)

## Scorecards

Example checks:

- Unit tests in CI
- SLO defined in monitoring
- Dependency updates < 90 days
- No critical CVEs on default branch

Use scorecards for guidance first; gates only for tier-0/1 when mature.
