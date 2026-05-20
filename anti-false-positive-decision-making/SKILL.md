---
name: Anti-False-Positive Decision Making
description: |
  Guides decision frameworks when false positives are costly—thresholds, evidence bars, and escalation
  so actions are not taken on weak signals. Covers FP/FN trade-offs, base rates, corroboration, tiered
  response (monitor vs act), security/compliance alert tuning, screening workflows, HITL gates,
  precision/recall/FDR, decision rationale docs, and alert fatigue. Use when the user mentions false
  positive, reduce false positives, alert tuning, too many false alarms, precision vs recall, when to
  escalate, evidence threshold, anti false positive, decision threshold, base rate, corroboration
  before action, alert fatigue, screening false positive, or don't block on weak signal—not for
  production ML classifiers (data-scientist, ml-ops-engineer), legal determinations
  (commercial-counsel), detection rules without decision policy (domain security/AML skills), or
  generic brainstorming (executive-mentor).
---

# Anti-False-Positive Decision Making

## When to Use

- Calibrate **when to act** vs **monitor** when false positives block users, delay revenue, or burn analyst capacity
- Design **evidence bars** and **multi-signal corroboration** before irreversible actions (block, freeze, terminate, auto-remediate)
- Tune **security, fraud, or compliance alerts** with explicit FP/FN trade-offs and base-rate context
- Define **tiered response** paths and **human-in-the-loop** gates for screening and monitoring workflows
- Choose **metrics** (precision, recall, FDR) and review cadence for alert quality—not model training alone
- Document **decision rationale** for auditors, regulators, or post-incident review when disposition matters
- Reduce **alert fatigue** and **over-blocking** without silently accepting unacceptable false negatives

## When NOT to Use

- Train, deploy, or optimize production **ML classifiers** (feature engineering, hyperparameters, MLOps) → `data-scientist`, `ml-ops-engineer`
- **Legal** conclusions, sanctions determinations, or contract interpretation → `commercial-counsel`
- Author detection **rules or queries only** with no decision policy, escalation, or disposition framework → `information-security-engineer`, `defensive-security-analyst`, `aml-compliance` (as primary)
- **Generic** strategy stress-tests without operational decision design → `executive-mentor`
- Full **AML program** design, KYC policy, or STR narrative drafting → `aml-compliance`, `str-report`
- **Internal audit** workpapers and control effectiveness sampling → `auditor`
- Pre-flight **architecture or build** validation without alert/disposition lens → `build-validator`

## Related skills

| Need | Skill |
|---|---|
| Security control implementation, SIEM/EDR integration | `information-security-engineer` |
| Technical compliance evidence and CCM pipelines | `compliance-engineer` |
| AML TM scenarios, alert triage, SAR paths | `aml-compliance` |
| Behavioral risk heuristics (volume, velocity, transit) | Use `behavioral-risk-screening-concepts` (blockint bundle) for UI/workflow concepts |
| AI system risk tiers, model governance, policy gates | `ai-risk-governance` |
| Incident severity, escalation, on-call design | `incident-management-engineer` |
| Audit sampling, deficiency write-ups, control testing | `auditor` |
| SOC triage and shift operations | `soc-analyst` |
| Detection content and hunt hypotheses | `defensive-security-analyst` |
| Plan/design go-no-go before execution | `build-validator` |
| Security risk registers and treatment decisions | `security-risk-analyst` |

## Core Workflows

### 1. Frame the decision and costs

1. Name the **action** (block, freeze, escalate, auto-close, notify, quarantine)
2. List **cost of false positive** (customer harm, ops load, revenue, reputation, legal exposure from over-action)
3. List **cost of false negative** (fraud loss, breach, regulatory miss, safety)
4. Estimate **base rate** or prevalence band for the population (see reference)
5. Set explicit **risk appetite** for this decision class (who approves exceptions)

**See `references/anti_fp_decision_scope.md` for scope, boundaries, and handoffs.**

### 2. Set evidence bar and corroboration

```
signal(s) → minimum evidence tier → optional corroboration → disposition → audit record
```

- Define **single-signal** vs **multi-signal** requirements before irreversible action
- Prefer **independent** evidence types (rule + graph + human review; not two copies of same feature)
- Document **what would falsify** the hypothesis before closing as benign

**See `references/evidence_bars_and_corroboration.md`.**

### 3. Map FP/FN trade-offs and thresholds

- Plot operating points: stricter threshold → fewer FPs, more FNs (usually)
- Use **base rate** to interpret raw alert rates; avoid judging rules on volume alone
- Segment by customer tier, geography, product, or asset criticality where policy differs

**See `references/fp_fn_tradeoffs_and_base_rates.md`.**

### 4. Design tiered response and HITL gates

| Tier | Typical disposition | Automation allowed |
|---|---|---|
| 0 — Observe | Log, aggregate metrics | Yes |
| 1 — Soft signal | Queue, enrich, no customer impact | Yes with caps |
| 2 — Review required | Analyst disposition before action | Human or timed SLA |
| 3 — Contain | Reversible hold (pending review) | Policy + dual control |
| 4 — Irreversible | Block, SAR, account closure | Executive / MLRO / legal path |

**See `references/tiered_response_and_hitl_gates.md`.**

### 5. Tune alerts in security and compliance contexts

- Govern threshold changes: hypothesis, backtest, approval, post-change review
- Separate **detection** quality from **workflow** quality (routing, SLAs, training)
- Track **precision at disposition** and **time-to-benign-close**, not alert count alone

**See `references/security_compliance_alert_tuning.md`.**

### 6. Measure, calibrate, and document

- Define metrics owners and review cadence (weekly ops, quarterly risk)
- Record **rationale template** on every material disposition
- Run **calibration reviews**: sample closed-as-benign and closed-as-true-positive

**See `references/metrics_calibration_and_documentation.md`.**

## When to load references

| Topic | Reference |
|---|---|
| Scope, boundaries, peer handoffs | `references/anti_fp_decision_scope.md` |
| FP/FN, base rates, prevalence | `references/fp_fn_tradeoffs_and_base_rates.md` |
| Evidence tiers and corroboration | `references/evidence_bars_and_corroboration.md` |
| Alert tuning (security, compliance, screening) | `references/security_compliance_alert_tuning.md` |
| Tiered response and HITL gates | `references/tiered_response_and_hitl_gates.md` |
| Metrics, calibration, audit trail | `references/metrics_calibration_and_documentation.md` |
