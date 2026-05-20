# Tactical AI autonomy scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [Constraint capture](#constraint-capture)
3. [Platform classes](#platform-classes)
4. [Compute and deployment envelope](#compute-and-deployment-envelope)
5. [What good looks like](#what-good-looks-like)

## Role boundary

| Tactical autonomy developer owns | Others own |
|---|---|
| PPC integration, behavior design, fusion interfaces, autonomy safety rules | General LLM apps (`ai-engineer`) |
| HITL workflows, geofence/abort enforcement design, autonomy audit logs | LLM red team (`ai-redteam`) |
| Sim/field validation plans for autonomy behaviors | Safeguard serving infra (`ml-infrastructure-engineer-safeguards`) |
| Degraded modes for autonomy stack | Governance sign-off (`ai-risk-governance`) |
| ROS2/middleware patterns at architecture level | MCU drivers/RTOS only (`embedded-real-time-software-engineer`) |
| | Plant PLC/DCS apps (`control-software-developer`) |
| | HIL security benches (`hardware-in-the-loop-security-tester`) |
| | Adversarial ML campaigns (`ai-adversarial-robustness-engineer`) |

## Constraint capture

Document before design:

| Dimension | Questions |
|---|---|
| **Mission class** | Surveillance, logistics, inspection, training—operational not marketing labels |
| **Autonomy level** | Assisted vs supervised vs delegated; what remains human-only |
| **Latency** | Sense-to-act chain; control rate; planner horizon vs actuator bandwidth |
| **Safety intent** | Fail-safe vs fail-operational segments; geographic/temporal limits |
| **Environment** | GPS-denied segments, weather, EM interference, night/low light |
| **Comms** | LOS/BLOS, latency, jamming assumptions, store-and-forward |
| **Compute** | Edge SoC/GPU, thermal, power, ruggedization, air vs ground vs maritime |
| **Lifecycle** | OTA for models vs rules; rollback; config signing expectations |
| **Test** | SIL/HIL availability, range rules, logging for reconstruction |

## Platform classes

| Class | Typical autonomy concerns |
|---|---|
| **Small UAS** | Tight SWaP, vibration, fast dynamics, short planner horizons |
| **Fixed-wing / long endurance** | Energy management, sparse updates, BLOS comms degradation |
| **Ground /UGV** | Obstacle density, slip, lidar/radar mix, pedestrian proximity |
| **Maritime / USV** | GPS multipath, swell, COLREGS-style rule hooks at policy level |
| **Multi-agent** | Deconfliction, task allocation, shared world model consistency |

Keep customer-specific payloads and classified CONOPS out of generic skill outputs.

## Compute and deployment envelope

| Topic | Capture |
|---|---|
| **Partitioning** | Which nodes run perception vs planning vs control; isolation |
| **Real-time** | Hard vs soft deadlines per stage; watchdog coupling |
| **Models** | On-device inference limits; quantization; fallback symbolic layer |
| **Storage** | Log volume at mission rates; ring buffers vs offload |
| **Security** | Signed configs, key storage pattern—no exploit recipes |

## What good looks like

- One-page **autonomy boundary diagram** with rates, owners, and safety enforcement points
- Explicit **assumptions list** (GPS, comms, human availability) tied to degraded modes
- **Release criteria** linked to scenario IDs, not ad hoc demo flights alone
- Peer review hooks to embedded (timing), control (actuation limits), and AI safety (rules)
