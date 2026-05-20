# Infrastructure portfolio strategy

## Table of contents

1. [Portfolio layers](#portfolio-layers)
2. [Prioritization](#prioritization)
3. [Roadmap horizons](#roadmap-horizons)
4. [Build vs buy vs cloud](#build-vs-buy-vs-cloud)
5. [Stage gates](#stage-gates)

## Portfolio layers

| Layer | Examples | Horizon |
|-------|----------|---------|
| **Foundation** | Landing zone refresh, identity, network backbone | 12–36 mo |
| **Capacity** | DC build, colo expansion, GPU halls, region add | 18–60 mo |
| **Efficiency** | FinOps program, commit rebalance, utilization | 0–12 mo |
| **Reliability** | Multi-AZ, DR drills, observability standard | 6–18 mo |
| **Security baseline** | Logging, encryption, vuln SLAs on estate | 6–18 mo |
| **Transformation** | Migration waves, K8s consolidation, DC exit | 12–48 mo |

## Prioritization

Score initiatives on:

1. **Revenue or customer risk** if delayed
2. **Regulatory / contractual** deadline
3. **Unit economics** (cost per txn, per GPU-hour, per seat)
4. **Option value** (unblocks future bets)
5. **Execution risk** and dependency count

Use a **fixed envelope** — rank, do not fund everything. Partner with `data-center-portfolio-planning-execution-lead` for DC and `enterprise-cloud-architect` for cloud foundation.

## Roadmap horizons

| Horizon | VP output |
|---------|-----------|
| **Now (0–2 q)** | Committed capacity, critical vulns, incident themes |
| **Next (2–4 q)** | Approved builds, migration waves, platform milestones |
| **Later (1–3 y)** | Regional strategy, repatriation options, major vendor bets |

Publish a **one-page portfolio map** — initiative, owner, $ band, dependency, kill criteria.

## Build vs buy vs cloud

For each major bet, require a **decision brief** (not full implementation):

- Problem and constraints (latency, residency, SLO, data gravity)
- Options: extend colo, new region, SaaS, managed service, self-build
- Economic band from `cloud-economist` (NPV/TCO), not VP-built spreadsheets
- Security and compliance sign-off from security partners
- Default **prefer managed/cloud** unless economics or control clearly favor build

## Stage gates

Lightweight gates for VP review:

- **Concept** — problem, alternatives, rough NPV band, risk tier
- **Plan** — dependencies, security, FinOps impact, named owner
- **Commit** — budget line, success metrics, rollback
- **Operate** — hand to run teams; VP tracks KPIs only

Deep DC RAID → portfolio lead; deep cloud ARB → `enterprise-cloud-architect`.
