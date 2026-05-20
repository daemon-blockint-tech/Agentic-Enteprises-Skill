# Architecture deliverables

## Table of contents

1. [Diagram types](#diagram-types)
2. [ADR template](#adr-template)
3. [Review checklist](#review-checklist)
4. [Stakeholder packaging](#stakeholder-packaging)

## Diagram types

| View | Audience | Content |
|---|---|---|
| Context (C4 L1) | Executives, security | Systems and trust boundaries |
| Container (C4 L2) | Engineering leads | Major deployables, data stores |
| Cloud deployment | Implementers | Accounts, VPCs, services, regions |
| Sequence | Integration disputes | Critical request flows |

Use consistent **legend**: environments, data classification, encryption in transit.

## ADR template

```markdown
# ADR-NNN: Title

## Status
Proposed | Accepted | Deprecated | Superseded by ADR-XXX

## Context
Forces and constraints (NFRs, compliance, timeline).

## Decision
What we will do.

## Options considered
| Option | Pros | Cons |

## Consequences
Positive, negative, risks to monitor.

## Follow-up
Tickets, pilots, review date.
```

Store ADRs in repo; link from architecture wiki.

## Review checklist

Before **Accepted**:

- [ ] NFRs traced to design elements
- [ ] Security review scheduled or complete
- [ ] Cost estimate (ROM) with assumptions
- [ ] Operational ownership named
- [ ] DR and backup approach stated
- [ ] Migration/rollback for changes to prod
- [ ] No undocumented one-way doors

## Stakeholder packaging

| Audience | Emphasis |
|---|---|
| Engineering | Deployment view, interfaces, SLAs |
| Security | Data flows, controls, exceptions |
| Finance | TCO, tag/chargeback model |
| TPM | Waves, dependencies, risks |

Program tracking → `technical-program-manager`.
