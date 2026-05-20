# Verification integration

## Table of contents

1. [CI and pipeline placement](#ci-and-pipeline-placement)
2. [Proof obligations and counterexamples](#proof-obligations-and-counterexamples)
3. [Release gates](#release-gates)
4. [Evidence packages](#evidence-packages)
5. [Regression and change impact](#regression-and-change-impact)
6. [Tool qualification note](#tool-qualification-note)

## CI and pipeline placement

| Stage | Activities | Fail policy |
|---|---|---|
| **PR / commit** | Fast static checks, lint specs, smoke MC/BMC (seconds–minutes) | Block merge on regression |
| **Nightly** | Full model checking, long proofs, fuzz with oracles | Ticket + owner; may not block if tier allows |
| **Pre-release** | Evidence package completeness, assumption review | Block release |
| **Post-release** | Monitor runtime verification alerts | Incident path |

Coordinate with `devsecops` for SSDF-aligned pipeline evidence; this skill defines **what** must pass, not how to configure Jenkins/GitHub Actions alone.

### Artifact retention

Store: tool version, commit SHA, config flags, seed, proof trace or counterexample file, human-readable summary.

Retention period aligns with certification or customer contract—default **≥ life of supported release**.

## Proof obligations and counterexamples

| Outcome | Action |
|---|---|
| **Proved** | Archive log; link to claim in assurance case |
| **Timeout / unknown** | Record bounds; schedule manual proof or weaken property |
| **Counterexample** | Minimize trace; file defect or refine spec/assumption |
| **False positive (tool)** | Document analyzer limitation; alternate evidence |

**Proof obligation register**:

| PO ID | Source | Location | Owner | Status | Linked claim |

Treat PO closure like defect backlog—visible in sprint/release reviews.

## Release gates

Example **tiered** gates (adjust to program):

| Gate | Criteria |
|---|---|
| G0 | Traceability matrix updated for this release |
| G1 | All **safety/security** properties: proved, tested, or waived with approver |
| G2 | No open counterexamples on tagged commit |
| G3 | Assumption register reviewed; expired assumptions closed |
| G4 | Independent review of assurance case delta since last release |

`build-validator` may run broader design review; **G1–G4** are claim-specific.

### Waivers

Waivers require: claim ID, reason, compensating evidence, approver role, expiry date, affected versions.

## Evidence packages

Folder structure (illustrative):

```
evidence/
  assurance_case/     # GSN export or PDF
  traceability/       # matrix CSV
  proofs/             # logs, certificates
  tests/              # linked suites IDs
  reviews/            # sign-off records
  assumptions/        # register snapshot
  tool_versions.txt
```

**Index file** lists each artifact with SHA-256 for integrity.

Deliver to certifiers, customers, or internal audit—not a dump of every intermediate solver log unless required.

## Regression and change impact

On each change affecting verified artifacts:

1. **Impact analysis** — which claims/properties touched?
2. **Re-run** minimal verification set (incremental proofs)
3. **Update** assurance case if decomposition or assumptions shift
4. **Version** evidence index

Map to hazard analysis when change is safety-related (FMEA row update reference only).

## Tool qualification note

For DO-178C / DO-330 and similar, tools may need **qualification kits** or justification as non-qualified with additional independence.

This skill does **not** reproduce qualification procedures—flag need early and involve process owners.

Partner: `compliance-engineer` for storing qualification records in audit systems.
