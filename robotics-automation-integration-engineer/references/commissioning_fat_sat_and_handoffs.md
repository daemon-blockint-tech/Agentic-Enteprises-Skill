# Commissioning, FAT/SAT, and handoffs

## Table of contents

1. [Commissioning phases](#commissioning-phases)
2. [FAT checklist themes](#fat-checklist-themes)
3. [SAT and go-live](#sat-and-go-live)
4. [MES, WMS, and ERP interfaces](#mes-wms-and-erp-interfaces)
5. [Turnover package](#turnover-package)

## Commissioning phases

| Phase | Activities |
|---|---|
| Power and network | LOTO release per step, IP check, switch port labels |
| I/O verification | Point-to-point wire test, sensor polarity, force table |
| Device comm | Bus online, no lost devices, firmware recorded |
| Dry motion | Robot dry run, conveyor inch, AMR test loop |
| Logic integration | Handshakes, modes, fault injection |
| Production trial | At-rate run, OEE baseline, quality sample |
| Documentation | As-built, backups, training |

Never skip **safety device functional test** before enabling motion at speed.

## FAT checklist themes

Factory acceptance (vendor shop or integrator hall):

- [ ] I/O dictionary matches signed drawing
- [ ] Safety chain test—each e-stop, curtain, door
- [ ] Robot reach and interference check vs. model
- [ ] Cycle time measured N consecutive cycles
- [ ] Recovery from each defined fault class
- [ ] Vision pass/fail and reject routing
- [ ] AMR dock/undock with robot interlock
- [ ] HMI screens: mode, fault, reset (integration tags only)
- [ ] Backup/restore procedure demonstrated
- [ ] Spare parts list and recommended stock

Record **punch list** with owner and target date; block SAT only for safety-critical open items.

## SAT and go-live

Site acceptance on customer floor:

- Re-verify network after transport (cable damage, IP drift)
- Re-teach or confirm frames if cell moved
- Align with site OT policies (`scada-ics-cyber-security-specialist`)
- Operator training on modes, resets, and LOTO
- Run at rate with customer quality sign-off
- Hypercare period—defined response times and escalation

**Change control after go-live:** parameter changes require revision log; robot path edits require re-FAT slice if safety-affecting.

## MES, WMS, and ERP interfaces

| Interface | Typical integration pattern |
|---|---|
| Order release | MES/ERP → cell supervisor: SKU, qty, routing ID |
| Start / complete | Cycle signals with timestamp and operator ID |
| Traceability | Serial, lot, vision image path, robot program ID |
| Exceptions | Scrap, rework, downtime reason codes |
| AMR missions | WMS pick → fleet → station (see `wms-developer`) |

Document **message spec**: OPC UA nodes, REST, MQTT, or flat file—schema, retry, idempotency, and error codes.

Integration engineer owns **cell boundary**; enterprise workflow depth routes to WMS/MES teams.

## Turnover package

Deliver to customer operations and maintenance:

| Artifact | Content |
|---|---|
| As-built drawings | Layout, panel, network one-line |
| I/O and signal dictionary | Final Excel/CSV export |
| Parameter backups | PLC, robot, vision, drive projects (versioned) |
| FAT/SAT records | Signed checklists, deviation log |
| Spare parts and manuals | OEM links, recommended stock |
| Runbooks | Start-up, homing, changeover, fault reset |
| Cyber notes | Default passwords changed, remote access policy |

Archive media in customer CMMS or document control per site rules.
