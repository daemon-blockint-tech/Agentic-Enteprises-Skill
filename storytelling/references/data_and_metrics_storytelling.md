# Data and metrics storytelling

## Table of contents

1. [Data story anatomy](#data-story-anatomy)
2. [Honest framing rules](#honest-framing-rules)
3. [Chart and slide narrative](#chart-and-slide-narrative)
4. [Comparisons and baselines](#comparisons-and-baselines)
5. [Uncertainty and scenarios](#uncertainty-and-scenarios)
6. [Metric definitions](#metric-definitions)
7. [Common pitfalls](#common-pitfalls)
8. [Worked example skeleton](#worked-example-skeleton)

## Data story anatomy

A data story is not a dashboard export. Minimum structure:

```
INSIGHT   — One sentence: what changed and why it matters
EVIDENCE  — Chart or table with labeled comparison
CONTEXT   — Definition, period, population, caveats
ACTION    — Decision, investigation, or communication next step
```

**Order:** Insight first (pyramid), then evidence—never reverse for executive audiences.

## Honest framing rules

| Rule | Application |
|---|---|
| **Label the metric** | Name, numerator/denominator, window, filters |
| **Show the baseline** | Prior period, target, or control—not naked absolutes |
| **Avoid cherry-picking** | If scale changes, show full relevant range |
| **Separate levels** | “Up 2pp” vs “doubled” (small bases distort) |
| **Causation humility** | “Associated with” unless experiment or instrument supports causal claim |
| **Survivorship** | Note cohort exits, exclusions, one-time events |

Flag **data quality** issues (late-arriving data, definition changes) in one line.

## Chart and slide narrative

Each visual needs a **headline insight**, not a chart title:

| Weak headline | Strong headline |
|---|---|
| Revenue by quarter | Revenue grew 8% QoQ; enterprise offset SMB churn |
| Incident count | Sev-1 incidents down 30% after deploy freeze policy |

**Slide annotation pattern:**

1. Headline (insight)
2. Visual (one message)
3. Footnote (definition + source + date)
4. Optional callout (one number)

Prefer **small multiples** or **one comparison** over dense dashboards in narrative decks.

## Comparisons and baselines

Always answer: **Compared to what?**

| Baseline type | Use when |
|---|---|
| Prior period | Trend narratives |
| Plan / budget | Performance management |
| Cohort | Product or retention stories |
| Control group | Experiment readouts |
| Peer / benchmark | Market context (cite source) |

When metrics **redefine**, show bridge or restate prior periods—do not blend incompatible series silently.

## Uncertainty and scenarios

| Situation | Narrative technique |
|---|---|
| Forecast | Range + assumptions; name drivers |
| Small samples | Confidence intervals or “directional only” |
| Model output | Model purpose, limitations, validation |
| Actuarial / risk | Central estimate + sensitivity (see incident/actuarial reference) |

**Scenario framing:**

- Base: most likely assumptions
- Downside: material risk case
- Upside: only if decision-relevant (avoid false optimism)

## Metric definitions

Include a **metric contract** in appendix or footnote:

| Field | Content |
|---|---|
| Name | Canonical ID |
| Definition | Formula, inclusion/exclusion |
| Unit | User, order, policy, etc. |
| Window | Calendar vs rolling |
| Source | System of record |
| Known biases | Seasonality, promos, migration |

Align definitions with analytics or actuarial owners before board or customer narratives.

## Common pitfalls

| Pitfall | Fix |
|---|---|
| Dual-axis abuse | Separate charts or indexed series |
| Truncated Y-axis misleading | Show context or label distortion |
| Percent on percent | State absolute and relative |
| Vanity metrics | Tie to outcome metric |
| One-week spike as trend | Show longer window |
| Mixing GAAP and operational | Separate stories or bridge |

## Worked example skeleton

**Prompt:** “Tell the data story for Q3 retention.”

```
INSIGHT: Net revenue retention fell from 112% to 104% driven by mid-market downgrades, not new-logo churn.

EVIDENCE: [Chart: NRR by segment, Q1–Q3] Mid-market −9pp; enterprise stable.

CONTEXT: NRR = (starting ARR + expansion − contraction − churn) / starting ARR; excludes one-time services.

CAVEAT: July price increase may have accelerated Q3 downgrades; cohort still maturing.

ACTION: Approve CS playbook pilot for mid-market; revisit packaging in Q4 planning.
```

Pair with `business-consultant` for driver analysis depth; storyteller owns **sequence and headline honesty**.
