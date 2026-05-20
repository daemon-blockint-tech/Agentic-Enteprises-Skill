# Alerting, burn rates, and policies

## Table of contents

1. [Alert philosophy](#alert-philosophy)
2. [Multi-window burn rates](#multi-window-burn-rates)
3. [Google SRE multipliers](#google-sre-multipliers)
4. [Severity routing](#severity-routing)
5. [Noise control](#noise-control)
6. [Policy document template](#policy-document-template)
7. [Handoff to implementation](#handoff-to-implementation)

## Alert philosophy

**Page on budget risk, not on symptoms alone.**

| Alert type | Purpose |
|---|---|
| **Fast burn** | Detect imminent SLO breach (hours) |
| **Slow burn** | Detect gradual erosion (days) |
| **Exhausted budget** | Trigger policy actions |
| **SLA early warning** | Internal buffer before customer SLA breach |

Symptom alerts (CPU, single 500 spike) support debugging; they do not replace burn alerts for SLO governance.

## Multi-window burn rates

Burn rate = how fast error budget is consumed **relative to steady consumption** for the window.

```
steady_burn = error_budget / window_length
actual_burn = budget_consumed_in_short_window / short_window_length
burn_rate = actual_burn / steady_burn
```

Example: 99.9% monthly budget → 0.1% bad allowed. If 0.1% bad occurs in 1 hour, burn rate ≈ 720× for that hour (illustrative—use your recording rules).

## Google SRE multipliers

For **99.9%** availability over **30d** (error budget 0.001):

| Window | Burn rate multiplier | Budget consumed in window | Typical severity |
|---|---|---|---|
| 1h | 14.4× | ~2% of monthly | Page |
| 6h | 6× | ~5% | Page |
| 3d | 1× | ~10% | Ticket |
| 30d | 1× | 100% at steady | Review meeting |

For **99.95%** (budget 0.0005), scale multipliers proportionally or recompute from budget math.

**Latency SLOs:** apply same structure on `(1 - latency_sli)` as error rate.

Document org-specific tuning when alert noise > 2 false pages per quarter.

## Severity routing

| Severity | Criteria | Route |
|---|---|---|
| **P1 / Page** | Fast burn alert firing | On-call per `incident-management-engineer` |
| **P2 / Urgent ticket** | Slow burn, no user flood | Service team queue |
| **P3 / Review** | 30d trend ticket | SLO review backlog |
| **Policy** | Budget >80% | Automated freeze signal to release tooling |

Every page includes:

- Service, SLO name, window, current burn %
- Link to **SLO dashboard** and **runbook** (runbook authored by SRE)
- Recent deploys and dependency status

## Noise control

| Technique | Detail |
|---|---|
| Minimum incident duration | Ignore blips < N minutes if policy allows |
| Maintenance suppression | Silence burn alerts in declared windows |
| Dependency dedup | One page for upstream if multiple services burn |
| Alert budget | Team reviews pages/SLO/quarter |
| Burn-only paging | Disable legacy threshold pages when burn live |

**False positive review:** monthly with on-call + SLA/SLO engineer; adjust multipliers, not SLO target, first.

## Policy document template

```yaml
alert_policy:
  service: checkout-api
  slo: availability
  objective: 0.999
  windows:
    - length: 1h
      burn_multiplier: 14.4
      severity: page
      route: pagerduty-checkout
    - length: 6h
      burn_multiplier: 6
      severity: page
      route: pagerduty-checkout
    - length: 3d
      burn_multiplier: 1
      severity: ticket
      route: jira-reliability
    - length: 30d
      burn_multiplier: 1
      severity: review
      route: slo-review-queue
  maintenance:
    suppress: true
    require_ticket: true
  runbook_url: https://wiki.example/runbooks/checkout-availability
```

Store alongside SLO spec; version in Git.

## Handoff to implementation

| Task | Owner skill |
|---|---|
| Recording rules, alert rules, routes | `devops` |
| Dashboards in portal | `platform-engineer` |
| Runbook content, incident playbooks | `site-reliability-engineer` |
| PagerDuty/Opsgenie routing | `incident-management-engineer` |

This skill delivers **policy YAML + acceptance tests** (e.g., simulate burn in staging). SRE validates paging during game day.
