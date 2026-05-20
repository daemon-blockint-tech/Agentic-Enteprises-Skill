# SIEM and SOAR playbooks

## Table of contents

1. [Playbook principles](#playbook-principles)
2. [Standard playbook stages](#standard-playbook-stages)
3. [SOAR case hygiene](#soar-case-hygiene)
4. [Approved automation](#approved-automation)
5. [When to stop automation](#when-to-stop-automation)

## Playbook principles

1. **Human decision at branches** — automation gathers; analysts approve destructive steps
2. **Idempotent steps** — safe to re-run enrichment without duplicate blocks
3. **Evidence first** — export logs/snapshots before isolate or disable when policy requires
4. **Mapped to category** — each playbook names severity default and escalation path
5. **Versioned** — cite playbook ID and version in every case note

## Standard playbook stages

| Stage | Actions | Outputs |
|---|---|---|
| **Ingest** | Parse alert; open case; assign owner | Case ID, entities |
| **Enrich** | TI lookup, asset CMDB, user manager, geo | Enrichment block in case |
| **Correlate** | Same-user/host queries; 24h window | Related alert count |
| **Decide** | FP / monitor / investigate / escalate | Decision + rationale |
| **Respond** | Approved SOAR actions only | Action log with UTC |
| **Resolve** | Close code; tuning ticket if FP | Final category + severity |
| **Retrospect** | Optional lesson for detection review | Link to tuning ticket |

## SOAR case hygiene

Every case must include:

- **Title** — `[Category] — primary entity — short behavior`
- **Timeline** — append-only notes with UTC timestamps
- **Evidence links** — SIEM search IDs, EDR investigation URLs (no secrets in title)
- **Owner and tier** — T1/T2/T3 at time of handoff
- **Related tickets** — IR, IT, cloud, legal as applicable

Update status when waiting on: approver, customer, engineering, or legal.

## Approved automation

Typical auto-actions (confirm against org runbook):

| Action | Preconditions |
|---|---|
| Block IOC at proxy/firewall | TI confidence high; not shared CDN without scope |
| Disable user session | Confirmed compromise; not service account without owner |
| EDR network isolate | Active malware; asset not critical singleton without approval |
| Quarantine file | EDR policy allows; hash seen on single host first |
| Create ticket | Always allowed — route to correct queue |

Require **secondary approval** for org-wide blocks, production service accounts, and executive users.

## When to stop automation

Halt SOAR and escalate manually when:

- Playbook branch missing or confidence below threshold
- Blast radius unclear (cloud org, IdP tenant, >10 assets)
- Destructive action could interrupt revenue-critical system
- Alert storm — possible detection bug or attack in progress at scale
- Legal hold or law enforcement involvement mentioned

Log **automation halted** reason in case; do not force-close as FP during storms.
