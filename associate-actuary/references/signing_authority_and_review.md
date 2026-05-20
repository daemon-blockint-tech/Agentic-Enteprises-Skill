# Signing authority and review chains

## Table of contents

1. [Deliverable types and authority](#deliverable-types-and-authority)
2. [Typical review tiers](#typical-review-tiers)
3. [Signing vs authoring vs peer review](#signing-vs-authoring-vs-peer-review)
4. [Materiality and model tiering](#materiality-and-model-tiering)
5. [Regulatory and external reliance](#regulatory-and-external-reliance)
6. [Documentation templates](#documentation-templates)

## Deliverable types and authority

Classify the user’s deliverable before advising on “sign-off”:

| Deliverable type | Associate typical role | Usually requires fellow / appointed |
|---|---|---|
| Internal workpapers | Author or reviewer | Material methodology change |
| Methodology memo (non-opinion) | Lead author | Enterprise assumption change |
| Pricing indication | Technical lead | Filed rate/ form where statute requires |
| Reserve analysis support | Lead; not sole opinion | Statement of actuarial opinion |
| Peer review memorandum | Reviewer | N/A (documents review, not opinion) |
| Regulatory exhibit | Prepare sections | Appointed / qualified signatory per jurisdiction |
| External letter to auditor | Draft technical appendix | Partner actuary letterhead rules |

**Never** instruct the agent or user to claim statutory sign-off the credential does not support.

## Typical review tiers

Illustrative insurer/consulting chain (firm policies vary):

```
Analyst → Associate actuary → Fellow actuary → Chief / Appointed actuary
                ↓
         Independent peer review (EQ) for material models
```

**Peer review** may be parallel (same level) or elevated (fellow reviews associate) depending on **materiality** and **model tier**.

Associates should:

- Know **who must review** before release
- Escalate early when conclusions change materially vs prior quarter
- Log **draft vs final** status on distributed files

## Signing vs authoring vs peer review

| Action | Meaning | Associate |
|---|---|---|
| **Author** | Prepared analysis; professional responsibility for content | Yes, within scope |
| **Peer review** | Independent assessment of another’s work | Yes, if qualified and not conflicted |
| **Approve / sign** | Formal attestation, often with legal/regulatory effect | Limited; jurisdiction- and role-specific |
| **Co-sign** | Shared attestation | Only if firm policy explicitly allows |

**Authoring** a memo is not the same as **signing** an opinion. Use precise language in agent outputs: “draft for review,” “technical conclusion subject to signatory approval.”

## Materiality and model tiering

Firms often tier models (example labels):

| Tier | Examples | Review expectations |
|---|---|---|
| Tier 1 | Statutory reserve model, core pricing engine | Validation, independent review, senior sign-off |
| Tier 2 | Planning models, niche LOB tools | Associate + fellow review |
| Tier 3 | Ad hoc spreadsheets | Associate review; analyst prep |

Associates **lead** Tier 2 cycles and **support** Tier 1 with documented inputs; they rarely **sole-sign** Tier 1 outputs.

Factors increasing escalation:

- Large **PYD** or reserve movement vs prior
- **New** product or territory with thin data
- **Method change** (tail, discount, frequency/severity blend)
- **Regulatory** examination or comment letter active
- **Reinsurance** or **M&A** transaction timing

## Regulatory and external reliance

**Auditors** may rely on actuarial memos; **regulators** may request exhibits. Associates prepare **factually accurate** schedules and **clearly labeled** draft conclusions.

- **Audit inquiries:** factual responses; judgment calls with fellow visibility
- **Regulatory meetings:** talking points per `actuarial-consulting` / `actuary` when engagement-shaped
- **Third-party reliance letters:** only per firm legal template; scope limitations explicit

India (**IRDAI**), US (**state insurance departments**, NAIC), UK (**PRA/FCA**), EU (**Solvency II**) each define **who may sign what**—do not generalize from ASA to ASAI signing rights.

## Documentation templates

**Review log (minimum):**

| Field | Content |
|---|---|
| Deliverable ID | Memo / model run version |
| Author | Name, credential |
| Reviewer(s) | Name, credential, independence note |
| Date | Review completion |
| Findings | Material / non-material |
| Resolution | Change made or exception accepted |
| Signatory | If applicable, final approver |

**Email discipline:** avoid “approved” in email without linking to signed review log when policy requires formal sign-off.

Coordinate with `compliance-engineer` only for **evidence of controls** (access, change management)—not for actuarial method approval.
