# Post-incident review

## Table of contents

1. [When to run](#when-to-run)
2. [Participants](#participants)
3. [Review agenda](#review-agenda)
4. [Report template](#report-template)
5. [Action items](#action-items)
6. [Feeding improvements back](#feeding-improvements-back)

## When to run

- **SEV1–2 security incidents**: review within 5 business days of containment (or per `incident-management-engineer` policy)
- **SEV3**: optional short review if recurrence risk or detection gap
- **SEV4**: trend in monthly SOC/CSIRT metrics unless pattern emerges

Do not close the incident record until critical actions have owners or explicit deferral with risk acceptance.

## Participants

- Incident commander, CSIRT lead, key technical leads
- SOC representative (`soc-analyst`) if detection involved
- `incident-management-engineer` delegate for process gaps
- Legal/privacy if data exposure; comms if external messaging occurred
- Optional: affected product/engineering manager

Exclude blame; focus on systems and decisions.

## Review agenda

1. **Timeline walkthrough** — final UTC timeline vs initial assumptions  
2. **Impact** — customers, data, duration, regulatory touchpoints  
3. **What went well** — fast containment, clear roles, useful runbooks  
4. **What went poorly** — delays, tooling gaps, comms confusion  
5. **Root cause classes** — people/process/technology/third party (multi-factor OK)  
6. **Detection** — MTTD, alert quality, escalation path  
7. **Containment/eradication** — effective actions and near misses  
8. **Actions** — prioritized with owners and dates  

## Report template

```markdown
# Post-incident review: INC-#### [Title]

## Summary
[2–3 sentences]

## Severity and duration
- Severity: SEV#
- Declared: UTC
- Contained: UTC
- Closed: UTC

## Impact
- Systems:
- Data:
- Customers:

## Timeline (abbreviated)
| UTC | Event |
|-----|-------|

## Root cause
[Primary and contributing factors]

## Lessons learned
1.
2.

## Action items
| ID | Action | Owner | Due | Type (detect/prevent/process) |
|----|--------|-------|-----|-------------------------------|
```

## Action items

Classify each item:

| Type | Example | Typical owner skill |
|---|---|---|
| Detect | New SIEM rule, EDR hunt | `soc-analyst` |
| Prevent | MFA enforcement, patch | `information-security-engineer` |
| Process | Escalation SLA, tabletop | `incident-management-engineer` |
| Cloud control | SCP, log retention | `cloud-security-engineer` |
| Comms | Template update | `communication-lead` |

Track to completion in same system as engineering work; review open items in monthly security ops forum.

## Feeding improvements back

- **5 Whys** only to actionable depth—stop at controllable fixes
- Share sanitized learnings with engineering and SOC
- Update runbooks and escalation criteria
- Schedule tabletop if systemic gap (program owner: `incident-management-engineer`)
- Link repeat incidents to reliability or compliance reviews when applicable
