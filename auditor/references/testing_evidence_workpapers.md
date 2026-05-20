# Testing, evidence, and workpapers

## Table of contents

1. [Test program design](#test-program-design)
2. [Sampling methodology](#sampling-methodology)
3. [Test procedures by ITGC domain](#test-procedures-by-itgc-domain)
4. [Evidence standards](#evidence-standards)
5. [Workpaper structure](#workpaper-structure)
6. [Analytics and automated controls](#analytics-and-automated-controls)
7. [Quality review checklist](#quality-review-checklist)

## Test program design

Link every procedure to:

- **Control ID** and narrative
- **Test objective** (what failure would mean)
- **Assertion** (if SOX-adjacent: completeness, accuracy, etc.)
- **Period** under review
- **Procedure steps** (numbered, reproducible)
- **Expected evidence**
- **Sample size** rationale
- **Result** (pass / exception / N/A)

### Procedure verbs

| Verb | When to use | Strength |
|---|---|---|
| **Inspect** | Documents, logs, configs, screenshots | Strong for documentary evidence |
| **Observe** | Physical or live process (one-time) | Limited period coverage |
| **Inquire** | Interviews | Weakest alone; corroborate |
| **Re-perform** | Recalculate, re-run report | Strong for automated checks |
| **Compare** | Match two independent sources | Strong for reconciliation controls |

Combine **inquiry + inspect** at minimum for key controls.

## Sampling methodology

### Define population first

Document:

- **Population description** (all production changes in Q1, all terminations in FY)
- **Source system** (ticket export, HR report, IAM log)
- **Cutoff** (inclusive dates, timezone)
- **Exclusions** (with rationale: emergency-only queue, test tenants)

### Approaches

| Method | Use when | Notes |
|---|---|---|
| **Random** | Large homogeneous population | Document seed and tool |
| **Systematic** | Every nth item after random start | State interval |
| **Haphazard** | Small population, low risk | Document anti-bias steps |
| **Judgmental** | High risk, fraud, key items | Select high-value, unusual, related-party |
| **Full population** | Automated control, small N | Export entire log; validate completeness |

### Sample size heuristics (internal audit — not statistical sign-off)

Adjust for risk and control frequency; document deviation from policy:

| Population size (annual) | Low risk indicative n | Higher risk indicative n |
|---|---|---|
| 1–25 | All or 25 | All |
| 26–100 | 25 | 40 |
| 101–500 | 30 | 60 |
| 500+ | 40–60 | 60–90 |

For **automated** controls with effective monitoring, test **one** instance plus **ITGC** over the tool; for **manual** quarterly controls, sample across quarters.

### Dual-purpose samples

Coordinate with **external audit** and **SOC** to reuse samples when criteria align—document **who tested what** to avoid gaps.

## Test procedures by ITGC domain

### Logical access

- New user: approval before grant, role appropriate, ticket linkage
- Termination: timely disablement (e.g., 24h), access removed from critical systems
- Privileged: MFA, logging, separate account, quarterly recertification
- Periodic review: evidence of owner review, remediation of orphans

### Change management

- Request, dev, test, approval, deploy segregation
- Emergency change: post-implementation review within N days
- Production access restricted; code review or CI gate evidence

### Computer operations

- Job success/failure monitoring and resolution
- Backup completion and **restore test** (annual minimum for critical)
- Capacity / incident management (high level)

## Evidence standards

### Acceptable evidence properties

- **Sufficient** — supports the conclusion
- **Relevant** — ties to period and control
- **Reliable** — from system of record; not editable-only spreadsheets without source
- **Timely** — obtained during fieldwork; bridge gaps documented

### Indexing convention

```text
WP-{Engagement}-{Control}-{Seq}
Example: WP-ITGC24-IAM01-003
```

Attach:

- Screenshot with **date/time** visible where possible
- Export **metadata** (who ran report, parameters)
- **Hash or version** for large exports when policy requires

### Red flags (challenge evidence)

- Screenshots without context or period
- Admin-only reports without independent extraction
- Policy-only documentation with no operation proof
- Samples missing from population export

## Workpaper structure

### Standard folder / section layout

```text
00 Admin — charter, scope, planning
10 Risk & understanding — narratives, walkthroughs
20 Testing — programs, samples, results
30 Findings — sheets, MAP
40 Reporting — drafts, AC deck
99 Review — lead notes, sign-offs
```

### Workpaper header (each file)

| Field | Value |
|---|---|
| Engagement | |
| Control ID | |
| Preparer | Date |
| Reviewer | Date |
| Objective | |
| Procedure ref | |
| Conclusion | Pass / Exception |

### Exception documentation (in testing section)

For each exception:

- Sample ID
- What was expected vs observed
- Quantify (count, $, delay days) when possible
- **Not** final severity here—that comes in findings reference

## Analytics and automated controls

When controls are **fully automated**:

1. Validate **configuration** (who can change rules)
2. Test **design** of rule logic
3. For operating effectiveness: export **entire exception population** for period or validate **monitoring** over population
4. Consider **re-performance** on sample of exceptions

Coordinate with `compliance-engineer` when continuous monitoring outputs are proposed as primary evidence—auditor still validates completeness and change control over the monitor.

## Quality review checklist

Before closing fieldwork:

- [ ] Every planned control has a conclusion or documented scope cut
- [ ] Samples trace to population workpaper
- [ ] Exceptions linked to finding sheets
- [ ] Evidence indexed and readable
- [ ] Reviewer notes cleared
- [ ] Management representations (if used) match scope
- [ ] Third-party gaps (bridge letter period) documented

## Work products

- Completed **test program** with tick-marks
- **Population** and **sample** listings
- **Evidence index** with storage location
- **Walkthrough** memo (if not in separate file)
- **Summary of exceptions** for findings phase
