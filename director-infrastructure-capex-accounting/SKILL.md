---
name: director-infrastructure-capex-accounting
description: |
  Guides director-level infrastructure capex accounting—capitalization policy and governance,
  WIP/CIP and project closeout, useful-life and impairment standards, capex forecast vs actual
  for data center and compute programs, board and audit narratives, SOX over fixed-asset and
  cloud-prepaid programs, and alignment with engineering and portfolio delivery.
  Use when setting capex accounting policy, reviewing material capitalization judgments,
  governing infrastructure asset programs, executive capex reporting, or audit steering for
  DC/compute investments—not for month-end JEs and CUR mapping (compute-accounting-manager),
  rack utilization (data-center-compute-supply-efficiency), facility design (data-center-design-execution-lead),
  or multi-site investment prioritization (data-center-portfolio-planning-execution-lead).
---

# Director, Infrastructure Capex Accounting

## When to Use

- Define or update **infrastructure capitalization policy** (hardware, DC build, cloud prepaids at scale)
- Adjudicate **material capex vs OpEx** and project accounting treatment
- Govern **WIP/CIP** through in-service and asset capitalization for builds
- Set **useful life, salvage, and impairment** standards for compute and facility assets
- Own **capex forecast** alignment with FP&A and engineering roadmaps
- Prepare **board, audit committee, or controller** narratives on infrastructure spend
- Design **SOX controls** over capitalization, disposals, and master data
- Steer **external audit** on fixed assets, prepaids, and construction projects

## When NOT to Use

- Operational close: cloud CUR mapping, depreciation runs → `compute-accounting-manager`
- ASC 606 revenue and deferred revenue → `senior-revenue-accountant`
- MW delivery program RAID → `senior-data-center-capacity-delivery-manager`
- Which sites to fund next → `data-center-portfolio-planning-execution-lead`
- MEP design and commissioning specs → `data-center-design-execution-lead`
- Control evidence automation packs → `compliance-engineer` (partner; director sets policy)
- Infrastructure portfolio, capex envelope, executive narratives → `vp-of-infrastructure`

## Related skills

| Need | Skill |
|---|---|
| Operational compute accounting | `compute-accounting-manager` |
| DC utilization and refresh economics | `data-center-compute-supply-efficiency` |
| Capacity delivery milestones | `senior-data-center-capacity-delivery-manager` |
| Enterprise DC portfolio steering | `data-center-portfolio-planning-execution-lead` |
| Facility design and commissioning | `data-center-design-execution-lead` |
| Field install and asset serials | `field-services-engineer` |
| SOX evidence and control mapping | `compliance-engineer` |
| Cross-team program tracking | `technical-program-manager` |
| Executive messaging | `communication-lead` |
| VP infrastructure leadership | `vp-of-infrastructure` |

## Core Workflows

### 1. Capex policy and governance

Thresholds, roles, escalation, policy exceptions.

**See `references/capex_policy_governance.md`.**

### 2. WIP/CIP and project capitalization

Construction and hardware projects through in-service.

**See `references/wip_cip_capitalization.md`.**

### 3. Capex forecast and executive reporting

Plan vs actual, variance drivers, board pack.

**See `references/capex_forecast_reporting.md`.**

### 4. Fixed-asset and prepaid program controls

SOX, audit PBCs, subledger governance.

**See `references/fixed_asset_program_controls.md`.**

### 5. Useful life, impairment, and disposals

Policy changes, triggering events, write-offs.

**See `references/useful_life_impairment.md`.**

### 6. Cross-functional alignment

Engineering, FP&A, tax, treasury, legal.

**See `references/cross_functional_alignment.md`.**

## Outputs

- **Policy memo** or accounting manual section for infrastructure capex
- **Capitalization decision log** — material judgments with approver
- **Capex bridge** — budget → commitments → WIP → placed in service → depreciation run-rate
- **Audit steering brief** — open items, estimates, timing
- **Board slide** — spend, runway, efficiency metrics tied to accounting view

## Principles

- **Policy before transactions** — train deal owners and engineering on thresholds early
- **One asset truth** — align CMDB/serial data, procurement, and fixed-asset register
- **Separate roles** — policy owner (director) vs operational accounting (`compute-accounting-manager`)
- **Not tax or legal advice** — lease classification, credits, transfer pricing to specialists
- **Tie to delivery truth** — in-service dates follow rack-ready / go-live, not PO date alone
