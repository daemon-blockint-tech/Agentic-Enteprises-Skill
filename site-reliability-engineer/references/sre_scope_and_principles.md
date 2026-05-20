# SRE scope and principles

## Table of contents

1. [Role boundary](#role-boundary)
2. [Core principles](#core-principles)
3. [Partnership model](#partnership-model)
4. [Maturity levels](#maturity-levels)

## Role boundary

| SRE owns | Others own |
|---|---|
| SLO targets and error budget policy | SEV taxonomy and paging program (`incident-management-engineer`) |
| Reliability requirements in PRR | Pipeline YAML and GitOps (`devops`) |
| Burn-rate alerts and reliability dashboards | Cloud IAM tickets (`cloud-system-administrator`) |
| Capacity headroom for SLO | FinOps GL close (`compute-accounting-manager`) |
| Failure-mode and dependency maps | Product feature prioritization (PM) |
| Release reliability gates | Cutover ceremony design (`deployment-strategist`) |

**DevOps** ships change; **SRE** defines how much unreliability is acceptable and measures it.

## Core principles

1. **Availability is a feature** — explicit target, not assumed
2. **Error budget** — shared language between eng and product for release pace
3. **Toil cap** — target <50% ops time on toil; automate or eliminate
4. **Simplicity** — fewer moving parts beats heroic on-call
5. **Gradual rollouts** — detect regressions before full blast radius

## Partnership model

| Partner | Interaction |
|---|---|
| Product | Negotiate SLO; trade scope vs reliability when budget exhausted |
| Engineering | Embed SRE in PRR; review timeouts, queues, fallbacks |
| DevOps | Align deploy frequency with budget; shared observability stack |
| IM engineer | SRE mitigates; IM owns process, comms cadence, postmortem program |
| Security | Joint game days; reliability controls for abuse/DoS |

## Maturity levels

| Level | Characteristics |
|---|---|
| 0 | Uptime hopes; reactive pages; no SLO |
| 1 | SLIs defined; basic dashboards; informal postmortems |
| 2 | SLO + error budget; burn alerts; PRR for major launches |
| 3 | Budget gates releases; toil tracked; game days |
| 4 | Chaos in prod (controlled); automated rollback on SLO breach |

Advance one level at a time; skipping levels creates alert fatigue without trust.
