# STR report scope

## Table of contents

1. [Purpose and boundaries](#purpose-and-boundaries)
2. [Definitions](#definitions)
3. [STR vs SAR vs internal artifacts](#str-vs-sar-vs-internal-artifacts)
4. [Roles and responsibilities](#roles-and-responsibilities)
5. [Inputs and outputs](#inputs-and-outputs)
6. [What this skill does not cover](#what-this-skill-does-not-cover)
7. [Quality principles](#quality-principles)

## Purpose and boundaries

This reference defines the **operational scope** of suspicious transaction / suspicious activity reporting narrative work. The goal is a **regulator-ready or MLRO-ready fact narrative** that explains why activity is suspicious—not to replace investigation, legal advice, or transaction monitoring engineering.

| In scope | Out of scope |
|---|---|
| Narrative structure and drafting | TM rule design, threshold tuning |
| Fact aggregation and chronology | Full blockchain forensic engagement |
| Red-flag-to-fact mapping | Legal determination to file |
| Subject/transaction field completeness | Law enforcement tactical briefing |
| QA checklist before filing | Sanctions list vendor configuration |

Always align drafts to the institution’s **approved STR/SAR policy**, **retention schedule**, and **MLRO authority matrix**.

## Definitions

| Term | Typical meaning (jurisdiction varies) |
|---|---|
| **STR** | Suspicious transaction report filed with FIU or supervisor (common in EU and many jurisdictions) |
| **SAR** | Suspicious activity report (US FinCEN Form 111 and similar) |
| **FIU** | Financial intelligence unit receiving reports |
| **MLRO** | Money laundering reporting officer (or equivalent second line) |
| **Subject** | Customer or party about whom suspicion is reported |
| **Counterparty** | Other party to transactions (may be unknown or nested) |
| **Continuing activity** | Ongoing suspicious pattern requiring follow-up or amended reports per policy |

Use **`fatf-glossary-reference`** for authoritative FATF terms when precision matters.

## STR vs SAR vs internal artifacts

| Artifact | Audience | Content emphasis |
|---|---|---|
| **STR/SAR (regulatory)** | FIU / supervisor via MLRO | Facts, suspicion basis, identifiers, chronology, minimal speculation |
| **Internal case notes** | Analysts, investigators | Working hypotheses, system screenshots, tentative leads |
| **Management summary** | Committee, non-AML executives | Risk rating, actions taken, no excessive PII |
| **Law enforcement referral** | Police, agency task forces | May include tactical detail; often separate from STR narrative |
| **Audit workpapers** | Internal/external audit | Control testing—not suspicion storytelling |

**Do not paste** internal speculation, unverified OSINT, or privileged counsel advice into STR narratives without MLRO review.

### When narratives diverge

- **STR/SAR**: stick to **verified** or **reasonably believed** facts; label gaps
- **Internal**: capture **alternative explanations** under investigation
- **LE package**: coordinate through **legal/compliance**; avoid duplicate contradictory stories

## Roles and responsibilities

| Role | Typical duties in STR workflow |
|---|---|
| **Front-line / business** | Initial unusual activity awareness, customer context |
| **AML analyst** | Alert review, fact gathering, draft narrative, exhibit index |
| **Investigator** (if separate) | Deep dive, external research within policy |
| **MLRO / compliance** | Filing decision, quality sign-off, regulator liaison |
| **Legal** | Privilege review, LE coordination, novel legal questions |
| **Audit** | Later assurance on process—not primary narrative author |

Escalate when: **PEP/sanctions** nexus, **terrorist financing** indicators, **reputational** crisis, **cross-border** complexity, or **tipping-off** risk in communications.

## Inputs and outputs

### Minimum inputs

- Case / alert ID and source system
- Customer master data (legal name, IDs, addresses, BO where known)
- Account and product list in scope
- Transaction export with timestamps, amounts, currencies, channels, counterparties
- Prior STR/SAR history (if any) and EDD/KYC summary
- Analyst investigation memo (facts only for narrative extraction)
- List of **documents reviewed** (statements, KYC files, contracts, blockchain analytics summary)

### Standard outputs

1. **Executive summary** (3–6 sentences)
2. **Full narrative** (who / what / when / where / why)
3. **Chronology table** (date, event, amount, account, reference)
4. **Subject and account appendix**
5. **Red-flag index** linked to facts
6. **Exhibit / documentation checklist**
7. **Open questions** for MLRO

## What this skill does not cover

| Topic | Route to |
|---|---|
| Enterprise AML program, CDD tiers, TM scenarios | `aml-compliance` |
| CFT/TF-specific typologies and TFS workflows | `aml-cft` |
| Technical SOC/ISO evidence | `compliance-engineer` |
| IT audit sampling and workpapers | `auditor` |
| Whether filing is legally required | `commercial-counsel` + MLRO |
| On-chain tracing methodology | blockint skills |

## Quality principles

1. **Traceability** — each suspicious assertion maps to a transaction, document, or verified statement
2. **Neutrality** — describe behavior; avoid labeling customers as criminals
3. **Completeness** — identifiers sufficient for FIU to act (within policy)
4. **Concision** — regulators read volume; avoid duplicate tables
5. **Consistency** — amounts and dates match across narrative, tables, and exhibits
6. **Confidentiality** — respect tipping-off and need-to-know distribution
