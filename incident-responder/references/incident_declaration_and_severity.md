# Incident declaration and severity

## Table of contents

1. [When to declare](#when-to-declare)
2. [Declaration checklist](#declaration-checklist)
3. [Severity model](#severity-model)
4. [Reclassification](#reclassification)
5. [SOC escalation criteria](#soc-escalation-criteria)

## When to declare

Declare a **security incident** when any of the following apply:

- Confirmed unauthorized access to production, corporate, or customer systems
- Malware or ransomware execution on managed endpoints or servers
- Suspected or confirmed **personal data** or regulated data exposure
- Compromise of privileged identity, break-glass, or CI/CD signing secrets
- Active command-and-control or ongoing attacker activity
- Supply-chain or third-party compromise affecting your environment
- Law enforcement or regulator inquiry tied to a security event

**Do not** require declaration for every SOC alert—`soc-analyst` closes benign/true-positive alerts per runbook.

## Declaration checklist

1. Assign **incident ID** and title (type + primary asset)
2. Record **declarer**, **time (UTC)**, and **trigger source**
3. Set **severity** with one-line rationale
4. Open **incident channel** and record link in ticketing system
5. Assign **IC** and **CSIRT lead**; page per matrix
6. Notify **legal** for SEV1–2 or any data exposure suspicion
7. Publish initial **scope hypothesis** (systems, accounts, data classes)—mark as preliminary
8. Start **timeline** and **action tracker**

## Severity model

Align with org `incident-management-engineer` SEV definitions where they exist. Example security-focused mapping:

| Level | Customer / business impact | Data | Response |
|---|---|---|---|
| SEV1 | Widespread outage or major breach; ransomware active | Confirmed or highly likely regulated data exfil | Immediate 24/7; exec + legal |
| SEV2 | Limited production impact; contained segment | Possible regulated data; investigation ongoing | < 1 h engagement; legal informed |
| SEV3 | Minimal customer impact; single system | No confirmed regulated data | Same business day |
| SEV4 | Policy violation; blocked attack; near-miss | None | Track; optional formal IR |

**Severity drivers (use highest that applies):**

- Number of users or tenants affected
- Privilege level of compromised accounts
- Data classification (public → confidential → regulated)
- Attacker persistence (active vs contained)
- Regulatory or contractual notification pressure

## Reclassification

- Reclassify when scope expands (new systems, new data class) or containment confirmed
- Document **old → new** severity, reason, and time in incident record
- Adjust comms cadence and staffing immediately on upgrade

## SOC escalation criteria

`soc-analyst` should escalate to CSIRT when:

- Multiple correlated alerts across identity, endpoint, and cloud
- Alert on Tier-0 assets (IdP, billing, prod admin, secrets store, CI signing)
- Unable to rule out data access within SLA (e.g., 30–60 minutes)
- User or customer report corroborates malicious activity
- Playbook step requires IR authority (legal hold, org-wide password reset, mass session revoke)

Escalation ticket must include UTC timestamps, entities, and evidence links.
