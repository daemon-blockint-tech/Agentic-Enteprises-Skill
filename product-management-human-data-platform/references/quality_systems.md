# Quality Systems

## Quality model

```
Raw labels → QA gates → Accepted dataset → Customer export
                ↑
         Gold / consensus / adjudication
```

## Mechanisms

| Mechanism | Use when |
|-----------|----------|
| **Gold tasks** | Known-answer items mixed into production |
| **Consensus** | Multiple annotators; majority or unanimous rule |
| **Adjudication** | Expert resolves disagreement |
| **Reviewer sampling** | % audit of accepted work |
| **Automated checks** | Schema, bounds, regex, model confidence |

## Metrics (define targets per project type)

| Metric | Definition |
|--------|------------|
| **Accuracy** | % match to gold (on gold items) |
| **IAA** | Cohen's kappa / Fleiss / Krippendorff as appropriate |
| **Rework rate** | % items sent back to contributor |
| **Throughput** | Labels per contributor hour |
| **SLA adherence** | % batches delivered on time |
| **Dispute rate** | Appeals per 1k labels |

Report **confidence intervals** on small samples.

## Gold set program

- Size: enough power for weekly monitoring (often 1–5% injection)
- Refresh: rotate gold to prevent memorization
- Stratify: cover rare classes and edge cases
- **Never** use customer production data as gold without rights

## Rejection taxonomy

Standardize reject reasons for product analytics:

```markdown
- Instruction misunderstanding
- Taxonomy error
- Incomplete annotation
- Tooling bug
- Policy violation (PII, unsafe)
- Borderline / needs adjudication
```

## Tiered workforce

| Tier | Access |
|------|--------|
| Trainee | Calibration only |
| Standard | Production with gold monitoring |
| Expert | Adjudication, rubric updates |
| Customer reviewer | Final accept on private queues |

Promotion rules must be **transparent** to contributors.

## Customer-facing quality SLAs

Document in contract appendix:

- Minimum accuracy on gold (if customer supplies gold)
- Consensus configuration
- Escalation when IAA drops below threshold
- Rework turnaround time

## Product features roadmap signals

- Spike in rework → instruction or UI issue
- IAA collapse on new class → taxonomy or training gap
- Gold accuracy drift → contributor gaming or spec ambiguity

## Pair with eval teams

Export formats should support `prompt-engineer-agent-prompts-evals` golden sets and regression harnesses without manual reformatting.
