# Reporting and Remediation Handoff

## Report structure

### Executive summary (1–2 pages)

- Engagement type, dates, authorization reference
- **Risk narrative**: what an adversary could achieve in scope
- Top 3 business-relevant findings (plain language)
- Detection program strengths and gaps (summary)
- Recommended strategic investments (people, process, technology)

### Technical appendix

- Scope and ROE summary
- Campaign timeline (UTC)
- ATT&CK heatmap: executed vs detected
- Attack paths (diagram or ordered steps)
- Operator log excerpts (redacted)
- Evidence index (hashes, queries, screenshots)

### Purple-team / blue-team section

- Detection validation matrix
- SOC process observations (escalation, tuning, noise)
- Tabletop or comms gaps if applicable

## Finding format

| Field | Guidance |
|---|---|
| Title | Outcome-focused (e.g., "Domain admin without MFA challenge") |
| Severity | Impact × likelihood; align to client rubric |
| ATT&CK | Technique IDs used |
| Path | Preconditions → steps → result |
| Detection | What fired / missed / blocked |
| Remediation | Specific, actionable (owner-agnostic if unknown) |
| Retest | Criteria for purple re-run or automated test |

## Remediation handoff

| Audience | Deliverable |
|---|---|
| **Blue / SOC** | Detection gaps, suggested data sources, IOC cleanup list |
| **Engineering** | Control fixes (patch, config, IAM) via tickets |
| **Leadership** | Prioritized roadmap items from executive summary |
| **GRC** | Map to frameworks if requested (`cybersecurity`, `compliance-engineer`) |

Do not assign legal or regulatory conclusions—flag for legal/compliance review.

## Cleanup attestation

Before final report sign-off:

- [ ] Persistence removed
- [ ] Test accounts disabled or deleted
- [ ] C2 infra torn down per schedule
- [ ] Artifacts removed from endpoints (or list exceptions)
- [ ] Blue team confirms no outstanding red-team access

## Retest and continuous improvement

1. Schedule **retest** for critical detection gaps (30–90 days typical)
2. Track remediation tickets to closure
3. Archive operator logs per evidence retention in ROE
4. Feed lessons into next campaign plan and threat model update

## What not to include

- Exploit code or weaponized payloads beyond what client needs
- Unredacted credentials or live session tokens
- Out-of-scope system data
- Attribution of real threat actors as fact (use "informed by" language)
