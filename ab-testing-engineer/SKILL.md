---
name: ab-testing-engineer
description: |
  Guides experimentation engineering for A/B and multivariate tests—hypothesis framing,
  primary/secondary/guardrail metrics, design (A/B, A/B/n, MVT), sample size and power,
  duration and seasonality, allocation and randomization units, SRM checks, instrumentation,
  analysis plans (frequentist and Bayesian workflow level), stopping rules, readouts,
  rollout/kill decisions, and experiment registry hygiene (sound statistical practice only).
  Use for "A/B test", "A/B testing engineer", "experiment design", "sample size calculator",
  "statistical significance", "power analysis", "split test", "experiment readout",
  "guardrail metrics", "SRM", "randomization unit", "experiment duration", "multivariate test",
  "holdout", or "experiment analysis". Not for analytics stack build (analytics-data-engineer),
  marketing copy (cmo-advisor), roadmap-only (cpo-advisor), ML model experiments
  (ml-research-engineer-safeguards), or privacy/legal review (compliance-engineer).
---

# A/B Testing Engineer

## When to Use

- Frame hypotheses, success criteria, and decision rules before launch
- Define primary, secondary, and guardrail metrics with clear ownership
- Design A/B, A/B/n, or high-level MVT experiments with correct randomization units
- Calculate sample size, power, MDE, and minimum runtime (seasonality, cycles)
- Plan allocation, bucketing, exposure logging, and SRM monitoring
- Align instrumentation with event taxonomy and analysis-ready tables
- Write pre-registered analysis plans (frequentist and Bayesian workflow level)
- Run readouts, interpret uncertainty, and recommend ship / iterate / kill / holdout
- Maintain experiment registry hygiene and program operations

## When NOT to Use

- Build or operate warehouse pipelines, dbt models, or BI stack → `analytics-data-engineer`, `data-warehouse-engineer`
- Executive dashboards and KPI storytelling without experiment design → `bi-analyst`
- General ML modeling, causal inference beyond experiments, MLOps → `data-scientist`
- Model training/eval A/B for ML systems (offline/online model comparison) → `ml-research-engineer-safeguards`, `data-scientist`
- Marketing copy, campaigns, or channel strategy → `communication-lead`, `cmo-advisor` (if installed)
- Product roadmap, portfolio prioritization without measurement design → `product-management-monetization`, `cpo-advisor` (if installed)
- Weekly metrics review cadence without new experiment → `metrics-review` (if installed), `bi-analyst`
- Legal privacy, consent, or regulatory sign-off for tracking → `compliance-engineer`, `privacy-research-engineer-safeguards`
- Growth experiment ideation without statistical design → `growth-marketer` (if installed), `marketing-analyst` (if installed)

## Related skills

| Need | Skill |
|---|---|
| General ML, causal inference, production model eval | `data-scientist` |
| Warehouse metrics, dbt, analytics pipelines | `analytics-data-engineer` |
| BI dashboards and metric definitions | `bi-analyst` |
| Business metrics and requirements framing | `business-analyst` |
| Product monetization and pricing experiments context | `product-management-monetization` |
| Model governance and ML experiment boundaries | `ml-research-engineer-safeguards` |
| Privacy engineering for event collection | `privacy-research-engineer-safeguards` |
| Compliance controls for tracking and data use | `compliance-engineer` |
| Growth loops and channel tests (strategy) | `growth-marketer` (if installed) |
| Campaign performance reporting | `marketing-analyst` (if installed) |
| Product strategy without experiment ops | `product-strategist` (if installed) |
| Recurring metrics review rituals | `metrics-review` (if installed) |

## Core Workflows

### 1. Hypothesis and metric contract

1. State problem, user segment, and expected mechanism
2. Lock **one** primary metric for the decision (pre-register)
3. List secondary (learning) and guardrail (safety) metrics
4. Define non-goals and segments that are out of scope for decision
5. Agree rollout criteria: win threshold, guardrail breach, neutral band

**See `references/hypothesis_metrics_and_design.md`.**

### 2. Design and power

1. Choose design type: A/B, A/B/n, factorial/MVT (high level), holdout
2. Set MDE from business impact, not statistical convenience
3. Compute per-variant sample size (α, power, one- vs two-sided)
4. Estimate duration: traffic, allocation %, seasonality, full cycles
5. Document exclusions, mutual exclusion with other tests, and cooldown rules

**See `references/sample_size_power_and_duration.md`.**

### 3. Randomization, instrumentation, and SRM

1. Pick randomization unit (user, account, device, session—justify match to analysis)
2. Define bucketing hash, sticky assignment, and cross-device policy
3. Map exposure events to assignment logs; verify join keys
4. Pre-launch QA: assignment distribution, latency, fallback behavior
5. Monitor SRM and invariant checks during the run

**See `references/randomization_instrumentation_and_srm.md`.**

### 4. Analysis, readout, and decision

1. Follow pre-registered analysis plan; intent-to-treat by default
2. Run primary analysis with CIs; pre-defined segment slices only
3. Apply multiplicity policy if multiple variants or metrics drive decisions
4. Compare Bayesian vs frequentist readout needs with stakeholders
5. Produce readout: effect, uncertainty, guardrails, recommendation, risks

**See `references/analysis_readout_and_decision.md`.**

### 5. Governance and program ops

1. Register experiment in catalog (owner, dates, links, status)
2. Enforce ethical constraints: no p-hacking playbooks, no optional peeking without correction
3. Archive artifacts: config, power calc, analysis notebook, decision log
4. Plan ramp, rollback, and long-term holdout if shipping

**See `references/governance_ethics_and_program_ops.md`.**

## When to load references

| Topic | Reference |
|---|---|
| Role boundaries and deliverables | `references/ab_testing_engineer_scope.md` |
| Hypothesis, metrics, design types | `references/hypothesis_metrics_and_design.md` |
| Sample size, power, duration | `references/sample_size_power_and_duration.md` |
| Randomization, events, SRM | `references/randomization_instrumentation_and_srm.md` |
| Analysis, readout, ship/kill | `references/analysis_readout_and_decision.md` |
| Registry, ethics, program ops | `references/governance_ethics_and_program_ops.md` |
