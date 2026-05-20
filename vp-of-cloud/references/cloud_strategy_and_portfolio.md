# Cloud strategy and portfolio

## Table of contents

1. [Strategy inputs](#strategy-inputs)
2. [Strategic themes](#strategic-themes)
3. [Portfolio structure](#portfolio-structure)
4. [Prioritization](#prioritization)
5. [Success metrics](#success-metrics)

## Strategy inputs

Gather before drafting strategy:

| Input | Source |
|-------|--------|
| Business growth and product roadmap | CTO, CPO |
| Regulatory and residency constraints | Legal, `cloud-compliance-specialist` |
| Current spend and commit utilization | `finops-analyst`, `cloud-economist` |
| Technical debt and exit risk | `enterprise-cloud-architect`, `cloud-architect` |
| Security and audit findings | `cloud-security-engineer` |
| Hybrid/DC constraints | `vp-of-infrastructure` |

## Strategic themes

Typical 3–5 year themes (pick 3–5, not all):

| Theme | Example outcomes |
|-------|------------------|
| **Cloud-first default** | New workloads on approved landing zone |
| **Sovereign / regional** | EU-only, in-country keys, approved regions |
| **Platform consolidation** | Fewer accounts, shared services hub |
| **FinOps maturity** | Tag compliance, unit cost visible per product |
| **AI-ready foundation** | GPU quotas, data egress, model hosting guardrails |
| **Exit and portability** | Container/K8s bias, avoid proprietary lock where costly |

State **decision principles** — e.g. managed services over self-run unless latency or cost proves otherwise.

## Portfolio structure

Organize initiatives in horizons:

| Horizon | Horizon | Examples |
|---------|---------|----------|
| H0 | Now (0–2 q) | EA true-up prep, tag enforcement, critical migration wave |
| H1 | Next (2–4 q) | Landing zone v2, CCoE vending API, secondary region |
| H2 | Later (1–2 y) | Mainframe exit, data platform lift, multi-cloud DR |
| H3 | Explore | Sovereign cloud pilot, repatriation option study |

Each initiative needs: **owner**, **funding source**, **dependency**, **stage gate**, **kill criteria**.

## Prioritization

Score candidates (weight to company context):

| Dimension | Questions |
|-----------|-----------|
| Value | Revenue enablement, risk reduction, cost takeout |
| Feasibility | Team skill, vendor readiness, data gravity |
| Risk | Compliance, security, customer impact |
| Cost | Migration spend, run-rate delta, commit fit |

Use **one portfolio forum** with finance; avoid parallel cloud and infra roadmaps without sync (`vp-of-infrastructure`).

## Success metrics

Leading indicators (quarterly):

- % production compute in approved landing zone
- Tag allocation coverage and untagged spend $
- EA/commit utilization vs target
- Migration wave on-time / on-budget
- Mean time to new account (vending SLA)
- Critical security misconfig trend (CSPM)

Lagging: cloud run-rate vs plan, unit cost per core/customer/API, audit findings closed.

Delegate metric definitions to `finops-analyst` and `enterprise-cloud-architect`; VP owns targets and accountability.
