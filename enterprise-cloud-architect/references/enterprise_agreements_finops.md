# Enterprise agreements and FinOps

## Table of contents

1. [Enterprise agreements](#enterprise-agreements)
2. [Commit strategy](#commit-strategy)
3. [Chargeback and showback](#chargeback-and-showback)
4. [Optimization cadence](#optimization-cadence)

## Enterprise agreements

Covers AWS EDP, Azure MCA/EA, GCP commits — structure varies by vendor.

Architecture inputs for procurement (not legal negotiation):

- **Growth forecast** by BU and workload type (compute, data, AI)
- **Region mix** and sovereign requirements
- **Commit coverage** — what spend is in-scope vs marketplace/excluded
- **True-up risk** — under-commit penalties vs over-commit waste

Coordinate with `commercial-counsel` on contract structure; `compute-accounting-manager` on GL mapping.

## Commit strategy

| Instrument | Fit |
|---|---|
| Compute/Savings Plans / CUD | Steady baseline |
| RI (legacy) | Long-stable workloads |
| Spot / preemptible | Batch only with SLO headroom |
| SaaS marketplace | Often excluded — track separately |

Model **utilization** monthly; reforecast quarterly before true-up.

## Chargeback and showback

Define **allocation keys**:

- Direct tags (cost center, project)
- Shared services split (logging, hub network) by % revenue, headcount, or usage
- EA benefit distribution — fixed % or consumption-based

Publish **monthly showback** before chargeback if culture requires transparency.

Finance owns invoice payment; architecture owns **tag policy** enforcement.

## Optimization cadence

| Cadence | Actions |
|---|---|
| Weekly | Anomalies, untagged spend |
| Monthly | Rightsizing, idle resources, RI/SP coverage |
| Quarterly | Architecture standards updates, EA forecast |
| Annual | EA renegotiation data pack |

BU-level waste remediation → `cloud-engineer` execution; standards → enterprise catalog.
