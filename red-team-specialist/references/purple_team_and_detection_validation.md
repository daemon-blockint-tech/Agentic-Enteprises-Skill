# Purple Team and Detection Validation

## Modes

| Mode | Blue visibility | Use for |
|---|---|---|
| **Collaborative purple** | Real-time or same-day sync | Detection tuning, training |
| **Semi-blind** | SOC unaware; leadership aware | Process test |
| **Blind** | Minimal pre-brief | Realistic detection/response |

Document mode in ROE and kickoff slides.

## Pre-exercise brief (purple)

Share with blue team / SOC (as agreed):

- UTC windows for injects
- High-level tactic list (not always exact timing)
- Deconfliction tokens (accounts, domains, file hashes)
- Escalation channel for false positives vs real chain
- **No** surprise destructive actions

## Detection validation matrix

| Technique ID | Data source expected | Detection expected | Observed? | Latency | Gap notes |
|---|---|---|---|---|---|
| T1078 | IdP / VPN logs | Impossible travel rule | Y/N | mm:ss | |
| T1059.001 | EDR process | PowerShell block/alert | | | |

Score each executed technique:

- **Detected** — alert or analyst within SLA
- **Missed** — no timely detection
- **Blocked** — control prevented technique (note if objective still met another way)
- **Unknown** — insufficient logging

## Working with SOC

- Do **not** ask `soc-analyst` to run the campaign; they **consume** telemetry
- Provide **after-action** IOC list and timeline for alert tuning
- Escalate to `incident-responder` only if a **real** incident occurs outside ROE

## Detection engineering handoff

For each gap, specify:

| Field | Content |
|---|---|
| Technique | ATT&CK ID + name |
| Log source | Windows Security, CloudTrail, proxy, etc. |
| Proposed detection | Sigma/KQL/rule concept (not full implementation unless scoped) |
| Priority | Based on objective criticality |
| Owner | SOC, detection engineering, platform team |

Route implementation to `information-security-engineer` when building pipelines or content.

## Hotwash (within 48h)

1. Timeline walkthrough (red + blue)
2. Top 3 detection wins and top 3 gaps
3. Process issues (escalation, comms, tooling)
4. Agreed actions with owners and dates
5. Optional: re-run selected TTPs after fixes

## Metrics for leadership

- % techniques detected within SLA
- Critical path stages missed
- Time to contain (if exercise includes response)
- Trend vs prior purple exercises
