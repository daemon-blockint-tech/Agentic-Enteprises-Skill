# Execution and commissioning

## Table of contents

1. [Phase plan](#phase-plan)
2. [Long-lead tracking](#long-lead-tracking)
3. [Commissioning tests](#commissioning-tests)

## Phase plan

| Phase | Gate |
|---|---|
| Concept | Signed capacity model and tier intent |
| Detailed design | MEP + IT drawings, BoM, permits submitted |
| Procurement | Critical path items ordered |
| Construction | MEP complete, inspection passed |
| IT install | Racks, PDUs, cabling, labeling |
| Commissioning | IST complete, punch list closed |
| Handoff | Ops sign-off, DCIM populated |

Use `technical-program-manager` for multi-vendor RAID across civil, MEP, and IT trades.

## Long-lead tracking

Typical long-lead (order early):

- Generators, switchgear, UPS modules
- Core switches, fiber panels
- Custom containment, CDUs for liquid cooling
- Permits and utility power upgrades

Weekly critical-path review until install complete.

## Commissioning tests

| Test | Pass criteria |
|---|---|
| Power failover | ATS/UPS transfer; no unplanned IT shutdown |
| Cooling failure | Redundant unit carries load; alarms fire |
| Redundant paths | Lose A or B feed; dual-cord hosts stay up |
| Network | Loop-free; BGP/WAN failover if applicable |
| Integrated | Full rack load soak 24–72h |

Document results; attach to handoff package. Red-tag unresolved life-safety items before energizing.
