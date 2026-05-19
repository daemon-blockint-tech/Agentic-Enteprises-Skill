---
name: senior-revenue-accountant
description: |
  Guides senior revenue accountants in revenue recognition, month-end close, SaaS metrics, and audit support.
  Covers ASC 606 / IFRS 15 (contract review, performance obligations, SSP allocation, modifications),
  month-end close procedures, reconciliations, ARR/MRR reporting, board metrics, SOX controls, and audit preparation.
  Use when analyzing revenue contracts, preparing journal entries, performing flux analysis, calculating SaaS metrics,
  building board reports, or supporting internal/external audits.
---

# Senior Revenue Accountant

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

**See `references/revenue_recognition.md` for contract review checklists, SSP methodologies, and modification accounting.**

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

**See `references/close_operations.md` for close checklists, reconciliations, and journal entry templates.**

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

**See `references/reporting_metrics.md` for metric calculations, board reporting templates, and forecasting.**

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

**See `references/compliance_audit.md` for SOX documentation, audit response templates, and control testing.**

## When to Load References

- **Revenue recognition** → `references/revenue_recognition.md`
- **Close operations** → `references/close_operations.md`
- **Reporting & metrics** → `references/reporting_metrics.md`
- **Compliance & audit** → `references/compliance_audit.md`
