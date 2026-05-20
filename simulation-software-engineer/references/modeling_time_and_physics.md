# Modeling time and physics

## Table of contents

1. [Purpose](#purpose)
2. [Time management](#time-management)
3. [Integrators and stability](#integrators-and-stability)
4. [Coordinate frames](#coordinate-frames)
5. [Kinematics and dynamics patterns](#kinematics-and-dynamics-patterns)
6. [Contacts and constraints](#contacts-and-constraints)
7. [Stochastic elements](#stochastic-elements)
8. [Performance vs accuracy](#performance-vs-accuracy)
9. [Checklist](#checklist)

## Purpose

Guide **time-base selection** and **physics/kinematics modeling** for simulation software—stable integration, consistent frames, and explicit assumptions suitable for SIL/HIL and validation.

## Time management

### Discrete-event (DE)

- Maintain an **event queue** ordered by simulation time; advance clock to next event.
- State updates occur on **events** (arrivals, failures, mode switches, message delivery).
- Use when dynamics are **piecewise** or dominated by protocol/logic timing.

**Contracts to document:**

- Event ordering tie-break rules (priority, entity ID) for determinism
- Relationship to any CT subsystems (interpolation between events)

### Continuous-time (CT)

- Choose integrator and **fixed vs variable** step based on stiffness and real-time needs.
- Sub-step physics inside a **macro frame** when coupling to sensors or controllers at rate \(f_s\).

| Mode | When | Notes |
|---|---|---|
| Fixed step | Real-time HIL, deterministic replay | May need sub-stepping for stiff dynamics |
| Variable step | Offline accuracy, adaptive error control | Harder for strict bit-replay; log step choices |

### Hybrid coupling

- **Scheduler owns time**—either DE master with CT slaves, or CT master with DE interrupts.
- Define **zero-crossing / guard conditions** for mode switches (gear shift, contact engage).
- Avoid **hidden aliasing**—controller running at 100 Hz while physics integrates at 1 kHz without documented hold/interpolation.

## Integrators and stability

| Integrator class | Typical use | Caution |
|---|---|---|
| Euler / semi-implicit Euler | Games, simple rigs | Energy drift; instability on stiff springs |
| RK4 | Smooth offline motion | Not inherently stable for stiff contact |
| Implicit / stiff solvers | Contact, flexible elements | Cost; Jacobian quality |
| DAE solvers | Constrained mechanisms | Index reduction, consistent initialization |

**Stability practices:**

- Unit-test **energy/momentum drift** on conservative systems where applicable
- Document **maximum stable step** for real-time targets
- Separate **physics step** from **control step** with explicit upsampling/hold policy

## Coordinate frames

- Define a **frame tree**: world (ENU/NED), body, sensor mounts, articulation joints.
- State **rotation conventions** (quaternion order, Euler sequence) in API docs.
- Propagate **uncertainty** at frame boundaries when calibrating extrinsics.

**Common bugs:** left vs right-handed frames, NED vs ENU in aerospace, IMU frame vs body frame.

## Kinematics and dynamics patterns

| Pattern | Model | Typical parameters |
|---|---|---|
| Kinematic agents | Direct pose integration | Speed limits, curvature constraints |
| Rigid body 6-DOF | Newton–Euler or Lagrange | Mass, inertia, CG, aero coeffs (if used) |
| Wheeled vehicles | Bicycle / multi-track approximations | Wheelbase, slip, steering map |
| Articulated robots | Joint space + FK/IK | DH or URDF-like kinematics, limits |
| Simplified aero | Stability derivatives or lookup tables | Validated envelope; avoid extrapolation |

**Simulink-style workflows:** block-diagram plants with **algebraic loops** resolved explicitly; document solver settings and algebraic variable initialization.

## Contacts and constraints

- Prefer **stable contact models** (penalty with tuned damping, LCP-based) for repeatable regression.
- Document **friction, restitution, and solver iterations**; they affect determinism.
- For game engines, **physics engine settings** are part of the replay contract (solver iterations, CCD on/off).

## Stochastic elements

- Drive randomness from **named RNG streams** per subsystem (environment, sensor, traffic).
- Never mix **unseeded** thread-local random in deterministic suites.
- Log **stream IDs and seeds** in replay headers.

## Performance vs accuracy

| Technique | Benefit | Cost |
|---|---|---|
| Sub-stepping only stiff subsystems | Stability in real-time | Complexity |
| LOD for distant actors | Throughput | Behavioral error |
| Tabulated aero vs online solve | Speed | Prep and envelope limits |
| GPU batching for ray-based sensors | Throughput | Determinism care |

## Checklist

- [ ] Master clock and all sub-clocks documented
- [ ] Integrator choice justified for stiffness and real-time mode
- [ ] Frame tree diagram and conventions published
- [ ] Contact/solver settings pinned for regression
- [ ] RNG streams and seeds specified per stochastic module
- [ ] Units enforced (SI) at module boundaries
