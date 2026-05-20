# Escalation and MLRO handoff

## Table of contents

1. [Escalation triggers](#escalation-triggers)
2. [MLRO pack structure](#mlro-pack-structure)
3. [Suspicion mapping](#suspicion-mapping)
4. [Options and recommendations](#options-and-recommendations)
5. [Handoff to STR drafting](#handoff-to-str-drafting)
6. [Post-MLRO actions](#post-mlro-actions)

## Escalation triggers

Escalate to MLRO (or designated delegate) when any apply:

- Policy **mandatory escalation** (amount, typology, PEP, sanctions nexus)
- **Unresolved** suspicion after investigation steps completed
- **Repeat** subject with prior STR consideration or open regulatory matter
- **Cross-border** or multi-entity complexity beyond analyst authority
- **Media, law enforcement, or partner bank** involvement
- **Control failure** or systemic issue affecting multiple customers
- Analyst **recommends** STR/SAR consideration regardless of threshold

Document **who** escalated, **when**, and **prior reviews** (QA sign-off where required).

## MLRO pack structure

| Section | Content |
|---|---|
| **Cover** | Case ID, entity, subjects, analyst, dates, classification |
| **Executive summary** | 5–10 sentences: what happened, why it matters, recommended next step |
| **Subject profile** | Customer type, CDD tier, PEP/sanctions, relationship length |
| **Chronology** | Key dates and events (table) |
| **Financial summary** | Aggregated amounts, accounts, corridors, instruments |
| **Suspicion mapping** | Facts linked to typologies / red flags |
| **Innocent explanations** | Tested and outcome |
| **Gaps** | Missing data; follow-up owner |
| **Exhibits** | Numbered index with description |
| **Prior history** | Alerts, cases, filings (internal reference only) |
| **Options** | See below—not a legal filing decision |

Restrict distribution per **need-to-know**; watermark or classify per policy.

## Suspicion mapping

Use a matrix:

| Red flag / indicator | Supporting fact (tx ID, date, amount) | Typology | Analyst assessment |
|---|---|---|---|
| Example: rapid movement | Tx list attached | Layering | Supported |

Avoid **legal conclusions** (“money laundering proved”). Use **suspicious indicators** language aligned to internal policy and FATF concepts via `fatf-glossary-reference` when helpful.

## Options and recommendations

Present **options**, not decisions, for MLRO:

| Option | When appropriate |
|---|---|
| **Close with rationale** | Hypotheses tested; innocent explanation evidenced; low residual risk |
| **Continue investigation** | Gaps remediable; additional lookback needed |
| **STR/SAR consideration** | Indicators meet internal threshold; hand to narrative drafting |
| **Refer CFT** | TF/PF-specific angle → coordinate with `aml-cft` |
| **Refer fraud / security** | Non-AML primary |
| **Exit / offboard** | Policy-driven relationship decision (with compliance approval) |
| **Law enforcement liaison** | Per policy and counsel guidance |

MLRO selects option; **do not** state “must file” unless user explicitly requests counsel skill.

## Handoff to STR drafting

When MLRO directs STR/SAR preparation:

1. Transfer **MLRO pack** and exhibit index to `str-report` workflow
2. Avoid duplicating investigation—narrative skill assembles **who/what/when/where/why**
3. List **open questions** for narrative author explicitly
4. Maintain case **master record** in FIU system of record

## Post-MLRO actions

- Record MLRO **decision, date, and rationale** in case system
- If closed: apply **closure code** and TM feedback
- If STR path: track **draft, review, approval** statuses (FIU may QA facts, not replace MLRO sign-off)
- Schedule **retrospective** for systemic issues (tuning, training, policy)
- **Retention** per jurisdictional schedule; restrict access post-filing
