# Agentic Enterprise OS - Orchestration & Routing

## Overview

This document defines how the **198** skills route, chain, and orchestrate work across the enterprise. It covers routing logic, execution patterns, error handling, state management, workflow templates, and **skills.sh** distribution.

**Package:** `daemon-blockint-tech/Agentic-Enteprises-Skill` — [skills.sh](https://skills.sh/daemon-blockint-tech/Agentic-Enteprises-Skill) · [CLI docs](https://www.skills.sh/docs/cli) · [Cursor](https://www.skills.sh/agent/cursor)

---

## 0. skills.sh discovery and install

External agents discover skills through the [skills CLI](https://www.skills.sh/docs/cli), not a separate registry API:

```bash
npx skills add daemon-blockint-tech/Agentic-Enteprises-Skill --list
npx skills add daemon-blockint-tech/Agentic-Enteprises-Skill --skill data-architect --agent cursor -y
```

| Step | Behavior |
|------|----------|
| **List** | Clone package; enumerate all `*/SKILL.md` folders |
| **Install** | Copy or symlink selected skills into agent paths (e.g. Cursor, Claude Code) |
| **Route** | Agent loads `description` frontmatter as trigger catalog |
| **Rank** | Anonymous install telemetry feeds [skills.sh leaderboard](https://skills.sh) |

**In-repo routing** (orchestrator, chains, workflows) uses the same folder names as skills.sh `--skill` arguments. Catalog index: [SKILL_REGISTRY.md](SKILL_REGISTRY.md).

---

## 1. Routing Architecture

### 1.1 Skill Selection Logic

```
User Request
    ↓
[Intent Classifier]
    ↓
┌─────────────────────────────────────┐
│  Layer Router (6 layers)            │
│  - Physical Infrastructure          │
│  - Business & Operations            │
│  - Software Engineering             │
│  - Infrastructure & Security        │
│  - Data & Analytics                 │
│  - AI & ML Operations               │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│  Skill Router (198 skills)          │
│  - Match trigger phrases            │
│  - Check skill availability         │
│  - Validate dependencies            │
│  - Select primary + backup skills   │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│  Execution Mode Selector            │
│  - Single Skill                     │
│  - Chain Execution                  │
│  - Parallel Execution               │
│  - Orchestrated (AI Manager)        │
└─────────────────────────────────────┘
    ↓
Execute & Return
```

### 1.2 Trigger Phrase Matching

Each skill defines explicit trigger phrases in its SKILL.md:

```yaml
skill: data-architect
triggers:
  - "design data architecture"
  - "create data model"
  - "plan data warehouse"
  - "data pipeline architecture"
  - "schema design"
  - "data governance framework"

skill: offensive-security-analyst
triggers:
  - "penetration test"
  - "vulnerability assessment"
  - "red team"
  - "security audit"
  - "exploit development"
  - "attack surface analysis"
```

### 1.3 Routing Priority

1. **Exact Match**: Trigger phrase matches exactly
2. **Semantic Match**: Intent matches skill purpose
3. **Layer Fallback**: Route to layer specialist
4. **Orchestrator Fallback**: AI manager routes dynamically

---

## 2. Execution Modes

### 2.1 Single Skill Mode

**Use when**: Quick, focused task that one skill can handle

```
User: "Design a data warehouse schema for sales analytics"
    ↓
Route: data-warehouse-engineer
    ↓
Execute → Return
```

**Characteristics**:
- Low latency
- Single context window
- No state sharing needed
- Direct response

### 2.2 Chain Execution Mode

**Use when**: Multi-step workflow with clear dependencies

```
User: "Build end-to-end analytics for customer churn"
    ↓
Chain:
  1. data-architect (design schema)
  2. data-warehouse-engineer (build ETL)
  3. analytics-data-engineer (create pipelines)
  4. data-scientist (build churn model)
  5. bi-analyst (create dashboard)
    ↓
Execute sequentially → Return
```

**Characteristics**:
- Sequential execution
- State passed between skills
- Each skill waits for previous output
- Error stops chain

### 2.3 Parallel Execution Mode

**Use when**: Independent tasks that don't depend on each other

```
User: "Audit our security and optimize our data pipeline"
    ↓
Parallel:
  ├─ offensive-security-analyst (security audit)
  ├─ defensive-security-analyst (blue team review)
  ├─ data-architect (pipeline review)
  └─ analytics-data-engineer (ETL optimization)
    ↓
Execute in parallel → Merge results → Return
```

**Characteristics**:
- Concurrent execution
- No state sharing needed
- Results merged at end
- Faster than chain

### 2.4 Orchestrated Mode

**Use when**: Complex, ambiguous tasks requiring dynamic routing

```
User: "Launch a new AI-powered product from scratch"
    ↓
Orchestrator: ai-lead-ops
    ↓
Dynamic routing:
  1. business-model-researcher (market analysis)
  2. ai-researcher (feasibility study)
  3. senior-system-architecture (system design)
  4. data-architect (data requirements)
  5. ai-engineer (AI development)
  6. senior-fullstack-developer (app development)
  7. cybersecurity (security review)
  8. compliance-engineer (compliance check)
  9. build-validator (quality gate)
    ↓
Execute with dynamic routing → Return
```

**Characteristics**:
- AI manager makes routing decisions
- Dynamic skill selection
- Conditional branching
- Error recovery

---

## 3. State Management

### 3.1 Context Passing

Skills pass context using structured payloads:

```json
{
  "context": {
    "task_id": "task-12345",
    "previous_skill": "data-architect",
    "next_skill": "data-warehouse-engineer",
    "state": {
      "schema": {...},
      "requirements": [...],
      "constraints": {...}
    },
    "metadata": {
      "started_at": "2026-05-20T10:00:00Z",
      "execution_mode": "chain",
      "chain_position": 2,
      "chain_length": 5
    }
  }
}
```

### 3.2 Memory Persistence

`ai-memory-developer` provides persistent context across sessions:

```
Session 1: User defines data architecture
    ↓
ai-memory-developer stores:
  - Schema definitions
  - Design decisions
  - Constraints
  - Preferences
    ↓
Session 2: User asks for ETL design
    ↓
ai-memory-developer retrieves prior context
    ↓
data-warehouse-engineer uses full context
```

### 3.3 State Validation

`build-validator` validates state at each step:

```json
{
  "validation": {
    "skill": "data-warehouse-engineer",
    "status": "pass",
    "checks": {
      "architecture": "pass",
      "security": "pass",
      "cost": "pass",
      "compliance": "pass"
    },
    "next_steps": ["analytics-data-engineer"],
    "warnings": []
  }
}
```

---

## 4. Error Handling

### 4.1 Error Types

| Error Type | Description | Recovery |
|------------|-------------|----------|
| Skill Not Found | No skill matches trigger | Route to orchestrator |
| Dependency Missing | Required skill unavailable | Fallback to alternative |
| Validation Failed | build-validator rejects | Return to previous skill |
| Timeout | Skill exceeds time limit | Retry or escalate |
| Context Lost | State not passed correctly | Request user input |
| Chain Broken | Skill in chain fails | Skip or abort |

### 4.2 Recovery Strategies

```
Error: Validation Failed
    ↓
build-validator returns rejection
    ↓
┌─────────────────────────────────────┐
│  Recovery Options:                  │
│  1. Return to previous skill        │
│  2. Request user clarification      │
│  3. Use fallback skill              │
│  4. Abort and report                │
└─────────────────────────────────────┘
    ↓
Execute recovery → Retry or escalate
```

### 4.3 Error Propagation

```
Chain: A → B → C → D
    ↓
Error in C
    ↓
┌─────────────────────────────────────┐
│  Propagation:                       │
│  - Stop D from executing            │
│  - Return error to B                │
│  - B can retry or abort             │
│  - User notified of failure         │
└─────────────────────────────────────┘
```

---

## 5. Workflow Templates

### 5.1 Data Pipeline Template

```yaml
name: data-pipeline
description: Build end-to-end data pipeline
skills:
  - data-architect
  - data-warehouse-engineer
  - analytics-data-engineer
  - data-scientist
  - bi-analyst
  - data-system-ops-lead
execution_mode: chain
validation_points:
  - after: data-architect
    validator: build-validator
  - after: data-scientist
    validator: build-validator
triggers:
  - "build data pipeline"
  - "create analytics pipeline"
  - "end-to-end data workflow"
```

### 5.2 Security Audit Template

```yaml
name: security-audit
description: Full security audit with D3FEND response
skills:
  - offensive-security-analyst
  - defensive-security-analyst
  - d3fend-harden
  - d3fend-detect
  - d3fend-evict
  - d3fend-isolate
  - d3fend-restore
  - d3fend-model
  - d3fend-deceive
  - compliance-engineer
  - incident-management-engineer
execution_mode: chain
validation_points:
  - after: offensive-security-analyst
    validator: build-validator
  - after: d3fend-deceive
    validator: build-validator
triggers:
  - "full security audit"
  - "penetration test with response"
  - "security assessment with D3FEND"
```

### 5.3 AI Product Development Template

```yaml
name: ai-product-dev
description: Build AI-powered product from research to deployment
skills:
  - business-model-researcher
  - ai-researcher
  - ml-research-engineer-safeguards
  - ml-systems-engineer-rl-engineering
  - ml-infrastructure-engineer-safeguards
  - ai-engineer
  - senior-system-architecture
  - senior-fullstack-developer
  - cybersecurity
  - compliance-engineer
  - build-validator
execution_mode: orchestrated
orchestrator: ai-lead-ops
validation_points:
  - after: ai-researcher
    validator: ai-risk-governance
  - after: ai-engineer
    validator: build-validator
triggers:
  - "build AI product"
  - "develop AI application"
  - "AI product from scratch"
```

### 5.4 Revenue Operations Template

```yaml
name: revenue-ops
description: End-to-end revenue operations workflow
skills:
  - commercial-counsel
  - deal-operations-administrator
  - senior-revenue-accountant
  - product-management-monetization
  - transaction-manager
  - transaction-principal
execution_mode: chain
validation_points:
  - after: senior-revenue-accountant
    validator: compliance-engineer
  - after: transaction-manager
    validator: build-validator
triggers:
  - "setup revenue operations"
  - "deal to revenue workflow"
  - "end-to-end revenue process"
```

### 5.5 Infrastructure Deployment Template

```yaml
name: infra-deployment
description: Deploy infrastructure from design to production
skills:
  - infrastructure-engineer
  - platform-engineer
  - cluster-deployment-engineer
  - devops
  - devsecops
  - deployment-strategist
execution_mode: chain
validation_points:
  - after: infrastructure-engineer
    validator: build-validator
  - after: devsecops
    validator: compliance-engineer
triggers:
  - "deploy infrastructure"
  - "setup cloud platform"
  - "production deployment"
```

---

## 6. Cross-Layer Dependencies

### 6.1 Dependency Matrix

| Layer | Depends On | Provides To |
|-------|-----------|-------------|
| L5: Governance | All layers | Validation, routing, management |
| L4: AI/ML | L3 (Data), L2 (Infra) | AI capabilities, models |
| L3: Data | L2 (Infra), L1 (Software) | Data pipelines, analytics |
| L2: Infra/Sec | L1 (Software), L-1 (Physical) | Hosting, security, platform |
| L1: Software | L0 (Business) | Applications, services |
| L0: Business | L-1 (Physical) | Business logic, operations |
| L-1: Physical | None | Infrastructure foundation |

### 6.2 Dependency Resolution

```
Request: "Build AI analytics dashboard"
    ↓
Resolve dependencies:
  1. L4: ai-engineer (needs L3 data)
  2. L3: data-scientist (needs L2 infra)
  3. L2: infrastructure-engineer (needs L1 software)
  4. L1: senior-fullstack-developer (needs L0 business)
  5. L0: product-designer (needs L-1 physical)
    ↓
Execute in dependency order:
  L-1 → L0 → L1 → L2 → L3 → L4
    ↓
Return integrated result
```

---

## 7. Quality Gates

### 7.1 build-validator Checks

| Check | Description | When Applied |
|-------|-------------|--------------|
| Architecture | System design is sound | After architecture skills |
| Security | No security vulnerabilities | After all skills |
| Cost | Within budget constraints | After infrastructure skills |
| Compliance | Meets regulatory requirements | After business/legal skills |
| Performance | Meets performance targets | After engineering skills |
| Scalability | Can scale to expected load | After architecture skills |

### 7.2 Validation Flow

```
Skill completes
    ↓
build-validator runs checks
    ↓
┌─────────────────────────────────────┐
│  Results:                           │
│  - Architecture: PASS               │
│  - Security: PASS                   │
│  - Cost: PASS                       │
│  - Compliance: PASS                 │
│  - Performance: PASS                │
│  - Scalability: PASS                │
└─────────────────────────────────────┘
    ↓
All PASS → Continue chain
Any FAIL → Return to skill for fix
```

---

## 8. Monitoring & Observability

### 8.1 Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| Task Completion Rate | % of tasks completed successfully | >95% |
| Chain Success Rate | % of chains completing without error | >90% |
| Validation Pass Rate | % of tasks passing build-validator | >85% |
| Average Latency | Time from request to response | <30s |
| Error Recovery Rate | % of errors successfully recovered | >80% |
| Skill Utilization | % of skills used in last 30 days | >70% |

### 8.2 Logging

```json
{
  "log": {
    "timestamp": "2026-05-20T10:00:00Z",
    "task_id": "task-12345",
    "skill": "data-architect",
    "action": "execute",
    "status": "success",
    "duration_ms": 1500,
    "input_tokens": 500,
    "output_tokens": 1200,
    "validation": "pass",
    "next_skill": "data-warehouse-engineer"
  }
}
```

---

## 9. Scaling Strategy

### 9.1 Horizontal Scaling

- Multiple skill instances for parallel execution
- Load balancer distributes requests
- State shared via ai-memory-developer

### 9.2 Vertical Scaling

- Complex tasks use orchestrated mode
- AI manager dynamically allocates resources
- Priority queue for urgent tasks

### 9.3 Caching

- Frequently used skill outputs cached
- Context reused across similar requests
- build-validator results cached for 24h

---

## 10. Future Enhancements

1. **Auto-Routing**: ML model predicts best skill chain
2. **Self-Healing**: Skills auto-recover from errors
3. **Skill Discovery**: Auto-discover new skills and integrate
4. **Multi-Tenant**: Support multiple organizations
5. **Real-Time Streaming**: Stream results as skills complete
6. **Skill Marketplace**: Third-party skill integration
7. **A/B Testing**: Test different skill chains for optimization
8. **Skill Versioning**: Version control for skill updates
