# Hypothesis, Metrics, and Experiment Design

## Table of contents

1. [Hypothesis framing](#hypothesis-framing)
2. [Metric hierarchy](#metric-hierarchy)
3. [Metric contract template](#metric-contract-template)
4. [Design types](#design-types)
5. [Population and eligibility](#population-and-eligibility)
6. [Decision rules](#decision-rules)
7. [Common pitfalls](#common-pitfalls)

## Hypothesis framing

Use a structure stakeholders can challenge before build:

```
Because [observation/data],
we believe [change]
will cause [measurable outcome]
for [population]
because [mechanism].
We will know this is true when [primary metric + direction + threshold].
```

**Good hypotheses** are falsifiable, name a mechanism, and tie to one decision metric.

**Weak hypotheses** ("improve UX") without a metric or population—refine before sizing.

## Metric hierarchy

| Type | Purpose | Decision use |
|---|---|---|
| **Primary** | Answer the experiment question | **Only** metric that can trigger ship/kill alone |
| **Secondary** | Explain mechanism or secondary value | Learning; not for overriding primary without pre-registration |
| **Guardrail** | Detect harm (latency, revenue, churn, support) | Veto or pause if breached |
| **Monitoring / invariant** | Sanity (SRM, platform mix) | Data quality; not product success |

### Guardrail examples

- Revenue per user, refund rate, crash rate, p95 latency
- Unsubscribe rate, support tickets per active user
- Fraud or abuse flags (if applicable)

Define **breach thresholds** up front (e.g., "stop if guardrail CI excludes 0 and effect < -1%").

## Metric contract template

For each metric document:

| Field | Content |
|---|---|
| Name | Canonical metric ID |
| Definition | Numerator/denominator, filters, time window |
| Unit of analysis | User, session, order—must match randomization where possible |
| Direction | Higher or lower is better |
| Source | Event(s) or table(s) |
| Latency | When metric is available post-exposure |
| Known biases | Novelty, seasonality, one-time promotions |

Align names with **event taxonomy** (`analytics-data-engineer`) before launch.

## Design types

### A/B (two variants)

- **Control** vs **treatment**; default when one clear change exists.
- Simplest power and interpretation.

### A/B/n (multiple treatments)

- One control + multiple treatments (e.g., copy A, B, C).
- Increases multiplicity—pre-define whether **any** variant wins vs **best** variant.
- Allocate traffic evenly unless powered for unequal splits.

### Multivariate (MVT) / factorial (high level)

- Test multiple factors simultaneously (e.g., headline × CTA).
- Requires more traffic; interactions are hard to power.
- Prefer **fractional factorial** or sequential tests when traffic is limited.
- Document which interactions are **in scope** for decisions.

### Holdout

- Long-running control cell excluded from launches.
- Measures cumulative lift; not a substitute for pre-launch A/B on a specific change.

### Switchback / geo (awareness)

- When user-level randomization is infeasible, time or geo designs may apply.
- Different assumptions (autocorrelation, spillover)—flag as advanced; partner with `data-scientist` for causal design.

## Population and eligibility

Define:

- **Targeting**: new vs returning, platform, locale, plan tier
- **Trigger**: exposure on page view vs action vs assignment at login
- **Exclusions**: bots, employees, accounts in other experiments (mutual exclusion)
- **Cooldown**: users recently in conflicting tests

Document **analysis population**: all assigned (ITT) vs exposed only (justify if used).

## Decision rules

Pre-register:

| Outcome | Action |
|---|---|
| Primary beats control beyond MDE with guardrails pass | Ship or ramp |
| Primary neutral within MDE | Do not ship; iterate or deprioritize |
| Primary wins but guardrail fails | Do not ship; investigate |
| Inconclusive at planned N | Extend (pre-defined max) or stop |

Avoid "win if p < 0.05" without effect size and guardrail context.

## Common pitfalls

| Pitfall | Mitigation |
|---|---|
| Multiple "primary" metrics | One decision metric; others secondary |
| Post-hoc segments | Pre-list segments; Bonferroni/FDR if many |
| Metric not tied to UX change | Trace mechanism; change metric or design |
| Ratio metrics without variance plan | Use appropriate test (delta method, bootstrap) |
| Novelty conflated with sustained lift | Run longer or holdout for durable metrics |
