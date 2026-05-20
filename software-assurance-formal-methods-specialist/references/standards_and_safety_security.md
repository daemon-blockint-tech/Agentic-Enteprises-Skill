# Standards and safety/security context

## Table of contents

1. [How to use this reference](#how-to-use-this-reference)
2. [DO-178C and DO-333](#do-178c-and-do-333)
3. [IEC 61508](#iec-61508)
4. [ISO 26262](#iso-26262)
5. [Common Criteria](#common-criteria)
6. [NIST SSDF](#nist-ssdf)
7. [Mapping assurance artifacts](#mapping-assurance-artifacts)

## How to use this reference

Provides **orientation only**—not a substitute for the standard, certifier guidance, or company QMS.

| You need | Action |
|---|---|
| Full control text | Obtain official standard; legal/compliance owns interpretation |
| Program scope | `compliance-specialist` or domain safety lead |
| Technical evidence automation | `compliance-engineer` |
| Operational tiering | `mission-critical`, `zero-tolerance-for-failure` |

## DO-178C and DO-333

**DO-178C** — software considerations in airborne systems and equipment certification.

| Concept | Assurance relevance |
|---|---|
| **DAL (A–E)** | Drives rigor of objectives and independence |
| **Requirements** | Traceable, verifiable, consistent |
| **Design** | Low-level requirements linked to code |
| **Verification** | Reviews, analysis, tests per DAL table |
| **Configuration management** | Baselines match evidence |
| **Quality assurance** | Process compliance records |

**DO-333** — formal methods supplement to DO-178C.

| Topic | Note |
|---|---|
| **Formal model** | May satisfy or supplement some verification objectives |
| **Property** | Must link to requirements |
| **Tool qualification** | DO-330 when tools reduce independence needs |
| **Soundness** | Document where proofs are incomplete or bounded |

Formal proofs rarely eliminate **all** structural coverage expectations at high DAL—plan hybrid evidence.

## IEC 61508

Functional safety of **E/E/PE** systems (general industry).

| Element | Mapping |
|---|---|
| **SIL 1–4** | Rigor of techniques (tables in Part 2/3) |
| **Safety lifecycle** | Assurance case aligns with safety plan phases |
| **SRS** | Source of claims |
| **V&V** | Formal methods listed as techniques with SIL-dependent recommendations |
| **Proof of competence** | Personnel evidence (process, not this skill) |

Pair with hazard studies (HAZOP, etc.) performed by safety engineering—this skill consumes **hazard IDs** as claim sources.

## ISO 26262

Road vehicles — functional safety.

| Concept | Mapping |
|---|---|
| **ASIL A–D** | Verification depth and metrics |
| **Safety goals** | Top assurance case goals |
| **Technical safety requirements** | Trace to software requirements |
| **SEooC** | Assumptions on integration context—explicit in case |
| **Freedom from interference** | Claims + analysis between elements |

Software unit design and integration testing remain required; formal methods support **refutation** of systematic design faults.

## Common Criteria

**CC** — IT security evaluation (EAL-oriented).

| Artifact | Role |
|---|---|
| **ST (Security Target)** | Claims about TOE |
| **SAR** | Security architecture rationale |
| **ADV_* / ALC_* / ATE_*** families | Development, lifecycle, tests—evidence classes |
| **Security case** | CAE-style argument for evaluators |

Formal verification may support **ATE** or design-level **ADV** objectives depending on assurance level and protection profile.

Partner: `information-security-engineer` for control implementation; this skill for **argument and proof** structure.

## NIST SSDF

**Secure Software Development Framework** (SP 800-218) — organizational practices, not product certification.

| Practice group | Formal methods touchpoint |
|---|---|
| Prepare the organization | Training, toolchain for verification |
| Protect the software | Integrity of proof artifacts in repo |
| Produce well-secured software | Property-based design, MC in CI |
| Respond to vulnerabilities | Counterexamples feed vuln management |

`devsecops` implements pipeline; map SSDF evidence to **verification_integration** artifacts.

## Mapping assurance artifacts

| Artifact | DO-178C-ish | 61508 / 26262 | CC | SSDF |
|---|---|---|---|---|
| Assurance case / GSN | Planning + verification narrative | Safety case input | Security case | Risk communication |
| Trace matrix | Req ↔ code ↔ tests | SRS trace | ST trace | PO.3 trace needs |
| Formal proof log | Analysis evidence | FM technique table | Design verification | Secure design evidence |
| Assumption register | Environment config | SEooC / integration | TOE boundary | Architecture assumptions |
| CI gate records | Process objective | Regression discipline | Lifecycle | PW.6/PV.7 |

When the user names a standard, **confirm target level** (DAL, SIL, ASIL, EAL) before recommending verification depth.
