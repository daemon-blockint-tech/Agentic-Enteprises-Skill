# Assurance cases and claims

## Table of contents

1. [Claims and goals](#claims-and-goals)
2. [GSN structure](#gsn-structure)
3. [CAE and alternatives](#cae-and-alternatives)
4. [Strategies and decomposition](#strategies-and-decomposition)
5. [Stakeholders and reviews](#stakeholders-and-reviews)
6. [Common pitfalls](#common-pitfalls)

## Claims and goals

A **claim** is a statement stakeholders must believe—for example:

- "No single software fault causes loss of braking authority."
- "Secret keys are never written to persistent logs."
- "Parser rejects all inputs longer than N before allocation."

Distinguish:

| Term | Meaning |
|---|---|
| **Goal** | Top-level assurance objective (often from hazard or threat analysis) |
| **Claim** | Specific proposition supported by evidence |
| **Assumption** | Condition taken as true without proof in this case (must be explicit) |
| **Context** | Scope limitation (configuration, mode, version) |

Claims must be **falsifiable** and **verifiable in principle**—avoid vague "secure" or "safe" without criteria.

## GSN structure

Goal Structuring Notation (GSN) links elements:

| Node | Role |
|---|---|
| **Goal (G)** | Claim to be supported |
| **Strategy (S)** | How the goal is decomposed (e.g., by subsystem, by failure mode) |
| **Context (C)** | Scope or operating conditions |
| **Assumption (A)** | External truth; requires separate validation |
| **Justification (J)** | Rationale not backed by direct evidence (use sparingly) |
| **Solution (Sn)** | Reference to evidence (report ID, test suite, proof artifact) |

**Supported-by** relations connect goals to strategies or solutions; **in-context-of** attaches context/assumption.

### Minimal GSN pattern (text)

```
G1: System meets integrity property P
  S1: Argue over components C1..Cn
    G1.1: C1 meets P1  --supported-by--> Sn: Proof report PR-12
    G1.2: C2 meets P2  --supported-by--> Sn: Test suite TS-4 + review RV-2
  A1: OS scheduler provides bounded priority inversion  --validated-by--> Analysis AX-1
  C1: Deployment profile "production-hardened" only
```

## CAE and alternatives

| Notation | When to use |
|---|---|
| **GSN** | Safety-critical, aerospace, rail; regulator familiarity |
| **CAE (Claims-Argument-Evidence)** | Security cases, Common Criteria-style work |
| **STPA-style control structure** | Systems with complex control loops (often paired with safety engineering) |

For **security**, map claims to **threats** and **controls**; evidence may include pentest reports (`penetration-tester`) as **Solution** nodes, not as the entire argument.

## Strategies and decomposition

Common strategies:

| Strategy | Decomposition |
|---|---|
| **Divide and conquer** | Subsystem claims compose to system claim |
| **Defense in depth** | Multiple independent lines for same goal |
| **Failure mode** | One goal per hazardous failure |
| **Lifecycle** | Goals per phase (boot, run, shutdown, update) |

**Composition rules** must be explicit: interface contracts, fault containment, and error propagation assumptions belong in **Context** or **Assumption** nodes.

## Stakeholders and reviews

| Stakeholder | Interest |
|---|---|
| Engineering | Feasible properties, toolchains, CI cost |
| Safety / security engineering | Hazard and threat alignment |
| QA / test | Test evidence mapping |
| Independent V&V | Case structure, assumption scrutiny |
| Certification / customer | Readable top-level argument |

Review checklist:

- [ ] Every top goal has at least one strategy or solution
- [ ] No orphan evidence (solution not linked to a claim)
- [ ] Assumptions have owners and validation plans
- [ ] Context nodes match deployed configuration
- [ ] Waivers documented with approver and expiry

## Common pitfalls

1. **Solution-only case** — pile of test reports without decomposition strategy
2. **Circular assumptions** — goal A assumes B; goal B assumes A
3. **Stale evidence** — proof for v1.2, shipping v1.5 without impact analysis
4. **Over-claiming** — "formally verified" when only one lemma was proved
5. **Hidden environment** — proofs valid only with specific compiler flags not in production build
