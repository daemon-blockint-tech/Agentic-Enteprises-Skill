# AML/CFT scope

## Table of contents

1. [Mission](#mission)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Relationship to aml-compliance](#relationship-to-aml-compliance)
5. [Handoffs](#handoffs)
6. [Operating principles](#operating-principles)

## Mission

Support **counter-terrorist financing (CFT)** and **proliferation financing (PF)** compliance and risk management: identify TF/PF exposure, apply typology-led controls, integrate **targeted financial sanctions (TFS)** and asset freezes, and prepare governance and reporting artifacts. Optimize for **purpose-based suspicion** (terrorist or proliferation aims) and **sanctions immediacy**—not for rebuilding enterprise-wide AML customer due diligence or transaction monitoring programs.

## In scope

- **CFT/PF risk assessment** slices (products, channels, geographies, customer types with TF/PF elevation)
- **Terrorist financing typologies** and investigation playbooks (distinct from ML patterns)
- **Proliferation financing** and **dual-use** goods red flags in trade and correspondent contexts
- **TFS** alignment, designation handling, **asset freeze** operational steps (conceptual)
- **CFT-specific STR/SAR** narrative structure and internal escalation packages
- **NPO/nonprofit** sector due diligence and proportionate de-risking
- **MVTS**, remittance, and informal value transfer **TF** risks
- **Correspondent** and **cross-border** TF vulnerabilities
- High-level mapping to **FATF Recommendations 6–8** and related guidance
- **Sanctions screening** integration with CFT disposition and freeze holds
- **CFT training**, **independent review**, and **exam readiness** for TF/PF topics

## Out of scope

| Topic | Route to |
|---|---|
| Full AML program design (KYC tiers, CDD/EDD, PEP, broad TM) | `aml-compliance` |
| SOC 2, ISO 27001, HIPAA technical control evidence | `compliance-engineer` |
| IT audit workpapers, COSO, ITGC without CFT lens | `auditor` |
| Legal advice, filing sufficiency, regulatory strategy | `commercial-counsel` / MLRO |
| SIEM rule build, screening engine implementation | `information-security-engineer` |
| Sanctions API/oracle engineering only | `chainalysis-sanctions-screening` |
| Law enforcement investigation, attribution, chain tracing | blockint skills |
| Sanctions list curation or government list maintenance | Competent authorities / list publishers |

## Relationship to aml-compliance

| Dimension | `aml-compliance` | `aml-cft` (this skill) |
|---|---|---|
| Primary focus | Risk-based AML program, KYC/CDD, TM, SAR/STR program | TF typologies, PF, TFS, NPO/MVTS, CFT narratives |
| FATF emphasis | Broader Recommendations (10–23 program elements) | **R6–R8** (TFS, PF, NPO) and TF purpose |
| Customer work | CDD/EDD tiers, beneficial ownership, refresh | NPO due diligence, MVTS oversight, correspondent TF |
| Monitoring | ML scenarios, structuring, mule patterns | TF typology scenarios, sanctions freeze triggers |
| Reporting | General SAR/STR program | **CFT-flavored** fact packs and TF purpose indicators |
| When to use both | New product launch affecting NPO/MVTS/correspondent | Start aml-compliance for program shell; aml-cft for TF/PF slice |

Use **aml-compliance** first when the user needs an enterprise AML framework. Use **aml-cft** when the question is specifically terrorist financing, proliferation, TFS, asset freezes, or FATF R6–R8—not when they only mention "AML program" without CFT/PF context.

## Handoffs

**From `aml-compliance`:**

- Receive: customer tiers, screening stack, TM governance, MLRO escalation paths
- Add: TF/PF typology coverage, NPO/MVTS procedures, TFS freeze runbooks, CFT exam topics

**To `aml-compliance`:**

- Return: gaps in CDD/TM that affect CFT (e.g., missing BO for trade finance) for program-level remediation

**To `commercial-counsel`:**

- Escalate: freeze legality, license applications, regulatory interpretation, filing decisions

**To `information-security-engineer`:**

- Request: screening API integration, case management workflows, audit logs—not CFT policy content

## Operating principles

- **Purpose over placement** — TF can involve small, seemingly legitimate flows; document terrorist **purpose** indicators
- **Do not duplicate aml-compliance** — link to existing KYC/TM where sufficient; extend only for CFT/PF gaps
- **Sanctions first** — TFS matches override normal payment processing pending disposition
- **Risk-based NPO approach** — comply with FATF NPO guidance spirit; avoid discriminatory blanket exits without governance
- **No legal determinations** — operational guidance only; counsel/MLRO owns filings and regulatory communications
