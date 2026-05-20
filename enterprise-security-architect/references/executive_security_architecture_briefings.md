# Executive security architecture briefings

## Table of contents

1. [Audience and cadence](#audience-and-cadence)
2. [Narrative structure](#narrative-structure)
3. [Investment framing](#investment-framing)
4. [Acquisition summaries](#acquisition-summaries)
5. [Anti-patterns](#anti-patterns)

## Audience and cadence

| Audience | Focus | Cadence |
|---|---|---|
| Board / audit committee | Architecture posture, standards adoption, material pattern gaps | Quarterly (appendix to CISO pack) |
| Executive committee | Investment trade-offs, cross-BU standards adoption | Monthly or quarterly |
| CISO staff | Architecture roadmap, pattern health, exception aging | Biweekly |
| BU leaders | Standards compliance, support model, acquisition integration | As needed |

**Boundary:** Program KRIs, risk appetite, crisis comms, and full board security narrative → `chief-information-security-officer`. This reference covers **architecture evidence** (reference model version, adoption metrics, zero-trust phases, exception register).

Keep **technical depth in appendix**; main deck is decision-oriented.

## Narrative structure

Recommended flow (10–15 slides max for board):

1. **Context** — threat landscape headline (1 slide, sourced)
2. **Posture snapshot** — domains: identity, data, app, network, endpoint, ops (traffic-light)
3. **Standards adoption** — % mandatory pattern coverage; top gaps
4. **Zero-trust / segmentation** — phase, milestones, blockers
5. **Material exceptions** — count, aging, compensating controls summary
6. **Incidents / lessons** — architecture-relevant themes only (not SOC ticket detail)
7. **Investments** — prioritized initiatives with outcomes and dependencies
8. **Acquisitions / major programs** — integration status
9. **Asks** — decisions, funding, policy, or risk acceptance

Link each gap to a **named initiative** and owner; avoid orphan findings.

## Investment framing

| Element | Guidance |
|---|---|
| Problem | Business impact (availability, fraud, regulatory, trust) |
| Option | Build vs buy vs consolidate; reference approved patterns |
| Cost | Capex/opex, licensing, headcount; multi-year view |
| Benefit | Risk reduction, audit efficiency, speed to market |
| Metrics | Leading indicators (coverage) and lagging (incidents, audit findings) |
| Dependencies | IdP, network, cloud foundation — flag cross-functional needs |

Coordinate infrastructure funding narratives with `vp-of-infrastructure` when initiatives span security and platform.

## Acquisition summaries

One-page **security integration status** per deal:

| Section | Content |
|---|---|
| Target profile | Data tiers, tech stack, identity model |
| Day 1 | Contain — MFA, admin lockdown, logging tap, incident contacts |
| Day 30 | Integrate — IdP federation plan, network connectivity, SIEM onboarding |
| Day 90 | Harmonize — mandatory patterns, retire duplicate tools where economical |
| Risks | Open exceptions, regulatory notifications if required |
| Decision | Continue standalone enclave vs full assimilation timeline |

Do not duplicate legal due diligence; flag **architecture blockers** for integration leadership.

## Anti-patterns

- Tool laundry lists without control outcomes
- Heat maps with no owners or remediation dates
- Conflating **risk score** with **architecture maturity** (use both, label clearly)
- Promising zero trust completion without identity and logging prerequisites
- Board decks that are audit evidence dumps (route detail to `compliance-specialist`)

Pair narratives with **architecture artifacts**: reference model version, standards catalog revision, exception register excerpt.
