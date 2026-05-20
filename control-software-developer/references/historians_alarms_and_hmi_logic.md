# Historians, alarms, and HMI logic

## Table of contents

1. [Historian pipelines](#historian-pipelines)
2. [Alarm philosophy](#alarm-philosophy)
3. [Events and SOE](#events-and-soe)
4. [HMI and SCADA server logic](#hmi-and-scada-server-logic)
5. [Operator workflow](#operator-workflow)
6. [Performance and flooding](#performance-and-flooding)

## Historian pipelines

| Element | Guidance |
|---|---|
| Sampling | Align to control relevance—not every tag at fastest rate |
| Compression | Deadband and swing-door policies per tag class |
| Metadata | Units, limits, instrument type, asset hierarchy for analytics |
| Retention | Hot/warm/cold tiers; legal/operations retention separately |
| Ingress | Buffer at collector; handle back-pressure from slow archives |

Document **timestamp source** (controller vs server vs gateway) for forensic alignment.

## Alarm philosophy

| Item | Practice |
|---|---|
| Priority model | Consistent P1–P4 (or site standard) mapped to response time |
| Alarm vs alert | Alarms require operator action; alerts are informational |
| Shelving / suppression | Time-bound, attributed, auditable; avoid permanent suppression |
| Chattering | Debounce, hysteresis, or deadband at source—not only in HMI |
| Standing alarms | Regular rationalization reviews with operations |

## Events and SOE

- Capture **sequence of events** with millisecond resolution where process requires
- Correlate SOE with historian trends for post-trip analysis
- Define **flood handling** during plant upsets—summary alarms vs raw storm
- Export formats for CMMS and incident reviews (coordinate with operations)

## HMI and SCADA server logic

This skill covers **server-side behavior**, not screen graphics alone.

| Capability | Examples |
|---|---|
| Calculations | Derived tags, mass/energy balances, KPI rollups |
| Command validation | Role checks, interlock verification before write |
| Faceplate logic | Min/max enforcement, mode labels, permissive display |
| Scripts | Scheduled reports, aggregated statuses, comms health |
| Navigation rules | Deep links, forced acknowledgment workflows |

Document **write paths**: who can command, through which service, with what timeout and feedback.

## Operator workflow

- Align alarm text with **operations vocabulary**—avoid vendor-generic messages
- Provide **recommended action** fields where standards allow
- Separate **control** faceplates from **monitoring** dashboards for critical tags
- Test workflows under **loss of comms** and **degraded quality** scenarios

## Performance and flooding

| Risk | Mitigation |
|---|---|
| Alarm storms | Rate limits, grouping, first-out capture, dynamic suppression policies |
| Historian overload | Tiered sampling, edge buffering, drop policies for non-critical tags |
| HMI script load | Move heavy analytics to services; keep scan-synchronous work minimal |
| Client fan-out | OPC subscription tuning; MQTT topic QoS choices |

When graphics teams own pixels, control software still owns **tag behavior, alarms, and server scripts**—hand off visual design separately.
