# Roaming, density, and performance

## Table of contents

1. [Roaming fundamentals](#roaming-fundamentals)
2. [802.11k, 11r, and 11v](#80211k-11r-and-11v)
3. [Band steering and client steering](#band-steering-and-client-steering)
4. [Sticky clients and mitigation](#sticky-clients-and-mitigation)
5. [High-density venue design](#high-density-venue-design)
6. [Voice and real-time traffic](#voice-and-real-time-traffic)
7. [Mesh and outdoor mobility](#mesh-and-outdoor-mobility)
8. [Performance testing and KPIs](#performance-testing-and-kpis)

## Roaming fundamentals

Roaming occurs when a client **reassociates** to a new AP while keeping L3 continuity (same subnet) or tolerating brief disruption.

| Roam type | Layer | User impact |
|---|---|---|
| L2 roam (same subnet) | fast if same SSID/VLAN | minimal if 11r or good drivers |
| L3 roam (subnet change) | requires mobile IP or app retry | noticeable for some apps |
| Inter-controller roam | tunnel or session handoff | depends on vendor fast roam |

Design for **L2 roaming domains** per SSID/VLAN within a site unless centralized L3 mobility (e.g., L3 roam anchors) is explicitly architected.

**Key metrics:**

- **Roam time** — association + auth (802.1X full reauth is slower than 11r key cache)
- **Packet loss** during roam — voice tolerates <150 ms gap (environment-specific)
- **Sticky duration** — time client holds weak AP before roam

## 802.11k, 11r, and 11v

| Standard | Name | Purpose |
|---|---|---|
| 802.11k | RRM | neighbor reports; faster AP selection |
| 802.11r | FT | fast BSS transition; cached keys |
| 802.11v | WNM | BSS transition management; disassoc guidance |

**802.11r (FT):**

- Reduces roam time for **802.1X** by pre-authenticating keys
- Requires **same mobility domain** on controller; SSID must enable FT
- Test **all client types**—some IoT and older phones break with FT enabled

**802.11k:**

- AP provides **neighbor list**; client makes better roam decisions
- Enable with 11v on dense campuses

**802.11v:**

- Network-assisted **BSS transition**; helps move clients off overloaded AP
- Use with **load balancing** and **band steering** carefully to avoid roam storms

## Band steering and client steering

**Band steering** — encourage dual-band clients to use 5 GHz or 6 GHz:

- Probe suppression or preference on 2.4 GHz
- Client **capability** checks before steer
- Monitor **steer failures** (client stays on 2.4)

**Client steering / load balancing** — move clients between APs on same band:

- Thresholds: **client count**, **utilization**, **SNR**
- Avoid aggressive steering causing **ping-pong** roams

Best practices:

- Pilot steering on one floor; watch **retry rates** and **helpdesk tickets**
- For **voice SSID**, conservative steering—stability over utilization
- Document **exceptions** for known-bad clients (allowlist 2.4 only)

## Sticky clients and mitigation

Sticky clients stay on a distant AP despite better neighbors—causes low throughput and CCI for others.

Mitigations:

| Technique | Effect |
|---|---|
| Minimum RSSI / disassoc | kick weak clients; risk brief disconnect |
| 802.11v BSS transition | guided roam to better AP |
| Adjust cell size (lower TX power) | smaller cells; more frequent natural roams |
| Client driver updates | fix vendor roam bugs |
| Separate SSID for problematic devices | isolate impact |

Set **min RSSI** per SSID/AP group—not globally maximum without validation.

## High-density venue design

Venues: stadium, arena, lecture hall, conference center, warehouse peak shifts.

Tactics:

- **High AP count**, **low power**, **narrow cells**
- **Directional antennas** for seating bowls; sectorization
- **Split bands** — dedicated 5 GHz and 6 GHz plans; limit 2.4 to legacy pockets
- **Disable low rates** (basic rate sets) where safe—reduces airtime waste
- **Multicast-to-unicast** for broadcast-heavy apps
- **DHCP and DNS** scale—short lease times; anycast DNS
- **Controller clustering** and **AP limits** per RF group

Capacity checklist:

- Model **peak concurrent clients** per AP/seat section
- Plan **uplink** (2.5G/5G/10G) per AP; avoid oversubscribed access switches
- **Airtime utilization** alarms per AP (typically investigate sustained >60–70%)

Healthcare and warehouse variants:

- **Healthcare** — roaming for carts and voice; minimize channel changes during DFS
- **Warehouse** — metal racks; plan for **aisle coverage**; scanner roam testing at rack ends

## Voice and real-time traffic

Wi-Fi voice (VoWLAN) requirements:

- Dedicated **voice SSID** with QoS (**WMM** UP queues)
- **802.11r** where supported by handsets
- **Consistent codec** and CAC on wired side
- **QoS trust** end-to-end—DSCP honored on switches if wired QoS used

VDI and video conferencing:

- Prefer **5/6 GHz**; adequate **SNR**; avoid hidden node in open offices
- Wired **QoS** or SD-WAN classes for egress—coordinate with `sd-wan-engineer`

## Mesh and outdoor mobility

**Mesh** (where offered):

- **Half-duplex** mesh backhaul reduces capacity—prefer **wired backhaul** when possible
- Hop count limits (typically ≤2–3 for production)
- **Outdoor mesh** — power, lightning, pole rights, and **line of sight**

**Outdoor bridging:**

- Point-to-point **5 GHz** links; align antennas; monitor **fade** from weather
- Regulatory **EIRP** and **licensing** for long links

Mobility across outdoor **campus** APs:

- Overlap at **building entrances** for seamless handoff indoor/outdoor
- Tune **min RSSI** at perimeter to encourage indoor AP when inside

## Performance testing and KPIs

Test scenarios:

| Test | Tool/method | Pass example |
|---|---|---|
| Association time | controller logs | within org standard |
| Roam trail | ping + walk | voice SSID gap within target |
| Throughput | iperf3 multi-thread | per-area Mbps target |
| Density soak | many clients iperf | no collapse at target load |
| Multicast | stream to group | acceptable loss with conversion |

Operational KPIs (monitor continuously):

- **Retry rate** (%), **channel utilization**, **noise floor**
- **Client count** per AP, **sticky client** reports
- **DFS events**, **radar detected** channel moves
- **Auth failures** (802.1X), **RADIUS latency**
- **AP uptime**, **capwap/tunnel** status

Escalation thresholds should be **baseline-relative** (compare to same hour prior week).
