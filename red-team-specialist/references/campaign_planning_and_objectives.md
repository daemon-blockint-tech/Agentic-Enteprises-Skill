# Campaign Planning and Objectives

## Planning flow

```
threat context → objectives → scenarios → phases → resources → metrics
```

## Threat context

1. Identify **relevant threat actors** (industry, geography, capability)
2. Pull recent **threat intelligence** (reports, ISAC, internal incidents)
3. Select **ATT&CK tactics** that match actor behavior for this organization
4. Note **defender maturity** (SIEM, EDR, MFA, segmentation) from discovery or prior assessments

## Objectives (SMART + measurable)

| Objective type | Example |
|---|---|
| Access | Obtain privileged access to {system} without triggering P1 |
| Data | Demonstrate read access to {dataset} with audit trail only |
| Detection | Validate alert within {N} minutes for {technique} |
| Process | Exercise escalation from SOC to CSIRT with timeline |

Write objectives so success/failure is **auditable** from logs and operator notes.

## Scenario design

Build **1–3 scenarios** per campaign; avoid scope creep.

| Element | Define |
|---|---|
| Entry | Phish, external exploit, stolen creds, supply chain (if in ROE) |
| Path | Expected kill-chain stages and decision branches |
| Crown jewels | Ultimate goal aligned to business risk |
| Constraints | Time box, geography, cloud vs on-prem |

## Campaign phases (template)

| Phase | Activities |
|---|---|
| **Prepare** | ROE, infra, tooling, purple brief, blocklists |
| **Initial access** | Per scenario; coordinate specialists |
| **Establish foothold** | Persistence only if ROE allows; document artifacts |
| **Privilege / lateral** | Map paths; stop at ROE limits |
| **Objective** | Demonstrate impact; capture evidence |
| **Closeout** | Cleanup, hotwash, reporting |

## Resource coordination

| Need | Route to |
|---|---|
| Web/API exploitation | `web-pentester` |
| Network/AD/lateral | `network-pentester` |
| Cross-domain pentest execution | `penetration-tester` |
| Detection content after gaps | `information-security-engineer` |

Red team lead owns **timeline, OPSEC, and narrative**—not every technical step.

## Metrics

Track during campaign:

- Techniques executed (ATT&CK ID)
- Time per stage (dwell, lateral, objective)
- Detections: none / alert / human / blocked
- Mean time to detect (if purple windows defined)
- Open findings by severity

## Risk register

| Risk | Mitigation |
|---|---|
| Scope creep | Change control via ROE amendment |
| Production impact | Staging, rate limits, approved tools |
| False IR | Deconfliction tokens, purple channel |
| Credential exposure | Vault, rotation, minimal retention |
