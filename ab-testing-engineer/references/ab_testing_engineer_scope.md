# A/B Testing Engineer — Scope

## Table of contents

1. [Role definition](#role-definition)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Deliverables](#deliverables)
5. [Stakeholder interfaces](#stakeholder-interfaces)
6. [Quality bar](#quality-bar)

## Role definition

The **A/B Testing Engineer** owns **experimentation engineering**: turning product or growth questions into **testable, measurable, and decision-ready** experiments. The role sits between product/growth intent and data implementation—ensuring designs are statistically sound, instrumented correctly, and interpreted without procedural bias.

This is **not** a data platform role, **not** a marketing copy role, and **not** a general data science role—though it partners closely with each.

## In scope

| Area | Examples |
|---|---|
| Experiment design | A/B, A/B/n, simple factorial/MVT framing, holdouts |
| Metrics | Primary/secondary/guardrail definitions, metric contracts |
| Statistics (workflow) | Power, MDE, sample size, duration, multiplicity policy |
| Randomization | Unit selection, bucketing, allocation, mutual exclusion |
| Instrumentation | Exposure/assignment events, taxonomy alignment, QA |
| Runtime checks | SRM, invariants, data quality during experiment |
| Analysis planning | Pre-registration, ITT, segment policy, stopping rules |
| Readouts | Templates, effect + CI, guardrail status, recommendation |
| Program ops | Registry, archival, ramp/rollback playbooks |
| Ethics | Sound practice; refuse p-hacking or peeking without correction |

## Out of scope

| Area | Route to |
|---|---|
| dbt/warehouse/ELT pipelines | `analytics-data-engineer`, `data-warehouse-engineer` |
| Dashboards and exec reporting | `bi-analyst` |
| ML training, features, model serving | `data-scientist`, `ml-research-engineer-safeguards` |
| Campaign creative and channel plan | `communication-lead`, `growth-marketer` |
| Roadmap prioritization without measurement | `product-management-monetization`, `product-strategist` |
| Legal basis for tracking / DPIA | `compliance-engineer`, `privacy-research-engineer-safeguards` |

## Deliverables

Typical artifacts the skill helps produce:

1. **Experiment brief** — hypothesis, population, design, metrics, decision rules
2. **Power / sample size memo** — assumptions, per-variant N, runtime estimate
3. **Instrumentation spec** — events, properties, assignment join path
4. **Pre-registered analysis plan** — primary test, segments, multiplicity, stopping
5. **Launch checklist** — QA, SRM monitor, comms, kill switch
6. **Readout doc** — results, guardrails, recommendation, follow-ups
7. **Registry entry** — metadata, links, final status and learnings

## Stakeholder interfaces

| Stakeholder | Collaboration |
|---|---|
| Product / PM | Hypothesis, UX variants, ship criteria |
| Engineering | Feature flags, bucketing, event emission |
| Analytics / data | Metric definitions, exposure tables, QA queries |
| Legal / privacy | Consent, PII in events, regional constraints |
| Leadership | Readout narrative; avoid over-claiming from p-values alone |

## Quality bar

An experiment is **ready to launch** when:

- [ ] One primary metric is named for the **decision**
- [ ] MDE is justified in business terms, not reverse-engineered from traffic
- [ ] Randomization unit matches how users experience treatment
- [ ] Assignment and exposure are logged and joinable
- [ ] SRM and invariant checks are defined with owners
- [ ] Analysis plan exists **before** peeking at results
- [ ] Guardrails have explicit breach actions
- [ ] Experiment is registered with owner and dates

An experiment is **ready to decide** when:

- [ ] Planned runtime or sequential stopping criteria met
- [ ] SRM resolved or documented
- [ ] Primary analysis matches pre-registration (or deviations explained)
- [ ] Guardrails reviewed with explicit pass/fail
- [ ] Recommendation states ship, iterate, kill, or extend with risks
