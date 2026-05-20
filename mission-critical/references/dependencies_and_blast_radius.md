# Dependencies and blast radius

## Table of contents

1. [Dependency mapping scope](#dependency-mapping-scope)
2. [Blast radius concepts](#blast-radius-concepts)
3. [Mapping workflow](#mapping-workflow)
4. [Shared fate and choke points](#shared-fate-and-choke-points)
5. [Containment strategies](#containment-strategies)
6. [Outputs and maintenance](#outputs-and-maintenance)

## Dependency mapping scope

For each Tier 0/1 service, document:

| Layer | Examples |
|---|---|
| **Runtime** | Compute, containers, serverless, OT gateways |
| **Data** | Primary DB, caches, queues, object stores, search |
| **Identity** | IdP, MFA, API keys, service accounts, HSM/KMS |
| **Network** | DNS, LB, WAF, private links, CDN |
| **Platform** | K8s control plane, service mesh, GitOps, CI/CD |
| **Third party** | SaaS APIs, payment rails, market data, SMS/email |
| **People / process** | On-call vendor, manual reconciliation desk |

Mark **direction** (sync/async), **criticality of path**, and **fallback** if dependency fails.

## Blast radius concepts

| Term | Meaning |
|---|---|
| **Blast radius** | Maximum scope of impact from one failure or change |
| **Failure domain** | Boundary within which a fault propagates freely |
| **Shared fate** | Independent-looking services that fail together |
| **Cascading failure** | Overload or retry storm amplifies initial fault |

Tier 0 design goal: **limit blast radius** even when availability SLO is momentarily met (e.g., corrupt downstream).

## Mapping workflow

1. **Anchor** on Tier 0/1 service and primary user journeys
2. **Walk the request path** — ingress → app → data → async consumers
3. **Walk the change path** — commit → build → deploy → config → secrets
4. **Walk the ops path** — metrics, logs, traces, paging, runbooks
5. **Label each node** with tier, owner, and **max outage if node fails alone**
6. **Identify cycles** — mutual dependencies (A→B→A) are high risk
7. **Validate** with game day or tabletop; update quarterly minimum

Use dependency truth from **CMDB/service catalog**; challenge “unknown” edges for Tier 0.

## Shared fate and choke points

Flag components that concentrate risk:

| Choke point type | Why it matters |
|---|---|
| **Regional control plane** | One API outage affects all clusters in region |
| **Global load balancer / DNS** | Misconfig affects all regions |
| **Shared secrets store** | Rotation or outage hits many services |
| **Central logging/SIEM** | Blind spot during incident—not always Tier 0 but document |
| **Monolithic database** | Schema change or corruption spans domains |
| **Single vendor SaaS** | Contract RTO may exceed your MTPD |

For each choke point: **mitigation** (shard, isolate, dual-vendor, break-glass) or **accepted risk** with sponsor sign-off.

## Containment strategies

| Strategy | Use when |
|---|---|
| **Bulkheads** | Isolate thread pools, queues, or cells per tenant/region |
| **Cell-based architecture** | Limit customer blast to one cell |
| **Async boundaries** | Queue between domains; absorb spikes |
| **Read replicas / CQRS** | Protect write path from read overload |
| **Feature flags** | Disable non-critical features under stress |
| **Manual break-glass** | Last resort; audited and rehearsed |

Pair `cyber-resilience-engineer` when dependency loss is **attack-driven** (IdP, logging, backup).

## Outputs and maintenance

| Artifact | Contents |
|---|---|
| **Dependency graph** | Nodes, edges, tier, sync/async, owner |
| **Blast-radius sheet** | Top N failure scenarios ranked by impact × likelihood |
| **Choke-point register** | Mitigation status, target date, executive owner |
| **Interface contracts** | Timeout, retry, idempotency requirements for Tier 0 consumers |

Trigger refresh on: new Tier 0 promotion, major vendor change, merger integration, or post-incident learning.
