# Readiness Gates

## Gate definitions

| Gate | Meaning | Typical approvers |
|---|---|---|
| **G0 — Charter** | Funded initiative, DRIs named | Portfolio / steering |
| **G1 — Design release** | IFC for construction | Design + delivery |
| **G2 — Energized** | Safe electrical energization per method | Facilities + electrician |
| **G3 — Commissioned** | IST/FAT complete | Commissioning agent + facilities |
| **G4 — Rack-ready** | Rack positions powered, cabled to demarc | Facilities + network |
| **G5 — Workload-ready** | Ready for production traffic | IT infra + cluster |

## Rack-ready checklist (sample)

- [ ] IT kW available at rack PDU within nameplate
- [ ] Grounding and labeling per standard
- [ ] Network demarc patched to row/hall standard
- [ ] Environmental within spec (temp, humidity)
- [ ] Fire/life safety in service for zone
- [ ] DCIM/BMS points live and alarming
- [ ] As-built drawings uploaded
- [ ] Access and safety briefing for install crew

## Workload-ready (additional)

- [ ] Racks installed and torqued
- [ ] Structured cabling per design
- [ ] Out-of-band management reachable
- [ ] Cluster/bootstrap smoke test (`cluster-deployment-engineer`)
- [ ] Change window approved if brownfield hall

Do not declare G5 without G4 sign-off.

## Partial delivery

**Phased rows** acceptable if:

- Safety boundaries respected
- kW accounting clear in burn-up
- Steering informed

Document which racks are in which phase.

## Rollback

If commissioning fails:

- Hold G4/G5; root cause owner assigned
- No IT install in affected zone until re-test pass
