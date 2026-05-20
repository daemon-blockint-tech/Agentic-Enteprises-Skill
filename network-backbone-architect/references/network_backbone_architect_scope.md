# Network backbone architect scope

## Table of contents

1. [Role and boundaries](#role-and-boundaries)
2. [Stakeholders and inputs](#stakeholders-and-inputs)
3. [Traffic matrix and critical flows](#traffic-matrix-and-critical-flows)
4. [Design constraints](#design-constraints)
5. [Deliverable checklist](#deliverable-checklist)
6. [Review gates](#review-gates)
7. [Handoffs to peer skills](#handoffs-to-peer-skills)

## Role and boundaries

The network backbone architect owns **carrier- and enterprise-scale routed infrastructure** between sites, data centers, and the public internet. Scope includes:

- **Logical and physical hierarchy** — core, distribution, aggregation, edge, and WAN attachment roles
- **Routing and addressing** — IGP domains, BGP policy, summarization, and multi-VRF/multi-tenant separation at the network layer
- **WAN and carrier services** — MPLS L3VPN, private lines, SD-WAN overlays, and hybrid underlay design
- **DCI and internet edge** — stretched fabrics only when justified; peering, transit, IX, and anycast placement
- **Resilience and operations** — ECMP, BFD, fast reroute, maintenance domains, QoS at backbone scope, capacity planning, and flow/SNMP/telemetry observability

Out of scope (defer to peer skills):

| Topic | Skill |
|---|---|
| Application APIs, ESB, message contracts | `enterprise-integration-api-developer` |
| Cloud landing zone, Well-Architected, service selection | `cloud-architect`, `enterprise-cloud-architect` |
| Cloud resource implementation | `cloud-engineer` |
| Endpoint and host security controls | `information-security-engineer` |
| OS/instance administration | `cloud-system-administrator` |
| Terraform/K8s delivery without routing design | `infrastructure-engineer` |
| SRE on-call and error budgets | `site-reliability-engineer` |
| OT/ICS and plant networks | `scada-ics-cyber-security-specialist` |

## Stakeholders and inputs

Gather before locking topology:

| Stakeholder | Typical inputs |
|---|---|
| Application / platform teams | East-west vs north-south ratios, latency budgets, multicast needs |
| Security architecture | segmentation model, inspection points, DDoS and filtering requirements |
| Data center / facilities | rack power, cross-connect limits, diverse path availability |
| Carriers / IX | SLA, MTU, BGP session limits, community support, LOA timelines |
| Operations / NOC | change windows, tooling (SNMP, gNMI, NetFlow), escalation paths |
| Compliance | data residency, lawful intercept hooks, audit logging for config changes |

Minimum discovery artifacts:

- Site inventory with **criticality tier** (Tier 0 backbone vs Tier 2 branch)
- Current **ASN**, prefix holdings, and IRR/RPKI posture
- Existing **IGP** (if any) and pain points (slow convergence, area sprawl)
- **RTO/RPO** per site pair for network path loss (not application DR alone)

## Traffic matrix and critical flows

Build a **traffic matrix** (source × destination × protocol × peak/average Mbps × packet size profile):

| Flow class | Examples | Design implications |
|---|---|---|
| Inter-site business | ERP, file shares, VoIP | Latency-sensitive; prefer stable IGP metrics |
| DCI replication | storage sync, DB log shipping | Loss/latency sensitive; may need dedicated DCI or QoS |
| Internet egress | SaaS, updates, guest Wi-Fi | Asymmetric; policy at edge; DDoS scrubbing |
| Cloud on-ramps | VPN/Direct Connect/ExpressRoute | Overlap with `cloud-architect`; document handoff points |
| Management | SNMP, SSH, NTP, syslog | Out-of-band or dedicated VRF; never compete with user QoS |

Label **critical flows** that must survive single-link or single-node failure within documented convergence time (e.g., sub-50 ms with BFD + FRR where required).

## Design constraints

Document non-negotiables early:

- **MTU end-to-end** — jumbo on DCI vs 1500 on internet; TCP MSS clamping plan
- **Address space** — RFC1918 vs provider-independent; IPv6 dual-stack policy
- **Vendor mix** — single-vendor backbone vs multi-vendor with standardized features only
- **Automation** — NETCONF/gNMI, Git-backed config, and rollback expectations
- **Regulatory** — encryption in transit (MACsec/IPsec on WAN), geo restrictions on traffic paths
- **Scale limits** — max prefixes per peer, max ECMP width, max areas/levels in IGP

## Deliverable checklist

| Deliverable | Contents |
|---|---|
| Context diagram | Sites, carriers, cloud on-ramps, security inspection |
| Logical topology | Layers, VRFs, summarization boundaries |
| IP plan | Allocations per site/VRF, loopbacks, link nets, anycast pools |
| Routing design | IGP type/areas, BGP AS plan, policies, communities |
| WAN architecture | Underlay, overlay, hub roles, carrier map |
| Internet edge | Peering/transit, IX list, prefix origination, filtering |
| Resilience matrix | Node/link SPOFs, BFD, FRR, maintenance domains |
| QoS design | DSCP classes, queue mapping on backbone hops |
| Capacity model | Link sizes, growth, upgrade triggers |
| Observability | Telemetry targets, flow export, alert thresholds |
| Migration waves | cutover order, rollback, parallel run duration |

## Review gates

Run structured reviews before build:

1. **Architecture review** — hierarchy, summarization, and failure domains
2. **Security review** — filtering, RPKI, management plane isolation
3. **Operations review** — change windows, monitoring, runbooks for peer loss
4. **Carrier review** — LOA, BGP parameters, SLA alignment with design assumptions

Capture decisions in short ADRs: problem, options, decision, consequences, and revisit triggers.

## Handoffs to peer skills

| When design touches… | Hand off to… |
|---|---|
| Account structure, shared services, hybrid cloud reference | `cloud-architect`, `enterprise-cloud-architect` |
| Implementing VPC, TGW, Cloud VPN, or managed LB | `cloud-engineer` |
| Terraform modules for network-adjacent infra | `infrastructure-engineer` |
| Production SLOs and incident playbooks | `site-reliability-engineer` |
| End-to-end system integration beyond L3 | `senior-system-architecture` |

Keep backbone documents **routing-centric**; cloud diagrams should reference backbone attachment points (peer IPs, VLANs, BGP neighbors) without duplicating full cloud service catalogs.
