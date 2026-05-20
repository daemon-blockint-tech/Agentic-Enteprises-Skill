# Randomization, Instrumentation, and SRM

## Table of contents

1. [Randomization unit](#randomization-unit)
2. [Bucketing and assignment](#bucketing-and-assignment)
3. [Exposure vs assignment](#exposure-vs-assignment)
4. [Instrumentation and event taxonomy](#instrumentation-and-event-taxonomy)
5. [Pre-launch QA](#pre-launch-qa)
6. [Sample ratio mismatch (SRM)](#sample-ratio-mismatch-srm)
7. [Invariant metrics](#invariant-metrics)
8. [Operational playbooks](#operational-playbooks)

## Randomization unit

The **randomization unit** is the entity hashed into variants. It must match the **unit of analysis** for the primary metric when possible.

| Unit | Use when | Risks |
|---|---|---|
| **User / account** | Most product metrics (conversion, retention) | Cross-device identity gaps |
| **Device / cookie** | Anonymous web before login | Split users across devices |
| **Session** | Session-scoped UX only | Same user multiple sessions → dependence |
| **Organization / team** | B2B seat or admin-led rollout | Spillover within org |
| **Geo / cluster** | Network effects, market-level changes | Fewer units; cluster SE needed |

**Rule:** If treatment is applied per user but analysis is per session without adjustment, expect bias.

Document **sticky assignment** duration (forever vs 30 days vs session).

## Bucketing and assignment

Standard pattern:

```
variant = hash(experiment_id + stable_id + salt) % bucket_map
```

Requirements:

- **Stable** across sessions for sticky tests
- **Independent** salt per experiment to reduce correlation across tests
- **Deterministic** given ID (reproducible QA)
- **Logged** at assignment time with timestamp and experiment version

Feature-flag systems should log:

- `experiment_id`, `variant_id`, `assignment_timestamp`
- `assignment_reason` (eligible, excluded, override)
- `experiment_version` / config hash

## Exposure vs assignment

| Concept | Definition |
|---|---|
| **Assignment** | User placed in variant bucket |
| **Exposure** | User actually saw treatment (UI rendered, email sent) |

**Intent-to-treat (ITT):** analyze all assigned users—recommended default.

**Per-protocol / exposed-only:** analyze exposed users only when exposure is well measured; risks bias if exposure differs by variant. Pre-register and report both when stakeholders require.

Log events:

- `experiment_assigned`
- `experiment_exposed` (with surface, locale, platform)
- `experiment_exposure_failed` (optional, for debugging)

## Instrumentation and event taxonomy

Minimum schema alignment with analytics engineering:

| Layer | Content |
|---|---|
| Client / server | Emit assignment + exposure with same `user_id` / `anonymous_id` |
| Pipeline | Dedupe, sessionize, map to canonical user |
| Mart | `fact_experiment_assignment`, `fact_experiment_exposure` |
| Analysis | Join outcomes on assignment_id or user_id + experiment_id |

**Property standards:**

- snake_case names; versioned event specs
- No PII in experiment properties unless approved (`compliance-engineer`)
- Include `app_version`, `platform`, `locale` for debugging splits

Partner with `analytics-data-engineer` for idempotent daily assignment tables.

## Pre-launch QA

Checklist before enabling traffic:

- [ ] Hash distribution uniform in staging (chi-square on synthetic IDs)
- [ ] Assignment logged on all code paths (including errors, mobile, web)
- [ ] Exposure fires only when treatment visible
- [ ] Mutual exclusion rules enforced in code
- [ ] Holdout and internal users excluded
- [ ] Backward compatibility when flag off
- [ ] Join query: assignment → exposure → primary metric returns sensible counts

Run **shadow mode** (assign but do not change UX) when platform is new.

## Sample ratio mismatch (SRM)

**SRM** occurs when observed assignment counts deviate significantly from expected allocation (e.g., 50/50 becomes 48/52 at scale).

| Cause | Investigation |
|---|---|
| Bad hash / bucket overflow | Review hash function and modulo |
| Conditional assignment after filter | Eligibility applied post-randomization |
| Bot or employee traffic | Filter populations |
| Crash path only in one variant | Engineering bug |
| Ramp or re-bucketing mid-flight | Versioning error |
| Data pipeline drop | Missing events in one arm |

**Response:**

1. **Pause** experiment if SRM is severe and unexplained
2. Query assignment logs at source vs warehouse
3. Fix bug; **restart** with new experiment_id if assignment corrupted
4. Do **not** treat results as valid until SRM resolved

Use chi-square test on assignment counts; platforms (Optimizely, internal) often automate SRM alerts—tune false positive rate.

## Invariant metrics

Metrics that should **not** differ by variant if randomization worked:

- Device type mix, OS, country (if not targeted)
- New vs returning mix (unless pre-period imbalance expected)
- Baseline activity pre-assignment (AA test)

Run **A/A** or **pre-period balance** on key covariates when traffic allows.

## Operational playbooks

| Scenario | Action |
|---|---|
| SRM alert fires | Page owner; freeze analysis; debug assignment |
| Exposure << assignment | Investigate render failures; do not switch to exposed-only without plan |
| Experiment paused | Document pause reason; exclude paused days or restart |
| Re-bucket users | Avoid mid-flight; if unavoidable, segment by version |
