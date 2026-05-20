# Audience profiles and register

## Table of contents

1. [Register dimensions](#register-dimensions)
2. [Audience profiles](#audience-profiles)
3. [Depth and format defaults](#depth-and-format-defaults)
4. [Sensitivity handling](#sensitivity-handling)

## Register dimensions

Tune each output on four axes:

| Dimension | Question |
|---|---|
| **Depth** | How much detail can they use in one sitting? |
| **Register** | Formal vs conversational; passive vs direct |
| **Evidence** | What proof do they require (data, policy cite, test result)? |
| **Decision rights** | Inform, recommend, approve, or execute? |

## Audience profiles

| Audience | Cares about | Typical vocabulary | Avoid |
|---|---|---|---|
| **Engineering** | Feasibility, dependencies, SLOs, rollback, security | APIs, latency, idempotency, blast radius | Unbounded "ASAP"; vague "alignment" |
| **Product** | Outcomes, scope, users, roadmap trade-offs | Jobs, metrics, experiments, guardrails | Implementation detail without user impact |
| **Finance** | Cash, margin, forecast variance, capitalization | Run rate, cohort, unit economics, bridge | Undefined metrics; engineering timelines without confidence bands |
| **Legal** | Obligations, liability, enforceability, notice | Shall/may, indemnity, data processing | Technical certainty on unsettled interpretation |
| **Compliance** | Controls, evidence, regulatory mapping | Control objective, attestation, scope | "We'll be compliant" without control reference |
| **Sales** | Deal impact, customer commitments, competitive | SLA, packaging, objection handling | Internal-only incident detail without talk track |
| **Operations** | Throughput, handoffs, runbooks, staffing | SLA, queue, runbook, escalation tier | Strategy without operational next step |
| **Actuarial** | Assumptions, uncertainty, model limitations | Triangle, tail, credibility, sensitivity | Point estimates without ranges or methods |
| **Executive** | Decision, risk, resource, timing | Trade-off, bet, exposure, milestone | Deep implementation unless decision-critical |

## Depth and format defaults

| Audience | Default depth | Preferred structure |
|---|---|---|
| Executive | ½–1 page | Answer → impact → options → ask |
| Finance | 1–2 pages + tables | Metric bridge; assumptions explicit |
| Engineering | Full context + diagrams | Problem → constraints → design → test plan |
| Legal / compliance | Issue list + citations | Obligation → current state → gap → owner |
| Sales / ops | Playbook bullets | What changed → what to say/do → escalation |

## Sensitivity handling

| Topic | Guidance |
|---|---|
| Personnel | No names in exec summaries unless necessary; route HR-sensitive content |
| Security incidents | Facts from incident commander; no speculation; separate customer vs internal |
| Material financial figures | Do not round without basis; flag preliminary vs audited |
| Regulatory | Distinguish **legal interpretation** from **engineering control**; tag review |
| M&A / litigation | Minimal distribution; mark confidential; defer to `commercial-counsel` |

When two audiences conflict (e.g., speed vs compliance), state the **trade-off explicitly** rather than smoothing over it.
