# Operations, troubleshooting, and integration

## Table of contents

1. [WLAN operations model](#wlan-operations-model)
2. [Integration with wired LAN](#integration-with-wired-lan)
3. [SD-WAN and edge integration](#sd-wan-and-edge-integration)
4. [Monitoring and telemetry](#monitoring-and-telemetry)
5. [Troubleshooting methodology](#troubleshooting-methodology)
6. [Common failure patterns](#common-failure-patterns)
7. [Change management and lifecycle](#change-management-and-lifecycle)
8. [Runbook templates](#runbook-templates)

## WLAN operations model

| Model | Characteristics | Ops focus |
|---|---|---|
| On-prem controller | WLC, Mobility Conductor, virtual appliance | HA pairs, upgrades, CAPWAP reachability |
| Cloud-managed | Meraki, Aruba Central, Mist | dashboard RBAC, template drift, internet dependency |
| Distributed / controllerless | cluster of smart APs | quorum, cluster split-brain procedures |

Define **roles**: RF engineering, network operations, security (NAC), and field services for AP hardware.

**Golden templates** — SSID, RF, and security policies pushed from templates; avoid one-off AP configs.

## Integration with wired LAN

Access layer checklist:

| Element | Wireless dependency |
|---|---|
| PoE | 802.3at/bt for 4x4 APs; budget per stack |
| Switchport | trunk with allowed VLANs; native VLAN discipline |
| STP | edge port fast; avoid STP on AP ports where possible |
| DHCP | scopes per WLAN VLAN; option 43/60 for controller discovery if used |
| DNS | internal resolvers; guest DNS filtering |
| MTU | jumbo not required; watch tunnel overhead if central switching |
| ACL / microseg | per-VLAN policy at firewall or switch |

**FlexConnect / local mode** — document which VLANs terminate locally vs at controller DC.

Handoff to `infrastructure-engineer` for **rack, power, and cabling**; to `network-backbone-architect` for **routing and core QoS**.

## SD-WAN and edge integration

Branch wireless often shares **internet breakout** with SD-WAN:

| Scenario | Design note |
|---|---|
| Guest traffic local breakout | guest VLAN exits branch firewall; ACL internet-only |
| Corp traffic hubbed | corp WLAN VLAN backhauled; latency affects app experience |
| Voice | prefer **local internet** or **regional** path; QoS on underlay |
| Split tunnel | align WLAN VLAN policy with SD-WAN interest lists |

Coordinate with `sd-wan-engineer` for:

- **Application routes** for SaaS used heavily over Wi-Fi
- **SLA classes** for real-time traffic from wireless VLANs
- **Failover** when broadband fails—guest may stay up while corp tunnels down

Do not redesign **overlay path selection** in this skill—document **requirements** and interfaces.

## Monitoring and telemetry

Sources:

- **Controller/cloud** — client events, roam, auth failures, RF metrics
- **SNMP** — AP radio stats where supported
- **Syslog** — auth, rogue, config change
- **NetFlow/IPFIX** — per-VLAN traffic (wired side)
- **Synthetic tests** — dedicated test client or sensor (optional)

Dashboards (examples):

- AP **up/down**, **channel utilization**, **retry %**
- **Top noisy APs/clients**
- **802.1X failure** rate and RADIUS latency
- **DFS** event count by site
- **Ticket correlation** — WLAN issues vs WAN outage

Alert hygiene:

- Alert on **sustained** thresholds, not single spikes
- Separate **RF** alerts from **auth** alerts from **WAN** alerts

Handoff to `site-reliability-engineer` when defining **SLOs** and error budgets for digital workplace services.

## Troubleshooting methodology

Structured flow:

1. **Scope** — one user, one floor, one site, or global?
2. **Correlate time** — change window, firmware, RADIUS cert, DFS event
3. **Layer** — physical (PoE), association, auth, IP, app, path
4. **Client vs infrastructure** — reproduce with second device; check driver
5. **RF vs wired** — compare on Wi-Fi vs wired same VLAN

Data to collect:

- Client **MAC**, AP name, **BSSID**, channel, **RSSI/SNR**
- **Connection phase** — assoc, 4-way, 802.1X, DHCP
- **Retry rate**, **data rate**, **roam history**
- Switch port **errors**, **PoE** status

## Common failure patterns

| Symptom | Likely causes | Checks |
|---|---|---|
| Cannot see SSID | AP down, wrong regulatory domain, RF disabled | AP status, country code |
| Assoc but no IP | DHCP scope, VLAN mismatch, ACL | DHCP logs, VLAN on AP port |
| 802.1X fail | cert, RADIUS, clock, wrong EAP | RADIUS logs, supplicant config |
| Slow throughput | CCI, hidden node, low SNR, WAN | channel plan, SNR, iperf wired vs Wi-Fi |
| Frequent disconnect | DFS, driver, min RSSI aggressive, PoE flap | DFS log, power, event log |
| Roam drops voice | no 11r, sticky, wrong VLAN | FT config, roam trace |
| Site-wide outage | controller reachability, WAN, DNS | CAPWAP, tunnel, SD-WAN status |
| Guest portal loop | DNS, cert, firewall | DNS resolution, redirect URL |

**SNR vs RSSI:**

- RSSI — received power
- SNR — RSSI minus noise floor; low SNR → low MCS and high retries

**DFS:** clients drop when AP moves channel—check radar detection logs; adjust channel plan.

**Co-channel / adjacent-channel:** retries rise without obvious low RSSI—review channel overlap map.

## Change management and lifecycle

| Activity | Practice |
|---|---|
| Firmware upgrade | staged: lab → pilot floor → site → global |
| Config change | template diff; rollback snapshot |
| AP replacement | RMA process; spare stock by model |
| License | true-up before expansion; expiration alarms |
| Survey refresh | major renovation or tenant change in building |

Document **maintenance windows** for channel changes (brief disconnect) and controller failover tests.

## Runbook templates

**Single client cannot connect (corp SSID)**

1. Verify SSID visible; compare with known-good client
2. Check 802.1X cert and EAP type; review RADIUS accept/reject
3. Confirm VLAN and DHCP scope
4. If isolated to one AP, check RF and AP logs for disassoc reason

**Floor-wide slow Wi-Fi**

1. Check AP up count vs expected
2. Review channel utilization and retry heatmap
3. Identify new interference or neighbor AP
4. Verify uplink congestion on access switches
5. Check WAN/SD-WAN if apps are cloud-hosted

**AP flapping / offline**

1. PoE budget and port errors
2. Cable/link (negotiation 1G vs 100M)
3. CAPWAP/tunnel to controller; firewall UDP/TCP paths
4. Replace hardware if physical layer failed

**Post-DFS event**

1. Identify affected channel and APs
2. Confirm clients reassociated
3. If recurring, exclude problematic DFS channel in plan

Export runbooks to NOC wiki with **vendor-specific click paths** as appendix—not in architecture docs.
