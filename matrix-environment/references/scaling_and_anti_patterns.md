# Scaling and Anti-Patterns

## Growth stages and model shifts

| Stage | Org signal | Typical shift |
|---|---|---|
| **Founding** | Generalists, informal | Champions + light central policy |
| **Scale-up** | Product lines multiply | Introduce platform team; formal RACI |
| **Enterprise** | Regulated, multi-BU | Federated security + strong chapters |
| **Post-M&A** | Duplicate functions | Integration playbook; 90-day interface merge |

Plan **transition triggers** (headcount, incident rate, audit grade, release frequency)—not calendar-only reorganizations.

## Consolidate vs federate

| Consolidate (central) when… | Federate (embed) when… |
|---|---|
| Scarce expertise (IR, CTI, crypto) | Context-heavy AppSec in product |
| Need uniform audit narrative | Speed dominates; standards via paved roads |
| Tooling economies of scale | Strong BU P&L ownership |
| Regulatory concentration | Distinct risk profiles per BU |

**Hybrid (common at scale):** central standards + embedded execution + chapter for craft.

## Anti-patterns

| Anti-pattern | Symptom | Remedy |
|---|---|---|
| **Matrix without RACI** | Meetings, no decisions | One A per outcome; publish matrix |
| **Security as gate only** | Late reviews, dev bypass | Shift-left, automated checks, office hours |
| **Platform ticket factory** | Long queues, shadow infra | Product mindset, SLAs, self-service |
| **SOC owns remediation** | Alerts closed without fix | Eng A on vuln/fix; SOC on detect |
| **Duplicate SOCs / AppSecs** | M&A or BU silos | Single tool of record; federated liaisons |
| **Guild without budget** | Talk, no templates | Chapter backlog + funded % capacity |
| **Consulted paralysis** | Every RFC needs 6 teams | Tiered review; risk-based gates |
| **Shadow governance** | Slack decides, docs lag | Align ritual to written model |
| **Ratio worship** | 1:50 AppSec regardless of risk | Risk-based staffing; peer benchmarks |
| **Confuse env matrix with org** | Account diagram = operating model | Split cloud design from people design |

## Scaling security + engineering together

1. **Automate** repeatable assurance (SCA, IaC scan, policy-as-code)
2. **Template** golden paths so embed teams are not bespoke every time
3. **Measure interfaces** before adding headcount
4. **Invest in chapters** when duplication of training/playbooks exceeds cost of central craft team
5. **Executive alignment** — CTO/CISO joint SteerCo for persistent conflicts (`chief-information-security-officer`, `vp-of-infrastructure`)

## Consolidation triggers (examples)

- Same incident fought by two IR teams
- Audit finding repeats across BUs with different interpretations
- Platform team &lt; 3 FTE supporting &gt; 150 engineers without self-service
- Critical vuln SLA missed due to routing, not technical difficulty

## De-scaling / simplification

Sometimes the fix is **fewer** forums and **clearer** lines:

- Merge overlapping councils
- Sunset committees with no decisions in two quarters
- Replace status meetings with written async + decision log

## Assessment rubric (quick)

Score 1–5 per dimension; ≤3 warrants action plan:

| Dimension | Question |
|---|---|
| Clarity | Can a new hire name who decides X? |
| Speed | Handoff wait vs work time for typical security item? |
| Duplication | Same work in two teams? |
| Standards | Are paved roads used without heroic exceptions? |
| Incidents | IR command unambiguous? |
| Audit | Evidence owners stable year over year? |
