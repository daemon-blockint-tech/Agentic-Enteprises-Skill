# Lifecycle phases and gates

## Table of contents

1. [Phase model overview](#phase-model-overview)
2. [Phase definitions](#phase-definitions)
3. [Gate structure](#gate-structure)
4. [Gate criteria by phase](#gate-criteria-by-phase)
5. [Waivers and emergency progression](#waivers-and-emergency-progression)
6. [Mapping to delivery methods](#mapping-to-delivery-methods)
7. [Gate packet checklist](#gate-packet-checklist)

## Phase model overview

Standard **eight-phase** model for extreme lifecycle (adapt names to org glossary):

```
Concept → Design → Build → Verify → Deploy → Operate → Sustain → Dispose
```

Each transition crosses a **gate** with defined entry/exit criteria and evidence.

```mermaid
flowchart LR
  C[Concept] --> D[Design]
  D --> B[Build]
  B --> V[Verify]
  V --> P[Deploy]
  P --> O[Operate]
  O --> S[Sustain]
  S --> X[Dispose]
```

## Phase definitions

| Phase | Purpose | Primary outputs |
|---|---|---|
| **Concept** | Need, feasibility, initial risk, lifecycle commitment | Concept brief, initial impact/tier hook, lifecycle charter draft |
| **Design** | Architecture, interfaces, security/privacy design, verification strategy | Design baseline, threat model pointer, traceability seed |
| **Build** | Implement to approved design baseline | Build records, SBOM/components, code/config under CM |
| **Verify** | Test, assess, and prove readiness against criteria | Test reports, assessment summaries, traceability closure plan |
| **Deploy** | Promote approved baseline to production | Deployment record, rollback plan, ops handoff |
| **Operate** | Run within baseline; detect drift | Runbooks, monitoring, incident hooks |
| **Sustain** | Long-term support, refresh, obsolescence | Sustainment reviews, patch posture, EOL plan |
| **Dispose** | Retire, decommission, disposition data | Shutdown evidence, destruction/archival certificates |

## Gate structure

Every gate documents:

| Field | Description |
|---|---|
| **Gate ID** | e.g., G3 Build→Verify |
| **Entry criteria** | Preconditions to start gate review |
| **Exit criteria** | Conditions to leave phase |
| **Evidence list** | Artifacts with location, version, approver |
| **Reviewers** | Independent roles where required |
| **Decision** | Pass / conditional pass / fail |
| **Conditions** | Remediation items with owners and dates |
| **Waiver** | If used: authority, scope, expiry |

**Independence:** for high assurance, **builder ≠ sole verifier**; separation documented in gate packet.

## Gate criteria by phase

### Concept → Design (Gate 1)

**Exit criteria (examples):**

- Approved concept brief and stakeholder sign-off
- Initial criticality/tier alignment (`mission-critical` if applicable)
- Lifecycle charter draft and sponsor assigned
- Top risks and regulatory/classified interfaces identified (generic)

### Design → Build (Gate 2)

- Design baseline frozen under configuration management
- Verification and validation plan linked to requirements
- Security/privacy design review complete (interface to assurance)
- Traceability matrix populated for design elements

### Build → Verify (Gate 3)

- Build matches approved design baseline (or approved deltas recorded)
- Component inventory / SBOM available where required
- Static analysis and required DevSecOps gates passed (`devsecops` interface)
- Known defects logged with disposition

### Verify → Deploy (Gate 4)

- Test evidence against acceptance criteria
- Independent assessment or review complete (scope-appropriate)
- Residual risk accepted by authority
- Deployment and rollback procedures approved
- Operations readiness (monitoring, runbooks, on-call)

### Deploy → Operate (Gate 5)

- Production baseline established and manifest archived
- Authorization/ATO **interfaces** satisfied per program (do not author ISSO package here)
- Handoff to operations complete

### Operate → Sustain (Gate 6)

- Stable operations period or trigger into formal sustainment (org-defined)
- Sustainment plan active: support contracts, spares, patch cadence

### Sustain → Dispose (Gate 7)

- EOL decision recorded; no unmitigated dependents
- Decommissioning plan approved → `change_baseline_and_retirement.md`

## Waivers and emergency progression

| Situation | Requirements |
|---|---|
| **Waiver** | Written scope, risk acceptance, compensating controls, expiry date |
| **Emergency deploy** | Post-facto baseline reconciliation within defined SLA |
| **Pilot / limited production** | Explicit boundary; not a silent bypass of Verify gate |

Document waivers in the **gate register**; never informal chat approval for high assurance.

## Mapping to delivery methods

| Delivery style | How phases appear |
|---|---|
| **Waterfall** | One gate per phase boundary |
| **Incremental** | Repeated mini-cycles Build→Verify→Deploy within sustainment |
| **Agile** | Sprints deliver **increments**; gate packets aggregate sprint evidence at baseline promotion |

**Rule:** agile cadence does not eliminate **baseline promotion** or **verify** before production.

## Gate packet checklist

Before scheduling a gate review, confirm:

- [ ] Correct gate ID and phase transition
- [ ] All exit criteria mapped to evidence items
- [ ] Traceability gaps listed with owners
- [ ] Open risks with acceptance or mitigation
- [ ] Baseline version identifiers (config, software, infra-as-code)
- [ ] Approver roster and independence noted
- [ ] Conditions from prior gate closed or explicitly carried

**Output:** signed gate record stored with retention per `traceability_and_evidence.md`.
