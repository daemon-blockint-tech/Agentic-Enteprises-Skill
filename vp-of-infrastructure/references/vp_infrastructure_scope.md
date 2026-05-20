# VP infrastructure scope

## Table of contents

1. [Mission](#mission)
2. [Span of control](#span-of-control)
3. [Org and operating model](#org-and-operating-model)
4. [Decision rights](#decision-rights)
5. [Handoffs](#handoffs)

## Mission

Own durable **capacity, reliability, cost efficiency, and security partnership** for compute, network, storage, and hybrid placement so product engineering can ship safely at scale.

## Span of control

Typical functions (varies by company):

| Function | VP sets | Specialists execute |
|----------|---------|---------------------|
| Cloud platform / foundation | Strategy, budget, standards adoption | `enterprise-cloud-architect`, `infrastructure-engineer` |
| Reliability | Org SLO policy, investment themes | `site-reliability-engineer`, `incident-management-engineer` |
| Data centers | Build/expand/exit portfolio | `data-center-portfolio-planning-execution-lead` |
| FinOps / cloud economics | Targets and accountability | `finops-analyst`, `cloud-economist` |
| Security partnership | Risk appetite, prioritization | `information-security-engineer`, `cloud-security-engineer` |
| Finance alignment | Envelope and narrative | `director-infrastructure-capex-accounting`, `compute-accounting-manager` |

## Org and operating model

Choose and document:

| Model | When | Risk |
|-------|------|------|
| **Central platform** | Need standards, shared services, efficiency | Bottleneck if understaffed |
| **Embedded SRE** | Strong product ownership, varied SLOs | Fragmented tooling and policy |
| **Federated cloud** | Multi-BU autonomy with guardrails | Policy drift, cost sprawl |
| **Hybrid DC + cloud** | Latency, residency, GPU density | Split accountability |

Define **interfaces**: product → platform intake; security → exception path; finance → forecast cadence; TPM → program RAID (VP sponsors, does not run weekly status).

Set **hiring bar** and **succession** for directors of platform, SRE, cloud ops, and DC delivery.

## Decision rights

| Decision | VP | Delegate |
|----------|-----|----------|
| Multi-year hybrid posture | Approves | Architects document options |
| Annual capex envelope allocation | Proposes; CFO approves | DC portfolio lead prioritizes sites |
| Org restructure (platform vs embedded) | Owns | Directors implement |
| EA/MACC sign-off threshold | Owns commercial frame | `cloud-economist` models; `finops-analyst` tracks utilization |
| Production SLO targets by tier | Sets policy | `site-reliability-engineer` implements per service |
| Single-region VPC design | Escalation only | `cloud-architect` |
| Capitalization treatment | Escalation only | `director-infrastructure-capex-accounting` |

## Handoffs

| Too detailed for VP | Skill |
|---|---|
| Terraform, pipelines, K8s | `infrastructure-engineer`, `devops` |
| CUR, rightsizing, dashboards | `finops-analyst` |
| JEs, amortization, GL | `compute-accounting-manager` |
| Weekly program RAID | `technical-program-manager` |
| Landing zone guardrails | `enterprise-cloud-architect` |
