# Regulatory and statutory accountability

## Table of contents

1. [Framework-level regimes](#framework-level-regimes)
2. [Opinion and report types](#opinion-and-report-types)
3. [Opinion structure (non-template)](#opinion-structure-non-template)
4. [Reliance and limitations](#reliance-and-limitations)
5. [Filing coordination](#filing-coordination)
6. [Multi-entity and group issues](#multi-entity-and-group-issues)

## Framework-level regimes

This reference describes **concepts**, not jurisdiction-specific legal requirements. Always escalate binding rules to qualified actuaries and counsel.

| Regime (concept) | Actuarial accountability theme |
|---|---|
| **Solvency II** (EU) | Technical provisions, SCR, ORSA, actuarial function requirements |
| **RBC** (US NAIC) | Risk-based capital, actuarial opinion on reserves and related topics |
| **IFRS 17** | Measurement assumptions; coordination with accounting—not duplicate of opinion |
| **Local appointed actuary** | Country-specific appointment, qualification, and report content |
| **Pension funding** | Actuary role in funding valuations vs accounting (separate from insurer SAO) |

Map user context to **one primary regime** per deliverable; note **group** reporting overlays separately.

## Opinion and report types

| Type (label varies) | Typical content owned by appointed actuary |
|---|---|
| **Statement of actuarial opinion (SAO)** | Reserve adequacy, methods, reliance, limitations |
| **Actuarial certification** | Premium rates, policy reserves, or specific schedules |
| **Appointed actuary report** | Broader narrative to regulator (methods, governance, risks) |
| **ORSA actuarial input** | Scenarios, assumptions, aggregation narrative (may not be a single “opinion”) |
| **Pension actuarial opinion** | Funding status, assumptions—often separate appointment |

Distinguish **opinion** (professional statement) from **exhibits** (calculations) and **management representation**.

## Opinion structure (non-template)

Draft structures for human review only—do not present as filed text.

**Typical sections:**

1. **Identification** — Appointed actuary, appointment basis, entity, valuation date
2. **Scope** — Lines of business, reserves/premiums covered, exclusions
3. **Standards** — Reference actuarial standards (framework-level citation)
4. **Methods and assumptions** — Summary; pointer to governance and `assumption-setting` artifacts
5. **Results** — Adequacy conclusion categories (e.g., reasonable, qualified—labels jurisdiction-specific)
6. **Reliance** — Data, models, auditors, reinsurance info, other experts
7. **Limitations** — Data gaps, uncertainty, events after valuation date
8. **Signature block** — For qualified human only

**Qualified vs adverse language** — Use only labels appropriate to the user’s jurisdiction and facts; AI must not invent regulatory conclusions.

## Reliance and limitations

| Reliance source | Document in opinion appendix |
|---|---|
| Data warehouses / bordereaux | Cutoff, controls, known issues |
| Vendor models | Version, validation status, use restrictions |
| Reinsurance collectibility | Assumptions on ceded recoverables |
| Investment / ALM | Cash-flow feeds from `asset-liability-management` partners |
| External experts | Scope and boundaries of their work |

**Limitations** must be **prominent** when:

- Material model changes not fully validated
- Large losses or cat events near valuation date
- M&A integration with incomplete data
- Regulatory or accounting method changes mid-cycle

## Filing coordination

Workflow (conceptual):

```
Technical work (actuary, actuarial-analyst)
        → Governance review (fellow, assumption committee)
        → Opinion drafting (appointed actuary)
        → Legal / compliance review (counsel, compliance-engineer for controls)
        → Filing (human signatories only)
```

**AI role:** Structure narratives, checklists, bridges, and gap lists—not execute filing or sign.

## Multi-entity and group issues

| Issue | Chief / appointed actuary consideration |
|---|---|
| **Local vs group** | Local opinions vs group consolidation narrative |
| **Ring-fencing** | Which entities hold appointment |
| **Reinsurance intragroup** | Elimination and collectibility assumptions |
| **Currency** | Translation and economic assumptions |
| **M&A** | Purchase accounting actuarial input; opinion timing |

Coordinate with `actuarial-consulting` for transaction **process**; retain accountability framing here.
