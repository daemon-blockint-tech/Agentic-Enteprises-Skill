# Operating model

## Table of contents

1. [Capability map](#capability-map)
2. [Process and RACI](#process-and-raci)
3. [Governance](#governance)
4. [Change impact](#change-impact)

## Capability map

List **business capabilities** (what the org must do), not org chart titles:

| Capability | Maturity (1–5) | Owner | Gap vs target |
|---|---|---|---|
| e.g. Lead-to-cash | 3 | Sales Ops | Quote automation |

Prioritize gaps that block strategic metrics.

## Process and RACI

For each critical process (5–7 max in exec view):

```markdown
## Process: [Name]
Trigger → Steps → Output

| Step | R | A | C | I |
|---|---|---|---|---|
```

- **R** does the work; **A** approves; **C** consulted; **I** informed
- One **A** per step; avoid everyone as C

Deep swimlanes and system touchpoints → `business-analyst`.

## Governance

| Forum | Cadence | Purpose | Inputs | Decisions |
|---|---|---|---|---|
| SteerCo | Monthly | Phase gates | Status, risks | Go / pivot / stop |
| Ops review | Weekly | Execution | KPIs | Priorities |

Define **decision rights** (who can commit budget, change scope, accept risk).

## Change impact

| Stakeholder group | Impact | Resistance risk | Actions |
|---|---|---|---|
| Sales | New CRM workflow | High | Champions, training |

Link technology changes to `senior-system-architecture` for build vs buy and integration.

Program timeline and RAID → `technical-program-manager`.
