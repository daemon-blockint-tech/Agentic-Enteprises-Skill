---
name: ai-risk-governance
description: |
  Guides AI risk management and governance—use-case risk assessment, model/system documentation,
  policies and guardrails, human oversight, third-party model/vendor review, and mapping to
  frameworks (NIST AI RMF, ISO 42001, EU AI Act concepts, internal AI policy).
  Use when classifying AI use cases, drafting AI acceptable-use policies, building risk registers,
  preparing model cards or DPIAs for AI, reviewing vendor LLMs, or aligning product teams with
  compliance—not for implementing RAG/agents (ai-engineer), running jailbreak tests (ai-redteam),
  or SOC 2/ISO evidence automation and technical control mapping (compliance-engineer),
  or general SOC 2 IT controls without AI scope (cybersecurity). For AI solution architecture in
  commercial or enterprise deployments, use applied-ai-architect-commercial-enterprise. For agent
  skills catalog standards and security review before publish, use ai-skill-manager.
---

# AI Risk & Governance

## When to Use

- Classifying AI use cases by risk tier and impact
- Drafting AI acceptable-use policies and governance frameworks
- Building AI risk registers with likelihood/severity/mitigation tracking
- Preparing model cards, system cards, or DPIAs for AI deployments
- Reviewing third-party LLM vendors (data terms, fine-tuning, safety commitments)
- Mapping AI products to frameworks (NIST AI RMF, ISO 42001, EU AI Act concepts)
- Aligning product and engineering teams with compliance requirements
- Designing human-in-the-loop oversight for consequential AI decisions

## When NOT to Use

- Implementing RAG pipelines, agents, or production features → `ai-engineer`
- Running jailbreak tests or adversarial campaigns → `ai-redteam`
- SOC 2/ISO evidence automation and technical control mapping → `compliance-engineer`
- General SOC 2 IT controls without AI scope → `cybersecurity`
- Commercial/enterprise AI solution architecture → `applied-ai-architect-commercial-enterprise`
- Skills portfolio governance and publish gates → `ai-skill-manager`

## Related skills

| Need | Skill |
|---|---|
| Building LLM products | `ai-engineer` |
| Adversarial testing | `ai-redteam` |
| Research and benchmarks | `ai-researcher` |
| Enterprise security program | `cybersecurity` |
| Pipeline and data security | `devsecops` |
| SOC 2/ISO evidence and technical controls | `compliance-engineer` |
| AI solution architecture (commercial/enterprise) | `applied-ai-architect-commercial-enterprise` |
| Agent skills governance | `ai-skill-manager` |

## Core Workflows

### 1. Use-case intake and classification

**Capture:**

| Field | Purpose |
|---|---|
| Purpose and users | Scope and accountability |
| Data types | PII, special categories, IP |
| Automation level | Human-in-loop vs autonomous |
| Impact if wrong | Safety, legal, financial, reputational |
| External exposure | Customer-facing vs internal |

**Risk tier (example):**

| Tier | Criteria | Controls |
|---|---|---|
| Low | Internal, low impact, no sensitive data | Standard policy + logging |
| Medium | Customer-facing or internal PII | Review + eval + monitoring |
| High | Regulated domain, high impact, autonomous actions | Governance board + red-team + enhanced oversight |

**See `references/risk_classification.md` for EU AI Act–oriented mapping (non-legal).**

### 2. Risk assessment

Use structured worksheet:

1. Identify hazards (bias, hallucination, leakage, misuse, dependency)
2. Estimate likelihood and severity
3. Define mitigations (technical, process, legal)
4. Assign owner and review date
5. Residual risk acceptance sign-off

**See `references/risk_assessment.md` for worksheets and NIST AI RMF functions.**

### 3. Documentation artifacts

| Artifact | When |
|---|---|
| Model card / system card | Every production model or vendor model |
| Data sheet | Training/fine-tune data described |
| Eval summary | Pre-deploy and periodic |
| Incident log | AI-specific harms and near-misses |

**See `references/documentation.md` for model card sections and change log.**

### 4. Policy and oversight

- Acceptable use policy (prohibited uses, approval paths)
- Human oversight rules for consequential decisions
- Escalation for policy violations and serious incidents
- Training for builders and reviewers

**See `references/policy_oversight.md` for governance committee cadence.**

### 5. Vendor and third-party models

Review: data processing terms, subprocessors, retention, fine-tuning on customer data, safety commitments, breach notification, exit plan.

**See `references/vendor_review.md` for vendor questionnaire topics.**

## When to load references

- **Tiering and regulation mapping** → `references/risk_classification.md`
- **Assessments and frameworks** → `references/risk_assessment.md`
- **Model cards** → `references/documentation.md`
- **Policies and committees** → `references/policy_oversight.md`
- **Vendors** → `references/vendor_review.md`
