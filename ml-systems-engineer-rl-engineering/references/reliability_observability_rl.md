# Reliability and observability (RL training)

## Table of contents

1. [Health signals](#health-signals)
2. [Stability incidents](#stability-incidents)
3. [Debugging playbook](#debugging-playbook)
4. [Cost controls](#cost-controls)

## Health signals

| Signal | Alert when |
|---|---|
| `steps_per_sec` drop | Actor fleet unhealthy |
| NaN in loss | Immediate stop |
| KL spike | Policy collapse risk |
| Actor heartbeat missing | Stuck or OOM |
| Checkpoint age | Stale — preempt risk |
| GPU mem | Leak across restarts |

Dashboard: one pane training, one pane infra.

## Stability incidents

| Incident | Mitigation |
|---|---|
| Reward explosion | Clip rewards; check env bug |
| All actors died | Restart job from checkpoint |
| Learner OOM | Reduce batch; gradient accumulation |
| Weight stale on actors | Shorten broadcast interval |
| Disk full on replay | Lower capacity; external store |

Post-incident: save **last good checkpoint** before corrupt state.

## Debugging playbook

1. Reproduce on **single actor + single learner** locally
2. Log one full episode with `info` reward terms
3. Compare policy weights hash actor vs learner
4. Plot reward vs global step for subset of seeds
5. Verify env version in container image digest

Escalate algorithm change to research; fix infra desync here.

## Cost controls

- Autoscale actors down after target steps
- Kill jobs over GPU-hour budget without checkpoint progress
- Use spot with aggressive checkpointing
- Profile sim — often cheaper to optimize env than add GPUs

Align long-range GPU needs with `data-center-compute-supply-efficiency` when capacity-bound.
