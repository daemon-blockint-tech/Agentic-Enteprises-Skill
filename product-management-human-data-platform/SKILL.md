---
name: product-management-human-data-platform
description: |
  Guides product management for human data platforms—annotation and labeling products, workforce
  workflows, task design, quality systems (gold sets, adjudication, inter-annotator agreement),
  customer ML-team project delivery, contributor experience, and privacy-safe handling of human-generated
  training data. Use when prioritizing roadmap for labeling/RLHF/eval data platforms, writing PRDs
  for annotation or QA features, defining success metrics for throughput and quality, scoping
  enterprise customer workflows, or balancing cost-quality-speed tradeoffs—not for hands-on model
  training (data-scientist), warehouse/analytics pipelines (data-warehouse-engineer), generic BRD
  workshops without product lens (business-analyst), AI solution architecture for copilots
  (applied-ai-architect-commercial-enterprise), or control implementation for audits
  (compliance-engineer). UX flows: product-designer. Eval harnesses: prompt-engineer-agent-prompts-evals.
  Pricing/packaging for platform: product-management-monetization.
---

# Product Management — Human Data Platform

## When to Use

- Define **vision, roadmap, and prioritization** for labeling, RLHF, or human-eval products
- Write **PRDs** for annotation UI, project setup, QA, workforce, or export/API features
- Design **annotation tasks** (taxonomy, instructions, rubrics, edge cases)
- Specify **quality programs**: gold tasks, consensus, adjudication, rejection reasons
- Scope **customer** workflows (ML teams): projects, batches, SLAs, delivery formats
- Improve **contributor/annotator** productivity, fairness, and trust/safety product surfaces
- Set **metrics**: throughput, quality, cost per label, time-to-delivery, contributor retention
- Partner on **privacy and ethics** requirements for human-submitted data (PII, consent, locale)

## When NOT to Use

- Facilitate generic process maps and BRDs without product ownership → `business-analyst`
- Wireframes and visual design only → `product-designer`
- RAG/copilot enterprise architecture → `applied-ai-architect-commercial-enterprise`
- Build eval harnesses and judges in code → `prompt-engineer-agent-prompts-evals`
- SOC/ISO evidence automation → `compliance-engineer`
- Data warehouse modeling → `data-warehouse-engineer`
- Cross-team delivery RAID without product discovery → `technical-program-manager`

## Related skills

| Need | Skill |
|---|---|
| BRD/user story format | `business-analyst` |
| Annotator and customer UX | `product-designer` |
| How labels feed model programs | `applied-ai-architect-commercial-enterprise` |
| Golden sets and regression evals | `prompt-engineer-agent-prompts-evals` |
| Privacy controls and audit evidence | `compliance-engineer` |
| Taxonomy/ontology for labels | `ontology-engineer` |
| Analytics for product teams | `analytics-data-engineering-manager-product` |

## Core Workflows

### 1. Vision, roadmap, and prioritization

Outcomes, segments, themes, RICE/ICE.

**See `references/roadmap_prioritization.md`.**

### 2. Annotation task and taxonomy design

Instructions, rubrics, schema, edge cases.

**See `references/annotation_task_design.md`.**

### 3. Quality systems

Gold sets, IAA, adjudication, rejection taxonomy.

**See `references/quality_systems.md`.**

### 4. Customer (ML team) delivery

Projects, pipelines, exports, SLAs.

**See `references/customer_ml_workflows.md`.**

### 5. Contributor and workforce product

Task UX, payments, trust, locale.

**See `references/contributor_workforce_product.md`.**

### 6. Privacy, ethics, and policy

PII, consent, retention, labor.

**See `references/privacy_ethics_policy.md`.**

## Output standards

- PRDs state **persona, problem, success metrics, non-goals, and launch tier**
- Task specs include **worked examples** (gold, borderline, reject)
- Quality bar defined as **measurable thresholds**, not "high quality"
- Every feature maps to **cost, quality, or speed** lever
- Escalate legal/labor questions; do not ship policy in product copy alone

## When to load references

- **Roadmap** → `references/roadmap_prioritization.md`
- **Tasks** → `references/annotation_task_design.md`
- **Quality** → `references/quality_systems.md`
- **Customers** → `references/customer_ml_workflows.md`
- **Contributors** → `references/contributor_workforce_product.md`
- **Privacy** → `references/privacy_ethics_policy.md`
