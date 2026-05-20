# Training platform architecture

## Table of contents

1. [Topology patterns](#topology-patterns)
2. [Components](#components)
3. [Scheduling](#scheduling)
4. [Networking](#networking)

## Topology patterns

| Pattern | Description |
|---|---|
| Single-process | Dev/debug only |
| Driver + remote actors | Production default |
| Learner pool + actor fleet | Scale collectors |
| Env-as-a-service | Remote sim farm |

```
Actors (CPU/GPU-light) → Trajectory stream → Learner (GPU-heavy)
                              ↓
                         Checkpoint store
```

## Components

| Component | Responsibility |
|---|---|
| Controller | Job lifecycle, config, global step |
| Rollout workers | `env.step`, policy inference (often CPU) |
| Learner | Gradient updates, replay sample |
| Parameter broadcast | Weights to actors (interval or async) |
| Metric aggregator | Reduce logs across workers |

Use frameworks (Ray RLlib, CleanRL distributed, custom) but document **ownership** of each box.

## Scheduling

- **GPU affinity** — learners on GPU nodes; actors on CPU unless inference-heavy
- **Gang scheduling** — avoid partial allocation leaving job stuck
- **Spot/preemptible** — checkpoint every N minutes; graceful SIGTERM handler
- **Queue fairness** — team quotas on GPU pool

Coordinate cluster primitives with `cluster-deployment-engineer`.

## Networking

- Compress observations if wide (JPEG, fp16, zstd)
- gRPC/IPC for local; Redis/pub-sub only if measured need
- Watch **NCCL** for learner multi-GPU vs actor traffic on same NIC
- Set timeouts on stale actors — do not block learner indefinitely
