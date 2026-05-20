# Metrics, reporting, and governance

## Table of contents

1. [KPI framework](#kpi-framework)
2. [Operational metrics](#operational-metrics)
3. [Test and exercise metrics](#test-and-exercise-metrics)
4. [Incident and RTA tracking](#incident-and-rta-tracking)
5. [Reporting audiences](#reporting-audiences)
6. [Governance cadence](#governance-cadence)
7. [NIST CSF Recover evidence map](#nist-csf-recover-evidence-map)

## KPI framework

| KPI | Definition | Target direction |
|---|---|---|
| **Tier coverage** | % tier-0/1 services with documented RTO/RPO | ↑ 100% documented |
| **Test coverage** | % tier-0/1 with restore test in last 12 mo | ↑ ≥90% |
| **Restore pass rate** | Tests meeting RTO/RPO and integrity | ↑ ≥95% |
| **Mean RTA gap** | Avg (RTA − RTO) for tested services | ↓ ≤0 on tier-0 |
| **Immutable coverage** | % tier-0/1 data on immutable backup path | ↑ per policy |
| **Backup lag SLA** | % jobs within RPO lag threshold | ↑ ≥99% |
| **Playbook freshness** | % playbooks reviewed <12 mo | ↑ 100% |
| **Open resilience debt** | Critical gaps past due | ↓ trend |

## Operational metrics

Leading indicators (automate where possible):

- Backup job success vs **verified** restore readiness
- Replication lag (seconds/minutes) vs RPO
- Object-lock deny events (attempted deletes)
- IdP/SIEM/EDR **synthetic availability** checks
- Gold image age and vulnerability scan status
- Secrets rotation failures blocking recovery

Dashboards should separate **prod** vs **security plane** vs **backup plane** health.

## Test and exercise metrics

Per quarter report:

| Metric | Notes |
|---|---|
| Exercises planned vs executed | Include cancelled with reason |
| Scenarios covered | Map to attack playbook IDs |
| Findings by severity | Critical/high/med/low |
| Mean time to remediate findings | By severity |
| Repeat findings | Flag process failure |
| RTA vs RTO scatter | Per service |

Link each metric to **evidence artifact** (report ID, ticket).

## Incident and RTA tracking

During real events capture:

- **Detection to mobilization** time
- **Mobilization to recovery start**
- **RTA** per service vs documented RTO
- **Effective RPO** (timestamp of restored data)
- **MVC duration** — time at degraded capability
- **Decision gates** invoked (G1–G5 from playbooks)

Post-incident: compare to **last drill**; if RTA >2× drill RTA, schedule targeted retest.

## Reporting audiences

| Audience | Content | Owner collaboration |
|---|---|---|
| **Engineering leadership** | Debt backlog, architecture changes, test pass rate | You lead |
| **BCM / risk** | Tier register, exercise summary, gaps | `bcm-disaster-recovery-specialist` |
| **CISO / security** | Security service recovery posture | `cybersecurity`, `chief-information-security-officer` |
| **Audit / compliance** | Evidence index, not legal opinions | `compliance-specialist` for control mapping |
| **Board / exec** | 1-page trend, top 3 risks, material incidents | BCM/CISO often present |

Keep reports **factual**—distinguish tested vs assumed recovery.

## Governance cadence

| Cadence | Activity |
|---|---|
| **Weekly** | Backup lag review, open critical gaps |
| **Monthly** | Resilience standup with SRE, IR, platform |
| **Quarterly** | Tier register review; test plan; KPI pack |
| **Semi-annual** | Game day or major failover |
| **Annual** | Architecture refresh; playbook full review; maturity assessment |

**Change control:** RTO/RPO tightening needs service owner approval; loosening needs risk acceptance.

## NIST CSF Recover evidence map

| CSF subcategory | Example evidence |
|---|---|
| RC.RP-01 | Recovery playbooks, dependency maps |
| RC.RP-02 | RTO/RPO register, BIA alignment memo |
| RC.RP-03 | Prioritized recovery sequence docs |
| RC.RP-04 | Critical service dependency diagram |
| RC.IM-01 | Post-test remediation tickets |
| RC.IM-02 | Lessons learned after incidents |
| RC.MA-01 | Restore test reports with RTA/RPO |
| RC.MA-02 | Game-day after-action reviews |
| RC.SC-01 | SaaS recovery register, vendor contacts |

Maintain an **evidence index** (control → artifact → date) for audit requests; control interpretation stays with compliance peers.
