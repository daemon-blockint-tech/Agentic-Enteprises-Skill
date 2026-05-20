# Agentic Enterprise OS

**~200-Skill Operating System for AI-Native Enterprises**

[![skills.sh](https://skills.sh/b/daemon-blockint-tech/Agentic-Enteprises-Skill)](https://skills.sh/daemon-blockint-tech/Agentic-Enteprises-Skill)

---

## Overview

Agentic Enterprise OS is not a collection of prompts — it's a **modular, layered operating system** for AI-native enterprises. It provides:

- **~198 specialized skills** (one `SKILL.md` per domain folder) across the original 7-layer model plus major expansions
- **8 workflow chains** for end-to-end operations (YAML templates in `.workflows/`, skills.sh install hints)
- **4 execution modes** for different task complexities
- **Cross-cutting validation** via `build-validator`
- **Persistent memory** via `ai-memory-developer`
- **Dynamic routing** via `ai-skill-manager`

Recent expansions add depth in **actuarial and insurance**, **cloud and FinOps**, **SRE and resilience**, **predictive analytics**, **ML safeguards and agentic AI**, **AML and financial crime**, **supply chain**, **OT/ICS and networking**, and a **broader security portfolio** (CTI, pentest, formal methods, vendor risk, executive security roles).

---

## Install via skills.sh

This package is installable from the [Agent Skills directory](https://skills.sh) using the open-source [skills CLI](https://www.skills.sh/docs/cli) (`npx skills add` — no global install required).

**Source:** [github.com/daemon-blockint-tech/Agentic-Enteprises-Skill](https://github.com/daemon-blockint-tech/Agentic-Enteprises-Skill)

### Cursor

Run from the **root of the project** where you want skills available (your app repo, not necessarily this catalog clone):

```bash
# Browse ~197 skills in this package
npx skills add daemon-blockint-tech/Agentic-Enteprises-Skill --list

# Install specific skills for Cursor
npx skills add daemon-blockint-tech/Agentic-Enteprises-Skill \
  --skill cloud-architect \
  --skill compliance-engineer \
  --agent cursor -y

# Interactive picker
npx skills add daemon-blockint-tech/Agentic-Enteprises-Skill --agent cursor
```

After install, start a **new Cursor session** so agents pick up the installed `SKILL.md` files. See [Skills for Cursor](https://www.skills.sh/agent/cursor).

If the [skills.sh package page](https://skills.sh/daemon-blockint-tech/Agentic-Enteprises-Skill) shows fewer skills than this repo, use `npx skills add daemon-blockint-tech/Agentic-Enteprises-Skill --list` for the full catalog—the directory index can lag behind GitHub.

### Other agents

The same CLI targets Claude Code, Codex, GitHub Copilot, Windsurf, Gemini, and others:

```bash
npx skills add daemon-blockint-tech/Agentic-Enteprises-Skill --agent claude-code -y
npx skills add daemon-blockint-tech/Agentic-Enteprises-Skill --agent '*' -y   # all supported agents
```

More: [skills.sh documentation](https://www.skills.sh/docs).

### Clone vs install

| Approach | When to use |
|----------|-------------|
| **`npx skills add …`** | Install skills into another project's agent paths (recommended for day-to-day work in Cursor, etc.) |
| **Clone this repo** | Browse the catalog, contribute skills, or point an agent at `<skill-name>/SKILL.md` in-tree |
| **Fork** | Maintain a private or customized enterprise skill portfolio |

Leaderboard ranking uses anonymous install telemetry from the CLI ([how skills are ranked](https://www.skills.sh/docs)). Opt out: `DISABLE_TELEMETRY=1`.

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
Orchestrator: ai-lead-ops dynamically routes through many skills
    ↓
Execute with dynamic routing → Return
```

---

## Using Skills

Each skill lives in `<skill-name>/SKILL.md` with YAML frontmatter (`name`, `description` triggers) and optional `references/` depth material.

| Goal | What to do |
|------|------------|
| **Find a skill** | Search this repo by keyword, or open [`.docs/SKILL_REGISTRY.md`](.docs/SKILL_REGISTRY.md) for the indexed catalog |
| **Route work** | Match user intent to a skill's `description` triggers; use `ai-skill-manager` for overlap, gaps, and portfolio hygiene |
| **Run a workflow** | Pick a template under [`.workflows/`](.workflows/) (data pipeline, security ops, revenue ops, AI product dev, infra deployment) |
| **Add a skill** | Create `<skill-name>/SKILL.md`, then update registry and architecture docs (see Contributing) |

**Agent clients (Cursor, Claude Code, etc.):** prefer [`npx skills add daemon-blockint-tech/Agentic-Enteprises-Skill`](#install-via-skillssh) for installs into your project; alternatively clone this repo or copy `<skill-name>/` folders into your agent skills path. Skills are discovered from `SKILL.md` files; no separate runtime is required beyond your agent host.

---

## Architecture

### 7 Layers (conceptual model)

The OS still organizes work into seven layers. Skill count per layer has grown well beyond the original 86-skill baseline; treat layers as **routing planes**, not fixed headcount.

```
Layer 5: GOVERNANCE & ORCHESTRATION
    ↑
Layer 4: AI & ML OPERATIONS
    ↑
Layer 3: DATA & ANALYTICS
    ↑
Layer 2: INFRASTRUCTURE & SECURITY
    ↑
Layer 1: SOFTWARE ENGINEERING
    ↑
Layer 0: BUSINESS & OPERATIONS
    ↑
Layer -1: PHYSICAL INFRASTRUCTURE
```

### 8 Workflow Templates

Executable YAML in [.workflows/](.workflows/) (v1.2.0, skills.sh install chains):

1. **Data Pipeline** — `data-pipeline.yaml`
2. **Security Ops** — `security-ops.yaml` (CTI → hunt → offensive → D3FEND → compliance → IR)
3. **Revenue Ops** — `revenue-ops.yaml`
4. **AI Product Dev** — `ai-product-dev.yaml` (orchestrated)
5. **Infra Deployment** — `infra-deployment.yaml`
6. **Cloud & FinOps** — `cloud-finops.yaml`
7. **Actuarial Credential** — `actuarial-credential.yaml`
8. **AML Operations** — `aml-operations.yaml`

**Compose manually:** software dev (architecture → fullstack → frontend → UI → UX → support)

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
| [ARCHITECTURE_GRAPH.md](.docs/ARCHITECTURE_GRAPH.md) | Mermaid graph of skills and dependencies |
| [ORCHESTRATION_ROUTING.md](.docs/ORCHESTRATION_ROUTING.md) | Routing logic, execution modes, state management, error handling |
| [SKILL_REGISTRY.md](.docs/SKILL_REGISTRY.md) | Full 198-skill catalog (layer tables + skills.sh index) |

> **Note:** `.docs/SKILL_REGISTRY.md` is generated from all `SKILL.md` files (`python3 scripts/generate_docs_registry.py`). Architecture graph shows core relationships; full catalog is in the registry.

## Workflow Templates

Each workflow includes `package`, `install.chain_cursor` (skills.sh CLI), and `skills_sh_folder` per step. Schema reference: [.workflows/_workflow-schema.yaml](.workflows/_workflow-schema.yaml).

| Workflow | Mode | Description | File |
|----------|------|-------------|------|
| Data Pipeline | chain | Architecture → warehouse → analytics → science → BI → ops | [.workflows/data-pipeline.yaml](.workflows/data-pipeline.yaml) |
| Security Ops | chain | CTI → hunt → offensive → defensive → D3FEND → compliance → IR | [.workflows/security-ops.yaml](.workflows/security-ops.yaml) |
| Revenue Ops | chain | Counsel → deal ops → accounting → monetization → transactions | [.workflows/revenue-ops.yaml](.workflows/revenue-ops.yaml) |
| AI Product Dev | orchestrated | Research → safeguards → agentic AI → build → red team → gate | [.workflows/ai-product-dev.yaml](.workflows/ai-product-dev.yaml) |
| Infra Deployment | chain | Infra → platform → K8s → CI/CD → DevSecOps → SRE → rollout | [.workflows/infra-deployment.yaml](.workflows/infra-deployment.yaml) |
| Cloud & FinOps | chain | Cloud architecture → security → compliance → FinOps → SRE | [.workflows/cloud-finops.yaml](.workflows/cloud-finops.yaml) |
| Actuarial Credential | chain | Foundations → exams → VEE → analyst → associate → actuary | [.workflows/actuarial-credential.yaml](.workflows/actuarial-credential.yaml) |
| AML Operations | chain | AML program → monitoring → FIU → STR → false-positive tuning | [.workflows/aml-operations.yaml](.workflows/aml-operations.yaml) |

---

## Skill Categories

### Core layers (original portfolio)

| Layer | Representative skills |
|-------|------------------------|
| **Governance & orchestration** | `build-validator`, `ai-risk-governance`, `ai-skill-manager`, `technical-program-manager`, `engineering-manager-*` |
| **AI & ML operations** | `ai-researcher`, `ai-engineer`, `ai-lead-ops`, `ai-redteam`, `prompt-engineer`, `ml-*-safeguards`, `ml-systems-engineer-rl-engineering` |
| **Data & analytics** | `data-architect`, `data-warehouse-engineer`, `analytics-data-engineer`, `data-scientist`, `bi-analyst`, `ontology-engineer` |
| **Infrastructure & security** | `infrastructure-engineer`, `platform-engineer`, `devops`, `devsecops`, `cybersecurity`, `offensive-security-analyst`, `defensive-security-analyst`, D3FEND (`d3fend-*`) |
| **Software engineering** | `senior-system-architecture`, `senior-fullstack-developer`, `ui-software-engineer`, `ux-software-engineer`, `support-engineer` |
| **Business & operations** | `business-consultant`, `commercial-counsel`, `deal-operations-administrator`, `product-management-monetization`, `customer-ops-specialist` |
| **Physical infrastructure** | `data-center-*`, `field-services-engineer`, `director-infrastructure-capex-accounting` |

### Expanded domains (examples)

| Domain | Example skills |
|--------|----------------|
| **Actuarial & insurance** | `actuary`, `actuarial-analyst`, `actuarial-consulting`, `appointed-chief-actuary`, `associate-actuary`, `asset-liability-management`, `assumption-setting`, `advanced-*-actuarial-mathematics`, `property-casualty-insurance`, `life-health-insurance`, `pension-retirement-funds`, `ifrs`, `ab-testing-engineer` |
| **AML & financial crime** | `aml-cft`, `aml-compliance`, `financial-intelligence-unit`, `str-report`, `anti-false-positive-decision-making` |
| **Cloud, FinOps & platform** | `cloud-architect`, `cloud-engineer`, `cloud-security-engineer`, `cloud-economist`, `cloud-compliance-specialist`, `enterprise-cloud-architect`, `finops-analyst`, `vp-of-cloud`, `vp-of-infrastructure` |
| **SRE & resilience** | `site-reliability-engineer`, `sla-slo-engineer`, `bcm-disaster-recovery-specialist` |
| **Predictive & quantitative analytics** | `predictive-analytics`, `predictive-logistics-developer`, `quantitative-researcher`, `sentiment-analysis-engineer`, `sentiment-forecasting-engineer`, `operations-research-algorithm-developer` |
| **ML safeguards & agentic AI** | `ml-research-engineer-safeguards`, `ml-infrastructure-engineer-safeguards`, `privacy-research-engineer-safeguards`, `ai-adversarial-robustness-engineer`, `agentic-ai-developer`, `multi-agent-system-engineer` |
| **Security (expanded)** | `advanced-persistent-threat`, `cti-analyst`, `penetration-tester`, `red-team-specialist`, `web-pentester`, `network-pentester`, `cyber-resilience-engineer`, `enterprise-security-architect`, `vendor-cyber-risk-analyst`, `scada-ics-cyber-security-specialist`, `yara-rule-authoring`, `cryptographer-specialist`, `reverse-engineer`, `software-assurance-formal-methods-specialist`, `chief-information-security-officer`, `certified-information-systems-security-professional` |
| **Supply chain, IoT & edge** | `supply-chain-manager`, `iot-network-edge-engineer`, `robotics-automation-integration-engineer`, `wms-developer`, `geospatial-telematics-developer` |
| **Networking** | `cisco-certified-network-professional`, `sd-wan-engineer`, `network-backbone-architect`, `wireless-wifi-mobility-specialist` |

For the full list, run `find . -maxdepth 2 -name SKILL.md` or browse [`.docs/SKILL_REGISTRY.md`](.docs/SKILL_REGISTRY.md).

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

1. Create skill in `<skill-name>/SKILL.md` (YAML frontmatter + triggers in `description`)
2. Add references under `references/` as needed
3. Regenerate registry: `python3 scripts/generate_docs_registry.py`; update [`.docs/ARCHITECTURE_GRAPH.md`](.docs/ARCHITECTURE_GRAPH.md) if routing relationships change
4. Run `build-validator` (or portfolio checks via `ai-skill-manager`) to validate routing and overlap

---

## License

Internal use only. Not for external distribution.

---

**This is not a collection of prompts. This is an operating system for AI-native enterprises.**
