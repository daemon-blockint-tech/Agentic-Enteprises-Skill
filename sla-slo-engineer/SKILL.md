---
name: sla-slo-engineer
description: |
  Guides SLA and SLO engineering—SLI selection and measurement specs, SLO targets and error budgets,
  multi-window burn-rate alerting policies, customer-facing SLA vs internal SLO alignment,
  criticality tiering, reporting and review cadences, and capacity implications of service levels.
  Use when defining SLIs, setting SLO targets, designing error-budget policy, burn-rate alerts,
  availability or latency SLOs, SLO reviews, or documenting SLO specs for engineering—not on-call or
  incident command (site-reliability-engineer, incident-management-engineer), contractual legal
  SLA negotiation (commercial-counsel), full observability stack implementation (platform-engineer,
  devops), or application performance tuning only (performance-engineer).
  Triggers: SLA, SLO, SLI, service level objective, error budget, burn rate alert, availability
  target, latency SLO, define SLOs, SLO review, customer SLA.
---

# SLA & SLO Engineer

## When to Use

- Select **SLIs** and document measurement queries, exclusions, and data sources
- Set **SLO targets**, rolling windows, and per-journey or per-tier policies
- Define **error-budget** math, consumption tracking, and policy actions (freeze, focus)
- Design **multi-window burn-rate** alert policies and severity routing
- Align **customer-facing SLAs** with internal SLOs (credits, measurements, carve-outs)
- Tier services by **criticality** and map tiers to targets and review cadence
- Run **SLO review** meetings, executive summaries, and quarterly governance
- Estimate **capacity headroom** implied by latency or availability targets
- Publish **SLO specs** for engineering (YAML/JSON schema, dashboard contracts)

## When NOT to Use

- Lead outage mitigation, paging, or on-call rotations → `site-reliability-engineer`, `incident-management-engineer`
- Negotiate contract language, credits, or legal remedies → `commercial-counsel`
- Build metrics/log/trace pipelines, collectors, or alertmanager config → `devops`, `platform-engineer`
- Profile application code, load-test, or tune queries only → `performance-engineer`
- Run production readiness reviews, chaos games, or release cutover → `site-reliability-engineer`, `deployment-strategist`
- Coordinate multi-team program milestones without SLO scope → `technical-program-manager`

## Related skills

| Need | Skill |
|---|---|
| SRE execution: PRR, incident mitigation, chaos, release gates | `site-reliability-engineer` |
| Incident program, SEV, on-call, postmortems | `incident-management-engineer` |
| CI/CD pipelines, DORA, deploy gates wired to SLO policy | `ci-cd-engineer` |
| Delivery infra, GitOps, alert stack implementation | `devops` |
| IDP golden paths, platform SLOs for portal/scaffold | `platform-engineer` |
| Load testing and latency profiling | `performance-engineer` |
| Rollout strategy and change tiers | `deployment-strategist` |
| Cross-team launch and RAID | `technical-program-manager` |
| Contractual SLA terms and redlines | `commercial-counsel` |
| Data pipeline freshness or warehouse SLAs | `data-system-ops-lead` |

## Core Workflows

### 1. Scope and principles

Service-level taxonomy, user-centric measurement, boundaries with SRE and legal.

**See `references/sla_slo_scope_and_principles.md`.**

### 2. SLI selection and measurement

Choose SLIs, define queries, exclusions, and validation.

**See `references/sli_selection_and_measurement.md`.**

### 3. SLO targeting and error budgets

Targets, windows, budget math, and policy actions.

**See `references/slo_targeting_and_error_budgets.md`.**

### 4. Alerting, burn rates, and policies

Multi-window alerts, routing, and noise control.

**See `references/alerting_burn_rates_and_policies.md`.**

### 5. Customer SLA vs internal SLO

Contract alignment, credits, carve-outs, and communication.

**See `references/customer_sla_vs_internal_slo.md`.**

### 6. Reporting, review, and governance

Cadences, dashboards, specs, and executive reporting.

**See `references/reporting_review_and_governance.md`.**

## Outputs

- **SLO specification** — SLI definition, query, target, window, exclusions, owners, tier
- **Error-budget policy** — thresholds, actions, escalation, link to release policy
- **Burn-rate alert policy** — windows, multipliers, severity, runbook links
- **SLA/SLO alignment matrix** — customer metric ↔ internal SLI, measurement gaps, carve-outs
- **Tier catalog** — criticality definitions with default targets and review cadence
- **SLO review pack** — budget consumed, trends, top burners, proposed target changes
- **Capacity note** — headroom vs latency/availability target (when in scope)

## Principles

- **Measure user outcomes** — availability and latency of journeys, not vanity infra metrics
- **Internal SLO stricter than external SLA** — buffer for measurement lag and goodwill
- **Policy before panic** — error-budget actions agreed before budget exhaustion
- **Alerts prove SLO risk** — every page ties to budget burn or imminent breach
- **Govern with data** — reviews change targets from evidence, not anecdotes
- **Hand off execution** — SRE and IM own incident response; this skill owns the level definitions

## When to load references

- **Scope and taxonomy** → `references/sla_slo_scope_and_principles.md`
- **SLI design** → `references/sli_selection_and_measurement.md`
- **Targets and budgets** → `references/slo_targeting_and_error_budgets.md`
- **Burn alerts** → `references/alerting_burn_rates_and_policies.md`
- **Customer SLA** → `references/customer_sla_vs_internal_slo.md`
- **Reviews and governance** → `references/reporting_review_and_governance.md`
