# Safety, human oversight, and rules

## Table of contents

1. [Operational design domain](#operational-design-domain)
2. [Constraint rules](#constraint-rules)
3. [Human-on-the-loop](#human-on-the-loop)
4. [Mission abort and escalation](#mission-abort-and-enforcement)
5. [Enforcement architecture](#enforcement-architecture)
6. [Coordination with AI safety](#coordination-with-ai-safety)

## Operational design domain

Define where autonomy may run:

| Element | Specify |
|---|---|
| **Geography** | Geofences, altitude bands, distance from structures/people |
| **Time** | Mission windows, lighting minima |
| **Speed / energy** | Caps by mode |
| **Payload / task** | Allowed behaviors per configuration |
| **Comms** | Minimum link quality for delegated autonomy |

Exit ODD → automatic degrade, hold, or RTL (return-to-launch) per program policy.

## Constraint rules

| Rule type | Examples (generic) |
|---|---|
| **Keep-out** | Airspace volumes, land zones, maritime exclusion |
| **No-strike / no-engage** | Prohibited target classes or regions (policy-defined) |
| **Proximity** | Standoff from structures, formations, friendly tracks |
| **Kinematic** | Max bank, climb, turn rate, descent |
| **Mission** | Waypoint order, loiter limits, fuel/battery reserves |

Each rule needs: **ID**, **inputs**, **predicate**, **action** (deny, clamp, abort), **priority**, **log event**.

## Human-on-the-loop

| Mode | Human role | System obligation |
|---|---|---|
| **Monitoring** | Observe; intervene if needed | Clear state/alert UX; low false-alarm rate |
| **Approval** | Authorize segment or weapon-adjacent action | Timeout → deny or hold |
| **Shared control** | Blending inputs | Explicit authority (who wins on conflict) |
| **Override** | Take manual control | Log override; smooth bumpless transfer |

Capture **latency** from operator action to effect; train on injected faults in sim.

## Mission abort and enforcement

| Trigger class | Typical response |
|---|---|
| **Operator abort** | Immediate mode change; RTL or land-in-place |
| **Rules violation** | Clamp command or abort subtree |
| **Watchdog / heartbeat** | Safe hold if planner or comms silent |
| **Estimator fault** | Degrade perception trust; reduce speed or exit autonomy |
| **Battery / fuel** | Forced RTB per reserves table |

Abort paths must be **tested** in sim and field with recorded traces.

## Enforcement architecture

Prefer **multiple layers**:

1. **Planner constraints** — soft costs, replanning
2. **Safety monitor** — independent check on proposed command (symbolic)
3. **Control limits** — saturations, rate limiters
4. **Hardware** — estop, mechanical limits (outside software skill scope but referenced)

Safety monitor should run at **control rate** or faster than planner commits irreversible actions.

## Coordination with AI safety

| Handoff | Tactical autonomy provides | AI safety / governance provides |
|---|---|---|
| **Rule set versioning** | IDs, tests, sim evidence | Approval workflow, change control |
| **Model updates** | Hash, dataset lineage, eval slice | Release policy, risk tier |
| **Incidents** | Decision trace package | Investigation template, reporting |

Do not conflate **operational rules** with **LLM content policies**—different stacks, may coexist on same platform.
