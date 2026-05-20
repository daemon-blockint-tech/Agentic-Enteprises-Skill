# TTP Selection and Execution Coordination

## ATT&CK-driven selection

1. Start from **campaign objectives** and threat actor profile
2. Map required outcomes to **tactics** (e.g., Initial Access → Execution → Persistence → Lateral Movement → Collection → Exfiltration)
3. Pick **techniques** with technique IDs (e.g., T1566.001, T1021.001)
4. For each technique, define:
   - Preconditions (access level, network position)
   - Expected **telemetry** (process, auth, network, cloud audit)
   - **Detection hypothesis** (rule name, data source, expected alert)
   - **Abort criteria** if impact exceeds ROE

## Prioritization

| Priority | Choose when |
|---|---|
| P0 | Directly tests stated objective or known gap |
| P1 | High realism for threat actor |
| P2 | Fills ATT&CK coverage map |
| Defer | Low risk relevance or tooling unstable |

Avoid "checklist dumping"—sequence TTPs into a **coherent story**.

## Operator log (required fields)

| Field | Example |
|---|---|
| UTC timestamp | 2026-05-20T14:32:00Z |
| Operator | Initials or role |
| Technique ID | T1059.001 |
| Host / account | WORKSTATION01 / CORP\user |
| Action summary | PowerShell download cradle (simulated) |
| Outcome | Success / blocked / partial |
| Detection | Y / N / delayed / unknown |
| Evidence ref | Ticket, screenshot ID, log query link |

## Coordinating execution specialists

| Specialist | Delegate when |
|---|---|
| `web-pentester` | OWASP classes, API authZ, session abuse in scope |
| `network-pentester` | AD paths, segmentation, service exploits, wireless |
| `penetration-tester` | Multi-vector PoC under unified ROE |

**Red team lead** provides: objective, technique ID, OPSEC constraints, stop conditions, and log format. Specialist returns: repro steps, evidence, cleanup list.

## In-scope execution rules

- Use **minimal** steps to prove the path; avoid gratuitous exploitation
- Prefer **documented playbooks** over ad-hoc tooling for repeatability
- Do not chain into out-of-scope systems—even if reachable
- Record **every** privilege change and persistence mechanism for cleanup

## C2 and infrastructure (if allowed)

- Register domains/IPs in ROE appendix
- Use TLS profiles and redirectors per OPSEC plan
- Plan **teardown** dates for infra and certificates
- Never reuse production admin channels for C2

## Post-execution

1. Confirm detection outcome with blue team (purple mode)
2. Update ATT&CK coverage matrix
3. Queue remediation or detection tickets with severity
4. Schedule retest for failed detections on critical techniques
