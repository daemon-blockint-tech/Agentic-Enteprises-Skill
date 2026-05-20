# Analysis, Readout, and Decision

## Table of contents

1. [Pre-registered analysis plan](#pre-registered-analysis-plan)
2. [Frequentist workflow](#frequentist-workflow)
3. [Bayesian workflow (high level)](#bayesian-workflow-high-level)
4. [Segments and multiplicity](#segments-and-multiplicity)
5. [Stopping rules](#stopping-rules)
6. [Readout template](#readout-template)
7. [Ship, kill, iterate, holdout](#ship-kill-iterate-holdout)
8. [Anti-patterns](#anti-patterns)

## Pre-registered analysis plan

Publish **before** viewing results:

1. Primary metric and test (z-test, t-test, bootstrap, regression)
2. Population (ITT vs exposed) and filters
3. Covariates / CUPED (if any)—specified upfront
4. Segment list (max 3–5 pre-defined)
5. Multiplicity correction for secondary claims
6. Handling of outliers and winsorization
7. Missing data policy

Deviations require documented reason in readout.

## Frequentist workflow

Standard steps:

1. **Validate data** — assignment counts, SRM, exposure rate
2. **Estimate effect** — absolute and relative lift on primary
3. **Uncertainty** — 95% CI (or pre-specified level)
4. **p-value** — report with CI; do not decide on p alone
5. **Guardrails** — same procedure with veto thresholds
6. **Sensitivity** — ITT vs exposed; with/without outliers if pre-specified

### Test selection (quick reference)

| Metric type | Common approach |
|---|---|
| Proportion | Two-proportion z-test; Wilson CI |
| Mean (continuous) | Welch t-test; bootstrap for heavy tails |
| Ratio | Bootstrap or delta method |
| Count / Poisson | Poisson or negative binomial regression |

Always check **independence** assumption at chosen unit.

## Bayesian workflow (high level)

Use when stakeholders prefer **probability of lift** language:

1. Choose priors (weakly informative default; document if informative)
2. Compute posterior for treatment − control
3. Report `P(lift > 0)`, `P(lift > MDE)`, expected loss
4. Decision rule: e.g., ship if `P(lift > 0) > 0.95` and guardrail posteriors acceptable

**Caution:** Peeking changes posterior interpretability unless using **sequential Bayesian** methods pre-specified.

Partner with `data-scientist` for prior sensitivity analysis on high-stakes tests.

## Segments and multiplicity

| Policy | When |
|---|---|
| Pre-defined segments only | Default |
| FDR/Bonferroni across segments | Many segments requested |
| Exploratory segments labeled | Post-hoc; not for ship decision |

Never promote a segment that "saved" a flat global result without correction.

## Stopping rules

| Approach | Guidance |
|---|---|
| **Fixed horizon** | Run planned N; analyze once at end—simplest |
| **Sequential (frequentist)** | Use spending functions or always-valid inference; pre-specify |
| **Bayesian monitoring** | Pre-specify stop if `P(win)` high and loss low |
| **Ad hoc peeking** | **Avoid**; inflates false positives |

If stopping early for harm (guardrail), document as **safety stop** separate from efficacy peeking.

## Readout template

```markdown
# Experiment readout: [Name] ([ID])

## Summary
- **Decision:** Ship / No ship / Iterate / Extend
- **Primary metric:** [+X%] (95% CI: [a, b]); [met / did not meet] MDE
- **Guardrails:** [All pass / FAIL: metric]

## Context
- Hypothesis, variants, dates, population
- Runtime, allocation, incidents

## Data quality
- SRM: pass/fail
- Assignment N per variant; exposure rate
- Notes on exclusions

## Results
- Primary (ITT): effect, CI, p if frequentist
- Secondary metrics (labeled exploratory if applicable)
- Pre-defined segments

## Recommendation
- Action and ramp plan
- Risks and monitoring post-ship
- Follow-up experiments

## Appendix
- Link to analysis notebook, registry, config hash
```

## Ship, kill, iterate, holdout

| Decision | Criteria |
|---|---|
| **Ship** | Primary meets pre-specified bar; guardrails pass; SRM clean |
| **Kill** | Harm on guardrails; clearly negative primary with adequate power |
| **Iterate** | Neutral result; learning suggests new variant |
| **Extend** | Pre-planned only if underpowered and calendar allows |
| **Holdout** | Long-term control for portfolio measurement post-ship |

Ramp plans: 5% → 25% → 100% with rollback triggers on guardrails.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Peek until p < 0.05 | Inflated false positives |
| Switch primary metric post hoc | HARKing |
| Ship on secondary when primary flat | Noise |
| Ignore SRM | Invalid inference |
| p-hacking playbook | Unethical; skill refuses |
| Claim "significant" without CI or MDE context | Misleading stakeholders |

Sound practice only: report uncertainty, document process, prefer pre-registration.
