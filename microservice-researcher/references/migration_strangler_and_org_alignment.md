# Migration, strangler, and org alignment

## Table of contents

1. [Migration drivers](#migration-drivers)
2. [Strangler fig pattern](#strangler-fig-pattern)
3. [Slice definition](#slice-definition)
4. [Data migration research](#data-migration-research)
5. [Cutover and parity](#cutover-and-parity)
6. [Team Topologies alignment](#team-topologies-alignment)
7. [Build vs buy vs managed](#build-vs-buy-vs-managed)
8. [Anti-patterns](#anti-patterns)

## Migration drivers

Document why leave monolith (or coarser estate):

| Driver | Research implication |
|---|---|
| Release cadence | Strangler slice per independent deploy unit |
| Scale hotspot | Extract high-RPS capability first |
| Compliance zone | Boundary at trust/data residency |
| Team scaling | Align slice to stream-aligned team |
| Technical debt | Avoid "rewrite in microservices" without capability map |

Include **cost of migration** (dual-run, training, ops) in options matrix.

## Strangler fig pattern

**Concept:** incrementally route traffic from legacy to new implementation behind a **facade** (gateway, router, feature flags) until legacy can be retired.

Research outputs:

1. **Facade placement** — edge gateway, monolith module router, or sidecar
2. **Routing rules** — by tenant, feature flag, % canary, or URL path
3. **Telemetry** — compare latency/error between legacy and new paths
4. **Retirement gate** — zero traffic + parity checklist green

**Not big-bang** unless constraints force it—document risk explicitly.

## Slice definition

A viable strangler **slice**:

- Delivers **user-visible or measurable** value when extracted
- Owns **data** it writes (with migration plan for reads)
- Minimizes **dual-write** duration
- Has **clear rollback** (route traffic back)

| Slice type | Example | Risk |
|---|---|---|
| **Edge read** | New read API + cache | Stale reads vs monolith |
| **Write behind** | New writes, legacy reads | Sync lag |
| **Parallel run** | Both paths, compare results | Cost, complexity |
| **Branch by abstraction** | ACL in monolith calling new service | Monolith still deploys |

Order slices by **learning** and **risk**, not by "easiest code."

## Data migration research

For each slice, specify:

| Topic | Research question |
|---|---|
| **Source of truth** | Monolith DB vs new service DB during transition |
| **Dual-write** | Duration, reconciliation job, conflict resolution |
| **Dual-read** | Which path is authoritative on conflict |
| **CDC vs batch** | Real-time vs nightly; cutover implications |
| **Referential integrity** | FKs across slices—eliminate or emulate |

Hand off detailed pipeline design to `data-architect` when warehouse/CDC scope dominates.

## Cutover and parity

**Parity checklist** (before traffic shift):

- Functional equivalence on critical journeys
- **Performance** within agreed % of legacy
- **Security** — authZ parity, audit logs
- **Observability** — dashboards/alerts for new path
- **Support runbook** outline

**Cutover types:**

| Type | Use when |
|---|---|
| **Canary** | Low risk; measurable comparison |
| **Blue-green** | Fast rollback; duplicate capacity affordable |
| **Big-bang slice** | Small slice; strong parity evidence |

Coordinate execution runbooks with `deployment-strategist`.

## Team Topologies alignment

Map candidate services to topology types (Team Topologies):

| Topology | Purpose | Boundary research note |
|---|---|---|
| **Stream-aligned** | End-to-end flow to user/business outcome | Default for product capabilities |
| **Platform** | Accelerate streams via paved roads | Not a dumping ground for shared domain logic |
| **Enabling** | Temporary uplift (e.g., DDD coaching) | Time-boxed |
| **Complicated-subsystem** | Deep specialty (billing engine, search) | Clear API to streams |

**Conway's law:** research should flag misalignment when desired boundaries contradict team structure—recommend org change or fewer services.

Hand off enterprise org design to `enterprise-strategist` when restructuring is in scope.

## Build vs buy vs managed

For each cross-cutting capability (auth, payments, search, messaging):

| Option | Research criteria |
|---|---|
| **Build** | Differentiation, control, long-term cost |
| **Buy (SaaS)** | Time to market, TCO, vendor risk |
| **Managed cloud** | Ops burden vs lock-in |

Document **exit strategy** and data portability for buy/managed options.

## Anti-patterns

- **Strangler without routing layer** — code flags only, no traffic control
- **First slice is framework** — "create platform team" before value slice
- **Data big-bang** — one weekend migration without reconciliation
- **Ignoring team topology** — services no team can own on-call
- **Perpetual dual-write** — no retirement date for legacy path
