---
name: fullstack-software-engineer
description: |
  Guides full-stack software engineering—end-to-end product features across web frontends
  (React/Next.js or similar), backend APIs (Node/TypeScript or Python), databases, auth, testing,
  and production debugging for maintainable application code.
  Use when building or fixing user-facing features, designing REST/GraphQL/tRPC contracts,
  implementing forms and API routes, writing migrations, adding tests, or reviewing application
  PRs—not for CI/CD platforms (devops), cloud VPC/IaC (infrastructure-engineer), data warehouse
  modeling (data-warehouse-engineer), LLM/RAG features (ai-engineer), or org security/compliance
  programs (cybersecurity, compliance-engineer). For browser web-app patterns (sessions, CSRF, CORS,
  CSP, SSR/SPA routing), use web-application-developer. For senior-level system design and
  mentorship-style review, also use senior-fullstack-developer. UI-only from design: ui-software-engineer.
  Ticket repro without code: support-engineer.
---

# Full Stack Software Engineer

## When to Use

- Implement a vertical feature (UI + API + persistence)
- Design or change an API consumed by the frontend
- Fix bugs spanning client and server
- Add auth, validation, pagination, or file upload flows
- Write or extend unit, integration, and critical-path e2e tests

## When NOT to Use

- Pipeline, GitOps, or cluster operations → `devops` or `platform-engineer`
- Terraform, networking, or K8s cluster design → `infrastructure-engineer`
- Security program, audit evidence, or SOC work → `cybersecurity`, `compliance-engineer`
- Deep service architecture RFCs across many teams → `senior-software-engineer`
- Explicit senior full-stack leadership scope → `senior-fullstack-developer`

## Related skills

| Need | Skill |
|---|---|
| Senior slice delivery and deeper review bar | `senior-fullstack-developer` |
| RFCs and cross-service design | `senior-software-engineer` |
| Deploy and observability plumbing | `devops` |
| Requirements and acceptance criteria | `business-analyst` |
| User-facing docs | `tech-writer-researcher` |
| Front-end-only architecture and a11y | `senior-frontend-software-engineer` |
| Web sessions, CSRF, CORS, hybrid rendering | `web-application-developer` |
| Customer ticket repro and escalation | `support-engineer` |

## Core Workflows

### 1. Vertical feature delivery

1. Confirm acceptance criteria and edge cases (empty, error, permissions)
2. Define API contract and UI states
3. Implement server: validation, authz, persistence, migrations
4. Implement client against typed contract
5. Test: unit (logic), integration (API), e2e (happy path)
6. Add logging/metrics on new paths; feature flag if risky

**See `references/feature_delivery.md` for checklist.**

### 2. API and database

| Concern | Default |
|---|---|
| Validation | Schema at boundary (Zod, Pydantic) |
| Auth | Session or JWT; check authz per resource |
| Queries | Avoid N+1; index for access patterns |
| Mutations | Transactions where needed; idempotency keys for payments-like flows |
| Errors | Stable codes; no internal details to clients |

**See `references/api_and_database.md` for pagination and migrations.**

### 3. Frontend integration

- Match loading/error/empty states to design
- Prefer server fetch for read-heavy pages when using Next.js App Router
- Client components only for interactivity
- Accessible forms (labels, focus, keyboard)

**See `references/frontend_integration.md` for forms and caching.**

### 4. Testing and PR hygiene

- Lint and typecheck clean
- Tests cover changed behavior, not only happy path
- No secrets in repo; env via configuration
- Small PRs; describe rollout and rollback

**See `references/testing_debugging.md` for test pyramid.**

### 5. Production debugging

1. Reproduce with correlation ID or request ID
2. Check deploys, flags, and recent config changes
3. Trace: logs → metrics → DB slow queries
4. Fix with regression test; hotfix or rollback per severity

**See `references/testing_debugging.md` for common failures.**

## When to load references

- **Feature flow** → `references/feature_delivery.md`
- **APIs and DB** → `references/api_and_database.md`
- **UI integration** → `references/frontend_integration.md`
- **Tests and prod issues** → `references/testing_debugging.md`
