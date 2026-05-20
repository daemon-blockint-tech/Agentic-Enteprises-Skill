# Software assurance scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [Assurance vs testing](#assurance-vs-testing)
3. [Evidence types](#evidence-types)
4. [Lifecycle placement](#lifecycle-placement)
5. [Deliverables](#deliverables)

## Role boundary

| This skill | Partner skill |
|---|---|
| Assurance cases, claims, formal verification planning | `senior-software-engineer` — implementation and conventional tests |
| Property specs, proof obligations, model checking | `build-validator` — pre-execution design review without claim structure |
| Traceability and verification evidence packages | `compliance-engineer` — audit control automation |
| GRC program and auditor coordination | `compliance-specialist` |
| Offensive validation of running systems | `penetration-tester` |
| Criticality tiering and release governance | `mission-critical` |

**Do not** replace safety engineers for hazard identification, certifying authorities for approval, or lawyers for regulatory interpretation.

## Assurance vs testing

| Dimension | Testing (typical QA) | Software assurance |
|---|---|---|
| Question | Does behavior match examples under sampled inputs? | Is there a **credible argument** that critical claims hold? |
| Coverage | Code paths, requirements samples | Claims, assumptions, and **evidence chains** |
| Failure signal | Test fail | Broken proof, counterexample, traceability gap, invalid assumption |
| Artifact | Test report | Assurance case + linked verification results |
| When sufficient | Lower criticality, well-understood domains | SIL/ASIL/DAL, high-consequence security, certification paths |

Testing is often **evidence** inside an assurance case—not the whole case.

## Evidence types

| Type | Examples | Strengths | Limits |
|---|---|---|---|
| **Review** | Design review, code inspection, checklist | Fast, catches context errors | Not exhaustive |
| **Analysis** | Static analysis, taint, abstract interpretation | Scales to large code | May false-positive; may need tuning |
| **Formal verification** | Model checking, theorem proving, SMT | Strong for properties | Cost, expertise, environment assumptions |
| **Test** | Unit, integration, HIL, fuzz (bounded) | Executable reality | Incomplete without argument |
| **Field / ops** | Incident data, monitoring, fault logs | Ground truth in deployment | Lagging; privacy constraints |

Tag each evidence item with: **claim supported**, **tool/version**, **configuration**, **date**, **reviewer**.

## Lifecycle placement

| Phase | Assurance activities |
|---|---|
| Requirements | Derive verifiable claims; assign trace IDs |
| Architecture | Identify trust boundaries; allocate verification depth |
| Design | Properties per component; assumption register |
| Implementation | Proof obligations; CI gates; counterexample triage |
| Integration | Compositional arguments; interface contracts |
| Release | Evidence package completeness check |
| Change | Impact analysis on claims; regression of proofs/tests |

## Deliverables

Minimum set for a non-trivial assurance effort:

1. **Claim register** — top-level and derived claims with owners
2. **Assurance case outline** — GSN or equivalent structure
3. **Traceability matrix** — req ↔ property ↔ verification ↔ result
4. **Assumption register** — environment, hardware, tools, compilers
5. **Verification plan** — techniques, schedule, pass criteria
6. **Evidence index** — pointers to artifacts (not copies of entire tool dumps in the case itself)

Hand off implementation-only test suites to `senior-software-engineer` when no claim linkage is required.
