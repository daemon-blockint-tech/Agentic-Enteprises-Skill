# Leadership, culture, and metrics

## Table of contents

1. [Leadership behaviors](#leadership-behaviors)
2. [Stop-the-line authority](#stop-the-line-authority)
3. [Metrics that matter](#metrics-that-matter)
4. [Dashboards and reviews](#dashboards-and-reviews)
5. [Anti-metrics and gaming](#anti-metrics-and-gaming)
6. [Communication templates](#communication-templates)

## Leadership behaviors

| Behavior | Example |
|---|---|
| **Ask about near-miss** | Standing question in ops review: “What almost failed?” |
| **Reward escalation** | Recognize stop-the-line that prevented harm |
| **Fund prevention** | Budget verification, test envs, review capacity |
| **Model curiosity** | Leaders admit unknowns; invite dissent |
| **Fix systems** | Repeat incident → engineering change, not slogans |
| **Separate blame** | Learning review distinct from HR process |

| Anti-pattern | Why it fails |
|---|---|
| “Zero incidents” without near-miss data | Hides weak signals |
| Velocity at all costs | Normalizes gate bypass |
| Shooting messenger | Stops reporting |
| Review theater | Checkboxes without independent verification |

## Stop-the-line authority

Define in policy:

| Element | Guidance |
|---|---|
| **Who** | Any trained role on tier-0/1; named backup |
| **Triggers** | Ambiguous safety, failed verification, unexplained metric shift, repeat near-miss |
| **Actions** | Halt deploy/change; freeze config; convene rapid review |
| **Duration** | Until exit criteria met or explicit risk acceptance |
| **Communication** | Notify stakeholders; no silent halt |
| **Restart** | Document evidence and approver |

**Success metric:** stop-the-line events that **prevented** customer or safety impact—celebrate, do not penalize.

## Metrics that matter

| Metric | Definition | Why |
|---|---|---|
| **Defect escape rate** | Defects found in prod / total defects (by tier) | Measures gate effectiveness |
| **Critical escape count** | Tier-0/1 defects in prod | Lagging severity with prevention lens |
| **Near-miss rate** | Reported near-misses per period (normalized) | Leading indicator if culture healthy |
| **Repeat incident rate** | Incidents with same root category within 90d | System fix effectiveness |
| **Gate bypass rate** | Emergency changes / total prod changes | Culture stress signal |
| **Verification coverage** | % tier-0 changes with independent check | Process adherence |
| **Time-to-detect** | For escapes, how long until noticed | Observability quality (pair SRE) |
| **Pre-mortem yield** | Mitigations implemented / identified | Risk work ROI |

**Not sufficient alone:** raw incident count (luck), deployment frequency without escapes, individual “error counts” for blame.

## Dashboards and reviews

| Cadence | Audience | Focus |
|---|---|---|
| **Weekly** | Engineering + ops leads | Escapes, near-miss, open mitigations |
| **Monthly** | Directors | Trends, bypass audit, repeat incidents |
| **Quarterly** | Exec + risk | Tier coverage, norms audit, investment asks |

Pair with SRE reliability review (`site-reliability-engineer`)—prevention metrics explain **why** SLOs broke, not only **that** they broke.

## Anti-metrics and gaming

| Gaming | Countermeasure |
|---|---|
| Under-report near-miss | Anonymous channel; leader modeling |
| Reclassify severity | Independent incident review |
| Bypass without ticket | Automated change detection |
| Close risks without mitigation | Expiry and audit of accepted risks |

## Communication templates

**Near-miss report (short):**

```
What almost happened:
What prevented impact:
What could fail next time:
Proposed system fix / owner / date:
```

**Stop-the-line notice:**

```
Halted: [change/deploy]
Reason: [signal]
Owner: [name]
Next step: [review time / criteria to resume]
```

**Executive brief (monthly):**

```
Defect escapes (tier-0/1): [n] trend
Near-miss reports: [n] trend
Repeat incidents: [n]
Gate bypasses: [n] with top reasons
Stop-the-line events: [n] outcomes
Top systemic actions: [list]
```

Keep narratives **learning-oriented**—escalate individual conduct to HR outside this skill.
