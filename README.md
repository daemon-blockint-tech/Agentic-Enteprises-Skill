# Agentic Enterprise OS

**198-skill operating system for AI-native enterprises**

Repository: [github.com/daemon-blockint-tech/Agentic-Enteprises-Skill](https://github.com/daemon-blockint-tech/Agentic-Enteprises-Skill)

---

## Overview

Agentic Enterprise OS is not a collection of prompts — it is a **modular, layered operating system** for AI-native enterprises. It provides:

- **198 specialized skills** (each in `<skill-name>/SKILL.md` with reference playbooks)
- **5 workflow chains** for end-to-end operations (YAML under `.workflows/`)
- **4 execution modes** for different task complexities
- **Cross-cutting validation** via `build-validator`
- **Persistent memory** via `ai-memory-developer`
- **Dynamic routing** via `ai-skill-manager` and `ai-lead-ops`

Use [`.docs/SKILL_REGISTRY.md`](.docs/SKILL_REGISTRY.md) and [`.docs/ORCHESTRATION_ROUTING.md`](.docs/ORCHESTRATION_ROUTING.md) as the canonical routing index. The registry documents core layers in depth; additional domain packs (cloud, actuarial, expanded security, supply chain, and others) are registered at the folder level.

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

### Layered model

Skills are organized in layers (governance at the top, physical infrastructure at the base). The original seven-layer model still applies; many new skills extend **Layer 2 (infrastructure & security)**, **Layer 3 (data & analytics)**, **Layer 4 (AI/ML)**, and **Layer 0 (business & operations)**.

```
Layer 5: GOVERNANCE & ORCHESTRATION
    ↑
Layer 4: AI & ML OPERATIONS
    ↑
Layer 3: DATA & ANALYTICS
    ↑
Layer 2: INFRASTRUCTURE & SECURITY (incl. cloud, SRE, D3FEND, expanded AppSec)
    ↑
Layer 1: SOFTWARE ENGINEERING
    ↑
Layer 0: BUSINESS & OPERATIONS (incl. actuarial, insurance, supply chain, talent)
    ↑
Layer -1: PHYSICAL INFRASTRUCTURE
```

See [`.docs/ARCHITECTURE_GRAPH.md`](.docs/ARCHITECTURE_GRAPH.md) for dependency diagrams.

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
| [ARCHITECTURE_GRAPH.md](.docs/ARCHITECTURE_GRAPH.md) | Mermaid graphs of skills and dependencies |
| [ORCHESTRATION_ROUTING.md](.docs/ORCHESTRATION_ROUTING.md) | Routing logic, execution modes, state management, error handling |
| [SKILL_REGISTRY.md](.docs/SKILL_REGISTRY.md) | Skill registry with triggers, inputs, outputs (core catalog; extend with folder scan) |

## Workflow Templates

| Workflow | Description | File |
|----------|-------------|------|
| Data Pipeline | End-to-end data pipeline from architecture to BI | [.workflows/data-pipeline.yaml](.workflows/data-pipeline.yaml) |
| Security Ops | Full security audit with D3FEND response | [.workflows/security-ops.yaml](.workflows/security-ops.yaml) |
| Revenue Ops | End-to-end revenue operations | [.workflows/revenue-ops.yaml](.workflows/revenue-ops.yaml) |
| AI Product Dev | Build AI-powered product from research to deployment | [.workflows/ai-product-dev.yaml](.workflows/ai-product-dev.yaml) |
| Infra Deployment | Deploy infrastructure from design to production | [.workflows/infra-deployment.yaml](.workflows/infra-deployment.yaml) |

---

## Skill Domains (198 packages)

Skills live in top-level folders named `<skill-name>/` with `SKILL.md` and `references/`. Major domain packs include:

| Domain | Examples |
|--------|----------|
| **Governance & orchestration** | `build-validator`, `ai-risk-governance`, `ai-skill-manager`, `technical-program-manager` |
| **AI & ML** | `ai-researcher`, `ai-engineer`, `ai-lead-ops`, `ml-*-safeguards`, `agentic-ai-developer`, `multi-agent-system-engineer` |
| **Data & analytics** | `data-architect`, `data-scientist`, `predictive-analytics`, `data-visualization`, `bi-analyst` |
| **Cloud & platform** | `cloud-architect`, `cloud-engineer`, `enterprise-cloud-architect`, `finops-analyst`, `site-reliability-engineer`, `vp-of-infrastructure` |
| **Infrastructure & DevOps** | `infrastructure-engineer`, `platform-engineer`, `devops`, `devsecops`, `ci-cd-engineer` |
| **Security** | `cybersecurity`, D3FEND skills, `penetration-tester`, `threat-hunter`, `soc-analyst`, `enterprise-security-architect` |
| **Actuarial & insurance** | `pre-actuarial-foundations`, `actuarial-analyst`, `associate-actuary`, `appointed-chief-actuary`, `property-casualty-insurance`, `validation-by-educational-experience` |
| **Business & operations** | `business-consultant`, `commercial-counsel`, `supply-chain-manager`, `talent-acquisition`, `enterprise-strategist` |
| **Software engineering** | `senior-system-architecture`, `senior-software-engineer`, `performance-engineer`, `solutions-architect` |
| **Physical infrastructure** | Data-center portfolio, capacity, and field-services skills |

To list all skills locally:

```bash
find . -maxdepth 2 -name 'SKILL.md' | sed 's|/SKILL.md||' | sed 's|^\./||' | sort
```

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

Every skill output can pass through `build-validator`:

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

1. Create skill in `<skill-name>/SKILL.md` (use `name` and `description` frontmatter only).
2. Add six `references/*.md` playbooks where applicable.
3. Update [`.docs/SKILL_REGISTRY.md`](.docs/SKILL_REGISTRY.md) and [`.docs/ARCHITECTURE_GRAPH.md`](.docs/ARCHITECTURE_GRAPH.md).
4. Run `build-validator` (or project validation scripts) before merge.

---

## License

Internal use only. Not for external distribution.

---

**This is not a collection of prompts. This is an operating system for AI-native enterprises.**
