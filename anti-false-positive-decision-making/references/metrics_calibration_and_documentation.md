# Metrics, calibration, and documentation

## Table of contents

1. [Metric hierarchy](#metric-hierarchy)
2. [Precision, recall, and FDR](#precision-recall-and-fdr)
3. [Labels and lag](#labels-and-lag)
4. [Calibration program](#calibration-program)
5. [Sampling methodology](#sampling-methodology)
6. [Documentation artifacts](#documentation-artifacts)
7. [Audit and regulatory readiness](#audit-and-regulatory-readiness)
8. [Dashboards](#dashboards)
9. [Failure modes](#failure-modes)

## Metric hierarchy

| Level | Question | Audience |
|---|---|---|
| L1 — Volume | How many alerts? | Ops capacity |
| L2 — Efficiency | How fast disposed? | Ops management |
| L3 — Quality | Were dispositions correct? | Risk, audit |
| L4 — Outcome | Loss prevented vs harm? | Executive |

**Anti-FP programs optimize L3–L4**, not L1 alone.

## Precision, recall, and FDR

| Metric | Formula | Use |
|---|---|---|
| Precision | TP / (TP + FP) | Trust in positive decisions |
| Recall | TP / (TP + FN) | Coverage of true harm |
| FDR | FP / (TP + FP) | Burden on reviewers |
| Specificity | TN / (TN + FP) | Often less actionable alone |

Report **confidence intervals** on sampled metrics when populations are small.

### Disposition precision

```
Precision_at_disposition = Confirmed_TP_after_review / All_closed_as_TP
```

Separate **rule-fired precision** from **analyst-confirmed**—analysts may rescue weak rules or bury FPs in benign closes.

## Labels and lag

Ground truth is delayed:

| Domain | Label lag | Implication |
|---|---|---|
| Fraud chargeback | 30–120 days | Recent precision understated |
| AML SAR | Months | Use proxy labels + thematic review |
| Security incident | Variable | Link cases to incident IDs |
| Benign close | Immediate | Risk of optimistic FP hide |

Run **matured cohort** reviews quarterly on older alert vintages.

## Calibration program

**Calibration** = periodic check that scores, tiers, and dispositions match reality.

### Cadence

| Activity | Frequency | Owner |
|---|---|---|
| Random benign sample | Weekly | Team lead |
| Random TP sample | Monthly | Risk |
| Matured cohort relabel | Quarterly | Risk + ops |
| Full rule review | Annual or post-incident | Engineering + risk |

### Calibration meeting agenda (60 min)

1. Metric dashboard vs targets
2. Top 5 FP drivers (root cause)
3. FN themes (from incidents + sample)
4. Open tuning packets status
5. Exceptions nearing expiry
6. Actions with owners

## Sampling methodology

| Goal | Method |
|---|---|
| Estimate precision | Stratified random sample of closed alerts |
| Find FN | Targeted sample: high-risk segment, near-miss cases |
| Audit defensibility | Include Tier 3–4 100% or high % |
| Analyst QA | Random 5–10% per analyst monthly |

Minimum sample sizes depend on volume; document **confidence** when n is small.

### Stratification dimensions

- Rule / scenario ID
- Tier at disposition
- Analyst / team
- Customer segment
- Geography

## Documentation artifacts

Maintain versioned artifacts:

| Artifact | Contents |
|---|---|
| Decision policy | Tiers, evidence bars, approvers |
| Tuning log | Change ID, hypothesis, metrics, approver |
| Disposition taxonomy | Codes: benign reason, TP type, escalate reason |
| Rationale template | Required fields (see evidence reference) |
| Exception register | Expiry, scope, approver |
| Training record | Annual refresh on disposition standards |

Store in systems of record—not only wiki.

## Audit and regulatory readiness

Auditors and regulators often ask:

- How do you know alerts are **appropriately** dispositioned?
- Show **threshold changes** and approvals
- Show **sample** of benign closes with rationale
- Prove **irreversible** actions had sufficient evidence

Prepare **audit pack** per scenario family:

1. Policy excerpt
2. Metric trend (precision, FN incidents)
3. Sample workpapers (redacted)
4. Tuning log excerpt

Use `auditor` for workpaper format; use this reference for **quality metrics** narrative.

## Dashboards

Minimum viable dashboard panels:

| Panel | Notes |
|---|---|
| Alerts by tier over time | Detect tier creep |
| Precision at disposition (matured) | Lag-adjusted |
| Benign close reason Pareto | Drives tuning |
| SLA breach | Capacity signal |
| FN count / incidents | Paired with FP |
| Open exceptions | Expiry warnings |

Avoid ranking analysts on **volume closed** only.

## Failure modes

| Symptom | Likely cause | Response |
|---|---|---|
| Precision ↑, complaints ↑ | Wrong benign taxonomy | Relabel sample |
| Precision ↑, losses ↑ | FN under-detection | Lower bar or add coverage |
| Benign close time ↓ | Rubric drift | QA sample |
| Auto-actions ↑ | Tier creep | Policy audit |
| Metrics flat, pain high | Wrong metric | Shift to disposition precision |

## Integration with build validation

Before launching new automated checks in product or CI, ask (`build-validator` complement):

- What **tier** can this signal trigger?
- What **evidence bar** is required?
- What **metric** proves it is not noisy?

Document answers in the launch checklist.
