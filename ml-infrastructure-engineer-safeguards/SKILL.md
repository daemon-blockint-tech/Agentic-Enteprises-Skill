---
name: ml-infrastructure-engineer-safeguards
description: |
  Guides ML infrastructure for safeguards—inference gateways, model serving (GPU/CPU), guardrail and
  moderation pipelines in the request path, policy enforcement hooks, safety observability, rollout
  of filter/model versions, and reliability of the protected inference plane.
  Use when designing or operating safeguard layers on LLM/ML endpoints, deploying classifiers or
  moderation services, wiring pre/post-filters, scaling safety microservices, or debugging
  block-rate/latency regressions on the safety path—not for corporate AI policy (ai-risk-governance),
  building RAG/agents (ai-engineer), adversarial test campaigns (ai-redteam), general CI/CD
  (devops), app perf profiling (performance-engineer), or DC facility compute programs
  (data-center-compute-supply-efficiency). Safeguard R&D: ml-research-engineer-safeguards;
  privacy research: privacy-research-engineer-safeguards.
---

# ML Infrastructure Engineer, Safeguards

## When to Use

- Design **inference gateway** with safeguard stages (auth, rate limit, pre-filter, model, post-filter)
- Deploy **model servers** — GPU pools, replicas, autoscaling, health checks
- Operate **moderation/classifier** services (hosted or self-hosted) in production
- Configure **policy runtime** — thresholds, categories, block vs rewrite vs escalate
- Instrument **safety metrics** — block rate, false positive sampling, safety-path latency
- Roll out **safeguard model versions** — canary, rollback, config flags
- Plan **capacity** for safety + main model (queueing, shedding, degradation modes)
- Integrate **human review** queues and appeal flows at infrastructure boundary
- Debug production incidents — safety service down, filter bypass, p99 on guard path

## When NOT to Use

- Draft AI acceptable-use policy or risk tiers → `ai-risk-governance`
- Implement product RAG, agents, or prompts → `ai-engineer`, `prompt-engineer`
- Run jailbreak/red-team engagements → `ai-redteam`
- Build generic developer portal or golden paths → `platform-engineer`
- SOC 2 control evidence mapping → `compliance-engineer`
- End-to-end commercial AI architecture ADRs → `applied-ai-architect-commercial-enterprise`
- AI ops cadence and vendor contracts → `ai-lead-ops`
- Classical ML experimentation and feature science → `data-scientist`

## Related skills

| Need | Skill |
|---|---|
| LLM product features and eval harnesses | `ai-engineer` |
| Governance, model cards, regulatory mapping | `ai-risk-governance` |
| Adversarial testing before launch | `ai-redteam` |
| Pipelines, GitOps, generic SLOs | `devops` |
| K8s cluster and Helm for shared platform | `cluster-deployment-engineer` |
| Latency/load on app paths | `performance-engineer` |
| GPU supply at facility/portfolio level | `data-center-compute-supply-efficiency` |
| Tenant isolation on product runtime | `product-infrastructure-security-engineer` |
| Release governance and incident rituals | `ai-lead-ops` |
| Enterprise AI architecture | `applied-ai-architect-commercial-enterprise` |
| Classifier research, eval suites, promotion | `ml-research-engineer-safeguards` |

## Core Workflows

### 1. Inference and serving platform

Gateways, model servers, scaling.

**See `references/inference_serving_platform.md`.**

### 2. Safeguards request path

Pre/post filters, ordering, failure modes.

**See `references/safeguards_request_path.md`.**

### 3. Policy runtime enforcement

Thresholds, actions, human loop hooks.

**See `references/policy_runtime_enforcement.md`.**

### 4. Safety observability

Metrics, logs, sampling, privacy.

**See `references/safety_observability.md`.**

### 5. Model and config rollout

Versions, canaries, kill switches.

**See `references/model_version_rollout.md`.**

### 6. Capacity and reliability

GPU, degradation, DR.

**See `references/capacity_reliability.md`.**

## Outputs

- **Architecture diagram** — request path with safeguard stages and dependencies
- **Runbook** — deploy, rollback, scale, incident playbooks for safety services
- **Config spec** — policy thresholds, model IDs, feature flags per environment
- **SLO sheet** — availability and p99 for gateway + each safety stage
- **Capacity plan** — GPU/CPU headroom, QPS limits, degradation matrix
- **Rollout plan** — canary criteria tied to block-rate and error budgets

## Principles

- **Fail closed for high-risk tiers** — when safety path unavailable, default deny or safe response per policy
- **Latency budgeted** — safety is part of user-facing SLO, not best-effort
- **Observable decisions** — log decision codes, not raw harmful content in clear text
- **Version everything** — policy config, classifier weights, and gateway routing independently
- **Test in prod-like path** — staging must run full safeguard chain, not model-only
