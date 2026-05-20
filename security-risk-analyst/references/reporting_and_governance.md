# Reporting and governance

## Table of contents

1. [Audiences](#audiences)
2. [Committee pack structure](#committee-pack-structure)
3. [KRIs](#kris)
4. [Board narrative](#board-narrative)
5. [Risk vs compliance reporting](#risk-vs-compliance-reporting)
6. [Cadence](#cadence)

## Audiences

| Audience | Focus | Depth |
|---|---|---|
| Risk owner | Their scenarios, treatments, due dates | Operational |
| Risk committee | Top risks, acceptances, trends | Tactical |
| Executive leadership | Appetite, investment tradeoffs | Summary |
| Board | Material cyber risk, incidents, program health | High level |

Tailor language: business impact and decisions, not CVE lists.

## Committee pack structure

Recommended sections (≤15 slides or equivalent):

1. **Executive summary** — posture vs appetite, key changes since last meeting
2. **Top risks** — residual heat map or ranked table (inherent vs residual)
3. **New and closed** — scenarios added/retired since last cycle
4. **Treatments** — on-track / at-risk mitigations; overdue callouts
5. **Acceptances** — open acceptances nearing expiry; new requests
6. **Third party** — tier changes, critical vendor issues
7. **KRIs** — RAG status and commentary
8. **Incidents and lessons** — link to register updates (no full IR timeline)
9. **Decisions needed** — acceptances, appetite exceptions, funding asks

Attach register export as appendix; do not read rows aloud in meeting.

## KRIs

Define **Key Risk Indicators** per top scenario or category:

| KRI example | Links to scenario |
|---|---|
| % critical vulns past SLA | Exploitation of unpatched systems |
| Mean time to contain (trend) | Breach impact duration |
| Vendors T1 without current assessment | Third-party breach |
| Admin accounts without MFA | Credential compromise |
| Failed phishing simulation rate | Human factor |

Rules:

- Thresholds aligned to **risk appetite** (green/amber/red)
- Owner for each KRI (usually control owner, not risk analyst alone)
- KRIs measure **risk drivers**, not compliance checkbox completion

## Board narrative

Board materials should answer:

- Are we **within appetite** for material cyber risk?
- What **changed** this quarter (threat, incident, regulation, major project)?
- What **investments** reduce top residual risks?
- Any **accepted risks** above normal delegation?
- How do **incidents** affect the risk profile?

Avoid: raw scan counts, tool logos, uncertified compliance claims. Coordinate with `cybersecurity` for program context.

## Risk vs compliance reporting

| Risk reporting | Compliance reporting (`compliance-engineer`) |
|---|---|
| Scenarios, residual, treatment | Control ID pass/fail, evidence status |
| Appetite and acceptance | Audit observation period, attestations |
| Prioritization for investment | Remediation for certification |

Cross-reference: a **failed control** may increase residual risk; do not duplicate full control matrices in risk packs.

## Cadence

| Activity | Frequency |
|---|---|
| Register hygiene | Monthly |
| KRI review | Monthly |
| Risk committee | Quarterly (minimum) |
| Board cyber risk item | Quarterly or per charter |
| Full methodology refresh | Annual |

After **SEV1/SEV2** security incident: ad hoc committee briefing within 10 business days if material to top risks.
