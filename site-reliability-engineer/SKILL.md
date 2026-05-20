---
name: site-reliability-engineer
description: |
  Guides Site Reliability Engineering—SLI/SLO and error budgets, reliability dashboards and burn-rate
  alerting, production readiness reviews, capacity planning for availability, toil reduction,
  dependency and failure-mode analysis, release reliability (canaries, rollback criteria), and
  service-owner incident mitigation tied to customer impact.
  Use when defining or operating SLOs, measuring error budget burn, improving service reliability,
  running PRRs before launch, planning scalable resilient capacity, or leading technical mitigation
  during outages—not for CI/CD pipeline implementation (devops), incident program and paging policy
  design (incident-management-engineer), cloud access and patch tickets (cloud-system-administrator),
  load-test profiling (performance-engineer), rollout cutover strategy (deployment-strategist), or
  greenfield cloud build-out (cloud-engineer).
---

# Site Reliability Engineer (SRE)

## When to Use

- Define **SLIs**, **SLOs**, and **error budgets** per service or user journey
- Configure **burn-rate** alerts and reliability dashboards
- Run **production readiness reviews** before launch or major change
- Analyze **incidents** for reliability gaps and SLO impact
- Plan **capacity** for traffic growth and failure scenarios (N+1, regional loss)
- Measure and reduce **toil**; prioritize automation with highest reliability ROI
- Map **dependencies** and failure modes; design graceful degradation
- Gate **releases** on SLO/error-budget policy (canary, rollback triggers)
- Conduct **chaos or game days** when org maturity supports it
- Partner with engineering on **reliability backlog** (timeouts, retries, circuit breakers)

## When NOT to Use

- Build or fix Jenkins/GitHub Actions/GitLab pipelines → `devops`
- Design SEV levels, on-call rotations, postmortem program → `incident-management-engineer`
- IAM grants, VM patching, snapshot restores → `cloud-system-administrator`
- Stand up VPC, RDS, or new managed services → `cloud-engineer`
- JMeter/k6 load tests and app profiling → `performance-engineer`
- Blue-green cutover playbooks and change tiers → `deployment-strategist`
- K8s cluster upgrades and Helm platform → `cluster-deployment-engineer`
- Customer status page copy and comms approval → `communication-lead`
- Org-wide reliability posture, tiering, investment themes → `vp-of-infrastructure`

## Related skills

| Need | Skill |
|---|---|
| CI/CD, GitOps, pipeline observability | `devops` |
| Incident program and paging policy | `incident-management-engineer` |
| Cloud day-2 operations | `cloud-system-administrator` |
| Cloud service implementation | `cloud-engineer` |
| Performance testing and tuning | `performance-engineer` |
| Release cutover strategy | `deployment-strategist` |
| Kubernetes platform ops | `cluster-deployment-engineer` |
| Data pipeline SLAs | `data-system-ops-lead` |
| Security incidents | `defensive-security-analyst`, `cybersecurity` |
| BCP/DRP, RTO/RPO for security/IdP, ransomware recovery planning | `bcm-disaster-recovery-specialist` |
| Architecture review | `senior-system-architecture` |
| VP infrastructure leadership | `vp-of-infrastructure` |

## Core Workflows

### 1. Scope and SRE principles

Service ownership, error budget policy, boundaries with DevOps and IM.

**See `references/sre_scope_and_principles.md`.**

### 2. SLI, SLO, and error budgets

Select SLIs, set targets, alert on burn.

**See `references/sli_slo_error_budgets.md`.**

### 3. Observability for reliability

Metrics, logs, traces, alert hygiene.

**See `references/observability_reliability.md`.**

### 4. Incident response (reliability lens)

Mitigation, SLO impact, follow-up actions.

**See `references/incident_reliability_response.md`.**

### 5. Capacity, toil, and automation

Scaling, toil metrics, reliability automation.

**See `references/capacity_toil_automation.md`.**

### 6. Release reliability and resilience testing

PRR, canaries, chaos, failure modes.

**See `references/release_reliability_chaos.md`.**

## Outputs

- **SLO document** — SLI definition, target, window, exclusions, owners
- **Error budget report** — burn %, policy actions (freeze, focus week)
- **PRR checklist** — pass/fail with required fixes before launch
- **Reliability backlog** — ranked items with estimated SLO impact
- **Incident reliability summary** — budget consumed, contributing factors, action items
- **Capacity plan** — headroom, scaling triggers, regional failover notes

## Principles

- **User-centric SLIs** — measure what customers experience
- **Error budgets drive decisions** — balance velocity and reliability
- **Automate toil** — repetitive manual work is a reliability risk
- **Blameless learning** — fix systems, not people
- **Progressive delivery** — small releases with measurable rollback criteria
