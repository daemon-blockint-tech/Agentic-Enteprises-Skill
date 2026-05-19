# Rack-and-Stack Install

## Install sequence (typical)

1. Verify rack location and U map against plan
2. Install rails / cage nuts / shelf per vendor spec
3. Mount heaviest equipment low (storage, GPU chassis)
4. Mount network top-of-rack per heat exhaust direction
5. Connect PDUs (redundant A/B if designed)
6. Dress power cords; no strain on connectors
7. Stage network cables; do not connect until labeling ready
8. Apply asset tags and update CMDB draft

## Mechanical checks

| Check | Pass criteria |
|-------|----------------|
| Rail engagement | Clicks both sides; screw torque per spec |
| Clearance | Door closes; no airflow blockage |
| Weight | Within rack static load limit |
| Cable management | Arms installed before dense cabling |

## Power

- Match **A/B feed** to design (never single-feed dual-PSU illusion)
- C13/C19 orientation consistent
- PDU load: do not exceed circuit label without approval
- **LOTO** per `safety_compliance.md` before panel work

## Decommission / RMA

1. Graceful shutdown signal from remote owner (if required)
2. Disconnect power and data
3. Remove rails; fill holes if policy requires
4. Pack anti-static; RMA label on box
5. Photo empty rack positions

## Hardware swap (FRU)

- Record old and new serial
- Same model generation unless change approved
- Firmware baseline note for remote team
- Run POST / BMC check before close

## Deviations

If physical layout cannot match design:

- Stop work
- Photo issue
- Escalate to `data-center-design-execution-lead` or delivery manager
- Do not drill or modify without approval

## Handoff data for remote install

```markdown
| Asset | Serial | Rack | U | PDU port | NIC ports | Notes |
```

Remote `cluster-deployment-engineer` uses this for bootstrap.
