# Roadmap and Prioritization

## Backlog structure

Each item should state:

| Field | Example |
|---|---|
| **Outcome** | Reduce time-to-insight for activation funnel |
| **Deliverable** | `fct_activation_events` + exposure to activation dashboard |
| **Domain** | Growth product |
| **Launch tie** | Feature flag GA 2026-Q3 |
| **Dependencies** | App event `signup_completed` in tracking plan |

## Prioritization lenses

| Lens | Question |
|---|---|
| **Revenue / retention** | Does this metric drive a core product bet? |
| **Launch blocker** | Is GA blocked without this mart? |
| **Risk** | Wrong metric in production today? |
| **Cost of delay** | Compliance or exec reporting deadline? |
| **Effort** | T-shirt; include test and backfill cost |

Use weighted score (e.g. RICE) **within** analytics backlog; PM owns product rank, manager owns **analytics capacity** fit.

## Roadmap horizons

| Horizon | Content |
|---|---|
| **Now (0–6 wk)** | Committed marts for current sprint/launch |
| **Next** | Sized, dependencies identified |
| **Later** | Themes (e.g. unified subscription grain) |

## Capacity rules

- Reserve **20–30%** for quality debt, incidents, and platform upgrades
- Cap **parallel launches** per engineer (often 1 major + 1 minor)
- Freeze risky full-refreshes during peak launch windows

## Escalation to leadership

Escalate when:

- Two squads need conflicting grain on same entity
- Launch date immovable but upstream schema not ready
- Headcount insufficient for committed OKRs

Bring **options** (cut scope, delay launch analytics, interim manual report).
