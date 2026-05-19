---
name: technical-program-manager
description: |
  Guides technical program management—multi-team initiatives with dependencies, milestones, RAID
  tracking, launch readiness, stakeholder status, and cross-functional coordination across
  engineering, product, and infrastructure (not application code or BRDs).
  Use when running a technical program, dependency maps, milestones, exec status, or unblocking
  cross-team delivery—not for requirements (business-analyst), rollout (deployment-strategist),
  CI/CD (devops), data roadmaps (data-manager), or single-team delivery (fullstack-software-engineer).
  Incidents: incident-management-engineer. Architecture: senior-system-architecture. Strategy:
  business-consultant. Comms: communication-lead. DC site build: data-center-design-execution-lead.
  DC portfolio: data-center-portfolio-planning-execution-lead. M&A/financing deal execution and
  closing matrix: transaction-manager. Exec/VIP and community customer escalations:
  community-executive-escalations-program-manager. CVD/disclosure:
  technical-program-manager-security-cvd.
---

# Technical Program Manager

## When to Use

- Coordinate a multi-team technical initiative with shared milestones
- Map dependencies, critical path, and integration points
- Maintain RAID log (risks, actions, issues, decisions)
- Run launch readiness or go/no-go reviews
- Produce weekly program status for leadership or steering committee
- Resolve cross-team blockers without owning the technical design

## When NOT to Use

- Write BRDs, user stories, or process maps → `business-analyst`
- Choose canary vs blue-green or write cutover runbooks → `deployment-strategist`
- Implement pipelines, GitOps, or on-call → `devops`
- Own data platform roadmap or data governance → `data-manager`
- Author service RFCs or code → `senior-software-engineer`, `fullstack-software-engineer`
- Platform product roadmap for IDP → `platform-engineer`
- Architecture decisions, ADRs, design review → `senior-system-architecture`
- Strategy, business case, operating model → `business-consultant`

## Related skills

| Need | Skill |
|---|---|
| Release strategy and rollback design | `deployment-strategist` |
| Pipeline and environment operations | `devops` |
| Requirements and business cases | `business-analyst` |
| UX scope and design handoff | `product-designer` |
| Engineering design and RFCs | `senior-software-engineer` |
| Data program roadmaps | `data-manager` |
| Security/compliance program gates | `compliance-engineer`, `cybersecurity` |
| System architecture and ADRs | `senior-system-architecture` |
| Strategy and business case | `business-consultant` |
| Incident ops: SEV, on-call, postmortems | `incident-management-engineer` |
| Board resolutions, entity, corporate closing | `corporate-counsel` |
| Launch and stakeholder messaging | `communication-lead` |
| Exec/VIP and community customer escalations | `community-executive-escalations-program-manager` |
| Data center design and facility execution | `data-center-design-execution-lead` |
| Multi-site DC portfolio planning and steering | `data-center-portfolio-planning-execution-lead` |
| M&A diligence, signing, closing coordination | `transaction-manager` |
| Coordinated vulnerability disclosure program | `technical-program-manager-security-cvd` |

## Core Workflows

### 1. Program charter

Define before execution:

- Objective and measurable outcomes (not output lists)
- Scope: teams, systems, in/out
- Timeline: phases, hard dates, external dependencies
- Roles: DRI per workstream, escalation path
- Success metrics and definition of done

**See `references/program_charter.md` for charter template.**

### 2. Work breakdown and dependencies

1. Decompose into workstreams (each with one DRI)
2. List deliverables per workstream with dates
3. Build dependency graph (finish-to-start; flag circular deps)
4. Identify critical path and buffer on that path only
5. Mark integration milestones (API freeze, env parity, dress rehearsal)

**See `references/dependency_risk.md` for dependency types and RAID format.**

### 3. Operating rhythm

| Cadence | Audience | Purpose |
|---|---|---|
| Weekly | Workstream DRIs | Blockers, date slips, dependency asks |
| Biweekly | Sponsors / leads | Scope, risk, decision needs |
| Pre-launch | Launch council | Readiness checklist |

- One source of truth for status (doc or tracker—not duplicate spreadsheets)
- Decisions logged with owner and date; no re-litigating closed calls

**See `references/status_reporting.md` for status template.**

### 4. Risk and issue management

- **Risk**: may happen → mitigation + trigger
- **Issue**: happened → owner + ETA + comms plan
- Escalate when: critical path slip > agreed threshold, scope creep without sponsor, unresolved cross-team conflict

**See `references/dependency_risk.md` for RAID columns.**

### 5. Stakeholder communication

- Status: RAG per workstream, changes since last week, asks
- No technical deep dives in exec updates—link appendix
- Align messaging before external comms (customers, support, legal)

**See `references/stakeholder_comms.md` for audience-specific formats.**

### 6. Launch readiness

Gate checklist before production:

- [ ] All critical-path items complete or explicitly waived by sponsor
- [ ] Rollback/runbook owned (`deployment-strategist` + `devops`)
- [ ] Monitoring and on-call briefed
- [ ] Support/docs updated
- [ ] Go/no-go with named approvers

**See `references/launch_readiness.md` for full checklist.**

## When to load references

- **Charter and phases** → `references/program_charter.md`
- **Dependencies and RAID** → `references/dependency_risk.md`
- **Status and steering** → `references/status_reporting.md`
- **Exec and sponsor comms** → `references/stakeholder_comms.md`
- **Go/no-go** → `references/launch_readiness.md`
