# SLA and SLO scope and principles

## Table of contents

1. [Definitions](#definitions)
2. [Role boundaries](#role-boundaries)
3. [Service taxonomy and tiers](#service-taxonomy-and-tiers)
4. [Design principles](#design-principles)
5. [Lifecycle](#lifecycle)
6. [Anti-patterns](#anti-patterns)

## Definitions

| Term | Meaning | Typical owner |
|---|---|---|
| **SLI** | Quantitative measure of service behavior (e.g., success ratio, latency percentile) | Service team + SLA/SLO engineer |
| **SLO** | Target range for an SLI over a window (e.g., 99.9% over 30 rolling days) | Service team + SLA/SLO engineer |
| **SLA** | Contractual commitment to a customer with remedies (credits, termination rights) | Legal/sales; engineering defines measurability |
| **Error budget** | Allowed unreliability = `1 - SLO` over the window | Product + engineering policy |
| **Burn rate** | Speed of budget consumption vs steady-state | Alerting policy |

**SLA ≠ SLO.** An SLA is a business/legal artifact; an SLO is an engineering control loop. Never set customer SLA equal to internal SLO without a documented buffer.

## Role boundaries

| Activity | Primary skill | This skill contributes |
|---|---|---|
| Define SLI queries and SLO targets | `sla-slo-engineer` | Owns |
| Wire burn-rate alerts in monitoring | `devops`, `platform-engineer` | Spec; others implement |
| Page during outage, run incident | `site-reliability-engineer`, `incident-management-engineer` | Consumes SLO impact data |
| PRR, chaos, release freeze execution | `site-reliability-engineer` | Supplies budget policy inputs |
| Negotiate credit language | `commercial-counsel` | Supplies measurement feasibility |
| Load test to validate latency SLO | `performance-engineer` | Defines target; PE validates |

Differentiate from `site-reliability-engineer/references/sli_slo_error_budgets.md`: that reference supports **operating** reliability (dashboards, PRR, incident lens). This skill owns **governance**—tiers, customer alignment, review cadence, and publishable SLO specs.

## Service taxonomy and tiers

Define **3–5 tiers** max to avoid analysis paralysis:

| Tier | Examples | Typical availability SLO | Review cadence |
|---|---|---|---|
| **T0** | Auth, payments API, control plane | 99.95–99.99% | Weekly |
| **T1** | Core product APIs, sync paths | 99.9% | Biweekly |
| **T2** | Batch, analytics, internal tools | 99.5% | Monthly |
| **T3** | Best-effort, sandbox | None or 99% | Quarterly |

Document per tier:

- Default latency SLO (if any)—e.g., % requests < 300ms at p99
- Whether **multi-region** or **single-region** SLO applies
- **Maintenance** and **force majeure** handling in SLA vs SLO
- Required **on-call** and **IM** tier (coordinate with `incident-management-engineer`)

## Design principles

1. **User-journey SLIs** — measure what customers experience (success + latency), not CPU.
2. **Fewer, better SLOs** — 2–4 SLOs per service beat twelve correlated metrics.
3. **SLO drives prioritization** — error budget links to release and roadmap decisions.
4. **Buffer below SLA** — internal SLO target ≥ SLA metric + measurement margin (often 0.05–0.1%).
5. **Explicit exclusions** — maintenance, client errors, abuse; document in spec and contract.
6. **Versioned specs** — SLO YAML in repo; changes via PR with reviewer from SRE + product.

## Lifecycle

```
Discover journeys → Select SLIs → Baseline → Set SLO → Policy + alerts → Publish spec
       ↑                                                              ↓
       └──────────── Quarterly review ←── Report burn ←── Operate ────┘
```

| Phase | Activities | Outputs |
|---|---|---|
| **Discover** | Journey map, dependencies, tier assignment | Tier + owner |
| **Measure** | Historical SLI, data quality check | Baseline report |
| **Commit** | Target, window, exclusions, budget policy | SLO spec v1 |
| **Operate** | Dashboards, burn alerts (implemented by DevOps/SRE) | Live metrics |
| **Review** | Trend, incidents, proposed target changes | Review pack |
| **Retire** | Deprecate SLO when service EOL | Archive spec |

## Anti-patterns

| Anti-pattern | Why it fails | Fix |
|---|---|---|
| SLA = SLO on marketing slide | No buffer; credits trigger on noise | Internal SLO stricter; document gap |
| 100% availability target | Unmeasurable; blocks change | Cap at 99.99% or tier-appropriate |
| Infra-only SLIs (disk < 90%) | No user signal | Proxy via journey SLI |
| Alert on every blip | Fatigue; ignores budget | Burn-rate multi-window only |
| SLO without owner | Drift, stale queries | Named service + product owner |
| Annual SLA review only | Targets diverge from reality | Rolling 30d SLO + quarterly governance |
| Copy-paste SLO across tiers | Over- or under-provisioning | Tier defaults with exceptions doc |
