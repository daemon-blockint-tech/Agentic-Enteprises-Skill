# M&A and investment diligence

## Table of contents

1. [Diligence objectives](#diligence-objectives)
2. [Workstream setup](#workstream-setup)
3. [Request list themes](#request-list-themes)
4. [Evidence review](#evidence-review)
5. [Interviews and technical sessions](#interviews-and-technical-sessions)
6. [Findings and deal implications](#findings-and-deal-implications)
7. [Integration planning](#integration-planning)

## Diligence objectives

Clarify upfront:

| Question | Why it matters |
|---|---|
| Buyer role (strategic vs financial) | Depth of integration and control expectations |
| Deal structure (asset vs stock) | Liability for legacy incidents and contracts |
| Regulatory / sector overlay | Healthcare, finance, critical infrastructure, export |
| Known cyber events | Prior breaches, ransomware, regulatory actions |
| Material systems and data | PII, PHI, payment, IP, customer production |

Align objectives with **deal lead** and **legal**; coordinate timing with `transaction-manager` for VDR and Q&A hygiene.

## Workstream setup

1. **Charter** — scope, exclusions, deliverables, deadline (signing vs close)
2. **Access** — VDR index, interview list, pen test reports (if available), policies
3. **Tracker** — request ID, owner, status, evidence link, follow-ups
4. **SME map** — identity, cloud, appsec, IR, privacy, IT general controls
5. **Readout cadence** — weekly steering; IC draft milestones

Do not duplicate **process** ownership held by `transaction-manager`; provide cyber content for their trackers.

## Request list themes

Organize requests by control domain (adjust for target size):

| Domain | Example requests |
|---|---|
| Governance | Security policy set, org chart, board reporting, risk register summary |
| Identity | IdP/MFA, privileged access, joiner-mover-leaver, SSO footprint |
| Infrastructure | Cloud accounts, segmentation, CSPM summary, key management |
| Application | SDLC, secure coding, prod access, secrets management |
| Vulnerability | Scan cadence, critical open items, patch SLAs |
| Detection / IR | SIEM/EDR coverage, IR plan, tabletop date, prior incidents |
| Data protection | Classification, encryption, DLP, retention, subprocessors |
| Third parties | Critical vendors, SOC reports, concentration |
| Compliance | Certifications in scope, audit dates, open findings |
| Physical / OT | If applicable — separate workstream |

Prioritize **material** systems and **customer data** paths. Flag when target cannot produce evidence within timeline.

## Evidence review

For each request:

1. **Authenticate** — date, scope, auditor/tester, version
2. **Map** — control intent vs artifact (policy alone ≠ operating effectiveness)
3. **Test** — sample consistency (e.g., access review ticket matches policy cadence)
4. **Correlate** — breach disclosures, customer churn, insurance claims, litigation mentions
5. **Record** — finding or clear pass with citation (document, page, date)

Use third-party reports (SOC 2, ISO) as **starting points**, not substitutes for targeted questions on gaps and incidents.

## Interviews and technical sessions

| Audience | Focus |
|---|---|
| CISO / security lead | Program maturity, top risks, incidents, budget, key gaps |
| IT leadership | Infrastructure, migrations, technical debt, integration constraints |
| Engineering | SDLC, cloud footprint, secrets, prod access |
| Privacy / legal (security facts) | Breach history, regulatory inquiries (not legal advice) |

Prepare question trees; avoid **leading** assertions. Document quotes as **attributed notes**, not binding representations.

## Findings and deal implications

Rate findings (see `references/red_flags_and_remediation.md`):

| Deal lever | When to consider (with legal) |
|---|---|
| Price adjustment | Quantified remediation cost or liability tail |
| Escrow / holdback | Unresolved critical gaps or unknown incident exposure |
| R&W / indemnity | Representation scope for security and privacy |
| Conditions precedent | Must-fix before close (e.g., MFA on admin, revoke compromised creds) |
| Post-close covenant | Milestones for integration or remediation |

Separate **fact findings** from **legal recommendations**; route terms to `commercial-counsel`.

## Integration planning

Post-signing themes for security backlog:

| Workstream | Day 1 | 30 | 90 |
|---|---|---|---|
| Identity | Emergency access, disable risky integrations | SSO alignment, admin MFA | Full IAM integration plan |
| Tooling | EDR/SIEM visibility on combined estate | Consolidation decision | Decommission overlap |
| Data | Data map, legal hold awareness | Segregation / migration plan | Unified classification |
| Vendors | Critical subprocessor notice | Contract assignment | Renegotiate or replace |
| Culture | Comms to security teams | Policy harmonization | Training and attestations |

Hand engineering execution to `information-security-engineer`; program narrative to `chief-information-security-officer` where appropriate.
