# Migration and hybrid

## Table of contents

1. [Assessment](#assessment)
2. [7Rs strategies](#7rs-strategies)
3. [Wave planning](#wave-planning)
4. [Hybrid operations](#hybrid-operations)
5. [Exit and portability](#exit-and-portability)

## Assessment

Inventory:

- Applications, dependencies, data stores
- **RTO/RPO**, compliance, peak load
- Technical debt (OS, licensing, coupling)
- Team readiness and runbook gaps

Output: **migration catalog** with recommended strategy per app.

## 7Rs strategies

| Strategy | Description |
|---|---|
| Retire | Decommission |
| Retain | Stay on-prem or SaaS unchanged |
| Rehost | Lift-and-shift |
| Replatform | Managed service swap (e.g. VM → RDS) |
| Refactor | Cloud-native redesign |
| Repurchase | Move to SaaS |
| Relocate | Same hypervisor, different region/account |

Prefer **refactor** only when business case clears cost of delay.

## Wave planning

Order waves by:

1. Low dependency, high learning value
2. Isolated domains before core systems
3. Data migration complexity and cutover window

Each wave: **pilot → prod cutover → hypercare**; rollback criteria documented.

Execution runbooks → `deployment-strategist`, `cloud-engineer`.

## Hybrid operations

- **Single pane** for identity and DNS where possible
- Latency budget for cross-prem calls
- **Split-brain** risks on active-active databases
- Observability across cloud and on-prem — `devops` alignment

## Exit and portability

Document:

- Data export formats and egress cost
- Vendor-specific lock-in services avoided or isolated
- Contractual termination clauses

Avoid architecture that cannot be operated without one proprietary skill set.
