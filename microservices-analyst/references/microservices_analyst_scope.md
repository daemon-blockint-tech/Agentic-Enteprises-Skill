# Microservices Analyst — Scope

## Role

Analyze **existing** microservice landscapes: what runs today, how services depend on each other, where operations hurt, and which changes reduce risk or cost. Output is **assessment and prioritization**, not greenfield architecture research.

## Distinction from Microservice Researcher

| Dimension | Microservices Analyst | Microservice Researcher |
|---|---|---|
| Primary question | "What is wrong or risky in our estate?" | "How should we split or integrate going forward?" |
| Inputs | Catalogs, metrics, traces, contracts, deploy history | Domain events, bounded contexts, NFR targets |
| Outputs | Dependency maps, health gaps, drift reports, hotspot backlog | ADRs, options matrices, boundary recommendations |
| Typical trigger | Operational pain, audit, consolidation, incident postmortem | New product, monolith escape, org restructure |

Cross-link both skills when a program needs **research then assessment**, or **assessment then targeted research** on one boundary.

## In scope

- Service and API **inventory** (name, owner, tier, repo, runtime, environments)
- **Dependency and coupling** analysis (sync chains, events, shared stores)
- **Observability and SLO** coverage gaps, alert quality, on-call load proxies
- **Deployment and version skew** across regions/clusters
- **Contract drift** (REST, gRPC, GraphQL, AsyncAPI) and consumer compatibility
- **Operational toil** indicators (manual steps, ticket themes, change failure signals)
- **Security blast radius** on critical paths (not full pentest—factual surface map)
- **Consolidation / strangler / decomposition** candidates with evidence

## Out of scope

- Greenfield bounded-context design only → `microservice-researcher`
- Writing or shipping new microservices → `senior-software-engineer`, `microservices-developer`
- Cluster/node performance tuning without estate framing → `cloud-engineer`
- Dedicated load-test campaigns → `performance-engineer`
- Full penetration test or compliance attestation → `penetration-tester`, `compliance-engineer`

## Stakeholders and deliverables

| Audience | Typical deliverable |
|---|---|
| Platform / architecture | Estate map, coupling heatmap, tiering proposal |
| SRE / operations | SLO gap table, toil themes, incident-correlated hotspots |
| Engineering leadership | Prioritized remediation backlog with owners |
| Security | Blast-radius paths, shared-secret and over-privilege flags |
| Executives | 1-page summary: top 5 risks, cost/complexity drivers, 90-day focus |

## Required inputs (gather early)

- Service catalog or CMDB export (even partial)
- API gateways, service mesh, or ingress route lists
- APM/traces, metrics, logs retention pointers
- CI/CD deploy history per service (frequency, failure rate if available)
- OpenAPI/AsyncAPI/Protobuf repos or registry
- Recent incident themes and postmortems (redacted)
- Org chart or team-to-service mapping

## Analysis phases

1. **Bound** the estate (product, env, region, namespace).
2. **Inventory** services, APIs, data stores, and owners.
3. **Map** dependencies and classify coupling.
4. **Measure** health (SLOs, deploys, drift, toil).
5. **Recommend** with evidence, effort, and owner handoffs.

## Quality bar

- Every finding links to **evidence** (edge in graph, metric, contract diff, ticket count).
- Distinguish **fact** vs **hypothesis**; label confidence.
- Prefer **actionable** next steps with a single accountable team per item.
