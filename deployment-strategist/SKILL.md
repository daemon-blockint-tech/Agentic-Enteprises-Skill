---
name: deployment-strategist
description: |
  Guides deployment and release strategy—choosing rollout patterns (rolling, blue-green, canary,
  feature flags), environment topology, promotion paths, blast-radius control, rollback design,
  change windows, and cross-team rollout plans for web, API, data, and ML workloads.
  Use when planning a production release, comparing deployment approaches, writing a rollout or
  cutover plan, designing multi-region or zero-downtime migrations, coordinating schema changes with
  deploys, or preparing executive/stakeholder release briefs (for launch messaging and customer
  comms copy, use communication-lead)—not for multi-team program tracking
  (technical-program-manager), implementing CI YAML (devops),
  Terraform/VPC design (infrastructure-engineer), security scan gates (devsecops), or upfront
  multi-service architecture and ADRs (senior-system-architecture). For Helm/Kustomize apply,
  cluster upgrades, and in-cluster rollout status, use cluster-deployment-engineer.
---

# Deployment Strategist

## When to Use

- Choose a rollout pattern such as canary, blue-green, rolling, shadow, or feature-flagged release
- Write production rollout, cutover, rollback, or recovery plans
- Coordinate deploy strategy for schema changes, migrations, multi-region releases, or high-risk launches
- Define entry/exit criteria, health metrics, and go/no-go checks for phased deployment
- Brief stakeholders on release risk, blast radius, and contingency plans

## When NOT to Use

- Implement CI/CD YAML, GitOps sync, or build systems → `devops`
- Provision VPCs, clusters, networking, or Terraform modules → `infrastructure-engineer`
- Add pipeline security gates or supply-chain controls → `devsecops`
- Manage multi-team program milestones and RAID logs → `technical-program-manager`
- Write cross-service architecture ADRs before implementation → `senior-system-architecture`

## Related skills

| Need | Skill |
|---|---|
| Pipeline implementation, GitOps, on-call | `devops` |
| Cloud networking, K8s clusters, IaC | `infrastructure-engineer` |
| Release gates, canary metrics for AI products | `ai-lead-ops` |
| Secure pipeline and supply chain | `devsecops` |
| App feature design and migrations in code | `senior-fullstack-developer` |
| Cross-team milestones, RAID, launch council | `technical-program-manager` |
| Architecture review before major migration | `senior-system-architecture` |
| Launch and customer messaging | `communication-lead` |
| K8s deploy execution and cluster ops | `cluster-deployment-engineer` |

## Core Workflows

### 1. Strategy selection

**Decision inputs:**

| Factor | Question |
|---|---|
| Blast radius | How many users affected if deploy fails? |
| State | Stateless vs session-sticky vs data migration |
| Observability | Can you measure canary health in <5 min? |
| Rollback speed | RTO target (seconds vs hours) |
| Compliance | Change freeze, audit trail, approval depth |

**Default recommendations:**

| Profile | Strategy |
|---|---|
| Stateless API, good metrics | Canary or rolling + feature flags |
| Major version, schema change | Blue-green or parallel stack + phased traffic |
| Mobile / app store | Phased rollout by % users; no instant rollback |
| ML model + prompt | Shadow → canary → full; version pins |
| Data warehouse | Expand-contract migrations; backfill before cutover |

**See `references/strategy_selection.md` for decision tree and trade-off matrix.**

### 2. Rollout plan document

Produce a plan containing:

1. **Objective** — what changes, for whom, by when
2. **Scope** — services, regions, tenants, feature flags
3. **Phases** — dev → staging → prod canary → prod 100%
4. **Entry/exit criteria** per phase (metrics, tests, approvals)
5. **Rollback** — trigger conditions, owner, steps, data implications
6. **Comms** — internal channels, customer status page if needed
7. **Schedule** — timezone-aware; avoid peak and freeze windows

**See `references/rollout_planning.md` for template and stakeholder RACI.**

### 3. Environment and promotion design

- Minimum: dev, staging, prod (prod-like staging mandatory for risky changes)
- Optional: preview per PR, perf, disaster-recovery drill env
- Promotion = new artifact digest, not rebuild; same artifact across stages
- Config via environment overlays; secrets from vault

**See `references/environments_promotion.md` for topology patterns and config rules.**

### 4. Database and dependency coordination

**Expand-contract pattern for schema:**

1. Expand: deploy code tolerant of old and new schema
2. Migrate data
3. Contract: remove old paths in later deploy

Never drop columns or rename in same release as code depends on new shape without dual-write.

**See `references/strategy_selection.md` for coupled release patterns.**

### 5. Rollback and recovery

| Rollback type | When |
|---|---|
| Fast | Redeploy previous artifact digest; flip traffic |
| Config | Revert feature flag or config map |
| Data | Restore backup / run down migration (slow, risky) |

Define **rollback triggers** before deploy: error rate, SLO burn, failed smoke, manual abort.

**See `references/rollback_recovery.md` for playbooks and drill cadence.**

### 6. Risk, compliance, and sign-off

- Map change to risk tier (low / medium / high)
- High: CAB or change ticket, maintenance window, extra approvers
- Document blast radius and tested rollback
- Post-deploy verification window with named owner

**See `references/risk_compliance.md` for tier definitions and evidence list.**

## When to load references

- **Choose strategy** → `references/strategy_selection.md`
- **Rollout plan template** → `references/rollout_planning.md`
- **Environments** → `references/environments_promotion.md`
- **Rollback** → `references/rollback_recovery.md`
- **Change control** → `references/risk_compliance.md`
