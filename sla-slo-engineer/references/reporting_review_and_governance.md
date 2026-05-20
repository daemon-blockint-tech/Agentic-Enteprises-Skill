# Reporting, review, and governance

## Table of contents

1. [Reporting layers](#reporting-layers)
2. [SLO review meeting](#slo-review-meeting)
3. [Executive summary](#executive-summary)
4. [Governance forum](#governance-forum)
5. [Target change process](#target-change-process)
6. [Metrics for the program](#metrics-for-the-program)
7. [Integration with TPM and SRE](#integration-with-tpm-and-sre)

## Reporting layers

| Layer | Audience | Contents | Cadence |
|---|---|---|---|
| **Operational** | Service team | SLI, burn, top errors, deploys | Daily dashboard |
| **Tactical** | Eng + product leads | Budget %, policy state, backlog | Weekly |
| **Strategic** | Directors / VP | Tier-0 trends, SLA risk, investments | Monthly |
| **Contract** | Finance, legal, CS | SLA compliance vs buffer | Monthly/quarterly |

Automate operational and tactical from SLO spec queries; minimize manual spreadsheets.

## SLO review meeting

**Attendees:** service owner, product owner, SRE partner, optional SLA/SLO engineer facilitator.

**Agenda (45–60 min):**

1. **SLI snapshot** — current vs objective, 30d trend
2. **Budget consumed** — % and policy tier
3. **Incidents** — budget attribution (facts from IM/SRE)
4. **Deploy correlation** — releases since last review
5. **Top burners** — routes, regions, dependencies
6. **Actions** — reliability backlog, target change proposals
7. **Decisions** — freeze lift, target change PR, capacity ask

**Outputs:** decision log, Jira/Linear items, updated spec PR if targets change.

### Review pack template

```markdown
# SLO Review — {service} — {date}

## Summary
- Tier: T0 | Budget consumed: 62% | Policy: freeze risky launches

## SLOs
| SLO | Objective | Current (30d) | Burn % | Trend |
|-----|-----------|---------------|--------|-------|
| availability | 99.95% | 99.97% | 40% | stable |
| latency | 99% <300ms | 98.2% | 80% | degrading |

## Incidents (budget impact)
- INC-1234: 12 min availability burn — root cause: DB failover

## Proposed changes
- [ ] Tighten pool timeouts (reliability backlog #456)
- [ ] Propose latency objective 98.5% → 99% after Q3 capacity

## Decisions
- Maintain release freeze until latency burn <50%
```

## Executive summary

One page maximum:

- **Red / yellow / green** per T0/T1 service by budget consumed
- **Customer SLA risk** — any service within buffer margin of contract breach
- **Investment asks** — capacity, staffing, dependency upgrades
- **Wins** — targets met after reliability work

Avoid raw metric dumps; link to dashboards.

## Governance forum

Quarterly **SLO council** (optional at scale):

| Role | Responsibility |
|---|---|
| SLA/SLO engineer chair | Standards, tier definitions, template updates |
| SRE representative | Operational feasibility, handoff to `site-reliability-engineer` |
| Product council rep | Tradeoffs vs roadmap |
| Platform rep | Instrumentation standards |
| TPM | Cross-service dependencies, `technical-program-manager` |

**Decisions:**

- Tier promotion/demotion
- Org-wide burn multiplier defaults
- New mandatory spec fields
- Exception registry for relaxed targets

## Target change process

```
Proposal (data) → Peer review (SRE) → Product sign-off → Legal if SLA-bound
       → PR to slo-spec repo → Announce in review → Effective date
```

| Change type | Approvers |
|---|---|
| Stricter SLO | Service owner + SRE |
| Relaxed SLO | + Product director |
| SLA-impacting | + `commercial-counsel` |
| Tier change | SLO council |

**Effective date:** next rolling window start unless emergency safety issue.

## Metrics for the program

Measure the **SLO program**, not only services:

| Metric | Why |
|---|---|
| % tier-0 services with current spec | Coverage |
| % SLOs with burn alerts configured | Operability |
| Mean time to update spec after tier change | Governance hygiene |
| False page rate per SLO | Alert quality |
| Incidents with budget attribution completed | Learning loop |
| SLA breaches vs internal buffer consumed | Alignment health |

## Integration with TPM and SRE

| Need | Skill | Interaction |
|---|---|---|
| Launch readiness with SLO sign-off | `technical-program-manager` | TPM gates include spec link |
| Incident-driven reliability work | `site-reliability-engineer` | SRE executes; this skill updates targets/policy |
| Pipeline freeze on burn | `ci-cd-engineer` | Wire policy thresholds to deploy gates |
| Data SLA reviews | `data-system-ops-lead` | Shared templates for freshness SLOs |

**Differentiation reminder:** `site-reliability-engineer` runs error-budget **response** during incidents and PRRs; this skill owns **definitions, alignment, and governance cadence** for service levels.
