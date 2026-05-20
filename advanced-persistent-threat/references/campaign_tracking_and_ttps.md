# Campaign tracking and TTPs

## Table of contents

1. [Campaign lifecycle](#campaign-lifecycle)
2. [Tracking methodology](#tracking-methodology)
3. [MITRE ATT&CK mapping](#mitre-attck-mapping)
4. [Victimology and targeting](#victimology-and-targeting)
5. [Campaign products](#campaign-products)

## Campaign lifecycle

Stages to document (not all campaigns exhibit every stage):

1. **Reconnaissance** — victim selection signals, sector/geo focus (often inferred)
2. **Initial access** — spearphish, drive-by, supply chain, credential abuse, edge appliance exploit
3. **Establish foothold** — malware drop, webshell, valid account, cloud token
4. **Persistence** — scheduled tasks, cloud IAM, firmware/bootkit (rare), supply-chain persistence
5. **Privilege escalation** — local/cloud elevation paths observed
6. **Defense evasion** — logging tampering, disable security tools, timestomp, living-off-the-land
7. **Credential access** — LSASS, Kerberos, cloud secrets, SSO abuse
8. **Discovery** — network/cloud enumeration patterns
9. **Lateral movement** — RDP, SMB, SSH, cloud role chaining, remote admin tools
10. **Collection** — staging directories, cloud storage targets, mailboxes
11. **C2** — protocols, domains, cloud abuse, dead-drop resolvers
12. **Exfiltration / impact** — compression, cloud egress, wipers, ransomware deployment

Flag **retooling** (new malware, new C2), **dormancy**, and **resurgence** with dates and evidence.

## Tracking methodology

1. Assign a **campaign ID** (internal, stable) at first credible link across incidents
2. Maintain a **master timeline** (UTC) merging CTI reporting, IR timelines, and hunt findings
3. Log **evidence objects** per event—hashes, domains, technique IDs, ticket/IR IDs
4. Note **confidence per link**—strong (shared custom malware + C2), weak (shared hosting only)
5. Review weekly during active campaigns; monthly for watch-list actors
6. **Close or merge** campaigns when infrastructure dies without replacement or attribution shifts

## MITRE ATT&CK mapping

1. Map at **technique** minimum; add **procedure** detail when evidence supports (commands, tools, configs)
2. Cite **data sources** required for detection (e.g., process creation, cloud audit logs, DNS)
3. Mark **gaps**—techniques used but not visible in org telemetry
4. Distinguish **observed** vs **reported-only** (vendor claim without internal validation)
5. Version ATT&CK explicitly; note deprecated techniques when reviewing legacy incidents

**Procedure documentation template:**

- Technique ID and name
- Procedure description (what happened)
- Evidence pointer (log type, artifact, report section)
- First/last seen (UTC)
- Detection opportunity (rule idea, hunt pivot)

## Victimology and targeting

Document without over-claiming:

- **Sectors and regions** — frequency, outliers, possible strategic rationale (as hypothesis)
- **Org profile** — size, tech stack, supply-chain position when relevant
- **Initial access vector trends** — shifts across campaign phases
- **Objectives** — espionage, destruction, pre-positioning, financial (label as assessment)

Avoid publishing victim identities beyond handling rules; use sector aggregates in broad briefs.

## Campaign products

**Campaign tracker (living):**

| Field | Content |
|---|---|
| Campaign ID | Internal identifier |
| Status | Active / dormant / closed |
| Summary | 3–5 bullets |
| Timeline | Key milestones UTC |
| ATT&CK highlights | Top techniques with procedures |
| Infrastructure/malware | Pointers to annex |
| Victimology | Sector/geo patterns |
| Confidence | Overall + per major link |
| Gaps | What is unknown |
| Consumers | Hunt, SOC, IR, leadership |
| Last updated | Date, analyst |

**Campaign flash (time-sensitive):**

- Bottom line, what changed, immediate defensive actions, confidence, handling
