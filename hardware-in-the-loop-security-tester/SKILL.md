---
name: hardware-in-the-loop-security-tester
description: |
  Guides security assessment of embedded and cyber-physical systems on hardware-in-the-loop
  (HIL) test benches—bench setup, ECU/ECM or PLC targets, bus interfaces (CAN/CAN-FD, LIN,
  automotive Ethernet, Modbus at high level), fault injection and stimulus design, simulated
  plant/environment integration, attack-surface monitoring on real hardware, reproducible test
  cases, lab safety interlocks, and evidence capture for firmware and vehicle security teams.
  Use for HIL security testing, ECU security assessment, CAN bus security, PLC HIL test, fault
  injection lab, embedded hardware security—not web/API pentest (web-pentester), network-only
  pentest (network-pentester), malware/binary RE only (reverse-engineer), SOC operations
  (soc-analyst), AI red team (ai-redteam), classified ISSO paperwork
  (information-systems-security-officer-classified-specialist), or pure software CI without
  hardware (build-validator).
---

# Hardware-in-the-Loop (HIL) Security Tester

## When to Use

- Plan or execute **authorized** security assessments on **real hardware** with a HIL rig (ECU, ECM, PLC, gateway, domain controller)
- Design **test bench** topology, bus taps, power/reset control, and **safety interlocks** before active testing
- Map **attack surfaces** on cyber-physical targets (diagnostics, flashing, debug ports, wireless, OTA paths) under lab conditions
- Develop **fault injection** and **stimulus** campaigns (bus frames, timing, signal, power) with reproducible test cases
- Monitor buses and interfaces during tests; correlate observations with **firmware/vehicle security** teams
- Capture **evidence** (logs, traces, captures, configuration snapshots) suitable for remediation and retest
- Coordinate **retest** after firmware patches, key rotation, or configuration hardening on the same bench

## When NOT to Use

- **Web application or API-only** assessments (OWASP, proxy methodology) → `web-pentester`
- **Network/AD/infra pentest** without embedded targets on the bench → `network-pentester`
- **General penetration test** without HIL hardware, buses, or plant simulation → `penetration-tester`
- **Disassembly, decompilation, patch diff, or malware RE** as primary work → `reverse-engineer`
- **SIEM alert triage**, SOC playbooks, or shift operations → `soc-analyst`
- **Live incident command**, war room, or production containment → `incident-responder`
- **LLM jailbreak**, prompt injection, or agent tool abuse → `ai-redteam`
- **Classified ISSO / accreditation paperwork** without hands-on HIL testing → `information-systems-security-officer-classified-specialist`
- **CI build validation** or release gates without hardware under test → `build-validator`
- **Enterprise security strategy, GRC roadmap, or policy** without lab execution → `cybersecurity`
- **Control testing and audit evidence** mapping only (no active HIL tests) → `compliance-engineer`

## Related skills

| Need | Skill |
|---|---|
| Authorized general pentest (non-HIL primary) | `penetration-tester` |
| Binary/firmware RE, protocol reverse engineering | `reverse-engineer` |
| Implement fixes (IAM, SIEM, guardrails) on IT systems | `information-security-engineer` |
| Security program, risk acceptance, engagement governance | `cybersecurity` |
| Audit control mapping and evidence packages | `compliance-engineer` |
| Web/API layer when also in scope | `web-pentester` |
| Network/AD when bench includes enterprise segment | `network-pentester` |
| Threat context and TTP mapping for reports | `cti-analyst` |
| Customer-facing technical writeups | `tech-writer-researcher` |

## Core Workflows

### 1. Authorization, scope, and bench readiness

**Do not energize targets or inject faults without written authorization and completed safety review.**

1. Confirm signed SOW/ROE: targets, buses, methods, time windows, stop conditions
2. Complete bench **FMEA / hazard review** with lab owner; document interlocks and e-stop
3. Inventory target firmware versions, keys, calibration, and baseline configuration
4. Define out-of-scope (moving machinery, public roads, production fleets, third-party networks)
5. Establish emergency stop, power-down procedure, and escalation contacts

**See `references/hil_security_tester_scope.md` and `references/test_bench_and_safety.md`.**

### 2. Attack surface mapping and test design

```
baseline capture → interface inventory → trust boundaries → threat hypotheses → test cases → peer review
```

Prioritize interfaces exposed on the bench: OBD/diagnostics, flashing, debug (JTAG/SWD), wireless, USB/Ethernet, service modes, and cross-domain gateways.

**See `references/bus_and_interface_security.md` and `references/automotive_and_industrial_patterns.md`.**

### 3. Execute fault injection and stimulus (in scope)

- Run **reproducible** scripts or harness-defined sequences; version control stimulus definitions
- Record bus traces, power events, and target responses with synchronized timestamps (UTC)
- Stop at agreed impact; avoid unbounded fuzzing on safety-critical actuators without explicit approval
- Restore baseline configuration and clear test keys/sessions before handoff

**See `references/fault_injection_and_stimulus.md`.**

### 4. Evidence, reporting, and coordination

Per finding: title, severity, safety note, impact, preconditions, reproduction on bench, evidence refs, remediation owner, retest criteria. Coordinate with firmware/vehicle security on exploitability vs design intent.

**See `references/evidence_and_reporting.md`.**

## When to load references

| Topic | Reference |
|---|---|
| Role boundaries and engagement types | `references/hil_security_tester_scope.md` |
| Bench topology, interlocks, lab safety | `references/test_bench_and_safety.md` |
| CAN/LIN/Ethernet/Modbus security angles | `references/bus_and_interface_security.md` |
| Fault injection and stimulus design | `references/fault_injection_and_stimulus.md` |
| Evidence capture and reporting | `references/evidence_and_reporting.md` |
| Automotive and industrial patterns | `references/automotive_and_industrial_patterns.md` |
