# Facility requirements

## Table of contents

1. [Decision matrix](#decision-matrix)
2. [Tier intent](#tier-intent)
3. [Capacity model](#capacity-model)

## Decision matrix

| Factor | Own build | Colo cage | Cloud |
|---|---|---|---|
| Capex | High | Medium (commit) | OpEx |
| Time to capacity | 12–24+ months | 3–9 months | Days–weeks |
| Control | Full | Contractual | Provider |
| GPU/HPC density | Custom liquid possible | Depends on colo | Instance types |

Use cloud for elastic burst; use facility for data residency, latency, or sustained high kW/rack.

## Tier intent

Align business RTO/RPO with facility design (Uptime Institute tier concepts, TIA-942):

| Intent | Typical facility features |
|---|---|
| Basic | Single path power/cooling; office-grade risk |
| Redundant components | N+1 cooling; dual PDUs to rack |
| Concurrently maintainable | Separate distribution paths; maintenance without shutdown |
| Fault tolerant | 2N or 2(N+1) for critical chain; min 96h fuel (if on-site gen) |

Document **actual** design vs marketing tier claims—gap analysis for insurance and audits.

## Capacity model

Spreadsheet rows per year:

| Year | Racks | kW/rack (design) | Total kW | Network 100G ports | Floor sq ft |
|---|---|---|---|---|---|
| Y0 | 20 | 8 | 160 | 40 | … |
| Y3 | 40 | 12 | 480 | 80 | … |

Include **growth headroom** (20–30% power, 15% cooling) before ordering switch gear and PDUs.

Validate floor loading and ceiling height for cabinet depth and overhead cable tray.
