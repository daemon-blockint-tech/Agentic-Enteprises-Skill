# Cloud architecture principles

## Table of contents

1. [Well-Architected pillars](#well-architected-pillars)
2. [NFR mapping](#nfr-mapping)
3. [Design principles](#design-principles)
4. [Anti-patterns](#anti-patterns)

## Well-Architected pillars

| Pillar | Architecture questions |
|---|---|
| Security | Identity, encryption, network isolation, audit |
| Reliability | Multi-AZ, backups, DR, blast radius |
| Performance | Latency, scaling model, caching |
| Cost | Right-sizing, commitments, waste |
| Operational excellence | IaC, observability, runbooks, change |
| Sustainability | Region choice, utilization, idle resources |

Run a **review** before major launch; track risks in backlog.

## NFR mapping

Capture measurable targets:

| NFR | Example metric |
|---|---|
| Availability | 99.9% monthly for tier-1 API |
| RTO / RPO | 4h / 15m for prod database |
| Latency | p99 < 200ms same-region |
| Throughput | Peak TPS and growth horizon |
| Compliance | Data residency EU-only |
| Cost | $/transaction budget cap |

Trace each NFR to **concrete services and patterns** in the target design.

## Design principles

- **Single responsibility per account** or bounded context where possible
- **Immutable infrastructure** — no snowflake prod changes
- **Defense in depth** — network + identity + app layers
- **Event-driven** when decoupling domains; sync only when needed
- **API-first** integration between teams

## Anti-patterns

- Lift-and-shift without refactoring dependencies
- One shared admin role for all workloads
- Public endpoints “temporarily” left open
- Multi-cloud active-active without operational maturity
- Architecture by slide deck without ADR or cost estimate

Enterprise-wide patterns spanning non-cloud systems → `senior-system-architecture`.
