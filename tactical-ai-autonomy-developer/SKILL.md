---
name: tactical-ai-autonomy-developer
description: |
  Guides edge and tactical autonomous systems—perception-planning-control under latency and safety
  constraints; behavior trees/state machines vs learned policies; human-on-the-loop; geofencing,
  no-strike rules, mission abort; sim and field testing; ROS2/middleware patterns; sensor fusion;
  degraded modes; autonomy audit logging. Use for UAS/autonomous stacks, safety rules, HITL,
  sim-to-field validation, fail-safe—not LLM products (ai-engineer), LLM red team (ai-redteam),
  safeguard serving (ml-infrastructure-engineer-safeguards), governance only (ai-risk-governance),
  MCU firmware without autonomy (embedded-real-time-software-engineer), plant PLC/DCS
  (control-software-developer), HIL security bench (hardware-in-the-loop-security-tester).
---

# Tactical AI & Autonomy Developer

## When to Use

- Integrate **perception, planning, and control** on edge compute with end-to-end latency and safety budgets
- Choose **behavior representation**—behavior trees, state machines, hybrid symbolic + learned policies
- Define **human-on-the-loop** workflows—monitoring, intervention, escalation, and handoff semantics
- Specify **operational constraints**—geofences, no-strike / keep-out rules, mission abort, ROE hooks
- Design **sensor fusion** and world-model interfaces—time sync, calibration, uncertainty propagation
- Plan **simulation and field validation**—SIL/HIL concepts, scenario suites, regression gates
- Engineer **degraded modes**—sensor loss, comms loss, compute derating, fail-safe and hold patterns
- Implement **autonomy audit logging**—decision traces, rule firings, model versions, override events
- Coordinate **middleware**—ROS2-style pub/sub, services, lifecycle nodes at pattern level (not distro pick)
- Align with **embedded**, **control**, and **AI safety** peers on interfaces and acceptance criteria

## When NOT to Use

- **General LLM/RAG products**, chat agents, or cloud inference features → `ai-engineer`
- **LLM jailbreak / app red team** engagements and ROE → `ai-redteam`
- **Safeguard gateway serving**, GPU routing, moderation infra SLOs → `ml-infrastructure-engineer-safeguards`
- **AI governance**, risk tiers, model cards, compliance mapping only → `ai-risk-governance`
- **Bare-metal MCU firmware**, ISR/RTOS, drivers without autonomy stack → `embedded-real-time-software-engineer` (unless autonomy runs on that edge target)
- **Plant PLC/DCS**, historian, OT scan cycles, Modbus/DNP3 plant logic → `control-software-developer`
- **HIL security bench**, bus fault injection, authorized exploitation on rigs → `hardware-in-the-loop-security-tester`
- **Adversarial ML robustness** (evasion/poison on models in lab) → `ai-adversarial-robustness-engineer`
- **Export-controlled weapon design detail** or customer-specific classified architectures → legal / program office; keep outputs generic

## Related skills

| Need | Skill |
|---|---|
| Production LLM/RAG and agent features | `ai-engineer` |
| LLM red team and jailbreak policy | `ai-redteam` |
| Safeguard serving and inference platform | `ml-infrastructure-engineer-safeguards` |
| Governance, risk tiers, model cards | `ai-risk-governance` |
| MCU/RTOS, drivers, WCET on chip | `embedded-real-time-software-engineer` |
| PLC/DCS, OT protocols, plant control apps | `control-software-developer` |
| HIL security assessment on benches | `hardware-in-the-loop-security-tester` |
| Adversarial robustness on ML models | `ai-adversarial-robustness-engineer` |

## Core Workflows

### 1. Scope and platform constraints

Capture mission class, latency chain, safety intent, compute envelope, and test environments before stack design.

**See `references/tactical_ai_autonomy_scope.md`.**

### 2. Perception–planning–control stack

Partition pipelines, interfaces, timing, and responsibility between learned and symbolic components.

**See `references/perception_planning_control_stack.md`.**

### 3. Safety, rules, and human oversight

Define geofencing, constraint rules, HITL escalation, and abort semantics with traceable enforcement points.

**See `references/safety_human_oversight_and_rules.md`.**

### 4. Simulation and validation

Build scenario matrices, sim-to-real gaps, metrics, and release gates from SIL through limited field trials.

**See `references/simulation_testing_and_validation.md`.**

### 5. Degraded modes and fail-safe

Specify detection, transitions, and safe outcomes for sensor, comms, and compute failures.

**See `references/degraded_modes_and_fail_safe.md`.**

### 6. Deployment, logging, and audit

Plan edge deployment, OTA boundaries, structured autonomy logs, and post-incident reconstruction.

**See `references/deployment_logging_and_audit.md`.**

## Outputs

- **Autonomy architecture brief** — PPC boundaries, rates, compute map, middleware topology
- **Behavior spec** — states/modes, BT or policy outline, preconditions and timeouts
- **Safety rules pack** — geofences, constraints, abort triggers, enforcement layer mapping
- **HITL playbook** — roles, UI cues, override logging, escalation paths
- **Validation plan** — scenarios, metrics, pass/fail gates, sim vs field phases
- **Degraded-mode matrix** — triggers, transitions, safe states, recovery rules
- **Audit schema** — fields per decision cycle, retention, correlation IDs

## Principles

- **Safety before capability** — prove constraint enforcement and abort paths before expanding autonomy
- **Traceable decisions** — every safety-critical branch logs rule ID, inputs hash, and outcome
- **Deterministic fallbacks** — symbolic safe modes when learned components are uncertain or unavailable
- **Measured latency** — budget per stage; no stack design without end-to-end timing evidence
- **Sim ≠ field** — document sim assumptions; require field scenarios for release-critical behaviors
- **Generic documentation** — UAS/autonomous systems terms only; no named customers or controlled technical dumps
