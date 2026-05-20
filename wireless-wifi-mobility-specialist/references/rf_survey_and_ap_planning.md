# RF survey and AP planning

## Table of contents

1. [Survey types and when to use them](#survey-types-and-when-to-use-them)
2. [Pre-survey discovery](#pre-survey-discovery)
3. [Predictive modeling](#predictive-modeling)
4. [Active survey and validation](#active-survey-and-validation)
5. [AP placement heuristics](#ap-placement-heuristics)
6. [Antennas and mounting](#antennas-and-mounting)
7. [Capacity planning](#capacity-planning)
8. [Documentation and acceptance](#documentation-and-acceptance)

## Survey types and when to use them

| Method | Purpose | Best for |
|---|---|---|
| **Predictive (desktop)** | Model coverage from floor plans and material attenuation | Greenfield, budgetary AP count, design iterations |
| **Passive onsite** | Measure existing RF (neighbor APs, noise) without test SSID | Brownfield, interference assessment, audit |
| **Active onsite** | Associate to test SSID; measure SNR, throughput, roam | Pre/post deploy validation, troubleshooting |
| **AP-on-a-stick (APoS)** | Temporary AP at planned location | High-stakes venues, stadium, hospital wings |

Use **predictive + active validation** for most enterprise rollouts. APoS for high density or first deployment in complex RF environments.

## Pre-survey discovery

Collect before modeling:

- Floor plans with **scale** and **ceiling height**
- **Wall materials** (drywall, concrete, glass, metal studs, elevator shafts)
- **Existing APs** and neighbor networks (co-channel risk in multitenant buildings)
- **Metal inventory** — racks, conveyors, foil-backed insulation, LED lighting drivers
- **Outdoor coverage** requirements and cable paths
- **Restricted areas** — no ceiling mount, aesthetic limits, hazloc rules

Define **survey objectives** per zone:

- **Coverage** — minimum RSSI (e.g., -67 dBm for data, -65 dBm for voice)
- **Capacity** — Mbps per user or per m² at busy hour
- **Interference** — max co-channel overlap, noise floor targets

## Predictive modeling

Modeling workflow:

1. Import floor plan; set **scale** and **per-wall attenuation** (calibrate with spot measurements if possible).
2. Place **AP models** matching intended hardware (antenna gain, MIMO, band support).
3. Set **transmit power** within regulatory and design caps; avoid “max power everywhere.”
4. Review **heatmaps** per band: 2.4 GHz, 5 GHz, 6 GHz (if applicable).
5. Iterate AP count and positions until coverage and capacity targets met.

Common modeling mistakes:

- Ignoring **elevators and shafts** as RF blockers and reflection sources
- Using default wall loss for **warehouse** (underestimate open space, overestimate metal aisles)
- Placing APs only in **hallways** for room coverage (adjacent-room penetration varies)
- Forgetting **vertical bleed** between floors in multi-story buildings

## Active survey and validation

Post-deployment or APoS validation:

| Measurement | Tooling notes | Pass criteria (example) |
|---|---|---|
| RSSI / SNR | walk with survey app | meet zone minimum SNR |
| Primary/secondary coverage | note AP serving each point | no long zones below min RSSI |
| Co-channel interference | same-channel APs overlapping | CCI within design threshold |
| Throughput | iperf or vendor test | meets seat/area target at busy hour sample |
| Roam | voice or ping trail | <150 ms gap for voice SSID (environment-specific) |
| Retry rate | controller or survey | retries not persistently elevated |

Walk **all critical paths**: entrances, conference rooms, stairwells, loading docks, nurse stations, etc.

## AP placement heuristics

General placement rules:

- Prefer **ceiling mount** at center of coverage cell for omnidirectional patterns.
- In **corridors**, stagger APs on alternating sides to reduce down-corridor co-channel coupling.
- For **open offices**, grid APs for capacity; overlap at -67 to -72 dBm for roam, not -55 dBm everywhere.
- Avoid **physical obstructions** within 1 m of antenna (HVAC, metal beams, large AP clusters).
- **Elevator lobbies** often need dedicated AP; shafts attenuate but doors open frequently.
- **Restrooms and small rooms** may get adequate penetration; do not over-densify without need.

**Cell overlap**: enough for roam without excessive CCI. Voice often needs more overlap than best-effort data.

## Antennas and mounting

| Antenna type | Use case | Caution |
|---|---|---|
| Internal omni (default) | Standard office, classroom | Ceiling height affects pattern |
| Directional patch | Corridors, warehouse aisles, stadium sections | Aim carefully; back lobe |
| External omni | Outdoor pole, courtyard | Weather rating, lightning grounding |
| High-gain directional | point-to-point bridge | Fresnel zone, alignment, wind load |

Mounting:

- Document **height**, **orientation**, and **down-tilt** for directional installs.
- Use **appropriate hardware** for ceiling type (grid, hard lid, exposed deck).
- Plan **cable length** for external antennas; avoid excessive loss on long coax (prefer fiber + indoor AP).

## Capacity planning

Estimate **AP count from capacity**, not coverage alone:

```
Required Mbps per area ≈ users × Mbps_per_user × busy_hour_factor
AP airtime capacity ≈ effective_goodput_per_radio × radios_used
```

Factors:

- **Wi-Fi 6/7** improves efficiency (OFDMA, MU-MIMO) but does not remove physics in dense venues.
- **2.4 GHz** — limit use; often 3 non-overlapping channels; high CCI in dense sites.
- **5 GHz** — more channels; DFS adds channels but radar events cause moves.
- **6 GHz (6E)** — large clean spectrum where clients exist; plan 6 GHz-capable APs and clients.

High-density tactics:

- More **APs at lower power** vs few APs at high power
- **Disable 2.4** on selected AP radios where legacy not required
- **Band steering** toward 5/6 GHz
- **Multicast mitigation** for large lecture/stadium spaces

## Documentation and acceptance

Survey deliverables:

- Annotated **floor plans** with AP IDs, channels (post-survey), and mounting notes
- **Heatmaps** (RSSI/SNR/SNR) per band with legend and survey date
- **Interference report** — rogue/neighbor APs, noise sources, recommended mitigations
- **AP table** — model, name, MAC, IP, group, channel, power, VLAN uplink
- **Exceptions list** — areas below threshold with remediation plan

Acceptance sign-off should tie to **requirements doc** thresholds, not subjective “looks fine.”
