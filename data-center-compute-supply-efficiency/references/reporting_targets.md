# Reporting and Targets

## Audience matrix

| Audience | Cares about | Format |
|---|---|---|
| **Engineering** | Utilization, queue time, migration backlog | Dashboard + backlog |
| **Finance** | Capex deferral, colo kW charges, TCO | Quarterly summary |
| **Sustainability** | PUE, carbon, refresh gains | Annual + trends |
| **Executives** | Risk, supply gaps, major wins | One-page |

## Monthly operational pack

1. **Supply** — inventory, incoming POs, GPU queue depth
2. **Demand** — utilization trends, new requests
3. **Gap** — surplus/deficit next 2 quarters
4. **Actions** — consolidations completed, kW reclaimed
5. **Risks** — lead times, cooling limits, SLA conflicts

## Target setting

| Target type | Example |
|---|---|
| **Utilization floor** | Prod compute avg CPU > 40% (excl. dedicated) |
| **Stranded kW cap** | < 5% of committed IT kW |
| **PUE** | Site-specific YoY improvement |
| **Refresh** | % fleet on current gen by year-end |
| **Decomm SLA** | Powered-off within 30d of approval |

Targets must be **achievable** and **excluded** where SLAs forbid consolidation.

## Initiative backlog fields

| Field | Purpose |
|---|---|
| Initiative | Short name |
| kW / capex impact | Estimated |
| Effort | T-shirt |
| Owner | Team |
| Dependency | K8s, app, facility |
| Status | Proposed / in progress / done |

## Narrative quality

- Lead with **business outcome** (deferred rack purchase, shorter GPU wait)
- Quantify uncertainty (± range on savings)
- Separate **one-time** reclaim vs **run-rate** efficiency

## Related comms

- Major sustainability claims → `communication-lead` for review
- Multi-site program → `technical-program-manager`
