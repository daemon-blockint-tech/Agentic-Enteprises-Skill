# Agentic Enterprise OS

**86-Skill Operating System for AI-Native Enterprises**

---

## Overview

Agentic Enterprise OS is not a collection of prompts — it's a **modular, layered operating system** for AI-native enterprises. It provides:

- **86 specialized skills** across 7 layers
- **5 workflow chains** for end-to-end operations
- **4 execution modes** for different task complexities
- **Cross-cutting validation** via build-validator
- **Persistent memory** via ai-memory-developer
- **Dynamic routing** via ai-skill-manager

---

## Quick Start

### 1. Single Skill Task

```
User: "Design a data warehouse schema for sales analytics"
    ↓
Route: data-warehouse-engineer
    ↓
Execute → Return
```

### 2. Chain Execution

```
User: "Build end-to-end analytics for customer churn"
    ↓
Chain: data-architect → data-warehouse-engineer → analytics-data-engineer → data-scientist → bi-analyst
    ↓
Execute sequentially → Return
```

### 3. Parallel Execution

```
User: "Audit our security and optimize our data pipeline"
    ↓
Parallel: offensive-security-analyst + defensive-security-analyst + data-architect + analytics-data-engineer
    ↓
Execute concurrently → Merge results → Return
```

### 4. Orchestrated Execution

```
User: "Launch a new AI-powered product from scratch"
    ↓
Orchestrator: ai-lead-ops dynamically routes through 9+ skills
    ↓
Execute with dynamic routing → Return
```

---

## Architecture

### 7 Layers

```
Layer 5: GOVERNANCE & ORCHESTRATION (7 skills)
    ↑
Layer 4: AI & ML OPERATIONS (12 skills)
    ↑
Layer 3: DATA & ANALYTICS (9 skills)
    ↑
Layer 2: INFRASTRUCTURE & SECURITY (19 skills + 7 D3FEND)
    ↑
Layer 1: SOFTWARE ENGINEERING (9 skills)
    ↑
Layer 0: BUSINESS & OPERATIONS (17 skills)
    ↑
Layer -1: PHYSICAL INFRASTRUCTURE (6 skills)
```

### 5 Workflow Chains

1. **Data Pipeline:** architect → warehouse → analytics → scientist → BI → ops
2. **Security Ops:** offensive → defensive → D3FEND (7 skills) → compliance → incident
3. **Revenue Ops:** counsel → deal-ops → accountant → monetization → transaction
4. **AI Dev Chain:** researcher → research-safeguards → RL-engineering → infra-safeguards → engineer
5. **Software Dev Chain:** architecture → fullstack → frontend → UI → UX → support

### Cross-Cutting Concerns

- **build-validator**: Quality gate at every layer
- **ai-risk-governance**: AI safety overlay
- **compliance-engineer**: Compliance overlay
- **ai-memory-developer**: Persistent context across sessions

---

## Documentation

| Document | Description |
|----------|-------------|
| [HIGH_LEVEL_DESIGN.md](.docs/HIGH_LEVEL_DESIGN.md) | High-level architecture and system design |
| [ARCHITECTURE_GRAPH.md](.docs/ARCHITECTURE_GRAPH.md) | Mermaid graph of all 86 skills and dependencies |
| [ORCHESTRATION_ROUTING.md](.docs/ORCHESTRATION_ROUTING.md) | Routing logic, execution modes, state management, error handling |
| [SKILL_REGISTRY.md](.docs/SKILL_REGISTRY.md) | Complete registry of all 86 skills with triggers, inputs, outputs |

## Workflow Templates

| Workflow | Description | File |
|----------|-------------|------|
| Data Pipeline | End-to-end data pipeline from architecture to BI | [.workflows/data-pipeline.yaml](.workflows/data-pipeline.yaml) |
| Security Ops | Full security audit with D3FEND response | [.workflows/security-ops.yaml](.workflows/security-ops.yaml) |
| Revenue Ops | End-to-end revenue operations | [.workflows/revenue-ops.yaml](.workflows/revenue-ops.yaml) |
| AI Product Dev | Build AI-powered product from research to deployment | [.workflows/ai-product-dev.yaml](.workflows/ai-product-dev.yaml) |
| Infra Deployment | Deploy infrastructure from design to production | [.workflows/infra-deployment.yaml](.workflows/infra-deployment.yaml) |

---

## Skill Categories

### Governance & Orchestration (7)
- build-validator, ai-risk-governance, engineering-manager-agent-prompts-evals, engineering-manager-vertical-ai-products, ai-skill-manager, technical-program-manager, technical-program-manager-security-cvd

### AI & ML Operations (12)
- ai-researcher, ai-engineer, ai-lead-ops, ai-redteam, ai-token-improvement-plan-engineer, ai-context-engineer, ai-memory-developer, ai-skill-manager (ops), prompt-engineer, prompt-engineer-agent-prompts-evals, ml-research-engineer-safeguards, ml-systems-engineer-rl-engineering, ml-infrastructure-engineer-safeguards

### Data & Analytics (9)
- data-architect, data-warehouse-engineer, analytics-data-engineer, analytics-data-engineering-manager-product, data-scientist, bi-analyst, ontology-engineer, data-system-ops-lead, data-manager

### Infrastructure & Security (19 + 7 D3FEND)
- infrastructure-engineer, platform-engineer, cluster-deployment-engineer, devops, devsecops, deployment-strategist, cybersecurity, information-security-engineer, incident-management-engineer, offensive-security-analyst, defensive-security-analyst, compliance-engineer
- D3FEND: harden, detect, evict, isolate, restore, model, deceive

### Software Engineering (9)
- senior-system-architecture, senior-fullstack-developer, fullstack-software-engineer, senior-software-engineer, senior-frontend-software-engineer, ui-software-engineer, ux-software-engineer, web-application-developer, support-engineer

### Business & Operations (17)
- business-model-researcher, business-consultant, commercial-counsel, corporate-counsel, senior-revenue-accountant, deal-operations-administrator, transaction-manager, transaction-principal, product-management-monetization, product-management-human-data-platform, product-designer, customer-ops-specialist, product-support-specialist, community-executive-escalations-program-manager, communication-lead, developer-education-lead, people-operations-specialist

### Physical Infrastructure (6)
- data-center-design-execution-lead, data-center-portfolio-planning-execution-lead, data-center-compute-supply-efficiency, director-infrastructure-capex-accounting, senior-data-center-capacity-delivery-manager, field-services-engineer

---

## Execution Modes

| Mode | Use When | Characteristics |
|------|----------|-----------------|
| Single | Quick, focused task | Low latency, single context |
| Chain | Multi-step workflow | Sequential, state passed between skills |
| Parallel | Independent tasks | Concurrent, results merged |
| Orchestrated | Complex, ambiguous tasks | Dynamic routing, AI manager |

---

## Quality Gates

Every skill output passes through `build-validator`:

- **Architecture**: System design is sound
- **Security**: No vulnerabilities
- **Cost**: Within budget
- **Compliance**: Meets regulations
- **Performance**: Meets targets
- **Scalability**: Can scale to load

---

## Usage Examples

### Data Pipeline
```
User: "Build end-to-end analytics pipeline"
    ↓
Chain: data-architect → data-warehouse-engineer → analytics-data-engineer → data-scientist → bi-analyst
    ↓
Validation: build-validator after architect and scientist
    ↓
Return: Complete analytics pipeline with dashboard
```

### Security Audit
```
User: "Full security audit with D3FEND response"
    ↓
Chain: offensive-security-analyst → defensive-security-analyst → D3FEND (7 skills) → compliance-engineer → incident-management-engineer
    ↓
Validation: build-validator after offensive and D3FEND
    ↓
Return: Complete security audit with defense plan
```

### AI Product Development
```
User: "Build AI-powered product from scratch"
    ↓
Orchestrator: ai-lead-ops
    ↓
Dynamic: business-model-researcher → ai-researcher → senior-system-architecture → data-architect → ai-engineer → senior-fullstack-developer → cybersecurity → compliance-engineer → build-validator
    ↓
Return: Complete AI product with security and compliance
```

---

## Contributing

1. Create skill in `<skill-name>/SKILL.md`
2. Add triggers, inputs, outputs, dependencies
3. Update SKILL_REGISTRY.md
4. Update ARCHITECTURE_GRAPH.md
5. Run build-validator to validate

---

## License

Internal use only. Not for external distribution.

---

**This is not a collection of prompts. This is an operating system for AI-native enterprises.**
