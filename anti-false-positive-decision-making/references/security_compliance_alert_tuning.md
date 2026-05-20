# Security and compliance alert tuning

## Table of contents

1. [Tuning vs detection](#tuning-vs-detection)
2. [Governed change process](#governed-change-process)
3. [Security operations (SOC)](#security-operations-soc)
4. [Compliance monitoring](#compliance-monitoring)
5. [Fraud and AML TM](#fraud-and-aml-tm)
6. [Screening systems](#screening-systems)
7. [Enrichment and deduplication](#enrichment-and-deduplication)
8. [Metrics for tuning](#metrics-for-tuning)
9. [Post-change review](#post-change-review)

## Tuning vs detection

| Layer | Owns | This skill focuses on |
|---|---|---|
| **Detection** | Logic, data, coverage | When detection may **drive action** |
| **Tuning** | Thresholds, suppressions, routing | **Operating point** and workflow |
| **Workflow** | Queues, SLAs, training | **Disposition quality** |

Do not conflate “fewer alerts” with success if FN rate rises without review.

## Governed change process

Every material tuning change follows:

```
1. Hypothesis → 2. Analysis → 3. Approval → 4. Deploy → 5. Post-review
```

### 1. Hypothesis

Document:

- Problem statement (FP pain, FN incident, new product)
- Affected rules/scenarios and population
- Expected direction (precision ↑, recall ↓, etc.)

### 2. Analysis

| Analysis type | Use when |
|---|---|
| Historical replay | Stable data; rule logic unchanged |
| Shadow mode | New threshold runs parallel; no customer impact |
| Sample review | Last N alerts stratified by outcome |
| Cohort comparison | Before/after for similar customers |

Include **base rate** and **disposition breakdown** (see `fp_fn_tradeoffs_and_base_rates.md`).

### 3. Approval

| Change magnitude | Typical approver |
|---|---|
| Routing / enrichment only | Team lead |
| Threshold affecting queue volume >20% | Risk + ops |
| Auto-action enabled or disabled | Second line + engineering |
| Irreversible auto-action | Risk owner + legal/compliance |

### 4. Deploy

- Version ID and effective timestamp
- Feature flag or gradual rollout where possible
- Rollback plan documented

### 5. Post-review

30- and 90-day checkpoints: precision at disposition, FN themes, customer complaints, SLA breach.

## Security operations (SOC)

| Tuning lever | Anti-FP note |
|---|---|
| Severity mapping | Map low-confidence detections to **monitor** not page |
| Correlation windows | Widen to reduce duplicate pages; watch FN on short attacks |
| Suppression lists | Time-boxed; owner; reason code |
| Auto-enrichment | Reduce analyst guesswork; improves precision at review |
| Playbook branching | “Weak signal” branch must not auto-isolate |

Pair with `soc-analyst` for shift ops; `defensive-security-analyst` for rule content.

## Compliance monitoring

Continuous control monitoring (CCM) alerts differ from threat alerts:

| CCM alert | Tuning principle |
|---|---|
| Config drift | Confirm asset in scope; suppress known approved exceptions with ticket |
| Access anomaly | Tier: self-service fix vs security incident |
| Evidence gap | Route to control owner, not 24/7 SOC by default |

Use `compliance-engineer` for evidence automation design; this reference for **alert disposition policy**.

## Fraud and AML TM

Transaction monitoring tuning (operational):

| Input | Review |
|---|---|
| Alert volume trend | vs customer growth and new scenarios |
| SAR yield / referral rate | Not sole metric—quality over count |
| Benign close reasons | Top 5 FP drivers → rule or enrichment fix |
| Reopen rate | Indicates weak initial disposition |

Hand off program-level scenario libraries to `aml-compliance`; use governed process here.

## Screening systems

| Control | Anti-FP tuning |
|---|---|
| Fuzzy name match | Tune match scores; require secondary identifiers for auto-action |
| Batch vs real-time | Different bars; batch may allow analyst batch review |
| Periodic rescreen | Delta-only alerts where vendor supports |
| Internal watchlist | Separate governance from sanctions vendor |

## Enrichment and deduplication

Often the highest ROI for FP reduction **without** lowering detection:

| Technique | Effect |
|---|---|
| Dedup by entity + scenario + window | Cuts analyst duplicate work |
| Attach KYC / expected activity | Faster benign close |
| Link related alerts to parent case | Single disposition |
| Auto-prioritize by loss exposure | Protects capacity for true risk |

## Metrics for tuning

Track **before and after** deploy:

| Metric | Definition |
|---|---|
| Alerts per 1k customers | Volume (context only) |
| Precision at disposition | Confirmed TP / all closed as TP |
| Benign close rate | With quality sample |
| Time to first touch | SLA health |
| FN count (sampled) | Active FN review required |
| Customer impact tickets | FP proxy |

## Post-change review

Template:

```
Change ID:
Effective date:
Hypothesis result: [met | partial | failed]
Volume delta: ___%
Precision at disposition delta: ___%
FN incidents (if any):
Customer impact signals:
Decision: [keep | rollback | iterate]
```

## When **not** to tune

- During active incident (stabilize first)
- Without baseline metrics
- To meet arbitrary “alert reduction OKR”
- By disabling detection without risk acceptance

Route systemic detection gaps to engineering and detection owners; route **policy** gaps to risk owner.
