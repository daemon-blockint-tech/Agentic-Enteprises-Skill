---
name: senior-fullstack-developer
description: |
  Guides senior full-stack delivery across TypeScript/React/Next.js frontends, Node or Python APIs,
  relational databases, authentication, testing, performance, and pragmatic system design for product features.
  Use when implementing end-to-end features, designing REST/GraphQL contracts, refactoring UI and backend,
  debugging production issues in app code, or reviewing PRs for maintainability—not for standard full-stack
  IC delivery without senior scope (fullstack-software-engineer), CI/CD platform work (devops), security
  program design (cybersecurity), ML modeling (data-scientist), or LLM prompt/agent design (ai-engineer,
  prompt-engineer).
---

# Senior Fullstack Developer

## When to Use

- Senior-owned vertical features with higher design bar
- PR review for authz, data layer, and frontend architecture
- Production debugging across app layers with mentorship-level guidance

## When NOT to Use

- Routine full-stack feature work at standard IC bar → `fullstack-software-engineer`
- Cross-team RFCs and service boundaries → `senior-software-engineer`
- Infrastructure or pipelines → `infrastructure-engineer`, `devops`

## Related skills

| Need | Skill |
|---|---|
| General full-stack IC delivery | `fullstack-software-engineer` |
| Pipelines, deploy, SLOs | `devops` |
| SAST, dependency, pipeline security | `devsecops` |
| Requirements and BRDs | `business-analyst` |
| RAG, agents, LLM APIs | `ai-engineer` |
| Docs and API reference publishing | `tech-writer-researcher` |
| RFCs, service design, senior code review | `senior-software-engineer` |
| Front-end-only senior work | `senior-frontend-software-engineer` |
| Web platform security and auth patterns | `web-application-developer` |

## Core Workflows

### 1. Feature delivery (vertical slice)

1. Clarify acceptance criteria and non-goals
2. Sketch API contract + UI states (loading, empty, error)
3. Implement backend with validation and authz checks first
4. Implement UI against contract; use typed client
5. Add tests: unit for logic, integration for API, e2e for critical path
6. Instrument logs/metrics for new endpoints
7. Ship behind flag if risky; document rollout and rollback

**See `references/feature_delivery.md` for slice checklist and PR template.**

### 2. API and data layer design

| Concern | Default |
|---|---|
| Style | REST with OpenAPI or tRPC for TS monoliths |
| Auth | Session or JWT; validate on every mutating route |
| Validation | Schema at boundary (Zod, Pydantic) |
| DB | Migrations versioned; indexes for query paths |
| Errors | Stable error codes; no stack traces to clients |

**See `references/api_data_patterns.md` for pagination, idempotency, and transaction patterns.**

### 3. Frontend architecture

- Prefer server components where data is read-heavy (Next.js App Router)
- Colocate state: server for fetch, client only for interaction
- Accessible components (labels, focus, contrast)
- Avoid premature abstraction; extract after second use

**See `references/frontend_patterns.md` for forms, caching, and performance.**

### 4. Quality and review

**PR review focus:** correctness, authz, input validation, N+1 queries, error paths, test coverage on changed lines.

**Before merge:** lint, typecheck, tests green; no secrets; migration plan if schema changed.

**See `references/testing_quality.md` for test pyramid and flaky test handling.**

### 5. Production debugging

1. Reproduce with correlation ID
2. Check recent deploys and feature flags
3. Trace logs → metrics → DB slow queries
4. Fix forward or rollback; add regression test

**See `references/debugging_ops.md` for common failure modes.**

## When to load references

- **End-to-end feature flow** → `references/feature_delivery.md`
- **APIs and databases** → `references/api_data_patterns.md`
- **React/Next UI** → `references/frontend_patterns.md`
- **Testing and review** → `references/testing_quality.md`
- **Prod debugging** → `references/debugging_ops.md`
