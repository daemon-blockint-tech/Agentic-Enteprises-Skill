# Reinsurance and Catastrophe

## Purpose

Explain how P&C carriers transfer risk to reinsurers, common treaty structures, and catastrophe accumulation concepts—at overview level for underwriting, finance, and strategy discussions.

## Why reinsurance

- **Capacity** — write larger limits than net retention
- **Stability** — smooth results against large or cat losses
- **Capital** — support rating agency and regulatory capital metrics (coordinate with `actuary`)
- **Expertise** — facultative support on unusual risks

## Treaty types (proportional)

### Quota share

- Reinsurer takes a **fixed percentage** of premium and losses on defined book
- Ceding commission compensates cedant for acquisition/expense
- Used for new ventures, capacity relief, or MGAs

### Surplus share

- Reinsurer takes portion **above retention** per line (property schedules common)
- Multiple lines (facultative automatic lines) possible

## Treaty types (non-proportional)

### Per-risk excess of loss (XOL)

- Reinsurer pays losses **above retention** per risk (e.g., $500K xs $500K)
- Applies to large single losses, not aggregate cat (unless structured)

### Catastrophe XOL

- Covers **aggregate losses** from a defined cat event above retention
- Often structured in layers (e.g., $10M xs $10M, $20M xs $20M)
- **Hours clause** and geographic definition of event
- **Reinstatement premium** if layer exhausted and coverage restored

### Aggregate XOL

- Protects **accumulation** of losses in period (not necessarily single event)

### Stop loss

- Protects combined ratio or loss ratio above threshold on a book

## Facultative reinsurance

- **Facultative** — individual risk submission when treaty capacity insufficient or risk unusual
- Common for property values above treaty capacity, difficult liability risks

## Fronting and captives (overview)

- **Fronting carrier** issues policy; reinsurer or captive assumes most risk via agreement
- Requires strong trust, collateral, and regulatory compliance—not legal advice

## Catastrophe modeling (overview)

Cat models estimate **probable maximum loss** and **average annual loss** by peril:

| Peril | Notes |
|---|---|
| Hurricane | Wind, surge by coastal zone |
| Earthquake | Shake by soil/zone |
| Wildfire | Wildland-urban interface accumulation |
| Severe convective storm | Hail, tornado footprint |
| Flood | Often excluded in primary; NFIP/private flood separate |

Model output feeds:

- **Cat load** in pricing
- **Aggregate monitoring** — PML, tail scenarios
- **Reinsurance buying** — attachment and limit selection

## Key terms

| Term | Meaning |
|---|---|
| Retention | Amount cedant keeps net |
| Limit | Maximum reinsurer payment per contract/layer |
| Reinstatement | Restoration of exhausted limit (often with premium) |
| Clash cover | Excess across multiple policies from one event |
| Reinstatement premium | Cost to restore layer |

## Buying workflow (simplified)

1. Set **risk appetite** and net retention by LOB
2. Run **exposure data** (geocoded locations, values, construction)
3. Model **gross and net** cat scenarios
4. Structure **treaty program** with brokers/reinsurers
5. Negotiate **terms** (hours, definitions, reinstatements, commissions)
6. Document in **slip/treaty**; track **bordereaux** and ceding accounting

## Integration with underwriting

- Property schedules drive **surplus** and **cat** needs
- Liability spikes (umbrella, railroad, etc.) may need **fac** or higher XOL
- MGA programs often have **quota share** behind capacity provider

## Boundaries

- Sign-off pricing and statutory statements → `actuary`
- Contract wording and disputes → `commercial-counsel`
- Primary policy flood/cat exclusions → `policy_coverage_and_forms.md`
