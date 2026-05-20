# Detection feedback and metrics

## Table of contents

1. [Tuning feedback format](#tuning-feedback-format)
2. [SOC metrics](#soc-metrics)
3. [Weekly detection review](#weekly-detection-review)
4. [Anti-patterns](#anti-patterns)

## Tuning feedback format

Open a tuning ticket for every repeatable false positive or noisy rule:

| Field | Content |
|---|---|
| Detection ID / name | SIEM rule or EDR policy ID |
| Alert volume | Count per 7d; peak times |
| FP pattern | Why benign (tool, job, admin task) |
| Sample case IDs | 2–3 examples with redacted entities |
| Proposed change | Threshold, enrichment, scope, time window |
| Risk if suppressed | ATT&CK technique affected |
| Requested test window | Dates for parallel run |

Detection engineering owns implementation; SOC owns **signal from the floor**.

## SOC metrics

Track at team level (daily or weekly dashboard):

| Metric | Definition | Target direction |
|---|---|---|
| Time to acknowledge | Alert created → owner assigned | Down |
| Time to triage | Alert created → FP close or TP classified | Down |
| True positive rate | TP / (TP + FP) per rule | Up for high-fidelity rules |
| False positive rate | FP / total closes per rule | Down |
| Reopen rate | Cases reopened within 7d | Down |
| Escalation rate | Cases escalated to T3/IR | Stable (not zero) |
| Playbook success | Auto-enrich steps completed | Up |
| Tuning backlog age | Open tuning tickets >14d | Down |
| Shift handoff compliance | Written handoff on schedule | Up |

Slice metrics by **source**, **category**, and **tier** to find systemic issues.

## Weekly detection review

Standing agenda (30–60 min):

1. Top 5 noisy rules by volume
2. New true positives worth promoting to higher fidelity
3. Open tuning tickets — owner and ETA
4. Missed activity (if any) from IR postmortems
5. Playbook gaps discovered on shift

SOC lead presents; detection engineering commits to change or documents risk acceptance.

## Anti-patterns

Avoid:

- **Global suppressions** without expiry on credential theft or C2 techniques
- **Closing without category** — breaks metrics and IR reporting
- **Silent queue drops** — every alert gets disposition
- **Analyst-only containment** outside runbook without ticket
- **Tuning via personal filters** — changes must be team-visible and reviewed

Improve detections through **documented feedback**, not individual queue hacks.
