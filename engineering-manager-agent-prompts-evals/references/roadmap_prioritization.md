# Roadmap and Prioritization

## Backlog item template

| Field | Example |
|---|---|
| **Agent / surface** | Support copilot v2 |
| **Outcome** | Reduce wrong-tool rate 50% |
| **Deliverable** | 40 new goldens + tool schema rewrite |
| **Risk tier** | Tier 2 |
| **Deps** | Platform trace API v2 |

## Priority buckets

| Bucket | Examples |
|---|---|
| **P0 — production regression** | Pass rate drop on safety/refusal slice |
| **P1 — launch blocker** | GA requires green golden set |
| **P2 — coverage** | New tool, new locale, new intent |
| **P3 — efficiency** | Harness speed, judge cost reduction |

Reserve **25–30%** capacity for P0/P1 buffer and harness maintenance.

## Trade-offs (manager decisions)

| Tension | Resolution framework |
|---|---|
| New agent vs eval debt | No new agent without minimum golden coverage bar |
| More tools vs eval combinatorics | Cap tools per agent; platform review |
| Judge quality vs cost | Calibrate quarterly; sample in prod |
| Speed vs human labels | SME budget upfront for Tier 1 |

## Metrics for roadmap reviews

- Pass rate trend by **tag** (not aggregate only)
- **Time-to-add-golden** after production failure
- Open waiver count
- Judge–human agreement drift

## Escalation

Escalate when: launch date conflicts with eval gate; risk refuses waiver without staffing; platform blocks harness access.

Bring options: reduce scope, delay GA, temporary human review layer.
