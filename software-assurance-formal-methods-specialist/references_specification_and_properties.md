# Specification and properties

## Table of contents

1. [From requirements to properties](#from-requirements-to-properties)
2. [Property taxonomy](#property-taxonomy)
3. [Contracts and interfaces](#contracts-and-interfaces)
4. [Temporal and concurrent specs](#temporal-and-concurrent-specs)
5. [Traceability](#traceability)
6. [Quality criteria for specs](#quality-criteria-for-specs)

## From requirements to properties

| Requirement style | Verifiable form |
|---|---|
| "Shall not exceed 100 ms" | Bounded latency property or measured test + environment assumption |
| "Shall reject malformed input" | Precondition + defensive postcondition or parser invariant |
| "Shall fail safe on sensor loss" | Mode machine + invariant per mode |
| "Shall encrypt at rest" | Data-flow or configuration invariant + review evidence |

Each property gets:

- **ID** (e.g., `PROP-SEC-014`)
- **Linked requirements** (e.g., `SYS-REQ-3.2.1`)
- **Component scope**
- **Verification method** (prove, MC, test, review)
- **Status** (open / bounded / proved / waived)

## Property taxonomy

| Kind | Example | Typical verification |
|---|---|---|
| **Invariant** | Balance ≥ 0 always | Induction, MC, SPARK proof |
| **Pre/post (Hoare)** | If valid input then output in range | WP, Dafny, ACSL |
| **Algebraic** | decrypt(encrypt(x)) = x | Theorem proving |
| **Temporal safety** | Never enter state ERROR without alarm | LTL, TLA+ |
| **Temporal liveness** | Request eventually acknowledged | LTL (harder; often bounded) |
| **Noninterference** | Low observer cannot see high data | Security typing, specialized provers |
| **Refinement** | Impl refines spec | Simulation proofs |

Avoid mixing **safety** and **liveness** in one informal sentence—split properties.

## Contracts and interfaces

For component **A** calling **B**:

```
requires:  B_ready && input_valid(x)
ensures:   result_ok(r) ==> post(x, r)
assigns:   memory regions listed explicitly
```

**Assume-guarantee** at system level:

- **A guarantees** calls only when `B_ready`
- **B guarantees** postcondition if requires met

Interface changes trigger **contract diff** in traceability matrix.

### Memory and concurrency

Explicitly state:

- Aliasing rules
- Lock ordering (or absence of locks)
- Reentrancy and ISR boundaries (embedded: coordinate with `embedded-real-time-software-engineer`)

## Temporal and concurrent specs

| Pattern | Spec sketch |
|---|---|
| Mutual exclusion | □ ¬(in_cs_1 ∧ in_cs_2) |
| Request-grant | □ (req → ◇ grant) — note liveness assumptions |
| Bounded response | □ (req → ◇≤t grant) — often proved via model + timing assumption |
| Failover | □ (primary_fail → ◇ backup_active) |

Use **PlusCal / TLA+** for design-level concurrency; refine to code-level invariants for implementation proofs.

## Traceability

Minimum matrix columns:

| Req ID | Property ID | Design element | Verification | Artifact ID | Result | Version |

Bidirectional rules:

- No property without requirement (or documented **derived** rationale)
- No release with **open** properties on safety-critical path without waiver
- Requirement change triggers **impact column** update

Export formats: CSV, DOORS/Jama links, or markdown tables in evidence package.

## Quality criteria for specs

A property is **ready for verification** when:

- [ ] **Unambiguous** — one interpretation, measurable predicates
- [ ] **Scoped** — names module, mode, configuration
- [ ] **Checkable** — tool or test can evaluate pass/fail
- [ ] **Independent** — minimal overlap with other properties (or decomposition documented)
- [ ] **Environment explicit** — hardware, OS, compiler flags listed

Reject "the system shall be robust" — decompose via hazard or threat analysis first.
