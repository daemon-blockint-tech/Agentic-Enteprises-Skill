# Team and Org Design

## Operating models

| Model | Pros | Cons |
|---|---|---|
| **Embedded in product squads** | Fast launches; domain context | Fragmented standards; duplicate dims |
| **Central analytics eng + embed rotation** | Consistent dbt patterns | Handoff friction |
| **Hub-and-spoke** | Platform standards + domain pods | Needs strong platform lead |

Default for product-heavy companies: **hub-and-spoke** with shared dbt repo and domain owners.

## Roles on the team

| Role | Focus |
|---|---|
| **Analytics engineer** | Marts, tests, docs — see `analytics-data-engineer` |
| **Analytics eng lead** | Standards, reviews, hardest domains |
| **BI analyst** (partner) | Dashboards, self-serve — `bi-analyst` |
| **Data platform DE** (partner) | Ingestion, warehouse SLOs — `data-warehouse-engineer` |

Clarify **who owns metric definition** (often PM + finance + analytics eng).

## Interfaces

| Partner | Cadence | Topic |
|---|---|---|
| Product management | Weekly domain sync | Roadmap, launches |
| App engineering | Bi-weekly | Event/schema contracts |
| Data platform | Weekly | Pipelines, incidents |
| Data architect | Monthly | Conformed dimensions, ADRs |

## Sizing heuristics

- 1 analytics engineer per 1–2 active product squads (mature marts lower need)
- Add **platform/analytics lead** when repo >30 contributors or test debt spikes

## Anti-patterns

- Analysts maintaining production dbt without engineering standards
- Each squad forks its own warehouse schema without architect review
- Manager doing IC work on critical path every sprint
