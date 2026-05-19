# Site Readiness and Access

## Pre-visit checklist

| Item | Verify |
|------|--------|
| Change ticket / work order approved | ID and window |
| Site contact and escort | Name, phone |
| Badge / background check | Lead time met |
| Colo work request | Ticket # if remote hands |
| Parts kit | Serials match BOM |
| Tools | Torque driver, console, fiber tester, labels |
| Drawings | Rack elevation, port map, cable plan |
| Rollback plan | Deinstall or leave-as-was |

## Site types

| Type | Typical constraints |
|------|---------------------|
| Enterprise customer DC | Customer change control, escort required |
| Colocation | Smart-hands SOW, lift limits, after-hours fees |
| Edge / closet | Power, cooling, space; often no redundant path |
| Lab / staging | Lower rigor; still document |

## Readiness gates

Before travel confirm:

- [ ] Rack space and U positions reserved
- [ ] Power circuit ID and breaker labeled
- [ ] Network demarc port allocated
- [ ] Lift available if equipment > solo carry limit
- [ ] Spares on-site or ship-to address confirmed

Pair with `senior-data-center-capacity-delivery-manager` when part of capacity delivery.

## Access documentation

Record on arrival:

- Time in / time out
- Escort name
- Areas accessed
- Deviations from planned rack IDs

## Common blockers

| Blocker | Action |
|---------|--------|
| Wrong rack | Stop; confirm with delivery manager |
| No power | Do not improvise; escalate facilities |
| Missing parts | Partial closeout; reschedule with logistics |
| Denied access | Document; notify program owner |

## Smart-hands work order (colo)

Include for vendor:

- Site, cage, rack, U range
- Step-by-step with photos required
- Prohibited actions (no logical config)
- Return packaging for RMA gear

## Anti-patterns

- Travel without approved change window
- Assume port numbers from old diagram
- Leave partial install unlabeled overnight energized
