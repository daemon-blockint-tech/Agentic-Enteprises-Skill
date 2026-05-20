# Deployment, testing, and safety coordination

## Table of contents

1. [Test pyramid for control software](#test-pyramid-for-control-software)
2. [MIL and SIL (high level)](#mil-and-sil-high-level)
3. [FAT and SAT hooks](#fat-and-sat-hooks)
4. [Versioned OT deployment](#versioned-ot-deployment)
5. [Rollback and verification](#rollback-and-verification)
6. [Safety and security coordination](#safety-and-security-coordination)

## Test pyramid for control software

| Layer | Focus |
|---|---|
| Unit/module | Function blocks, sequences, state machines with injected I/O |
| Integration | Protocol mappings, gateway transforms, historian collectors |
| System | Controller + HMI server + comms on staging hardware |
| Regression | Golden traces for loops after logic changes |
| Field | FAT/SAT checklists—operations-led with engineering support |

Prefer **automated regression** where vendor tooling allows; export traces for diff on logic changes.

## MIL and SIL (high level)

| Type | Intent | This skill provides |
|---|---|---|
| MIL | Plant/model simulated; control logic connected to model I/O | Interface spec, tag mapping, scenario list |
| SIL | Controller/runtime tested against simulated or recorded I/O | Staging configs, test harness hooks |

**Does not** certify SIL levels or replace process-safety engineering. Document assumptions and gaps explicitly.

## FAT and SAT hooks

- Deliver **test cases** tied to tag scenarios: modes, trips, comms loss, manual override
- Provide **expected traces** (trend snapshots) for critical sequences
- Include **alarm verification** matrix: trigger, priority, shelving behavior
- Stage **protocol load tests** before connecting enterprise consumers

## Versioned OT deployment

| Artifact | Versioning practice |
|---|---|
| Controller logic | Vendor project version + git export where possible |
| HMI server scripts | Semantic version aligned with logic package |
| Protocol maps | Separate version id; checksum in deploy manifest |
| Certificates | Track expiry in deploy prerequisites |

Deployment steps (generic):

1. Freeze package in staging; run regression and MIL/SIL suites
2. Operations change ticket and outage window
3. Backup running config; deploy to standby first if redundant
4. Verify I/O feedback, alarms, historian, and critical sequences
5. Promote to active; monitor overrun and comms health
6. Archive manifest and sign-offs

## Rollback and verification

- Keep **last-known-good** images per controller area
- Define **rollback triggers**: failed sequence test, unexpected alarms, comms storm
- Verify rollback on **staging** periodically—not only during emergencies
- Post-deploy: capture **24–72h** monitoring checklist for integrator windup and alarm rationalization

## Safety and security coordination

| Topic | Control software role | Peer |
|---|---|---|
| SIS separation | Never merge; document interfaces only | Process safety |
| Unsafe downloads | Stop; require operations approval | Operations |
| New exposure (OPC/MQTT/cloud) | Document data flows and write paths | `scada-ics-cyber-security-specialist` |
| Bench security tests | Provide builds and mappings | `hardware-in-the-loop-security-tester` |
| Criticality / DR expectations | State dependencies and RTO needs | `mission-critical` |
| Release discipline / HRO gates | Checklists, independent verification | `zero-tolerance-for-failure` |

**Never** recommend live-plant security testing (scanning, fuzzing, exploit validation) as part of application deploy—route to OT security with safety gates.
