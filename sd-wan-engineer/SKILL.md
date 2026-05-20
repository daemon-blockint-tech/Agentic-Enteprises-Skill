---
name: SD-WAN (Software-Defined WAN) Engineer
description: |
  Design, deploy, and operate SD-WAN—overlay WAN (hub-spoke, mesh, regional hubs), underlay overlay (MPLS, broadband, LTE/5G), path selection, application-aware routing, SASE, zero trust WAN, branch connectivity, orchestration templates, NGFW/SWG/ZTNA insertion, HA, and brownfield SD-WAN migration; vendor-agnostic (Viptela, VeloCloud, Prisma SD-WAN). This skill should be used when the user asks about SD-WAN, software-defined WAN, SDWAN engineer, overlay WAN, path selection, application-aware routing, hub-spoke SD-WAN, SASE, zero trust WAN, branch connectivity, underlay overlay, VeloCloud, Viptela, Prisma SD-WAN, WAN optimization, or brownfield SD-WAN migration—not carrier BGP/MPLS backbone-only (network-backbone-architect), cloud VPC design (cloud-architect, cloud-engineer), enterprise APIs (enterprise-integration-api-developer), endpoint security program only (information-security-engineer), or physical DC cabling (infrastructure-engineer).
---

# SD-WAN (Software-Defined WAN) Engineer

## When to Use

- Design **overlay WAN** topologies—hub-spoke, full mesh, regional hub, dynamic mesh
- Plan **underlay** diversity—MPLS, DIA broadband, LTE/5G, private line, and carrier handoff
- Define **path selection**, SLA classes, and application-aware routing policies
- Architect **SASE** integration—SWG, CASB, ZTNA, and cloud security service insertion
- Build **orchestration** models—device templates, feature templates, policy groups, RBAC
- Plan **brownfield migration** from MPLS/VPN hub-spoke or legacy WAN optimizers
- Specify **branch CPE** roles—active/active, TLOC extensions, service chaining, local breakout
- Troubleshoot **overlay vs underlay**—tunnels, BFD, NAT, MTU, and path stickiness
- Design **multi-cloud and DC breakout**—regional gateways, cloud on-ramps, and hairpin avoidance
- Produce **runbooks**, acceptance tests, and monitoring baselines for WAN operations

## When NOT to Use

- Carrier core BGP/MPLS design, IX peering, or internet backbone routing only → `network-backbone-architect`
- Cloud landing zone, VPC design, and Well-Architected service selection → `cloud-architect`, `enterprise-cloud-architect`
- Provision cloud subnets, VPN to cloud, and managed LB without SD-WAN overlay focus → `cloud-engineer`
- Cloud IAM, CSPM, and org guardrails as primary deliverable → `cloud-security-engineer`
- Corporate security program, IdP, and endpoint controls without WAN architecture → `information-security-engineer`
- Terraform modules, CI/CD, and K8s delivery without SD-WAN design → `infrastructure-engineer`
- SLO programs, on-call, and production incident process as main task → `site-reliability-engineer`
- Application throughput, caching, and horizontal scale without WAN path design → `high-concurrency-scalability`
- REST/GraphQL and enterprise application integration → `enterprise-integration-api-developer`
- Physical rack, power, and cabling without SD-WAN edge role → `infrastructure-engineer`, `field-services-engineer`

## Related skills

| Need | Skill |
|---|---|
| Carrier backbone, BGP/MPLS core, DCI at scale | `network-backbone-architect` |
| Cloud reference architecture and hybrid connectivity | `cloud-architect` |
| Enterprise cloud governance and multi-BU programs | `enterprise-cloud-architect` |
| Implement cloud networking and managed connectivity | `cloud-engineer` |
| Cloud network security controls and posture | `cloud-security-engineer` |
| IaC, physical build, and platform delivery | `infrastructure-engineer` |
| Reliability engineering, SLOs, and production incidents | `site-reliability-engineer` |
| Application-scale concurrency and load distribution | `high-concurrency-scalability` |
| Corporate security program and tooling | `information-security-engineer` |

## Core Workflows

### 1. Scope, constraints, and success criteria

Clarify sites, traffic matrix, compliance, and migration constraints.

**See `references/sd_wan_engineer_scope.md`.**

### 2. Overlay topology and underlay

Select hub roles, mesh policy, and circuit mix per site class.

**See `references/overlay_topology_and_underlay.md`.**

### 3. Path selection, SLA, and application routing

Define business policies, SLA classes, and app identification.

**See `references/path_selection_sla_and_app_routing.md`.**

### 4. Security, SASE, and service insertion

Place NGFW, SWG, ZTNA, and local vs centralized breakout.

**See `references/security_sase_and_ztna_insertion.md`.**

### 5. Orchestration, templates, and day-two operations

Model controllers, templates, change workflow, and observability.

**See `references/orchestration_templates_and_operations.md`.**

### 6. Migration, HA, and troubleshooting

Plan cutover waves, HA modes, and overlay/underlay fault isolation.

**See `references/migration_ha_troubleshooting.md`.**

## Outputs

- **WAN context** — site inventory, traffic matrix, critical apps, and compliance constraints
- **Logical topology** — overlay roles, hub map, regional gateways, and breakout points
- **Underlay map** — circuits per site, diversity, carrier handoff, and IP addressing plan
- **Policy catalog** — SLA classes, path selection rules, and application definitions
- **Security architecture** — service insertion, SASE integration, and segmentation zones
- **Orchestration model** — template hierarchy, RBAC, and promotion workflow
- **Migration plan** — waves, rollback triggers, parallel-run criteria, and acceptance tests
- **Operations pack** — dashboards, alarms, runbooks, and escalation matrix

## Principles

- Treat **underlay independence** as a design goal—overlay must survive single-circuit loss where required
- Prefer **explicit SLA classes** over opaque “best path” defaults; document stickiness and failover timers
- Minimize **hairpinning**—local breakout for trusted SaaS and regional gateways for cloud on-ramps
- Design **brownfield** with parallel run and measurable cutover gates, not big-bang unless constrained
- Separate **control plane** (orchestrator) resilience from **data plane** (edge) HA in runbooks
- Use **vendor concepts** generically; validate against target platform docs before production config
