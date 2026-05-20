# Resilience, QoS, capacity, and operations

## Table of contents

1. [Redundancy models](#redundancy-models)
2. [ECMP and hash polarization](#ecmp-and-hash-polynomial)
3. [BFD and fast detection](#bfd-and-fast-detection)
4. [Fast reroute and FRR](#fast-reroute-and-frr)
5. [Backbone QoS and DSCP](#backbone-qos-and-dscp)
6. [Capacity planning and link sizing](#capacity-planning-and-link-sizing)
7. [Maintenance domains and change windows](#maintenance-domains-and-change-windows)
8. [Observability architecture](#observability-architecture)
9. [Operational runbooks](#operational-runbooks)

## Redundancy models

| Model | Description | Use case |
|---|---|---|
| 1+1 | Active/standby path or device | Legacy serial links, firewalls in A/S |
| 1:1 | Dedicated backup | Cost-sensitive remote sites |
| N+1 | Shared spare capacity | Core link groups |
| N+N (ECMP) | Active/active parallel paths | Modern backbone default |

**Device redundancy:**

- **Dual supervisors** on chassis where available
- **vRR/NSR** for control-plane restart
- **Geographic redundancy** — second DC or POP, not only second line card

Document **SPOFs** explicitly when cost prevents true diversity (single carrier entrance, single IX port).

## ECMP and hash polarization

**Equal-cost multipath** load-shares flows across parallel links:

| Topic | Guidance |
|---|---|
| Hash fields | L3/L4 5-tuple typical; avoid polarizing on single field |
| Unequal cost | UCMP where supported for diverse bandwidth links |
| Polarization | Add **link numbers** or **LAG member diversity** to vary hash |
| Flow stickiness | Long flows stay on one path — size each member for peak single-flow + average |

**LAG/MC-LAG:** prefer **L3 ECMP** across routers over stretched L2 bundles when possible.

Verify **symmetric routing** with stateful firewalls in path.

## BFD and fast detection

**Bidirectional Forwarding Detection** sub-second failure detection for:

- IGP (OSPF, IS-IS)
- BGP (especially eBGP on internet and MPLS CE)
- MPLS LSP (platform-dependent)
- LAG member links

| Parameter | Aggressive | Conservative |
|---|---|---|
| Tx/Rx interval | 50–300 ms | 500 ms–1 s |
| Multiplier | 3 | 3–5 |

Match **carrier BFD** support on MPLS handoffs. Disable aggressive BFD on **high-latency satellite** unless tested.

## Fast reroute and FRR

| Mechanism | Layer | Benefit |
|---|---|---|
| LFA / RLFA | IGP | Local repair before global reconvergence |
| TI-LFA | IGP + SR | Broader repair coverage |
| BGP PIC | BGP | Precomputed backup next-hop |
| FRR for MPLS | MPLS | Fast switch to backup LSP |

**Design steps:**

1. Enable IGP **fast convergence** features platform supports
2. Verify **micro-loop** avoidance settings
3. Lab-test **single fiber cut** and **node isolation**

Document expected **traffic shift** during FRR (some micro-bursts acceptable).

## Backbone QoS and DSCP

Define **end-to-end DSCP model** (example enterprise classes):

| Class name | DSCP (example) | Traffic |
|---|---|---|
| Network control | CS6 (48) | Routing protocols, BFD |
| Voice | EF (46) | RTP telephony |
| Video | AF41 (34) | Interactive video |
| Business critical | AF31 (26) | Tier-1 apps |
| Default | BE (0) | Standard |
| Scavenger | CS1 (8) | Backup, bulk |

**Backbone queuing:**

- **Strict priority** for voice (policed EF)
- **WFQ/CBWFQ** for assured and default
- **Shape** at WAN edge to carrier CIR

**WAN carrier mapping:** document **DSCP → MPLS EXP** or **COS** per carrier contract.

Avoid **re-marking** at every hop; trust boundaries at **edge** only unless mitigating trust issues.

Application QoS without network participation → coordinate with `high-concurrency-scalability` for app-level throttling; network still defines classes for real-time traffic.

## Capacity planning and link sizing

### Traffic engineering inputs

- **Busy hour** utilization per link (95th percentile)
- **Growth rate** (historical 6–12 months + business forecast)
- **Burst factor** for elephant flows (storage, backup windows)

### Sizing formula (simplified)

```
required_bandwidth = peak_measured × (1 + growth%) × headroom_factor
```

Typical **headroom_factor**: 1.3–1.5 for backbone; higher for internet unpredictable bursts.

### Triggers

| Metric | Action |
|---|---|
| >70% util 5-min BH | Plan upgrade |
| >85% sustained | Emergency upgrade / traffic shift |
| Queue drops on PQ/WFQ | Review QoS or capacity |
| RTT/loss SLA miss | Path diversity or carrier escalation |

Maintain **capacity dashboard** per critical path; review quarterly.

## Maintenance domains and change windows

**Maintenance domain:** set of nodes/links upgraded together with controlled traffic drain.

| Technique | Use |
|---|---|
| max-metric router-lsa / overload bit | Drain IGP before reboot |
| BGP graceful shutdown | Withdraw with GSHUT community |
| AS-path prepend outbound | Reduce inbound during window |
| Maintenance BGP community | Signal peers (if supported) |

**Change classification:**

| Class | Example | Window |
|---|---|---|
| Standard | ACL tune, description | Business hours with rollback |
| Major | IGP area redesign, RR move | Planned outage window |
| Emergency | Security filter for attack | Anytime with approval |

Document **rollback** (config snapshot, parallel run duration) for every backbone change.

## Observability architecture

Architecture-level telemetry (implementation with NOC/tools):

| Source | Data | Use |
|---|---|---|
| NetFlow / IPFIX / sFlow | Per-flow stats | Capacity, anomaly, security |
| SNMP / gNMI telemetry | Interface counters, queues, CPU | Threshold alerts |
| BGP monitoring | Update rate, prefix count | Leak detection |
| Synthetic probes | TWAMP, ICMP, HTTP | Path SLA |
| Syslog / audit | Config changes | Compliance |

**Key alerts (examples):**

- eBGP session down > 1 min
- Prefix count deviation >10% from baseline
- Interface errors/CRC increment
- BFD session flap rate
- QoS drop counters on PQ

Correlate with `site-reliability-engineer` SLIs where application paths cross backbone.

## Operational runbooks

Minimum runbook set:

| Scenario | Actions |
|---|---|
| Transit provider outage | Shift to alternate provider; verify prefix origination |
| IX port failure | Fail to backup cross-connect or transit |
| DCI link loss | Verify storage replication pause; IGP/BGP convergence |
| BGP prefix leak internal | Filter at RR; isolate source VRF |
| DDoS on public service | RTBH or scrubbing center diversion |
| Planned core upgrade | Drain via max-metric; verify ECMP shift |

Include **escalation** to carrier with circuit ID, LOA, and last-good config diff.

Store **topology and policy source of truth** in Git; tie to change tickets.

Review runbooks after **post-incident review**; feed architecture updates when recurring failures indicate design debt.
