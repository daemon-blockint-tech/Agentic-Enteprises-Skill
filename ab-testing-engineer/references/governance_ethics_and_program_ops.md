# Governance, Ethics, and Program Operations

## Table of contents

1. [Experiment registry](#experiment-registry)
2. [Lifecycle states](#lifecycle-states)
3. [Ethical and statistical standards](#ethical-and-statistical-standards)
4. [Privacy and compliance hooks](#privacy-and-compliance-hooks)
5. [Mutual exclusion and traffic budgeting](#mutual-exclusion-and-traffic-budgeting)
6. [Archival and learning](#archival-and-learning)
7. [Program metrics](#program-metrics)
8. [RACI (lightweight)](#raci-lightweight)

## Experiment registry

Maintain a single catalog (spreadsheet, Notion, internal tool) with:

| Field | Example |
|---|---|
| `experiment_id` | `exp_2026_checkout_cta_v2` |
| Name / link | Brief + design doc |
| Owner | PM + eng + analyst |
| Status | Draft / Running / Analyzed / Shipped / Killed |
| Dates | Start, planned end, actual end |
| Population | Eligible users, platforms |
| Design | A/B, A/B/n, allocation |
| Primary metric | `checkout_conversion_7d` |
| MDE / N | From power memo |
| Hypothesis | One paragraph |
| Results link | Notebook, dashboard |
| Decision | Ship / no ship + date |

**Hygiene rules:**

- No unregistered production experiments
- One registry row per `experiment_id`; new IDs for restarts after SRM bugs

## Lifecycle states

```
Draft → Review → Ready → Running → Paused → Analyzed → Decision → Archived
```

| State | Gate |
|---|---|
| Review | Power memo + instrumentation spec + analysis plan |
| Ready | QA sign-off, SRM monitor configured |
| Running | Daily SRM/guardrail monitor |
| Analyzed | Readout published |
| Decision | Stakeholder sign-off logged |
| Archived | Config removed or 100% rolled out; docs linked |

## Ethical and statistical standards

This skill teaches **sound practice only**. Do not provide guidance to:

- Manipulate metrics, drop outliers selectively post hoc, or re-run until significant
- Hide negative results from registry
- Cherry-pick segments without multiplicity control
- Recommend optional peeking without sequential methods

**Do provide:**

- Pre-registration encouragement
- Transparent reporting of null results
- Guardrails for user harm and business risk
- Clear "we do not know" when underpowered

## Privacy and compliance hooks

Coordinate with `compliance-engineer` and `privacy-research-engineer-safeguards` when:

- New tracking events or PII properties added
- Regional restrictions (GDPR, COPPA, sector rules)
- Email/push experiments with consent requirements
- Sensitive populations (minors, health, financial)

Document **lawful basis** and data retention for experiment logs—not legal advice; escalate to counsel.

## Mutual exclusion and traffic budgeting

| Mechanism | Purpose |
|---|---|
| Layer / namespace | Parallel tests on orthogonal layers |
| Mutual exclusion groups | Tests that cannot overlap on same users |
| Global holdout | Long-term measurement cell |

Define **max concurrent experiments** per surface to protect power and UX coherence.

## Archival and learning

After decision, archive:

- Final config / flag state
- Power calculation inputs and outputs
- Analysis notebook (frozen hash)
- Readout PDF or wiki page
- Post-ship monitoring plan (2–4 weeks)

**Learning library:** tag outcomes (`win`, `loss`, `inconclusive`) for meta-analysis quarterly.

## Program metrics

Track program health (not individual test p-values):

| Metric | Why |
|---|---|
| % experiments with pre-registration | Process quality |
| Time in Running without decision | Stale experiments |
| SRM rate | Platform health |
| % shipped with guardrail pass | Safety |
| Median power (ex post) | Planning calibration |
| Duplicate / conflicting tests | Coordination |

## RACI (lightweight)

| Activity | PM | Eng | A/B engineer / analyst | Legal |
|---|---|---|---|---|
| Hypothesis | A | C | C | I |
| Metric contract | A | C | R | I |
| Randomization / flags | C | R | C | I |
| Power / duration | C | I | R | I |
| Instrumentation | C | R | C | C |
| Analysis / readout | C | I | R | I |
| Ship decision | A | C | C | I |

R = responsible, A = accountable, C = consulted, I = informed.
