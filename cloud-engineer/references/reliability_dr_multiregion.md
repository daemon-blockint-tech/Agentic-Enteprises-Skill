# Reliability and DR

## Table of contents

1. [Availability tiers](#availability-tiers)
2. [Backups and restore](#backups-and-restore)
3. [Multi-region](#multi-region)
4. [Operational drills](#operational-drills)

## Availability tiers

| Tier | Pattern | Typical RTO |
|---|---|---|
| Dev | Single AZ acceptable | Hours |
| Staging | Multi-AZ | < 1 hour |
| Prod | Multi-AZ + tested backups | Minutes–hours |
| Critical | Active-active multi-region | Minutes |

Align with product **RTO/RPO** from `senior-system-architecture` or TPM.

## Backups and restore

- **Automated backups** on managed DB and critical volumes
- **Cross-region copy** for regional disaster only when justified
- **Restore drill** quarterly: time to restore, data integrity check
- Document **runbook** — who approves failover, comms template

## Multi-region

Active-passive:

- DNS failover (Route 53, Cloud DNS, Traffic Manager)
- Replica DB promote procedure tested
- **Data residency** — legal before second region

Active-active:

- Conflict resolution, split-brain risk, higher cost
- Global load balancing + replicated stateless tier

## Operational drills

- Game day: kill AZ, verify autoscaling and alerts
- Tabletop: regional outage, credential compromise
- Post-drill: update runbooks and IaC gaps

Incident comms → `incident-management-engineer` if program-level.
