# Team Metrics and Accountability

## Scorecard

| Metric | Notes |
|---|---|
| **Overall golden pass rate** | Trend; not sole metric |
| **Pass rate by tag** | safety, tools, refusal, domain |
| **Coverage** | % prod failure modes with goldens |
| **Time-to-golden** | Hours/days from incident → case |
| **Flaky case rate** | Quarantined / total |
| **Judge–human agreement** | Calibration health |
| **Prompt releases with full gate** | % without waiver |
| **P1 prompt incidents** | Count and recurrence |

## Targets (set per org)

- No drop on **safety/refusal** slice without waiver
- **Time-to-golden** < 5 business days for Tier 1–2
- **Eval debt** burn: N cases/quarter per agent

## Accountability

| Event | EM action |
|---|---|
| Pass rate drop on merge | Block release; root cause |
| Repeat wrong-tool class | Platform or prompt initiative |
| Waiver spike | Review with risk; staffing plan |
| Judge drift | Pause judge-gated deploys; recalibrate |

## Reporting

**Weekly:** slice heatmap, blockers, waivers open

**Quarterly:** coverage map per agent, harness investment ROI (fewer incidents, faster launches)

## vs `ai-lead-ops`

Ops owns SLOs and incidents; this function owns **preventive eval quality** and **prompt change discipline**.
