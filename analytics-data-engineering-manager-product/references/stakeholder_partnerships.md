# Stakeholder Partnerships

## Product management

| You provide | You need from PM |
|---|---|
| Realistic analytics timelines | Prioritized outcomes, launch dates |
| Trade-off options | Clear MVP vs full metric scope |
| Metric impact when schema slips | Early tracking plan involvement |

**Forum:** Weekly domain sync; shared backlog view (Jira/Linear).

## Product analytics / experimentation

- Align on **event taxonomy** and experiment assignment tables
- Avoid duplicate experiment logic in marts and BI layer
- Escalate conflicting definitions to single **metric council** if needed

## Finance and operations

- Revenue and billing metrics need **written definitions** before mart GA
- Route disputes through `business-analyst` + finance owner

## Legal and privacy

- PII columns tagged; role-based access before broad self-serve
- Involve early for new data sources (mobile, ads, third party)

## Data architect and data manager

| Topic | Skill |
|---|---|
| New conformed dimension | `data-architect` |
| Org-wide SLA / incident process | `data-manager` |
| Squad-level delivery | This skill |

## Communication templates

**Status (weekly):** shipped / in progress / blocked / decisions needed

**Escalation:** problem → impact → options → recommendation → decision maker

## Anti-patterns

- Committing to launch metrics without app eng on tracking plan
- Letting PM define SQL grain without analytics eng review
- Skipping finance sign-off on revenue-facing marts
