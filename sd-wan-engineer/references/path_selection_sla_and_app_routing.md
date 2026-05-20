# Path selection, SLA, and application routing

## Table of contents

1. [Policy model](#policy-model)
2. [SLA classes](#sla-classes)
3. [Path selection mechanics](#path-selection-mechanics)
4. [Application-aware routing](#application-aware-routing)
5. [DPI and identification caveats](#dpi-and-identification-caveats)
6. [WAN optimization concepts](#wan-optimization-concepts)
7. [QoS and DSCP](#qos-and-dscp)
8. [Testing and validation](#testing-and-validation)

## Policy model

SD-WAN policy typically stacks:

1. **Centralized business policy** — who talks to whom (topology), default action
2. **SLA / performance policy** — which underlays satisfy latency, loss, jitter
3. **Application policy** — match apps to SLA classes and breakout
4. **Security policy** — firewall, IPS, URL filtering (often paired with SASE)

Keep policies **composable**: site overrides only where justified; document exceptions.

## SLA classes

Define a small set of **SLA classes** (3–6) rather than per-app tunnels:

| Class | Typical metrics | Underlay preference |
|---|---|---|
| **Realtime** | Latency, jitter, loss | MPLS or best low-jitter path; fast failover |
| **Business-critical** | Latency + loss | Prefer stable paths; limited fallback to broadband |
| **Standard** | Throughput + loss | ECMP across acceptable underlays |
| **Bulk** | Throughput | Broadband; deprioritize on congestion |
| **Default** | Best effort | Any available underlay |

Per class, specify:

- **Measurement interval** and **probe type** (BFD, IP SLA, synthetic HTTP)
- **Failover threshold** (e.g., loss > 2% for 3 intervals)
- **Stickiness** duration (avoid flapping)
- **Backup** order when primary underlay fails

**Path selection** should be deterministic for operations—avoid opaque “AI routing” without exported logic.

## Path selection mechanics

| Mechanism | Purpose |
|---|---|
| **BFD / fast hello** | Sub-second underlay failure detection |
| **Tunnel health** | Overlay keepalives independent of routing protocol |
| **Application-aware reroute** | Move flows when SLA violated (vendor-specific session handling) |
| **Weighted load-sharing** | Spread bulk across multiple underlays |
| **Conditional pinning** | Force MPLS for regulated apps |

Document **asymmetric paths** (different forward/return underlay) when allowed and when blocked.

## Application-aware routing

**Application-aware routing** maps identified traffic to SLA classes and breakout:

| Identification method | Pros | Cons |
|---|---|---|
| **Port/protocol** | Simple | Ambiguous (443 everything) |
| **FQDN / SaaS database** | Good for cloud apps | Requires updates; split-DNS interactions |
| **IP ranges** | Stable for DC apps | Churn in SaaS IPs |
| **DPI / L7 signature** | Granular | CPU cost; encryption limits visibility |
| **User-group / ZTNA** | Identity-aware | Needs IdP integration |

Build an **application catalog**:

| App | Category | SLA class | Breakout (local / hub / SASE) |
|---|---|---|---|
| Microsoft 365 | SaaS | Standard | Local or regional SASE PoP |
| ERP | Private DC | Business-critical | Hub or DC |
| VoIP | Realtime | Realtime | Local or regional gateway |

## DPI and identification caveats

- **Encrypted traffic** (TLS 1.3, QUIC) reduces DPI fidelity—prefer domain/SaaS lists and endpoint agents where required
- **Split tunnel vs full tunnel** changes what CPE inspects
- **DNS** misconfiguration causes wrong breakout (internal resolver vs public)
- **Custom ports** need explicit rules—do not rely on default web classification

## WAN optimization concepts

**WAN optimization** in SD-WAN context may include:

- **TCP optimization** (window scaling, retransmission handling)—verify benefit on modern high-BW links
- **Deduplication / compression**—often retired for encrypted SaaS; still relevant for replication to DC
- **Protocol-specific proxies** (CIFS, etc.)—legacy; prefer app modernization

When user mentions **WAN optimization**, clarify whether they mean:

1. Legacy WAN accel appliances → migration to app-aware routing + adequate bandwidth
2. SD-WAN **performance features** (FEC, packet duplication for lossy links)
3. **SaaS acceleration** via SASE PoP proximity

## QoS and DSCP

| Layer | Guidance |
|---|---|
| **LAN QoS** | Mark at switch/AP if trust model extends to CPE |
| **Overlay QoS** | Map SLA classes to tunnel queues |
| **Underlay QoS** | MPLS COS / DSCP honored only if end-to-end contract exists |

If provider does not honor DSCP on broadband, do not assume end-to-end QoS—use **path selection** instead.

## Testing and validation

| Test | Pass criteria |
|---|---|
| Primary underlay fail | Failover within SLA class timer; minimal session drop |
| Brownout (5–10% loss) | Reroute or FEC engages per design |
| App policy | Identified app uses intended hub/breakout |
| Throughput | Achieve contracted Mbps minus overlay overhead |
| VoIP/UDP | Jitter within spec on failover |

Record baseline **overlay vs underlay** metrics before production cutover.
