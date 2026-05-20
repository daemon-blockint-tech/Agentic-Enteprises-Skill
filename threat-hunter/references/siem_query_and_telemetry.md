# SIEM query and telemetry

## Table of contents

1. [Telemetry inventory](#telemetry-inventory)
2. [Query workflow](#query-workflow)
3. [Cross-domain pivots](#cross-domain-pivots)
4. [Baselines and anomalies](#baselines-and-anomalies)
5. [Quality and gaps](#quality-and-gaps)

## Telemetry inventory

Before hunting, confirm availability and retention:

| Domain | Common sources | Hunt uses |
|---|---|---|
| Identity | IdP sign-in, MFA, conditional access, group changes | Session abuse, privilege add |
| Endpoint | EDR process, file, registry, network | Execution, persistence, lateral |
| Network | Firewall, proxy, DNS, NDR | C2, exfil, beaconing |
| Email | Gateway, O365/GWS mail audit | phishing, forwarding rules |
| Cloud | CloudTrail, Activity Audit, K8s audit | API abuse, IAM, storage |
| App | WAF, app logs, DB audit | fraud, SQLi, token abuse |

Document **retention** (hot/warm/cold), **parse status**, and **known blind spots** in the hunt record.

## Query workflow

1. **Anchor** on a known entity, IOC, or time window from trigger
2. **Broad pull** — low-cardinality filters; count by entity
3. **Rank** — sort by rarity, first-seen, or deviation from baseline
4. **Deep dive** — pull full events for top N entities only
5. **Validate** — alternate data source confirms the same story
6. **Snapshot** — save query text, parameters, time range, and result count

### Query hygiene

- Use **UTC** in queries; note display timezone in reports
- Prefer **structured fields** over raw regex when parsers exist
- Cap result sets; paginate or aggregate before exporting millions of rows
- Version queries in the hunt repo or ticket—do not rely on ad hoc UI history alone

### Platform notes

- **Splunk (SPL):** `tstats`, `datamodel`, `transaction` for session stitching; watch index=* cost
- **Microsoft Sentinel (KQL):** `join`, `has_any`, `ago()`; use `union` sparingly with time bounds
- **Chronicle / UDM:** normalize entity fields; use reference lists for IOCs
- **Elastic:** ECS fields, runtime fields; watch cluster load on wildcards

Adapt syntax to your stack; principles are platform-agnostic.

## Cross-domain pivots

| From | Pivot on | To |
|---|---|---|
| Phishing email | recipient, URL hash | IdP sign-in, EDR on mailbox host |
| Suspicious process | parent, user, hash | Network egress, DNS |
| Cloud API key use | access key id, role | CloudTrail source IP, IAM changes |
| VPN / ZTNA session | user, device id | EDR device id, internal auth |

Build a **mini-timeline** per entity before declaring malicious intent.

## Baselines and anomalies

1. Define **peer group** (role, department, OS image, region)
2. Measure **frequency** (logins/day, rare processes, new destinations)
3. Flag **first-seen** or **top-N rare** with minimum volume thresholds
4. Exclude known change windows (patch Tuesday, marketing campaigns)
5. Re-check flagged entities manually—automation suggests, humans confirm

Document baseline assumptions; stale baselines create false hunts.

## Quality and gaps

Log issues for detection engineering:

- Missing fields (no `process.command_line`, no `source.ip` on cloud events)
- Clock skew between sources (>5 minutes)
- Duplicate or dropped events
- Parser errors and mis-tagged `action` values

Stop or narrow the hunt if critical data is unavailable; state **inconclusive** rather than over-interpreting partial logs.
