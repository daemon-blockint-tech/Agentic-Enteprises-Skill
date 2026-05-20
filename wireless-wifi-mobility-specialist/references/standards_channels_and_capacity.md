# Standards, channels, and capacity

## Table of contents

1. [802.11 generations at architecture level](#80211-generations-at-architecture-level)
2. [Frequency bands and channel planning](#frequency-bands-and-channel-planning)
3. [Channel width and airtime tradeoffs](#channel-width-and-airtime-tradeoffs)
4. [Transmit power and cell sizing](#transmit-power-and-cell-sizing)
5. [DFS and regulatory domains](#dfs-and-regulatory-domains)
6. [Interference types and mitigation](#interference-types-and-mitigation)
7. [Wi-Fi 6/6E/7 feature selection](#wifi-66e7-feature-selection)
8. [Vendor-agnostic design patterns](#vendor-agnostic-design-patterns)

## 802.11 generations at architecture level

| Marketing | IEEE | Typical use | Architecture notes |
|---|---|---|---|
| Wi-Fi 5 | 802.11ac | Legacy enterprise | 5 GHz only wave-2; plan migration path |
| Wi-Fi 6 | 802.11ax | Current enterprise default | OFDMA, better dense efficiency; 2.4+5 |
| Wi-Fi 6E | 802.11ax + 6 GHz | Greenfield dense sites | Requires 6 GHz clients; country dependent |
| Wi-Fi 7 | 802.11be | Early adoption | Wider channels, MLO; verify client ecosystem |

Select generation based on **client mix**, **venue density**, **lifecycle** (5–7 year AP refresh), and **licensing cost**—not headline peak Mbps.

## Frequency bands and channel planning

| Band | Pros | Cons |
|---|---|---|
| 2.4 GHz | Range, legacy IoT | 3 non-overlapping 20 MHz channels; crowded; CCI |
| 5 GHz | More channels, higher throughput | Shorter range; DFS; some clients band-steer poorly |
| 6 GHz | Clean spectrum (where allowed) | Client/adoption; AFC outdoor rules (region-specific) |

**Channel planning principles:**

- Use **non-overlapping** 20 MHz channels as the baseline grid; widen only where benefit proven.
- Assign channels to minimize **co-channel** overlap between APs on same ESS.
- Group APs into **RF profiles** / **zones** (floor, building) for consistent channel plans.
- In multitenant buildings, document **external CCI** from neighbors; adjust channels or negotiate.

Example 5 GHz 20 MHz non-DFS set (region-dependent): 36, 40, 44, 48, 149, 153, 157, 161.

## Channel width and airtime tradeoffs

| Width | When to use | Risk |
|---|---|---|
| 20 MHz | High density, many APs, voice | Lower peak throughput per client |
| 40 MHz | Moderate density, fewer APs | Fewer independent channels; more CCI |
| 80/160 MHz | Low AP count, home-style | Poor enterprise density; often discouraged campus-wide |

Wi-Fi 6 **does not eliminate** channel planning—wider channels reduce planning flexibility.

**Preamble puncturing** (Wi-Fi 6/7) can help in partial interference scenarios—verify controller/AP support before relying on it in design docs.

## Transmit power and cell sizing

- Start from **minimum power that meets coverage/capacity** targets, not max EIRP.
- Align **TX power** with cell size; high power increases hidden nodes and sticky clients.
- Use **automatic power control** cautiously—validate it does not create roaming holes.
- Document **min/max power** per AP group (office vs atrium vs outdoor).

**Hidden node** symptoms: retries, asymmetric uplink/downlink, poor TCP performance despite good RSSI on one side.

## DFS and regulatory domains

**DFS channels** (5 GHz): radar detection required; AP may leave channel and clients disconnect briefly.

Design practices:

- Include **DFS channels** in plan where legal to expand capacity; monitor **DFS events** in operations.
- For **latency-sensitive voice**, consider avoiding primary operation on DFS-heavy plans if events are frequent in region.
- Set correct **country code** on controllers/APs—regulatory violation and client connectivity risk.

**6 GHz**: indoor low-power indoor (LPI) vs standard power with AFC outdoors—follow local rules for 6E deployment.

## Interference types and mitigation

| Type | Source | Mitigation |
|---|---|---|
| Co-channel (CCI) | own/other APs same channel | channel plan, power reduction, more APs lower power |
| Adjacent-channel | overlapping widths | use non-overlapping 20 MHz; avoid 40 MHz in dense RF |
| Non-Wi-Fi | microwave, Bluetooth, Zigbee, analog video | locate AP away; 5/6 GHz; shielding |
| Rogue AP | unauthorized SSID on corp VLAN | WIPS, rogue detection, switch port shutdown |
| Client misbehavior | hot-spot, USB tether | policy, NAC, education |

**SNR** matters more than RSSI alone: target SNR thresholds per application class (e.g., 25 dB+ for robust MCS).

## Wi-Fi 6/6E/7 feature selection

Features to evaluate at **architecture** level (vendor naming varies):

| Feature | Benefit | Design note |
|---|---|---|
| OFDMA | uplink/downlink efficiency in dense | needs compatible clients; not magic for all traffic |
| MU-MIMO | multiple spatial streams to clients | client must support; best with line-of-sight |
| BSS coloring | spatial reuse in dense | plan color assignments in RF groups |
| Target Wake Time (TWT) | IoT battery | IoT SSID strategy |
| 802.11ax on 6 GHz | clean high throughput | parallel SSID or band-specific SSID policies |
| MLO (Wi-Fi 7) | multi-link aggregation | early client support; phased rollout |

Do not enable every feature globally—**pilot** on one floor or RF profile first.

## Vendor-agnostic design patterns

Document design intent independent of vendor UI labels:

- **ESS** (extended service set) — same SSID across APs; roaming domain
- **RF group / zone** — shared channel and power policy
- **Minimum basic rate** — affects coverage footprint and legacy support
- **Band steering** — policy to move capable clients to 5/6 GHz
- **Airtime fairness** — reduce one client dominating medium

Conceptual vendor families (not endorsements):

- **Cisco** — WLC-based or Meraki cloud; CAPWAP, flexconnect/local switching
- **Aruba/HPE** — Mobility Conductor or Central; role-based policies
- **FortiAP** — integration with FortiGate security fabric
- **Others** — Ruckus, Extreme, Juniper Mist—same RF principles, different orchestration

Capture **handoff to operations**: firmware train, config backup, and license renewal dates in design package.
