---
name: senior-software-engineer
description: |
  Guides senior software engineering across languages and stacks—system and service design, RFCs,
  code review, refactoring, reliability patterns, testing strategy, performance analysis, technical
  decomposition, and engineering leadership on delivery teams.
  Use when designing services or modules, writing technical specs, reviewing PRs for architecture and
  correctness, improving legacy code, choosing trade-offs (coupling, consistency, latency), estimating
  complex work, or mentoring engineers—not for stack-specific full-stack UI delivery (senior-fullstack-developer),
  deployment rollout strategy (deployment-strategist), infrastructure/IaC (infrastructure-engineer),
  org-wide security programs (cybersecurity), or cross-system ADRs and architecture review
  (senior-system-architecture).
---

# Senior Software Engineer

## When to Use

- Design services, modules, APIs, or technical approaches across general software stacks
- Write RFCs, technical specs, decomposition plans, or engineering trade-off analysis
- Review PRs for correctness, maintainability, reliability, operability, and test coverage
- Refactor legacy code safely while preserving behavior
- Mentor engineers on implementation quality, estimates, and delivery risks

## When NOT to Use

- Build stack-specific full-stack product features end to end → `senior-fullstack-developer`, `fullstack-software-engineer`
- Focus only on React/UI architecture and accessibility → `senior-frontend-software-engineer`
- Choose rollout plans, canaries, or cutover strategy → `deployment-strategist`
- Provision infrastructure, Kubernetes, or IaC → `infrastructure-engineer`
- Make enterprise-wide architecture decisions or ADR review gates → `senior-system-architecture`

## Related skills

| Need | Skill |
|---|---|
| React/Next + vertical feature delivery | `fullstack-software-engineer`, `senior-fullstack-developer` |
| Senior front-end architecture and a11y | `senior-frontend-software-engineer` |
| Rollout plans and release strategy | `deployment-strategist` |
| CI/CD implementation | `devops` |
| Cloud/K8s/Terraform | `infrastructure-engineer` |
| Requirements and BRDs | `business-analyst` |
| AI/LLM product features | `ai-engineer` |
| Cross-service ADRs, NFRs, architecture review | `senior-system-architecture` |

## Core Workflows

### 1. Technical design (RFC)

1. State problem, constraints, and non-goals
2. List options with trade-offs (at least two alternatives)
3. Recommend one; define interfaces and data contracts
4. Identify risks: scale, failure modes, migration, operability
5. Define success metrics and rollout approach (link `deployment-strategist` if needed)

**Deliverable:** short RFC or design doc with diagram (C4 or sequence for critical paths).

**See `references/system_design.md` for templates, boundaries, and consistency patterns.**

### 2. Implementation planning

Break work into:

| Slice | Outcome |
|---|---|
| Foundation | Types, interfaces, skeleton with tests |
| Core behavior | Happy path end-to-end |
| Edge cases | Errors, idempotency, authz |
| Operability | Logs, metrics, runbooks |
| Cleanup | Remove flags, deprecate old path |

Estimate each slice; call out unknowns and spikes.

**See `references/rfc_technical_leadership.md` for estimation and decomposition.**

### 3. Code review (senior bar)

Review order: **correctness → design → operability → style**.

| Check | Question |
|---|---|
| Correctness | Edge cases, races, error handling |
| API design | Clear contracts, backward compatibility |
| Security | Authz, injection, secrets |
| Tests | Meaningful cases, not snapshot noise |
| Operability | Logs, metrics, configurable limits |
| Maintainability | Coupling, naming, duplication |

Leave actionable comments; distinguish blocker vs nit.

**See `references/code_review.md` for rubric and comment patterns.**

### 4. Refactoring and quality

**When to refactor:** before adding feature in tangled module, or when change touches same area third time.

**Approach:**

1. Add characterization tests around behavior
2. Small commits: extract → rename → move
3. Preserve external behavior; use feature flags for risky swaps
4. Delete dead code in same PR when safe

**See `references/refactoring_quality.md` for smells and safe sequences.**

### 5. Reliability and performance

**Reliability defaults:**

- Timeouts on all outbound calls
- Retries with jitter only for idempotent ops
- Circuit breakers at integration boundaries
- Graceful degradation with clear user messaging

**Performance:**

1. Measure (profiler, traces, query plans)—no premature optimization
2. Fix N+1, unnecessary allocation, hot loops
3. Cache with explicit TTL and invalidation story

**See `references/reliability_patterns.md` for distributed systems primitives.**

### 6. Technical leadership

- Unblock others: pair on hard bugs, clarify design decisions in writing
- Raise risks early; propose phased delivery
- Document decisions in ADR when reversal is costly
- Align with product on scope vs quality trade-offs

**See `references/rfc_technical_leadership.md` for ADRs and mentoring prompts.**

## When to load references

- **Service design and RFCs** → `references/system_design.md`
- **PR review** → `references/code_review.md`
- **Refactoring** → `references/refactoring_quality.md`
- **Reliability and performance** → `references/reliability_patterns.md`
- **Estimation, ADRs, mentoring** → `references/rfc_technical_leadership.md`
