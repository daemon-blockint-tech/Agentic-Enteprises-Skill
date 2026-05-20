# IOC enrichment and investigation

## Table of contents

1. [IOC types and handling](#ioc-types-and-handling)
2. [Enrichment sources](#enrichment-sources)
3. [Correlation queries](#correlation-queries)
4. [Timeline construction](#timeline-construction)
5. [Investigation depth by tier](#investigation-depth-by-tier)

## IOC types and handling

| IOC | Validate | Notes |
|---|---|---|
| File hash | Prevalence, signature, sandbox summary | Treat unknown hash as suspicious on critical assets |
| IP / domain | TI reputation, passive DNS, registration age | Shared hosting needs host-level context |
| URL | Redirect chain, domain age, path | Do not click untrusted URLs on analyst workstation |
| User / UPN | Role, MFA status, recent auth geography | Executive and break-glass = escalate early |
| Host | Criticality, owner, EDR coverage | Missing EDR = escalate |
| Process | Parent chain, signer, path | LOLBins need parent context |

Record **confidence** (high/medium/low) per IOC in case notes.

## Enrichment sources

Use org-approved sources only:

- **Internal** — CMDB, asset tags, data classification, recent changes
- **SIEM** — historical prevalence, peer alerts, peer entities
- **EDR** — process tree, network connections, file operations
- **Identity** — sign-in logs, risky sign-in, MFA events, app consents
- **Email** — message headers, delivery path, similar campaigns
- **Cloud** — CloudTrail/Audit Logs, IAM changes, storage access
- **Threat intel** — feeds integrated in SIEM; cite feed name and score

Do not paste full TI reports into customer-visible tickets; summarize in case.

## Correlation queries

Minimum pivots for true positives:

1. **Same user** — auth, cloud, proxy, email (24–72h)
2. **Same host** — EDR, local logons, outbound connections
3. **Same IOC** — other hosts/users hit (prevalence)
4. **Parent process** — if execution alert, trace parent and child

Stop correlation when runbook depth reached; hand off breadth to `defensive-security-analyst`.

## Timeline construction

**Required fields per event:**

| Field | Example |
|---|---|
| `timestamp_utc` | `2026-05-20T14:32:01Z` |
| `entity` | `host:wkst-042` / `user:jane@corp` |
| `action` | `Sign-in success from new country` |
| `source` | `IdP sign-in logs` |
| `analyst_note` | `Matches phishing case #1234` |

Order chronologically; mark **first malicious** and **last observed** activity.

## Investigation depth by tier

| Tier | Depth | Stop condition |
|---|---|---|
| T1 | Enrichment + playbook + single-source timeline | Escalate if multi-source needed |
| T2 | Multi-source timeline + containment recommendation | Escalate if hunt hypothesis required |
| T3 | Full case package for IR; tuning proposal | Hand to IR commander for SEV1–2 |

Preserve chain of custody: export raw logs to secure case folder per policy.
