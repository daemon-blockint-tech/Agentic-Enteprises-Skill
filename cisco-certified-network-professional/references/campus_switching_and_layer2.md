# Campus switching and Layer 2

## Table of contents

1. [VLAN design](#vlan-design)
2. [Spanning Tree (STP/RSTP/MST)](#spanning-tree-stprstpmst)
3. [EtherChannel and physical design](#etherchannel-and-physical-design)
4. [Stacking and redundancy models](#stacking-and-redundancy-models)
5. [L2 security and hygiene](#l2-security-and-hygiene)
6. [Wireless integration touchpoints](#wireless-integration-touchpoints)
7. [Common failure patterns](#common-failure-patterns)
8. [Verification commands (IOS-XE)](#verification-commands-ios-xe)

## VLAN design

**Principles:**

- One **subnet per VLAN** at access; avoid stretching subnets across sites without documented L2 extension risk
- Separate **voice**, **guest**, **management**, and **user** VLANs by policy
- Keep VLAN count manageable; use **VRF-lite** at L3 edge when security zones need routing separation without VLAN sprawl

| VLAN type | Typical placement | Notes |
|---|---|---|
| User data | Access switch | 802.1X or MAB |
| Voice | Access + QoS trust | DSCP/CoS plan with `wan_edge_qos_and_services.md` |
| Guest | DMZ or isolated VRF | No route to corporate without firewall |
| Management | OOB or dedicated VRF | Restrict source ACLs |
| AP management | Local to WLC or Meraki | Document DHCP option 43 / discovery |

**Inter-VLAN routing:** prefer **distribution or core** as L3 gateway (router-on-a-stick only for small sites).

## Spanning Tree (STP/RSTP/MST)

**Default preference:** **RSTP** (rapid PVST+ or MST) with explicit root bridge placement.

**Root bridge plan:**

| Region | Root primary | Root secondary |
|---|---|---|
| Access block A | Distribution switch A | Distribution switch B |
| Building floor | Access stack master (if documented) | Alternate path via uplink |

**MST** when multiple VLAN groups need different forwarding:

- Instance 0: bulk data VLANs
- Instance 1: voice or critical VLANs (optional)
- Document **name**, **revision**, and **VLAN-to-instance** mapping in the runbook

**Port roles:**

- Edge ports: `spanning-tree portfast` + BPDU guard on access/host ports
- Uplinks: normal RSTP; no portfast toward switches
- Disable STP only with extreme justification (and loop risk acceptance)

**Alignment with FHRP:** STP root should live on the **same distribution switch** that owns active FHRP for that VLAN (see `wan_edge_qos_and_services.md`).

## EtherChannel and physical design

**LACP (preferred)** between access ↔ distribution and distribution ↔ core:

- Match speed, duplex, and MTU on member links
- Use **port-channel** consistent hashing; document critical flows if ECMP polarization matters
- **Mismatched configs** are a top cause of intermittent loss

**Design rules:**

- Dual homing access switches to **two** distribution switches when budget allows
- Avoid **vPC/MEC** complexity unless operations can support it; defer data-center MLAG depth to backbone peers

## Stacking and redundancy models

| Model | Use case | CCNP-level notes |
|---|---|---|
| **Stackwise / stacking** | Access or small distribution | Single control plane; plan stack master/replacement |
| **VSS / virtual switching** | Distribution pair | Reduces STP complexity; document split-brain recovery |
| **Traditional dual uplink** | Most campuses | STP + FHRP; well-understood ops |

**Stacking checklist:**

- Power diversity across members
- **Stack bandwidth** vs east-west load
- Hot spare or RMA process for member failure

## L2 security and hygiene

| Control | Purpose |
|---|---|
| **BPDU Guard** | Block rogue switches on access |
| **Root Guard** | Protect root placement on uplinks |
| **Loop Guard / UDLD** | Detect unidirectional links (where supported) |
| **DHCP Snooping** | Mitigate rogue DHCP on access VLANs |
| **Dynamic ARP Inspection** | Pair with DHCP snooping for user VLANs |
| **Storm control** | Limit broadcast/multicast storms |

**Private VLANs** — use sparingly; document promiscuous/isolated/community mapping.

## Wireless integration touchpoints

This skill does **not** replace `wireless-wifi-mobility-specialist` for RF design.

**L2/L3 boundaries to document:**

- AP VLAN vs client VLANs
- **FlexConnect/local mode** vs central switching (controller-dependent)
- mDNS/Bonjour gateway requirements
- Multicast for video (IGMP snooping, querier placement)

**Meraki:** VLANs and SSIDs mapped in dashboard; confirm **same subnet plan** as IOS-XE campuses.

## Common failure patterns

| Symptom | Often caused by |
|---|---|
| Intermittent connectivity | STP reconvergence, unidirectional link, port-channel mismatch |
| One VLAN works, others do not | VLAN trunk pruning, wrong SVI, FHRP mismatch |
| Slow roaming or one-way audio | QoS trust, wrong CoS/DSCP, oversized STP domain |
| Duplicate IP | Rogue DHCP, HSRP misconfiguration |

## Verification commands (IOS-XE)

Use as structured evidence during TSHOOT (not exhaustive):

```
show spanning-tree summary
show spanning-tree vlan <id>
show etherchannel summary
show interfaces trunk
show vlan brief
show mac address-table dynamic vlan <id>
show cdp neighbors detail
```

Capture **before/after** for change windows: STP root ID, port-channel state, trunk allowed VLANs.
