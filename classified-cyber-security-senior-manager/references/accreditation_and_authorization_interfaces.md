# Accreditation and authorization interfaces

## Table of contents

1. [Manager-level RMF/ATO lens](#manager-level-rmfato-lens)
2. [Authorization boundary](#authorization-boundary)
3. [Lifecycle milestones](#lifecycle-milestones)
4. [Inherited controls and dependencies](#inherited-controls-and-dependencies)
5. [Significant change and continuous monitoring](#significant-change-and-continuous-monitoring)
6. [Assessor and ISSO interfaces](#assessor-and-isso-interfaces)

## Manager-level RMF/ATO lens

At **senior manager** depth, focus on:

- **Authorization boundary** — what is in vs out of the package
- **Status** — authorized, interim, denied, or in progress
- **Top risks** — POA&M themes, not every control ID
- **Decisions** — risk acceptance, resources, schedule

Defer control-by-control assessment to ISSOs, assessors, and engineers—summarize impact for leadership.

## Authorization boundary

Document for each system or enclave:

| Element | Question |
|---|---|
| System name and mission | What business/mission outcome does it support? |
| Boundary diagram (reference) | Where is the authorization boundary drawn? |
| Data types | Classification per org policy; aggregation rules |
| Interconnections | Other systems, cross-domain, remote admin paths |
| Common controls | Inherited from org provider or parent system? |

**Significant change** candidates: new interconnection, major version, cloud shift, privileged path change, new data category.

## Lifecycle milestones

Typical phases (labels vary by organization):

| Phase | Manager deliverable |
|---|---|
| Categorize | Confirm impact level aligns with mission and data |
| Select | Control baseline agreed; tailoring documented at summary |
| Implement | POA&M burn-down; resource plan for gaps |
| Assess | Entry/exit criteria for assessment; open finding triage |
| Authorize | Decision brief for authorizing official |
| Monitor | ConMon metrics, recurring findings, reauth date |

Track **reauthorization date** and **interim authorization** conditions explicitly in status reports.

## Inherited controls and dependencies

| Type | Risk if weak |
|---|---|
| Identity provider | Account lifecycle gaps affect all systems |
| Enterprise logging | Cannot support incident or inspection evidence |
| Vulnerability management | Inherited scan coverage holes |
| Physical / personnel | Inherited PS controls out of date |

For each dependency: owner, last assessment date, open POA&M count, and escalation path.

## Significant change and continuous monitoring

**Significant change board (concept):**

1. Change description and mission impact
2. Security impact analysis summary (from ISSO/engineering)
3. Updated boundary or data flow if needed
4. Authorizing official notification if required
5. POA&M updates before production

**Continuous monitoring themes:** vulnerability scan cadence, configuration drift, privileged access review, contingency test dates.

## Assessor and ISSO interfaces

| Meeting | Manager prepares |
|---|---|
| Weekly ISSO sync | POA&M velocity, blockers, resource asks |
| Pre-assessment | Evidence plan; known gaps with dates |
| Assessment exit | Finding severity rollup; accept/mitigate plan |
| Authorizing official read-ahead | One-page decision memo |

Escalate **conflicting assessor positions** early—do not let findings accumulate without owner.
