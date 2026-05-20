# Jargon decoding and glossary

## Table of contents

1. [Jargon pass workflow](#jargon-pass-workflow)
2. [Overloaded terms](#overloaded-terms)
3. [Assumption surfacing](#assumption-surfacing)
4. [Glossary format](#glossary-format)
5. [Metric alignment](#metric-alignment)

## Jargon pass workflow

1. **Extract** candidate terms (acronyms, product codenames, role-specific nouns)
2. **Classify** each term:
   - Universal (define once)
   - Overloaded (disambiguate by audience)
   - Local slang (replace or footnote)
3. **Rewrite** sentences so a target reader needs no insider context
4. **Footnote** only terms that must stay specialized

## Overloaded terms

These words mean different things by department—always disambiguate in dual-audience docs:

| Term | Engineering | Finance | Legal/compliance | Product |
|---|---|---|---|---|
| Platform | Shared services / infra | Cost center or revenue line | Vendor/subprocessor context | User-facing capability |
| Risk | Security/availability | Financial exposure | Regulatory/legal | User or reputational |
| Material | N/A (unless accounting) | Financial statement threshold | Disclosure trigger | Roadmap priority |
| Done | Shipped + monitored | Recognized / booked | Contractually satisfied | Meets acceptance criteria |
| Customer | Tenant / account entity | Revenue account | Contract party | Persona / segment |

## Assumption surfacing

Convert implicit assumptions into labeled statements:

| Hidden assumption | Surfaced as |
|---|---|
| "Finance already approved budget" | **Assumption:** FY26 opex approved through Q2 per [ref] |
| "Legal signed off" | **Assumption:** DPA executed 2026-03-01; marketing use not in scope |
| "Data is clean" | **Assumption:** Source table `X` reconciled to GL within 2% |
| "Team has capacity" | **Assumption:** 2 FTE available after Project Y cutover |

Use **Facts** / **Assumptions** / **Open questions** headers when ambiguity is high.

## Glossary format

Keep glossaries minimal—only terms used in the artifact:

```markdown
| Term | Definition (for this doc) | Owner |
|---|---|---|
| ARR | Annual recurring revenue per signed contract; excludes usage overage | Finance |
| P99 latency | 99th percentile request duration over 5m windows | Engineering |
```

For dual-audience docs, add a **plain-language** column for executive readers.

## Metric alignment

When translating metrics across teams:

1. State **numerator and denominator**
2. Specify **time window** and **population** (all customers vs segment)
3. Note **lag** (real-time vs month-close)
4. Map **engineering SLIs** to **business KPIs** in one table:

| Engineering SLI | Business KPI | Relationship |
|---|---|---|
| Checkout error rate | Conversion | Inverse; segment by region |
| API availability | SLA credits | Contractual threshold at 99.9% |

Never equate metrics without documenting the mapping assumption.
