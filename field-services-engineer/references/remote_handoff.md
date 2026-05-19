# Remote Handoff

## Handoff triggers

Hand off to remote when **L0/L1 field complete** and runbook requires:

- OS install / imaging
- BMC/IPMI standardization
- Cluster join (`cluster-deployment-engineer`)
- Network zoning on fabric (`infrastructure-engineer`)
- Storage zoning
- License activation

## Handoff packet

```markdown
## Field closeout — WO [ID]

**Site / rack:** …
**Devices:** table of serial, U, mgmt MAC if known
**Physical port map:** attach or link
**Photos:** [links]
**L1 status:** BMC ping Y/N, link lights Y/N
**Blockers:** …
**Spares consumed:** …
**Next owner:** @team
**Requested remote SLA:** …
```

## Remote teams map

| Need | Skill / team |
|------|----------------|
| K8s bootstrap | `cluster-deployment-engineer` |
| Cloud/network config | `infrastructure-engineer` |
| Capacity program status | `senior-data-center-capacity-delivery-manager` |
| Design clarification | `data-center-design-execution-lead` |
| Customer relationship | Account team / `community-executive-escalations-program-manager` |

## Field support during remote work

Remain on standby if SOW includes:

- Reseat cables after remote misconfig suspicion
- Swap FRU if remote diagnoses hardware fault
- Colo coordination for after-hours extension

Use separate time log for scope creep.

## Escalation from field

| Situation | Escalate to |
|-----------|-------------|
| Design error blocks install | Design + delivery manager |
| Colo damaged gear | Logistics + legal per policy |
| Customer scope dispute | Account + program manager |
| Safety incident | Safety officer + manager |

## Ticket hygiene

- One parent WO for visit; child tasks for remote
- Link photos to ticket storage
- Close field WO only when L1 criteria met or exception approved

## Lessons learned

After major visits, 15-min retro:

- Parts accuracy
- Drawing accuracy
- Tooling gaps
- Update playbooks in references

## Anti-patterns

- "Throw it over the wall" without port map
- Remote asks for unlabeled port guesses
- Field closes ticket before remote confirms BMC
