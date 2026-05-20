# Detection and hunting handoffs

## Table of contents

1. [APT detection priorities](#apt-detection-priorities)
2. [Handoff to threat-hunter](#handoff-to-threat-hunter)
3. [Handoff to SOC and engineering](#handoff-to-soc-and-engineering)
4. [Detection engineering backlog](#detection-engineering-backlog)
5. [Feedback loop](#feedback-loop)

## APT detection priorities

Prioritize controls that survive **retooling**:

1. **Behavioral detections** — LOLBins, abnormal cloud API sequences, rare process ancestry
2. **Identity-centric** — impossible travel, MFA fatigue patterns, OAuth app abuse, tiered admin use
3. **Network patterns** — beaconing statistics, DNS anomalies, unexpected egress volumes
4. **Persistence mechanisms** — scheduled tasks, services, cloud IAM backdoors
5. **Deception and canaries** — high-fidelity signals for patient adversaries (where deployed)

Deprioritize **brittle IOC-only** blocks as the sole control for APT; use with expiration and context.

## Handoff to threat-hunter

Package for `threat-hunter`:

| Element | Description |
|---|---|
| Campaign ID | Link to tracker |
| Hypotheses | Falsifiable statements tied to ATT&CK |
| Query seeds | Starting SPL/KQL/SQL or platform-specific pivots |
| Time range | UTC bounds; note retention limits |
| Data sources | Required logs; explicit gaps |
| Entities | Users, hosts, apps, cloud principals to prioritize |
| Negative indicators | Known FP patterns, red-team ranges |
| Success criteria | What confirms/refutes APT presence |
| Confidence | Per hypothesis |

**Example hypothesis:** “If CLUSTER-FOX-12 is active, OAuth consent grants to rare app IDs will appear in Entra sign-in logs within 30 days.”

## Handoff to SOC and engineering

**To `soc-analyst`:**

- Campaign summary (short), relevant technique alerts, enrichment pivots
- IOC tier: block vs monitor vs hunt-only
- Expected false positives and escalation criteria

**To `information-security-engineer`:**

- Logging gaps (missing fields, retention, parser errors)
- Feed requirements; STIX fields needed for campaign metadata
- Architecture changes (EDR coverage, cloud audit policies)

Do not dump raw intel feeds—provide **contextualized packages**.

## Detection engineering backlog

For each candidate detection:

1. **Name and campaign link**
2. **Logic summary** — behavior detected, not just IOC
3. **ATT&CK mapping**
4. **Data sources and dependencies**
5. **Expected true-positive rate** and known FP modes
6. **Tuning notes** — exclusions, thresholds, entity baselines
7. **Validation plan** — purple-team, historical replay, hunt confirmation
8. **Priority** — based on actor activity in sector and visibility gap

## Feedback loop

After hunt or SOC validation:

1. Record **confirmed** / **disconfirmed** / **inconclusive** per hypothesis
2. Update campaign tracker and confidence
3. Retire or tune detections producing unacceptable FP volume
4. Feed lessons to `cti-analyst` for collection gap closure
5. Escalate confirmed widespread compromise to `incident-responder`

APT analysis owns **what to hunt for and why**; hunters own **execution**; engineering owns **implementation**.
