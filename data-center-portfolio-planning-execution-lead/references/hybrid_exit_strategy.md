# Hybrid Cloud and Site Exit

## Portfolio placement rules

Document **default** and **exceptions**:

| Workload class | Default placement | Exception criteria |
|---|---|---|
| Latency-sensitive prod | On-prem / edge near users | |
| GPU training burst | Cloud or dedicated hall | Contracted capacity |
| Regulated data | Sovereign region site | Legal list |
| Dev/test | Cloud or low-tier site | Cost cap |

Rules prevent **every team** negotiating ad hoc colo vs cloud.

## Cloud burst vs committed metal

| Factor | Favor cloud burst | Favor DC commit |
|---|---|---|
| Duration | <12 mo peak | Steady 3+ yr load |
| Unit economics | Spot/preempt OK | GPU $/hr below cloud |
| Lead time | Need capacity now | Can wait build |
| Data gravity | Egress cost low | Large datasets on-prem |

Portfolio lead arbitrates **enterprise** view; `infrastructure-engineer` implements hybrid technical design.

## Site exit or consolidation

1. **Trigger** — lease end, TCO, utilization, disaster risk
2. **Inventory** — workloads, dependencies, data residency
3. **Target** — other site or cloud
4. **Sequence** — migrate, decomm, reclaim contracts
5. **Financial** — termination fees, write-offs

Coordinate decomm efficiency with `data-center-compute-supply-efficiency`.

## Colo contract portfolio

| Track | Review date |
|---|---|
| Renewal / renegotiate | 12–18 mo before |
| Right-size committed kW | Annual |
| Multi-site vendor concentration | Risk review |

## M&A (light touch)

- Capacity and contract liabilities in target DC footprint
- Integration into portfolio roadmap—not full due diligence alone
