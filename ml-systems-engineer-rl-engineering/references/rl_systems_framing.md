# RL systems framing

## Table of contents

1. [Problem shape](#problem-shape)
2. [On-policy vs off-policy](#on-policy-vs-off-policy)
3. [Scale dimensions](#scale-dimensions)
4. [Non-goals](#non-goals)

## Problem shape

Capture before building infra:

| Question | Drives design |
|---|---|
| Discrete vs continuous actions? | Env batching, policy head export |
| Single-agent vs multi-agent? | Shared replay, comms bus |
| Sim vs real robot/API? | Latency, safety interlocks |
| Episode length distribution? | Buffer size, timeout handling |
| Partial observability? | Frame stacking, RNN state in checkpoint |

Document **observation normalization** — running stats owned by trainer or env.

## On-policy vs off-policy

| Pattern | Infra emphasis |
|---|---|
| On-policy (PPO, A2C) | Fresh rollouts each epoch; many actors; tight sync |
| Off-policy (SAC, DQN) | Large replay; async actors; learner decoupled |
| Offline RL | Fixed dataset pipeline; no live env required |

Wrong pattern → wasted GPUs (replay-bound vs rollout-bound).

## Scale dimensions

Estimate:

- **Steps/sec** target across fleet
- **Actor count** vs **learner GPUs**
- **Observation size** × batch → network bandwidth
- **Checkpoint frequency** vs storage cost
- **Preemption rate** on spot nodes → resume SLA

## Non-goals

Route elsewhere:

- Reward function **design** (research/product) — systems expose hooks only
- **Hyperparameter search** orchestration — may share platform but not core RL path
- **Supervised** pretraining — separate pipeline unless warm-start checkpoint
