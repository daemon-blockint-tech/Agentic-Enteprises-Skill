# Stakeholder and regulatory communications

## Table of contents

1. [Principles](#principles)
2. [Audiences and cadence](#audiences-and-cadence)
3. [Update template](#update-template)
4. [Executive summary](#executive-summary)
5. [Customer and partner messaging](#customer-and-partner-messaging)
6. [Regulatory notification preparation](#regulatory-notification-preparation)
7. [What not to say](#what-not-to-say)

## Principles

- **Facts vs hypotheses**: label clearly; update when facts change
- **Single voice**: comms lead drafts; legal approves external/regulatory text
- **No legal advice**: CSIRT supplies timelines and technical facts; legal decides obligations
- **Consistent numbers**: one source of truth for affected counts (versioned)
- **Privilege**: mark sensitive counsel communications appropriately per org policy

## Audiences and cadence

| Audience | Owner | Typical cadence (SEV1) |
|---|---|---|
| Incident team | IC | Continuous in channel |
| Engineering leadership | IC / CSIRT | Every 30–60 min until stable |
| Executive | IC + comms | Every 60 min or per charter |
| All staff | Comms | As needed; avoid speculation |
| Customers | Comms + legal | When material impact confirmed |
| Partners / regulators | Legal | Per legal direction only |

Align cadence with `incident-management-engineer` program; use `communication-lead` for polished crisis packs.

## Update template

**Subject:** `[INC-####] Security incident update — YYYY-MM-DD HH:MM UTC`

1. **Status** — Investigating / Contained / Eradicating / Recovering / Monitoring / Closed  
2. **Severity** — SEV# (unchanged / upgraded / downgraded since last update)  
3. **Customer impact** — Known / None identified / Under investigation  
4. **Facts since last update** — Bullet list with UTC times  
5. **Actions in progress** — Owner per line  
6. **Next update** — Time (UTC)  
7. **Open questions** — Only if useful for decision-makers  

## Executive summary

One page max:

- What happened (one paragraph, factual)
- Scope: systems, data classes, geographies, tenant count (ranges if uncertain)
- Current status and time to next milestone
- Decisions needed (resources, customer comms, law enforcement)
- Regulatory touchpoints flagged for legal (yes/no/unknown)

## Customer and partner messaging

- Do not disclose IOCs or TTPs that aid copycat attacks without security review
- Avoid blaming users; describe protective actions taken
- Provide actionable steps for customers (rotate API keys, review audit logs) only when validated
- Offer support channel and reference number

Route all external copy through **legal** and **comms** before send.

## Regulatory notification preparation

CSIRT prepares a **fact pack** for legal/compliance (`compliance-engineer` supports evidence structure—not legal determinations):

| Field | Content |
|---|---|
| Discovery date/time (UTC) | |
| Incident type | |
| Categories of personal data | |
| Approximate number of data subjects | Ranges with confidence level |
| Likely geographic residence of subjects | |
| Containment measures | |
| Remediation in progress | |
| Third parties involved | Processors, subprocessors |
| Cross-border transfer relevance | If known |
| Prior related incidents | |

Legal assesses GDPR, state breach laws, sector rules (HIPAA, PCI, etc.), and contract notice clauses. **Do not** promise notification timelines in technical channels.

## What not to say

- Definitive “no data was accessed” before log proof
- Attribution to named threat actors without approved intel
- Legal conclusions or regulatory filing commitments
- Unverified attacker demands or ransom status in customer channels
