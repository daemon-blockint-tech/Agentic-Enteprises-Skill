# SD-WAN engineer scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [Intake checklist](#intake-checklist)
3. [Traffic matrix and site classes](#traffic-matrix-and-site-classes)
4. [Non-functional requirements](#non-functional-requirements)
5. [Compliance and data residency](#compliance-and-data-residency)
6. [Deliverables](#deliverables)
7. [Handoffs](#handoffs)

## Role boundary

The SD-WAN engineer owns **overlay WAN design and operations**: how branches and data centers connect over diverse underlays with centralized policy, application-aware forwarding, and integrated security services.

| In scope | Out of scope (use peer skill) |
|---|---|
| Hub-spoke / mesh overlay, TLOC, templates | Carrier core BGP/MPLS only → `network-backbone-architect` |
| Underlay circuit mix and handoff | Cloud VPC/landing zone design → `cloud-architect` |
| Path selection, SLA classes, app routes | Cloud resource implementation → `cloud-engineer` |
| SASE/ZTNA insertion at WAN edge | Corp IdP/SIEM program → `information-security-engineer` |
| Brownfield migration from MPLS/VPN | Terraform/K8s platform → `infrastructure-engineer` |
| Overlay vs underlay troubleshooting | App horizontal scale → `high-concurrency-scalability` |

## Intake checklist

Capture before topology or policy design:

| Item | Questions |
|---|---|
| Sites | Count, regions, tier (HQ, large branch, small branch, DC) |
| Applications | SaaS, private cloud, on-prem DC, VoIP/video, bulk replication |
| Current WAN | MPLS L3VPN, internet VPN, optimizers, dual-hub, regional hubs |
| Security | NGFW at branch, centralized inspection, ZTNA, segmentation zones |
| Carriers | Contracts, SLAs, handoff (Ethernet, NNI), diversity rules |
| Cloud | AWS/Azure/GCP breakout, on-ramp partners, private connectivity |
| Constraints | Budget, timeline, mandated vendor, sovereign data paths |
| Operations | Existing NMS/SIEM, change windows, staffing model |

## Traffic matrix and site classes

Build a **traffic matrix** (source → destination → app → volume/latency sensitivity):

| Flow type | Typical sensitivity | Design hook |
|---|---|---|
| Real-time (VoIP, UC) | Low jitter, fast failover | Dedicated SLA class, DSCP if honored end-to-end |
| Interactive (VDI, Citrix) | Latency, loss | Regional hub or local breakout where licensed |
| Business apps (ERP, CRM) | Moderate | Hub or regional gateway with path selection |
| Bulk (backup, replication) | Throughput | Separate SLA; avoid starving interactive on shared broadband |
| SaaS (M365, Salesforce) | Latency to nearest PoP | Local or regional breakout; SASE PoP alignment |
| East-west (branch-branch) | Policy-dependent | Full mesh vs hub hairpin vs SD-WAN service chaining |

Define **site classes** with default templates:

- **DC / regional hub** — high bandwidth, dual underlay, security stack, cloud on-ramp
- **Large branch** — dual underlay, local breakout optional, guest segmentation
- **Small branch** — LTE backup, simplified policy, zero-touch provisioning
- **Temporary / IoT** — minimal overlay, strict segmentation, no lateral paths

## Non-functional requirements

Document measurable targets per site class:

| NFR | Example target | Notes |
|---|---|---|
| Availability | 99.9% overlay for tier-1 branches | Requires dual underlay + HA CPE mode |
| Failover | Sub-3s for voice SLA class | BFD/tunnel timers must align with carrier SLA |
| Latency | p95 < 120 ms to regional hub | Depends on geography and breakout |
| Throughput | N× Mbps committed per circuit | Include headroom for burst and IPsec overhead |
| Change | Template push < 15 min for policy group | Staged rollout and rollback plan required |
| Observability | 5-minute metrics retention 13 months | Overlay and per-underlay health |

## Compliance and data residency

- Identify **data residency** requirements (traffic must not transit specific countries)
- Map **inspection points** (centralized vs local) to regulatory allow/deny lists
- Document **logging** retention for security and WAN telemetry (PII in flow records)
- Align with **zero trust** posture—identity before app access, not VPN trust alone

## Deliverables

| Artifact | Purpose |
|---|---|
| WAN context summary | Sites, matrix, constraints, assumptions |
| Logical overlay diagram | Hubs, meshes, gateways, breakout |
| Underlay and carrier map | Circuits, diversity, handoff details |
| Policy catalog | SLA classes, app definitions, path rules |
| Security insertion diagram | NGFW/SWG/ZTNA placement |
| Template/orchestration model | Hierarchy, RBAC, promotion |
| Migration waves and test plan | Cutover, rollback, acceptance |
| Operations pack | Dashboards, alarms, runbooks |

## Handoffs

| Partner skill | When to engage |
|---|---|
| `network-backbone-architect` | Core routing, MPLS VPN design at carrier, DCI |
| `cloud-architect` | Multi-cloud architecture, private connectivity strategy |
| `cloud-security-engineer` | Cloud-side segmentation and guardrails for breakout |
| `information-security-engineer` | Corp security standards, ZTNA vendor selection |
| `site-reliability-engineer` | SLO/error budget for WAN as a platform |
| `infrastructure-engineer` | Physical install, DC cross-connect, automation outside controller |
