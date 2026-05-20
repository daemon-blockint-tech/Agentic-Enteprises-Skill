# Reliability and security posture

## Table of contents

1. [Posture definition](#posture-definition)
2. [Service tiering](#service-tiering)
3. [Reliability themes](#reliability-themes)
4. [Security partnership](#security-partnership)
5. [Investment prioritization](#investment-priorization)

## Posture definition

**Posture** = org-wide minimum bar + tiered expectations + gap backlog funded over 2–4 quarters.

VP owns **policy and investment**; `site-reliability-engineer` owns SLI/SLO mechanics; security owns control catalog.

## Service tiering

Define tiers (example — adapt to company):

| Tier | Examples | SLO expectation | DR expectation |
|------|----------|-----------------|----------------|
| **0** | Payments, auth, core API | Strict error budget | Multi-region or RTO < 1h |
| **1** | Revenue paths | Standard SLO | AZ failover |
| **2** | Internal tools | Best effort | Backup restore |
| **3** | Sandbox | None | None |

Publish **tier assignment rules** — who can declare Tier 0; annual review with product VPs.

## Reliability themes

Set org-level themes (pick 2–4 per year):

- **Observability standard** — metrics/logs/traces baseline on all Tier 0–1
- **Incident learning** — blameless PMs, action-item SLA, repeat incident reduction
- **Capacity headroom** — regional loss, burst traffic, GPU queue depth
- **Release safety** — canary policy tied to error budget (`site-reliability-engineer`)
- **Toil reduction** — platform automation ROI

Escalate **systemic** outages (same root cause, same tier) to portfolio priority.

## Security partnership

VP does **not** own control implementation. Partner on:

| Topic | VP role | Partner skill |
|-------|---------|---------------|
| Risk appetite on infra estate | Prioritize backlog $ | `information-security-engineer` |
| Cloud guardrails adoption | Mandate timeline | `cloud-security-engineer`, `enterprise-cloud-architect` |
| Vuln SLAs on infra | Executive escalation | `cloud-security-engineer` |
| Audit / compliance narrative | SteerCo alignment | `cloud-compliance-specialist` |

Align **security baseline** with reliability tiers — Tier 0 inherits stricter logging, access, and patch windows.

## Investment prioritization

Rank reliability/security spend:

1. **Customer-visible risk** (Tier 0 gap)
2. **Regulatory / contractual** deadline
3. **Repeat incident** root causes
4. **Efficiency** that also reduces risk (automation, standard images)

Defer point fixes that belong in product code — VP funds **platform and estate** work only.
