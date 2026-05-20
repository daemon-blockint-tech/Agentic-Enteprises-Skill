# SOC analyst scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [Tier model](#tier-model)
3. [Partnership model](#partnership-model)
4. [What good looks like](#what-good-looks-like)

## Role boundary

| SOC analyst owns | Others own |
|---|---|
| Alert queue triage and case documentation | SEV taxonomy, paging, postmortems (`incident-management-engineer`) |
| Playbook and SOAR case execution | SIEM/EDR/SOAR integration engineering (`information-security-engineer`) |
| Initial severity/category classification | Enterprise IR strategy and policy (`cybersecurity`) |
| IOC enrichment and analyst timelines | Deep hunts and detection rule design (`defensive-security-analyst`) |
| Runbook containment recommendations | Control implementation and guardrails (`information-security-engineer`, `cloud-security-engineer`) |
| Shift handoffs and tuning feedback | Audit evidence and frameworks (`compliance-engineer`) |
| Escalation packages for IR/engineering | Pentest and offensive validation (`offensive-security-analyst`) |

**SOC** operates the **detection and response floor**; it does not own security program design or infrastructure build-out.

## Tier model

| Tier | Typical work | Escalate when |
|---|---|---|
| **T1** | Queue intake, enrichment, known-FP closure, playbook branches A/B | Unknown alert type, executive account, multi-host scope |
| **T2** | Correlation across sources, timeline build, containment per runbook | Cross-tenant, regulated data, unclear root cause |
| **T3** | Complex cases, playbook gaps, tuning proposals, mentor T1 | Active breach commander needed, legal hold, org-wide block |

Tiers are **skills**, not titles—document who owns the case at handoff.

## Partnership model

| Partner | Interaction |
|---|---|
| IR / defensive analyst | Receives escalations with timeline, IOCs, recommended actions |
| Detection engineering | Consumes tuning tickets; provides rule context and test windows |
| IT / identity | Executes approved account resets, group changes |
| Cloud / platform | Assists with cloud audit queries and resource isolation |
| Legal / comms | Engaged only via IR commander (`communication-lead` for messaging) |
| IM engineer | Aligns case severity to SEV definitions; does not replace SOC triage |

## What good looks like

1. Every true positive has a **UTC timeline** with cited sources
2. False positives exit with a **tuning ticket**, not silent suppression
3. Playbook actions are **logged** and **approved** per policy
4. Shift handoff is **written**—no verbal-only transfer of SEV1–2 cases
5. Metrics improve: lower FP rate, stable time-to-triage, fewer reopen loops
