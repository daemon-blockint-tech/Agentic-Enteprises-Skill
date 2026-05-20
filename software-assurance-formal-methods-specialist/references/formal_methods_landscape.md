# Formal methods landscape

## Table of contents

1. [Technique overview](#technique-overview)
2. [Model checking vs theorem proving](#model-checking-vs-theorem-proving)
3. [Abstraction and refinement](#abstraction-and-refinement)
4. [Bounded and incremental techniques](#bounded-and-incremental-techniques)
5. [Specification languages (concept level)](#specification-languages-concept-level)
6. [Tool classes](#tool-classes)
7. [Selection heuristic](#selection-heuristic)

## Technique overview

| Technique | What it establishes | Typical scale |
|---|---|---|
| **Model checking** | Property holds for all states of a finite (or bounded) model | Protocols, controllers, concurrent designs |
| **Theorem proving** | Property derived from axioms and definitions | Algorithms, crypto, kernels, compilers |
| **Abstract interpretation** | Sound over-approximation of behaviors | Large C/C++ codebases, taint, nullness |
| **SMT / bounded model checking (BMC)** | Property for bounded execution steps | C functions, LLVM bitcode slices |
| **Runtime verification** | Monitor spec at execution | Live enforcement, test oracles |
| **Type systems / refinement types** | Structural invariants by construction | Rust, SPARK, dependent types |

Formal methods **complement** testing; they do not remove the need for integration evidence on real hardware.

## Model checking vs theorem proving

| Criterion | Model checking | Theorem proving |
|---|---|---|
| **Automation** | High for finite models | Interactive; automation partial |
| **Counterexamples** | Often concrete traces | May need manual interpretation |
| **State explosion** | Primary limit | Less state enumeration; proof effort shifts |
| **Best for** | Concurrency, protocols, temporal properties | Complex invariants, mathematics, refinement chains |
| **Team skill** | Model abstraction, property writing | Logic, proof engineering, maintenance |

**Hybrid**: prove critical lemmas, model-check composed system, test on target.

## Abstraction and refinement

| Concept | Purpose |
|---|---|
| **Abstraction** | Hide detail to make verification tractable; must be **sound** for the property class |
| **Refinement** | Show implementation refines more abstract spec (data refinement, simulation) |
| **Compositional verification** | Verify components; glue with assume-guarantee contracts |

Document **abstraction gap**: what the proof model omits (timing, caches, DMA, interrupts) and why that is acceptable.

## Bounded and incremental techniques

| Technique | Use when |
|---|---|
| **BMC** | Need push-button on code slice; accept depth limit |
| **k-induction** | Strengthen inductive proofs for hardware/software loops |
| **Incremental model checking** | Design changes frequently; reuse previous results |
| **Proof caching / regression** | CI re-runs proofs on every commit |

Treat **bounded results** as explicit claims: "No violation within K steps" ≠ "never."

## Specification languages (concept level)

| Language / family | Typical use | Notes |
|---|---|---|
| **TLA+** | Distributed systems, concurrency, temporal properties | PlusCal for algorithms; TLC model checker |
| **Alloy** | Structural constraints, relational models | SAT-based; good for design exploration |
| **ACSL / Frama-C** | C code contracts, memory safety | WP, Eva, plugins; proof obligations |
| **SPARK (Ada)** | High-integrity embedded | No runtime overhead when proved |
| **Dafny / Verus / Lean** | Algorithmic correctness | Growing in systems research |
| **Property DSLs** | LTL/CTL in model checkers | Spin, nuXmv, CBMC hooks |

Match language to **team language** and **certification toolchain** constraints (DO-330 tool qualification context—see standards reference).

## Tool classes

| Class | Examples (illustrative) | Output |
|---|---|---|
| Explicit-state MC | Spin, PAT | Counterexample trace |
| Symbolic MC | nuXmv, Kind2 | Witness, proof obligation |
| SMT solvers | Z3, cvc5 | sat/unsat, model |
| Provers | Isabelle, Coq, Lean | Checked proof term |
| C analyzers | CBMC, Frama-C, Infer | Violations, coverage of properties |
| Protocol | ProVerif, Tamarin | Security properties |

Pin **tool name, version, options** in evidence index.

## Selection heuristic

1. **Property class** — safety (invariant), liveness (eventually), security (noninterference), data (bounds)
2. **Artifact** — design model vs source vs binary
3. **Criticality** — depth per `mission-critical` tiering
4. **Change rate** — prefer automation + CI if daily commits
5. **Qualification** — if cert path requires qualified tools, narrow choices early

If property is unclear, **do not** start proving—refine the claim in the assurance case first.
