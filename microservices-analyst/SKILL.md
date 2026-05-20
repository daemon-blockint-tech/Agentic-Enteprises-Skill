---
name: microservices-analyst
description: |
  Guides analysis of existing microservice estates—service and API inventory, dependency and
  coupling maps (sync chains, shared-database smells), observability and SLO coverage gaps,
  deployment and version skew, API contract drift and breaking consumers, operational toil
  indicators, security blast radius, and consolidation or decomposition recommendations with
  evidence. Produces executive summaries for platform, SRE, and architect audiences. Use when
  the user says microservices analyst, analyze microservices, service dependency map, coupling
  analysis, microservice health, API drift, service inventory, blast radius, operational analysis,
  SLO coverage, technical debt microservices, strangler assessment—not greenfield boundary research
  only (microservice-researcher), writing new services (senior-software-engineer), Kubernetes-only
  tuning (cloud-engineer), or pure load testing (performance-engineer).
---

# Microservices Analyst

## When to Use

- Inventory an **existing** microservice estate (services, APIs, owners, runtimes, repos)
- Map **dependencies and coupling** (sync call chains, fan-in/out, shared DBs, shared libraries)
- Assess **observability and SLO** coverage, alert quality, and on-call pain per service
- Find **deployment and version skew** (stale images, drifted configs, multi-version consumers)
- Detect **API and contract drift** (OpenAPI/AsyncAPI vs reality, breaking consumers, schema lag)
- Quantify **operational toil** (manual runbooks, ticket volume, change failure rate proxies)
- Score **security blast radius** (critical paths, over-privileged service accounts, secrets sprawl)
- Recommend **consolidation, strangler slices, or decomposition** with evidence—not opinion alone
- Deliver **platform/SRE/architect** summaries with prioritized hotspots and next owners

## When NOT to Use

- Greenfield **boundary research**, bounded contexts, or ADR options only → `microservice-researcher`
- Implement or refactor production service code, handlers, or deployables → `senior-software-engineer`, `microservices-developer`
- Kubernetes cluster ops, node tuning, or cloud landing zones without estate analysis → `cloud-engineer`, `infrastructure-engineer`
- Pure load-test design and execution without estate-wide dependency context → `performance-engineer`
- Broker/outbox implementation or stream processing build → `event-driven-architecture`
- Enterprise portfolio strategy unrelated to operational estate health → `enterprise-strategist`

## Related skills

| Need | Skill |
|---|---|
| Greenfield decomposition, strangler research, ADR options | `microservice-researcher` |
| Estate-wide ADRs, C4, cross-system NFR sign-off | `senior-system-architecture` |
| IDP, golden paths, paved roads for remediation | `platform-engineer` |
| SLO design, error budgets, incident and on-call programs | `site-reliability-engineer` |
| Load testing, latency tuning, capacity experiments | `performance-engineer` |
| Event contracts, brokers, outbox (when building fixes) | `event-driven-architecture` |
| IaC, cluster delivery, cloud foundations | `infrastructure-engineer`, `cloud-engineer` |
| Service implementation and twelve-factor deployables | `senior-software-engineer`, `microservices-developer` |
| Rollout, cutover, and rollback tactics for remediation | `deployment-strategist` |

## Core Workflows

### 1. Scope the estate and stakeholders

Define analysis boundary (product line, region, cluster namespace, business capability), data sources, and audience (exec brief vs engineering backlog). List non-goals and hand off greenfield design to `microservice-researcher` when appropriate.

**See `references/microservices_analyst_scope.md`.**

### 2. Build service inventory and dependency map

Catalog services, APIs, events, data stores, owners, and environments. Produce dependency graph with sync/async edges, critical paths, and orphan or zombie services.

**See `references/service_inventory_and_dependency_analysis.md`.**

### 3. Assess coupling and data ownership

Flag chatty sync chains, cyclic dependencies, shared-database antipatterns, and unclear aggregate ownership. Tie findings to change risk and test burden.

**See `references/coupling_and_data_ownership.md`.**

### 4. Review observability, SLOs, and operational health

Map golden signals and SLO coverage per tier-1 service; note alert noise, missing traces, and deployment frequency vs incident correlation.

**See `references/observability_slo_and_operational_health.md`.**

### 5. Audit API contracts and version drift

Compare published contracts to runtime behavior; list breaking consumers, deprecated fields still in use, and skew across regions/clusters.

**See `references/api_contracts_and_version_drift.md`.**

### 6. Prioritize risks and recommendations

Synthesize consolidation candidates, strangler slices, decomposition triggers, and security blast-radius hotspots with evidence links. Close with executive summary and owned next steps.

**See `references/consolidation_risk_and_recommendations.md`.**

## Principles

- **Analyze what exists**—inventory and metrics before recommending new boundaries
- **Evidence over opinion**—every hotspot cites a dependency edge, metric, contract diff, or incident pattern
- **Separate research from remediation**—hand greenfield ADRs to `microservice-researcher`; implementation to engineering peers
- **Tier services**—not every pod deserves the same SLO depth; focus tier-1 paths first
- **Make blast radius visible**—critical paths and shared fate drive prioritization

## When to load references

| Topic | Reference |
|---|---|
| Scope, inputs, deliverables | `references/microservices_analyst_scope.md` |
| Inventory and dependency mapping | `references/service_inventory_and_dependency_analysis.md` |
| Coupling and data ownership | `references/coupling_and_data_ownership.md` |
| Observability, SLOs, ops health | `references/observability_slo_and_operational_health.md` |
| Contracts and version drift | `references/api_contracts_and_version_drift.md` |
| Consolidation, risk, recommendations | `references/consolidation_risk_and_recommendations.md` |
