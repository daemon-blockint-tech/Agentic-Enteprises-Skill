# Fault injection and stimulus

## Table of contents

1. [Planning principles](#planning-principles)
2. [Stimulus categories](#stimulus-categories)
3. [Test case structure](#test-case-structure)
4. [Harness and automation](#harness-and-automation)
5. [Abort and rollback](#abort-and-rollback)

## Planning principles

- Tie every stimulus to a **hypothesis** (e.g., gateway forwards unsigned diagnostic write)
- Obtain **safety approval** before actuator-affecting or power-anomaly tests
- Prefer **smallest step** that falsifies the hypothesis; avoid shotgun fuzzing
- Keep human **operator in the loop** for first run of a new stimulus class
- Version-control stimulus definitions alongside firmware hash and bench config ID

## Stimulus categories

| Category | Examples | Typical observables |
|---|---|---|
| **Bus / protocol** | Frame injection, timing skew, diagnostic sequences | NACKs, DTCs, bus-off, session changes |
| **Electrical / power** | Brownout, reset glitch (approved rigs only) | Boot mode, corruption, safe state |
| **Environmental** | Temperature chamber setpoints (if in scope) | Derating, sensor plausibility faults |
| **RF / wireless** | Isolated anechoic or cabled RF when authorized | Pairing bypass, downgrade |
| **HIL plant** | Sensor out-of-range, actuator delay injection | Control loop alarms, limp modes |
| **Human interface** | Tooling abuse (flashing dongle, JTAG when exposed) | Unlock persistence, debug shells |

Document **prohibited** stimuli in the test plan (e.g., airbag bus, steering torque, HV contactors).

## Test case structure

Use a consistent template:

```text
ID: HIL-SEC-###
Title:
Hypothesis:
Preconditions: (firmware hash, keys, bench mode, interlocks)
Stimulus: (script ref, frame list, duration, rate cap)
Expected (design intent):
Observed:
Evidence: (trace file, screenshot, log path)
Severity / safety note:
Retest criteria:
```

## Harness and automation

- Separate **stimulus generation** from **monitoring** (dual CAN interfaces or logger + injector)
- Synchronize clocks; embed test case ID in log filenames
- Implement **rate limits** and **max duration** in scripts
- Run automated suites only after manual proof on the same bench configuration

## Abort and rollback

Define abort triggers before execution:

| Trigger | Action |
|---|---|
| Unexpected motion or torque | E-stop; cut bus power per procedure |
| Target thermal or current fault | Power down; log last 60s of traces |
| Loss of watchdog / brick indicators | Stop stimulus; initiate reflash procedure |
| Stimulus script exception | Halt injection; hold plant in safe state |

After abort: preserve traces, file safety incident if required, do not resume until review.
