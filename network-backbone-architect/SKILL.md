---
name: Network Backbone Architect
description: |
  Design carrier- and enterprise-scale backbone networks—core/distribution/edge topology, OSPF, IS-IS, BGP
  and route policy, WAN/MPLS/SD-WAN, DCI, peering, transit, IX, anycast, ECMP, BFD, FRR, addressing,
  backbone QoS, capacity, maintenance domains, and observability (NetFlow, SNMP, telemetry); EVPN/VXLAN
  spine-leaf where relevant. This skill should be used when the user asks about network backbone, backbone
  architect, BGP design, OSPF, IS-IS, WAN architecture, MPLS, SD-WAN, data center interconnect, DCI,
  internet peering, transit provider, IX, core network design, route policy, ECMP, network redundancy,
  spine-leaf, or EVPN—not app HTTP/API (enterprise-integration-api-developer), cloud landing zone or VPC only
  (cloud-architect, enterprise-cloud-architect), host or endpoint security (information-security-engineer),
  cloud/Linux sysadmin (cloud-system-administrator), cabling without routing (infrastructure-engineer), or
  OT/ICS (scada-ics-cyber-security-specialist).
---

# Network Backbone Architect

## When NOT to Use

- REST/GraphQL, ESB, or enterprise application integration design → `enterprise-integration-api-developer`
- Cloud Well-Architected, landing zone, and managed VPC/service selection → `cloud-architect`, `enterprise-cloud-architect`
- Day-two cloud resource configuration (subnets, LB, managed VPN to cloud) → `cloud-engineer`
- Cloud security guardrails, CSPM, and cloud IAM as primary deliverable → `cloud-security-engineer`
- Host firewall, endpoint, and corporate security control catalog → `information-security-engineer`
- OS patching, VM admin, and cloud instance operations → `cloud-system-administrator`
- Terraform modules, CI/CD, and K8s platform delivery without backbone routing design → `infrastructure-engineer`
- SLO programs, on-call, and incident response as the main task → `site-reliability-engineer`
- Cross-domain system ADRs unrelated to routing → `senior-system-architecture`
- Application throughput, caching, and horizontal scale without L3 design → `high-concurrency-scalability`
- Event bus and messaging topology only → `event-driven-architecture`
- OT/ICS segmentation, Purdue model, and plant protocols → `scada-ics-cyber-security-specialist`

## Related skills

| Need | Skill |
|---|---|
| Cloud reference architecture and hybrid connectivity hooks | `cloud-architect` |
| Enterprise cloud governance and multi-BU landing zones | `enterprise-cloud-architect` |
| Implement cloud networking and managed connectivity | `cloud-engineer` |
| Cloud network security controls and posture | `cloud-security-engineer` |
| IaC, physical DC build, and platform delivery | `infrastructure-engineer` |
| Reliability engineering, SLOs, and production incidents | `site-reliability-engineer` |
| Enterprise system architecture across domains | `senior-system-architecture` |
| Application-scale concurrency and load distribution | `high-concurrency-scalability` |
| Async messaging and event-driven integration | `event-driven-architecture` |

## Core Workflows

### 1. Scope, constraints, and design principles

Clarify scale (sites, regions, carriers), traffic matrix, RTO/RPO for paths, and regulatory or sovereignty constraints.

**See `references/network_backbone_architect_scope.md`.**

### 2. Topology, hierarchy, and addressing

Define core/distribution/edge roles, summarization boundaries, and IP/VLAN/VRF plan.

**See `references/topology_hierarchy_and_addressing.md`.**

### 3. Routing protocols and policy

Select IGP (OSPF, IS-IS) and BGP design—peering, communities, path selection, and filtering.

**See `references/routing_igp_bgp_and_policy.md`.**

### 4. WAN, MPLS, and SD-WAN

Architect carrier services, underlay/overlay, hub-spoke vs full mesh, and SLA alignment.

**See `references/wan_mpls_sdwan_and_carriers.md`.**

### 5. DCI, peering, and internet edge

Design data center interconnect, IX/transit/peering, and anycast or multi-homing at the edge.

**See `references/dci_peering_and_internet_edge.md`.**

### 6. Resilience, QoS, capacity, and operations

Plan redundancy, BFD/FRR, backbone QoS, link sizing, change windows, and observability.

**See `references/resilience_qos_capacity_operations.md`.**

## Outputs

- **Backbone context** — sites, traffic matrix, critical flows, and failure domains
- **Logical topology** — hierarchy, VRFs, summarization points, and DCI attachment
- **Routing design** — IGP areas/levels, BGP AS plan, policies, and community/tag semantics
- **WAN/SD-WAN architecture** — underlay, overlay, hub roles, and carrier map
- **Internet edge brief** — peering vs transit, IX placement, prefix origination, and filtering
- **Resilience and QoS matrix** — ECMP, BFD, FRR, DSCP classes, and maintenance domains
- **Capacity model** — link sizing assumptions, growth headroom, and trigger thresholds
- **Observability plan** — flow telemetry, SNMP/telemetry targets, and backbone dashboards

## Principles

- **Hierarchy before complexity** — aggregate at core; keep edge policies simple
- **Explicit failure domains** — maintenance windows and blast radius per region or plane
- **Policy at the edge** — filter and tag at borders; keep core transit predictable
- **Measure before oversizing** — size links from busy-hour matrices and growth, not peak anecdotes
- **Prefer L3 DCI** — stretch L2 only with documented operational cost and risk
- **Document one-way doors** — ASN allocation, summarization boundaries, and peering contracts
