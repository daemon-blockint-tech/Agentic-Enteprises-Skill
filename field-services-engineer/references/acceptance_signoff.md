# Acceptance and Sign-off

## Acceptance test tiers

| Tier | Scope | Who signs |
|------|-------|-----------|
| **L0** | Mechanical mount, power present | Field engineer |
| **L1** | Link lights, BMC reachable on console | Field + remote NOC |
| **L2** | OS/install ready per runbook | Remote platform team |
| **L3** | Workload smoke test | Application owner |

Field typically owns **L0–L1** unless SOW includes staging OS.

## Field acceptance checklist

```markdown
- [ ] Rack/U matches work order
- [ ] Serials photographed and logged
- [ ] Rails/torque verified
- [ ] A/B power connected per design
- [ ] PDU load within label
- [ ] Network ports cabled per port map
- [ ] Labels both ends
- [ ] Link lights on expected ports (photo)
- [ ] BMC/IPMI ping or serial console login (if in scope)
- [ ] No foreign objects, packaging removed from airflow
- [ ] Spares and trash removed from site
- [ ] Customer/colo sign sheet or email confirmation
```

## Photo set (minimum)

1. Wide rack front
2. Each new asset nameplate/serial
3. PDU connections (without exposing unrelated customer gear)
4. Cable dress at TOR
5. Link lights close-up
6. Completed label examples

Follow customer photo policy (no PII screens).

## CMDB / asset update

Within 4h of leave site:

- Asset tag, serial, model
- Rack, U, site ID
- Install date, work order #
- Status: installed / pending remote config

## Sign-off template

```markdown
**Work order:** [ID]
**Site:** [name] **Window:** [start–end]
**Summary:** Installed [n] devices per plan; L0/L1 complete.
**Exceptions:** [none / list]
**Remote actions needed:** OS install, zoning, cluster join — owner [team]
**Customer signatory:** [name] [time]
```

## Partial completion

If blocked:

- Document completed vs remaining
- Secure equipment (power off if unsafe)
- Schedule return visit with parts list
- Do not claim full acceptance

## RMA / failed hardware

- Photo damage if shipping claim
- Retain failed part until RMA auth
- Update ticket with serial and failure mode
