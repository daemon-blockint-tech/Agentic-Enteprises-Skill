---
name: microservice-researcher
description: |
  Guides research and analysis for microservices architecture decisions—domain decomposition,
  bounded contexts, service boundary options and trade-offs, sync vs async integration patterns,
  data ownership and consistency (eventual consistency, sagas at research level), API and contract
  evolution, Team Topologies alignment, build vs buy vs managed services, monolith strangler
  migration, NFR impact (latency, reliability, operability), and decision records with options and
  recommendations. Use for microservice research, service boundaries, bounded context, strangler
  fig, monolith to microservices, saga vs two-phase commit, domain decomposition, microservices
  trade-off, team topologies, eventual consistency research, API versioning strategy—not assessing
  an existing estate (microservices-analyst), production service code (senior-software-engineer,
  platform-engineer), Kubernetes cluster ops only (cloud-engineer), pure network design
  (network-backbone-architect), or EDA implementation when building not researching
---

# Microservice Researcher

## When to Use

- Research **domain decomposition**, bounded contexts, and candidate service boundaries
- Compare **microservices vs modular monolith** (or other styles) with explicit trade-offs
- Analyze **sync vs async** integration, data ownership, and consistency models at decision level
- Evaluate **saga vs 2PC**, outbox, and choreography/orchestration without implementation tutorials
- Define **API and contract evolution** strategy (versioning, compatibility, deprecation)
- Plan **monolith-to-microservices** migration (strangler, parallel run, cutover criteria)
- Align services with **Team Topologies** (stream-aligned, platform, enabling, complicated-subsystem)
- Assess **build vs buy vs managed** for cross-cutting capabilities
- Quantify **NFR impact** (latency budgets, reliability, operability, cost) per boundary option
- Produce **ADRs**, options matrices, and research memos with a clear recommendation

## When NOT to Use

- Write or refactor production microservice code, handlers, or deployables → `senior-software-engineer`
- Operate Kubernetes clusters, Terraform modules, or CI/CD pipelines only → `platform-engineer`, `cloud-engineer`, `infrastructure-engineer`
- Design carrier/WAN routing, VPC topology, or physical network without application boundaries → `network-backbone-architect`
- Implement brokers, outbox consumers, schema registry ops, or stream processing → `event-driven-architecture` (when building), `microservices-developer`
- Enterprise portfolio strategy, operating model, and board-level where-to-play → `enterprise-strategist`
- Load-test execution, caching implementation, and horizontal scale tuning only → `high-concurrency-scalability`
- Cross-domain system architecture sign-off unrelated to service decomposition → `senior-system-architecture` (hand off when scope is whole-estate ADR)
- Inventory, dependency maps, SLO gaps, API drift, or operational health on a **live** estate → `microservices-analyst`

## Related skills

| Need | Skill |
|---|---|
| Existing estate inventory, coupling, SLO/API drift, ops health | `microservices-analyst` |
| Cross-system ADRs, C4, estate-wide NFR sign-off | `senior-system-architecture` |
| Event contracts, brokers, outbox, sagas (implementation) | `event-driven-architecture` |
| Service code, gRPC/REST, twelve-factor deployables | `senior-software-engineer`, `microservices-developer` |
| IDP, golden paths, paved roads | `platform-engineer` |
| Cloud landing zone, IaC, cluster delivery | `infrastructure-engineer`, `cloud-engineer` |
| Application throughput, caching, scale testing | `high-concurrency-scalability` |
| Enterprise strategy, portfolio, org design | `enterprise-strategist` |
| Enterprise API hub, iPaaS, B2B integration programs | `enterprise-integration-api-developer` |
| Rollout, cutover, and rollback tactics | `deployment-strategist` |

## Core Workflows

### 1. Frame the research question

Capture before comparing boundaries:

- Business capability and **measurable outcome**
- Constraints: teams, timeline, compliance, existing monolith/estate
- **Reversibility** (one-way vs two-way door)
- Non-goals and explicit **out-of-scope** peers

**See `references/microservice_researcher_scope.md`.**

### 2. Decompose the domain

Identify bounded contexts, ubiquitous language, and context maps (upstream/downstream, ACL, OHS).

Produce **candidate services** with ownership hypotheses—not a box diagram without data flow.

**See `references/domain_decomposition_and_boundaries.md`.**

### 3. Integration and consistency

For each boundary, document sync/async choice, data ownership, consistency model, and failure semantics.

Compare **eventual consistency**, **saga** compensation, and **2PC** only when research warrants—not as default distributed transactions.

**See `references/integration_patterns_and_consistency.md`.**

### 4. Contracts and evolution

Define public API/event contracts, versioning rules, compatibility matrix, and deprecation timeline.

**See `references/api_contracts_and_evolution.md`.**

### 5. Migration and organization

Plan strangler slices, parity criteria, dual-write/read duration, and team alignment (Team Topologies).

**See `references/migration_strangler_and_org_alignment.md`.**

### 6. Deliverables and decision record

Package options matrix, NFR table, risks, recommendation, and follow-on owners (build vs research complete).

**See `references/research_deliverables_and_decision_records.md`.**

## Principles

- **Research before split**—boundaries follow domain and team cognition, not org chart alone
- **Prefer reversible experiments**—strangler slices over big-bang when uncertainty is high
- **One writer per aggregate**—document who owns each consistency boundary
- **Make trade-offs explicit**—latency, ops burden, and team autonomy in the same table
- **Cite patterns and literature**—DDD, Team Topologies, enterprise integration patterns—without cargo-culting microservices
