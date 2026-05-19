# CVD program charter

## Table of contents

1. [Charter sections](#charter-sections)
2. [Roles](#roles)
3. [SLA targets](#sla-targets)

## Charter sections

| Section | Content |
|---|---|
| Mission | Why CVD exists; researcher-friendly posture |
| Scope | In-scope assets (domains, products, repos); explicit out-of-scope |
| Channels | security@, portal URL, bounty platform link |
| Safe harbor | Pointer to published policy; counsel-approved language |
| Severity model | Link to rubric (CVSS + business context) |
| Disclosure defaults | Coordinated date, max embargo, exception criteria |
| Metrics | Time-to-ack, time-to-triage, time-to-fix by severity, publication count |

## Roles

| Role | Responsibility |
|---|---|
| CVD program DRI (TPM) | Queue, SLAs, cross-team tracking, publication calendar |
| Security engineering lead | Severity validation, fix acceptance criteria |
| Product/component DRI | Remediation owner per affected system |
| Legal | Policy, bounty terms, advisory approval, safe harbor |
| Comms / PR | External messaging, blog timing, media hold |
| CVE coordinator | CNA requests, CVE metadata, MITRE coordination |

## SLA targets

Example starting points (tune to policy):

| Milestone | Critical | High | Medium | Low |
|---|---|---|---|---|
| Initial ack to reporter | 24h | 48h | 5d | 10d |
| Triage complete | 3d | 7d | 14d | 30d |
| Fix target (coordinated) | 7–30d | 30–90d | 90d+ | best effort |
| Publication after fix | Agreed date | Agreed date | Optional | Optional |

Document **business days** vs calendar and holiday coverage for ack SLA.
