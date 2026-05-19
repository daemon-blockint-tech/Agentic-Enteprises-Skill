---
name: senior-revenue-accountant
description: |
  Apply ASC 606/IFRS 15 to revenue recognition and contract analysis.
  Cover performance obligations, deferred revenue, commission accounting,
  revenue metrics (ARR, NRR, GRR), and audit preparation.
  Triggers on "revenue recognition", "ASC 606 compliance", "contract analysis",
  "deferred revenue schedule", "commission accounting", "revenue metrics",
  "revenue audit", "IFRS 15", or "revenue accounting policy".
---

# Senior Revenue Accountant

## Overview

Apply ASC 606/IFRS 15 to revenue recognition and contract analysis. This skill covers performance
obligations, deferred revenue, commission accounting, revenue metrics (ARR, NRR, GRR), and
audit preparation.

## Features

- ASC 606/IFRS 15 five-step revenue recognition model
- Contract analysis: performance obligations, transaction price allocation, variable consideration
- Deferred revenue scheduling: monthly amortization, contract modifications, renewals
- Commission accounting: capitalization, amortization, impairment testing
- Revenue metrics: ARR, NRR, GRR, churn, expansion calculation formulas
- Audit preparation: revenue rollforwards, contract testing, documentation packages

## Usage

1. Identify the user's revenue accounting need (recognition, contracts, deferred revenue, metrics, or audit)
2. Follow the corresponding workflow below
3. Produce structured outputs: revenue recognition memos, contract analyses, deferred revenue schedules, or audit packages

## Examples

- **User**: "Recognize revenue for a SaaS contract"
  **Agent**: Runs ASC 606 workflow, identifies performance obligations, allocates transaction price, produces recognition schedule

- **User**: "Calculate NRR"
  **Agent**: Runs Revenue Metrics workflow, gathers starting ARR, expansion, contraction, churn data, calculates NRR with formula

- **User**: "Prepare for revenue audit"
  **Agent**: Runs Audit Preparation workflow, creates revenue rollforward, samples contracts for testing, assembles documentation package

## When to Use

- Applying ASC 606 / IFRS 15 to contracts, POBs, SSP allocation, and modifications
- Running month-end revenue close, reconciliations, flux analysis, and journal entries
- Calculating SaaS metrics (ARR, MRR, NRR, GRR, RPO) and board-ready revenue reporting
- Preparing SOX controls, audit PBCs, and external auditor support

## When NOT to Use

- Customer support billing ops, dunning playbooks, or ticket SLAs → use `customer-ops-specialist`
- BI dashboards or exploratory product analytics → use `bi-analyst`
- Data pipeline reliability or warehouse incident management → use `data-system-ops-lead`
- General business requirements or process maps for non-finance systems → use `business-analyst`
- Commercial terms negotiation (liability, indemnity, DPA redlines) → use `commercial-counsel`
- Order form processing, deal desk, CRM-to-billing handoff → use `deal-operations-administrator`
- Business model canvas, market sizing, competitor pricing research → use `business-model-researcher`
- Compute capex, cloud COGS GL mapping, chargeback → use `compute-accounting-manager`

## Core Workflows

### 1. Revenue Recognition Workflow

**ASC 606 / IFRS 15 five-step model:**

1. **Identify the contract**
   - Signed agreement or enforceable commitment
   - Collectibility probable
   - Commercial substance exists

2. **Identify performance obligations (POBs)**
   - Distinct goods/services
   - Series guidance for recurring services
   - Material right identification

3. **Determine transaction price**
   - Fixed consideration
   - Variable consideration (constraints)
   - Significant financing component
   - Non-cash consideration

4. **Allocate to POBs**
   - Standalone selling price (SSP) for each POB
   - Residual approach when SSP not observable
   - Discount allocation patterns

5. **Recognize revenue**
   - Point in time vs over time
   - Input/output methods for over-time
   - Progress toward completion

### 2. Month-End Close Process

**Close calendar (days 0-10):**

| Day | Activity | Owner | Dependencies |
|---|---|---|---|
| 0 (Month-end) | Cutoff: stop entries | Controller | — |
| 1 | Preliminary close | All | — |
| 2 | Revenue waterfall | Revenue acct | Billing data |
| 3 | Deferred revenue rec | Revenue acct | Rev waterfall |
| 4 | AR reconciliation | Staff acct | Collections data |
| 5 | Flux analysis | Senior acct | All subledgers |
| 6 | Management review | Controller | Draft reports |
| 7 | Adjusting entries | Senior acct | Review comments |
| 8 | Final close | Controller | All clean |
| 9 | Board package | FP&A | Final numbers |
| 10 | Distribution | CFO | Board package |

### 3. SaaS Metrics & Reporting

**Key SaaS revenue metrics:**

| Metric | Formula | Use |
|---|---|---|
| ARR | Ending MRR × 12 | Run-rate revenue |
| Net Revenue Retention | (Starting + Expansion - Churn) / Starting | Growth efficiency |
| Gross Revenue Retention | (Starting - Churn) / Starting | Stickiness |
| ACV | Annual contract value per customer | Sales efficiency |
| TCV | Total contract value (multi-year) | Booking size |
| RPO | Remaining performance obligation | Future revenue |
| Billings | Cash collected + AR change | Cash proxy |

### 4. Audit & Compliance Support

**SOX control categories:**
- Entity-level controls ( tone at the top, integrity)
- IT general controls (access, change management, operations)
- Process-level controls (authorization, reconciliation, review)

**Audit preparation checklist:**
- [ ] PBC list items prepared 2 weeks ahead
- [ ] Contract sample selected (statistical or judgmental)
- [ ] SSP documentation current
- [ ] Journal entries supported
- [ ] Flux explanations documented
- [ ] Prior year adjustments addressed
