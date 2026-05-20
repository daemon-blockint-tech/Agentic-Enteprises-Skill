# Actuarial consulting scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [Engagement types](#engagement-types)
3. [Independence and conflicts](#independence-and-conflicts)
4. [Professional standards (overview)](#professional-standards-overview)
5. [Documentation and quality](#documentation-and-quality)
6. [Handoffs to technical actuary work](#handoffs-to-technical-actuary-work)

## Role boundary

Actuarial **consulting** frames how actuarial work is sold, governed, communicated, and reviewed. It is distinct from:

| Adjacent function | Consulting focus | Typical handoff |
|---|---|---|
| `actuary` | Methods, calculations, triangles, assumptions | Consulting defines SOW; actuary executes models |
| `business-consultant` | Enterprise strategy, operating model | Consulting when reserve/pricing/capital is central |
| `commercial-counsel` | Legal interpretation, contracts | Consulting supplies exhibits; counsel interprets law |
| `compliance-engineer` | Control evidence, SOC/ISO automation | Consulting on actuarial governance, not IT controls |
| `financial-analyst` | Corporate FP&A, investor KPIs | Consulting on insurance liabilities and technical metrics |

## Engagement types

| Type | Primary client question | Consulting deliverables |
|---|---|---|
| Reserve / opinion support | Are reserves reasonable? Is documentation audit-ready? | Scope, memo structure, review plan, board narrative |
| Pricing review | Are rates adequate by segment? | Engagement design, management storyline, governance |
| Capital / solvency review | How sensitive is surplus to key risks? | Issue framing, exhibit plan, regulator/board prep |
| Model validation | Is the model fit for purpose? | Validation plan, findings template, remediation tracking |
| M&A / DD | What are reserve and pricing risks in the deal? | DD checklist, data request, findings by materiality |
| Regulatory / board prep | What will examiners or directors ask? | Talking points, exhibit index, consistency checks |

Scope each engagement to **one primary purpose**. Split pricing and reserving opinions across teams when independence requires.

## Independence and conflicts

Document before work begins:

- **Prior services** to the same entity (pricing, validation, software selection)
- **Management roles** (CFO actuary, board observer) that constrain advocacy
- **Data vendors** or software partners with economic ties
- **Contingent fees** tied to deal outcome (generally avoid for opinion work)

When conflicts cannot be cleared, narrow scope, add disclosure, or decline.

## Professional standards (overview)

Align workpapers to jurisdiction-specific actuarial standards (e.g., US ASOPs, IAA guidance) at a high level:

- **Purpose** and intended user of the work
- **Documentation** sufficient for another qualified actuary to evaluate
- **Limitations** of data, methods, and reliance on others
- **Communication** appropriate to audience sophistication

Do not claim **appointed actuary**, **qualified actuary sign-off**, or **legal compliance** unless the user holds that authority.

## Documentation and quality

Minimum consulting file structure:

```
engagement/
├── SOW and change orders
├── data inventory and reliance letters
├── analysis/ (technical work by actuary team)
├── review log (EQR, peer review)
├── deliverables/ (memo, exhibits, deck)
└── correspondence/ (management, board, regulator)
```

Quality gates:

- Partner or qualified reviewer sign-off before client delivery
- Versioned exhibits tied to data cutoff
- Traceability from conclusion to exhibit

## Handoffs to technical actuary work

Consulting ends where **repeatable calculation** begins. Hand off to `actuary` when the user needs:

- Triangle development and IBNR selection
- Mortality/morbidity studies and credibility weighting
- Detailed pricing indications by segment
- Capital model runs and stress testing execution

Retain consulting ownership of **narrative, governance, and stakeholder packaging**.
