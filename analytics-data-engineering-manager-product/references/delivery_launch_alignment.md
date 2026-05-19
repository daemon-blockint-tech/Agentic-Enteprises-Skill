# Delivery and Launch Alignment

## Analytics definition of done (launch)

| Gate | Owner | Evidence |
|---|---|---|
| Tracking / events in prod | App + PM | Spec signed; QA sample |
| Staging models | Analytics engineer | PR merged; tests pass |
| Mart + grain documented | Analytics engineer | YAML + analyst note |
| Tests green | Analytics engineer | CI + prod monitor |
| BI exposure / dashboard | `bi-analyst` | Linked in exposures.yml |
| Metric reconciliation | PM + finance | Sign-off doc or ticket |
| Runbook for failures | Analytics eng lead | On-call playbook link |

## Milestone timeline (typical)

| Phase | Weeks before GA | Activities |
|---|---|---|
| **Discover** | 8–6 | Metric definitions; event gap analysis |
| **Build** | 6–2 | dbt models; incremental strategy |
| **Harden** | 2–1 | Load test; backfill; shadow metrics |
| **Launch** | 0 | Monitor freshness; war room if Tier-1 |
| **Stabilize** | +1–2 | Fix drift; tech debt ticket |

## Dependency checklist

- [ ] Source pipeline lands before mart schedule
- [ ] PII classification and access roles
- [ ] Feature flag / cohort dimension available in warehouse
- [ ] Rollback plan if mart wrong (disable dashboard, revert model)

## Non-launch work

Still require DoD: tests, docs, owner — but lighter stakeholder sign-off.

## Post-launch

- 7-day **hypercare** for Tier-1 metrics
- Retro: actual vs estimated effort; update estimation guide
