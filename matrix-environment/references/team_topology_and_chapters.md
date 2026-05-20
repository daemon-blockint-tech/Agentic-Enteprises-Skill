# Team Topology and Chapters

## Topology patterns

| Pattern | Best when | Watch-outs |
|---|---|---|
| **Functional (central)** | Early stage, heavy compliance, scarce specialists | Bottleneck, distant from product context |
| **Product-led (vertical)** | Strong product ownership, fast delivery | Duplicated security/platform, inconsistent standards |
| **Matrix (dual reporting)** | Need standards + speed; mature management | Ambiguous accountability if RACI weak |
| **Platform + stream-aligned** (Team Topologies) | Scale with internal developer platform | Platform becomes ticket queue without product mindset |

## Common security/tech structures

### Central security (horizontal)

- AppSec, GRC, IAM, vuln management, architecture review
- SOC and/or CTI as shared service
- IR/CSIRT as declared incident command

### Embedded security (in verticals)

- Security champions, BUs security liaisons, embedded AppSec in tribes
- Federated GRC with central policy

### Platform organization

- **Platform engineering** — IDP, CI/CD templates, observability baselines
- **Cloud center of excellence** — standards, guardrails, not every ticket
- **SRE** — reliability standards + embedded capacity in critical services

## Chapters, guilds, communities of practice

| Element | Purpose | Typical membership |
|---|---|---|
| **Chapter lead** | Career, hiring bar, craft standards | People managers or senior ICs in discipline |
| **Guild / CoP** | Cross-cutting learning, playbooks | Volunteers + facilitator from central team |
| **Chapter backlog** | Tooling, training, template improvements | Funded slice from central budget |

**Security chapter topics:** secure SDLC, threat modeling clinic, control automation patterns, purple-team learnings.

**Platform chapter topics:** golden paths, service templates, incident tooling, cost visibility.

## Alignment: platform vs product vs security

```
                    ┌─────────────────┐
                    │  Standards /    │
                    │  policy (GRC,   │
                    │  architecture)  │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
 ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
 │   Platform   │   │   Product    │   │   Security   │
 │   (enable)   │   │   (deliver)  │   │   (assure)   │
 └──────┬───────┘   └──────┬───────┘   └──────┬───────┘
        │                  │                  │
        └──────────────────┴──────────────────┘
                    Shared interfaces
                    (intake, SLAs, tools)
```

**Rules of thumb:**

- Platform **enables**; product **owns** service outcomes; security **assures** with proportional controls
- Do not make platform the only path for every security control—use paved roads + guardrails
- Embed security **at design and release** boundaries, not only at audit time

## Sizing heuristics (indicative, adjust for risk)

| Company size (eng+FTE) | Central security | Embedded/champions | Platform |
|---|---|---|---|
| &lt; 50 | 2–5 generalists | Champions per squad | Often part-time |
| 50–200 | AppSec + GRC + SOC starter | 1 liaison per major product line | Small platform team |
| 200–1000 | Specialized functions + SOC | Embedded AppSec in tribes | IDP + SRE hub |
| 1000+ | Federated model with strong chapter | CoE + embedded mix | Multi-platform domains |

Document assumptions; ratios are not substitutes for risk-based staffing.

## Outputs

- Topology diagram (boxes, solid/dotted lines)
- Chapter charters (mission, scope, funding)
- Placement decision: central vs embedded per capability
