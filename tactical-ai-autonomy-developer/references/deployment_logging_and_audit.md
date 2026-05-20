# Deployment, logging, and audit

## Table of contents

1. [Edge deployment](#edge-deployment)
2. [Configuration and OTA](#configuration-and-ota)
3. [Autonomy decision logging](#autonomy-decision-logging)
4. [Audit and reconstruction](#audit-and-reconstruction)
5. [Privacy and retention](#privacy-and-retention)
6. [Incident handoff](#incident-handoff)

## Edge deployment

| Topic | Capture |
|---|---|
| **Topology** | On-vehicle compute vs ground relay; what runs where |
| **Containers vs bare** | Process isolation; restart policy |
| **Resources** | CPU/GPU affinity for perception; deterministic cores for control |
| **Startup order** | Lifecycle: sensors → estimators → planner → arming gates |
| **Secrets** | Key storage pattern; no keys in logs |

Align image versions with **model hash**, **rules version**, and **map/geofence version** in manifest.

## Configuration and OTA

| Artifact | Versioned |
|---|---|
| Behavior trees / state machines | Yes |
| Safety rules / geofences | Yes, signed |
| Neural nets / calibrations | Yes, with eval report ID |
| Mission files | Per sortie ID |

OTA plan: staged rollout, **rollback image**, canary vehicles, compatibility matrix between stack components.

## Autonomy decision logging

Minimum structured fields per control cycle or planner tick (adjust rate):

| Field | Purpose |
|---|---|
| `timestamp` | Monotonic + UTC if available |
| `mission_id` / `sortie_id` | Correlation |
| `mode` | AUTONOMOUS, DEGRADED, etc. |
| `rules_evaluated` | Rule IDs + pass/fail |
| `planner_output_hash` | Waypoint/command fingerprint |
| `safety_veto` | If monitor modified command |
| `estimator_quality` | Health flags |
| `model_versions` | Perception/planner artifacts |
| `operator_override` | Boolean + channel |

Use **append-only** storage on vehicle; offload post-mission with integrity check (hash chain optional).

## Audit and reconstruction

| Use case | Required artifacts |
|---|---|
| **Rules dispute** | Rule ID, inputs snapshot, geofence version |
| **Unexpected maneuver** | Trajectory log + mode timeline |
| **Post-incident review** | Full bag + autonomy trace + config manifest |

Build a **replay toolchain** that feeds logged inputs through offline stack for diff (same versions pinned).

## Privacy and retention

- Avoid logging **unnecessary PII** or imagery beyond program policy
- Define retention TTL per environment (lab vs operational)
- Redact or crop sensors in exports when sharing outside program

## Incident handoff

Package for investigators:

1. Config manifest (all versions)
2. Autonomy trace + raw sensor bag (if authorized)
3. Scenario ID if test; ODD statement if ops
4. Known software issues / open defects

Route **security incidents** on comms/compromise to cybersecurity peers; **model safety** policy breaches to `ai-risk-governance` / safeguards as appropriate.

Do not include export-controlled performance parameters or customer-identifying metadata in generic skill outputs.
