# VP cloud scope

## Table of contents

1. [Mission](#mission)
2. [Span of control](#span-of-control)
3. [Vs VP of infrastructure](#vs-vp-of-infrastructure)
4. [Cloud operating model](#cloud-operating-model)
5. [Decision rights](#decision-rights)
6. [Handoffs](#handoffs)

## Mission

Own durable **cloud adoption, spend discipline, and risk partnership** so engineering can build on hyperscaler and hybrid foundations with clear standards, predictable economics, and executive accountability.

## Span of control

Typical functions (varies by company):

| Function | VP sets | Specialists execute |
|----------|---------|---------------------|
| Cloud strategy and portfolio | Themes, waves, funding gates | `enterprise-cloud-architect`, `technical-program-manager` |
| Landing zone / platform | Adoption targets, CCoE charter | `enterprise-cloud-architect`, `cloud-engineer` |
| Migration program | Prioritization, ROI narrative | `cloud-architect`, `technical-program-manager` |
| EA / commits | Commercial frame, coverage policy | `cloud-economist`, `finops-analyst` |
| Cloud security partnership | Risk appetite, investment themes | `cloud-security-engineer`, `information-security-engineer` |
| Regulated placement | Residency and segmentation themes | `enterprise-cloud-architect`, `cloud-compliance-specialist` |
| Finance alignment | Cloud envelope and showback | `finops-analyst`, `compute-accounting-manager` |

## Vs VP of infrastructure

| Topic | VP of Cloud | VP of Infrastructure |
|-------|-------------|----------------------|
| Primary lens | Cloud program, CCoE, EA, migration | Full stack: DC + cloud + platform portfolio |
| Capex | Cloud commits, migration funding | Racks, colo, network, GPU supply |
| Reliability | Cloud tiering and adoption blockers | Org SLO policy, DC + platform reliability |
| When to escalate | Cross-domain infra bet | Cloud-only bet stays with cloud VP |

Partner on **hybrid placement**, **total envelope**, and **board narrative**; avoid duplicate SteerCo forums.

## Cloud operating model

Document one of:

| Model | When | Risk |
|-------|------|------|
| **Central cloud platform** | Need guardrails, vending, EA efficiency | Bottleneck if understaffed |
| **Federated BUs** | Strong BU P&L, varied compliance | Policy drift, tag sprawl |
| **Embedded cloud champions** | Fast product teams | Inconsistent patterns |
| **Managed service partner** | Skill gap, time pressure | Lock-in, margin leakage |

Define **interfaces**: product intake; security exception path; finance forecast cadence; TPM owns RAID (VP sponsors).

Set **hiring bar** and **succession** for directors of cloud platform, CCoE, and migration office.

## Decision rights

| Decision | VP | Delegate |
|----------|-----|----------|
| Multi-year cloud-first / hybrid posture | Approves | `enterprise-cloud-architect` documents options |
| Migration wave funding and order | Owns portfolio | `cloud-architect` per-app design |
| Annual cloud spend envelope | Proposes; CFO approves | `finops-analyst` tracks utilization |
| EA/MACC sign-off threshold | Owns commercial frame | `cloud-economist` models; legal reviews contract |
| CCoE mandatory standards | Approves catalog tier | `enterprise-cloud-architect` drafts |
| Single-service IAM or subnet design | Escalation only | `cloud-engineer` |

## Handoffs

| Too detailed for VP | Skill |
|---|---|
| Terraform, pipelines, K8s | `cloud-engineer`, `infrastructure-engineer`, `devops` |
| OU map, SCPs, ARB packets | `enterprise-cloud-architect` |
| CUR, rightsizing, dashboards | `finops-analyst` |
| TCO/NPV spreadsheets | `cloud-economist` |
| Weekly migration RAID | `technical-program-manager` |
| DC site selection and MW | `vp-of-infrastructure`, `data-center-portfolio-planning-execution-lead` |
