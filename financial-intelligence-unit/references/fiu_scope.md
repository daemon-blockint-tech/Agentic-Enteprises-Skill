# FIU scope

## Table of contents

1. [Mission](#mission)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Handoffs](#handoffs)
5. [Operating principles](#operating-principles)
6. [Deliverable patterns](#deliverable-patterns)

## Mission

Operate the **Financial Intelligence Unit (FIU)** as the investigative and analytical arm of an AML/CFT program. Convert alerts and referrals into **defensible case files**: triage, financial analysis, typology testing, documentation, quality review, and **MLRO-ready escalation packs**. Optimize for **throughput with quality**, clear audit trails, and feedback into transaction monitoring—not for substituting enterprise policy design, legal filing decisions, or IT audit fieldwork.

## In scope

| Domain | Examples |
|---|---|
| **Intake & triage** | Queue management, prioritization, duplicate handling, disposition codes |
| **Investigation** | Flow reconstruction, counterparty mapping, product/channel context |
| **Typologies** | ML patterns (structuring, layering, mules, trade-based ML, crypto/VASP) |
| **Case documentation** | Chronology, exhibit index, hypotheses tested, analyst notes |
| **QA / peer review** | Sampling, rework, standards, lessons learned |
| **MLRO escalation** | Fact packs, suspicion elements, gaps, options (not filing advice) |
| **Internal reporting** | Backlog, SLA, typology mix, outcome metrics, management MI |
| **Coordination** | TM tuning input, compliance second line, fraud/security investigations |
| **Training & handover** | Playbooks, shadowing, shift handover checklists |

## Out of scope

| Topic | Route to |
|---|---|
| Enterprise AML/CFT **policy**, risk assessment, KYC program design | `aml-compliance` |
| **STR/SAR narrative** drafting as primary filing deliverable | `str-report` |
| **CFT/PF-only** programs, TFS/asset freeze, NPO sector controls | `aml-cft` |
| **Internal/IT audit** workpapers and control testing | `auditor` |
| **Technical** evidence automation, SOC/ISO control implementation | `compliance-engineer` |
| **Legal** filing duty, regulator strategy, entity structuring | `commercial-counsel` |
| Deep **sentiment/NLP** pipelines for media | `sentiment-analysis-engineer` |
| Primary **blockchain LE** investigation reports | blockint skills |

## Handoffs

**From transaction monitoring / first line:**

- Provide: alert ID, scenario, thresholds, lookback, customer profile snapshot, prior alerts
- Receive: disposition, tuning feedback, and documented rationale for closure or escalation

**To MLRO / `str-report`:**

- Deliver: verified fact pack, chronology, suspicion mapping, exhibit index, open questions
- Request: STR/SAR narrative drafting when filing preparation is the next step—not duplicate investigation

**To `aml-compliance`:**

- Escalate: systemic control gaps, policy exceptions, program-level risk changes
- Do not: rewrite enterprise AML policy inside a single case file

**To `auditor`:**

- Provide: sample cases, QA results, disposition codes, access logs for independent review
- Distinguish: FIU QA (second-line operations) vs third-line audit plan

**To blockint / investigation skills:**

- Request: on-chain traces and entity labels with **confidence**; FIU owns case disposition and internal narrative

## Operating principles

- **Investigate to standard** — same minimum steps for like cases; avoid ad hoc shortcuts
- **Document as you go** — contemporaneous notes; reconstructable by another analyst
- **Separate facts and inference** — label assumptions and data gaps explicitly
- **Escalate early** — complex typologies, high amounts, PEP/sanctions touchpoints, media attention
- **Protect confidentiality** — need-to-know access; no casual sharing of suspicion details
- **No legal conclusions** — describe suspicious indicators; MLRO/counsel decide filings

## Deliverable patterns

| Deliverable | Contents |
|---|---|
| **Triage note** | Source, priority, minimum data check, route/assign |
| **Investigation memo** | Chronology, flows, typology assessment, innocent explanations |
| **MLRO pack** | Executive summary, facts, suspicion elements, gaps, recommendation options |
| **QA record** | Reviewer, findings, rework required, sign-off |
| **MI slide / table** | Volumes, aging, outcomes, top typologies, SLA breach drivers |
