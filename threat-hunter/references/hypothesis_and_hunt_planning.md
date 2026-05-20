# Hypothesis and hunt planning

## Table of contents

1. [Hunt triggers](#hunt-triggers)
2. [Hypothesis format](#hypothesis-format)
3. [Hunt types](#hunt-types)
4. [Planning checklist](#planning-checklist)
5. [Scoping and ethics](#scoping-and-ethics)

## Hunt triggers

Accept work from:

- **SOC escalation** — correlated alerts, unknown true positives, noisy rules masking activity
- **Threat intel** — sector advisory, ISAC report, actor profile, leaked credentials
- **Post-incident** — hunt for related infrastructure after IR closes initial scope
- **Purple / red feedback** — techniques that evaded detection in exercise
- **Baseline drift** — new app, merger, cloud migration, or identity change breaking “normal”
- **Leadership / audit ask** — targeted assurance on technique or asset class

Decline or redirect pure **alert backlog clearing** to `soc-analyst`.

## Hypothesis format

Write hypotheses so they can be **falsified**:

> **If** [threat scenario / actor behavior], **then** we expect [observable behavior] in [data source] during [time window].

Add:

- **Success criteria** — what counts as confirmed, suspicious, or ruled out
- **Null result value** — “not found” still improves coverage documentation
- **ATT&CK focus** — tactic/technique IDs when known (e.g., T1078, T1021.001)

**Bad:** “Look for hackers.”  
**Good:** “If FIN-style actor uses stolen session cookies, we will see impossible-travel auth plus new device enrollments in IdP logs within 14 days.”

## Hunt types

| Type | Start from | Typical data |
|---|---|---|
| Intel-led | Reported IOCs, TTPs, sector campaign | Proxy, DNS, email, EDR, IdP |
| ATT&CK-led | Technique coverage gap | Domain-specific logs for that technique |
| Baseline-led | Peer group or historical “normal” | Stats on volume, rare commands, new paths |
| Entity-led | Crown-jewel user/host/app | Deep dive on one principal |
| Hunt-after-incident | IR scope boundaries | Broader enterprise pivot from known IOC |

Time-box hunts (e.g., 4–40 hours); extend only with documented rationale.

## Planning checklist

1. Assign **hunt ID**, owner, and stakeholders (SOC lead, detection engineer)
2. Define **UTC window** and retention limits per source
3. List **required data sources**; flag gaps early
4. Identify **in-scope** assets, regions, business units, and **exclusions** (personal devices, M&A carve-outs)
5. Draft **initial query plan** (broad → narrow); estimate false-positive volume
6. Set **stop rules** — max entities reviewed, escalation triggers, end date
7. Plan **outputs** — report template, detection tickets, IR escalation threshold
8. Record **related incidents**, tickets, and intel report IDs

## Scoping and ethics

- Hunt only **authorized enterprise systems** and data you are permitted to access
- **Privacy / HR**: route insider-threat hunts through legal/HR policy; minimize PII in reports
- **Production safety**: prefer read-only queries; coordinate with IR before isolation or account disables
- **Third parties**: do not query customer tenants or partner environments outside contract scope

When scope is unclear, stop and confirm with security leadership before running broad searches.
