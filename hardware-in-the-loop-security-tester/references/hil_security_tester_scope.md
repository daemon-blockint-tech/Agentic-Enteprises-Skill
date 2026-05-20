# HIL security tester scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [Engagement types](#engagement-types)
3. [Partnership model](#partnership-model)
4. [What good looks like](#what-good-looks-like)

## Role boundary

| HIL security tester owns | Others own |
|---|---|
| Security assessment on **real hardware** with HIL/plant simulation | Web/API OWASP testing (`web-pentester`) |
| Bench setup, bus monitoring, fault injection **within ROE** | Network/AD/infra pentest (`network-pentester`) |
| Reproducible embedded/cyber-physical test cases | General pentest without hardware focus (`penetration-tester`) |
| Evidence capture (traces, logs, configs) for embedded findings | Binary RE and patch diff labs (`reverse-engineer`) |
| Lab safety interlocks and test hygiene | SOC alert triage (`soc-analyst`) |
| Coordination with firmware/vehicle security on exploitability | Live IR command (`incident-responder`) |
| Retest on same bench after fixes | AI/LLM adversarial testing (`ai-redteam`) |
| | Classified ISSO accreditation work (`information-systems-security-officer-classified-specialist`) |
| | CI-only build gates (`build-validator`) |
| | Enterprise GRC strategy (`cybersecurity`) |
| | Control testing without active lab tests (`compliance-engineer`) |

**HIL security tester** validates weaknesses on **physical targets under controlled conditions**; it does **not** replace IT pentest, SOC operations, or production incident response.

## Engagement types

| Type | Focus | Typical deliverable |
|---|---|---|
| **Automotive ECU/domain** | Diagnostics, flashing, gateway, SOME/IP/DoIP exposure on bench | Bus traces + reproduction steps + safety notes |
| **Industrial PLC/RTU** | Modbus/register abuse, engineering station paths, logic download | Stimulus scripts + evidence bundle |
| **Aftermarket / telematics** | Wireless, OTA, companion connectivity on isolated rig | Interface matrix + test case pack |
| **Supply-chain sample** | New ECU revision before fleet integration | Baseline vs hardened comparison |
| **Retest** | Prior critical/high on same firmware/hardware rev | Pass/fail per finding on bench |

Clarify **grey-box vs white-box** (schematics, DBC/LDF, firmware images, keys) in the SOW.

## Partnership model

| Partner | Interaction |
|---|---|
| Firmware / embedded security | Provides images, keys, threat models; reviews exploitability |
| Vehicle / product safety | Approves actuator tests; defines prohibited stimuli |
| `reverse-engineer` | Deep protocol or binary analysis when bus traces are insufficient |
| `penetration-tester` | Overlapping IT attack paths when bench includes full stack |
| `information-security-engineer` | Production control implementation—not lab execution |
| `compliance-engineer` | Maps findings to controls when audit evidence is required |
| Legal / safety | Reviews ROE, export, and physical hazard constraints |

## What good looks like

1. **Written authorization** and completed safety review before energizing targets
2. Every finding is **reproducible on the bench** with versioned stimulus and captured traces
3. **Safety interlocks** documented; e-stop tested; hazardous motion isolated or mocked
4. Evidence is **redacted**; no unnecessary exfiltration of customer calibration or PII
5. **Baseline restored**; test keys and diagnostic sessions cleared before handoff
6. **Retest** scheduled for critical/high with frozen hardware/firmware identifiers
